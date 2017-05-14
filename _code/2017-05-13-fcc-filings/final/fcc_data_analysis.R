# Load things we will use later
library(scales)
library(dplyr)
library(ggplot2)
library(lubridate)
library(ggthemes)
library(knitr)
library(stringr)
library(tidyr)

# Setting for later
options(scipen=999)

# Read in the data 
d <- read.csv("raw_data_pub_api_sorted_5_14_2AM.csv", stringsAsFactors = F)

# Clean up dates 
d$clean_date_submission <- as.POSIXct(strptime(as.character(d$date_submission), "%Y-%m-%dT%H:%M:%OSZ", tz = "UTC"))
d$clean_date_disseminated <- as.POSIXct(strptime(as.character(d$date_disseminated), "%Y-%m-%dT%H:%M:%OSZ", tz = "UTC"))
d$clean_date_received <- as.POSIXct(strptime(as.character(d$date_received), "%Y-%m-%dT%H:%M:%OSZ", tz = "UTC"))

# Aggregations using date of submission
# Other date fields don't seem to make sense 
d %>% 
  mutate(
    round_hr_utc = ceiling_date(clean_date_submission, unit = "hour") 
    , round_hr_est = with_tz(round_hr_utc, tzone="US/Eastern")
  ) -> d

# Run a few data checks 
d %>% is.na() %>% colSums()

# Any duplicated records? 
d %>% 
  group_by(id_submission) %>% 
  summarise(n = n()) %>% 
  arrange(desc(n)) %>% head(20) -> check

nrow(unique(d %>% select(-X))) #No duplicates

## COUNTS & AGGREGATIONS ANALYSIS 

d %>% 
  group_by(round_hr_est) %>% 
  summarise(n_filings = n()) %>% 
  mutate(cum = cumsum(n_filings), 
         cum_thous = cum/1000, 
         n_filings_thous = n_filings/1000) -> cumulative_filings

# Cumulative over time
cumulative_filings %>% 
  filter(round_hr_est >= '2017-05-06') %>%  
  ggplot(aes(x=round_hr_est, y = cum_thous)) + 
  geom_line(size = 1.5, color = ggthemes_data$fivethirtyeight["blue"]) +
  xlab("Date & Time (EST)") + 
  ylab("Cumulative count of filings\n(in thousands)") + 
  geom_vline(aes(xintercept = as.numeric(as.POSIXct(strptime("2017-05-08 00:00:00", "%Y-%m-%d %H:%M:%S")))), linetype = 'dashed', size = 1.3, color = ggthemes_data$fivethirtyeight["green"]) + 
  scale_y_continuous(breaks = c(0,200,400,600,800,1000)) +
  ggtitle("Volume of Net Neutrality Filings Greatly Increased\nAfter Last Week Tonight Aired") +
  labs(subtitle = "Cumulative count of public filings on FCC proceeding 17-108 over time") + 
  theme_fivethirtyeight() + 
  theme(legend.position = 'right', 
        title = element_text(size=22),
        axis.title = element_text(size=20,hjust=.5,vjust=.5,face="plain"), 
        axis.text = element_text(size=15,hjust=.5,vjust=.5,face="plain"))

# Hourly rates 
cumulative_filings %>% 
  filter(round_hr_est >= '2017-05-06') %>%
  ggplot(aes(x=round_hr_est, y=n_filings_thous)) + 
  geom_bar(stat='identity',fill = ggthemes_data$fivethirtyeight["blue"]) + 
  #geom_line(size = 1.5, color = ggthemes_data$fivethirtyeight["blue"]) + 
  xlab("Date & Time (EST)") + 
  ylab("Count of filings per hour\n(in thousands)") + 
  geom_vline(aes(xintercept = as.numeric(as.POSIXct(strptime("2017-05-08 00:00:00", "%Y-%m-%d %H:%M:%S")))), linetype = 'dashed', size = 1.3, color = ggthemes_data$fivethirtyeight["green"]) + 
  ggtitle("FCC Filings Accumulated at a Rapid Rate\nDespite Periods of Downtime") +
  labs(subtitle = "Hourly count of public filings on FCC proceeding 17-108 over time") + 
  theme_fivethirtyeight() + 
  theme(legend.position = 'right', 
        title = element_text(size=25),
        axis.title = element_text(size=20,hjust=.5,vjust=.5,face="plain"), 
        axis.text = element_text(size=15,hjust=.5,vjust=.5,face="plain"))

Clean_String <- function(string){
  # Function adapted from http://www.mjdenny.com/Text_Processing_In_R.html 
  # Simple function to clean text, with some tweaks specific to this case. 
  
  # Lowercase
  temp <- tolower(string)
  
  # Replace "II" with "2" for title 2/II consistency
  temp <- stringr::str_replace_all(temp,"ii", "2")
  
  # Collapse apostrophes to nothing (handles ISPs vs. ISP's)
  temp <- stringr::str_replace_all(temp,"[']", "")
  
  # Remove everything else that is not a number, letter or whitespace
  temp <- stringr::str_replace_all(temp,"[^0-9a-zA-Z\\s]", " ")
  
  # Shrink down to just one white space
  temp <- stringr::str_replace_all(temp,"[\\s]+", " ")
  
  # Trim whitespace
  temp <- trimws(temp, which = 'both')
  
  return(temp)
}

# Apply function to text 
vf_clean <- Vectorize(Clean_String)
d %>% 
  mutate(clean_text = Clean_String(text_data)) -> d

# Find most frequent comments
d %>% 
  group_by(clean_text) %>% 
  summarise(n=n()) %>% 
  ungroup() %>% 
  mutate(share=100*(n/sum(n))) %>% 
  arrange(desc(n)) %>% head(50) -> top_comments_df

top_comments_df %>% 
  mutate(rnk = row_number()) %>% 
  select(rnk, clean_text, n, share) %>% 
  head(10) %>% 
  kable(col.names = c("Rank", "Statement", "Count", "% of Total"), digits = 1, align = c('c', 'l', 'c', 'c'))

d %>% 
  mutate(
    is_spam = ifelse(grepl("unprecedented regulatory power the obama administration imposed", clean_text), 'Spam', 'Not Spam')
  ) %>% 
  group_by(is_spam, round_hr_est) %>% 
  summarise(n_filings = n()) -> filings_per_hour_spam_vs_rest

# Colors 
vals <- c("#9370DB", "#F67670")
names(vals) <- c("Spam", "Not Spam")

filings_per_hour_spam_vs_rest %>% 
  mutate(n_filings_thous = n_filings/1000) %>% 
  filter(round_hr_est >= '2017-05-07 12:00:00') %>% 
  ggplot(aes(x=round_hr_est, y=n_filings_thous)) + 
  geom_bar(stat='identity',aes(fill = is_spam)) + 
  scale_fill_manual(values = vals) + 
  theme_fivethirtyeight() + 
  #geom_line(size = 1.5, color = ggthemes_data$fivethirtyeight["blue"]) + 
  xlab("Date & Time (EST)") + 
  ylab("Count of filings per hour\n(in thousands)") + 
  geom_vline(aes(xintercept = as.numeric(as.POSIXct(strptime("2017-05-08 00:00:00", "%Y-%m-%d %H:%M:%S")))), linetype = 'dashed', size = 1.3, color = ggthemes_data$fivethirtyeight["green"]) + 
  ggtitle("Anti-Net Neutrality Spam Was\nSubmitted Thousands of Times") + 
  labs(subtitle="Hourly count of public filings on FCC proceeding 17-108 over time") +
  facet_grid(is_spam~.) + 
  theme(legend.position = 'right', 
        title = element_text(size=25),
        axis.title = element_text(size=20,hjust=.5,vjust=.5,face="plain"), 
        axis.text = element_text(size=15,hjust=.5,vjust=.5,face="plain")) + 
  theme(legend.position="hide") + 
  theme(strip.background = element_blank(),
        strip.text.y = element_blank())

### SPAM <> PWNED EMAILS ANALYSIS 

set.seed(117) # reproducibility

# Dump a random sample of spam
d %>% 
  filter(grepl("unprecedented regulatory power the obama administration imposed", clean_text)) %>% 
  sample_n(1000) %>% # random sample 
  select(contact_email) %>% 
  write.csv(file = "spam_email_sample.csv", row.names = F)

# Emails were sent to API with python (see pwned_emails.py)
# and results were dumped to pwned_email_results.csv

# Read back in results and display 
pwnd_results <- read.csv('pwned_email_results.csv')
pwnd_results %>% 
  select(in_RCM, in_SpecialK, in_any_dump) %>% 
  gather(var, value) %>% 
  mutate(var = factor(var, labels = c("In Any Breach", "In RCM Breach", "In SpecialK Breach"))) %>% 
  group_by(var) %>% 
  summarise(share = mean(value)) %>% 
  ggplot(aes(x=reorder(var,share), y = share)) + 
  geom_bar(stat='identity', fill = ggthemes_data$fivethirtyeight["blue"]) + 
  geom_text(aes(label = paste(round(100*share,2), '%', sep = ''), y = share-0.05), color = 'white', size = 9, face = 'bold') + 
  xlab("") + 
  ylab("Share of spam emails included") + 
  scale_y_continuous(labels = percent) + 
  coord_flip() + 
  ggtitle("Most Spam Emails Appear \nIn At Least One Data Breach") +
  theme_fivethirtyeight() + 
  theme(legend.position = 'right', 
        title = element_text(size=25),
        axis.title = element_text(size=20,hjust=.5,vjust=.5,face="plain"), 
        axis.text = element_text(size=15,hjust=.5,vjust=.5,face="plain")) + theme(legend.position="bottom")

### ANALYSIS OF NET NEUTRALITY SUPPORT 

# Dump a random sample of non-spam comments
d %>% 
  filter(!grepl("unprecedented regulatory power the obama administration imposed", clean_text)) %>% 
  sample_n(200) %>% # random sample
  select(contact_email, text_data) %>% 
  write.csv(file = "sample_non_spam.csv", row.names = F)

# Data was hand-tagged in google docs and then 
# dumped to aggregated_support.csv
support_results_df <- read.csv('aggregated_support.csv')

# Read in data and display it
support_results_df %>% 
  filter(Category != 'Total') %>% 
  mutate(frac_share = Share/100, 
         se = sqrt(frac_share*(1-frac_share)/Count), 
         ci = 1.96*se, 
         upper = frac_share + ci,
         lower = ifelse(frac_share - ci < 0 , 0, frac_share - ci )) %>% 
  ggplot(aes(x=reorder(Category,frac_share), y = frac_share)) + 
  geom_bar(stat='identity', fill = ggthemes_data$fivethirtyeight["blue"]) + 
  geom_errorbar(aes(ymin=lower, ymax=upper), width = 0.2) + 
  xlab("Filer Position on Net Neutrality") + 
  ylab("Share of Filings (%)") + 
  scale_y_continuous(labels = percent) + 
  coord_flip() + 
  ggtitle("Non-spam Filings Overwhelmingly\nSupport Net Neutrality") +
  labs(subtitle = "Distribution of non-spam filings by position on Net Neutrality (N=200)") + 
  theme_fivethirtyeight() + 
  theme(legend.position = 'right', 
        title = element_text(size=25),
        axis.title = element_text(size=20,hjust=.5,vjust=.5,face="plain"), 
        axis.text = element_text(size=15,hjust=.5,vjust=.5,face="plain")) + theme(legend.position="bottom")


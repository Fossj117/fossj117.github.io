setwd('~/Files/research/fcc_filings/')

df <- read.csv('fcc_filings.csv', stringsAsFactors = F)

library(dplyr)
library(ggplot2)
library(plotly)

df$clean_date <- as.POSIXct(strptime(as.character(df$date_submission), "%Y-%m-%dT%H:%M:%OSZ"))

options(scipen=999)

df %>% 
  mutate(round_hour = as.POSIXct(round(clean_date, units = "hours"))) %>%
  group_by(round_hour) %>% 
  summarise(n_filings = n()) %>% 
  mutate(cum = cumsum(n_filings), 
         cum_thous = cum/1000) %>%
  filter(round_hour >= '2017-05-06') -> res 
  
View(res)

res %>% ggplot(aes(x=round_hour, y = cum_thous)) + 
  geom_line(size = 1.5, color = ggthemes_data$fivethirtyeight["blue"]) + 
  xlab("Time") + 
  ylab("Cumulative count of FCC filings (in thousands)") + 
  geom_vline(aes(xintercept = as.numeric(as.POSIXct(strptime("2017-05-07 23:30:00", "%Y-%m-%d %H:%M:%S")))), linetype = 'dashed', size = 1.3, color = ggthemes_data$fivethirtyeight["green"]) + 
  ggtitle("Cumulative Count of Filings on \nFCC Net Neutrality Proceeding (17-108)") +
  theme_fivethirtyeight() + 
  theme(legend.position = 'right', 
        title = element_text(size=25),
        axis.title = element_text(size=20,hjust=.5,vjust=.5,face="plain"), 
        axis.text = element_text(size=15,hjust=.5,vjust=.5,face="plain"))

g %>% ggplotly()

df %>% 
  mutate(day = as.Date(date_submission)) %>% 
  group_by(day) %>% 
  summarise(n_filings = n()) %>% 
  ggplot(aes(x=day, y = n_filings)) + geom_bar(stat = 'identity')
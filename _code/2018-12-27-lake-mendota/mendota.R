library(tidyverse)
library(ggthemes)
library(stargazer)
library(viridis)

setwd("./Files/research/lake_mendota/")

# Read in the Data
df_mendota <- read.csv("Lake_Mendota_Ice.csv", stringsAsFactors = F)

## Data Preparation 
START_YEAR_MOS <- c("Nov", "Dec")

df_mendota %>% 
  separate(CLOSED, into = c("Closed_Day", "Closed_Month"), sep = " ", remove = F) %>% 
  separate(OPENED, into = c("Opened_Day", "Opened_Month"), sep = " ", remove = F) %>% 
  mutate(
    Closed_Year = ifelse(Closed_Month %in% START_YEAR_MOS, START.YEAR, END.YEAR),
    Opened_Year = ifelse(Opened_Month %in% START_YEAR_MOS, START.YEAR, END.YEAR), 
    Opened_Date = dmy(paste(Opened_Day, Opened_Month, Opened_Year, sep = " ")), 
    Closed_Date = dmy(paste(Closed_Day, Closed_Month, Closed_Year, sep = " ")), 
    # Standardized dates
    Closed_Year_Stand = ifelse(Closed_Month %in% START_YEAR_MOS, 2018, 2019),
    Opened_Year_Stand = ifelse(Opened_Month %in% START_YEAR_MOS, 2018, 2019), 
    Opened_Date_Stand = dmy(paste(Opened_Day, Opened_Month, Opened_Year_Stand, sep = " ")), 
    Closed_Date_Stand = dmy(paste(Closed_Day, Closed_Month, Closed_Year_Stand, sep = " ")), 
    DAYS = as.integer(DAYS) # '-' records become NAs
  ) -> df_mendota 

df_mendota %>% 
  group_by(START.YEAR, END.YEAR) %>% 
  summarise(
    DAYS=max(DAYS, na.rm = T)
  , Opened_Date = max(Opened_Date, na.rm = T)
  , Closed_Date = min(Closed_Date, na.rm = T)
  , Opened_Date_Stand = max(Opened_Date_Stand, na.rm = T)
  , Closed_Date_Stand = min(Closed_Date_Stand, na.rm = T)
  ) %>% 
  mutate(DAYS_manual = as.numeric(Opened_Date-Closed_Date), 
         Season_Start_Date_Stand = dmy('01 Nov 2018'), 
         Opened_Day_of_Season = as.numeric(Opened_Date_Stand-Season_Start_Date_Stand), 
         Closed_Day_of_Season = as.numeric(Closed_Date_Stand-Season_Start_Date_Stand), 
         t=START.YEAR-1855) %>% 
  ungroup() -> df_mendota_clean

# Plotting 
my_theme <- theme_base() + 
  theme(legend.position = 'none', 
    legend.title = element_blank(), 
    title = element_text(size=12),
    axis.title = element_text(size=10), 
    axis.text = element_text(size=10,face="plain"), 
    strip.text = element_text(size=10),
    panel.border=element_blank())

vir_cols <- viridis(10)

# Plot 1 
df_mendota_clean %>% 
  ggplot(aes(x=START.YEAR, y  = DAYS_manual)) + 
  geom_point(colour = vir_cols[4], alpha=0.7, size=2.5) + 
  geom_smooth(method='lm', se=F, colour = vir_cols[4], size=1.5, alpha=0.8) + 
  ylab("Days of Ice in Season") + 
  xlab("Year of Season") + 
  ggtitle("Lake Mendota Days of Ice Cover By Yearly Season") + 
  my_theme -> p1

# Plot 2 
df_mendota_clean %>% 
  select(
    START.YEAR, 
    Closed_Date_Stand, 
    Opened_Date_Stand
  ) %>% 
  gather(var, val, 2:3) %>% 
  mutate(var = factor(var, labels = c("Ice On", "Ice Off"))) %>% 
  ggplot(aes(x=START.YEAR, y = val, colour = var)) + 
  geom_point(alpha=0.8, size=2.5) +
  geom_smooth(method='lm', se = F,size=1.5) + 
  geom_ribbon(aes(x=START.YEAR, ymin=Closed_Date_Stand, ymax=Opened_Date_Stand), data = df_mendota_clean, colour = NA, fill=vir_cols[4], alpha=0.2, inherit.aes = F) + 
  xlab("Year of Season") + 
  ylab("Date of Ice On / Ice Off in Season") + 
  my_theme + 
  scale_colour_manual(values=c(vir_cols[2], vir_cols[8])) + 
  ggtitle("Lake Mendota Date of Ice On and Ice Off By Yearly Season") -> p2

# Combine Plots
gp1<- ggplot_gtable(ggplot_build(p1))
gp2<- ggplot_gtable(ggplot_build(p2))
maxWidth = unit.pmax(gp1$widths[2:3], gp2$widths[2:3])
gp1$widths[2:3] <- maxWidth
gp2$widths[2:3] <- maxWidth
grid.arrange(gp2, gp1)

# Analysis
mod_days <- lm(formula = DAYS_manual ~ t, data=df_mendota_clean)
open_mod <- lm(formula = Opened_Day_of_Season ~ t, data=df_mendota_clean)
close_mod <- lm(formula = Closed_Day_of_Season ~ t, data=df_mendota_clean)

stargazer(mod_days,open_mod, close_mod, 
          type = 'html', omit.stat = "adj.rsq", 
          dep.var.labels = c("Days of Ice Cover", "Ice Off Day of Season", "Ice On Day of Season"), 
          covariate.labels = c("Trend", "Constant"), 
          report = "vc*s")


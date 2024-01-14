library(lubridate)

setwd("~/Documents/Research/fossj117.github.io/_posts/how_many_smart_contracts/")

df <- read.csv("daily_contract_creation_count_eth_flipside.csv")

df %>% 
  filter(!is.na(N_CONTRACTS_CREATED)) %>% 
  mutate(DS = as.Date(DS)) %>% 
  ggplot(aes(x=DS, y = N_CONTRACTS_CREATED)) + geom_line() + theme_bw() + 
  xlab("Date") + 
  ylab("Number of Successful Contract Creations") + 
  ggtitle("Daily Count of Successful Contract Creation Events on Ethereum", subtitle = "Data from ethereum.core.fact_traces on Flipside Crypto")
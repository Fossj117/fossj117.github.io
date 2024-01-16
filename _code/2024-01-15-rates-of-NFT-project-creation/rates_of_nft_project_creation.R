library(lubridate)
library(shroomDK)

setwd("~/Documents/Research/fossj117.github.io/_code/2024-01-15-rates-of-NFT-project-creation/")

df <- read.csv("daily_count_of_nft_projects_with_first_mint_event.csv") %>% filter(!is.na(N_PROJECTS_WITH_FIRST_MINT)) # filters out a fake row
sum(df$N_PROJECTS_WITH_FIRST_MINT)

df %>% 
  mutate(
    DS = as.Date(DS)
  , DS_WEEK = floor_date(DS, "week")
  ) %>% 
  group_by(DS_WEEK) %>% 
  summarise(
    n_projects = sum(N_PROJECTS_WITH_FIRST_MINT)
  ) %>% 
  ggplot(aes(x=DS_WEEK, y = n_projects)) + geom_point(size=0.9) + 
  geom_line() + theme_bw() + 
  xlab("Date") + 
  ylab("Number of NFT Projects with First Mint Event (Weekly)") + 
  ggtitle("Weekly Count of Distinct NFT Projects with First Mint Event in Week", subtitle = "Data from Flipside Crypto")

df %>% 
  mutate(
    DS = as.Date(DS)
    , DS_WEEK = floor_date(DS, "week")
  ) %>% 
  ggplot(aes(x=DS, y = N_PROJECTS_WITH_FIRST_MINT)) + geom_point(size=0.5) + 
  geom_line(stat = 'identity') + theme_bw() + 
  xlab("Date") + 
    ylab("Number of NFT Projects with First Mint Event (Daily)") + 
    ggtitle("Daily Count of Distinct NFT Projects with First Mint Event", subtitle = "Data from Flipside Crypto")

# Query for creator level aggregation
query <- "
WITH mint_events AS (
  SELECT
    nft_address
  , MIN(block_timestamp) AS first_mint_timestamp
  FROM
    ethereum.nft.ez_nft_mints
  WHERE
    block_timestamp > '2021-01-01'
    AND block_timestamp < '2024-01-01'
  GROUP BY 
    nft_address
)
SELECT 
  creator_address_from_deploy_tx
, COUNT(DISTINCT nft_address) as n_projects_created 
, MIN(ts_first_mint) AS ts_first_mint
FROM(
  SELECT 
    me.nft_address
  , me.first_mint_timestamp AS ts_first_mint
  , fc.block_timestamp AS ts_contract_creation
  , fc.from_address AS creator_address_from_deploy_tx
  FROM 
    mint_events me
  LEFT JOIN 
    ethereum.core.dim_contracts dc ON me.nft_address = dc.address
  LEFT JOIN 
    ethereum.core.fact_transactions fc ON dc.created_tx_hash = fc.tx_hash
)
GROUP BY 1
ORDER BY 1
;
"

api_key = readLines("/Users/jfossett/Documents/Research/resale_royalties/progress/rates_of_new_project_creation/api_key.txt") # always gitignore your API keys!
query = query %>% paste(collapse = " ")

df_creator_level <- auto_paginate_query(query, api_key = api_key, page_size = 20000, page_count = NULL)

summary(df_creator_level$n_projects_created)

df_creator_level %>% 
  mutate(log_projects = log(n_projects_created)) %>% 
  ggplot(aes(x=log_projects)) + geom_histogram() + theme_bw() + xlab("ln(Num. NFT projects created)") + ylab("Count of NFT Project Creators") + ggtitle("Distribution of Number of NFT Projects Created per Creator", subtitle = "Natural Log Scale; Data from Flipside Crypto")

df_creator_level %>% 
  mutate(creator_w_link = paste("[",creator_address_from_deploy_tx, "](http://opensea.io/", creator_address_from_deploy_tx,")", sep="")) %>% 
  select(creator_w_link, n_projects_created) %>% 
  arrange(desc(n_projects_created)) %>% head(10) %>% kable(col.names = c("Address", "Num Projects"))

df_creator_level %>% 
  filter(n_projects_created == 1) %>% 
  sample_n(5) %>% 
  mutate(creator_w_link = paste("[",creator_address_from_deploy_tx, "](http://opensea.io/", creator_address_from_deploy_tx,")", sep="")) %>% 
  select(creator_w_link, n_projects_created) %>% 
  arrange(desc(n_projects_created)) %>% head(10) %>% kable(col.names = c("Address", "Num Projects"))

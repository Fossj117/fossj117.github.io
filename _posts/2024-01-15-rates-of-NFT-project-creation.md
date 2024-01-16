---
layout: post
title: "Estimating Rates of NFT Project Creation per Creator"
date: 2024-01-15
latex: true
mathjax: true
comments: true
tag: ["web3"]
---

In this post, I will build on my [previous post](https://jeffreyfossett.com/2024/01/14/who-created-this-contract.html) about identifying the EOA creator of an NFT project. The questions that I would now like to answer are: 

1. **What is the distribution of NFT projects (and assets) created per creator?** (on Ethereum)
2. **What share of NFT creators create more than one project?** (on Ethereum)

Where "creator" will be defined at the *address* level[^1]. For this analysis, I will work with the [`ez_nft_mints`](https://flipsidecrypto.github.io/ethereum-models/#!/model/model.ethereum_models.nft__ez_nft_mints) table maintained by Flipside, which "contains NFT mint events on the Ethereum blockchain". I note that minting is not identical to creating a contract; however, (1) I do not see a way to readily pick out the universe of NFT contracts on Flipside (except via the NFT minting/transfer/sales) tables[^2], and (2) first minting is arguably a more meaningful event for defining project creation anyhow. 

With this in mind, to answer question (1) above, let's proceed in the following way:

1. Using `ez_nft_mints`, collect all projects with at least one mint event (over a period of time). 
2. For each project, find the timestamp (`block_timestamp`) of the *first* minting event for that project (over some period). 
3. Identify the EOA creator of the project in the manner described in my [previous post](https://jeffreyfossett.com/2024/01/14/who-created-this-contract.html), by identifying the creator as the EOA that initiated the transaction that created the NFT project's contract. 

Here is a base Flipside query implementing this logic: 

{% highlight sql %}
WITH mint_events AS (
  SELECT
    nft_address
  , MIN(block_timestamp) AS first_mint_timestamp
  FROM
    ethereum.nft.ez_nft_mints
  WHERE
    block_timestamp > '2020-01-01'
    AND block_timestamp < '2024-01-01'
  GROUP BY 
    nft_address
), 
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
  ethereum.core.fact_transactions fc ON dc.created_tx_hash = fc.tx_hash;
{% endhighlight %}

We can add aggregations on top of this query to start answering some of our initial questions. Let's start with an even simpler question, asking how many distinct NFT projects are represented in this dataset, and how their first creation events are distributed over time. First, I find that there are `267,267` distinct NFT projects (contracts) represented in this dataset, which should include all Ethereum NFT projects with at least one mint event since Jan 1, 2020[^3]. Aggregating at the weekly level, here is the distribution of first mint events over time

<p>
  <img alt="Count" src="/figs/2024-01-15-rates-of-NFT-project-creation/weekly_count_of_distinct_NFT_projects_with_first_mint.png" width="100%">
</p>

Unsurprisingly, this mostly tracks the general rise and fall of the NFT space: slowly building through 2021, with the most activity in 2022, and then falling off in 2023. In peak weeks, there are on the order of 5,000 projects created[^4]. 

Next, we can consider the volume of project creations (first mint events) per creator (aggregation query in notes below). First, I find that there are `158,454` distinct creators for our `267,267` projects, which means that the average creator has created `1.69` projects over this period. The standard deviation is `2.73` projects, and the median is `1`. I find that `74.4%` of creators have created exactly one project, meaning that about `25.6%` create two or more, addressing question (2) above. As we might expect, the full distribution of projects created per creator is quite skewed; here it is on a natural log scale: 

<p>
  <img alt="Count" src="/figs/2024-01-15-rates-of-NFT-project-creation/nft_projects_created_per_creator.png" width="100%">
</p>

Here are the ten creator addresses that have created the most NFT contracts based on this methodology (with an attempt to link to their OpenSea page if it exists): 

|Address                                    | Num Projects|
|:------------------------------------------|------------:|
|[0xf8238a3dd9a67b8419412ede613a06d73ffc2d93](http://opensea.io/0xf8238a3dd9a67b8419412ede613a06d73ffc2d93)|          220|
|[0x47144372eb383466d18fc91db9cd0396aa6c87a4](http://opensea.io/0x47144372eb383466d18fc91db9cd0396aa6c87a4)|          218|
|[0x86bf3fe7d91a4d25282ae896452146d825c8ae23](http://opensea.io/0x86bf3fe7d91a4d25282ae896452146d825c8ae23)|          218|
|[0xee31de24bae8fd4e7c9fec8986d9953f39cd0a7d](http://opensea.io/0xee31de24bae8fd4e7c9fec8986d9953f39cd0a7d)|          204|
|[0xfbc3b76a206f03f1edbf411f280444cd3fd9c7c8](http://opensea.io/0xfbc3b76a206f03f1edbf411f280444cd3fd9c7c8)|          182|
|[0x90ea805e049c06bdf233c8d3754707f8b2054673](http://opensea.io/0x90ea805e049c06bdf233c8d3754707f8b2054673)|          154|
|[0x945dc4a0e40b4fb183389a0f3e6ebd100819e276](http://opensea.io/0x945dc4a0e40b4fb183389a0f3e6ebd100819e276)|          146|
|[0xfc5636fd6bf2a7b41456ffc8583100e10fea51ca](http://opensea.io/0xfc5636fd6bf2a7b41456ffc8583100e10fea51ca)|          144|
|[0xd973564a85ee827e7f983c9eaacadd6fa74b9da1](http://opensea.io/0xd973564a85ee827e7f983c9eaacadd6fa74b9da1)|          126|
|[0x33eb4e632383f5561e3146c52cc3535a099ad1b5](http://opensea.io/0x33eb4e632383f5561e3146c52cc3535a099ad1b5)|          120|

Where the linked OpenSea pages exist, these do seem to be high volume creators; however, there are a number of cases where no OpenSea page is found. I am not sure why this is. As far as I can tell from etherscan, these are legitimate wallet addresses which is good.  

One concerning record is [this](https://etherscan.io/address/0xfbc3b76a206f03f1edbf411f280444cd3fd9c7c8) one, which is called "Ethernity Deployer" and seems to [Etherenal Labs](https://ethernity.io/). I don't know much about this project; however, for my purposes the concern is that this does not seem to be an individual creator -- i.e. my method for identifying individual creators still has some limitations, which I will need to consider further. 

Finally, we can also try validating by looking at some more "typical" creators; here is a set of five random creators (with opensea links) that I find have created exactly one NFT project: 

|Address                                    | Num Projects|
|:------------------------------------------|------------:|
|[0x1228666a2136ddc6edfe2e5e2bcd01869788ed9b](http://opensea.io/0x1228666a2136ddc6edfe2e5e2bcd01869788ed9b)|            1|
|[0x1d9ec70282886c8a355e3ab60d96c0ab180a4085](http://opensea.io/0x1d9ec70282886c8a355e3ab60d96c0ab180a4085)|            1|
|[0xd2aeb1fae0f08a6b72fccb945a299c2a914062ab](http://opensea.io/0xd2aeb1fae0f08a6b72fccb945a299c2a914062ab)|            1|
|[0xf8bde4b9debcd406e13102f04ff4fb1f86759f72](http://opensea.io/0xf8bde4b9debcd406e13102f04ff4fb1f86759f72)|            1|
|[0xdcba90ca2e3a3bb1cf40a43b92f740c9c656666f](http://opensea.io/0xdcba90ca2e3a3bb1cf40a43b92f740c9c656666f)|            1|

Manually inspecting, these do seem to be creators who have created a single NFT project (or less) according to OpenSea. For some reason [this](https://opensea.io/0xf8bde4b9debcd406e13102f04ff4fb1f86759f72/created) account does not have any created assets on OpenSea; however, I am able to verify [via Etherscan](https://etherscan.io/address/0xf8bde4b9debcd406e13102f04ff4fb1f86759f72) that this address is indeed the creator of [this](https://etherscan.io/address/0x968188538e3ef6355eff3bdda3bb38367c399e42) NFT contract. I will need to dig in further on some of these edge cases, and also try to think more about how to validate my methdology[^5].

## Appendix

Here is the query for daily aggregations: 

{% highlight sql %}
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
  ts_first_mint::DATE as DS 
, COUNT(DISTINCT nft_address) as n_projects_with_first_mint
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
{% endhighlight %}

Here is the query for creator-level aggregation: 

{% highlight sql %}
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
{% endhighlight %}

Here is a daily version of the weekly chart from above.

<p>
  <img alt="Count" src="/figs/2024-01-15-rates-of-NFT-project-creation/daily_count_of_distinct_NFT_projects_with_first_mint.png" width="100%">
</p>

## Footnotes 

[^1]: We know individual creators can of course create more than one address, and so this is not perfect. However, it seems like the only real option for now.

[^2]: The `dim_nft_metadata` table says that it only includes information about "popular" collections, not the full universe of collections.

[^3]: I would love to have a sanity check of whether this number seems "reasonable"; however, I am having difficulty finding a good external reference for a stat similar to this one. Let me know if you have one. 

[^4]: At the daily level, I note that the volume of new projects is quite large right around 2023-01-01, with 2022-12-31, 2023-01-01 and 2023-01-02 all being among the four highest volume dates (see daily version of chart above). I was initially worried this might be a data anomaly (e.g. defaulting timestamps to `2023-01-01 00:00:00` or something similar); however, on further inspection, the high volume of creation on the surrounding dates suggests something else is going on; however, I don't know exactly what. If you do, please tell me! 

[^5]: All the code for this analysis can be found on my github [here](https://github.com/Fossj117/fossj117.github.io/tree/master/_code)
---
layout: post
title: "Determining the creator of an NFT contract on Ethereum using Flipside"
date: 2024-01-14
latex: true
mathjax: true
comments: true
tag: ["web3"]
---

In this post I want to determine the following: given the address of some NFT contract on Ethereum, how do I identify the externally owned account (EOA) that created this contract? I am working with data from [Flipside Crypto](https://flipsidecrypto.xyz/), so will be attempting to answer this question in that context. 

To answer the question, let's first collect a set of NFT contract addresses to attempt to link to creators. For a generic set, we can collect the set of NFT contracts with at least one "mint" event in the past month from the `ethereum.nft.ez_nft_mints` on Flipside (table docs [here](https://flipsidecrypto.github.io/ethereum-models/#!/model/model.ethereum_models.nft__ez_nft_mints)): 

{% highlight sql %}
SELECT 
    nft_address
FROM 
    ethereum.nft.ez_nft_mints
WHERE 
    block_timestamp::DATE > '2023-12-14'
    AND block_timestamp::DATE < '2024-01-14'
GROUP BY
    1; 
{% endhighlight %}

This turns out to be a set of 11,155 distinct NFT contracts. To link these to creator EOAs, one approach would be to use the `ethereum.core.dim_contracts` table in [in Flipside](https://flipsidecrypto.github.io/ethereum-models/#!/model/model.ethereum_models.core__dim_contracts). This table has a `creator_address` field that would seem to solve the problem. To examine, let's try merging with `dim_contracts` and looking at the distribution of NFT contracts created per creator. Here is the new query: 

{% highlight sql %}
SELECT 
    dc.creator_address 
,   COUNT(DISTINCT enm.nft_address) AS n_nft_contracts_created
FROM 
    ethereum.nft.ez_nft_mints enm
LEFT JOIN 
    ethereum.core.dim_contracts dc
ON 
    enm.nft_address = dc.address
WHERE 
    enm.block_timestamp::DATE > '2023-12-14'
    AND enm.block_timestamp::DATE < '2024-01-14'
GROUP BY
    1 
ORDER BY 
    2 DESC; 
{% endhighlight %}

First, I note that all 11,155 contracts are indeed linked to a `creator_address` here. There are a total of 4038 distinct creator addresses. Let's look at some of the most prolific contract creators. Here are the top 5 (with links to their etherscan pages): 

|Creator Address                            | Num Contracts Created|
|:------------------------------------------|---------------------:|
|[0x000000f20032b9e171844b00ea507e11960bd94a](http://etherscan.io/address/0x000000f20032b9e171844b00ea507e11960bd94a#code) |                  2399|
|[0x612e2daddc89d91409e40f946f9f7cfe422e777e](http://etherscan.io/address/0x612e2daddc89d91409e40f946f9f7cfe422e777e#code) |                  1840|
|[0x3b612a5b49e025a6e4ba4ee4fb1ef46d13588059](http://etherscan.io/address/0x3b612a5b49e025a6e4ba4ee4fb1ef46d13588059#code) |                   323|
|[0x000000008924d42d98026c656545c3c1fb3ad31c](http://etherscan.io/address/0x000000008924d42d98026c656545c3c1fb3ad31c#code) |                   243|
|[0x76f948e5f13b9a84a81e5681df8682bbf524805e](http://etherscan.io/address/0x76f948e5f13b9a84a81e5681df8682bbf524805e#code) |                   200|

We see that the top two addresses alone account for 4,239 of our 11,155 contracts. Further, checking the Etherscan links, **we see that none of these top five creator addresses are actually EOAs; instead, they are all contracts that can be used to deploy NFT contracts**. For example, the most prolific creator is called [ERC1155SeaDropCloneFactory](https://etherscan.io/address/0x000000f20032b9e171844b00ea507e11960bd94a#code) and describes itself as "A factory contract that deploys ERC1155 token contracts". 

What share of our NFT projects are, in fact, created by other contracts like this one? We can join back to `dim_contracts` to find out: 

{% highlight sql %}
SELECT 
  sub.*  
, CASE WHEN dc2.creator_address IS NULL THEN 0 ELSE 1 END AS creator_is_contract_address
FROM(
  SELECT 
      dc.creator_address AS creator_address
  ,   COUNT(DISTINCT enm.nft_address) AS n_nft_contracts_created
  FROM 
      ethereum.nft.ez_nft_mints enm
  LEFT JOIN 
      ethereum.core.dim_contracts dc
  ON 
      enm.nft_address = dc.address
  WHERE 
      enm.block_timestamp::DATE > '2023-12-14'
      AND enm.block_timestamp::DATE < '2024-01-14'
  GROUP BY
      1
) sub
LEFT JOIN
  ethereum.core.dim_contracts dc2 
ON 
  sub.creator_address = dc2.address
;
{% endhighlight %}

Here is a summary of this query: 

| Is Creator Contract?| Num NFT Contracts| Num Creators|
|--------------------:|-----------------:|------------:|
|                   No|              4821|         3826|
|                  Yes|              6334|          212|

The table shows that of our 4038 distinct creators, only 212 are contracts. However, these contracts actually account for the majority of our 11,155 NFT contracts (6334/11155 or about 57%). Hence, if we are interested in the EOA that originally created the NFT contract (as I am), this approach will not suffice.

As an alternative approach, we can try the following: 

1. Using `dim_contracts`, identify the transaction hash that created the NFT contract of interest (via the `created_tx_hash` field).
2. Join to the `fact_transactions` table ([link](https://flipsidecrypto.github.io/ethereum-models/#!/model/model.ethereum_models.core__fact_transactions)) to look up the EOA *that iniated the transaction that created the NFT contract* (i.e. `from_address` in the `fact_transactions` table). 

This approach should identify an EOA *regardless* of whether the NFT contract was created via a factory contract or deployed directly (since only EOAs can initiate transactions). Further, I would hope that it will identify *the same* EOA as `creator_address` in `dim_contracts` in the case where the NFT was deployed directly by an EOA. Here is a query to investigate further: 

{% highlight sql %}
SELECT 
  enm.nft_address AS enm_nft_address
, dc.creator_address AS dc_creator_address
, CASE WHEN dc2.creator_address IS NULL THEN 0 ELSE 1 END AS dc_creator_is_contract_address
, fc.from_address AS tx_creator_address
FROM(
  SELECT 
    nft_address
  FROM 
    ethereum.nft.ez_nft_mints
  WHERE 
      block_timestamp::DATE > '2023-12-14'
      AND block_timestamp::DATE < '2024-01-14'
  GROUP BY
      1
) enm 
LEFT JOIN 
    ethereum.core.dim_contracts dc
ON 
    enm.nft_address = dc.address
LEFT JOIN 
    ethereum.core.dim_contracts dc2
ON 
    dc.creator_address = dc2.address
LEFT JOIN 
    ethereum.core.fact_transactions fc
ON 
    fc.tx_hash = dc.created_tx_hash
;
{% endhighlight %}

This query creates a table with one row for each of our 11155 NFT projects with a new field `tx_creator_address` that is the address that initiated the transaction that created the NFT contract. Using this new field, let's again look at the most prolific NFT project creators: 

|Creator Address (Tx init)                  | NFT Contracts Created|
|:------------------------------------------|---------------------:|
|[0xfbc3b76a206f03f1edbf411f280444cd3fd9c7c8](http://etherscan.io/address/0xfbc3b76a206f03f1edbf411f280444cd3fd9c7c8) |                    24|
|[0xff1896cfc912ceda37319eba452906dea8cb343c](http://etherscan.io/address/0xff1896cfc912ceda37319eba452906dea8cb343c) |                    17|
|[0x2f2d07d60ea7330dd2314f4413ccbb2dc25276ef](http://etherscan.io/address/0x2f2d07d60ea7330dd2314f4413ccbb2dc25276ef) |                    16|
|[0x9f218c1380ad55e4a40b4da89795bd56e93e90ea](http://etherscan.io/address/0x9f218c1380ad55e4a40b4da89795bd56e93e90ea) |                    15|
|[0x868964fa49a6fd6e116fe82c8f4165904406f479](http://etherscan.io/address/0x868964fa49a6fd6e116fe82c8f4165904406f479) |                    14|

As desired, these are indeed all EOAs. Further, as we might expect, the distribution of NFT contracts created per creator is far less skewed; the most prolific creator now has only 24 NFT creations. We can also confirm that the transaction initiator address differs from the `creator_address` we were using previously if and only if the `creator_address` *is* a contract. This is indeed the case: 

| Creator_addr is Contract     |Creator_addr == Tx init addr.    | Num NFT Contracts|
|-----------------------------:|:--------------------------------|-----------------:|
|                            No|                              Yes|              4821|
|                           Yes|                               No|              6334|

Finally, for some additional sanity checking, let's pull a random sample of creator addresses (based on the tx initiator) where the `creator_address` *was* a contract and see if they line up with the "creator" listed on OpenSea. Here is a random ten with links to the corresponding OpenSea pages for the project and creator address:

|NFT Address                                |TX-based Creator Address                   |
|:------------------------------------------|:------------------------------------------|
|[0x0cb02368ab4d88186f265f157ac7fe6ceca8623c](https://opensea.io/assets/ethereum/0x0cb02368ab4d88186f265f157ac7fe6ceca8623c) |[0xc97f169275b3ed28b28f7050385ec0ee533fd316](https://opensea.io/0xc97f169275b3ed28b28f7050385ec0ee533fd316) |
|[0x8f2224b40fe0c390bdd2c20132488a29b382fca3](https://opensea.io/assets/ethereum/0x8f2224b40fe0c390bdd2c20132488a29b382fca3) |[0xb9d5c93ec9aba93180ddd00a628e8facc3103039](https://opensea.io/0xb9d5c93ec9aba93180ddd00a628e8facc3103039) |
|[0x5381200d7fb93f2424173668921acee869dfe0b2](https://opensea.io/assets/ethereum/0x5381200d7fb93f2424173668921acee869dfe0b2) |[0x04e389eef182446662b11bc408c5e5d6c32a4cad](https://opensea.io/0x04e389eef182446662b11bc408c5e5d6c32a4cad) |
|[0xf2519e127e983cf996ee085fd1bf8a2fc9001287](https://opensea.io/assets/ethereum/0xf2519e127e983cf996ee085fd1bf8a2fc9001287) |[0xe524a47bbda078208e94ca8028985af52caf408f](https://opensea.io/0xe524a47bbda078208e94ca8028985af52caf408f) |
|[0x766cfda32f6e04691018cd431faedbe4e51fd2d6](https://opensea.io/assets/ethereum/0x766cfda32f6e04691018cd431faedbe4e51fd2d6) |[0x5d2b4063aedb121b5c8aeea39f9626f04da6bffb](https://opensea.io/0x5d2b4063aedb121b5c8aeea39f9626f04da6bffb) |
|[0xdd74ca629bf62620301050d0afacd3efaac18177](https://opensea.io/assets/ethereum/0xdd74ca629bf62620301050d0afacd3efaac18177) |[0x002652b2cebda595da4c2707a83146b5f5b63494](https://opensea.io/0x002652b2cebda595da4c2707a83146b5f5b63494) |
|[0x92961bbf2ad8eaf2f63b68d7a10ca1917f9f9a8f](https://opensea.io/assets/ethereum/0x92961bbf2ad8eaf2f63b68d7a10ca1917f9f9a8f) |[0x14709717a07a654e40f963a1ce49a06ee3430049](https://opensea.io/0x14709717a07a654e40f963a1ce49a06ee3430049) |
|[0x995b4a37259ae6684c37385b8095c61c25c2c3f0](https://opensea.io/assets/ethereum/0x995b4a37259ae6684c37385b8095c61c25c2c3f0) |[0xdf8671f53db260239e0ab0af114ac85a0f3ef028](https://opensea.io/0xdf8671f53db260239e0ab0af114ac85a0f3ef028) |
|[0x9d7ae1cf50c5081ce1dabc60fc9d7ccd5dfa90d1](https://opensea.io/assets/ethereum/0x9d7ae1cf50c5081ce1dabc60fc9d7ccd5dfa90d1) |[0x63c42555dccea639ad1796dac1dc0cdd5680ad50](https://opensea.io/0x63c42555dccea639ad1796dac1dc0cdd5680ad50) |
|[0x0e683cf6b10b18eae4576a26897f419b1011899b](https://opensea.io/assets/ethereum/0x0e683cf6b10b18eae4576a26897f419b1011899b) |[0xd2b4705434d298d26c157d7be14dbff480923df4](https://opensea.io/0xd2b4705434d298d26c157d7be14dbff480923df4) |

Manually inspecting, this seems to work decently well; however, there is one case where things do not line up with OpenSea: [this collection](https://opensea.io/collection/ethernity-master). I am not sure why this case behaves differently. In my next phase of analysis, I will explore comparing with OpenSea more systematically using the [OpenSea API](https://docs.opensea.io/reference/api-overview) to better understand the magnitude of misalignment. The OpenSea API in general could be another way to identify the creator of an NFT project, and so is worth better understanding for this purpose as well (e.g. what is the process that OpenSea is using to link projects and creators?). 
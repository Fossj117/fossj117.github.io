---
layout: post
title: "How many smart contracts are deployed on Ethereum?"
date: 2024-01-13
latex: true
mathjax: true
comments: true
tag: ["web3"]
---

For a research project, I have an interest in determining whether particular ETH addresses are smart contracts vs. EOAs. This is slightly less straightforward to answer than I expected. However, here is a [Flipside](https://flipsidecrypto.xyz/) query that was recommended to me by [Sam](https://twitter.com/sem1d5) in the Flipside Discord for building a table of contract addresses on Ethereum:

{% highlight sql %}
SELECT
    to_address AS created_contract_address
FROM
    ethereum.core.fact_traces
WHERE
    TYPE ILIKE 'create%'
    AND to_address IS NOT NULL
    AND input IS NOT NULL
    AND input != '0x'
    AND tx_status = 'SUCCESS'
    AND trace_status = 'SUCCESS'
{% endhighlight %}

In my understanding, this query is essentially getting a list of all successful contract creation events based on the `fact_traces` table. What is in this table exactly? Per [the documentation](https://flipsidecrypto.github.io/ethereum-models/#!/model/model.ethereum_models.core__fact_traces), the `fact_traces` table:

> contains flattened trace data for internal contract calls on the Ethereum blockchain.

In my understanding, a `CREATE` or `CREATE2` trace is generated both when a contract is deployed directly by an EOA (as [here](https://etherscan.io/tx/0xe605400927bfaef21248dd0e5ef9787b1a5d84495eedca574bfbeb0e8cce4b5a/advanced)) or when a contract is deployed via another contract (as [here](https://etherscan.io/tx/0x0680bad178f1470727ce1972a27f2fa45cdb2d6a71d2d7f045384054a5b00480)). (Sam also recommended [Blocksec Phalcon](https://phalcon.blocksec.com/explorer/tx/eth/0xe605400927bfaef21248dd0e5ef9787b1a5d84495eedca574bfbeb0e8cce4b5a) for looking at trace data.)

So, this query should capture all contract creation events. What does it say about the total volume of contracts created on Ethereum? Going back to the start of 2021 and grouping by date, here is a plot of the daily count of Ethereum contract creation events:

<p>
  <img alt="Count" src="/figs/2024-01-13-how-many-smart-contracts/daily_contract_creation.png" width="100%">
</p>

Here is the total count by year:

| Year | # Contracts |
| ---: | ----------: |
| 2021 |    11212980 |
| 2022 |     7771282 |
| 2023 |     9217212 |

So this suggests that something like 28,201,474 contracts were deployed on Ethereum between the start of 2021 and the end of 2023. Per the chart, the volume of contract creations events seems to be fairly volatile, with distinct phases of high and low volume. I am not sure exactly what accounts for these phases, as they don't exactly seem to line up with general strength in the Ethereum market. 

*Thank you to [Kassandra](https://github.com/kassandraoftroy) for working through this with me*

## Notes

For reference, here is [a similar query](https://dune.com/queries/3349747/5613990/) that works on Dune.

{% highlight sql %}
SELECT
    COUNT(*) as n_contracts_created
FROM 
    ethereum.traces
WHERE
    AND "type" = 'create'
    AND success
    AND tx_success;
{% endhighlight %}

Here is the full daily query on Flipside:
{% highlight sql %}
SELECT
    block_timestamp::date AS DS
,   COUNT(*) AS n_contracts_created
FROM
    ethereum.core.fact_traces
WHERE
    TYPE ILIKE 'create%'
    AND to_address IS NOT NULL
    AND input IS NOT NULL
    AND input != '0x'
    AND tx_status = 'SUCCESS'
    AND trace_status = 'SUCCESS'
    AND block_timestamp::date >= '2021-01-01'
    AND block_timestamp::date < '2024-01-01'
GROUP BY 1
ORDER BY 1;
{% endhighlight %}

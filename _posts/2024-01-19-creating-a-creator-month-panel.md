---
layout: post
title: "Building a Creator-Month Panel Dataset"
date: 2024-01-19
latex: true
mathjax: true
comments: true
tag: ["web3"]
---

*N.B. I'm not sure this post will be interesting to anyone besides me (unless you also happen to be doing some very related analysis with Flipside!)* 

Today, I will be continuing my series of posts about an ongoing web3 academic research project. Building on my [last post](https://jeffreyfossett.com/2024/01/15/rates-of-NFT-project-creation.html), I will today be building a creator-level panel dataset. The goal is to create a dataset with the following measure: 

* $NewProjects_{it}$: the number of new NFT project created by creator $i$ with a first mint event in month $t$. 

Project ownership will be defined as outlined in [my previous post](https://jeffreyfossett.com/2024/01/14/who-created-this-contract.html). The inclusion criteria for the panel will be as follows[^1]: 

* All creators with at least one NFT asset that was sold between `2021-01-01` and `2022-01-01` (based on Flipside's `ez_nft_sales` table).
* All months from `2022-03` through `2023-12`.

This straightforward in principle; however, the query logic starts to get a bit long, so let's build it up in pieces. First, I will build a table called `first_mint_events` with one record per project that ever has a mint event according to Flipside; I also join in some additional date info at this stage: 

{% highlight sql %}
WITH first_mint_events AS (
  SELECT 
    fme.nft_address
  , fme.ts_first_mint
  , fme.ds_first_mint
  , dd.month_start_date as ds_month_start
  FROM(
    SELECT
      nft_address
    , MIN(block_timestamp) AS ts_first_mint
    , MIN(block_timestamp)::DATE AS ds_first_mint
    FROM
      ethereum.nft.ez_nft_mints
    WHERE
      block_timestamp < '2024-01-01'
    GROUP BY 
      nft_address
  ) fme 
  LEFT JOIN 
    ethereum.core.dim_dates dd ON fme.ts_first_mint::DATE = dd.date_day
)
{% endhighlight %}

This yields a dataset of `274,197` distinct NFT projects. Next, I will link projects in this table to the addresses of their creators using the method outlined [here](https://jeffreyfossett.com/2024/01/15/rates-of-NFT-project-creation.html); this will create a table I will call `first_mint_events_w_creators`: 

{% highlight sql %}
first_mint_events_w_creators AS ( 
    SELECT 
        fme.*
    ,   fc.from_address AS creator_address
    FROM 
        first_mint_events fme
    LEFT JOIN
        ethereum.core.dim_contracts dc ON fme.nft_address = dc.address
    LEFT JOIN 
        ethereum.core.fact_transactions fc ON dc.created_tx_hash = fc.tx_hash
)
{% endhighlight %}

This yields a project-level table (still with `274,197` records), and `161,660` distinct creators[^2]. There are no cases where an NFT contract is *not* linked to a creator address (which is good because *someone* had to deploy it). This table is important for me because it links projects with creators. 

Next, I need to find the set of creators who meet my historical filtering logic -- in particular, I only want to include creators with at least one NFT asset that was sold between `2021-01-01` and `2022-01-01`. For this, I combine Flipside's `ez_nft_sales` with my `first_mint_events_w_creators` table, to create a project-level table called `sales_history` with only projects (and their creators) that sold at least once during the desired period (I also make a creator-level version): 

{% highlight sql %}
WITH sales_history AS (
    SELECT
      fmec.creator_address
    , ens.nft_address
    FROM
      ethereum.nft.ez_nft_sales ens
    JOIN 
        first_mint_events_w_creators fmec ON ens.nft_address = fmec.nft_address
    WHERE
      ens.currency_symbol = 'ETH'
      AND ens.price > 0
      AND ens.price_usd > 0
      AND ens.block_timestamp > '2021-01-01'
      AND ens.block_timestamp < '2022-01-01'
    GROUP BY 
        1,2
), 
sales_history_creator_level AS(
    SELECT creator_address FROM sales_history GROUP BY 1
)
{% endhighlight %}

I find that there are `8697` distinct projects that appear during this transaction period and `6097` distinct creators. I do note that there are `159` NFT projects exclude by my `INNER JOIN` here; these are projects for which I did not have an associated "mint" event in the database; I am not sure what explains the presence of projects that are sold at some point but never have a mint event. For now, I exclude them since they are a relatively small portion of projects. 

Finally, we are ready to create our creator-month level panel. To do this, I `CROSS JOIN` a set of month-level observations with the `sales_history_creator_level` table, and then left join on a creator-month aggregation of `first_mint_events_w_creators` and finally filter out creators who never have any new project creations during the entire 15-month period. If you want the whole query in all its CTE glory, here it is (I am using this as an excuse to try a collapsible code block): 

<html>
<p><details>

<summary><code><strong>Expand for the query!</strong></code></summary>

{% highlight sql %}
-- First, get a table of all NFT projects with first mint event
WITH first_mint_events AS (
  SELECT 
    fme.nft_address
  , fme.ts_first_mint
  , fme.ds_first_mint
  , dd.month_start_date as ds_month_start
  FROM(
    SELECT
      nft_address
    , MIN(block_timestamp) AS ts_first_mint
    , MIN(block_timestamp)::DATE AS ds_first_mint
    FROM
      ethereum.nft.ez_nft_mints
    WHERE
      block_timestamp < '2024-01-01'
    GROUP BY 
      nft_address
  ) fme 
  LEFT JOIN 
    ethereum.core.dim_dates dd ON fme.ts_first_mint::DATE = dd.date_day
), 
-- Then, join to contracts table to get creator address from deploy tx; also add in first mint month
first_mint_events_w_creators AS ( 
    SELECT 
        fme.*
    ,   fc.from_address AS creator_address
    FROM 
        first_mint_events fme
    LEFT JOIN
        ethereum.core.dim_contracts dc ON fme.nft_address = dc.address
    LEFT JOIN 
        ethereum.core.fact_transactions fc ON dc.created_tx_hash = fc.tx_hash
),
-- Select projects that transacted during the relevant period
sales_history AS (
    SELECT
      fmec.creator_address
    , ens.nft_address
    FROM
      ethereum.nft.ez_nft_sales ens
    LEFT JOIN 
        first_mint_events_w_creators fmec ON ens.nft_address = fmec.nft_address
    WHERE
      ens.currency_symbol = 'ETH'
      AND ens.price > 0
      AND ens.price_usd > 0
      AND ens.block_timestamp > '2021-01-01'
      AND ens.block_timestamp < '2022-01-01'
    GROUP BY 
        1,2
), 
-- Aggregate at the creator level
sales_history_creator_level AS(
    SELECT creator_address FROM sales_history GROUP BY 1
), 
-- Build a table of monthly dates for the panel
monthly_dates AS (
  SELECT month_start_date as ds_month_start 
  FROM ethereum.core.dim_dates 
  WHERE date_day >='2022-03-01' and date_day <= '2023-12-31'
  GROUP BY 1
), 
-- Cross join creator addresses with monthly dates to build a panel
creator_month_panel AS (
  SELECT 
    shc.creator_address
  , md.ds_month_start
  FROM 
    sales_history_creator_level shc
  CROSS JOIN 
    monthly_dates md
), 
-- Add the number of projects created in each month to the panel
creator_month_panel_w_n_projects_created_in_month AS (
  SELECT 
    cmp.creator_address 
  , cmp.ds_month_start as ds_month_start
  , COALESCE(fm.n_projects_w_first_mint_in_month, 0) AS n_projects_created_in_month
  FROM 
    creator_month_panel cmp
  LEFT JOIN(
    SELECT 
      creator_address
    , ds_month_start
    , COUNT(DISTINCT nft_address) AS n_projects_w_first_mint_in_month
    FROM 
      first_mint_events_w_creators
    GROUP BY
      1,2
  ) fm ON cmp.creator_address = fm.creator_address AND cmp.ds_month_start = fm.ds_month_start
)
-- Finally, filter cases where there's never a project creation event
SELECT 
  c.*
FROM  
  creator_month_panel_w_n_projects_created_in_month c
JOIN (
  SELECT 
    creator_address
  FROM 
    creator_month_panel_w_n_projects_created_in_month
  WHERE 
    n_projects_created_in_month > 0
  GROUP BY 
    1
) c2 
ON c.creator_address = c2.creator_address
;
{% endhighlight %}
</details>
</p>
</html>
The final table has `1098` distinct creators observed over `22` months for a total of `24,156` creator-month observations. This may not be the cleanest or most efficient way to build the dataset I am interested; however, what is most important to me is getting the logic correct. It would be nice if Flipside allowed analysts to build their own intermediate tables in at least some limited way; that would be easier than working with all these CTEs and would make it easier to confirm that intermediate logic steps are working properly. I have been told that there is some support for using LiveQuery to access the output of one query in another; however, I haven't explored this (one reference [here](https://medium.com/@der_piper/how-to-use-livequery-in-flipside-studio-and-its-most-asked-questions-36a500f4f2d9)). 

Anyhow, that's all for me today. In my next post on this theme, I will try adding even more fields to this dataset, and maybe finally get to some analysis.

## Footnotes

[^1]: These may seem like arbitrary criteria; however, they are motivated by other aspects of my analysis plan which have not yet been documented on this site! 

[^2]: Note, these numbers are slightly larger than my [previous post](https://jeffreyfossett.com/2024/01/15/rates-of-NFT-project-creation.html) because I am including a slightly longer date range. 
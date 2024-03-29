---
layout: post
title: FCC Filings Overwhelmingly Support Net Neutrality Once Spam is Removed
date: 2017-05-13
comments: true
latex: true
tag: ["analysis"]
---

### An Explosion of Comments

Public comments on [the FCC's anti-net neutrality proceeding](https://www.fcc.gov/ecfs/search/filings?proceedings_name=17-108&sort=date_disseminated,DESC) have
exploded over the past week following [an incisive pro-net neutrality rant from John Oliver](https://www.youtube.com/watch?v=92vuuZt7wak) on Sunday. The proceeding, which had accumulated about 39,000 public comments as of Saturday 5/7 at 8PM (prior to Oliver's segment), has now seen more than 1.1 million comments as of Friday 5/12 at 8PM (just five days later)[^1]:

![center](/figs/2017-05-13-fcc-filings/final_version/cumulative_filings_over_time.png)

Comments accumulated rapidly over the course of the week, peaking at a rate of over 44,000 comments per hour on Thursday[^2]:

![](/figs/2017-05-13-fcc-filings/final_version/hourly_filings_over_time.png)

On this chart, the gap between Oliver's segment concluding and the influx of comments is presumably due to site downtime that the [FCC reported on Monday morning](http://transition.fcc.gov/Daily_Releases/Daily_Business/2017/db0508/DOC-344764A1.pdf). The FCC claims that this downtime was driven by a malicious DDoS attack. However, the timing of the downtime relative to Oliver's segment casts some doubt on this claim; as many have pointed out, an influx of requests & comments from Oliver's audience could easily be mistaken for a DDoS attack. [Two senators](https://arstechnica.com/information-technology/2017/05/after-net-neutrality-comment-system-fails-senators-demand-answers/) and one pro-net neutrality group has [called on the FCC to release logs](http://www.networkworld.com/article/3195466/security/fcc-should-produce-logs-to-prove-multiple-ddos-attacks-stopped-net-neutrality-comments.html) supporting the claim that they were DDoSed.

The chart also shows evidence of other periods of intermittent downtime throughout the week, [as reported by pro-net neutrality group Fight for the Future](https://www.fightforthefuture.org/news/2017-05-11-what-is-the-fcc-hiding-thousands-call-for-the/).

### Anti-Net Neutrality Spam Floods the Comments

Not long after Oliver's segment aired, [reports](https://www.recode.net/2017/5/10/15612864/fcc-net-neutrality-bots-spam-comments-online-government-rules-ajit-pai) [began](https://www.theverge.com/2017/5/10/15610744/anti-net-neutrality-fake-comments-identities) to surface that FCC commenting had become a target of bots and spammers. What was the impact of these efforts? After some light text cleaning[^3], here are the top 10 most common free text filings:

| Rank | Statement[^4]                                                                                                   |  Count  | % of Total |
| :--: | :-------------------------------------------------------------------------------------------------------------- | :-----: | :--------: |
|  1   | the unprecedented regulatory power the obama administration imposed on the internet is smothering innovation... | 440,049 |   38.8%    |
|  2   | i support strong net neutrality backed by title 2 oversight of isps                                             | 26,324  |    2.3%    |
|  3   | i specifically support strong net neutrality backed by title 2 oversight of isps                                | 16,014  |    1.4%    |
|  4   | i was outraged by the obama wheeler fccs decision to reclassify the internet as a regulated public utility...   | 13,748  |    1.2%    |
|  5   | preserve net neutrality and title 2                                                                             | 12,285  |    1.1%    |
|  6   | i am in support of strong net neutrality backed by title 2 oversight of isps                                    |  5,369  |    0.5%    |
|  7   | as an internet user im asking the fcc to protect the net neutrality protections currently in place...           |  5,309  |    0.5%    |
|  8   | i support net neutrality backed by title 2 oversite of internet service providers                               |  5,182  |    0.5%    |
|  9   | please preserve net neutrality and title 2                                                                      |  5,051  |    0.4%    |
|  10  | [No Text]                                                                                                       |  3,801  |    0.3%    |

Many of the top comments are variants of [Oliver's recommended comment](https://www.youtube.com/watch?v=92vuuZt7wak&t=16m08s) supporting net neutrality backed by Title II oversight. This demonstrates that Oliver was likely an inspiration for many filings[^5].

However, most striking is that the top-submitted comment ("the unprecedented regulatory power..."[^6]) has been filed over 440,000 times, including over 270,000 times on Thursday 5/11 alone:

![](/figs/2017-05-13-fcc-filings/final_version/hourly_filings_spam_vs_organic.png)

We can't say for sure whether these submissions were due to a bot (see below); however, [various](https://medium.com/@nhf/whats-up-with-all-of-those-identical-comments-on-the-fcc-net-neutrality-docket-105835f59c3e) [reports](https://www.theverge.com/2017/5/10/15610744/anti-net-neutrality-fake-comments-identities) [suggest](http://www.zdnet.com/article/a-bot-is-flooding-the-fccs-website-with-fake-anti-net-neutrality-comments/) that there are reasons to believe that at least some share of them were. In particular, although the repeated (hereafter: "spam") submissions include real names and addresses, a number of individuals whose names appear [have](https://www.theverge.com/2017/5/11/15626278/net-neutrality-spam-bot-fcc-leak-data) [denied](http://www.zdnet.com/article/a-bot-is-flooding-the-fccs-website-with-fake-anti-net-neutrality-comments/) submitting the comments.

### Spam Comment Emails May Have Come From a Data Breach

Earlier this week, [The Verge reported](https://www.theverge.com/2017/5/11/15626278/net-neutrality-spam-bot-fcc-leak-data) that the names and email addresses used in the fraudulent filings may have been pulled from a data breach of River City Media (RCM).

To further investigate this hypothesis, I randomly sampled 1000 filings that used the repeated text and queried the [HaveIBeenPwned API](https://haveibeenpwned.com/API/v2#BreachesForAccount) to retrieve a list of known data breaches that the associated emails were involved in. I found that ~76% of emails associated with the repeated comment had been involved in at least one data breach, and ~66% were part of the RCM breach specifically:

![](/figs/2017-05-13-fcc-filings/final_version/breach_appearances.png)

This lends some support to the claim that many of the repeated comments are fraudulent. However, a few caveats are worth keeping in mind. First, the RCM breach is extremely large (1.4 billion records), and so the majority of _any_ random list of emails might show up in the breach. Second, just because an email shows up on the RCM list doesn't mean that the associated filing is bogus, given that we [know](https://www.theverge.com/2017/5/10/15610744/anti-net-neutrality-fake-comments-identities) that a conservative group called Center for Individual Freedom provided a form to its supporters that included the same spam text.

### After Removing the Anti-NN Spam, Filings Overwhelmingly Support Net Neutrality

Supposing that the anti-net neutrality spam _is_ all fraudulent, do most filings support or oppose net neutrality? To find out, I took a [random sample](https://docs.google.com/spreadsheets/d/1SrM59Ol5OtLM96mH8Mm1QanBoyESy4V5YV9rJDmbD38/edit?usp=sharing) of 200 comments from the pool of filings (excluding the repeated anti-NN comments) and hand-tagged the comments as "Supports net neutrality", "Opposes net neutrality" or "Other". The results show that the remaining comments overwhelming support net neutrality[^7]:

![](/figs/2017-05-13-fcc-filings/final_version/non_spam_support.png)

As noted above, we don't know for sure whether the spam comments are (exclusively) fraudulent; however, even if the spam comments _were all legitimate_[^8], this analysis suggests that filings _would still be in favor of net neutrality_ by roughly a 59-40 margin overall[^9]. We also don't know the extent or impact of possible botting / spamming on the pro-NN side, which could shift the balance of opinion as well.

### The FCC Should Reconsider its Position on Net Neutrality

The FCC has [now entered](https://assets.documentcloud.org/documents/3719846/DA-17-454A1.pdf) a "Sunshine" period for docket 17-108, during which it will not consider new comments. Given the magnitude of filings (~695,000 if you exclude the anti-NN spam) and the balance of opinion expressed (97% in favor of net neutrality or 59% if you include the spam), **this analysis suggests that the FCC should reconsider its position on net neutrality** during this period of reflection[^10].

### Edits

<i> **EDIT**: Did not expect this to blow up as much as it has! With that, wanted to highlight some important caveats to keep in mind when reading this post: (i) in this post I use the term "spam" to connote an identical bit of text that was repeatedly filed many times; importantly, we don't know exactly what share of these "spam" comments are legitimate, though we do know that some are fabricated; (ii) there is some evidence of botting/spamming on the pro-NN side as well (though likely not to the same degree), which is not addressed in this post, and could shift conclusions. If anyone is interested to futher address these caveats, please let me know and I am happy to collaborate or share data.

<i> **EDIT 2**: For more analysis on this topic (including important points not addressed here), I highly recommend you check out [this](https://medium.com/@csinchok/an-analysis-of-the-anti-title-ii-bots-463f184829bc) analysis from [Chris Sinchok](https://twitter.com/chrissinchok), as well as [this](https://medium.com/@nhf/whats-up-with-all-of-those-identical-comments-on-the-fcc-net-neutrality-docket-105835f59c3e) analysis from [Nathaniel Fruchter](http://www.nathanielfruchter.com/)

<i> **EDIT 3**: [New analysis](http://dailycaller.com/2017/05/17/more-than-300000-pro-net-neutrality-comments-on-fccs-public-forum-likely-fakes/) from the Daily Caller suggests that substantial pro-NN botting may have occurred as well (a point not addressed here). Please take a look!

### Appendix

[^1]: Data for this post was scraped directly from FCC.gov on Friday 5/12 at 11 PM using Python. The astute reader may notice that the number of comments quoted for 5/7 deviates somewhat from my [previous post on reddit](https://www.reddit.com/r/dataisbeautiful/comments/6akxrh/john_olivers_impact_on_fcc_net_neutrality_filings/). This is because I am quoting from a different time on 5/7 (8PM vs. 12AM) for ease of comparison.
[^2]: On this plot and the previous one, we are assigning posts to timestamps using the `date_submission` field in the JSON returned. My understanding of this field is that it gives the timestamp for when the comment was submitted by the filer. To convert to hourly volumes, posts are rounded to the _next_ whole hour (so e.g. the count of filings for 2PM EST is the count of filings submitted between 1:00:01 and 2:00:00 PM).
[^3]: Lowercasing, removal of punctuation, whitespace trimming, collapse "II" to "2" to capture "Title II" vs. "Title 2" variation.
[^4]: For ease of consumption, I have truncated several of the longer comments. Note that comment number 10 is filings that were submitted with no text.
[^5]: Note that some of these filings may be bots as well. For example, submissions of comment number 8 appear to be [driven by a pro-net neutrality bot](https://www.fcc.gov/ecfs/filing/1051252019619) calling itself "The Internet". Additionally, this simple analysis fails to capture slightly-more-clever form messages, like [this](https://dearfcc.org/) one, which allows user to customize their message and sign their name. Further analysis could investigate the impact of such campaigns.
[^6]: The full text of the comment reads: "The unprecedented regulatory power the Obama Administration imposed on the internet is smothering innovation, damaging the American economy and obstructing job creation. I urge the Federal Communications Commission to end the bureaucratic regulatory overreach of the internet known as Title II and restore the bipartisan light-touch regulatory consensus that enabled the internet to flourish for more than 20 years. The plan currently under consideration at the FCC to repeal Obama's Title II power grab is a positive step forward and will help to promote a truly free and open internet for everyone."
[^7]: Plot includes 95% confidence interval.
[^8]: We know for a fact that they are not, but this is the most charitable assumption possible.
[^9]: Here is how I compute this: `Opposed = .388 + .02(1-.388) = .400 = 40.0%`; `Support = (1-.388)*.965 = 0.591 = 59.1%`
[^10]: I have done my best to make this analysis as reproducible as possible. All code is available in the github for this blog post [here](https://github.com/Fossj117/fossj117.github.io) (see the `_code` folder). A copy of the data set is also availabe there, though I have stripped the emails in the interest of privacy. If you find any errors in the analysis, please do not hesitate to contact me at fossj117@gmail.com to let me know.

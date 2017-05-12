---
layout: post 
title: Comey Has Never Been A Bigger Focus of Attention in American Politics
date: 2017-05-12
comments: true
---

James Comey has loomed large in American political discourse over the past year. However, according to [Google search data](https://trends.google.com/trends/explore?date=2016-05-12%202017-05-12&geo=US&q=comey) (see below), Comey has never been a bigger focus of popular attention than he is right now, after being fired by President Trump: 

![center](/figs/2017-05-12-comey-interest/comey_interest_full_year.png)

This chart shows the relative frequency[^1] of US google searches for the term "Comey" over the past year, and can be used as rough proxy for US public "interest" in Comey-related stories[^2]. 

As the chart suggests, Comey has drawn substantial public attention at least four times over the past year. Here is a timeline of the major events:

* **Jul. 5, 2016**: Comey [gives press conference](https://www.fbi.gov/news/pressrel/press-releases/statement-by-fbi-director-james-b-comey-on-the-investigation-of-secretary-hillary-clinton2019s-use-of-a-personal-e-mail-system) on Clinton's use of private email server. Comey recommends that Clinton not be prosecuted, but noted that she was "extremely careless" in handling of classified information. 

* **Oct. 28, 2016**: Comey sends [letter to Congress](https://www.washingtonpost.com/apps/g/page/politics/oct-28-fbi-letter-to-congressional-leaders-on-clinton-email-investigation/2113/) informing leadership that FBI will be investigating newly-discovered Clinton emails from Huma Abedin's laptop. Comey would [later announce]((https://www.washingtonpost.com/politics/9-days-after-roiling-campaign-fbi-says-it-wont-seek-charges-against-clinton/2016/11/06/6f0f5d5c-a468-11e6-8fc0-7be8f848c492_story.html?utm_term=.e54a13872a2a)) (on Nov. 6) that new emails will not change the FBI's previous recommendation that Clinton not be prosecuted. 

* **Mar. 20, 2017**: Comey [confirms existence of FBI probe on Russia election hacking & Trump campaign connections to Russia](https://www.theatlantic.com/politics/archive/2017/03/its-official-the-fbi-is-investigating-trumps-links-to-russia/520134/). 

* **May 9, 2017**: Trump [fires James Comey](https://www.nytimes.com/2017/05/09/us/politics/james-comey-fired-fbi.html).

Although these events have varied in the volume of attention they have drawn, the above chart shows that Comey's firing has created by far the biggest splash, driving almost twice as many Google searches as the next largest event (Comey's pre-election letters to Congress about Clinton's emails). 

While the extra attention to the Comey firing is certainly warranted to some extent, readers should also be mindful that this story [not drown out everything else that's happened this week](https://fivethirtyeight.com/features/trumpbeat-yes-there-was-non-comey-news-this-week/).  

## Comey was Associated with both Clinton and Trump at Different Times

As outlined above, Comey and the FBI have been involved in storylines involving both President Trump and Secretary Clinton over the past year. But which stories were associated with which candidate, and to what degree? [Google search data](https://trends.google.com/trends/explore?date=2016-05-12%202017-05-12&geo=US&q=comey,comey%20trump,comey%20clinton) can again shed some light on these questions: 
 
![center](/figs/2017-05-12-comey-interest/comey_clinton_trump.png)

Much of the Comey search volume is independent and associated with neither candidate; however, to the extent that the candidate searches *are* associated with Comey, the degree of association for each candidate depends on the event. In particular, Clinton was more associated with the email stories, whereas Trump was more associated with the FBI probe and Comey's firing, as we'd expect. To see this more clearly, here is the normalized share of Comey searches also including "Trump" vs. "Clinton" for each major Comey event[^3]: 

![center](/figs/2017-05-12-comey-interest/comey_clinton_trump_by_event_2.png)

This plot gives us a sense, for each event, of the *degree* to which Comey attention was associated with Trump vs. Clinton. Interestingly, it seems that some Comey events were more singularly associated with a particular candidate (e.g. Clinton & the email server press conference, Trump & Russia probe), whereas others showed more of a mix (e.g. Comey's pre-election letters to congress) [^4]. 

Overall, these plots show that Comey has been a repeated focus of public attention over the course of the past year, and has never been a bigger focus than he is right now. 

### Footnotes

[^1]: Google search trends returns a "relative interest" score which is normalized against the highest point in the graph. Thus, while relative changes are observable & comparable, the absolute volume of searches is not shared by Google. See [google trends](https://support.google.com/trends/answer/4365533?hl=en) for more information.  

[^2]: Note that this data is aggregated on the *weekly* level which can be a bit coarse for investigating shorter news cycles. Here is a [similar plot](https://trends.google.com/trends/explore?date=2016-10-12%202017-05-12&geo=US&q=comey) with a more recent range of data, aggregated at the *daily* level instead:  ![center](/figs/2017-05-12-comey-interest/comey_interest_daily.png) Among other things, the more granular aggregation shows that the bump in Comey attention around the election actually splits into several smaller spikes corresponding to Comey's first and second letters to congress (and then subsequent post-election stories).

[^3]: This chart was generated by taking the week with the highest volume of Comey search coverage, and then computing the share of Comey searches also containing *each* candidate's name, and then normalizing (dividing) by the total number of Comey searches containing *either* candidate's name. It thus measures relative Comey attention to Trump vs. Clinton rather than the degree to which either candidate was associated with the story overall. 

[^4]: Note that Comey's firing also shows up as relatively more mixed than the others as well; however, this may be partially due to the fact that it includes some bleed from [Comey's testimony to Congress about handling of the Clinton investigation](https://www.nytimes.com/2017/05/03/us/politics/james-comey-fbi-senate-hearing.html), which in early May. 
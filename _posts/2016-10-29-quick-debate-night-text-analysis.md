---
layout: post 
title: "Quick Debate Night Text Analysis" 
date: 2016-10-29
latex: true 
mathjax: true
comments: true
---

After watching the first debate earlier this fall & listening to the following coverage, I was curious to apply a data-driven perspective to some of the news narratives that resulted. Fortunately, I was able to pull [Vox’s debate transcript](https://www.vox.com/2016/9/26/13065174/first-presidential-debate-live-transcript-clinton-trump). Here is what I found.

After cleaning up the Vox transcript and doing some sentence/words parsing with [NLTK](https://www.nltk.org/), I started to play with the data to see if it could provide any new insight into how the debate had gone. Defining an utterance as a unique entry on the transcript (roughly: one turn speaking), a quick look at summary statistics provided the following results:

<p>
<center>
<img alt="summary stats" align="center" src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*SE7fKanMucDZWaIqmWAYYQ.png">
</center>
</p>

It seems that Trump spoke roughly 27% more times at the debate (88 times v.s. Clinton’s 69), including roughly 21% more words and 40% more sentences. To me, these numbers generally support the narrative that’s been told about Trump’s performance & speaking style — interjecting often, typically in smaller bursts, and speaking in somewhat shorter, direct sentences.

Examining the full distribution of utterances, we see that Trump also had the longest utterance of the night, his [464-word ramble on NATO](https://www.youtube.com/watch?v=7BGYYaaLrTc&t=77m2s&ab_channel=PBSNewsHour) that ran a full 3+ minutes:

<p>
<center>
<img alt="Histogram of utterance length" align="center" src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*eD2bkpsBTGIurY-82ChVJA.png">
</center>
</p>

Another interesting thing to look at is how the length of responses (perhaps a rough proxy for more “substantive” discussion vs. quippy back-and-forth) changed over the course of the night. In the next chart, we show how utterance length varied over the course of the debate for each speaker:

<p>
<center>
<img alt="length of utterances over time" align="center" src="https://miro.medium.com/v2/resize:fit:786/format:webp/1*fSNhgpDnA4R1G6lmwKwKTg.png">
</center>
</p>

The overlaid lines here are locally smoothed trend lines by speaker. We see that responses seemed to get longer in the middle/latter portion of the debate, around the time when the discussion shifted to Trump’s business record and later race & policing. 

The segment of shorter responses earlier on (around response #50) seems to correspond to the portion of the debate where Trump was on attack about NAFTA and interrupting a lot, generating a lot of back-and-forth. A *very* rough coding of Trump interruptions (based on [this](https://www.youtube.com/watch?v=PDEC0iMxokw&ab_channel=CNN) video from CNN) confirms this hypothesis. Here is the same plot as above, but now with Trump interruptions overlaid with vertical lines:

<p>
<center>
<img alt="length of utterances over time" align="center" src="https://miro.medium.com/v2/resize:fit:786/format:webp/1*NG9XjgndqORpPdGi6fW5Qw.png">
</center>
</p>

The cluster of interruptions around the 150 mark are Trumps repeated “wrong” interjections as Clinton accused him of supporting the Iraq war.

To be sure, there’s a lot more that could be done with this data. For anyone interested, my cleaned up version of the transcript is on google sheets [here](https://docs.google.com/spreadsheets/d/1-OHfz7eUWORNDLdz9FB4AhBy1ogVNSetBQrb9iVCe90/edit?usp=sharing).








---
layout: post
title: Visualize the Freezing and Thawing Cycle of Lake Mendota
date: 2018-12-27
comments: true
latex: true
tag: ["dataviz"]
---

### Data Visualization

The goal of this data visualization is to explore trends over time in yearly "Ice On", "Ice Off" and "Days of Ice Cover" on [Lake Mendota](https://en.wikipedia.org/wiki/Lake_Mendota) using [data](http://www.aos.wisc.edu/~sco/lakes/Mendota-ice.html) from the Wisconsin State Climatology Office. The visualization is an entry in the [December 2018 /r/dataisbeautiful DataViz Battle](https://www.reddit.com/r/dataisbeautiful/comments/a2p5f0/battle_dataviz_battle_for_the_month_of_december/) (UPDATE: this visualization was [awarded second place](https://www.reddit.com/r/dataisbeautiful/comments/adihze/comment/edh5esv/?utm_source=share&utm_medium=web2x&context=3) in the competition).

![center](/figs/2018-12-27-lake-mendota/mendota_plot_final.png)

### Analysis

The plots show that Lake Mendota's seasonal days of ice cover has decreased over time by 0.18 days per year on average (p<0.01; 95% CI: [0.12 0.23]). The decrease in total days of ice cover is due in roughly equal parts to "Ice On" occuring later in the season (roughly 0.09 days later per year on average; p<0.01) and "Ice Off" occuring earlier in the season (roughly 0.09 days earlier per year on average; p < 0.01). Here are bivariate regression results supporting these findings:

<table style="text-align:center"><tr><td colspan="4" style="border-bottom: 1px solid black"></td></tr><tr><td style="text-align:left"></td><td colspan="3"><em>Dependent variable:</em></td></tr>
<tr><td></td><td colspan="3" style="border-bottom: 1px solid black"></td></tr>
<tr><td style="text-align:left"></td><td>Days of Ice Cover</td><td>Ice Off Day of Season</td><td>Ice On Day of Season</td></tr>
<tr><td style="text-align:left"></td><td>(1)</td><td>(2)</td><td>(3)</td></tr>
<tr><td colspan="4" style="border-bottom: 1px solid black"></td></tr><tr><td style="text-align:left">Trend</td><td>-0.179<sup>***</sup></td><td>-0.091<sup>***</sup></td><td>0.088<sup>***</sup></td></tr>
<tr><td style="text-align:left"></td><td>(0.028)</td><td>(0.018)</td><td>(0.018)</td></tr>
<tr><td style="text-align:left"></td><td></td><td></td><td></td></tr>
<tr><td style="text-align:left">Constant</td><td>117.489<sup>***</sup></td><td>160.467<sup>***</sup></td><td>43.225<sup>***</sup></td></tr>
<tr><td style="text-align:left"></td><td>(2.613)</td><td>(1.701)</td><td>(1.704)</td></tr>
<tr><td style="text-align:left"></td><td></td><td></td><td></td></tr>
<tr><td colspan="4" style="border-bottom: 1px solid black"></td></tr><tr><td style="text-align:left">Observations</td><td>163</td><td>163</td><td>163</td></tr>
<tr><td style="text-align:left">R<sup>2</sup></td><td>0.203</td><td>0.135</td><td>0.127</td></tr>
<tr><td style="text-align:left">Residual Std. Error (df = 161)</td><td>16.754</td><td>10.908</td><td>10.927</td></tr>
<tr><td style="text-align:left">F Statistic (df = 1; 161)</td><td>41.066<sup>***</sup></td><td>25.023<sup>***</sup></td><td>23.345<sup>***</sup></td></tr>
<tr><td colspan="4" style="border-bottom: 1px solid black"></td></tr><tr><td colspan="4" style="text-align:right"><sup>*</sup>p<0.1; <sup>**</sup>p<0.05; <sup>***</sup>p<0.01</td></tr>
</table>

Note that Ice On / Ice Off "Day of Season" are defined as the number of days _after_ November 1st that Ice On / Ice Off occured so that the negative coefficient in model (2) means that Ice Off occured earlier in the season, while the positive coefficient in model (3) means that Ice On occurred later.

### Data Preparation Details

Data for this analysis was pulled from [here](https://docs.google.com/spreadsheets/d/1_cYXBTsv5pzXj-BYuGQIFAQHiPEq4jZYCeJuhj3kg5w/edit) and was aggregated by "Season" (i.e. "Start Year"). Dates for Ice On and Ice Off were computed manually for each season based on the earliest/last date of reported ice cover respectively. "Days of Ice Cover" was computed manually as the difference between the derived Ice On and Ice Off dates. This derived field mostly matches the "Days" field of the original dataset, though deviates somewhat in cases where the Lake was opened / closed multiple times in a season. Note that the analysis excludes the seasons 1852-1854, as the data for these years were incomplete. All code for this analysis and visualization is available in the github for this blog post [here](https://github.com/Fossj117/fossj117.github.io) (see the `_code` folder).

Please note that visualizations presented here were inspired by similar plots found in Magee et al. (2016).

### References

Magee, M., Wu, C., Robertson, D., Lathrop, R., & Hamilton, D. (2016). Trends and abrupt changes in 104 years of ice cover and water temperature in a dimictic lake in response to air temperature, wind speed, and water clarity drivers. Hydrology and Earth System Sciences, 20(5), 1681-1702.

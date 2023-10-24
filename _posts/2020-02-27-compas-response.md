---
layout: post 
title: "Response to 'How we analyzed the COMPAS recidivism algorithm' (Larson et al.)" 
date: 2020-02-20
latex: true 
mathjax: true
comments: true
---

## Introduction

In this essay, I will discuss the article “[How we analyzed the COMPAS recidivism algorithm](https://www.propublica.org/article/how-we-analyzed-the-compas-recidivism-algorithm)” by Larson, Mattu, Kirchner & Angwin (2016). I will first summarize the approach and key findings of Larson et al. Subsequently, I will discuss some strengths and weaknesses of the article and its analysis. 

## Summary of Larson et al. (2016)

Broadly speaking, Larson et al. are interested in quantitatively testing whether a algorithmic risk assessment tool called COMPAS (short for Correctional Offender Management Profiling for Alternative Sanctions) is biased against Black defendants. COMPAS is an algorithmic tool that generates “risk scores” that are meant to reflect the likelihood that a defendant will recidivate (i.e. commit a crime), conditional on being released. According to the companion ProPublica article (Angwin et al. 2016), risk assessment tools like COMPAS are increasingly used to inform decisions in various parts of the criminal justice system, from assigning bond amounts to making decisions about parole and sentencing. Given this prevalence, along with the large extant racial disparities in the US criminal justice system, it is clearly crucial to understand whether COMPAS and related tools are biased against particular demographic groups (and Black defendants in particular). 

To investigate COMPAS, Larson et al. use open records laws to collect data on COMPAS predictions made on a sample of real defendants in Broward County, FL during 2013 and 2014. Defendants in this sample were scored by COMPAS in the course of decisions about whether they should be detained following a pretrial hearing. Each defendant received a score from one to ten, with a score of ten reflecting the highest risk of recidivism (note: COMPAS bins these raw scores into Low/Medium/High). Larson et al. merge these risk scores with publicly--available crime data and construct “ground truth” measures of recidivism, and also measures of defendant race as categorized by Broward County. The basic idea of the analysis is then to examine whether the COMPAS risk predictions in fact predict subsequent crime, and whether this accuracy varies systematically by race. To this end, the Larson et al. analysis presents three main pieces of quantitative evidence. 

First, Larson et al. ask whether COMPAS’ risk scores are associated with race overall. Examining marginal distributions of scores for Black vs. white defendants, Larson et al. show that the answer is clearly yes; for example: Black defendants are substantially more likely than white defendants to be classified as “high” risk. Further, Larson et al. show in a regression setup that this correlation is robust to the inclusion of basic controls for criminal history, age, and gender which confound the basic race comparison. 

Second, Larson et al. aim to test whether the COMPAS algorithm’s overall accuracy is in line with creator Northpointe’s claims. For this analysis they use a Cox proportional hazards model (apparently replicating Northpointe’s analysis strategy). The basic finding of this analysis is that the model’s predictive accuracy overall seems to be roughly in line with Northpointe’s claims (Larson et al. report an overall concordance of ~64% vs. Northpointe’s 68%). Larson et al. also present a version of the Cox model with race*score interactions and note that the Black*high coefficient is “almost statistically significant” (p=0.057), which they interpret as evidence of disparate predictive performance by race. 

Third and finally, Larson et al. more directly compare COMPAS’s predictive performance for Black vs. white defendants by constructing two-way contingency tables, and computing binary classification accuracy measures. The key finding here (and perhaps from the analysis as a whole) is that, although COMPAS’s overall classification accuracy is similar for Black vs. white defendants, the *types of mistakes* that the model makes differ substantially across groups. In particular, *conditional on not recidivating*, Black defendants were much more likely than white defendants to be (incorrectly) classified as “high” risk (i.e. likely to recidivate). In other words, the false positive rate was much higher for Black defendants than for white defendants (~45% vs. ~23%). Likewise, *conditional on eventually recidivating*, white defendants were more likely than Black defendants to be (incorrectly) classified as “low” risk (i.e. not likely to recidivate). In other words, the false negative rate was higher for white than for Black defendants (~47% vs. ~28%). Intuitively, these findings suggest that the COMPAS algorithm is comparatively “too aggressive” in assigning “high risk” labels to Black defendants (and comparatively “too conservative” for white defendants), which Larson et al conclude is evidence that COMPAS is biased against Black defendants. 

## Strenghts and Weaknesses of Larson et al. (2016)

Overall, the Larson et al. analysis has both strengths and limitations. On the one hand, as a piece of data journalism, I think that the article is largely successful. Even if the methods are imperfect (and I will discuss a number of concerns below), Larson et al. are right to draw attention to the question of racial bias in risk assessment tools, and have no doubt had a substantial impact in bringing more attention to this concern (and related issues) in academic, public, and policy conversations. Arguably, this is exactly what journalism is supposed to do. Further, compared to the average piece of journalism, Larson et al. do an impressive job of collecting important data and using it to (attempt to) make rigorous, transparent and falsifiable claims. 

However, on the other hand, understood as a pure piece of data analysis or social science, Larson et al. has clear limitations that have been highlighted in a range of critical follow-on work by academic computer scientists and economists. I now summarize three strands of this critical response that I find interesting and/or persuasive.

First, a narrow but important line of criticism highlights issues with Larson et al.’s choice of “ground truth” data. The issue here is that Larson et al.’s outcome data is collected from a setting where the COMPAS risk scores are being used to (in part) determine these very outcomes. If defendants with different risk scores are assigned to different sentencing regimes, and these different sentencing regimes affect the probability of recidivating, then it is difficult to disentangle accuracy from the algorithm’s effect on outcomes itself. We would really like to assess the algorithm’s accuracy against the propensity to commit a crime at the time the risk score was calculated, but we do not observe this, and the observed recidivism rate is not the same thing (Doleac & Stevenson 2016). While I take this criticism seriously, it’s also not immediately obvious what direction or to what extent this concern would bias Larson et al.’s results. However, Cowgill (2018) uses a regression discontinuity design to show that COMPAS scores do seem to have had a causal effect on criminal proceedings and recidivism in this setting, and so this does seem to be a valid concern. 

Second, supposing that we take Larson et al.’s data as basically correct, a perhaps deeper line of criticism questions their choice to focus on disparate false positive and false negative rates as a key measures of fairness or bias. While similar false positive rates across groups does have some intuitive appeal as a basic group-level fairness requirement (why should non-risky Black defendants be systematically assessed as being higher risk?), other approaches are also viable. For example, a natural alternative fairness requirement would be to require that rates of positive predictive value should match across groups — in other words, *conditional on getting a certain risk score*, the probability of recidivating should be the same across groups. This approach also has intuitive appeal—we would likely be concerned if we found that Black defendants labeled “high risk” were substantially less likely to recidivate than “high risk” white defendants. As discussed in a response by Feller et al. (2016), this fairness measure is the one touted by Northpointe (Dieterich et al. 2016), and indeed is largely satisfied by COMPAS (as Larson et al. also find). Importantly, as highlighted by the Feller et al. response (and demonstrated more formally by Kleinberg et al. 2016 for plausible scenarios), these two notions of fairness are fundamentally in tension, at least in a setting where there is disparity between groups in overall rates of recidivism. That is, if overall rates of recidivism differ and we enforce parity in in positive predictive value across groups, then we will necessarily have disparity in false positive rates (as Feller et al. explain). 

A third and final line of criticism questions whether it is helpful think about an algorithm as being “biased” in a vacuum in the first place, or whether it is more useful to think in counterfactual terms--i.e. as biased *compared to something*. As highlighted by Cowgill & Tucker (2017), a biased algorithm could still yield equity improvements if it is less biased than the status quo process (i.e. judges making decisions without algorithmic aid). This perspective also emphasizes that, in practice, the equity consequences of a risk assessment tool like COMPAS will depend crucially on how it interacts with the *human* judgements and biases of judges and parole boards. For example, the introduction of even a wholly “unbiased” risk assessment tool could exacerbate disparities if there is biased non-compliance by judges (e.g. “high” risk scores are used to justify harsher sentencing for Black but not white defendants). Likewise, assessment tools could have little impact on bias if their impact on judge decisions is low overall. In general, a range of interactions between human and algorithm are ex ante possible. A handful of recent papers seem to be empirically evaluating risk assessment tools in particular from this perspective (e.g. Stevenson & Doleac, 2019, Albright 2019). 

## Conclusion

Where does this all leave us? Although it is beyond the scope of this essay, there is an interesting question about how we ought to mediate competing perspectives (even technical perspectives) on questions like algorithmic bias. For example, considering the competing bias measures outlined above which are evidently in tension -- who should get to decide which of these measures prevails? Is it technical experts? 

## References 

Albright, Alex. "If You Give a Judge a Risk Score: Evidence from Kentucky Bail Decisions. The John M." Olin Center for Law, Economics, and Business Fellows’ Discussion Paper Series 85 (2019).

Angwin, Julia, et al. "Machine bias." ProPublica, May 23 (2016): 2016.

Cowgill, Bo. “The impact of algorithms on judicial discretion: Evidence from regression discontinuities”. Technical Report. Working paper (2018).

Cowgill, Bo, and Catherine Tucker. "Algorithmic bias: A counterfactual perspective." NSF Trustworthy Algorithms (2017).

Dieterich, William, Christina Mendoza, and Tim Brennan. "COMPAS risk scales: Demonstrating accuracy equity and predictive parity." Northpointe Inc (2016).

Doleac, Jennifer L., and Megan Stevenson. "Are Criminal Risk Assessment Scores Racist?." Brookings, August 22 (2016).

Feller, Avi, et al. "A computer program used for bail and sentencing decisions was labeled biased against blacks. It’s actually not that clear." The Washington Post (2016).

Kleinberg, Jon, Sendhil Mullainathan, and Manish Raghavan. "Inherent trade-offs in the fair determination of risk scores." arXiv preprint arXiv:1609.05807 (2016).

Larson, Jeff, et al. "How we analyzed the COMPAS recidivism algorithm." ProPublica (5 2016) 9 (2016).

Stevenson, Megan T., and Jennifer L. Doleac. "Algorithmic Risk Assessment in the Hands of Humans." Available at SSRN (2019).


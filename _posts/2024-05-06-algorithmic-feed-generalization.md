---
layout: post
title: "Algorithmic Feed Theoretical Modeling - Part 2"
date: 2024-05-06
latex: true
mathjax: true
comments: true
tag: ["econ", "draft"]
---

In this post, I am going to try to build on the theory model I outlined in [this]({% post_url 2024-04-23-algorithmic-feed-theory %}) previous post. The piece I want to try adding/tweaking to the model today is the viewer's choice to "subscribe" to or "follow" a creator, and the way that that changes as algorithmic prediction improves. 

## Intuition

What is the intuition that I want to capture? Intuitively, my thoughts are as follows: 

* Viewers make the decision about who to subscribe to in view of their expectations about how it will impact the "quality" of their feed.
    * When the platform's ability to predict quality is low, viewers have an incentive to be cautious in their subscription decisions -- if they subscribe to a creator who is distant from their interests, they are likely to get served content that they don't actually like (i.e. feed quality will degrade).
    * However, as the platform's ability to predict quality increases, viewers are more willing to subscribe "liberally", since they know that the platform will only serve them content from a creator that is "distant" in horizontal differentiation terms if it is high quality / a good match for the viewer.
        * More generally, as prediction quality increases, the "following" decision has less of an impact on the substance of a viewer's feed, since the platform always just serves the highest quality video to a viewer. 
* An interesting tradeoff that I am wondering about here is: to the extent that the above mechanism is present, I guess that the informativeness of the "following" signal should degrade for the platform as prediction quality increases.

## Setup

I am hoping I can reuse at least some ideas from my previous post. Per above, I now want to focus on the "subscription" stage to the game; so I have something like: 

1. Viewers arrive and decide which creator(s) to follow. 
2. Creators create pieces of content (with uncertain vertical quality)
3. Platform curates the "feed" for the viewer -- i.e. chooses a single piece of content to serve them. 
4. Viewers (decide whether) to consume the content. 

Again, I will try to do the simplest setup possible that addresses my set of intuitions. 

### Creators

As before, assume that there are two horizontally differentiated and indexed by $j \in \\{0,1\\}$, reflecting their locations on a horizontal line. Assume for now that creators will each emit a single piece of content, $c_j$, with some uncertain vertical quality $\epsilon_j$.

To maximally simplify, suppose that $\epsilon_j \in \\{0, \epsilon_H\\}$ where $\epsilon_H > 0$ is thought of as "high" quality. Suppose that creator $j$ produces a high quality piece of content with probability $p_j$. To start, let's assume $p_0 = p_1 := p_H$. 

### Viewers

As before, I want viewers to have horizontal and vertical preferences. To simplify my setup further, let's assume for now that there are only two types of viewers; let these types be indexed by $i \in \\{0,1\\}$. Let $u_i(.)$ be the utility function for consumer $i$. Assume that: 

$$u_i(c_j) :=  \epsilon_j - |j-i|$$

So intuitively, a viewer of type $i$ will prefer content from creator $j$ with $j=i$; however, this preference can possibly be overcome by the content quality $\epsilon_j$. I suppose it will be interesting to assume that $\epsilon_H > 1$, so that viewer $i$ will prefer high quality content from creator $j\neq i$ over low-quality content from creator $j=i$. 

Assume that viewers have an outside option with utility normalized to zero. Note that $u_1(c_0; \epsilon_0 = 0) = u_0(c_1; \epsilon_1 = 0) < 0$, so viewer $i$ will prefer the outside option to consuming low quality content from creator $i \neq j$. 

### Platform

As before, assume the platform wants to curate the feed to maximize the expected number of content views. 

## The Game

Contra my previous setup, the game is now more of a signaling game type setup. I think I want something like this: 

* Nature chooses the viewer's type as 1 or 0. Suppose that both types are equally likely. 
* Viewers choose between the following options: 
    * Subscribe to creator 0 
    * Subscribe to creator 1 
    * Subscribe to both creators
* Nature chooses the quality $\epsilon_j$ of each creator's content. 
* Platform decides whether to serve viewer content $c_0$ or $c_1$. 
* Viewer observes $\epsilon_j$ of served content and decides whether to consume. 

Assume that: 
* The platform does not know the type of the viewer. 
* The platform does not directly observe the quality $\epsilon_j$. Instead, they observe an informative signal $\delta_j \in \\{0,1\\}$ with the property that: $P(\delta_j = \epsilon_j) = \theta$, where $0.5 \leq \theta \leq 1$. Intuitively, I think of $\theta$ as reflecting the quality of the platform's prediction technology: 
    * If $\theta = 0.5$, the platform has no information about content quality. 
    * If $\theta = 1$, the platform has perfect information about content quality. 

As before, I will be interested in how the equilibria of the game change as $\theta$ (prediction quality) increases. 

Here is a rough sketch of the extensive form of this game, where I'm leaving out some symmetric parts of the tree: 

<p>
<center>
<img alt="1" align="center" src="/figs/2024-05-06-algorithmic-feed-generalization/extensive_form.png" width="85%">
</center>
</p>

The creator (nature) node reflects the different cases of low and high quality content that could be produced by the creators with different probabilities (I wrote them backwards in the drawing): 

* LL = both produce low quality with probability $(1-p_H)^2$
* LH / HL = one produces low, other high with probability $p_H(1-p_H)$
* HH = both produce high quality with probability $p_H$. 

This drawing also doesn't reflect the partial information that the platform has about content quality. I guess strictly we would draw that as the nature node having two steps -- the acutal quality $\epsilon_j$ of the content is drawn, and then the platform signals $\delta_j$ are drawn with probabilities given by $\theta$. Then the platform chooses to serve $C_1$ or $C_2$ based on the pair of signals they observe. 

The payoffs of the game are implied in the above discussion. The viewers get payoff $u_i(c_j)$ where $i$ is their type and $c_j$ is the content that the platform chooses. For simplicity, assume the platform gets payoff 1 if the viewer consumes the content that they are served, and gets payoff 0 otherwise. Recall that viewer $i$ views the content $j$ iff $u_i(c_j) > 0$. 

## Solution

The solution concept for this game should be Perfect Bayesian Equilibrium (PBE). While the game has a lot of nodes, there is also a lot of symmetry so hopefully it should be clear how to solve. In the current setup, it is basically just a standard signaling game with the twists that: 

1. Viewers (signalers) have *three* choices (S1, S2 or both) rather than the standard two. 
2. Platform (receiver of signal) has uncertainty about which response is best for each viewer type.


---
layout: post
title: "Network Effects & Platform Trust"
date: 2024-05-04
latex: true
mathjax: true
tag: ["econ", "draft"]
---

This post is based on a discussion with [Daniel](https://sites.google.com/view/danielyue/home). 

Suppose that $n=2$ complementors participate in a platform market with one-sided network effects. Let the complementors be indexed by $i \in \\{1,2\\}$. 

The platform facilitates these network effects through ownership of some information or technological asset/product and charges baseline price $p$.

Complementors have the choice to (1) "Stay" with the incumbent platform or (2) "Defect" to a new platform, possibly of their own making. Suppose defecting has some cost $c > 0$. 

Suppose that the incubment platform's price is *uncertain* to the platform participants -- in particular, there is some chance that the platform is going to increase price / degrade quality, affecting complementor payoffs. In particular, suppose that there is some probability $q$ that the price will increase from $p$ to $p'$. 

Intuitively, I am thiniking of the probability $q$ as being a subjective probability from the perspective of the complementors -- it reflects their level of "trust" in the platform. For now I'll assume there is a common $q$ for both complementors. 

The last piece of the setup is that there are positive one-sided network effects, so the complementors get some additional benefit if they both choose to be on the same platform (i.e. both participate or both defect). Let this added benefit be $b>0$. 

With all this in mind, let's write down the expected payoff matrix for complementors. I will assume that complementor utility is linearly decreasing in price. This implies the following payoff matrix: 

<title>Payoff matrix</title>
<table border="1">
  <tr>
    <th></th>
    <th>Stay</th>
    <th>Defect</th>
  </tr>
  <tr>
    <th>Stay</th>
    <td>$b-(1-q)p - qp', b-(1-q)p - qp'$</td>
    <td>$-(1-q)p - qp', -c$</td>
  </tr>
  <tr>
    <th>Defect</th>
    <td>$-c,-(1-q)p - qp'$</td>
    <td>$b-c, b-c$</td>
  </tr>
</table>

If we define $f(q) = (1-q)p - qp'$ to be the expected price given probability $q$ of a price increase, then we can write more simply: 

<table border="1">
  <tr>
    <th></th>
    <th>Stay</th>
    <th>Defect</th>
  </tr>
  <tr>
    <th>Stay</th>
    <td>$b-f(q), b-f(q)$</td>
    <td>$-f(q), -c$</td>
  </tr>
  <tr>
    <th>Defect</th>
    <td>$-c,-f(q)$</td>
    <td>$b-c, b-c$</td>
  </tr>
</table>

What are the pure-strategy equilibria of this simple game?

First, suppose, the column player plays "Stay". Then the row player chooses between $b-f(q)$ and $-c$. So if $b-f(q) > -c$, then they will prefer "Stay", and (Stay, Stay) will be a NE by symmetry. We can rewrite this condition as: $f(q) < c+b$. 

Next, suppose the column player plays "Defect". Then, the row player chooses between $-f(q)$ (Stay) and $b-c$ (Defect). So if $b-c > -f(q)$, Defect will be preferred and (Defect, Defect) will be a NE. We can rewrite this condition as $f(q) > c-b$.

Note that $c-b < c+b$, so we have the following situation for pure strategy equilibria: 

<p>
<center>
<img alt="1" align="center" src="/figs/2024-05-04-network-effects-platform-trust/NE_Drawing.png" width="85%">
</center>
</p>

Can (Stay, Defect) and (Defect, Stay) ever be NE? By above, BR(Stay) = Defect if $f(q) > c+b$ and BR(Defect) = Stay if $f(q) < c-b$; since these can never be simultaneously true, (Stay, Defect) and (Defect, Stay) cannot be NE. 

Note that $df/dq > 0$ (expected price increases in probability of a price increase); so in general, as platform trust decreases and $q$ increases, we move from a regime where (Stay, Stay) is the only pure strategy equlibrium, to a regime where (Defect, Defect) is the only pure strategy equilibrium.

For completeness, let's check if there are any mixed strategy equilibria in the game. Suppose the column player plays "Stay" with probablity $m$ and "Defect" with probability $1-m$. Then the expected payoffs for the row player are: 

* $E[Stay] = m(b-f(q)) - (1-m)f(q) = mb-mf(q)-f(q)+mf(q) = mb-f(q)$
* $E[Defect] = m(-c) + (1-m)(b-c) = -mc + b-c -mb+mc = b-mb-c$

For the row player to be mixing in equilibrium, we must have 

$$E[Stay]=E[Defect] \iff mb-f(q) = b-mb-c$$

This gives:

$$m^* := \frac{f(q)+b-c}{2b}$$

So by symmetry there is a mixed strategy NE where both players play "Stay" with this probability $m^\*$ if $ 0 < m^\* < 1$. When is this the case? 

$$\frac{f(q)+b-c}{2b} < 1$$

$$\iff \frac{f(q)-b-c}{2b} < 0$$

$$\iff f(q)-(b+c) < 0$$

$$\iff f(q) < b+c$$

Similarly, $m^\* >0 \iff f(q)+b-c > 0 \iff f(q) > c-b$.

So updating our picture, this game has a symmetric mixed strategy equilibrium when $f(q)$ is between $c-b$ and $c+b$: 

<p>
<center>
<img alt="1" align="center" src="/figs/2024-05-04-network-effects-platform-trust/NE_drawing_mix.png" width="85%">
</center>
</p>

To summarize, none of this is too surprising, and I am not sure if the model is very interesting yet. It does kind of capture the basic but maybe obvious intuition that as "trust" in the platform degrades (expected price $f(q)$ increases), we move from a regime where all participants staying is the only NE, to one where defecting becomes possible and eventually inevitable in equilbrium. 

There are various ways that this model could be complicated; I am not sure if or which of these are interesting. But some possibilities: 
* Do we want to endogenize the platform's action / price-setting?
* Do we want to introduce "voice" here / merge this with the Gans model somehow? 
* Is it interesting / relevant if the complementors have possibly asymmetric beliefs about $q$?
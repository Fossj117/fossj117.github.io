---
layout: post
title: Arrow Replacement Effect
date: 2020-06-05
latex: true
mathjax: true
comments: true
tag: ["econ"]
---

## The Arrow replacement effect

Arrow (1962) introduces at least two key ideas that would become important in the subsequent literature on the economics of innovation. The first idea is that “ideas” (or knowledge) and their production have some key properties that ensure that competitive markets will not achieve an optimal allocation of resources to idea production (in particular there will be underproduction of ideas).

The second key idea that Arrow (1962) establishes is the so-called “Arrow replacement effect”. The Arrow replacement idea is important because it is framed as one of the classical answers to the question of how market structure affects innovation. In particular, the Arrow idea seems to be identified as one “pole” of the competition / innovation debate — namely, as a key mechanism explaining why product market competition encourages innovation (as Shapiro 2012 summarizes). Per the Shapiro (2012) framing, Schumpeter (1942) classically forms the other “pole” of this debate — i.e. the opposing view that actually (the prospect of) market power and monopoly profits is what spurs innovation (or that larger firms are otherwise a better home for innovation).

So what is the Arrow replacement effect? The basic idea of the replacement effect is that a monopolist has less incentive to innovate than a competitive firm, due to the monopolist’s financial interest in the status quo. As Arrow puts it: “The preinvention monopoly power acts as a strong disincentive to further innovation”. Indeed, in Arrow’s setup, for any given level of post-invention (“ex post”) profits, the incentive to innovate will be decreasing in pre-invention (or “ex ante”) profits.

### The Formal Treatment

A clean version of the Arrow model is outlined in the Tirole (1988) IO textbook (which also, apparently, coined the “replacement” effect term), so I will walk through this version. The setup of the model is a static setting in which we abstract away form any strategic interactions; the model aims to consider how the incentives for production of a cost-reducing innovation vary with the initial market structure (and also compare to the social value). In particular, let the innovation reduce the constant marginal cost of production of some good from $c$ to $c'$ and suppose market demand is $D(p)$. What is the value of the innovation to the social planner, monopolist or competitive firm?

**Social planner**. The planner will set price equal to marginal cost before and after the innovation. So the net social surplus of the innovation is equal to:

$$V^s = \int_{c'}^cD(x)dx$$

**Monopolist**. The assumption here is that there is a monopolist in the product market and also in R&D (so that importantly there is no threat of outside entry). Let mbe the monopoly profits and let pm(c)be the monopoly price given marginal cost $c$. How do profits change with $c$?

$$\frac{d\pi^m}{dc}=\frac{d}{dc}[(p(c)-c)D(p(c))] = \frac{\partial\pi^m}{\partial p}\frac{dp^m}{dc} + \frac{\partial\pi^m}{\partial c} =\frac{\partial\pi^m}{\partial c}=-D(p^m(c))$$

because of the envelope theorem (i.e. $\frac{\partial\pi^m}{\partial p}=0$ at the optimum). So the value of the process innovation for the monopolist is:

$$v^m=\pi^m(c')-\pi^m(c)=\int_{c'}^c(-\frac{d\pi^m}{dc}dx = \int_{c'}^c D(p^m(x))dx.$$

Comparing $v^m$ and $v^s$ we have that $p^m(c) > c$ at all $c$ and so $D(p^m(c))<D(c)$ for all $c$ and thus $v^s > v^m$. Hence, we expect the monopolist to underinvest relative to the social planner.

**Competition**. Now consider a competitive case where we initially have a large number of firms producing homogenous goods with identical marginal costs $c$. The firms are in Bertrand competition (i.e. they are competing in price), and so the market price is just cand everyone earns zero profits. Per above, if a firm innovates, their cost is reduced to $c'$. There are two cases:

- **“Drastic” innovation**: $p^m(c') \leq c$. In this case, the optimal monopoly price at the ex post lower marginal cost is less than ex ante cost and market price, and so the innovator will simply set the monopoly price and capture the whole market. Intuitively, a “drastic” innovation makes the previous technology irrelevant.

- **Minor (or “nondrastic”) innovation**: $p^m(c')>c$. In this case, the innovation is not so large (i.e. does not reduce costs enough) that the previous technology is irrelevant—the innovator is constrained to charge no more than psince there is competitive supply at this price. We assume that the innovator’s ex post profit function is strictly concave and so she will charge $p=c-\varepsilon$ to capture the whole market (i.e. effectively $p$ for small epsilon).

How do the incentives for innovation look in these two cases? In the nondrastic case, the innovator’s ex post profit will be $v^c=(c-c')D(c)$. But note that $c < p^m(c') \leq p^m(x)$ by assumption for all $x \geq c'$, and hence $D(c)<D(p^m(x))$ for $x\leq c$. And thus:

$$v^m=\int_{c'}^c D(p^m(c))dx < \int_{c'}^c D(c)dx =(c-c')D(c) =v^c,$$

and so incentives to innovate will be higher in the competitive setting in this case. However, $D(c) < D(x)$for all $x<c$, and so we will have $v^c<v^s$ and hence innovation incentives are still less than the social optimum.

Likewise, in the drastic case, the ex-post profit will just be:

$$v^c=(p^m(c')-c')D(p^m(c'))=\pi^m(c') > \pi^m(c')-\pi^m(c)=v^m.$$

In other words, the ex post profits are the same as in the monopoly case; however, there are now no ex ante profits and so the innovation incentive is clearly higher. Hence, in either case we have $v^m<v^c$(and both always less than $v^s$, though I didn’t show this in the drastic case). This is the Arrow replacement idea.

### Relevance and Limitations

To what extent is the Arrow replacement idea actually relevant to the world? Gilbert (2006) usefully discusses some of the key assumptions of the Arrow setup. A few key points I take from this discussion:

- **Arrow (1962) assumes that there is only a single successful inventor**. If we relaxed this in, say, the competitive setting, then I suppose that the results will completely reverse. If a competitor can immediately copy your innovation, then things will go right back to zero profit Bertrand, and so there will be no incentive to innovate in the competitive setting. In general, this suggests that Arrow considerations are more relevant in cases where there is relatively strong IP protection.

- **Arrow (1962) only considers process innovations (i.e. reducing marginal costs) and not product innovations (i.e. introducing a new product)**. Gilbert (2006) points out that in the product innovation case, a replacement effect is still at play (since a competitive firms ex ante profits can be no greater than a monopolist’s), but that it is only part of the story. In particular, for a monopolist, introducing a new product can facilitate price discrimination and allow the monopolist to extract more surplus from consumers. This means that a monopolist producing both a new and old products might be able to make more ex post profits than a competitive firm offering the new product in an environment where the old product is still competitively available. This could offset the replacement effect. This said, Gilbert (2006) explains that the basic Arrow result can be recovered in the product innovation case if we impose a stronger assumption that the new product makes the old product obsolete.

- **Arrow (1962) assumes that the monopolist is entirely shielded from competition**. That is, there is no chance in the monopoly case that some external entrant firm could introduce the innovation and capture the monopoly position. This rules out the possibility of Gilbert & Newbury (1982) style preemption concerns or what Tirole (1988) calls efficiency effects. I should write more about this later, but the basic intuition of efficiency effects is essentially the reverse of Arrow: if some disruptive innovation is coming down the pike (or e.g. already exists but can be licensed/purchased), then the monopolist actually has greater incentive than a competitive firm to acquire/develop it, since the monopolist has “more to lose” from the innovation reaching market. Arrow assumes this mechanism away.

### References

Arrow, Kenneth. 1962. “Economic Welfare and the Allocation of Resources for Invention.” In The Rate and Direction of Inventive Activity: Economic and Social Factors, pp. 609-625. Princeton, NJ: Princeton University Press.

Gilbert, Richard. 2006. “Looking for Mr. Schumpeter: Where Are We in the Competition-Innovation Debate?” Innovation Policy and the Economy 6: 159-215.

Gilbert, Richard, and David
Newbery. 1982. “Preemptive Patenting and the Persistence of Monopoly.” American Economic Review 72:514–26.

Schumpeter, Joseph. 1942. “The Process of Creative Destruction.” Chapter VII, pp. 81-86 in Capitalism, S ocialism, and Democracy. New York, NY: Harper & Row.

Tirole, J. (1988). The theory of industrial organization. MIT press.

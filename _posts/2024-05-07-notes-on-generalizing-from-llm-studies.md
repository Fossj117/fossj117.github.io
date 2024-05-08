---
layout: post
title: "On generalizing to humans from empirical studies of LLMs"
date: 2024-05-06
latex: true
mathjax: true
comments: true
tag: ["econ", "llm"]
---

## Setup

Recently, there has been a lot of discussion about the role of LLMs in social science research. I am part of the [expected parrot](https://www.expectedparrot.com/) discord channel, where a handful of researchers in this space hang out. In that setting, a conversation started about the logic of generalizing from studies of LLM agents to human agents. There is a lot to consider here; however, in the course of the conversation, I wrote up an extended comment with a few thoughts that I thought would be worth preserving & sharing here for further consideration. This is far from my final thoughts on this, and I can imagine many further points and counterpoints here that I am not getting into. However, I think there are a few useful ideas here. 

Below is my comment reproduced in full. It was initially in response to someone raising a question about the viability of generalizing from LLM studies to humans.

## My Comments

I’ll bite here to continue the conversation. Mostly agree that these concerns are valid/important as far as drawing inferences about people directly from studies on LLM agents (vs. using them to augment research in other ways — e.g. survey imputation, hypothesis generation). 

Agree with [John](https://john-joseph-horton.com/) above that there are always important questions about generalizability in studies with humans — both to other populations, and to other settings. And we are never really sure whether an effect observed with one population in one setting will generalize to another. 

However per the previous point, it does seem much clearer how to think / reason about when generalizability is/is not plausible in studies with humans. For example, I can check how similar my study population is to the population I want to generalize to (on observable characteristics). I can also e.g. look for heterogeneous effects across observables within the population I do observe, and reweigh accordingly in my generalization if necessary. Yes, there will always be untestable assumptions in any generalization effort, but at least I can state them clearly and constrain them in the human case? And more fundamentally, I am generalizing to the same kind of thing (i.e. humans). 

By contrast, if I run a study with LLM agents, there’s always going to be this comparatively large ontological gap to overcome — I am doing a study on one type of thing (an LLM model) and trying to draw a conclusion about a different type of thing (human agents). And it’s just not as clear to me a priori why I should believe that that is possible. (Though maybe building a lot of empirical evidence that this generalizability does seem to work in practice can help address this?)

Another relative benefit of the human agents world is that my study can still teach us something new / relevant about the world in a lot of cases, even if nobody believes that my study generalizes to other contexts. I.e. in a lot of cases with humans we don’t claim much generalizability, but can still find the study useful if it is in e.g. a policy-relevant context 

One other comparison that comes to mind is medical studies in animals (e.g. mice) which are taken to tell us *something* about e.g. the effect of a treatment in humans even though mice and humans are very different categories of things. 

It seems useful to think about the conceptual argument for why mice studies are a reasonable thing to do. In terms of *a priori* arguments there, presumably the key points are that we can look and see the extent to which mice and humans share e.g. biological structures that are relevant to the mechanism of the effect we are studying -- i.e. humans / mice are different things, but are the same or similar in ways that are relevant to generalizability. 

Thinking more about the mouse case -- and its successes/limitations -- seems pretty interesting and useful here as a comparison point ([wiki](https://en.wikipedia.org/wiki/Laboratory_mouse#Limitations)). 

## Some Responses

There was some interesting follow-on discussion in the discord group about this topic. For example, [Jesse](https://jessecallahanbryant.com/) added some thoughts on the mouse analogy: 

> The claim I'd love thoughts on is that (for me) mice and humans are a part of a category of being that LLMs are not: life. further: mammalian life. This is a category of organized material that shares similar material components and natural histories even if the overall things (mice, humans, blue whale) are quite different. the generalizability between systems then isn't about the emergent thing but about the similarity between substructures. In my case, this was that mice and humans both have something called the amygdala which is built out of the same material tissues organized in a relatively similar fashion. The generalizability of the effects (in my case) bipolar drugs from mice to human amygdala seem to be quite theoretically sound because of biochemical theories that hold up quite clearly. that said, like some ungodly proportion of drugs that pass mice trials do not generalize to human systems at all. I'm just still struggling to understand clearly what the generalizability field is between LLMs and humans, like between mouse amygdala and human amygdala.

I agree with Jesse for the most part here.

An interesting and relevant follow-up question seems to be: to what extent is the logic of doing mouse studies (e.g. for new medical drugs) *actually* based on any sort of *a priori* consideration (i.e. the sharing of biological structures / evolutionary history) vs. the *a posteriori* (empirical) observation that mouse studies have historically been sufficiently predictive of human outcomes to be "worth it" given their lower cost/risk.

[John](https://john-joseph-horton.com/) made a similar kind of argument regarding LLM studies in the discord (and alluded [in his prior paper](https://arxiv.org/abs/2301.07543)); for example, even if we had no "principled" *a priori* reason why LLM results should generalize to humans, we might observe across a range of tests that this *does* seem to be the case and thus be convinced that experimenting with LLMs to generate hypotheses about humans is worthwhile from a cost-benefit perspective. In the same vein as mice studies, the goal here is not ever to generalize *directly* to human actors; instead, the goal is to generate / refine plausible hypotheses which can subsequently be validated on human actors.

Another related idea/question is the use of LLMs to explore *mechanisms*. This is also something that comes up in the context of mice studies, where the ability to manipulate more features of the environment & biology (I guess including doing ex post dissections etc.) makes it possible to dive deeper into understanding mechanisms of action than are directly difficult to observe/study in humans. 

It's an interesting question whether a similar logic applies in the case of LLMs. In one sense, it might seem that the answer is "no", given the fundamental ontological differences between LLMs and humans -- e.g. we (probably) wouldn't presume that digging into the pattern of weights & activations of an LLM teaches us much e.g. about human decision-making or psychology. 

However, at a higher level of abstraction, it does seem plausible that LLMs could help produce hypotheses about social mechanisms for some of the same reasons that mice studies do. For example, we can imagine that with LLM studies it is possible to experimentally vary all sorts of granular features of the environment or agent which are difficult or impossible to manipulate in human studies. Likewise, we can set up an LLM study to make any part of the decision process "observable" in a way that could present opportunities. 

Here I see an analogy with research in the economics of digitization. Digital markets have often been useful for researchers empirically because they allow us to observe or manipulate more granular features of the environment. [Another paper from John is relevant](https://john-joseph-horton.com/papers/minimum_wage.pdf) on this point. For my purposes, a key value-add of this paper is that it studies a policy intervention of general interest (minimum wage) in a context where it's possible to investigate a mechanism of interest (labor-labor substitution) that *could* be at play more broadly (and explain certain empirical results), but is otherwise hard to observe. The point of the paper is not to conclude that this mechanism must hold in all cases; however, this is a plausible hypothesis which is lent some credence by showing evidence that the mechanism does hold in a particular (digital) case. 

We can imagine that LLM studies could play a similar analytical role -- especially if there are sometimes plausible mechanisms that are otherwise difficult, costly, or impossible to investigate with real individuals. 
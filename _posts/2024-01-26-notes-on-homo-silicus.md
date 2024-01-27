---
layout: post
title: "Notes on Homo Silicus"
date: 2024-01-26
latex: true
mathjax: true
comments: true
tag: ["econ", "llm"]
---

## Introduction

Today I am reading through and taking some notes on [this](https://arxiv.org/abs/2301.07543) very interesting paper from [John Horton](https://john-joseph-horton.com/) about using LLMs as simulated economic agents. I have been interested in learning more about this emerging field for a while (and also following John's related [Emeritus](https://www.goemeritus.com/) project and [edsl python package](https://pypi.org/project/edsl/)), and today is the day. 

My main goal for today is to try to understand what this paper is up to conceptually, and also learn a bit more about the *edsl* package in particular. In the spirit of bloggin, I will be writing my notes here "live" as I read through the paper

## Homo Silicus Paper

The first few sentences of the *homo silicus* paper seem to give a clear articulation of the conceptual approach here. Here is the first, setup point: 

> Most economic research takes one of two forms: (a) “What would *homo economicus* do?” and b) “What did *homo sapiens* actually do?” The (a)-type research takes a maintained model of humans, homo economicus, and subjects it to various economic scenarios, endowed with different resources, preferences, information, etc., and then deducing behavior; this behavior can then be compared to the behavior of actual humans in (b)-type research.

Against this background, the conceptual intervention of the paper is then as follows (emphasis mine): 

> In this paper, I argue that newly developed large language models (LLM)—because of how they are trained and designed—**can be thought of as implicit computational models of humans—a homo silicus. These models can be used the same way economists use homo economicus: they can be given endowments, put in scenarios, and then their behavior can be explored**—though in the case of homo silicus, through computational simulation, not a mathematical deduction.

So the key conceptual point here is that we are going to use LLMs as a replacement for what Horton calls *homo economicus* -- i.e. the theoretical models that economists use to understand the world, and that in particular are used in economics research as a benchmark for making predictions that can be compared against *actual* behavior. 

Pausing here for a personal reflection: I guess one thing that the story being told so far elides is the fact that theoretical models of *homo economicus* (or really any scientific model) are also centrally relevant in creating understanding of how a particular research subject "works". Models are like little (but precisely-articulated) stories about what's going in a particular setting. And they're useful in part because human researchers understand stories -- they give us an answer to the question of "why" XYZ is happening in this setting. Another way to say this is that models help us (1) understand *mechanisms* as well as (2) *make predictions*. And replacing human-understandable economic models with large black box LLMs seems limited on point (1), though (to Horton's argument) potentially useful on (2). I imagine this may be addressed further later on in the paper. 

Horton goes on to address the question of why working with LLMs might be useful for understanding humans. He explains: 

> The core of the argument is that LLMs—by nature of their training and design—are (1) computational models of humans and (2) likely possess a great deal of latent social information

The ultimate argument for experimenting with LLMs is pragmatic: 

> ultimately, what will matter in practice is whether these AI experiments are practically valuable for generating insights.

Horton describes the value further a few pages later after describing the use of AI simulations of various experiments from the economic literature: 

> what is the value of these experiments? The most obvious use is to pilot experiments in silico first to gain insights. They could cheaply and easily explore the parameter space, test whether behaviors seem sensitive to the precise wording of various questions, and generate data that will “look like” the actual data.

And further (parens mine): 

> As insights are gained (from AI experiments), they could guide actual empirical work—or interesting effects could be captured in more traditional theory models. This use of simulation as an engine of discovery is similar to what many economists do when building a “toy model”–a tool not meant to be reality but rather a tool to help us think.

So per my concern above, Horton here seems to be suggesting the use of LLMs more as a tool to develop more traditional forms of theory and research. This makes sense to me, but is somewhat less ambitious of a claim than I initially understood. I.e. rather than proposing *homo silicus* as a full-on replacement for *homo economicus*, the idea is more to use *homo silicus* to inform better development of *homo economicus*, and/or its relationship to *homo sapiens* (i.e. "actual" economic actors). 

The paper next gets into a handful of conceptual issues that I find very interesting. There's a lot to think about here and I would like to revisit. One particularly interesting piece (section 2.3) is about concerns that *homo silicus* might be "performative" if used in economic research, simply regurgitating/parrotting behavior from economics textbooks in its training corpus.

Horton's response to this worry is as follows: 

>  But the fact it [the LLM model] does not “know” these theories is useful to us because it will not try to apply them. For example, it is clear GPT3 knows π and will recite it if asked for the answer in textbook language, yet it also does not know π or how to apply it in even simple real settings. Like students who have crammed for an exam, these models “know” things, but often do not apply that knowledge consistently to scenarios. This is useful because it makes this “performativity” critique less important. But even if it is a concern, we should avoid a textbook framing of questions.

I think I follow and agree with the argument Horton is making here, but I was also wondering if there is also a more “bite the bullet” type response to this line of critique, inspired by the STS / economic sociology literature which Horton cites via MacKenzie (2007). 

I spent [a while reading in this literature recently](https://jeffreyfossett.com/2023/05/01/sts-performativity-in-economics.html),and my understanding of their point is that real economic actors (i.e. *homo sapiens* in context of paper) also know about theoretical economic ideas and might sometimes use that knowledge in making economic decisions in various ways.

I’m not sure much that idea has been explored/tested in economics world; however, in the context of the *homo silicus* argument it seems relevant because ”being exposed to formal economic ideas” or “having read economics textbooks”(and having that potentially influence behavior sometimes) are actually both properties that *homo silicus* and *homo sapiens* share, but which *homo economicus* generally lacks. And so that actually seems like potentially a point in favor of working with *homo silicus* over homo economicus if the goal is to understand real people.

In the next piece of the paper, Horton shows examples of simulating various economic experiments using LLMs. To better understand this piece, I'm going to shift gears and try messing around with `edsl`, the new Python package he's put out with [Emeritus](https://www.goemeritus.com/) for running these kinds of tests. 

## Understanding `edsl`

In this section, I want to start exploring the `edsl` package. I am going to implement a little test inspired by [this](https://jeffreyfossett.com/2024/01/05/gpt-experiments.html) recent joke post and based on the tutorial outlined [here](https://examples.goemeritus.com/example_agent/#Base-agent). Here is the code: 

{% highlight python %}
import edsl
from edsl.agents import Agent
from edsl.questions import QuestionFreeText

# Make some political alignments
# (These were generated by chatGPT)
political_alignments = [
    "Conservative",
    "Liberal",
    "Progressive",
    "Socialist",
    "Libertarian",
    "Moderate",
    "Populist",
    "Green",
    "Nationalist",
    "Neoconservative",
    "Tea Party",
    "Democratic Socialist",
    "Anarchist",
    "Centrist",
    "Feminist",
    "Paleoconservative",
    "Alt-Right",
    "Communist",
    "Isolationist",
    "Technocrat"
]

# Make some agents with these alignments
agents = [Agent(traits = {'politics':p}) for p in political_alignments]

q = QuestionFreeText(
    question_name = "favorite_color",
    question_text = "What is the color that best represents your political attitude? Please respond with just a hex code corresponding to that color."
)

result = q.by(agents).run()
{% endhighlight %}

The `result` is a list with one record for each of the 20 agents. Each record looks something like this (which also adds some more clarity on what's happening behind the scenes, including the full prompt): 

{% highlight python %}
Result(agent={'politics': 'Conservative'}, scenario={}, model=LanguageModelOpenAIThreeFiveTurbo(model = 'gpt-3.5-turbo', parameters={'temperature': 0.5, 'max_tokens': 1000, 'top_p': 1, 'frequency_penalty': 0, 'presence_penalty': 0, 'use_cache': True}), iteration=0, answer={'favorite_color': '#FF0000'}, prompt={'favorite_color_user_prompt': Prompt(text='You are being asked the following question: What is the color that best represents your political attitude? Please respond with just a hex code corresponding to that color.
Return a valid JSON formatted like this:
{"answer": "<put free text answer here>"}'), 'favorite_color_system_prompt': Prompt(text='You are playing the role of a human answering survey questions.
Do not break character.
You are an agent with the following persona:
{'politics': 'Conservative'}')}
{% endhighlight %}

In the middle there, we can see our question answer. Let's visualize what our whole set of results look like! Here's some python code for making a nice table (via ChatGPT): 

{% highlight python %}
def create_html_table(name_color_pairs):
    html = '<table border="1">'

    # Adding table headers
    html += '<tr><th>Name</th><th>Color</th></tr>'

    # Looping through each tuple to create table rows
    for name, color in name_color_pairs:
        html += f'<tr><td>{name}</td><td style="background-color:{color};"></td></tr>'

    html += '</table>'
    return html

tups = [(r.agent.to_dict()['traits']['politics'], r.answer['favorite_color']) for r in result]

html_table = create_html_table(tups)
print(html_table)
{% endhighlight %}

Here is the result:

<html>
<table border="1"><tr><th>Name</th><th>Color</th></tr><tr><td>Conservative</td><td style="background-color:#FF0000;"></td></tr><tr><td>Liberal</td><td style="background-color:#0000FF;"></td></tr><tr><td>Progressive</td><td style="background-color:#007bff;"></td></tr><tr><td>Socialist</td><td style="background-color:#FF0000;"></td></tr><tr><td>Libertarian</td><td style="background-color:#FEEA00;"></td></tr><tr><td>Moderate</td><td style="background-color:#808080;"></td></tr><tr><td>Populist</td><td style="background-color:#FF9900;"></td></tr><tr><td>Green</td><td style="background-color:#00FF00;"></td></tr><tr><td>Nationalist</td><td style="background-color:#FF0000;"></td></tr><tr><td>Neoconservative</td><td style="background-color:#FF0000;"></td></tr><tr><td>Tea Party</td><td style="background-color:#FF0000;"></td></tr><tr><td>Democratic Socialist</td><td style="background-color:#0066CC;"></td></tr><tr><td>Anarchist</td><td style="background-color:#000000;"></td></tr><tr><td>Centrist</td><td style="background-color:#808080;"></td></tr><tr><td>Feminist</td><td style="background-color:#FF69B4;"></td></tr><tr><td>Paleoconservative</td><td style="background-color:#800000;"></td></tr><tr><td>Alt-Right</td><td style="background-color:#FF0000;"></td></tr><tr><td>Communist</td><td style="background-color:#FF0000;"></td></tr><tr><td>Isolationist</td><td style="background-color:#FF0000;"></td></tr><tr><td>Technocrat</td><td style="background-color:#808080;"></td></tr></table>
</html>

Funny. The use of grey for moderate / technocratic attitudes is interesting. Most are otherwise fairly intuitive.
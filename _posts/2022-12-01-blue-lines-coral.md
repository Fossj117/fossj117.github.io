---
layout: post 
title: "Data x Design Exhibit: Blue Lines & Future Coral" 
date: 2023-03-06
latex: true 
mathjax: true
comments: true
---

In March 2022, [Jesse](https://www.instagram.com/jessecallahanbryant/), [Evan](https://www.linkedin.com/in/evanfinkle/) and I were participating artists in the [Data Through Design 2022](https://datathroughdesign.com/2022) exhibit, titled "Ground Truth IRL" at the Hall gallery space in Brooklyn Navy Yards. As described by DxD, the exhibition featured works that “creatively analyze, interpret and interrogate data made available in NYC’s Open Data Portal”. Our project was titled “Blue Lines + Future Coral”; here is how we summarized the project in our exhibit label: 

> Blue Lines + Future Coral attempts to render sensible the growing socio-environmental problems involving water, the people of New York, and our climatic future. Like all issues related to climate change, these problems are both material and political. First, there is the increased material threat of flooding that will continue to rise as global temperatures increase. But second, there is the financial threat of “blue-lining”, or the commercial practice of incorporating flood models into profit calculations, and thus limiting access to flood insurance or 30-year mortgages based on estimations of future climate risk. 
> 
> This project combines flood data from projected sea level rise maps with US census data, interviews, and drawings to imagine future waves of climate-driven displacement within the neighborhoods of New York, and explore their uncertain consequences. At a macro level, we visualize New Yorkers as dots, initially washing away from the city as flood waters come in, but eventually re-aggregating as generative, coral-like forms that represent unknown future communities. We pair this with “on the ground” drawings and interviews taken from flood-prone areas of the city, where we ask anonymous New Yorkers to reflect on the question: “If there was a flood, where would you go?”

Here is an image of our exhibit at the Hall gallery space in Brooklyn, NY: 

<p>
<center>
<img alt="Gallery Image" align="center" src="/figs/2022-12-01-blue-lines-coral/gallery_space.png" width="75%">
</center>
</p>

Here is a screenshot of our coral animation which was projected in the gallery (the full animation is [on YouTube](https://www.youtube.com/watch?v=OnkTffFi_Eo&t=1s&ab_channel=JeffFossett)): 

<p>
<center>
<img alt="Coral Animation" src="/figs/2022-12-01-blue-lines-coral/coral_animation_ss.png" width="75%">
</center>
</p>
For more details, check out our broader writeup of the project on the 90percentart blog [here](https://90percentart.blogspot.com/2022/12/blue-lines-future-coral.html). Additionally, the code to generate the coral animation is on github [here](https://github.com/90-Percent-Art/nyc_coral/tree/main).  

I have many further thoughts on the project concept, execution, and the experience of exhibiting with DxD which I hope to write about futher in the future. For now, I want to highlight one theme in the project that is interesting to me and seems fruitful for further exploration -- namely, the way the project uses generative art to think about broad, qualitative forms of uncertainty, and how this contrasts with the way conventional social scientific statistical analysis approaches uncertainty. Quoting from the [other blog post](https://90percentart.blogspot.com/2022/12/blue-lines-future-coral.html): 

> While conventional statistical analysis often uses data to place tight quantitative boundaries on tractable statistical uncertainty (confidence intervals, p-values and so on), such tools struggle to capture the kinds of broad, qualitative uncertainty involved in imagining complex socioeconomic-environmental futures (like climate-driven displacement and resettlement). Here, generative art steps in, using data to support the imagination in a different way. Each coral form in our animation is the result of a random, simulated process called diffusion-limited aggregation, with initial conditions based on the real NYC population distribution. We ran the process incrementally based on different extents of flooding and using a range of other parameter values to generate a varied range of coral-like forms. 

The point here is not that diffusion-limited aggregation is a "realistic" model of future patterns of migration (of course it is not). The point is that the project is interested in reflecting a type of uncertainty that is too broad and forward-looking to capture with conventional statistical tools or models. The reality of climate-driven displacement and resettlement in New York will arise out of some vastly complex mixture of mutually-interacting social, economic and environmental forces. In this context, generative art can support the imagination in a more open-ended, metaphorical way -- highlighting the uncertainty that is implicit in real data (about sea levels, and people, and so on), without claiming to have fully boxed it in.

Here is a creative prompt I wrote for myself on this theme: 

> How might we use data to become *less* certain? In statistical analysis, data is used to minimize, manage, control, and quanify uncertainty. How might we instead use data to introduce more complexity, uncertainty, un-knowing — and their counterparts: richness, nuance, diversity — into the world?

---
layout: post
title: "Chaotic System"
date: 2023-12-28
latex: true
mathjax: true
comments: true
genuaryDay: 8
tag: ["art", "genuary2024"]
---

<div id="jan-8"></div>
<!-- <input type="range" id="slider" min="0" max="5" step="0.1" value="1.0" name="epislon"/>
<label for="epislon">epsilon</label>
<input type="range" id="slider" min="0" max="5" step="0.1" value="0" name="mu"/>
<label for="mu">mu</label>
<input type="range" id="slider" min="0" max="5" step="0.1" value="0" name="k"/>
<label for="k">k</label>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script> -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.6.1/p5.js"></script>
<script src="{{ base.url | prepend: site.url }}/assets/2023-12-28-genuary-2024/jan8.js"></script>

Today I am messing with the [Bogdanov Map](https://en.wikipedia.org/wiki/Bogdanov_map) (sourced from [this](https://en.wikipedia.org/wiki/List_of_chaotic_maps) fun wikipedia list of chaotic maps) which for some parameters $\varepsilon$, $\mu$, $k$ maps $(x_n, y_n)$ to:

$$x_{n+1} = x_n + y_{n+1}$$

$$
y_{n+1} = y_n + \varepsilon y_n + k*x_n(x_n-1) + \mu x_ny_n
$$

The map seemed to be sending things off to very large numbers; so, here I am in each step updating the value modulus the canvas width and height. I am choosing random values in $(-3,3)$ (or exactly $0$) for $\varepsilon$, $\mu$, and $k$ and iterating on a single starting point in the middle of the canvas (note the chosen values are printed with `console.log` for now). I would like to play with this more and see what parameter values yield interesting results (or see what else I can do with it), but don't have time today. Still, this has convinced me that playing around with different sorts of chaotic maps would be fun in the future.

[back to the genuary index]({{ base.url | prepend: site.url }}/2023/12/28/genuary-2024.html)

$$
$$

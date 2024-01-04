---
layout: post
title: "ASCII"
date: 2023-01-28
latex: true
mathjax: true
comments: true
genuaryDay: 0x9
tag: ["art", "genuary2024"]
---

<div id="jan-9" style="font-family: 'Menlo'; font-size:10px"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.4.0/p5.min.js"></script>
<script src="{{ base.url | prepend: site.url }}/assets/2023-12-28-genuary-2024/jan9.js"></script>
<br>
I never experimented much with manipulating the DOM via `p5.js`, so today was my chance to give it a try. The game is that on every frame, a random cell updates and tries to be the opposite value (`0` or `.`) of all its neighbors. I'm interested to experiment more with `p5` DOM manipulation in the future.

[back to the genuary index]({{ base.url | prepend: site.url }}/2023/12/28/genuary-2024.html)

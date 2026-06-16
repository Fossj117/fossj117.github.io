---
layout: post
title: "Light a Candle"
date: 2026-04-02
latex: true
mathjax: true
comments: true
tag: ["art"]
---

<style>
.candle-caption { position: relative; z-index: 1; margin-bottom: 0; }
.candle-frame {
  display: block;
  border: none;
  background: transparent;
  width: calc(100% + 80px);
  margin-left: -40px;
  margin-right: -40px;
  margin-top: -120px;
  height: 600px;
  position: relative;
  z-index: 0;
}
@media screen and (max-width: 600px) {
  .candle-frame { width: 100%; margin-left: 0; margin-right: 0; margin-top: -80px; }
}
</style>

<p class="candle-caption">Click to light a candle (maybe <a href="#" onclick="document.body.classList.add('dark-mode'); localStorage.setItem('theme', 'dark'); return false;">turn off the lights</a> first?)</p>
<iframe src="/figs/2026-04-02-candle-sketch/index.html" class="candle-frame" frameborder="0" scrolling="no" allowtransparency="true"></iframe>

<html>
<p><details>

<summary><strong>More</strong></summary>

<p>I started this sketch for another project but didn't wind up using it for that purpose. I've been enjoying making digital elements like this "by hand" on my computer. This one was drawn with the pencil tool in Figma, then styled a bit more ex post and animated. It'd be nice to add a few more animation frames for the candle to be extinguished when clicked again, with little bits of smoke. 
</p>

</details>
</p>
</html>


---
layout: post
title: "Place-based Typeface"
date: 2026-11-24
latex: true
mathjax: true
comments: true
tag: ["technology", "art"]
---

My latest experiment is a project I am (for the moment) calling "Place-based Typeface". 

Here is the concept: 

1. Go around the city/world and take photos of text in various places (billboards, street signs, grafitti, flyers, whatever). 
2. Site extracts letters from the photo and attaches them to the location of the photo. So you get a map of characters attached to specific places on a map. 
3. Assemble a new "place-based typeface" in the following way: (i) choose a location on the map as your center point, (ii) extend a radius until you accumulate enough letters for a full typeface. The site then allows swapping in and out different letters from the radius and experimenting. 

Here is a screenshot of some of the interface: 

{% include image.html src="/figs/2026-11-24-placebased-typeface/interface.jpg" alt="Screenshot of the Place-based Typeface interface: a map of Inman Square with letters pinned to photo locations, and the assembled alphabet alongside" width="100%" %}

I am sure that other folks have experimented with similar kinds of things. For me, the project was loosely inspired by doing some collage from magazines last week, including assembling some cutout lettering from different places. 

So far, I've found the project fun to play with, as it draws attention to a particular set of things when moving through the urban environment--namely, all the text--which I am seeing and processing all the time, but often not thinking too much about. 

The code and interface was mostly built with Claude Code. There is a draft version of the site (still mostly closed to submissions) up [here](https://placebased-typeface.vercel.app/).

<style>
@font-face {
  font-family: "Inman Square 733 m";
  src: url("{{ '/assets/Inman-Square-733-m/Inman-Square-733-m.woff2' | relative_url }}") format("woff2");
  font-display: swap;
}
.post-title { font-family: "Inman Square 733 m", 'spectral', serif; letter-spacing: 0; font-size: 40px; }
</style>
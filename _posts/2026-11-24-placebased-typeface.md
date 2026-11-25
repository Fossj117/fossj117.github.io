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

## Related Projects

After exploring this idea, I found that it is very similar to a project called [Urban Alphabets](https://vimeo.com/117375299) developed by Suse Miessner in 2014. A few links about the project: [1](https://www.connectingcities.net/projects/urban-alphabets/), [2](https://www.behance.net/gallery/25496187/Urban-Alphabets). The website listed for the Urban Alphabets project seems to be down, and I don't see the app in the app store currently. So maybe I can consider my project a kind of revival. Perhaps I will reach out to Miessner at some point after I've played around with this idea a bit more. From some of the media about the Urban Alphabets, Miessner seems to be interested in this direction for similar reasons to me; for example, the project "encourages users to re-experience their surroundings"--a way to encourage people to engage with the city and its particular character in a new and different way.   

A few other related projects connected to collecting letters/type connected to specific places:

* [Type of Place](https://www.metanewhouse.com/typeofplace) (2011) by Meta Newhouse and Nathan Davis
* [Typewalk](https://typewalk.net/)
* [Type of Berlin](https://iammartin.dk/work/type-of-berlin/)
* [Letters & Landmarks](https://designsbytellie.com/case-studies/letters-landmarks)

<style>
@font-face {
  font-family: "Inman Square 733 m";
  src: url("{{ '/assets/Inman-Square-733-m/Inman-Square-733-m.woff2' | relative_url }}") format("woff2");
  font-display: swap;
}
.post-title { font-family: "Inman Square 733 m", 'spectral', serif; letter-spacing: 0; font-size: 40px; }
</style>
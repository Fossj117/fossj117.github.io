---
layout: post
title: "Bike Ride Art"
date: 2024-10-06
latex: true
mathjax: true
comments: true
tag: ["art"]
---

## Introduction

I continue to enjoy my daily practice of creative work. I like getting up early and exploring something new each day.

However, as my previous reflections have noted, I am ready for a change from the watercolor process that I've been exploring the past few weeks. In my next cycle of work, I want to try something a bit different and focus on a particular project. The project I have in mind is roughly the following. 

I love riding my bike around the Cambridge area. It is a particularly nice time of the year for it right now, with the cooler weather, and the leaves changing colors.

I want to make a piece of visual art that abstracts and captures some of the color of these bike rides. Here is my plan: 

1. I will start with a recorded video of a bike ride loop. For example, I have a nice video of a loop around part of the Charles River, which I enjoy.
2. I will write some code to process the video to extract important or interesting colors from each frame. I will need to explore some different ways of potentially doing this. I have a few rough thoughts on how to do this. 
3. Then, I will render the extracted colors visually, eventually using the pen plotter and some CMYK ink. Initially, my vision is to render the colors in a kind of circle or wheel shape -- reflecting both the geographic loop that underlies the video, and the wheel shape of the bicycle. There are also several other possibilities I could explore here.
4. If the piece comes together, I hope to submit it to [The Quinobequin Review](https://www.instagram.com/quinobequinreview/), which is a "place-based, literary journal for the Charles Watershed area" which also displays some art. 

## Day 1 (Sunday)

Today, I am going to start by simply trying to read in and process the colors from my video of riding around the Charles. The full video is here: 

<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/ZyS8Rai8B5k?si=Us94QfmX9oYRrsgn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</center>

The video is about 15 minutes and is 60FPS which means around 15 x 60 x 60 = 54,000 frames in the video. With some help from chatgpt, I write some code to open the video and compute the "average" RGB color of every 100 frames, and then render this as an SVG. Here is the result: 

![Avg colors test](/assets/2024-10-05-bike-ride-art/average_colors.svg)

The data processing is surprisingly slow. In general, displaying "average" color is not at all my intention, however this is a good starting point and it's interesting how it already communicates some elements of the ride. For example, the early part of the ride is on a dirt path rather than a paved one, rendering the average color more brown than grey. Later on, the ride goes through a bit more of an off-road path with greenery on both sides, rendering a greener average. I think you can even see the bits going through a tunnel under the road near the start and end of the ride. 

While this is just a starting point, it's nice how this is already starting to do some of what I hoped -- tell the story of a ride in colors. 

As a simple next step to make things a bit more interesting, I want to try re-running a version of this where we only look at the top part of each frame, since this skews more towards greens and sky, and will be nicer colors to emphasize. Here is an example of a top half frame: 

<div align="center">

<img src="/assets/2024-10-05-bike-ride-art/top_frame_2900.png" alt="top_half_ex" style="width: 70%;"/>

</div>

Here is the average color SVG results from processing only the top halfs: 

![Avg colors top](/assets/2024-10-05-bike-ride-art/average_colors_top.svg)

This is already nicer in terms of colors - more blue-green colors, from the combination of sky and trees. Finally, let's try a version with only the top third of the images:

![Avg colors top](/assets/2024-10-05-bike-ride-art/average_colors_top_third.svg)

This is even a bit brigther. This is a good start for the project. In my next iteration, I will explore some different ways of processing and displaying the color data. 

<!-- /Users/jfossett/Documents/Research/fossj117.github.io -->

<!-- What are my intentions? 

1. I want to explore CMYK color blending again. We've done a good handful of pen-plotted CMYK work previously. 
2. In contrast to the previous work, I want to explore working with fountain pens. I want to try to combine some of what I have learned with blending water and fountain pen ink with these previous CMYK experiments. 
3. Ultimately, I have a broader project idea in mind, which involves extracting colors from videos and 

What about procedural intentions? 

1. I think finishing *something* daily is important to the practice. Ideally, it would be a small finished piece. This helps with the iterative approach and feeling of learning and building.
2. Mindfulness and presence with what I am doing and working on is essential.  -->
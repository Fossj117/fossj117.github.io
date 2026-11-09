---
layout: post
title: "Scanning Trees"
date: 2026-11-06
latex: true
mathjax: true
comments: true
tag: ["nature", "art", "technology"]
---

This autumn, I am taking a fun course on 3D scanning trees, organized and taught by [Zach Mollica](https://zacharymolli.ca/). I have followed Mollica online for a while, and signed up on a bit of a whim. I have no specific background in or need for 3D scanning, but I have a general interest in using digital & technical tools for creative purposes--and to investigate the natural world in particular--and so thought it would be an interesting direction to explore. In this page I will document some of my thoughts, learnings, and creations. 

For one of my first scans, I wanted to revisit a tree in the area of Harvard Square that was previously a subject of our [Tree Portraits](https://jeffreyfossett.com/2023/03/06/tree-portraits.html) series. Rather than attempting to capture the branches and full extent of the tree, I did a close-up focus on just the trunk, which has some interesting knots and things. As in the tree portraits project, I am interested in 3D scanning as a way to individuate trees, and invite attention to their particularities of shape and form. 

## First Mesh Renders

<html>
<div style="display: flex; justify-content: center;">
<video
  src="/figs/2026-11-06-scanning-trees/mesh_renders_web.mp4"
  controls
  autoplay
  muted
  loop
  playsinline
  style="max-width: 100%; width: 325px; height: auto; border-radius: 4px;">
  Your browser does not support the video tag.
</video>
</div>
</html>

Rendered in Blender.

## Tree MRI

I was curious about the cross-sections of the model and what they might show. A friend mentioned that this visual reminded them of an MRI with its slices. 

<html>
<div style="display: flex; justify-content: center;">
<video
  src="/figs/2026-11-06-scanning-trees/tree_mri_web.mp4"
  controls
  autoplay
  muted
  loop
  playsinline
  style="max-width: 100%; width: 325px; height: auto; border-radius: 4px;">
  Your browser does not support the video tag.
</video>
</div>
<p style="text-align: center;"><a href="https://www.tiktok.com/@_j117_/video/7705065793477807390" target="_blank">Watch on TikTok</a></p>
</html>

I also experimented with some other visuals. A grid of the slices: 

{% include image.html src="/figs/2026-11-06-scanning-trees/series_grid.jpg" alt="Grid of the trunk's cross-section shapes, one per slice" width="100%" %}

Cross-sections nested and re-scaled to look like tree rings (but actually made from the same cross-sections):

{% include image.html src="/figs/2026-11-06-scanning-trees/rings_preview.jpg" alt="Trunk cross-section outlines nested like tree rings" width="100%" %}

## Bark Explorer

An idea I have been thinking about is how interactivity and exploration can help to promote attention, curiosity: 

<html>
<div id="tree-embed" style="aspect-ratio:16/10;background:#0b1018;display:flex;align-items:center;justify-content:center;cursor:pointer;color:#c9d2cf;font-family:Georgia,serif" onclick="this.outerHTML='<iframe src=&quot;{{ '/assets/tree/' | relative_url }}&quot; style=&quot;width:100%;aspect-ratio:16/10;border:0;display:block&quot; allow=&quot;fullscreen; autoplay&quot; title=&quot;A real tree&quot; onload=&quot;this.contentWindow.focus()&quot;></iframe>'">
  Click to explore the tree (about 60 MB; desktop with keyboard and mouse)
</div>
<p><a href="{{ '/assets/tree/' | relative_url }}" target="_blank">Open the tree in its own window</a></p>
</html>

This experiment was loosely inspired by the game [Outer Wilds](https://en.wikipedia.org/wiki/Outer_Wilds). I am not sure if it could be interesting to add more directedness to this tree version, or just leave it as just an exploration experiment. I could do something like mark specific locations that the player needs to find. A few other interactive ideas that have come to mind: 

1. I thought of the game "roll off" in Fall Guys, where players have to navigate obstacles to stay atop a rotating cylinder shape. I imagined something like this but the tree texture provides the cylinder form and the obstacles. A bit more silly. 

2. I thought of a version of this game inspired by my recent piece, "What do the turkeys do at night?" ([link](https://jeffreyfossett.com/files/turks_at_night.pdf)), where you play as a turkey and have to find a way up into a tree to roost, perhaps with energetic constraints and access to some human-made ramps. In general, a game where you play as an urban turkey seems pretty funny and interesting. 

3. I have a rough idea of a 2D platformer, a bit pixelated or halftoned, where the simple goal is to climb to the top of different trees around town. Like pokemon go, maybe you have to be near the real world tree to climb it, and then when you do you check it off in your tree pokedex. Again, an invitation to pay attention to and engage with particular trees in a place. 
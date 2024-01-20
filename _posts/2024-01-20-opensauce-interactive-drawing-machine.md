---
layout: post
title: "OpenSauce 2023: Collaborative Machine Art Making"
date: 2024-01-20
latex: true
mathjax: true
comments: true
tag: ["art", "electronics"]
---

In July 2023, [Evan](https://www.linkedin.com/in/evanfinkle/) and I were fortunate to be included as exhibitors at [OpenSauce](https://opensauce.live/) 2023 in San Francisco. The event was really great, and featured a huge range of interesting makers and builders doing strange and fascinating things with technology[^1].

Our exhibit built on our creative practice working with CNC drawing machines as [90percentart](https://90percentart.com/). In addition to sharing off [some of our existing work](https://www.instagram.com/90percent.art), we built an interactive tool for collaborative generative art-making with attendees.

<p>
<center>
<img alt="Drawing Machine" align="center" src="/figs/2024-01-20-opensauce-interactive-drawing-machine/drawing_machine_off.jpg" width="60%">
</center>
</p>

Built with [RGB slide potentiometers from adafruit](https://www.adafruit.com/product/5295?gad_source=1&gclid=Cj0KCQiA-62tBhDSARIsAO7twbYzVDTZP4Zy68k2jUgZKy-s1B_NcTdYkgEP-ELBp8BLkOT6b9AhfEoaAveFEALw_wcB) (wired up via [I2C](https://en.wikipedia.org/wiki/I%C2%B2C)), a [Raspberry Pi 3a+](https://www.raspberrypi.com/products/raspberry-pi-3-model-a-plus/) and some laser cut parts, the tool allowed users to manually explore the parameter space & aesthethic possibilities of a simple generative art algorithm we coded in python.

<p>
  <img alt="evan booth" src="/figs/2024-01-20-opensauce-interactive-drawing-machine/evan_booth.jpg" width="45%">
  <img alt="instructions" src="/figs/2024-01-20-opensauce-interactive-drawing-machine/instructions.jpg" width="45%">
</p>

When users found a design they liked, they could press a button to send it to us for live drawing on our CNC pen plotter at the conference. The resulting draw was theirs to keep.

<center>
<iframe width="315" height="560"
src="https://youtube.com/embed/XZEHNBZRx1U"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
allowfullscreen></iframe>
</center>

Overall, the build was a great way to engage and collaborate with conference attendees in our style of art-making; it was a lot of fun to watch folks (especially kids) experimenting with different design parameters and watch the machine draw.

<center>
<iframe width="315" height="560"
src="https://youtube.com/embed/n6NZzteHi6U"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
allowfullscreen></iframe>
</center>

Find all the code for the project on GitHub [here](https://github.com/Fossj117/interactive_drawing_machine/tree/main)!

## Footnotes 

[^1]: Our booth was right next to [our buddy Russ, who makes cool 3d-printed pottery](https://russfogle.com/). Check him out! Some of Evan's colleagues were also at the event showing off [BattleBot Chomp's](https://battlebots.fandom.com/wiki/Chomp) impressive walking mechanism.

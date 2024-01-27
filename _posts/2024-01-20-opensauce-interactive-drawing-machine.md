---
layout: post
title: "OpenSauce 2023: Collaborative Art-Making Machine"
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

## Reflection

I think what I find interesting about this project from a conceptual perspective is the way that it expresses a kind of flattening of the hierarchy of creative "expertise". In much conventional art, there is a kind of uni-directionality: the artist has "something to say" (an idea, a feeling, an aesthetic direction), and uses their mastery of the techinical tools of their medium (paint, words, photos, whatever) to speak it to an audience who is likewise positioned in a passive, receptive role as listener and receiver. While our project was very simple, I like the way it breaks down this speaker/audience division. An artistic "vision" is still present (e.g. in the design of the whole collaborative system as well as the visual algorithm); however, the exact articulation of it is now determined in collaboration with an audience who is far more active.

This kind of artist/audience interaction is certainly possible in a range of creative media[^2]; however, it seems particularly available for exploration in the generative art context, where new designs can readily be created/rendered/shared /materialized. Several recent generative art projects have explored this direction; salient examples include [QQL](https://qql.art/about) from Tyler Hobbs and Dandelion Wist, and [Fluint](https://medium.com/@eangolden/introducing-fluint-make-ink-and-water-art-with-your-friends-over-zoom-and-everyone-gets-63721d47fc35) from Ean Golden and team[^3]. (Note: there's an interesting interview with Hobbs [here](https://www.rightclicksave.com/article/tyler-hobbs-on-qql-and-the-future-of-generative-art) that touches on some related themes)

These are both interesting projects that I recommend checking out. In each, the artist's role is repositioned as the designer of a socio-technological system -- a set of building blocks that include large elements of randomness (computationally-mediated in the case of QQL; physically-mediated in the case of Flunit) -- which the audience engages with dynamically to make something new. 

This "stepping back" of the artist resonates with the broader movement towards "long form" generative art (e.g. [ArtBlocks](https://www.artblocks.io/)), where the artist gives up the right to explicit "curation" of which outputs to share from a generative algorithm. 

Getting even more conceptual, I think there are strong parallels with anarchist thought here, and a broader set of themes I am interested in around modularity and ownership in technological design -- see e.g. the discussion of "bottom-up design" [here](https://jeffreyfossett.com/2023/12/20/notes-on-scott.html). Broadly, the idea is that designers and artists have an important choice about *how strongly to impose their views* about what a  creative artifact *is* or *ought to be used for*. And further that -- at least in some settings -- there are some strong arguments (both practical and descriptive) for preferring a more humble, bottom-up, interactive, design mode that does not impose the creator's views so strongly. 

## Footnotes 

[^1]: Our booth was right next to [our buddy Russ, who makes cool 3d-printed pottery](https://russfogle.com/). Check him out! Some of Evan's colleagues were also at the event showing off [BattleBot Chomp's](https://battlebots.fandom.com/wiki/Chomp) impressive walking mechanism.

[^2]: One personal example that comes to mind for me is [this](https://www.zone3westernave.com/sketchbook/) "Community Sketchbook" project near me in Allston, MA, which variously invites community members to participate in the design of the mural. Another random example that comes to mind is a project like Abramović's [The Artist is Present](https://www.moma.org/calendar/exhibitions/964), which has something of this flavor. 

[^3]: Our unreleased "[Artproofs](https://jeffreyfossett.com/ArtproofsRadial/)" project is also in this spirit. Maybe we will finish it someday!
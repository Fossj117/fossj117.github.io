---
layout: post
title: "Drawing Practice"
date: 2026-07-25
comments: true
tag: ["art", "drawing"]
---

I have been drawing for much of my life in different ways, but I haven't spent much time really trying to *improve* drawing as a skill -- learning the craft and principles, doing deliberate practice, and so on. I've decided to make a commitment to do this for a while, starting with Brent Eviston's course on [the basic skills of drawing](https://www.udemy.com/course/the-art-and-science-of-drawing/).

As with other kinds of learning, I find documentation to be a helpful part of the process -- a chance to reflect, analyze, and stay curious. So I'm keeping a short log of each day of practice. This post indexes the series and will update as new days are added.

<!-- Liquid to build the ordered list of drawing days -->

{% assign drawing_days = site.drawing | sort: "day" %}

<ul>
{% for d in drawing_days %}
<li><a href="{{ d.url }}">Day {{ d.day }}</a> - {{ d.date | date: "%b %-d, %Y" }}</li>
{% endfor %}
</ul>

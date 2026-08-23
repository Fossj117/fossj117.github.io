---
layout: post
title: "Where do the Cambridge turkeys roost?"
date: 2026-08-23
comments: true
tag: ["nature", "llm"]
---

I have a longstanding interest in learning about and seeking to understand the Cambridge-area wild turkeys. Today, I wanted to try to learn more about the roosting patterns of the turkeys. In general, I know that wild turkeys roost in trees in the evenings primaily to protect themselves from predators. But I've only seen them up in the trees myself a few times (once around Linnean st I think, another time near Oxford street). I was curious if there was other information online from folks about where the Cambridge turkeys roost at night. 

I tasked Claude with investigating and had it put together this rough map from a variety of publicly-available reports online (e.g. Reddit, iNaturalist, news reports). Of course, there's not much of a way to verify any of this, and this investigation does not claim to be exhaustive or particularly systematic. Instead, I'm treating this as a starting point; I would like to investigate some of these locations for myself and see what I can see. 

Anyhow, here is the map: 

<style>html,body{overflow-x:hidden}</style>
<iframe src="/assets/turkeys/turkey_roost_map.html"
        style="width:calc(100vw - 48px);margin-left:calc(50% - 50vw + 24px);height:85vh;min-height:520px;border:1px solid #ddd;display:block"
        title="Cambridge MA wild turkey roost map" loading="lazy"></iframe>

<p style="font-size:14px">
<a href="/assets/turkeys/turkey_roost_map.html" target="_blank">View the map full screen</a> &middot;
<a href="/assets/turkeys/turkey_roost_reports.csv">Download the source list (CSV)</a>
</p>

## Methods (summarized by Claude)

The map draws on 40 reports compiled from public web sources (Reddit, iNaturalist, the Harvard Gazette and Crimson, local news, and a few blogs), spanning 2012 to 2026. Each report was classified as follows:

* **Evidence type**: a *roost report* means the source describes turkeys sleeping or perched overnight, or going up into a tree at dusk / seen up at dawn. A *daytime flock location* only records where a flock spends the day -- weak evidence for a roost, though turkeys usually roost within a few hundred meters of their daytime range. The set is split evenly: 20 roost reports and 20 daytime locations.
* **Confidence**: *high* means a firsthand account of explicit roosting at a specific spot; *medium* means explicit roosting but a vague location, or a secondhand account; *low* means the roosting is inferred, or the report is daytime only.
* **Location and uncertainty**: coordinates are placed by hand from the description in each source -- they are not GPS points. The circle around each marker reflects a judgment of how precisely the source pins the place, from ~30-60 m for a named tree or geotag up to ~1 km for descriptions like "along the Charles."
* **Date**: every record carries a year. The slider in the sidebar hides older reports, and the marker outlines distinguish reports from 2024 or later (solid), 2019-2023 (thin), and before 2019 (dashed).
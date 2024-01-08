---
layout: post
title: "Decentralized Society, Cooperation, and Plurality"
date: 2024-01-05
latex: true
mathjax: true
comments: true
tag: ["governance", "plurality"]
---

This January, I am excited to be participating in [this](https://www.ccc.mit.edu/eventopportunities/iap-2024-decentralized-society-cooperation-and-plurality/) IAP course at MIT with Wes Chow and Manon Revel. The short course will be heavy on reading and writing; I am planning to post my notes on this post as I go.

<!-- Liquid nonsense to build the ordered post list -->

{% assign post_list = site.posts %}
{% assign iap_posts = "" | split: "" %}
{% for post in post_list %}
{% if post.tag contains 'iap' %}
{% assign iap_posts = iap_posts | push: post %}
{% endif %}
{% endfor %}
{% assign sorted_iap = iap_posts | sort: 'class_num' | reverse %}

<ul>
{% for post in sorted_iap %}
<li>Class {{post.class_num}} - <a href="{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}
</ul>

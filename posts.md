---
layout: page
title: Posts
permalink: /posts/
---

<div class="home">
  <ul class="post-list">
    {% for post in site.posts %}
		{% if post.tag contains 'genuary2024'%}
		{% else %}
	      <!-- <li>
	        <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>
	        <h3>
	          <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
	        </h3>
	      </li> -->
		  <li>
		  <span class="post-meta">{{ post.date | date: "%Y/%m/%d" }}</span> - <a class="post-link" href="{{ post.url | prepend: site.baseurl }}"  style="display: inline;">{{ post.title }}</a>
		  <span class="post-tag">
			{% for tag in post.tag %}
				{{- tag -}}
		  		{% unless forloop.last %},{% endunless %}
		  	{% endfor %}
		</span>
		  </li>
		  {% endif %}
    {% endfor %}
  </ul>

  <p class="rss-subscribe">subscribe <a href="{{ "/feed.xml" | prepend: site.baseurl }}">via RSS</a></p>

</div>

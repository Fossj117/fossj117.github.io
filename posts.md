---
layout: page
title: Posts
permalink: /posts/
---

<script>
let currentFilter = null;
let allPosts = [];

// Initialize the tag filtering functionality
window.onload = function() {
  initializeTagFiltering();
};

function initializeTagFiltering() {
  // Store all posts and their data
  const postItems = document.querySelectorAll('.post-list li');
  postItems.forEach(item => {
    const tags = Array.from(item.querySelectorAll('.post-tag span')).map(span => span.textContent.trim());
    allPosts.push({
      element: item,
      tags: tags
    });
  });
}

function filterByTag(tag) {
  // If clicking the same tag that's already active, clear the filter
  if (currentFilter === tag) {
    clearFilter();
    return;
  }
  
  // Set new filter
  currentFilter = tag;
  
  // Update tag styling and filter posts
  updateTagStyling();
  filterPosts();
}

function clearFilter() {
  currentFilter = null;
  updateTagStyling();
  filterPosts();
}

function updateTagStyling() {
  // Remove bold from all tags
  document.querySelectorAll('.post-tag span').forEach(span => {
    span.style.fontWeight = 'normal';
  });
  
  // Bold the active filter tag
  if (currentFilter) {
    document.querySelectorAll('.post-tag span').forEach(span => {
      if (span.textContent.trim() === currentFilter) {
        span.style.fontWeight = 'bold';
      }
    });
  }
}

function filterPosts() {
  allPosts.forEach(post => {
    if (!currentFilter) {
      // Show all posts when no filter is active
      post.element.style.display = 'block';
    } else {
      // Show only posts that have the current filter tag
      const hasTag = post.tags.includes(currentFilter);
      post.element.style.display = hasTag ? 'block' : 'none';
    }
  });
}
</script>

<div class="home">
  <ul class="post-list">
    {% for post in site.posts %}
		{% if post.tag contains 'genuary2024' or post.tag contains 'iap' or post.tag contains 'draft' or post.tag contains 'excluded' or post.tag contains 'genuary2025' %}
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
				<span style="cursor: pointer;" onclick="filterByTag('{{ tag }}')">{{- tag -}}</span>
		  		{% unless forloop.last %},{% endunless %}
		  	{% endfor %}
		</span>
		  </li>
		  {% endif %}
    {% endfor %}
  </ul>

  <p class="rss-subscribe">subscribe <a href="{{ "/feed.xml" | prepend: site.baseurl }}">via RSS</a></p>

</div>

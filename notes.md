---
layout: default
title: Notes
---

<script>
// Function to display a random note on page load
window.onload = function() {
  var noteCount = {{ site.notes | size }};
  var randomNote = Math.floor(Math.random() * noteCount) + 1;
  displayNote(randomNote);
};

function displayNote(number) {
  fetch('https://jeffreyfossett.com/notes/' + number + '.html')
    .then(response => response.text())
    .then(content => {
      document.getElementById('note-container').innerHTML = content;
    });
}
</script>

*Just little notes and quotes that I want to hold on to...*

{% assign sorted_notes = site.notes | sort: "num" %}

{% for note in sorted_notes %}<a href="javascript:void(0);" onclick="displayNote('{{ note.num }}')">{{ note.num }}</a>{% unless forloop.last %} - {% endunless %}{% endfor %}  

<div id="note-container">
  <!-- Random note content will be displayed here on page load -->
</div>

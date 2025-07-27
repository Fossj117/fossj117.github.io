---
layout: default
title: Notes
---

<script>
// Store all notes data for searching
let allNotes = [];
let noteContentCache = {};

// Function to display a random note on page load
window.onload = function() {
  var noteCount = {{ site.notes | size }};
  var randomNote = Math.floor(Math.random() * noteCount) + 1;
  displayNote(randomNote);
  
  // Initialize search functionality
  initializeSearch();
};

function displayNote(number) {
  fetch('https://jeffreyfossett.com/notes/' + number + '.html')
    .then(response => response.text())
    .then(content => {
      document.getElementById('note-container').innerHTML = content;
    });
}

function initializeSearch() {
  // Get all note items and store their data
  const noteItems = document.querySelectorAll('.note-item');
  noteItems.forEach(item => {
    const link = item.querySelector('.note-link');
    const noteNum = link.getAttribute('data-num');
    allNotes.push({
      num: noteNum,
      element: item
    });
  });
  
  // Add event listener to search input
  const searchInput = document.getElementById('note-search');
  searchInput.addEventListener('input', function() {
    filterNotes(this.value);
  });
}

function filterNotes(searchTerm) {
  const searchLower = searchTerm.toLowerCase();
  
  if (searchTerm === '') {
    // Show all notes if search is empty
    allNotes.forEach(note => {
      note.element.style.display = 'inline';
    });
    // Reset all separators to their original state
    resetSeparators();
    return;
  }
  
  // Search through each note's content
  allNotes.forEach(note => {
    searchNoteContent(note.num, searchLower, note.element);
  });
  
  // After filtering, hide trailing separators
  hideTrailingSeparators();
}

function resetSeparators() {
  // Show all separators that should be visible in the original list
  document.querySelectorAll('.note-separator').forEach(separator => {
    separator.style.display = 'inline';
  });
}

function hideTrailingSeparators() {
  const visibleItems = Array.from(document.querySelectorAll('.note-item')).filter(item => 
    item.style.display !== 'none'
  );
  
  // Hide all separators first
  document.querySelectorAll('.note-separator').forEach(separator => {
    separator.style.display = 'none';
  });
  
  // Show separators only between visible items (not after the last one)
  visibleItems.forEach((item, index) => {
    if (index < visibleItems.length - 1) {
      const separator = item.querySelector('.note-separator');
      if (separator) {
        separator.style.display = 'inline';
      }
    }
  });
}

function searchNoteContent(noteNum, searchTerm, itemElement) {
  // Check if we've already cached this note's content
  if (noteContentCache[noteNum]) {
    const matches = noteContentCache[noteNum].toLowerCase().includes(searchTerm);
    itemElement.style.display = matches ? 'inline' : 'none';
    return;
  }
  
  // Fetch the note content and cache it
  fetch('https://jeffreyfossett.com/notes/' + noteNum + '.html')
    .then(response => response.text())
    .then(content => {
      // Cache the content
      noteContentCache[noteNum] = content;
      
      // Check if content matches search term
      const matches = content.toLowerCase().includes(searchTerm);
      itemElement.style.display = matches ? 'inline' : 'none';
    })
    .catch(error => {
      console.error('Error fetching note content:', error);
      // If we can't fetch the content, hide the item to be safe
      itemElement.style.display = 'none';
    });
}
</script>

*Some bits and bobs that I want to hold on to...*

<div style="margin: 20px 0;">
  <input type="text" id="note-search" placeholder="Search notes...">
</div>

<style>
/* Base styles for search input */
#note-search {
  width: 50%;
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 14px;
  background-color: #f8f9fa;
  color: #333;
  transition: all 0.2s ease;
}

/* Dark mode support */
.dark-mode #note-search {
  background-color: #0f1419 !important;
  border-color: #2d3748 !important;
  color: #e2e8f0 !important;
}

.dark-mode #note-search::placeholder {
  color: #718096 !important;
}

.dark-mode #note-search:focus {
  background-color: #1a202c !important;
  border-color: #63b3ed !important;
  outline: none !important;
  box-shadow: 0 0 0 3px rgba(99, 179, 237, 0.1) !important;
}

/* Light mode focus styles */
#note-search:focus {
  outline: none !important;
  border-color: #3182ce !important;
  box-shadow: 0 0 0 3px rgba(49, 130, 206, 0.1) !important;
  background-color: #ffffff !important;
}

#note-search::placeholder {
  color: #718096;
}
</style>

{% assign sorted_notes = site.notes | sort: "num" %}

{% for note in sorted_notes %}<span class="note-item"><a href="javascript:void(0);" onclick="displayNote('{{ note.num }}')" class="note-link" data-num="{{ note.num }}">{{ note.num }}</a>{% unless forloop.last %}<span class="note-separator"> - </span>{% endunless %}</span>{% endfor %}  

<div id="note-container">
  <!-- Random note content will be displayed here on page load -->
</div>

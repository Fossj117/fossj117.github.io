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
  // Check if there's a note specified in the URL hash
  var noteFromHash = getNoteFromHash();
  
  if (noteFromHash) {
    displayNote(noteFromHash, false); // Don't update hash since we're loading from it
  } else {
    var noteCount = {{ site.notes | size }};
    var randomNote = Math.floor(Math.random() * noteCount) + 1;
    displayNote(randomNote, true);
  }
  
  // Initialize search functionality
  initializeSearch();
  
  // Listen for browser back/forward navigation
  window.addEventListener('hashchange', function() {
    var noteFromHash = getNoteFromHash();
    if (noteFromHash) {
      displayNote(noteFromHash, false);
    }
  });
};

// Extract note number from URL hash
function getNoteFromHash() {
  var hash = window.location.hash;
  if (hash && hash.length > 1) {
    var noteNum = hash.substring(1); // Remove the '#'
    // Validate that it's a valid note number
    if (noteNum && !isNaN(noteNum)) {
      return noteNum;
    }
  }
  return null;
}

function displayNote(number, updateHash) {
  // Default to updating hash if not specified
  if (updateHash === undefined) updateHash = true;
  
  // Update URL hash for shareable links
  if (updateHash) {
    history.pushState(null, null, '#' + number);
  }
  
  fetch('https://jeffreyfossett.com/notes/' + number + '.html')
    .then(response => response.text())
    .then(content => {
      document.getElementById('note-container').innerHTML = content;
      boldNoteNumber(number);
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
    // Display a random note
    var noteCount = {{ site.notes | size }};
    var randomNote = Math.floor(Math.random() * noteCount) + 1;
    displayNote(randomNote);
    return;
  }
  
  // Hide all notes initially
  allNotes.forEach(note => {
    note.element.style.display = 'none';
  });
  
  // Track pending searches and matches
  let pendingSearches = allNotes.length;
  let hasMatches = false;
  let matchingNotes = [];
  
  // Search through each note's content
  allNotes.forEach(note => {
    searchNoteContent(note.num, searchLower, note.element, (matches) => {
      pendingSearches--;
      if (matches) {
        hasMatches = true;
        matchingNotes.push(note.num);
      }
      
      // When all searches are complete
      if (pendingSearches === 0) {
        if (!hasMatches) {
          // No matches found, clear content
          document.getElementById('note-container').innerHTML = '';
        } else {
          // Display a random matching note and bold its number
          var randomIndex = Math.floor(Math.random() * matchingNotes.length);
          var randomMatchingNote = matchingNotes[randomIndex];
          displayNote(randomMatchingNote);
          boldNoteNumber(randomMatchingNote);
        }
      }
    });
  });
  
  // After filtering, hide trailing separators
  hideTrailingSeparators();
}

function boldNoteNumber(noteNum) {
  // Remove bold and underline from all note links
  document.querySelectorAll('.note-link').forEach(link => {
    link.style.fontWeight = 'normal';
    link.style.textDecoration = 'none';
  });
  
  // Bold and underline the displayed note number
  document.querySelectorAll('.note-link').forEach(link => {
    if (link.getAttribute('data-num') === noteNum.toString()) {
      link.style.fontWeight = 'bold';
      link.style.textDecoration = 'underline';
    }
  });
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

function searchNoteContent(noteNum, searchTerm, itemElement, callback) {
  // Check if we've already cached this note's content
  if (noteContentCache[noteNum]) {
    const matches = noteContentCache[noteNum].toLowerCase().includes(searchTerm);
    itemElement.style.display = matches ? 'inline' : 'none';
    if (callback) callback(matches);
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
      if (callback) callback(matches);
    })
    .catch(error => {
      console.error('Error fetching note content:', error);
      // If we can't fetch the content, hide the item to be safe
      itemElement.style.display = 'none';
      if (callback) callback(false);
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

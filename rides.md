---
layout: default
title: Rides
---

<script>
// Function to display a random ride report on page load
window.onload = function() {
  var rideCount = {{ site.ride_reports | size }};
  var randomRide = Math.floor(Math.random() * rideCount) + 1;
  displayRide(randomRide);
};

function displayRide(number) {
  fetch('/rides/' + number + '.html')
    .then(response => response.text())
    .then(content => {
      document.getElementById('ride-container').innerHTML = content;
    });
}
</script>

*Notes and thoughts on bike rides...*

{% assign sorted_rides = site.ride_reports | sort: "num" %}

{% for ride in sorted_rides %}<a href="javascript:void(0);" onclick="displayRide('{{ ride.num }}')">{{ ride.num }}</a>{% unless forloop.last %} - {% endunless %}{% endfor %}  

<div id="ride-container">
  <!-- Random ride report content will be displayed here on page load -->
</div>

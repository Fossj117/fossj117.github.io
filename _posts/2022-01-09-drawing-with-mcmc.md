---
layout: post 
title: "Drawing with Markov Chain Monte Carlo" 
date: 2022-01-09
latex: true 
mathjax: true
comments: true
---
*This project is a collaboration with [Evan](https://www.linkedin.com/in/evanfinkle/) via [90percentart](https://90percentart.com/)*

I took this graduate bayesian statistics course a while back ([Stat 220](https://statistics.fas.harvard.edu/statistics-courses)). The course largely involved working through different pieces of the Gelman & co. [Bayesian Data Analysis](https://books.google.com/books?id=ZXL6AQAAQBAJ&printsec=frontcover&source=gbs_ge_summary_r&cad=0#v=onepage&q&f=false) textbook (which is an excellent textbook), and implementing a whole bunch of Markov Chain Monte Carlo (MCMC) algorithms. 

Later on after I got into generative art, I thought that these MCMC methods could be used to create paths that could be rendered via a drawing machine. The basic idea is to think of a greyscale image as a 2D probability distribution, where darker areas of the image are areas with more probability mass. This distribution (or some transformation of it), can then be taken as the target distribution in an MCMC method, generating a continuous path which has a stationary distribution that matches the target. Rendering this path with a pen then amounts to adding pigment to areas of the paper roughly in proportion to how dark they are in the original image, yielding some reflection of the original. 

Here are a few drawn results from this method using [Metropolis-Hastings](https://en.wikipedia.org/wiki/Metropolis%E2%80%93Hastings_algorithm) (both Pigma micron on strathmore bristol): 

<p>
  <img alt="Tree Portrait 1" src="/figs/2022-01-09-drawing-with-mcmc/lupita.jpg" width="45%">
  <img alt="Tree Portrait 2" src="/figs/2022-01-09-drawing-with-mcmc/sagrada.jpg" width="45%">
</p>

As with MCMC methods in statistics, there are plenty of tuning parameters available here that yield different visual results. For example, the variance of the proposal distribution, the number of steps, and the transformation of the original greyscale distribuiton all have a big impact on the resulting image. 

Also, in practice, the resulting path -- and its visual look -- can be quite different on each run of the algorithm, even with identical parameters. As shown in the drawings above, I like the visual feel when the algorithm fails to fully reach certain parts of the input image, yielding an "incomplete" kind of look.

Separately, I think that this sort of play could be a great and engaging way to teach about these algorithms in stats class. 

Here is a final image of the drawing machine at work: 

<p>
<center>
<img alt="Tree Portrait 2" src="/figs/2022-01-09-drawing-with-mcmc/drawing_machine.jpg" width="60%">
</center>
</p>

See more about this work [on](https://www.instagram.com/p/CRppt1Ituiv/?igshid=MzRlODBiNWFlZA==) [our](https://www.instagram.com/p/CPd4bwNH9JF/?igshid=MzRlODBiNWFlZA==) [Instagram](https://www.instagram.com/p/CYg70lXlgi5/?igshid=MzRlODBiNWFlZA==).
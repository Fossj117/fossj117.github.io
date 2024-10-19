---
layout: post
title: "Notes on the Plurality Book (Weyl & Tang)"
date: 2023-12-27
latex: true
mathjax: true
comments: true
toc: true
tag: ["plurality", "notes", "excluded"]
---

In this post, I will keep some very rough notes about the [Plurality book](https://github.com/pluralitybook/plurality/tree/main/contents/english) led by Weyl and Tang. These notes are mostly for personal use, but I like the idea of documenting them publicly for various reasons. Maybe I will make a separate blog section for reading notes at some point.

<div id="toc"></div>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
  $(document).ready(function() {
    var toc = $("<ul>");
    $("article h2").each(function(index) {
      var text = $(this).text();
      var id = "section-" + index;
      $(this).attr("id", id);
      var listItem = $("<li><a href='#" + id + "'>" + text + "</a></li>");
      toc.append(listItem);
    });
    $("#toc").append("<h2>Table of Contents</h2>").append(toc);
  });
</script>

## [1-Preface](https://github.com/pluralitybook/plurality/blob/main/contents/english/01-preface.md)

Reference to [The Declaration for the Future of the Internet](https://www.whitehouse.gov/wp-content/uploads/2022/04/Declaration-for-the-Future-for-the-Internet_Launch-Event-Signing-Version_FINAL.pdf)

- Basically affirming liberal democratic values on the internet, against threats from authoritarian governments (firewalls, censorship) and dominant technology platforms
- "We affirm our commitment to promote and sustain an Internet that: is an open, free, global, interoperable, reliable, and secure and to ensure that the Internet reinforces democratic principles and human rights and fundamental freedoms; offers opportunities for collaborative research and commerce; is developed, governed, and deployed in an inclusive way so that unserved and underserved communities, particularly those coming online for the first time, can navigate it safely and with personal data privacy and protections in place; and is governed by multistakeholder processes. In short, an Internet that can deliver on the promise of connecting humankind and helping societies and democracies to thrive."
  - Principles outlined:
    - Protection of human rights
    - A global internet
    - Inclusive and affordable access
    - Trust in the digital ecosystem
    - Multistakeholder internet governance

What is Plurality?

- Goal to magnify and strengthen the virtue of cognitive diversity across borders.
- "The idea of Plurality captures the symbiotic relationship between democracy and collaborative technology. The challenge of digitally transforming democracy might seem daunting, but it is not insurmountable. By fusing democracy with technology, as we've shaped science with diversity, we can weave a fabric of trust for the public to nurture and cherish, breathing new life into our river of democracy"
- I think that this is one of the things that differentiates the plurality space from a more general focus on liberal democratic values -- namely a focus on technological development as an important site of investment / intervention in supporting democracy. Two related ideas:
  - Supporting the collaborative / democratic development of technologies like the internet _per se_
  - Understanding technology [as a mode of governance](https://jeffreyfossett.com/2023/10/18/my-lens-on-technology.html), as something [that has politics](https://www.jstor.org/stable/20024652), that can support or undermine broader social values like democracy. Clearly consonant with lots of STS ideas.

## [Introduction](https://github.com/pluralitybook/plurality/blob/main/contents/english/02-introduction.md)

Updated version is [2-0: Information Technology and Democracy: a Widening Gulf](https://github.com/pluralitybook/plurality/blob/main/contents/english/2-0-information-technology-and-democracy-a-widening-gulf.md). 

Key idea is that there is currently a tension between (digital) technology and democracy. But this need not be the case.

- "the path technology and democracy as systems have taken have put them at loggerheads and the ensuing battle has claimed victims on both sides"
- Issues from recent developments in both AI and blockchain: "The dominant trends in technology in recent decades have been artificial intelligence and blockchains. These have, respectively, empowered centralized top-down control and turbo-charged atomized polarization and financial capitalism. Both outcomes are corrosive to the values of democratic pluralism"
  - I was a little surprised to see blockchain critiqued here, but I agree with the pieces critiqued. I want to understand more what they mean by "turbo-charged atomized polarization"
  - General skepticism that democracy is working well right now, partly because of its lethargy in keeping up technologically. Interesting to note the resonances here with [Scott and his brand of anarchism](https://jeffreyfossett.com/2023/12/20/notes-on-scott.html). Something I will be keeping an eye on in the plurality space is what version and "scale" of democracy seems to be the main focus; so far, I think I detect a set of values that are consonant with Scott (e.g. emphasizing small-scale participatory models over large-scale hierarchies even if democratic). But it will be interesting to keep an eye on this.

Key counterpoint: technology and democracy can be natural allies.

- "In this book we hope to show that this tragic conflict is avoidable, that properly conceived technology and democracy can be powerful and natural allies"
- This counterpoint relies on the key analytical point (rightly attributed to STS thinkers) that the direction of technological development is not inevitable. That there are many potential pathways which can have many possible effects on the social and democratic order.
  - They reference various future technological visions, which I would think of basically as "[sociotechnical imaginaries](https://press.uchicago.edu/ucp/books/book/chicago/D/bo20836025.html)".
  - The main ones they higlight are "Abundance Technocracy" and "Entrepreneurial Sovereignty"

The goal of the book, then, is to flesh out a different imaginary -- "Digital Democracy" wherein technology and democracy are mutually supportive.

Other takeaways for me on this section are that I should definitely read [the new Acemoglu book](https://www.amazon.com/Power-Progress-Thousand-Year-Technology-Prosperity/dp/1541702530) and more deeply in his technology research agenda in general.

From the STS side, I think there are clear resonances with someone [Yaron Ezrahi](https://www.amazon.com/Descent-Icarus-Transformation-Contemporary-Democracy/dp/067419828X) in addition to the Jasanoff work noted above. I need to re-read this and dive into it more deeply.

In general, one of the things on display in this chapter that excites me about the plurality research agenda is the way it manages to borrow from various fields that I am interested in in exactly the pieces that I think are most appropriate. In other words, if plurality is a venn diagram that includes economics, STS, web3 among other fields, the parts of these various fields that I find most compelling are exactly those that seem to overlap in the venn diagram with Plurality.

- For example, I think there are some interesting things happening in the blockchain space (e.g. experiments in new modes of digital governance), but there is also a lot of junk especially related to over-financialization in the space; the plurality agenda seems to carve out exactly the right boundary here.
- Similarly with the econ and STS spaces. I often feel that the econ of technology world could learn more from STS, especially STS' emphasis on the contingency of technological pathways and its skepticism towards technological determinism. Weyl and Tang highlight exactly this point, and focus on the part of the economics world that _does_ rightly integrate this consideration (i.e. Acemoglu's work).

Some lists of helpful economic citations to make sure I've read all of (most are familiar):

- "The Rise of Market Power and the Macroeconomic Implications" by Jan De Loecker and Jan Eeckhout, Quarterly Journal of Economics, 2017.; "The Race Between Man and Machine: Implications of Technology for Growth, Factor Shares and Employment" by Daron Acemoglu, American Economic Review, 2019.; "The Cost of Convenience: Ridehailing and Traffic Fatalities" by John Barrios, Yael Hochberg, and Hanyi Yi, Journal of Political Economy, 2020. "Firming Up Inequality" by David Autor, David Dorn, Lawrence F. Katz, Christina Patterson, and John Van Reenen, Centre for Economic Performance Discussion Paper, 2020. "The Increasing Dominance of Large Firms" by Gustavo Grullon, Yelena Larkin, and Roni Michaely, Review of Financial Studies, 2019.; "The Digital Economy, Business Dynamism and Productivity Growth" by Chad Syverson, National Bureau of Economic Research, 2018.; "Industrial Concentration in the Age of Digital Platforms" by Fiona Scott Morton, Yale Law Journal, 2019.;"The Failure of Free Entry" by Philippe Aghion, Antonin Bergeaud, Timo Boppart, Peter Klenow, and Huiyu Li, Review of Economic Studies, 2019.; "The Capitalist Machine: Computerization, Workers' Power, and the Decline in Labor's Share within U.S. Industries" by Shouyong Shi and Wei Cui, Journal of Political Economy, 2021. "Competition and Market Power in the Era of the Big Five" by Thomas Philippon, American Economic Review, 2021.
- "The Race Between Machine and Man: Implications of Technology for Growth, Factor Shares, and Employment" by Daron Acemoglu and Pascual Restrepo (2018); "Capitalism without Capital: The Rise of the Intangible Economy" by Jonathan Haskel and Stian Westlake (2018); "The Rise of the Machines: Automation, Horizontal Innovation and Income Inequality" by Daron Acemoglu and Pascual Restrepo (2018) ; "The Economics of Artificial Intelligence: An Agenda" by Ajay Agrawal, Joshua Gans, and Avi Goldfarb (2018); "The Impact of Artificial Intelligence - Widespread Job Losses" by Kai-Fu Lee (2021) ; "Skill Biased Technical Change and Rising Wage Inequality: Some Problems and Puzzles" by David Autor (2014)

## [A View from Yu Shan](https://github.com/pluralitybook/plurality/blob/main/contents/english/03-00-a-view-from-yu-shan.md)

This section of the book seems to be largerly under development still at the time of my reading. However, the section cites some important milestones in Taiwan's digital democracy which I can learn more about from elsewhere:

- **318 Sunflower Movement**: student protest movement protesting a trade deal between Taiwan and China which protestors thought would increase Taiwan's dependence on China and leave it vulnerable to political pressure. Per [wiki](https://en.wikipedia.org/wiki/Audrey_Tang#Political_career), this movement was the start of Audrey Tang's political career, and led to their first political appointments. I would like to learn more about this.
- **PDIS**: I think this is the the [Public Digital Innovation Space](https://pdis.nat.gov.tw/en/). Via LinkedIn: "PDIS is a team of creative minds working with the Digital Minister in Executive Yuan, government of Taiwan, leading digital transformation and open government movement."
- **The Digital Ministry**: The [ministry of digital affairs in Taiwan](<https://en.wikipedia.org/wiki/Ministry_of_Digital_Affairs_(Taiwan)>), which I'd also like to learn more about

Incidentally, I noticed as I was googling about these that, indeed, Tang identifies as a "conservative anarchist" in the sense described [here](<https://en.wikipedia.org/wiki/Ministry_of_Digital_Affairs_(Taiwan)>). Essentially, her politics emphasize voluntary cooperation rather than top-down hierarchy (whether from the state or capitalist actors) in the anarchist sense; the "conservative" modifier seems to refer to a respect for the diversity of existing cultures and traditions that exist in Taiwan, and a desire to preseve these. In practice, Tang seems to connect these values with an emphasis on radical openness and transparency. I would be interested to see this political perspective expanded on further.

## [Living in a Plural World](https://github.com/pluralitybook/plurality/blob/main/contents/english/03-01-living-in-a-plural-world.md)

Basic idea of this section is to think about different conceptual foundations of science, and explain how these lead to the different sociotechnical imaginaries outlined in the previous section. The section is pretty ranging (perhaps a bit too much so); but my understanding of the basic ideas:

- They first define the "monist atomist" understanding of science and argue that it informs the Abundance Technocracy (AT) and Entrepreneurial Sovereignty (ES) worldviews outlined in the previous chapters.
- The monist atomist view understands the physical (or social) world as having an objective state and as obeying an ultimately simple set of laws, waiting to be discovered. There's a commitment to a kind of reductionism here -- breaking complex phenomena down to atomic parts, which can be modeled in clear mathematical terms.
- The monist atomist / reductionist approach is then contrasted with scientific paradigms based in complexity, emergence, networks and collective intellgience.
- They argue that the latter paradigm has been influential across a range of scientific fields over the past century or so including math, physics, neuroscience and biology
- The rough idea is then to align the plurality project with this latter set of paradigms. Very coarsely: "monist atomist" is to AT/ES as "complexity/emergence/collective intelligence" are to the plural sociotechnical imaginary (DD?) that they are trying to develop.

Here is one way that this is stated (my parenthetical):

> Plurality is, scientifically, the application of an analogous perspective (to that of the complexity/emergence/network/collective intelligence paradigms) to the understanding of human societies and, technologically, the attempt to build formal information and governance systems that account for and resemble these structures as physical technologies built on plural science

There is an extended discussion of Granovetter and network sociology themes, which is contrasted with the methodological individualism of economics. Interestingly, "science of science" is aligned with the former.

I have a lot of thoughts on this section that I need to process more. One thing that I would like to see more of here is a connection with how STS scholars think about knowledge and expertise as a governing technology/institution in society. Thus when thinking about "plural" (social) science, the goal should not be just to integrate e.g. more network science considerations into economic modeling, while retaining the rest of the technocratic knowledge-making aparatus as is; instead, I think it should be more about how to pluralize/democratize the tools and systems of knowledge making, and thinking about how to mediate between different modes of knowing -- e.g. as I've discussed a bit [here](https://jeffreyfossett.com/2023/10/25/brainstorm-on-plurality-and-quant-social-science.html). I think this idea is also present more abstractly e.g. in [Latour](https://jeffreyfossett.com/2021/10/19/we-have-never-been-modern.html) and others.

## [The Lost DAO](https://github.com/pluralitybook/plurality/blob/main/contents/english/03-02-the-lost-dao.md)

Note: I am reading as of [this](https://github.com/pluralitybook/plurality/commit/41f6428a4a15a1502f90908f1b1ad27d6997c90b) commit on the project. This section seems to be still under development.

Here is a key motivating claim at the outset of the chapter:

> Liberal democracies often celebrate themselves as pluralistic societies, which would seem to indicate they have already drawn the available lessons from plural social science. Yet despite this formal commitment to pluralism and democracy, almost **every country has been forced by the limits of available information systems to homogenize and simplify social institutions in a monist atomist mold that runs into direct conflict with its values**.

Importantly, this is a claim about technologies and social institutions: that the limits of our existing information systems render our social institutions insufficiently supportive of the pluralism that we seek in liberal democracy. The goal of the research program is then to overcome these limitations and bring information technology into better alignment with the goals of pluralism.

Key features of liberal democracy that they are going to focus on: private property, identity and rights, voting. The basic claim is that these institutions are all too much based on "monist atomist" type principles.

### Property

This bit looks to be still in development. Here's a bit from later on:

> Where once commons-based property systems inhibited innovation when outsiders and industrialists found it impossible to navigate a thicket of local customs, private property cleared a path to development and trade by reducing those who could inhibit change

This reminds me of another piece from an STS course along the lines of _Seeing Like a State_, but it's not by Scott. The idea is similar though, about the imposition of systems of private property and capital by colonialists. More critical perspective than this one.

### Identity

Not sure about the story they tell here. Would be interesting to connect this narrative more to STS folks -- Porter, and Scott especially. I feel like this section especially should be peppered with Scott citations. And it makes me want to re-read _Seeing Like A State_ in more depth.

Here's the main piece:

> These documentary practices mean that some aspect of identity could be rooted outside of direct personal relations and into new abstrct relationship with the state based on primary registration at birth and secondary registration with subsequent documents usually issued in early adulthood. These state issued documents serve as foundational trust anchors for many other types of institutions

Thesis is that these forms of identity abstract people. Identity not based in (kin-, relationship-)based networks that are personally meaningful; instead abstracted identity that is really about the relationship with the state.

Interesting that so much of the argument for why we should move away from this seems to center on "how things were done through most of history" -- a kind of appeal to tradition argument. Seems like fleshing out the critique here would be productive (Scott cites could probably help). In any case, what is the new direction they propose?

> We have an opportunity to extend these documentary practices of state institutions and other formal institutions to peer and networked institutions

### Voting

Here's the baseline, centered around "one person one vote":

> the idea that numerical majorities (or in some cases supermajorities) should prevail regardless of the social composition of groups is at the core of how democracy is typically understood.

Presumably this is going to push towards quadratic voting type ideas once it is fleshed out further.

### Plural Social Science

The next section goes through a handful of social scientific thinkers who have critiqued these foundational institutions

- **Henry George** -- land tax ideas, also discussed in _Radical Markets_. Roughly, questioning ideas of private property in relation to land especially; who creates / is entitled to the value that accrues in land? Generally compelling.
- **George Simmel** -- "intersectional" theories of identity. Main idea:
  > humans are deeply social creatures and thus their identities are deeply formed through their social relations. Humans gain crucial aspects of their sense of self, their goals, and their meaning through participation in social, linguistic, and solidaristic groups
- One reference that this brings to mind for me is [MacIntyre on the virtue of patriotism](https://mirror.explodie.org/Is%20Patriotism%20a%20Virtue-1984.pdf) which I wrote about [here](https://jeffreyfossett.com/2021/11/15/partiality-and-carbon-chauvinism.html) in a random context. Never thought much about how that might connect to this research program, but in a sense it is a good moral philosophy analogue of the kind of shift they are recommending from an individualist focus (e.g. as represented by e.g. Mill) to one that understands people as existing in (and constituted by) networked, social contexts.
- **John Dewey** - love this citation, and want to read again / more completely _The Public and its Problems_. I wrote about it a bit in my reflection [here](https://jeffreyfossett.com/2020/02/20/sts-public-reason.html). Reading their discussion here convinces me I definitely need to dive deeper on Dewey. I'm intrigued by what they say about his discussion of technology:
  > Dewey focused specifically on the role of technology in creating new forms of interdependence that created the necessity for new publics. Railroads connected people commercially and socially who would never have met. Radio created shared political understanding and action across thousands of miles. Pollution from industry was affecting rivers and urban air. All these technologies resulted from research, the benefits of which spread with little regards for local and national boundaries. The social challenges (e.g. governance railway tariffs, safety standards, and disease propagation; fairness in access to scarce radio) arising from these forms of interdependence are poorly managed by both capitalist markets and preexisting “democratic” governance structures.
- Key ideas on what it means to be "democratic". I love this and need to dive in on him more. Democracy is not just about "voting" per se:
  > Core to true democracy is the idea that the “relevant public”, the set of people whose lives are actually shaped by the phenomenon in question, manage that challenge. Because technology is constantly throwing up new forms of interdependence, which will almost never correspond precisely to existing political boundaries, true democracy requires new publics to constantly emerge and reshape existing jurisdictions.
- Having [just been doing some reading on anarchism](https://jeffreyfossett.com/2023/12/20/notes-on-scott.html), there's a clear resonance with that perspective here too (h/t [Jesse](https://jessecallahanbryant.com/) highlighting this point), which is not surprising given Tang's stated anarchist preferences.
- And then, more interesting stuff about the role of experts in society:
  > Furthermore, because new forms of interdependence are not easily perceived by most individuals in their everyday lives, Dewey saw a critical role for what he termed “social science experts” ... to perceive a new form of interdependence (e.g. solidarity among workers, the carbon-to-global-warming chain), explain it to those involved by both word and deed, and thereby empower a new public to come into existence.
- This is a really interesting way to think about the purpose / role of expertise in society, and something that I want to process and internalize more. Dewey is so good, I feel like need to read _The Public and its Problems_ ASAP from cover to cover and internalize it. I love that they are drawing on him here.
- Here's their final Deweyan punchline on democracy:
  > Dewey’s conception of democracy and emergent publics is at once profoundly democratic and yet challenges and even overturns our usual conception of democracy. Democracy, in this conception, is not the static system of representation of a nation-state with fixed borders.
- **Norbert Wiener** and cybernetics.

<!-- They connect to network science, Granovetter.

> While we have emphasized the positive vision of pluralistic social science (a “network society”), it is important to note that beyond its inherent plausibility, a key reason for adopting such a perspective is the impossibility of explaining most social problems using monistic atomism given both complexity and chaos. Even in the social science field, economics, that most consistently aims for “methodological individualism”, it is universally accepted that trying to model complex organizations exclusively as the outgrowth of individual behavior is unpromising.

I feel like this is not reflecting on the more important aspect of plural social science. Plurality in the creation of social scientific knowledge...

> Yet, whatever level of explanation is chosen [in economics], actors are almost always modeled as atomistically self-interested and planners as coherent, objective maximizers, rather than socially-embedded intersections of group affiliations

Instead, plurality seeks to capture:

> social nature of motivations, to empower a diversity of social groups, to anticipate and support social dynamism and evolution, to ground personal identity in social affiliations and group choices in collective, democratic participation and to facilitate the establishment and maintenance of social context facilitating community.

I think for me a richer perspective here would focus on the role of plurality in the making of scientific and expert knowledge in society.

<!-- * "The simplest and most naïve way to think about science is what might be called “objectivist”, “rationalist” or, as we will dub it, “monist atomism”3. The physical world has an objective state and obeys an ultimately quite simple set of laws, waiting to be discovered"
* "They are also the foundation of the Abundance Technocracy (AT) and Entrepreneurial Sovereignty (ES) worldviews we discussed in the last chapter, though each emphasizes a different aspect. AT focuses on the unity of reason and science inherent in monism and seeks to similarly rationalize social life, harnessing technology. ES focuses on the fragmentation intrinsic to atomism and seeks to model “natural laws” for the interaction of these atoms (like natural selection and market processes). In this sense, while ES and AT seem opposite, they are opposites within an aligned scientific worldview."
* "Critical to all these developments are ideas such as “complexity”, “emergence”, “networks”, and “collective intelligence” that challenge the elegance of monist atomism." -->

Skipping forward a bit...

## [5-0 Collaborative Technology and Democracy](https://github.com/pluralitybook/plurality/blob/main/contents/english/05-00-collaborative-technology-and-democracy.md)

### First Read

Summarizing in my words, the first set of key ideas in this section are about (1) how we can do more if we work together, and (2) how collaborating across social difference (or "collaborating across diversity") is particularly productive. The question is how to use technology in ways that support this type of collaboration. 

The next section is about justifying the focus on "collaborating across diversity". Lots of overlap with Danielle Allen's work e.g. "Toward A Connected Society" ([my notes](https://jeffreyfossett.com/2024/01/09/decentralized-society-class3-allen.html)). Interestingly, the argument in Plurality book is more based in principles / high-level arguments rather than empirical work (as in the Allen piece). E.g. from the plurality book: 

> First, on the defensive/protective side, diversity is a consistent and omnipresent feature of life. If collaboration across it fails, it often translates into violent and destructive conflict. Second, on the positive/productive side, beauty, growth and progress all primarily result from collaboration across diversity.

The next point in this section is that collaborating across diversity is difficult. It is also comes with *the risk of eroding diversity*: 

> A critical concern, then, in Plurality is not just harnessing collaboration across diversity but also regenerating diversity, ensuring that in the process of harnessing diversity it is also replenished by the creation of new forms of social difference.

Interesting that this point is surfaced. It seems to connect to Tang's "conservative" anarchism perspective discussed above.  

Next piece discussed in this chapter is about "breadth" and "depth" tradeoffs in collaboration. A key point: 

> The goal of Plurality is to mitigate this trade-off and allow greater collaboration for any given level of diversity, or greater diversity for any depth of collaboration

Interesting discussion of breadth and depth tradeoff ideas in democratic systems: 

> One example illustrating this trade-off is common in political science: the debate over the value of deliberation compared to voting in democratic polities. High quality deliberation is traditionally thought to only be feasible in small groups and thus require processes of selection of a small group to represent a larger population such as representative government elections or sortition (choosing participants at random), but is believed to lead to richer collaboration, more complete airing of participant perspectives and therefore better eventual collective choices. On the other hand, voting can involve much larger and more diverse populations at much lower cost, but comes at the cost of each participant providing thin signals of their perspectives in the form (usually) of assent for one among a predetermined list of options.

Reminds me of some of our recent discussions from the [decentralized society](https://jeffreyfossett.com/2024/01/05/decentralized-society-IAP.html) class. 

Final piece of the discussion is about what it *means* to improve collaboration or the breadth/depth tradeoff around it. This gets into a welcome critique of the narrowness of attempts to define global welfare measures or singular measures of social progress. Glad to see this here, and also would be interested in seeing it hooked into more of the thinking about social scientific knowledge creation elsewhere in the book (per above). What is the basis of their critique: 

* This type of singular optimization is naive & papers over the plurality of ways of thinking about what is desirable about the world. Singular optimization in tension with broader goals of plurality. 
* Risks of "playing god", claiming "objective" "view from nowhere". 

Obvious connections here to STS in a way that is welcome to me. For example, see my discussion of Scott's critique of audit society I was taking notes on recently [over here](https://jeffreyfossett.com/2023/12/20/notes-on-scott.html); but of course also many other thinkers in STS on these points, as I discuss there. 

Interestingly, they also here emphasize the "opposite danger" rooted in a "ground-level view" without a "broader guiding mission". I'm not sure I fully understand the articulation here. I would have expected the emphasis to be more around the risks of a fully fractured information environment or the death of truth online or in our current politics. The points they do make here seem to be rooted more in choice about the values present in technological development rather than epistemology (what I thought they were talking about)? 

In any case, I do agree with the recommendation towards a "pragmatic, plural path", which is exactly where I landed in my discussion of the Scott piece. 

The chapter closes with some more discussion of the risks of homogenization that arise from cross-group and cross-disciplinary engagement/collaboration. The counter vision: 

> Bridging political divides may lead to excess homogenization, but it can also lead to the birth of new political cleavages

I think that there could also be a connection back to Deweyan publics here and some of the ideas in the Allen piece. Should make some more notes on this. 

### Second Read ([this](https://github.com/pluralitybook/plurality/blob/main/contents/english/5-0-collaborative-technology-and-democracy.md) version)

Discussion of [supermodularity](https://cip.org/supermodular) -- idea that whole is greater than sum of the parts. Interesting to connect that to the idea of comparative advantage. Obviously a lot of other paradigms that link up here -- e.g. "Complexity" world seems very related. Here is the connection: 

> Comparative advantage is understood as an 'economic law' stating in effect that there are guaranteed gains from diversity that can be realized through the market mechanism.

Goal of this part of the book: 

> Thus, what we will describe in this part of the book is, most precisely, how technology can empower supermodularity across social difference or, more colloquially, "collaboration across diversity".

Collaboration across diversity as a key goal. Why does it matter? 

* Oded Galor work: societies' ability to prodcutively and cooperatively harness the potential of social diversity is key driver of economic growth. Should read: 
  * Oded Galor, The Journey of Humanity: A New History of Wealth and Inequality with Implications for our Future (New York: Penguin Random House, 2022). 
  * Quamrul Ashraf and Oded Galor, "The 'Out of Africa' Hypothesis, Human Genetic Diversity, and Comparative Economic Development", American Economic Review 103, no.1 (2013): 1-46

Collaboration across diversity or difference is difficult. Different types of difference are more or less difficcult to bridge. Especially ahrd to bridge are related to systems of identification and meaning-making ("culture"). 

Interesting point here related to conversations I've had with [Jesse](https://jessecallahanbryant.com/): 

> Beyond the difficulty of overcoming difference, it also holds an important peril. Bridging differences for collaboration often erodes them, harnessing their potential but also reducing that potential in the future. While this may be desirable for protection against conflict, it is an important cost to the productive capacity of diversity in the future. The classic illustration is the way that globalization has both brought gains from trade, such as diversifying cuisine, while at the same time arguably homogenizing culture and thus possibly reducing the opportunity for such gains in the future. A critical concern, then, in ⿻ is not just harnessing collaboration across diversity but also regenerating diversity, ensuring that in the process of harnessing diversity it is also replenished by the creation of new forms of social difference.

How do you facilitate collaboration across diversity without flattening it, homogenizing it? Is this possible? I think there are real resonances here with anarchist perspectives implicit in Tang's worldview. Not just a tolerance for the messiness of difference and perspectival conflict, but an embrace of this as a fundamental value. A fundamental source of productive capacity. This is also, in a sense, embedded in the idea of gains from trade or supermodularity outlined above. 

The thesis on why collaboration need not lead to homogenization is discussed later in the chapter. Here is the idea: 

> Yet homogenization is not an inevitable outgrowth of bridging, even when one effect is to recombine existing culture and thus lessen their average divides. The reason is that bridging plays a positive, productive role, not just a defensive one. Yes, interdisciplinary bridging of scientific fields may loosen the internal standards of a field and thus the distinctive perspective it brings to bear. But it may also give rise to new, equally distinctive fields.

And further: 

> Similar phenomena emerge throughout history. Bridging political divides may lead to excess homogenization, but it can also lead to the birth of new political cleavages. Families often bear children, who diverge from their parents and bring new perspectives. Most artistic and culinary novelty is born of "bricolage" or "fusion" of existing styles.15 The syntheses that emerge when thesis and antithesis meet are not always compromises, but instead may be new perspectives that realign a debate.16

There are depth-breadth tradeoffs in collaboration. 
* Depth -- the "degree" of supermodularity for a fixed set of participants. How much greater is what they create than the sum of what they can create separately? (According to the standards of the participants). 
* Breadth -- how many individuals can participate? 

Idea of low vs high bandwidth communication. This diagram is a key one, thinking of this as [production possibility frontier](https://en.wikipedia.org/wiki/Production%E2%80%93possibility_frontier): 

<center>
<img alt="4" align="center" src="https://raw.githubusercontent.com/pluralitybook/plurality/main/figs/PPF.png" width="85%">
</center>

The idea of plural technologies is to shift out this frontier. This is a very economic frame kind of intuition about the effect of technology. Shifting "out" the PPF means that for any given level of collaborative *depth*, a higher level of breadth becomes possible. Additionally, in the picture above, there is a suggestion that 

While this intuition makes sense, a somewhat strange implication of this visualization (as drawn) is how it suggests scope for extension along the axes -- i.e. at low breadth, there is considerable scope as drawn for deepening collaboration, and likewise on the other axis (which suggests extending collaboration across more than the entire world of humans?). The quantitative labeling of the x-axis is also an interesting choice.

This example from political science is a good one for illustrating the tradeoff: 

> One example illustrating this trade-off is common in political science: the debate over the value of deliberation compared to voting in democratic polities. High quality deliberation is traditionally thought to only be feasible in small groups and thus require processes of selection of a small group to represent a larger population such as representative government elections or sortition (choosing participants at random), but is believed to lead to richer collaboration, more complete airing of participant perspectives and therefore better eventual collective choices. On the other hand, voting can involve much larger and more diverse populations at much lower cost, but comes at the cost of each participant providing thin signals of their perspectives in the form (usually) of assent for one among a predetermined list of options.

What does it mean to improve? Dual risks: 

1. Of "gods eye view". The "optimal" way to organize things. Many pitfalls -- playing "god", appealing to a disembodied perspective that does not really exist. The "right" direction for technological development. 
2. Build technologies "without a broader guiding mission" --> current predicament. (Not really without a mission, but without driving non-capitalistic values). 

Instead, a pragmatic "middle" path. The summary: 

> build tools that pursue the goals of a range of social groups, from intimate families and friends to large nations, always with an eye to limitations of each perspective and on the parallel developments we have to connect to and learn from emanating from other parallel directions of development.

And further: 

> We can do this guided by a common principle of cooperation across difference that is too broad to be formulated as a consistent objective function, yet elegant enough to unify a wide range of technologies: **we develop tools that allow greater cooperation and consensus at the same time as they make space for greater diversity**. 

## [5-1 Post Symbolic Communication](https://github.com/pluralitybook/plurality/blob/main/contents/english/5-1-post-symbolic-communication.md)

> Post-symbolic communication, a term coined by Jaron Lanier , ventures beyond the realm of language and symbols to explore the potential for direct and immersive shared experience by harnessing all senses, including proprioception

Various examples: combat, sports, romantic intimacy, religious experience, yoga. 

> Each of these contexts illustrates how shared experiences, beyond the scope of verbal communication, can create deep bonds and understanding between participants through intensive, shared sensorial inputs

Can also have post-symbolic communication within oneself -- meditation, prayer, psychedelics. 

## [5-1 Immersive Shared Reality](https://github.com/pluralitybook/plurality/blob/main/contents/english/5-2-immersive-shared-reality.md)

[1000 Cut Journey](https://www.gamesforchange.org/games/1000-cut-journey/). Summary from the site for the game: 

> Achieving racial justice requires that we understand racism. Not only an understanding that emerges from intellectual exercise or even in the consumption or production of science – but rather a visceral understanding that connects to spirit and body as much as reason.

> 1,000 Cut Journey is an Immersive Virtual Reality experience in which participants embody a Black male, Michael Sterling, experiencing racism as a child through disciplinary action in the classroom, as an adolescent encountering the police, and as a young adult experiencing workplace discrimination.

This organization looks cool: https://www.gamesforchange.org/

From book: 

> Immersive shared reality technologies unlocks a new chapter in human interaction, leveraging cutting-edge virtual reality (VR), augmented reality (AR) and mixed reality (MR) systems. Unlike the deeply personal and sensorially rich exchanges of post-symbolic communication, shared immersive reality presents a broader canvas for human interaction, enabling people to engage in shared, multisensory experiences.

> ISR refers to technology that creates a shared virtual environment where users can interact in real-time. 

Interesting examples from art world: 

> Immersive artistic experiences: Alongside the rise of remote shared experience, a new genre of in-person immersive art has developed and become and increasingly prevalent form at the intersection of live entertainment and museums. Participants jointly explore mysteries, escape from puzzles, live in the world of an artist who saw the world through differently abled eyes, or surround themselves in worlds of novel tactile and visual sensations that transport them to new shared understandings of the possible

It seems like one of the key points here is that there seems to be scope for a lot more expansion in this vein of technology. 

---
layout: post
title: "Plurality Reading Group Prep"
date: 2024-04-23
latex: true
mathjax: true
comments: true
tag: ["plurality", "notes"]
---

With [Eugene](https://twitter.com/bbeats1) and [Plurality Institute](https://www.plurality.institute/), I am co-organizing a reading group, which will start by discussing the [Plurality Book](https://www.plurality.net/chapters/) by Weyl and Tang. In this post, I will keep some notes on my latest reading of the book, specifically with an eye toward the book club. My previous notes are [here]({% post_url 2023-12-27-notes-on-plurality-book %})

## Part 0 

In [Finding your Dao](https://www.plurality.net/v/chapters/0-2/eng/?mode=dark) they suggest that the book can be read in any order and has a "circular" structure. They suggest: 

> * Those with a primarily topical, political or current affairs interest begin at the beginning of the book, with the preface and read straight through.
> * Those with a more conceptual, theoretical or broadly intellectual interest consider skipping Parts 1 and 2 and beginning in Part 3.
> * Those with a more technical, technological or engineering focus consider beginning with Part 4.
> * Those with an interest in concrete technologies and their applications consider beginning with Part 5.
> * Those with an interest in real-world impact in specific social sectors consider beginning with Part 6.
> * Those with a focus on public policy, government and social mobilization consider beginning with Part 7.

While we will start with parts 1-3 in the book club (since we have to start somewhere), we will do quadratic voting after the first session to decide what we read next. I guess just choosing between sections 4,5,6 vs. 7 seems like a good way to set this up. 

## Part 1 - Seeing Plural

This section sets the stage. At core, the book is about democracy (vs autocracy), digital technology, and plurality / collaboration. 

> The internet is a powerful technology for tying people together in new collaborations across vast differences. Unfortunately, it has also recently proven to be a powerful tool for thwarting those collaborations and sowing new forms of division.

> It is no coincidence that democracy now finds itself at a low tide. Authoritarian regimes now command nearly half of the global GDP. Only a modest one billion people find solace under the umbrella of democratic systems, while over two billion dwell under authoritarian rule.

> In Mandarin, 數位 means both "digital" and "plural." To be plural is to be digital. To be digital is to be plural.

> Plurality captures the symbiotic relationship between democracy and collaborative technology. Together, democracy and collaborative technology can power infinite diversity in infinite combinations.

## Part 2 - Introduction

### [Section 2-0 - INFORMATION TECHNOLOGY AND DEMOCRACY: A WIDENING GULF](https://www.plurality.net/v/chapters/2-0/eng/?mode=dark)

Basic claim of this chapter: (digital) technology and democracy are in tension with one other in various ways. But this need not be the case: 

> In this book, we hope to show that this tragic conflict is avoidable and that, properly conceived, technology and democracy can be powerful and natural allies

The purpose of the analysis in this section, then, is to draw out the architecture of this conflict so as to have a chance to overcome it. 

**Technology's attack on democracy**: basic idea is that information technologies seem to be "narrowing the corridor" (between societal collapse & authoritarianism). They bucket the issues into consequences for the two sides of the corridor: 

* "Anti-social" threats: breaking down the social fabric, heightening polarization, eroding norms, undermining law enforcement and accelerating the speed and expanding the reach of financial markets to the point where they are unaccountable to democratic polities
    * Social media has exacerbated feelings of poor mental health, social isolation, exclusion
    * Rise of flexible ad hoc work, but without complementary labor market instituions / protections. 
    * Political polarization via algorithmic curation, filter bubbles etc. 
* "Centralizing" threats: e.g. technologies of surveillance & manipulation. 
    * Eroded sphere of private life -- proliferation of digital data / data exhaust etc.: 
        > While such transparency might in principle have a range of social effects, the power to process and make sense of such information has increasingly concentrated in the hands of corporations and firms that have a combination of privileged access to the information and the capital to invest in large scale statistical models (viz. “AI”) to make these data actionable. Furthermore, because these models improve greatly with access to more data and capital, societies where central actors have access to very large pools of both have tended to pull ahead in the perceived “AI race”, putting pressure on all societies to allow such concentration of informational power to compete
    * Economically 
        > there is growing evidence that AI and the related broader tendency of information technology since the mid-1980s to replace rather than complement (especially low-educated) human labor has been a central factor in the dramatic rise in the share of income accruing to capital (rather than labor) in past decades and thereby has been a core cause of increased income inequality in developed countries. A rise in market power, mark-ups and (less consistently) industrial concentration around the world has accompanied this decline in labor’s share, particularly in countries and sectors that have most heavily adopted information technology

**Democracies' hostility to technology**. This is an interesting point that I don't see many folks making in this context:  

> Where once the public sector in democratic countries was the global driving force behind the development of information technology (e.g. the first computers, the internet, global positioning satellites), today most democratic governments are focused instead on constraining its development

It's nothing crazy, but it does seem true to me that much government / regulatory discourse takes the form of critique / control -- managing risks/harms etc. vs more constructively articulating/supporting/funding a constructive vision for technological development. Of course, there are conversations in this latter tone, but they are seemingly conversations that are had by a fairly different set of policymakers/advisors (e.g. innovation economists rather than critical tech folks). In general, I think I am sympathetic to the idea that those two veins of policymaking are both available, and can / should / could work together more? With AI, it seems that we *are* seeing some of this e.g. with the [NAIRR](https://new.nsf.gov/focus-areas/artificial-intelligence/nairr) initiative. 

They make four specific empirical claims about declining democratic support for tech: 

1. Techlash: policy-makers are increasingly hostile to large technology companies and even many technologists
2. Reduced direct investment 
3. Public sector is slow to adopt new technology. 
4. "Democratic governments have largely failed to address the areas where most technologists believe public participation, regulation, and support are critical to technology advancing in a sustainable way, focusing instead on more familiar social and political problems" 

I don't really understand what they have in mind with point (4)  here. The citation says something about open source, so maybe that is what they are thinking of support for OSS? 

On point (1) -- this is intuitive to me, though I do think it would be interesting to see a more systematic review of the data here. [Jesse](https://jessecallahanbryant.com/) and I had a conversation the other day about this, and had different intuitions about the extent to which the pbulic is critical of digital technology in general. Certainly a key distinction here is around attitudes towards "big tech" companies vs. (their) technologies more generally. It seems there are also big stated vs. revealed preferences considerations to unpack with this kind of topic--e.g. people say they hate Meta/big tech, but then also spend all day scrolling on Instagram (digital addiction is also a concern). To Jesse's point, there is clearly a way in which we are still societally deeply invested in our digital tools, even if we are unhappy e.g. with some of their corporate patrons. In general this does seem like an important but easy to forget -- if obvious -- point: namely, that corporate 

Point (3) is also interesting to think more about and is something I've engaged with a bit. A few reactions: 

* First, I am not sure whether this is true across all public contexts. For example, we have seen ready adoption of e.g. ML tools for predictive policing, and recidivism risk assessment etc, which have brought with them much justified worry about equity, fairness, transparency etc. See e.g. controversy around COMPAS. 
* In general, on this theme, I am not sure how fast we *do* want the public sector be adopting new technologies. Unlike private firms, governments *should* be cautious and probably slow in adopting new things, taking care to ensure that they are ethical, fair, accountable etc. They cannot be "moving fast and breaking things" in the same way as private firms (where this ethos has also proved problematic). A good topic for discussion is -- what is the right balance here? 

Also, to the extent that government has been slow in adopting new technology -- I am not sure how much this has to do with attitudes towards technology in general vs. a broader set of challenges around adaptivity / pace of change in large adminstrative institutions.

This point about public investment in Web3 seems a *bit* odd: 

> the recent movements around “web3” and decentralized social technologies have received virtually no public financial support

There is clearly a central antagonism between web3 tech imaginaries, and engagement with state actors which can partly explain this. However, the point about public involvement with GFMs etc. seems more apt (though see some efforts linked above around NAIRR).

They make this comparison with authoritarian regimes pace of innovation. Certainly this is true, but to what extent is it just a fundamental necessity of these public forms? Like: the pace of policy change* in general* is presumably slower in democratic contexts; that is like part of the point -- deliberation, voting, consensus-formation all take time. Even in the most efficient possible setting of democratic collaboration, authoritarian decision-making will always be better/faster. And like here: 

> Most ambitiously, democracies could, as so many autocracies have been doing, help facilitate radical experiments with how technologies could reshape social structures. Yet, here again, democracy seems so often to stand in the way rather than facilitate such experimentation. The PRC government has built cities and reimagined regulations to facilitate driverless cars, such as Shenzhen, and has more broadly built a detailed national technology strategy covering nearly every aspect of policy, regulation and investment.27 Saudi Arabia is busy building a new smart city in the desert, Neom, to showcase a range of green and smart city technology, while even the most modest localized projects in democratic countries, such as Google’s Sidewalk Labs, have been swamped by local opposition.28

This feels odd because like -- if the demos *doesn't want* some sort of experimentation e.g. like Sidwalk Labs...that seems like a good thing if it gets blocked and the demos wins out? Like I guess I take the point that that feels like antagonism for some technologists. But it's like *good* antagonism?

Similarly here: 

> There is a growing consensus among technologists that a range of emerging technologies may pose catastrophic or even existential risks that will be hard to prevent after they start to emerge. Examples include artificial intelligence systems that could rapidly self-improve their capacities, cryptocurrencies that could pose systemic financial risks, and the development of highly contagious bioweapons. They regularly bemoan the failure of democratic governments to even contemplate much less plan to confront such risks.

This point is better since it compares democratic investment in public infrastructure to itself historically: 

> Digitization of conventional public services is perhaps the least ambitious dimension along which one might expect democracies to advance in adopting technology. Technology has redefined what services are relevant and in these novel areas, democratic governments have almost entirely failed to keep up with changing times. Where once government-provided postal services and public libraries were the backbone of democratic communication and knowledge circulation, today most communication flows through social media and search engines. 

**Ideologies of the twenty-first century** 

Points about sociotechnical imaginaries are well taken and worth discussing more. Interesting comparative point about how things have aligned across nation states in different ways. 

I think there is a much richer analysis probably available (e.g. from STS angle) about the ways in which we are making choices about what forms of technological development to support. 

They outline two main imaginaries: 

* Artificial Intelligence and technocracy
* Crypto and hyper-capitalism

I do see these around but is this point true? 

> These two ideologies have, to a significant extent though often in moderated form, dominated public imagination about the future of technology in most liberal democracies and thus shaped the direction of technology investment for most of the last half-century

I guess it seems to me that there are a bunch of interlocking ideologies here. 

I am reminded of the influential [Californian Ideology](https://en.wikipedia.org/wiki/The_Californian_Ideology).

Conclusion of this section: 

> Another path is possible. Technology and democracy can be each other’s greatest allies. In fact, as we will argue, large-scale “Digital Democracy” is a dream we have only begun to imagine, one that requires unprecedented technology to have any chance of being realized

In general, I guess that something I want to think more about is like: which parts of the critique from both sides (technology, democracy) am I sympathetic to?

### View from Yushan

Sunflower movement a key inspiration point ([wiki](https://en.wikipedia.org/wiki/Sunflower_Student_Movement)). 

> Perhaps most importantly, the movement led to a deeper and more lasting shift in politics, as the government at the time gained respect for the movement and ministers invited younger "reverse mentors" to help them learn from youth and civil society.

I heard Audrey speak about this idea of reverse mentors [here](https://www.youtube.com/watch?v=ZtW6c8tOYMw), and it seems liek a great idea. 

On the politics and political division of Taiwan. Different parties "correspond to different facets and imaginations of what "this place is."" 

* Democratic Progressive Party 
* Kuomintang (KMT or Nationalist) party - "Taiwan is defined by most of its people speaking Chinese languages such as Mandarin, Taigi (Taiwanese Hokkien) and Hakka. Some would go as far as to argue that Taiwan is more ethno-historically "Chinese" than the PRC"

> a system of alternation between the Blue vision of "free China" and the Green vision of "island nation" was established as the pattern of politics.

Connections between George/Dewey and the ROC historically is not something I understood. [This reference](https://www.academia.edu/3125320/_Pragmatism_and_East_Asian_Thought) seems pretty interesting: 

> this fluid, experimental and emergent approach [from Dewey / pragamatists] shared much with Taoist traditions popular among democratic opponents of Qing and warlord monarchy

I have been wanting to read more about this connection. They also offer [this](https://taiwantoday.tw/news.php?unit=12,29,33,45&post=22731) link. 

I was also ignorant of the history of the ROC, the PRC and the UN: 

> The United Nations was central to the ROC's early identity under the White Terror as it was not only one of the founding members of the UN, but also the only Asian permanent member of the Security Council. This prominent international role was the leading irritant to the People's Republic of China (PRC) regime, preventing it from participating in international affairs and leading the CCP to change its position from initially supporting Taiwanese independence to an ideological focus on conquering Taiwan. However, as the US sought to contain its failures in Vietnam, President Richard Nixon secretly pursued accommodation with the PRC, including supporting an Albanian-sponsored Resolution 2758 by the General Assembly on October 25, 1971 that transferred recognition of "China" from the ROC to the PRC, finally culminating in Nixon's visit to PRC in 1972. As a result, the ROC "withdrew" from the UN, transforming its identity and international standing.

Taiwan democracy & emergence of digital sphere co-evolve / develop around same time in 90s. 

### Life of a Digital Democracy 

Goal: 

> Thus we aim here to provide concrete illustrations and quantitative analyses of what distinguishes Taiwan's digital civic infrastructure from those of most of the rest of the world

g0v is a big one: 

> Founded in 2012 by civic hackers including Kao Chia-liang, g0v arose from discontent with the quality of government digital services and data transparency.1 Civic hackers began to scrape government websites (usually with the suffix gov.tw) and build alternative formats for data display and interaction for the same website, hosting them at g0v.tw. These "forked" versions of government websites often ended up being more popular, leading some government ministers, like Simon Chang to begin "merging" these designs back into government services.

In general it's interesting that this is something that really started from *outside* government and then was re-integrated. I wonder why that is not something that happens more in the US? Or maybe it does? Or could? It would be neat to invite some of the civic hackers behind these tools to the group for discussion to hear more about how / why they created these things and what is the story of them. 

Another point that is interesting about g0v is the presence of "hackathons" that incorporate diverse -- and especially non-technical -- participants. How is this inclusiveness accomplished? 

This story is great but I am not sure how to replicate it:

> The contributions of g0v to both sides and the resolution of their tensions led the sitting government to see the merit in g0v's methods and in particular cabinet member Jaclyn Tsai recruited one of us as a youth "reverse mentor" and began to attend and support g0v meetings, putting an increasing range of government materials into the public domain through g0v platforms.

As told here, it seems like the success of this movement is some function of: 

1. The tools that were created by the civic tech community were particularly "good". But also: 
2. A real wisdom / humility / openness on behalf of people like Tsai in the government who humbly recognized the merit of these efforts and brought them into the fold. What accounts for this? 

Same for vTaiwan and Pol.is. They say that: 

> vTaiwan was deliberately intended as an experimental, high-touch, intensive platform for committed participants

(When) is such experimentalism available in US government insitutions? Also, they note that there is this challenge with these types of initiatives around "the absence of mandates for governmental responses", which is a broader point of concern. 

In general, a key reaction for me from this section is about the close collaboration between government and civil society, which is not something that I see so much of in the US? Though maybe I am not paying enough attention. 

On this point: 

> While this is an interesting set of programs, one might naturally inquire about evidence of their efficacy. Tracing causal impacts precisely for so many projects is obviously an arduous task beyond our scope here

It seems that more causal research here could / should be possible; it would be great to see more of this. Same here: 

> It will doubtless take decades of study to understand the precise causal connections between Taiwan's unique and dramatic digital democratic practices and the range of success it has found in confronting today's most vexing challenges. Yet given this appeal, in the interim, it seems critical to articulate as so many have done for Scandinavia and Singapore, the generalizable philosophy behind the strategies of the world's most admired digital democracy. It is to that task that the rest of this book is devoted.

## Part 3- Plurality 

### What is Plurality? 

Briefly, plurality is "technology for collaboration across social difference". 

> break Plurality into three components (descriptive, normative and prescriptive) each associated with one of three thinkers (Hannah Arendt, Danielle Allen and Audrey Tang) each of whom has used the term in these three distinct and yet tightly connected ways

More complex definition with three components: 

* **Descriptive** (Arendt): "The social world is neither an unorganized collection of isolated individuals nor a monolithic whole. Instead, it is a fabric of diverse and intersecting affiliations that define both our personal identities and our collective organization". 
    * This is a point about identity, and what are the features of the units of interest. Interesting to compare this with our previous discussion about ontology in Dewey. 
* **Normative** (Allen): "Diversity is the fuel of social progress and while it may explode like any fuel (into conflict), societies succeed largely to the extent they manage to instead harness its potential energy for growth". (A Connected Society). 
    * Also connect this to Dewey and George. 
* **Prescriptive** (Tang): "Digital technology should aspire to build the engines that harness and avoid conflagration of diversity, much as industrial technology built the engines that harnessed physical fuel and contained its explosions"

These seem like great references to add to the Plurality syllabus. 

### Living in a Plural world 

Claim that technocratic and libertarian perspectives are reooted in "monist atomist" understanding of people. 

Plurality analogies with scientific elements. 

* "Edge of chaos" where complex behaviors can emerge (neither too orderly nor too chaotic). Goal of plurality is to widen this corridor. 

I am not too sure what to make of all these referencces to quite diverse and ranging scientific/computational/mathematical concepts -- what are we supposed to take from these analogies? 

Here is what they say: 

> ⿻ is, scientifically, the application of an analogous perspective to the understanding of human societies and, technologically, the attempt to build formal information and governance systems that account for and resemble these structures as physical technologies built on ⿻ science do

Then: 

> Perhaps the crispest articulation of this vision appears in the work of the leading figure of network sociology, Mark Granovetter

What are we supposed to take from Granovetter? Here is what they say: 

> There is no basic individual atom; personal identity fundamentally arises from social relationships and connections. Nor is there any fixed collective or even set of collectives: social groups do and must constantly shift and reconfigure. This bidirectional equilibrium between the diversity of people and the social groups they create is the essence of ⿻ social science.

I feel like I need more here as far as what the takeaway is. Are they saying we should all be network scientists? There is a set of references that they claim substantiate this perspective, but I am not too familiar with many of them: 

> Scott Page, The Difference: How the Power of Diversity Creates Better Groups, Firms, Schools, and Societies, (Princeton: Princeton University Press, 2007); César Hidalgo, Why Information Grows: The Evolution of Order, from Atoms to Economies, (New York: Basic Books, 2015); Daron Acemoglu, and Joshua Linn, “Market Size in Innovation: Theory and Evidence from the Pharmaceutical Industry,” Library Union Catalog of Bavaria, (Berlin and Brandenburg: B3Kat Repository, October 1, 2003), https://doi.org/10.3386/w10038; Mark Granovetter, “The Strength of Weak Ties,” American Journal of Sociology 78, no. 6 (May 1973): 1360–80; Brian Uzzi, “Social Structure and Competition in Interfirm Networks: The Paradox of Embeddedness,” Administrative Science Quarterly 42, no. 1 (March 1997): 35–67. https://doi.org/10.2307/2393808; Jonathan Michie, and Ronald S. Burt, “Structural Holes: The Social Structure of Competition,” The Economic Journal 104, no. 424 (May 1994): 685. https://doi.org/10.2307/2234645; McPherson, Miller, Lynn Smith-Lovin, and James M Cook. “Birds of a Feather: Homophily in Social Networks.” Annual Review of Sociology 27, no. 1 (August 2001): 415–44.

Seems mostly likely network science type ideas though. 

They also have this example of "metascience"; I kind of get it, but also seems like much of this overlaps with existing ideas in economics of science and economics of innovation? They mostly reference James Evans' work here, so maybe I should read some more of that to understand the distinctions: 

* Valentin Danchev, Andrey Rzhetsky, and James A Evans, “Centralized Scientific Communities Are Less Likely to Generate Replicable Results.” ELife 8 (July 2, 2019), https://doi.org/10.7554/elife.43094. ↩
* Alexander Belikov, Andrey Rzhetsky, and James Evans, "Prediction of robust scientific facts from literature," Nature Machine Intelligence 4.5 (2022): 445-454. ↩
* Lingfei Wu, Dashun Wang, and James Evans, "Large teams develop and small teams disrupt science and technology," Nature 566.7744 (2019): 378-382. ↩
* Yiling Lin, James Evans, and Lingfei Wu, "New directions in science emerge from disconnection and discord," Journal of Informetrics 16.1 (2022): 101234. ↩
* Feng Shi, and James Evans, "Surprising combinations of research contents and contexts are related to impact and emerge with scientific outsiders from distant disciplines," Nature Communications 14.1 (2023): 1641. ↩
* Jacob Foster, Andrey Rzhetsky, and James A. Evans, "Tradition and Innovation in Scientists’ Research Strategies," American Sociological Review 80.5 (2015): 875-908. ↩

What seems to make this a "plurality" perspective is that it is grounded in "many intersecting levels of social organization" /  

### Connected Society

Key influences: 

> Georg Simmel, one of the founders of sociology, originated the idea of the "web" as a critique of the individualist concept of identity

> John Dewey, widely considered the greatest philosopher of American democracy, argued that the standard national and state institutions that instantiated the idea hardly scratched the surface of what democracy required

> Norbert Wiener coined the term "cybernetics" for a field studying such rich interactive systems

I guess the idea that many standard institutions of liberal democracy rest on "monist atomist" foundations. And so there is scope to reimagine these institutions in line with a more plural foundation. Especially: property, identity, and voting. 

**Property**: strong sense of individual or family ownership. In contrast with "property regimes that have prevailed in most human societies throughout most of history, in which individual ownership was rarely absolutely institutionalized and a diversity of "traditional" expectations governed how possessions can rightly be used and exchanged"  
* Counterpoint: Henry George. Savannah example. Value of an asset is not fundamentally individual in many cases. They say: 
    > The value of their land, George insisted, could not justly belong to that family: it was a collective product that should be taxed away. Such a tax was not only just, it was crucial for economic development, as highlighted especially by later economists including one of the authors of this book. Taxes of this sort, especially when carefully designed as they were in Taiwan, ensure property owners must use their land productively or allow others to do so.
* "The world George invites us to reflect on and imagine how to design for is thus one of ⿻ value, one where a variety of entities, localized at different scales (universities, municipalities, nation states, etc.) all contribute to differing degrees to create value, just as networks of waves and neurons contribute to differing degrees to the probabilities of particles being found in various positions or thoughts occurring in a mind. And for both justice and productivity, property and value should belong, in differing degrees, to these intersecting social circles" 
* In general, a big point they highlight in George is the idea of networked value. 

**Identity**: "Prior to modernity, individuals were born into families rooted within kin-based institutions that provided everything, livelihood, sustenance, meaning, and that were for the most part inescapable. No "official documents" were needed or useful as people rarely traveled beyond the boundaries of those they knew well. " 

* Interesting point here that identity has actually about relationship to the state rather than position in embedded social networks. 
* Simmel an influence here: 
    > Simmel’s “intersectional” theory of identity offered an alternative to both the traditional individualist/atomist (characteristic at the time in sociology with the work of Max Weber and deeply influential on Libertarianism) and collectivist/structuralist
    * This point reminds me of [MacIntyre](https://jeffreyfossett.com/2021/11/15/partiality-and-carbon-chauvinism.html) *Is Patriotism a Virtue*
        > In his view, humans are deeply social creatures and thus their identities are deeply formed through their social relations. Humans gain crucial aspects of their sense of self, their goals, and their meaning through participation in social, linguistic, and solidaristic groups.

**Voting**: "one person one vote" as the be all end all. "Again this contrasts with decision-making structures throughout most of the world and most of history, including ones that involved widespread and diverse representation by a range of social relationships, including family, religious, relationships of fealty, profession, etc.6 We again see the same pattern repeated: liberal states have "extracted" "individuals" from their social embedding to make them exchangeable, detached citizens of an abstracted national polity."

Interestingly, a lot of this seems to be about knock-on effects of 'state legibility' in the James Scott type of sense. In general, seems like they should have *Seeing Like a State* reference in here somewhere. Do they want to undercut the centering of these elements in relationship to the state? Or do they just want to change the intellectual foundations of this centering? 

> Governments and organizations around the world adopted these systems for some good reasons.

So they do acknowledge the (real) benefits of many of these systems. Yet also: 

> Yet just as the Euclidean-Newtonian worldview turned out to be severely limited and naïve, ⿻ social science was born by highlighting the limits of these atomist monist social systems.

There's a kind of interesting but not super substnatiated theory here of where individualism comes from: 

> In his view, humans are deeply social creatures and thus their identities are deeply formed through their social relations. Humans gain crucial aspects of their sense of self, their goals, and their meaning through participation in social, linguistic, and solidaristic groups. In simple societies (e.g., isolated, rural, or tribal), people spend most of their life interacting with the kin groups we described above. This circle comes to (primarily) define their identity collectively, which is why most scholars of simple societies (for example, anthropologist Marshall Sahlins) tend to favor methodological collectivism.14 However, as we noted above, as societies urbanize social relationships diversify. People work with one circle, worship with another, support political causes with a third, recreate with a fourth, cheer for a sports team with a fifth, identify as discriminated against along with a sixth, and so on. These diverse affiliations together form a person’s identity. The more numerous and diverse these affiliations become, the less likely it is that anyone else shares precisely the same intersection of affiliations.

> As this occurs, people come to have, on average, less of their full sense of self in common with those around them at any time; they begin to feel “unique” (to put a positive spin on it) and “isolated/misunderstood” (to put a negative spin on it). This creates a sense of what he called “qualitaitive individuality” that helps explain why social scientists focused on complex urban settings (such as economists) tend to favor methodological individualism

**Dewey**. Love him of course. What are some of the key points they draw out from his analysis: 

> Dewey focused specifically on the role of technology in creating new forms of interdependence that created the necessity for new publics

What is the issue? 

> The problem is that existing democratic institutions are not, in Dewey’s view, truly democratic with regards to the emergent challenges created by technology.

What makes something truly democratic to Dewey is: 

> Core to true democracy is the idea that the “relevant public”, the set of people whose lives are actually shaped by the phenomenon in question, manage that challenge. Because technology is constantly throwing up new forms of interdependence, which will almost never correspond precisely to existing political boundaries, true democracy requires new publics to constantly emerge and reshape existing jurisdictions.

The role of "experts" / leaders is in cultivating new publics / helping them understand themselves as a public and emerge. 

>  Dewey’s conception of democracy and emergent publics is at once profoundly democratic and yet challenges and even overturns our usual conception of democracy. Democracy, in this conception, is not the static system of representation of a nation-state with fixed borders. It is a process even more dynamic than a market, led by a diverse range of entrepreneurial mirrors, who draw upon the ways they are themselves intersections of unresolved social tensions to renew and re-imagine social institutions

So they like him for the dynamism and fluidity of his vision of democracy. 

What is the key link across all these different ideas? 

> Across all of these authors, we see many common threads. We see appreciation of the ⿻ and layered nature of society, which often shows even greater complexity than other phenomena in the natural sciences: while an electron typically orbits a single atom or molecule, a cell is part of one organism, and a planet orbits one star, in human society each person, and even each organization, is part of multiple intersecting larger entities, often with no single of them being fully inside any other. **But how might these advancements in the social sciences translate into similarly more advanced social technologies?**

Norbert Wiener & Cybernetics as an influence. 

### The Lost DAO 

Here is a clear statement of the broader agenda: 

> Liberal democracies often celebrate themselves as pluralistic societies, which would seem to indicate they have already drawn the available lessons from ⿻ social science. Yet despite this formal commitment to pluralism and democracy, almost every country has been forced by the limits of available information systems to homogenize and simplify social institutions in a monist atomist mold that runs into direct conflict with such values. The great hope of ⿻ social science and ⿻ built on top of it is to use the potential of information technology to begin to overcome these limitations.

The Information Processing Techniques Office led by *Joseph Carl Robnett (JCR) Licklider*

JC Licklider had background in psych, AI themes. Interested in human-machine collaboration. MIT Lincoln Lab. ARPA. 

Lick was particularly focused on "human factors" in computing. 

> he gave particular attention and support to projects he believed could bring computing closer to the lives of more people, integrating with the functioning of human minds

Story about the origin of the internet. Key takeaway: 

> At the core of the development of what became the internet was replacing centralized, linear and atomized structures with ⿻ relationships and governance

Three dimensions: 

> packet switching to replace centralized switchboards,
> hypertext to replace linear text,
> open standard setting processes to replace both government and corporate top-down decision-making

In this context, ⿻ really just means "networked"? I.e. decentralized / not hierarchical? What were the motivations for this decentralized network approach? 

1. Technical resilience
2. Creative expression

Where did (2) inspiration come from? Margaret Mead's "Margaret Mead's vision of democratic and pluralistic media" 

==> Ted Nelson and "Project Xanadu" 

> Nelson imagined hypertext as a way to liberate communication from the tyranny of a linear interpretation imposed by an original author, empowering a "pluralism" (as he labeled it) of paths through material through a network of (bidirectional) links connecting material in a variety of sequences. This "choose your own adventure"17 quality is most familiar today to internet users in their browsing experiences but showed up earlier in commercial products in the 1980s (such as computer games based on hypercard). Nelson imagined that such ease of navigation and recombination would enable the formation of new cultures and narratives at unprecedented speed and scope. The power of this approach became apparent to the broader world when Tim Berners-Lee made it central to his "World Wide Web" approach to navigation in the early 1990s, ushering in the era of broad adoption of the internet.

This is an interesting thing to think about more. Makes me think of websim.ai a bit as a contemporary example. In general LLMs present many opportunities for richer non-linear pathways through a set of information.

> At the core of the approach was the vision of a "network of networks" that gave the "internet" its name: that many diverse and local networks (at universities, corporations and government agencies) could inter-operate sufficiently to permit the near-seamless communication across long distances, in contrast to centralized networks (such as France's concurrent Minitel) that were standardized from the top down by a government.18 Together these three dimensions of networking (of technical communication protocols, communicative content and governance of standards) converged to create the internet we know today.

Claim that Ted Nelson foresaw all the limitations of the Web. 

This seems like a good cite to potentially add to the Plurality syllabus: 

> As early as 1980, while TCP/IP was coalescing, Lick foresaw in his classic essay "Computers and Government" "two scenarios" (one good, the other bad) for the future of computing: it could be dominated and its potential stifled by monopolistic corporate control or there could be a full societal mobilization that made computing serve and support democracy

I want to dig in more on these claims that various early internet pioneers foresaw various risks in the design of the internet. Mainly the people cited are Nelson, Lick. Also Jaron Lanier. Here is the punchline claim of what happened: 

> How did we fall into a trap clearly described by the founders of hypertext and the internet? After having led the development of the internet, why did government and the universities not rise to the challenge of the information age following the 1970s?

Is that true? In any case, their explanation for what happened is that for various historical contingent reasons, there was declining public/social sector investment in internet development. This led to key technical ideas that internet pioneers thought necessary being left by the wayside -- identity, privacy/security, asset sharing, commerce. Instead, private sector took over and served these needs. I should read this story against Shane's book. 

**Wikipedia** as a key example o a more pluralistic model. 

> In contrast to the informational fragmentation and conflict that pervades much of the digital sphere that we highlighted in the introduction, Wikipedia has become a widely accepted source of shared understanding.

Some key features: 

* Linked structure
* Self-governance 
* Inclusiveness: "Wikis invite all users, not just experts, to edit or create new pages using a standard web browser and to link them to one another, creating a dynamic and evolving web landscape in the spirit of ⿻." 

Wikis as a broader kind of movement. HackMD as an example. We should use one of these for reading group notetaking. OSS. 

> This represents the practice of ⿻ on a large scale; emergent, collective co-creation of shared global resources. Communities form around shared interests, freely build on each other’s work, vet contributions through unpaid maintainers, and "fork" projects into parallel versions in case of irreconcilable differences

Integration with web3 world? Here is what they say about it: 

> While many projects in the (web3) space have been influenced by Libertarianism and hyper-financialization, the enduring connection to original aspirations of the internet, especially under the leadership of Vitalik Buterin (who founded Ethereum, the largest smart contract platform), has inspired a number of projects, like GitCoin and decentralized identity, that are central inspirations for ⿻ today as we explore below.

They also connect with fediverse ecosystem. Beth Noveck cite! 

## Discussion Questions 

* What is the current state of public opinion in relation to digital technology? 
* What is the "right" pace of digital technology adoption in the public sector? 
* To what extent are we sympathetic to the grievances on the two sides of this divide -- technology / democracy?
* Connection between policy conversations on (1) tech regulation / antitrust on the one hand and (2) public investment on the other hand is interesting question. 
    * Current state of this -- e.g. considering the NAIRR? 
* Discussion about sociotechnical imaginaries & the many pathways of tech development in relationship to democracy?
* Discussion on "tech solutionism" 
* Discussion on civic tech space in the US? Why have these initiatives been so successful in Taiwan? Is such a movement possible here? If so, how? If not, why not? 
    * How much of the success in Taiwan has to do with the civic hacking community being particularly vibrant etc. vs. the culture from the government side being particularly open / humble / willing to integrate new ideas? 
* What do we make of 3-1's concept of "plural social science"? What direction is this pointing? Is it towards network science? Something different? I don't feel like the ideas here are super well developed? What is the real methodological preference that is being suggested here? 


## Plurality References

* Georg Simmel
* John Dewey
* Henry George
* Norbert Wiener
* [The Dream Machine](https://www.amazon.com/Dream-Machine-M-Mitchell-Waldrop/dp/1732265119)
* Licklider, "Comptuers and Government", op. cit. ↩
* OSS work -- Working in Public (Nadia Eghbal (now Asparouhova))




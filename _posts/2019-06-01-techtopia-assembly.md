---
layout: post 
title: "Automated Decision-Making Systems in Municipal Governments" 
date: 2019-06-01
latex: true 
mathjax: true
comments: true
---

This past year, I was part of the inaugural [Techtopia](https://cyber.harvard.edu/projects/techtopia) cohort at the Berkman Klein Center (note: this program later merged with the "[Assembly](https://www.berkmankleinassembly.org/)" program), organized by Jonathan Zittrain within the [Ethics & Governance of AI Initiative](https://cyber.harvard.edu/topics/ethics-and-governance-ai). The program involved participating in a series of resesearch seminars alongside an interesting cohort of other students from across the university, as well as the completion of a group project in the spring semester. 

For the project phase, I helped develop the "Technology Procurement Playbook Project" alongside a great team[^1]. Our team's deliverable was a playbook intended for municipal governments to help guide the procurement and development of automated decision-making systems (i.e. algorithms & machine learning products). The aim was to provide broad guidance for local government nationwide by examining the principles and processes required to ensure that municipal technology empowers, rather than harms citizens, and respects various moral/ethical considerations like equity, fairness & accountability. We developed the playbook through conversations with stakeholders in Boston city governemnt as well as academic experts and independent research. 

While the project so far has not made it out of the "draft" phase, I wanted to reflect a bit on what I learned from engaging with it[^2]. I will highlight two main buckets of learnings. 

First, I learned a set of things about the context of deploying automated decision-making systems in local governments. Three main points jump out for me here: 

1. There is a clear need for this type of technical guidance in local governments, 
2. Academia & civil society can play a meaningful role in addressing this need, and 
3. Procurement processes are (even if "unsexy") a very reasonable site of intervention for technology ethics & governance questions in this context. 

The learnings around (1) and (2) mainly arose out of our conversations with local government stakeholders, who are facing real questions / needs around deploying automated decision-making systems (i.e. algorithms & machine learning), and have both very limited resources (in terms of time, technical background etc.), and a strong interest in deploying these systems responsibly. 

On point (3), procurement is a relevant point of intervention for two reasons. First, local governments are often working with third-party contractors to develop or procure these systems rather than building them in-house (due to technical limitations). Second, the procurement process puts government stakeholders face-to-face with contractors and is a high-leverage moment (before a purchase commitment is made) to ask questions or extract concenssions from contractors around moral / ethical / governance issues that are relatively more important to government stakeholders in the negotiation[^3].

Second, I learned that making general recommendations around the responsible deployment of automated decision-making systems -- that will apply across various complex sociotechnical contexts -- is hard. This is true for all of the same reasons that social science and policy are hard: social contexts are complex and particular, and the specific issues that might arise in deploying a new technical system--and the best ways to address them--are likewise varied and difficult to predict ex ante. So what can we do? In my understanding of our approach in the Playbook, we address this issue by first outlining a broad range of *potential* algorithmic harms for stakeholders to consider up front, and second by detailing generalizable processes for creating *algorithmic accountability* -- that is, processes for (i) detecting, (ii) creating responsibility for, and (iii) redressing/mitigating any harms that might arise in the deployment of automated decision-making sytems. 

The basic idea in focusing on accountability is that, while it might be difficult to predict up front everything might go wrong in a particular context (especially with limited technical resources), governments can at least take steps to ensure that there are robust systems for detecting and addressing these issues (possibly with help from academia & civil society) before they become bigger problems. Hence our recommendations around accountability included taking steps toward public disclosure of algorithmic processes[^4] & ensuring wherever possible that they are open and auditable by independent third parties[^5]. Further, we emphasized the importance of iterative development in collaboration with affected stakeholders & subject-matter experts[^6] wherever possible. An iterative approach is helpful here (if possible) since it allows for detection of unintended consequences & feedback from affected stakeholders. In practice, this may mean moving away from rigidly-specified RFP ("request for proposal") models of procurement towards more collaborative models of engagement between governments, developers & stakeholders. 

A final piece of the puzzle that we discussed was the importance of creating a public "chain of responsibility" for algorithmic systems. This seemed important to highlight since it can be otherwise difficult to assign responsibility in complex socio-technical systems. When something goes wrong with a predictive model in the field, who is to blame? Is it the user of the model? The model's original developer? The team that procured the model? The model itself? Without clarity here, it's sure to be difficult to create accountability for issues. There is a risk of what a related [Data & Society Report](https://datasociety.net/wp-content/uploads/2019/09/DandS_Algorithmic_Accountability.pdf) calls "moral crumple zones", where "one entity is held legally liable for errors, even if they aren't in full control of the system" (21). 

Overall, this was an interesting project for me to be a part of, and I'm hopeful that I will have a chance to work on these topics further in the future. 

_Footnotes_

[^1]: The team was me, [Irene](https://www.irenesolaiman.com/), [Yo](https://yonadavshavit.com/), [Saffron](https://saffronhuang.com/), and [Phil](https://www.linkedin.com/in/philip-chertoff-75366352/). 

[^2]: These views are my own and not necessarily those of anyone on the team. However, where indicated, they overlap with some of the writing / ideas that we worked on together in developing the project. Any mistakes or innaccuracies are my own and not a reflection of the team. 

[^3]: This is not to say that contractors / vendors for these products do not care about moral / ethical issues. However, in this context, their incentive is to make a sale; government stakeholders, by contrast, want to determine whether and how the systems address a civic need in a civicly-responsible & equitable way etc. 

[^4]: The prospect of public accountability is low if the public does not even know that the algorithmic process exists. 

[^5]: For example, we talk about making "input-output" testing available for models and considering opening up source code & audit logs where possible. 

[^6]: For example, the front-line teams that implement non-automated versions of the decision process, or will be using the new tool (e.g. judges who make bail decisions, or inspectors who decide what restaurants to inspect). 
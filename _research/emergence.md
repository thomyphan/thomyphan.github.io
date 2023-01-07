---
layout: archive
title: "Emergence in Multi-Agent Systems"
permalink: /research/emergence/
author_profile: true
---

{% include base_path %}

## Emerging Swarms

<img src="https://thomyphan.github.io/images/research/emergence_research.png" style="float:right; width:200pt;padding-left:10px;"  alt="Swarming vs. Independent Escape"/>

Animals and human tend to form swarms to collectively forage and protect each other from predators. Such swarms emerge based on local interaction of hundreds or thousands of individuals without any centralized controller. Due to the vast scale of such systems, the emergence and characteristics of swarms are hard to understand and anticipate.

Using RL techniques, we can study and quantify the effect of emerging swarms under controlled conditions. We built a large-scale predator-prey simulation, where all preys must learn to survive independently [1]. We also adapted the simulation to a foraging scenario, where multiple agents independently find and follow some target under partial observability [2].

*Publications:*  
[1] [Emergent Flocking](https://thomyphan.github.io/publication/2019-07-01-alife-hahn)  
[2] [Foraging Swarms](https://thomyphan.github.io/publication/2020-07-01-alife-hahn)  

## Emergent Sustainability

<img src="https://thomyphan.github.io/images/research/domain_harvest.png" style="float:right; width:200pt;padding-left:10px;"  alt="Harvest Domain"/>

Common resources can lead to competitive behavior in self-interested MAS, where agents learn to greedily deplete resources without leaving any chance for regeneration. Such behavior is typicaly not desirable for real-world applications like autonomous driving or network communication, where limited resources should be used in a sustainable way.

We study environment factors of existing domains, e.g., the predator-prey domain mentioned above, that are needed to enable the emergence of sustainable behavior in self-interested MAS [1]. We also evaluate the effect of the number of agents on emergent sustainability [2]. 

*Publications:*  
[1] [Ecosystem Management](https://thomyphan.github.io/publication/2020-07-01-alife-ritz)  
[2] [Multi-Agent Ecosystem Management](https://thomyphan.github.io/publication/2021-07-01-alife-ritz)  

## Peer Incentivization

<img src="https://thomyphan.github.io/images/research/peer_incentivization.png" style="float:right; width:200pt;padding-left:10px;"  alt="Peer Incentivization"/>

As self-learning agents become more and more omnipresent in the real world, they will inevitably learn to interact with each other. In self-interested MAS, where multiple autonomous systems with individual goals coexist in a shared environment, conflict and competition may arise due to opposing goals or shared resources. Naive RL approaches commonly fail to cooperate in such scenarios, possibly leading to undesirable emergent results.

To incentivize cooperative behavior in self-interested MAS, we study decentralized mechanisms, where agents learn to reward or penalize each other. These mechanisms are based on market mechanisms [1] or social behavior like acknowledgments [3], which are well studied in other fields [2]. We also consider real-world aspects like locality of information, defectors, as well as limited and noisy communication channels [3].

*Publications:*  
[1] [Action Markets](https://thomyphan.github.io/publication/2018-08-01-icann-schmid)  
[2] [The Sharer's Dilemma](https://thomyphan.github.io/publication/2018-11-01-isola-belzner)  
[3] [Mutual Acknowledgment Exchange](https://thomyphan.github.io/publication/2022-05-01-aamas-phan)  

<div style="float: right;">
    <a href="https://thomyphan.github.io/research/"><strong>Back to Research</strong></a>
</div>
---
layout: archive
title: "Emergence in Multi-Agent Systems"
permalink: /research/emergence/
author_profile: true
---

{% include base_path %}

## Emerging Swarms

<img src="https://thomyphan.github.io/images/research/emergence_research.png" title="Predator-Prey Domain" style="float:right; width:250pt;padding-left:10px;"  alt="Swarming vs. Independent Escape"/>

Animals like birds and fishes tend to form swarms to collectively forage or protect each other from predators. Swarms emerge from *local interaction* of thousands of individuals without a centralized controller. Due to the vast scale of such systems, the emergence and characteristics of swarms are hard to interpret and anticipate.

Using *reinforcement learning (RL)* techniques, we can study and quantify the effect of emerging swarms under controlled conditions. Therefore, we employ a large-scale predator-prey simulation, where all preys must learn to survive independently [1]. We also adapt the simulation to foraging scenarios, where multiple agents independently search and follow some target under partial observability [2]. In all cases, we observe the emergence of swarms without explicit incentivization through rewards.

*Publications:*  
[1] [Emergent Flocking](https://thomyphan.github.io/publication/2019-07-01-alife-hahn)  
[2] [Foraging Swarms](https://thomyphan.github.io/publication/2020-07-01-alife-hahn)  

## Emergent Sustainability

<span style="float:right">
<img src="https://thomyphan.github.io/images/research/sustainable_hunting1.gif" title="Sutstainable Hunting with Multiple Predators" style="width:115pt;padding-left:10px;" alt="Sutstainable Hunting 1"/> <img src="https://thomyphan.github.io/images/research/sustainable_hunting2.gif" title="Sutstainable Hunting with Multiple Predators" style="width:115pt;padding-left:10px;" alt="Sutstainable Hunting 2"/>
</span>

Common resources can lead to greedy behavior in self-interested *multi-agent system (MAS)*, where agents learn to deplete all resources without any chance for regeneration. Such behavior known as *tradegy of the commons* is not desirable for real-world applications like autonomous driving or network communication, where limited resources should be used in a sustainable way.

We study different environment factors of existing domains, e.g., the predator-prey domain mentioned above, to enable the emergence of sustainable behavior in self-interested MAS [1]. We also evaluate how the number of self-interested agents affects emergent sustainability [2]. 

*Publications:*  
[1] [Ecosystem Management](https://thomyphan.github.io/publication/2020-07-01-alife-ritz)  
[2] [Multi-Agent Ecosystem Management](https://thomyphan.github.io/publication/2021-07-01-alife-ritz)  

## Peer Incentivization

<img src="https://thomyphan.github.io/images/research/peer_incentivization.png" title="Peer Incentivization" style="float:right; width:250pt;padding-left:10px;" alt="Peer Incentivization"/>

As self-learning agents become more and more omnipresent in the real world, they will inevitably learn to interact with each other. In self-interested MAS, conflict and competition may arise due to opposing goals or shared resources. Naive RL approaches commonly fail to cooperate in such scenarios, leading to undesirable emergent results.

To incentivize cooperative behavior in self-interested MAS, we study *decentralized mechanisms*, where agents learn to reward or penalize each other. These mechanisms are based on market theory [1] or social behavior like acknowledgments [2], which are well studied in other fields [3]. We also consider real-world aspects like defectors, locality of information, and noisy communication [2].

*Publications:*  
[1] [Action Markets](https://thomyphan.github.io/publication/2018-08-01-icann-schmid)  
[2] [Mutual Acknowledgment Exchange](https://thomyphan.github.io/publication/2022-05-01-aamas-phan)  
[3] [The Sharer's Dilemma](https://thomyphan.github.io/publication/2018-11-01-isola-belzner)  

<div style="float: right;">
    <a href="https://thomyphan.github.io/research/"><strong>Back to Research</strong></a>
</div>
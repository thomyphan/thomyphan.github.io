---
layout: archive
title: "Multi-Agent Reinforcement Learning"
permalink: /research/marl/
author_profile: true
---

{% include base_path %}

## Cooperative Settings

<img src="https://thomyphan.github.io/images/research/cooperative_mas_domains.png" style="float:right; width:300pt;padding-left:10px;"  alt="MAS Domains"/>

Many real-world problems like fleet management, industry 4.0 scenarios, or communication networks can be formulated as cooperative *multi-agent system (MAS)*, where multiple agents have to collaborate to achieve a common goal. *Multi-agent reinforcement learning (MARL)* is a promising approach to solve these problems, which has recently achieved remarkable progress in challenging domains like [StarCraft II](https://github.com/oxwhirl/smac). However, current MARL is still at a preliminary stage, where many real-world aspects are neglected for simplicity therefore limiting practicability.

We address current weaknesses in MARL with respect to the real world beyond classic benchmark optimization like scalability and state uncertainty. Our algorithms are based on value function factorization and use agent hierarchies [1] or attention-based recurrency [2]. In addition, we provide a [new benchmark](https://github.com/thomyphan/messy_smac) that exhibit higher degrees of state uncertainty through stochastic initial states and noisy observations, which is commonly neglected in MARL research [2].

*Publications:*  
[1] [Variable Agent Sub-Teams](https://thomyphan.github.io/publication/2021-12-01-neurips-phan)  
[2] [State Uncertainty](https://thomyphan.github.io/publication/2023-05-01-aamas-phan)  

## Planning and Learning

<img src="https://thomyphan.github.io/images/research/planning_value_function_2.png" style="float:right; width:300pt;padding-left:10px;"  alt="Planning with Value Function"/>

Cooperative MARL commonly exploits global information like states and joint actions during training to produce coordinated strategies for decentralized decision making. However, emergent phenomena can dynamically occur in various forms and levels which are difficult to deduce from mere states and joint actions therefore limiting performance and scalability in large-scale domains.

We propose to explicitly consider emergent behavior via distributed planning to overcome these limitations. To support the distributed planning process, we provide learned value [1] and policy functions [2,3] to narrow the search beam for higher efficiency.

*Publications:*  
[1] [Value Function Approximation for Distributed Planning](https://thomyphan.github.io/publication/2018-06-01-aamas-phan)  
[2] [Distributed Planning for Multi-Agent Policy Approximation](https://thomyphan.github.io/publication/2019-05-01-aamas-phan)  
[3] [Centralized Learning and Decentralized Planning](https://thomyphan.github.io/publication/2020-05-01-ala-phan)  

## Adversarial Settings

<img src="https://thomyphan.github.io/images/research/antagonist_in_MAS.png" style="float:right; width:300pt;padding-left:10px;"  alt="Antagonists in MAS"/>

Cooperative MARL agents are commonly trained under idealized condition, assuming that agents will always exhibit cooperative behavior. However, (partial) *adversarial behavior* may occur nevertheless due to flaws in hardware and software, potentially leading to catastrophic failure. Thus, even cooperative *multi-agent system (MAS)* need to be prepared for adversarial change as each agent may be a potential *source of failure*.

We devise algorithms to improve resilience in MAS. During training, we randomly replace productive agents by antagonists to expose the system to partial adversarial change [1]. We also devise evaluation methods to compare resilience of different MARL algorithms in a fair way [2].

*Publications:*   
[1] [Antagonist-Based Learning](https://thomyphan.github.io/publication/2020-05-01-aamas-phan)  
[2] [Adversarial Value Decomposition](https://thomyphan.github.io/publication/2021-02-01-aaai-phan)  

## Self-Interested Settings

<img src="https://thomyphan.github.io/images/research/peer_incentivization.png" style="float:right; width:250pt;padding-left:10px;"  alt="Peer Incentivization"/>

As self-learning agents become more and more omnipresent in the real world, they will inevitably learn to interact with each other. In self-interested MAS, conflict and competition may arise due to opposing goals or shared resources. Naive RL approaches commonly fail to cooperate in such scenarios, leading to undesirable emergent results.

To incentivize cooperative behavior in self-interested MAS, we study *decentralized mechanisms*, where agents learn to reward or penalize each other. These mechanisms are based on market theory [1] or social behavior like acknowledgments [2], which are well studied in other fields. We also consider real-world aspects like defectors, locality of information, and noisy communication [2].

*Publications:*  
[1] [Action Markets for Emergent Cooperation](https://thomyphan.github.io/publication/2018-08-01-icann-schmid)  
[2] [Mutual Acknowledgment Exchange for Reciprocity](https://thomyphan.github.io/publication/2022-05-01-aamas-phan)  

<div style="float: right;">
    <a href="https://thomyphan.github.io/research/"><strong>Back to Research</strong></a>
</div>
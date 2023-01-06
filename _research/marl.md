---
layout: archive
title: "Multi-Agent Reinforcement Learning"
permalink: /research/marl/
author_profile: true
---

{% include base_path %}

## Cooperative Settings

<img src="https://thomyphan.github.io/images/research/cooperative_mas_domains.png" style="float:right; width:250pt;padding-left:10px;"  alt="MAS Domains"/>

Many real-world problems like fleet management, industry 4.0 scenarios, or communication networks can be formulated as cooperative *multi-agent system (MAS)*, where multiple agents have to collaborate to achieve a common goal. *Multi-agent reinforcement learning (MAS)* is a promising approach to solve these problems, which has recently achieved remarkable progress in domains like StarCraft II. However, current MARL is still at an early stage, where many real-world aspects are neglected for simplicity therefore limiting real-world applicability.

We aim to address current weaknesses in MARL regarding real-world aspects like scalability and state uncertainty. Our algorithms improve the state-of-the-art beyond classic benchmark optimization. In addition, we provide new benchmarks that exhibit higher degrees of uncertainty through stochastic initial states and noisy observations to cover relevant aspects that are commonly neglected in MARL research.

*Publications:*  
[1] [Variable Agent Sub-Teams](https://thomyphan.github.io/publication/2021-12-01-neurips-phan)  
[2] [State Uncertainty](https://thomyphan.github.io/publication/2023-05-01-aamas-phan)  

## Competitive Settings

<img src="https://thomyphan.github.io/images/research/antagonist_in_MAS.png" style="float:right; width:300pt;padding-left:10px;"  alt="Antagonists in MAS"/>

RL agents are commonly trained under idealized condition, assuming that nothing can fail. However, (partially) adversarial behavior may still occur due to flaws in hardware and software, potentially leading to catastrophic failure. Thus, even cooperative MAS need to be prepared for adversarial change as each agent may be a potential source of failure.

We devise algorithms to improve resilience in MARL systems. During training, we randomly replace productive agents by antagonist agents to expose the system to partial adversarial change. We also devise evaluation methods to compare resilience of different MARL algorithms in a fair way.

*Publications:*  
[1] [Coevolutionary Reinforcement Learning](https://thomyphan.github.io/publication/2019-06-01-gecco-gabor)  
[2] [Antagonist-Based Learning](https://thomyphan.github.io/publication/2020-05-01-aamas-phan)  
[3] [Adversarial Value Decomposition](https://thomyphan.github.io/publication/2021-02-01-aaai-phan)  

## Self-Interested Settings

<img src="https://thomyphan.github.io/images/research/peer_incentivization.png" style="float:right; width:250pt;padding-left:10px;"  alt="Peer Incentivization"/>

As self-learning agents become more and more omnipresent in the real world, they will inevitably learn to interact with each other. In self-interested MAS, where multiple autonomous systems with individual goals coexist in a shared environment, conflict and competition may arise due to opposing goals or shared resources. Naive RL approaches commonly fail to cooperate in such scenarios, possibly leading to undesirable emergent results.

To incentivize cooperative behavior in self-interested MAS, we study decentralized mechanisms, where agents learn to reward or penalize each other. These mechanisms are based on market mechanisms or social behavior like acknowledgments, which are well studied in other fields. We also consider real-world aspects like locality of information as well as limited and noisy communication channels.

*Publications:*  
[1] [Action Markets for Emergent Cooperation](https://thomyphan.github.io/publication/2018-08-01-icann-schmid)  
[2] [Mutual Acknowledgment Exchange for Reciprocity](https://thomyphan.github.io/publication/2022-05-01-aamas-phan)  

## Planning and Learning

<img src="https://thomyphan.github.io/images/research/planning_value_function_2.png" style="float:right; width:250pt;padding-left:10px;"  alt="Planning with Value Function"/>

Cooperative MARL commonly exploits global information like states and joint actions during training to produce coordinated strategies for decentralized decision making. However, emergent phenomena can dynamically occur in various forms and levels which are difficult to deduce from mere states and joint actions therefore limiting performance and scalability in large-scale domains.

We propose to explicitly consider emergent behavior via distributed planning to overcome these limitations. To support the distributed planning process, we provide learned value and policy functions to narrow the search beam to improve efficiency.

*Publications:*  
[1] [Value Function Approximation for Distributed Planning](https://thomyphan.github.io/publication/2018-06-01-aamas-phan)  
[2] [Distributed Planning for Multi-Agent Policy Approximation](https://thomyphan.github.io/publication/2019-05-01-aamas-phan)  
[3] [Centralized Learning and Decentralized Planning](https://thomyphan.github.io/publication/2020-05-01-ala-phan)  

<div style="float: right;">
    <a href="https://thomyphan.github.io/research/"><strong>Back to Research</strong></a>
</div>
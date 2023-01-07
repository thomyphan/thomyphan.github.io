---
layout: archive
title: "Resilience in Autonomous Systems"
permalink: /research/resilience/
author_profile: true
---

{% include base_path %}

## Diverse Evolutionary Optimization

<img src="https://thomyphan.github.io/images/research/solution_landscape_example.png" style="float:right; width:250pt;padding-left:10px;"  alt="Solution Landscape Example"/>

Many optimization approaches aim for a single optimum in the solution landscape, which makes them vulnerable for changes in the solution landscape, where some optima are removed or changed, e.g., when some paths are removed from a navigation graph due to obstacles or accidents. Diverse optimization can address that problem by searching for multiple optima to provide flexible solutions for better resilience in autonomous systems.

We study diversity-aware optimization in evolutionary algorithms and use the concepts for planning to demonstrate improved resilience through diversity [1]. We also devise diversity-based objectives to ease optimization, which may be useful for resilient reinforcement learning and planning algorithms [2].

*Publications:*  
[1] [Diversity-Aware Planning](https://thomyphan.github.io/publication/2018-09-01-icac-gabor)  
[2] [Productive Fitness](https://thomyphan.github.io/publication/2021-01-01-naco-gabor)  

## Coevolution in Autonomous Systems

RL agents are commonly trained under idealized condition by assuming a stationary environment. In complex domains, such agents can be vulnerable to rare events that are not (frequently) encountered during training thus potentially causing unintended behavior. To learn resilient behavior, the agent needs to be exposed to such rare events more frequently during training.

We devise coevolutionary RL algorithms, where the environment is modeled as an adversary and optimized with evolutionary algorithms to minimize the original RL objective. The adversarial environment can be used to train resilient agents [1] and evolve in an open-ended manner to provide adequate test cases for self-adaptive systems [2].

*Publications:*  
[1] [Coevolutionary Reinforcement Learning](https://thomyphan.github.io/publication/2019-06-01-gecco-gabor)  
[2] [Adaptive Quality Assurance](https://thomyphan.github.io/publication/2020-01-01-sttt-gabor)  

## Resilience in Multi-Agent Systems

<img src="https://thomyphan.github.io/images/research/antagonist_in_MAS.png" style="float:right; width:300pt;padding-left:10px;"  alt="Antagonists in MAS"/>

Cooperative MARL agents are commonly trained under idealized condition, assuming that nothing can fail. However, (partially) adversarial behavior may still occur due to flaws in hardware and software, potentially leading to catastrophic failure. Thus, even cooperative MAS need to be prepared for adversarial change as each agent may be a potential source of failure.

We devise algorithms to improve resilience in MARL systems. During training, we randomly replace productive agents by antagonists to expose the system to partial adversarial change [1]. We also devise evaluation methods to compare resilience of different MARL algorithms in a fair way [2].

*Publications:*  
[1] [Antagonist-Based Learning](https://thomyphan.github.io/publication/2020-05-01-aamas-phan)  
[2] [Adversarial Value Decomposition](https://thomyphan.github.io/publication/2021-02-01-aaai-phan)  

<div style="float: right;">
    <a href="https://thomyphan.github.io/research/"><strong>Back to Research</strong></a>
</div>
---
layout: archive
title: "Resilience in Autonomous Systems"
permalink: /research/resilience/
author_profile: true
---

{% include base_path %}

## Scenario Coevolution

<img src="https://thomyphan.github.io/images/research/scenario_coevolution.png" title="Scenario Coevolution Process" style="float:right; width:250pt;padding-left:10px;"  alt="Scenario Coevolution Process"/>

RL agents are commonly trained under idealized condition, assuming a stationary environment. In complex domains, such agents are typically vulnerable to *rare events* that are not (frequently) encountered during training, potentially performing poorly or causing catastrophic failure. To learn resilient behavior, the RL agent needs to be exposed to such rare events more often during training.

We devise *coevolutionary* RL algorithms, where the environment is modeled as an adversary and optimized with evolutionary algorithms to minimize the original RL objective. The adversarial environment can be used to train resilient agents [1] and evolve in an open-ended manner to provide adaptive test cases for continuously evolving systems [2].

*Publications:*  
[1] [Coevolutionary Reinforcement Learning](https://thomyphan.github.io/publication/2019-06-01-gecco-gabor)  
[2] [Adaptive Quality Assurance](https://thomyphan.github.io/publication/2020-01-01-sttt-gabor)  

## Resilience in Multi-Agent Systems

<img src="https://thomyphan.github.io/images/research/resilience_research.png" title="Smart Factory with Antagonists" style="float:right; width:200pt;padding-left:10px;"  alt="Antagonists in MAS"/>

Cooperative *multi-agent RL (MARL)* agents are commonly trained under idealized condition, assuming that agents will always exhibit cooperative behavior. However, (partial) *adversarial behavior* may occur nevertheless due to flaws in hardware and software, potentially leading to catastrophic failure. Thus, even cooperative *multi-agent system (MAS)* need to be prepared for adversarial change as each agent may be a potential *source of failure*.

We devise adversarial algorithms to improve resilience in MAS. During training, we randomly replace productive agents by antagonists to expose the system to partial adversarial change [1]. We also devise evaluation methods to compare resilience of different MARL algorithms in a fair way [2].

*Publications:*  
[1] [Antagonist-Based Learning](https://thomyphan.github.io/publication/2020-05-01-aamas-phan)  
[2] [Adversarial Value Decomposition](https://thomyphan.github.io/publication/2021-02-01-aaai-phan)  

<div style="float: right;">
    <a href="https://thomyphan.github.io/research/"><strong>Back to Research</strong></a>
</div>
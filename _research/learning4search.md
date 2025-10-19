---
layout: archive
title: "Learning-Based Search"
permalink: /research/learning4search/
author_profile: true
---

{% include base_path %}

## Machine Learning-Guided Search for Multi-Agent Path Finding

<img src="https://thomyphan.github.io/images/research/mapf_instance.png" style="float:right; width:150pt;padding-left:10px;" title="Random MAPF Instance" alt="Random MAPF Instance"/>

Heuristic search is important for a variety of real-world applications such as routing, robot motion planning, and multi-agent coordination. Hand-crafted heuristics are often used to exploit structural properties of the underlying problem to speed up the search.

We currently focus on *multi-agent path finding (MAPF)* as a particularly challenging search domain and use machine learning to guide heuristic search algorithms via online adaptation [1,2]. We also develop simple curriculum approaches to learn fast policies for highly constraint environments [3,4].

*Publications:*  
[1] [Adaptive Anytime Multi-Agent Path Finding](https://thomyphan.github.io/publication/2024-02-01-aaai-phan)  
[2] [Adaptive Delay-Based Multi-Agent Path Finding](https://thomyphan.github.io/publication/2025-02-01-aaai-phan1)  
[3] [Curriculum Learning for Multi-Agent Path Finding](https://thomyphan.github.io/publication/2024-05-01-aamas-phan)  
[4] [Generative Curricula for Multi-Agent Path Finding](https://thomyphan.github.io/publication/2025-04-01-jair-phan)  

## Multi-Agent Planning and Learning

<img src="https://thomyphan.github.io/images/research/planning_value_function_2.png" style="float:right; width:300pt;padding-left:10px;" title="Planning with Value Function" alt="Planning with Value Function"/>

Cooperative MARL commonly exploits global information like states and joint actions during training to produce coordinated strategies for decentralized decision making. However, emergent phenomena can dynamically occur in various forms and levels which are difficult to deduce from mere states and joint actions therefore limiting performance and scalability in large-scale domains.

We propose to explicitly consider emergent behavior via distributed Monte Carlo planning to overcome these limitations. To support the distributed planning process, we provide learned value [1] and policy functions [2] to narrow down the search beam for improved efficiency.

*Publications:*  
[1] [Value Function Approximation for Distributed Planning](https://thomyphan.github.io/publication/2018-06-01-aamas-phan)  
[2] [Distributed Planning for Multi-Agent Policy Approximation](https://thomyphan.github.io/publication/2019-05-01-aamas-phan)  

<div style="float: right;">
    <a href="https://thomyphan.github.io/research/"><strong>Back to Research</strong></a>
</div>
---
layout: archive
title: "Learning-Based Search"
permalink: /research/learning4search/
author_profile: true
---

{% include base_path %}

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
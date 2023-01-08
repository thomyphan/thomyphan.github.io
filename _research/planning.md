---
layout: archive
title: "Planning and Optimization"
permalink: /research/planning/
author_profile: true
---

{% include base_path %}

## Stochastic Optimization

<img src="https://thomyphan.github.io/images/research/solution_landscape_example.png" title="Optimization Problem with Multiple Optima" style="float:right; width:250pt;padding-left:10px;"  alt="Solution Landscape Example"/>

Optimization forms the basis of machine learning and planning algorithms, where one or more objective functions must be maximized or minimized, e.g., a differential loss function or the expected cumulative reward of a sequential problem.

We focus on stochastic optimization based on diversity-aware evolutionary algorithms [1,2] and hybrid quantum-classical algorithms [3,4] to solve problems in planning [2] and polymatrix game theory [3].

*Publications:*  
[1] [Productive Fitness](https://thomyphan.github.io/publication/2021-01-01-naco-gabor)  
[2] [Diversity-Aware Optimization](https://thomyphan.github.io/publication/2018-09-01-icac-gabor)  
[3] [Quantum Annealing for Nash Equilibria Search](https://thomyphan.github.io/publication/2020-08-01-iccs-roch)  
[4] [Quantum Approximate Optimization](https://thomyphan.github.io/publication/2020-10-01-icrc-roch)  

<div style="float: right;">
    <a href="https://thomyphan.github.io/research/"><strong>Back to Research</strong></a>
</div>

## Monte Carlo Planning

<img src="https://thomyphan.github.io/images/research/open_loop_planning.png" style="float:right; width:300pt;padding-left:10px;" title="Closed-Loop and Open-Loop Planning" alt="Closed-Loop and Open-Loop Planning"/>

*Monte Carlo Planning (MCP)* is a sampling-based approach to decision making in complex domains with enormous branching factors. Given a fixed computation budget per decision, MCP can be used for online planning, where the agent alternates between acting and reasoning per time step. MCP only requires limited domain knowledge in form of a black box simulator and a computation budget for stochastic optimization of plans.

We devise algorithms that address various real-world challenges regarding MCP like domain shifts [1], resource restrictions [2,3], and temporal abstraction [4]. Most of our algorithms are open-loop and based on evolutionary algorithms [1] or stacks of multi-armed bandits [2,3] to reduce the search space, while still being able to make good decisions under limited resources.

*Publications:*  
[1] [Evolutionary Planning](https://thomyphan.github.io/publication/2018-09-01-icac-gabor)  
[2] [Memory Bounded Open-Loop Planning](https://thomyphan.github.io/publication/2019-02-01-aaai-phan)  
[3] [Adaptive Thompson Sampling Stacks](https://thomyphan.github.io/publication/2019-08-01-ijcai-phan)  
[4] [Subgoal-Based Monte Carlo Planning](https://thomyphan.github.io/publication/2019-08-01-ijcai-gabor)   

## Planning and Learning

<img src="https://thomyphan.github.io/images/research/planning_value_function_2.png" style="float:right; width:300pt;padding-left:10px;" title="Planning with Value Function" alt="Planning with Value Function"/>

Cooperative MARL commonly exploits global information like states and joint actions during training to produce coordinated strategies for decentralized decision making. However, emergent phenomena can dynamically occur in various forms and levels which are difficult to deduce from mere states and joint actions therefore limiting performance and scalability in large-scale domains.

We propose to explicitly consider emergent behavior via distributed Monte Carlo planning to overcome these limitations. To support the distributed planning process, we provide learned value [1] and policy functions [2,3] to narrow the search beam to improve efficiency.

*Publications:*  
[1] [Value Function Approximation for Distributed Planning](https://thomyphan.github.io/publication/2018-06-01-aamas-phan)  
[2] [Distributed Planning for Multi-Agent Policy Approximation](https://thomyphan.github.io/publication/2019-05-01-aamas-phan)  
[3] [Centralized Learning and Decentralized Planning](https://thomyphan.github.io/publication/2020-05-01-ala-phan)  

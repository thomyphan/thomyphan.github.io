---
layout: archive
title: "Stochastic Optimization"
permalink: /research/optimization/
author_profile: true
---

{% include base_path %}

## Optimization Algorithms

<img src="https://thomyphan.github.io/images/research/solution_landscape_example.png" title="Optimization Problem with Multiple Optima" style="float:right; width:250pt;padding-left:10px;"  alt="Solution Landscape Example"/>

Optimization forms the basis of machine learning and planning algorithms, e.g., to minimize a loss function or maximize the expected cumulative reward of a sequential problem.

We focus on stochastic optimization based on evolutionary [1] or quantum computing [2] to solve complex problems in planning and (polymatrix) game theory.

*Publications:*  
[1] [Productive Fitness](https://thomyphan.github.io/publication/2021-01-01-naco-gabor)  
[2] [Quantum Annealing for Nash Equilibria Search](https://thomyphan.github.io/publication/2020-08-01-iccs-roch)

## Monte Carlo Planning

<img src="https://thomyphan.github.io/images/research/open_loop_planning.png" style="float:right; width:300pt;padding-left:10px;" title="Closed-Loop and Open-Loop Planning" alt="Closed-Loop and Open-Loop Planning"/>

*Monte Carlo Planning (MCP)* is a sampling-based approach to sequential decision making suitable for domains with enormous branching factors. MCP can be used for online planning, where the agent alternates between acting and reasoning per time step. MCP only requires limited domain knowledge in form of a black box simulator and a computation budget for stochastic optimization of decisions.

We devise algorithms that address various real-world challenges regarding MCP like resource restrictions [1,2] and temporal abstraction [3], and counterfactual reasoning [4]. Our algorithms are open-loop to reduce the search space, while being able to make good decisions in complex domains.

*Publications:*  
[1] [Memory Bounded Open-Loop Planning](https://thomyphan.github.io/publication/2019-02-01-aaai-phan)  
[2] [Adaptive Thompson Sampling Stacks](https://thomyphan.github.io/publication/2019-08-01-ijcai-phan)  
[3] [Subgoal-Based Monte Carlo Planning](https://thomyphan.github.io/publication/2019-08-01-ijcai-gabor)
[4] [Counterfactual Monte Carlo Planning](https://thomyphan.github.io/publication/2025-02-01-aaai-phan2)   

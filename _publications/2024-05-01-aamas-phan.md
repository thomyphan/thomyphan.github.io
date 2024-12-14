---
author_list: "Thomy Phan and Joseph Driscoll and Justin Romberg and Sven Koenig"
title: "Confidence-Based Curriculum Learning for Multi-Agent Path Finding"
collection: publications
permalink: /publication/2024-05-01-aamas-phan
excerpt: "A wide range of real-world applications can be formulated as Multi-Agent Path Finding (MAPF) problem, where the goal is to find collision-free paths for multiple agents with individual start and goal locations. State-of-the-art MAPF solvers are mainly centralized and depend on global information, which limits their scalability and flexibility regarding changes or new maps that would require expensive replanning. Multi-agent reinforcement learning (MARL) offers an alternative way by learning decentralized policies that can generalize over a variety of maps. While there exist some prior works that attempt to connect both areas, the proposed techniques are heavily engineered and very complex due to the integration of many mechanisms that limit generality and are expensive to use. We argue that much simpler and general approaches are needed to bring the areas of MARL and MAPF closer together with significantly lower costs. In this paper, we propose Confidence-based Auto-Curriculum for Team Update Stability (CACTUS) as a lightweight MARL approach to MAPF. CACTUS defines a simple reverse curriculum scheme, where the goal of each agent is randomly placed within an allocation radius around the agent's start location. The allocation radius increases gradually as all agents improve, which is assessed by a confidence-based measure. We evaluate CACTUS in various maps of different sizes, obstacle densities, and numbers of agents. Our experiments demonstrate better performance and generalization capabilities than state-of-the-art approaches while using less than 600,000 trainable parameters, which is less than 5% of the neural network size of current MARL approaches to MAPF."
venue_short: "AAMAS"
booktitle: "Proceedings of the 23rd International Conference on Autonomous Agents and MultiAgent Systems"
#paper_pages: "11308--11316"
date: "2024-05-01"
bibtexid: "phanAAMAS24"
#paperdoi: "https://doi.org/10.1609/aaai.v35i13.17348"
paperurl: "https://thomyphan.github.io/files/2024-aamas.pdf"
eprint: "https://thomyphan.github.io/files/2024-aamas.pdf"
coderepository: "https://github.com/thomyphan/rl4mapf"
venuelocation: "Auckland, New Zealand"
research_emergence: "False"
research_resilience : "False"
research_dependability : "False"
research_marl : "True"
research_planning : "False"
research_learning4search: "True"
---

{% include base_path %}

## Related Articles
- T. Phan et al., ["Anytime Multi-Agent Path Finding with an Adaptive Delay-Based Heuristic"](https://thomyphan.github.io/publication/2025-02-01-aaai-phan1), AAAI 2025
- S. Chan et al., ["Anytime Multi-Agent Path Finding using Operator Parallelism in Large Neighborhood Search"](https://thomyphan.github.io/publication/2024-05-01-aamas-chan), AAMAS 2024
- T. Phan et al., ["Adaptive Anytime Multi-Agent Path Finding using Bandit-Based Large Neighborhood Search"](https://thomyphan.github.io/publication/2024-02-01-aaai-phan), AAAI 2024
- P. Altmann et al., ["CROP: Towards Distributional-Shift Robust Reinforcement Learning using Compact Reshaped Observation Processing"](https://thomyphan.github.io/publication/2023-08-01-ijcai-altmann), IJCAI 2023
- T. Phan et al., ["Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability"](https://thomyphan.github.io/publication/2023-07-01-icml-phan), ICML 2023
- T. Phan et al., ["VAST: Value Function Factorization with Variable Agent Sub-Teams"](https://thomyphan.github.io/publication/2021-12-01-neurips-phan), NeurIPS 2021
- T. Phan et al., ["A Distributed Policy Iteration Scheme for Cooperative Multi-Agent Policy Approximation"](https://thomyphan.github.io/publication/2020-05-01-ala-phan), ALA 2020
- T. Phan et al., ["Distributed Policy Iteration for Scalable Approximation of Cooperative Multi-Agent Policies"](https://thomyphan.github.io/publication/2019-05-01-aamas-phan), AAMAS 2019
- T. Phan et al., ["Leveraging Statistical Multi-Agent Online Planning with Emergent Value Function Approximation"](https://thomyphan.github.io/publication/2018-06-01-aamas-phan), AAMAS 2018
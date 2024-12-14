---
author_list: "Shao-Hung Chan and Zhe Chen and Dian-Lun Lin and Yue Zhang and Daniel Harabor and Sven Koenig and Tsung-Wei Huang and Thomy Phan"
title: "Anytime Multi-Agent Path Finding using Operator Parallelism in Large Neighborhood Search"
collection: publications
permalink: /publication/2024-05-01-aamas-chan
excerpt: "Multi-Agent Path Finding (MAPF) is the problem of finding a set of collision-free paths for multiple agents in a shared environment while minimizing the sum of travel times. Since the MAPF problem is NP-hard to solve optimally, anytime algorithms are promising to quickly find a solution and keep optimizing it before interrupting. The current state-of-the-art anytime algorithm for MAPF is based on Large Neighborhood Search (LNS), called MAPF-LNS, which is a combinatorial search algorithm that iteratively destroys and repairs a subset of collision-free paths in order to optimize the sum of travel times. However, the destroy and repair operations in MAPF-LNS can be time-consuming, thus limiting the effectiveness due to fewer iterations and scalability w.r.t. the number of agents. In this paper, we propose Destroy-Repair Operation Parallelism for LNS (DROP-LNS), a parallel framework that performs multiple destroy and repair processes simultaneously to explore a larger searching space under a limited time budget. Unlike MAPF-LNS, DROP-LNS is able to exploit parallelized hardware to improve the solution quality. We extend DROP-LNS to two alternatives and conduct experimental evaluations to compare the performance. The results show that DROP-LNS significantly outperforms the state-of-the-art."
venue_short: "AAMAS"
booktitle: "Extended Abstracts of the 23rd International Conference on Autonomous Agents and MultiAgent Systems"
paper_pages: "2183--2185"
date: "2024-05-01"
bibtexid: "chanAAMAS24"
paperdoi: "https://dl.acm.org/doi/10.5555/3635637.3663101"
extendedversion: "https://arxiv.org/pdf/2402.01961.pdf"
paperurl: "https://arxiv.org/pdf/2402.01961.pdf"
eprint: "https://arxiv.org/pdf/2402.01961.pdf"
venuelocation: "Auckland, New Zealand"
research_emergence: "False"
research_resilience : "False"
research_dependability : "False"
research_marl : "False"
research_planning : "True"
research_learning4search: "False"
---

{% include base_path %}

## Related Articles
- T. Phan et al., ["Anytime Multi-Agent Path Finding with an Adaptive Delay-Based Heuristic"](https://thomyphan.github.io/publication/2025-02-01-aaai-phan1), AAAI 2025
- T. Phan et al., ["Confidence-Based Curriculum Learning for Multi-Agent Path Finding"](https://thomyphan.github.io/publication/2024-05-01-aamas-phan), AAMAS 2024
- T. Phan et al., ["Adaptive Anytime Multi-Agent Path Finding using Bandit-Based Large Neighborhood Search"](https://thomyphan.github.io/publication/2024-02-01-aaai-phan), AAAI 2024
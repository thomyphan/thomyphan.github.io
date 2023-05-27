---
author_list: "Thomy Phan and Fabian Ritz and Jonas Nüßlein and Michael Kölle and Thomas Gabor and Claudia Linnhoff-Popien"
title: "Attention-Based Recurrency for Multi-Agent Reinforcement Learning under State Uncertainty"
collection: publications
permalink: /publication/2023-05-01-aamas-phan
excerpt: 'State uncertainty poses a major challenge for decentralized coordination but is largely neglected in state-of-the-art research due to a strong focus on state-based centralized training for decentralized execution (CTDE) and benchmarks that lack sufficient stochasticity like StarCraft Multi-Agent Challenge (SMAC). In this paper, we propose Attention-based Embeddings of Recurrence In multi-Agent Learning (AERIAL) to approximate value functions under agent-wise state uncertainty. AERIAL replaces the true state with a learned representation of multi-agent recurrence, considering more accurate information about decentralized agent decisions than state-based CTDE. We then introduce MessySMAC, a modified version of SMAC with stochastic observations and higher variance in initial states, to provide a more general and configurable benchmark regarding state uncertainty. We evaluate AERIAL in Dec-Tiger as well as in a variety of SMAC and MessySMAC maps, and compare the results with state-based CTDE. Furthermore, we evaluate the robustness of AERIAL and state-based CTDE against various state uncertainty configurations in MessySMAC.'
booktitle: "Extended Abstracts of the 22nd International Conference on Autonomous Agents and Multiagent Systems"
venue_short: "AAMAS"
date: "2023-05-01"
bibtexid: "phanAAMAS23"
isbn: "9781450394321"
paper_pages: "2839--2841"
paperurl: "https://thomyphan.github.io/files/2023-aamas-preprint.pdf"
extendedversion: "https://thomyphan.github.io/files/2023-icml-preprint.pdf"
eprint: "https://thomyphan.github.io/files/2023-aamas-preprint.pdf"
keywords: "recurrence, state uncertainty, multi-agent learning, dec-pomdp"
publisher: "International Foundation for Autonomous Agents and Multiagent Systems"
venuelocation: "London, United Kingdom"
coderepository: "https://github.com/thomyphan/messy_smac"
research_emergence: "False"
research_resilience : "False"
research_dependability : "False"
research_marl : "True"
research_planning : "False"
#layout: archive
---

{% include base_path %}

## Related Articles
- T. Phan et al., ["Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability"](https://thomyphan.github.io/publication/2023-07-01-icml-phan), ICML 2023 (extended version)
- T. Phan et al., ["VAST: Value Function Factorization with Variable Agent Sub-Teams"](https://thomyphan.github.io/publication/2021-12-01-neurips-phan), NeurIPS 2021

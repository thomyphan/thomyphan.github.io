---
author_list: "Thomy Phan and Fabian Ritz and Jonas Nüßlein and Michael Kölle and Thomas Gabor and Claudia Linnhoff-Popien"
title: "Attention-Based Recurrency for Multi-Agent Reinforcement Learning under State Uncertainty"
collection: publications
permalink: /publication/2023-05-01-aamas-phan
excerpt: 'State uncertainty poses a major challenge for decentralized coor- dination, where multiple agents act according to noisy observa- tions without any access to other agents’ information. Centralized training for decentralized execution (CTDE) is a multi-agent rein- forcement learning paradigm, which exploits global information to learn a centralized value function in order to derive coordinated multi-agent policies. State-based CTDE has become popular in multi-agent research due to remarkable progress in the StarCraft Multi-Agent Challenge (SMAC). However, SMAC scenarios are less suited for evaluation against state uncertainty due to determinis- tic observations and low variance in initial states. Furthermore, state-based CTDE largely neglects state uncertainty w.r.t. decentral- ization of agents and observations thus being possibly less effective in more general settings. In this paper, we address state uncer- tainty and introduce MessySMAC, a modified version of SMAC with stochastic observations and higher variance in initial states to pro- vide a more general and configurable benchmark. We then propose Attention-based Embeddings of Recurrency In multi-Agent Learning (AERIAL) to approximate value functions under consideration of state uncertainty. AERIAL replaces the true state in CTDE with the memory representation of all agents’ recurrent functions, which are processed by a self-attention mechanism. We evaluate AERIAL in Dec-Tiger as well as in a variety of SMAC and MessySMAC maps, and compare the results with state-based CTDE. We also evaluate the robustness of AERIAL and state-based CTDE against various configurations of state uncertainty in MessySMAC.'
booktitle: "Proceedings of the 22nd International Conference on Autonomous Agents and MultiAgent Systems (Extended Abstract)"
venue_short: "AAMAS"
date: "2023-05-01"
bibtexid: "phanAAMAS23"
paperurl: "https://arxiv.org/abs/2301.01649"
eprint: "https://thomyphan.github.io/files/2023-aamas-preprint.pdf"
keywords: "Dec-POMDP, state uncertainty, multi-agent learning, recurrency, self-Attention"
publisher: "International Foundation for Autonomous Agents and Multiagent Systems"
venuelocation: "London, UK"
coderepository: "https://github.com/thomyphan/messy_smac"
#layout: archive
---

{% include base_path %}

## Related Articles

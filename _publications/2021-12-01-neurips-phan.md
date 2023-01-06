---
author_list: "Thomy Phan and Fabian Ritz and Lenz Belzner and Philipp Altmann and Thomas Gabor and Claudia Linnhoff-Popien"
title: "VAST: Value Function Factorization with Variable Agent Sub-Teams"
collection: publications
permalink: /publication/2021-12-01-neurips-phan
excerpt: 'Value function factorization (VFF) is a popular approach to cooperative multi-agent reinforcement learning in order to learn local value functions from global rewards. However, state-of-the-art VFF is limited to a handful of agents in most domains. We hypothesize that this is due to the flat factorization scheme, where the VFF operator becomes a performance bottleneck with an increasing number of agents. Therefore, we propose VFF with variable agent sub-teams (VAST). VAST approximates a factorization for sub-teams which can be defined in an arbitrary way and vary over time, e.g., to adapt to different situations. The sub-team values are then linearly decomposed for all sub-team members. Thus, VAST can learn on a more focused and compact input representation of the original VFF operator. We evaluate VAST in three multi-agent domains and show that VAST can significantly outperform state-of-the-art VFF, when the number of agents is sufficiently large.'
booktitle: "Advances in Neural Information Processing Systems"
venue_short: "NeurIPS"
paper_pages: "24018--24032"
date: "2021-12-01"
bibtexid: "phanNeurIPS21"
paperurl: "https://openreview.net/forum?id=hyJKKIhfxxT"
eprint: "https://proceedings.neurips.cc/paper/2021/file/c97e7a5153badb6576d8939469f58336-Paper.pdf"
publisher: "Curran Associates, Inc."
coderepository: "https://github.com/thomyphan/scalable-marl"
#layout: archive
---

{% include base_path %}

## Related Articles
- T. Phan et al., ["Resilient Multi-Agent Reinforcement Learning with Adversarial Value Decomposition"](https://thomyphan.github.io/publication/2021-02-01-aaai-phan), AAAI 2021
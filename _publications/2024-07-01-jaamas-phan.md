---
author_list: "Thomy Phan and Felix Sommer and Fabian Ritz and Philipp Altmann and Jonas Nüßlein and Michael Kölle and Lenz Belzner and Claudia Linnhoff-Popien"
title: "Emergent Cooperation from Mutual Acknowledgment Exchange in Multi-Agent Reinforcement Learning"
collection: publications
permalink: /publication/2024-07-01-jaamas-phan
excerpt: 'Peer incentivization (PI) is a recent approach where all agents learn to reward or penalize each other in a distributed fashion, which often leads to emergent cooperation. Current PI mechanisms implicitly assume a flawless communication channel in order to exchange rewards. These rewards are directly incorporated into the learning process without any chance to respond with feedback. Furthermore, most PI approaches rely on global information, which limits scalability and applicability to real-world scenarios where only local information is accessible. In this paper, we propose Mutual Acknowledgment Token Exchange (MATE), a PI approach defined by a two-phase communication protocol to exchange acknowledgment tokens as incentives to shape individual rewards mutually. All agents condition their token transmissions on the locally estimated quality of their own situations based on environmental rewards and received tokens. MATE is completely decentralized and only requires local communication and information. We evaluate MATE in three social dilemma domains. Our results show that MATE is able to achieve and maintain significantly higher levels of cooperation than previous PI approaches. In addition, we evaluate the robustness of MATE in more realistic scenarios, where agents can deviate from the protocol and communication failures can occur.  We also evaluate the sensitivity of MATE w.r.t. the choice of token values.'
booktitle: "Autonomous Agents and Multi-Agent Systems"
venue_short: "JAAMAS"
#isbn: "9781450392136"
#paper_pages: "1047--1055"
date: "2024-07-01"
bibtexid: "phanJAAMAS2024"
paperdoi: "https://doi.org/10.1007/s10458-024-09666-5"
paperurl: "https://link.springer.com/article/10.1007/s10458-024-09666-5"
eprint: "https://link.springer.com/content/pdf/10.1007/s10458-024-09666-5.pdf"
keywords: "multi-agent learning, reinforcement learning, mutual acknowledgments, peer incentivization, emergent cooperation"
publisher: "Springer Nature"
coderepository: "https://github.com/thomyphan/emergent-cooperation"
#venuelocation: "Virtual Event, New Zealand"
#layout: archive
research_emergence: "True"
research_resilience : "False"
research_dependability : "False"
research_marl : "True"
research_planning : "False"
research_learning4search: "False"
---

{% include base_path %}

## Related Articles

- M. Koelle et al., ["Multi-Agent Quantum Reinforcement Learning using Evolutionary Optimization](https://thomyphan.github.io/publication/2024-02-01-icaart-koelle), ICAART 2024
- T. Phan et al., ["Emergent Cooperation from Mutual Acknowledgment Exchange"](https://thomyphan.github.io/publication/2022-05-01-aamas-phan), AAMAS 2022 (conference version)
- L. Belzner et al., ["The Sharer's Dilemma in Collective Adaptive Systems of Self-Interested Agents"](https://thomyphan.github.io/publication/2018-11-01-isola-belzner), ISoLA 2018
- K. Schmid et al., ["Action Markets in Deep Multi-Agent Reinforcement Learning"](https://thomyphan.github.io/publication/2018-08-01-icann-schmid), ICANN 2018
- T. Phan, ["Emergence and Resilience in Multi-Agent Reinforcement Learning"](https://thomyphan.github.io/publication/2023-06-26-phd-thesis-phan), PhD Thesis
---
author_list: "Andreas Sedlmeier and Thomas Gabor and Thomy Phan and Lenz Belzner and Claudia Linnhoff-Popien"
title: "Uncertainty-Based Out-of-Distribution Classification in Deep Reinforcement Learning"
collection: publications
permalink: /publication/2020-02-01-icaart-sedlmeier
excerpt: "Robustness to out-of-distribution (OOD) data is an important goal in building reliable machine learning systems. Especially in autonomous systems, wrong predictions for OOD inputs can cause safety critical situations. As a first step towards a solution, we consider the problem of detecting such data in a value-based deep reinforcement learning (RL) setting. Modelling this problem as a one-class classification problem, we propose a framework for uncertainty-based OOD classification: UBOOD. It is based on the effect that an agent's epistemic uncertainty is reduced for situations encountered during training (in-distribution), and thus lower than for unencountered (OOD) situations. Being agnostic towards the approach used for estimating epistemic uncertainty, combinations with different uncertainty estimation methods, e.g. approximate Bayesian inference methods or ensembling techniques are possible. We further present a first viable solution for calculating a dynamic classification threshold, based on the uncertainty distribution of the training data. Evaluation shows that the framework produces reliable classification results when combined with ensemble-based estimators, while the combination with concrete dropout-based estimators fails to reliably detect OOD situations. In summary, UBOOD presents a viable approach for OOD classification in deep RL settings by leveraging the epistemic uncertainty of the agent's value function."
booktitle: "Proceedings of the 12th International Conference on Agents and Artificial Intelligence"
venue_short: "ICAART"
paper_pages: "522--529"
date: "2020-02-01"
bibtexid: "sedlmeierICAART20"
paperdoi: "https://doi.org/10.5220/0008949905220529"
paperurl: "https://www.scitepress.org/Link.aspx?doi=10.5220/0008949905220529"
eprint: "https://thomyphan.github.io/files/2020-icaart-preprint.pdf"
#layout: archive
---

{% include base_path %}


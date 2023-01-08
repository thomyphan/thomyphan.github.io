---
layout: archive
title: "Dependability in Machine Learning Systems"
permalink: /research/dependability/
author_profile: true
---

{% include base_path %}

## Anomaly Detection

<img src="https://thomyphan.github.io/images/research/out_of_distribution.png" style="float:right; width:250pt;padding-left:10px;"  alt="OOD Example"/>

Generalization is an important concern in RL since agents are typically trained in a simulation with a limited scope. As the real-world is complex and messy, it is likely that RL agents encounter *novel situations* which are different from samples seen during training. Such *anomalies* or *out-of-distribution* samples can cause undesired behavior thus need to be considered carefully in safety-critical domains.

We investigate methods to measure an agent's uncertainty regarding a particular situation which can be used for monitoring to warn operators [1,2]. We also regard anomaly detection in a wider scope proposing desiderata for future problems like modeling of normalcy, absence of rewards during deployment, suitable response strategies, etc. [3].

*Publications:*  
[1] [Uncertainty-Based Detection](https://thomyphan.github.io/publication/2019-11-01-isaai-sedlmeier)  
[2] [Out-of-Distribution Classification Methods](https://thomyphan.github.io/publication/2020-02-01-icaart-sedlmeier)  
[3] [Anomaly Detection in Reinforcement Learning](https://thomyphan.github.io/publication/2022-05-01-aamas-mueller)  

## Specification Awareness

<img src="https://thomyphan.github.io/images/research/crashing_robots.png" style="float:right; width:250pt;padding-left:10px;"  alt="Crashing Robots"/>

RL agents are often trained and evaluated with respect to a single objective. In the real-world, a system typically has to comply with a *specification* consisting of functional and non-functional *requirements* though. These requirements may be aligned or in conflict with the original objective, e.g., finding a shortest path or maximizing throughput in a factory. Therefore, a *tradeoff solution* is needed which is hard to find for classic RL methods that preferrably stick to easy requirements while neglecting harder ones.

We investigate such solutions by proposing specification-aware (MA)RL which attempts to comply with several requirements in a smart factory scenario [1,2].

*Publications:*  
[1] [Specification Aware Learning](https://thomyphan.github.io/publication/2021-02-01-icaart-ritz)  
[2] [Specification Aware Multi-Agent Training](https://thomyphan.github.io/publication/2022-01-01-icaart-ritz)  

## Engineering and Operation

<img src="https://thomyphan.github.io/images/research/dependability_research.png" style="float:right; width:200pt;padding-left:10px;"  alt="Smart Grid Simulation"/>

Similar to software and system engineering, *machine learning (ML)* requires suitable tools, e.g., for design, validation, monitoring, root cause analysis, etc., beyond mere data to build and operate dependable systems. Such tools would help to improve safety, trust, and acceptance to deploy such systems in the real-world.

We develop process models and paradigms to enable an organized approach to building and operating dependable ML systems. We address adaptive testing for continuously evolving systems through coevolution [1], generic processes with ML specific artefacts [2], and self-adaptive operations which enable a high degree of automation in the engineering and operation process.

*Publications:*  
[1] [Scenario Coevolution Paradigm](https://thomyphan.github.io/publication/2020-01-01-sttt-gabor)  
[2] [Process Model for ML Engineering](https://thomyphan.github.io/publication/2020-08-01-qse-gabor)  
[3] [Self-Adaptive Engineering of ML Systems](https://thomyphan.github.io/publication/2022-10-01-isola-ritz)  

<div style="float: right;">
    <a href="https://thomyphan.github.io/research/"><strong>Back to Research</strong></a>
</div>
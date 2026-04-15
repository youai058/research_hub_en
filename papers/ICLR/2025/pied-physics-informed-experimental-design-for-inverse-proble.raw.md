---
title: "PIED: Physics-Informed Experimental Design for Inverse Problems"
authors: ["Apivich Hemachandra", "Gregory Kang Ruey Lau", "See-Kiong Ng", "Bryan Kian Hsiang Low"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "w7P92BEsb2"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ecbc79cad364be2be0e1e48a7cf0b675efc75687.pdf"
published: "2025"
categories: []
keywords: ["Physics-Informed Neural Network", "PINNs", "Experimental Design", "AI For Science", "Active Learning", "Data Selection"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:39+09:00"
---

# PIED: Physics-Informed Experimental Design for Inverse Problems

## Abstract
In many science and engineering settings, system dynamics are characterized by governing partial differential equations (PDEs), and a major challenge is to solve inverse problems (IPs) where unknown PDE parameters are inferred based on observational data gathered under limited budget. 
Due to the high costs of setting up and running experiments, experimental design (ED) is often done with the help of PDE simulations to optimize for the most informative design parameters (e.g., sensor placements) to solve such IPs, prior to actual data collection. This process of optimizing design parameters is especially critical when the budget and other practical constraints make it infeasible to adjust the design parameters between trials during the experiments.
However, existing experimental design (ED) methods tend to require sequential and frequent design parameter adjustments between trials. Furthermore, they also have significant computational bottlenecks due to the need for complex numerical simulations for PDEs, and do not exploit the advantages provided by physics informed neural networks (PINNs) in solving IPs for PDE-governed systems, such as its meshless solutions, differentiability, and amortized training. 
This work presents Physics-Informed Experimental Design (PIED), the first ED framework that makes use of PINNs in a fully differentiable architecture to perform continuous optimization of design parameters for IPs for one-shot deployments. 
PIED overcomes existing methods' computational bottlenecks through parallelized computation and meta-learning of PINN parameter initialization, and proposes novel methods to effectively take into account PINN training dynamics in optimizing the ED parameters. 
Through experiments based on noisy simulated data and even real world experimental data, we empirically show that given limited observation budget, PIED significantly outperforms existing ED methods in solving IPs, including for challenging settings where the inverse parameters are unknown functions rather than just finite-dimensional.

## Metadata
- venue: ICLR
- year: 2025
- authors: Apivich Hemachandra, Gregory Kang Ruey Lau, See-Kiong Ng, Bryan Kian Hsiang Low
- arxiv_id: 
- openreview_id: w7P92BEsb2
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ecbc79cad364be2be0e1e48a7cf0b675efc75687.pdf
- published: 2025
- keywords: Physics-Informed Neural Network, PINNs, Experimental Design, AI For Science, Active Learning, Data Selection

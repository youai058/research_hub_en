---
title: "EMFuse: Energy-based Model Fusion for Decision Making"
authors: ["Kejie He", "Yi-Chen Li", "Yang Yu"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "6wDp8XRmNI"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2d1bae055f1c4fe088d5bb5b7271a99eaae0c63f.pdf"
published: "2026"
categories: []
keywords: ["Model Fusion", "Energy-Based Model", "Decision Making"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:21+09:00"
---

# EMFuse: Energy-based Model Fusion for Decision Making

## Abstract
Model fusion has emerged as a promising research direction, offering a resource-efficient paradigm that leverages existing pre-trained models to circumvent the need for training from scratch. In this work, we investigate the fusion of models specifically adapted for decision-making tasks. This challenge divides into two distinct, yet related subproblems: the direct fusion of models that act as policy and the fusion of dynamics models that subsequently induce a policy. We suggest that these seemingly divergent subproblems can be unified through the lens of energy-based models (EBMs), which parameterizes a conditional distribution via an energy function where lower energy implies higher probability. Our framework, \textbf{EMFuse}, provides this convergence by leveraging the concept of energy as a common currency for fusion. For direct fusion of policies, such as those in language models, the output distribution is commonly softmax (Boltzmann), which essentially defines the negative logarithmic probability as an energy function. For dynamics models, existing works often train a set of models on the same dataset to obtain robust uncertainty estimation; such an ensemble approach leads to an exponential explosion in computational complexity when it comes to dynamics fusion across multiple sets of models. To overcome this, we introduce the Any-step Dynamics Energy-based Transition Model (ADETM), a novel architecture that performs efficient single-model-per-dataset uncertainty estimation with its energy-based backbone, thereby avoiding this computational explosion. Our EMFuse framework surpasses other baselines by 0.34\% to 6.63\% on single/cross domain discrete decision-making benchmarks, and achieved an extra 2.3 to 7.4 normalized points on average in D4RL MuJoCo continuous-control scenarios. Our code is available at https://github.com/LAMDA-RL/EMFuse.

## Metadata
- venue: ICLR
- year: 2026
- authors: Kejie He, Yi-Chen Li, Yang Yu
- arxiv_id: 
- openreview_id: 6wDp8XRmNI
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2d1bae055f1c4fe088d5bb5b7271a99eaae0c63f.pdf
- published: 2026
- keywords: Model Fusion, Energy-Based Model, Decision Making

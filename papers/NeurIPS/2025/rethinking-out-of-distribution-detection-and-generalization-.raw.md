---
title: "Rethinking Out-of-Distribution Detection and Generalization with Collective Behavior Dynamics"
authors: ["Zhenbin Wang", "Lei Zhang", "Wei Huang", "Zhao Zhang", "Zizhou Wang"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "VD22PY0fZm"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/68095a4ea2fb3abccdf64e4f86a2b70b6ce0a2e6.pdf"
published: "2025"
categories: []
keywords: ["domain shift", "out-of-distribution detection", "out-of-distribution generalization", "transfer learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:45+09:00"
---

# Rethinking Out-of-Distribution Detection and Generalization with Collective Behavior Dynamics

## Abstract
Out-of-distribution (OOD) problems commonly occur when models process data with a distribution significantly deviates from the in-distribution (InD) training data. In this paper, we hypothesize that a $\textit{field}$ or $\textit{potential}$ more essential than features exists, and features are not the ultimate essence of the data but rather manifestations of them during training. we investigate OOD problems from the perspective of collective behavior dynamics. With this in mind, we first treat the output of the feature extractor as charged particles and investigate their collective behavior dynamics within a self-consistent electric field. Then, to characterize the relationship between OOD problems and dynamical equations, we introduce the $\textit{basin of attraction}$ and prove that its boundary can be represented as the zero level set of a differentiable function of the potential, $\textit{i.e.}$, the spatial integral of field. We further demonstrate that: $\textit{i)}$ InD and OOD inputs can be effectively separated based on whether they are steady state solutions for specific field conditions, enabling robust OOD detection and outperforming prior methods over three benchmarks. $\textit{ii)}$ the generalization capability correlates positively with the basin of attraction. By analyzing the dynamics of perturbations, we propose that the potential is well-characterized by a Fourier-domain form of the Poisson equation. Evaluated on six benchmark datasets, our method rivals the SoTA approaches for OOD generalization and can be seamlessly integrated with them to deliver additional gains.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Zhenbin Wang, Lei Zhang, Wei Huang, Zhao Zhang, Zizhou Wang
- arxiv_id: 
- openreview_id: VD22PY0fZm
- anthology_id: 
- pdf_url: https://openreview.net/pdf/68095a4ea2fb3abccdf64e4f86a2b70b6ce0a2e6.pdf
- published: 2025
- keywords: domain shift, out-of-distribution detection, out-of-distribution generalization, transfer learning

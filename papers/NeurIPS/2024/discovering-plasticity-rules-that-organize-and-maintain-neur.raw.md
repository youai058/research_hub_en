---
title: "Discovering plasticity rules that organize and maintain neural circuits"
authors: ["David G Bell", "Alison Duffy", "Adrienne Fairhall"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "nw4TWuEPGx"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2c8b4c60fb82f62769e10bc0419f404b8627168d.pdf"
published: "2024"
categories: []
keywords: ["biologically plausible learning rules plasticity self-organization RNNs homeostasis meta-learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:31+09:00"
---

# Discovering plasticity rules that organize and maintain neural circuits

## Abstract
Intrinsic dynamics within the brain can accelerate learning by providing a prior scaffolding for dynamics aligned with task objectives. Such intrinsic dynamics would ideally self-organize and self-sustain in the face of biological noise including synaptic turnover and cell death. An example of such dynamics is the formation of sequences, a ubiquitous motif in neural activity. The sequence-generating circuit in zebra finch HVC provides a reliable timing scaffold for motor output in song and demonstrates a remarkable capacity for unsupervised recovery following perturbation. Inspired by HVC, we seek a local plasticity rule capable of organizing and maintaining sequence-generating dynamics despite continual network perturbations. We adopt a meta-learning approach introduced by Confavreux et al, which parameterizes a learning rule using basis functions constructed from pre- and postsynaptic activity and synapse size, with tunable time constants. Candidate rules are simulated within initially random networks, and their fitness is evaluated according to a loss function that measures the fidelity with which the resulting dynamics encode time. We use this approach to introduce biological noise, forcing meta-learning to find robust solutions. We first show that, in the absence of perturbations, meta-learning identifies a temporally asymmetric generalization of Oja's rule that reliably organizes sparse sequential activity. When synaptic turnover is introduced, the learned rule incorporates a form of homeostasis, better maintaining robust sequential dynamics relative to other previously proposed rules. Additionally, inspired by recent findings demonstrating that the strength of projections from inhibitory interneurons in HVC also dynamically responds to perturbations, we explore the role of inhibitory plasticity in sequence-generating circuits. We find that learned plasticity adjusts both excitation and inhibition in response to manipulations, outperforming rules applied only to excitatory connections. We demonstrate how plasticity acting on both excitatory and inhibitory synapses can better shape excitatory cell dynamics to scaffold timing representations.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: David G Bell, Alison Duffy, Adrienne Fairhall
- arxiv_id: 
- openreview_id: nw4TWuEPGx
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2c8b4c60fb82f62769e10bc0419f404b8627168d.pdf
- published: 2024
- keywords: biologically plausible learning rules plasticity self-organization RNNs homeostasis meta-learning

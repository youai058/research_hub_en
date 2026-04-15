---
title: "Universal Value-Function Uncertainties"
authors: ["Moritz Akiya Zanger", "Max Weltevrede", "Yaniv Oren", "Pascal R. Van der Vaart", "Caroline Horsch", "Wendelin Boehmer", "Matthijs T. J. Spaan"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "NeAzH9u2jh"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/71045037555bfed0492f7a3b41a96f87b073c013.pdf"
published: "2026"
categories: []
keywords: ["Uncertainty Quantificaiton", "Epistemic Uncertainty", "Exploration", "Offline RL", "Neural Tanget Kernel", "Multitask RL"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:44+09:00"
---

# Universal Value-Function Uncertainties

## Abstract
Estimating epistemic uncertainty in value functions is a crucial challenge for many aspects of reinforcement learning (RL), including efficient exploration, safe decision-making, and offline RL. While deep ensembles provide a robust method for quantifying value uncertainty, they come with significant computational overhead. Single-model methods, while computationally favorable, often rely on heuristics and typically require additional propagation mechanisms for myopic uncertainty estimates. In this work we introduce universal value-function uncertainties (UVU), which, similar in spirit to random network distillation (RND), quantify uncertainty as squared prediction errors between an online learner and a fixed, randomly initialized target network. Unlike RND, UVU errors reflect policy-conditional $\textit{value uncertainty}$, incorporating the future uncertainties $\textit{any policy}$ may encounter. This is due to the training procedure employed in UVU: the online network is trained using temporal difference learning with a synthetic reward derived from the fixed, randomly initialized target network. We provide an extensive theoretical analysis of our approach using neural tangent kernel (NTK) theory and show that in the limit of infinite network width, UVU errors are exactly equivalent to the variance of an ensemble of independent universal value functions. Empirically, we show that UVU achieves equal performance to large ensembles on challenging multi-task offline RL settings, while offering simplicity and substantial computational savings.

## Metadata
- venue: ICLR
- year: 2026
- authors: Moritz Akiya Zanger, Max Weltevrede, Yaniv Oren, Pascal R. Van der Vaart, Caroline Horsch, Wendelin Boehmer, Matthijs T. J. Spaan
- arxiv_id: 
- openreview_id: NeAzH9u2jh
- anthology_id: 
- pdf_url: https://openreview.net/pdf/71045037555bfed0492f7a3b41a96f87b073c013.pdf
- published: 2026
- keywords: Uncertainty Quantificaiton, Epistemic Uncertainty, Exploration, Offline RL, Neural Tanget Kernel, Multitask RL

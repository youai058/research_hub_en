---
title: "Learning conformational ensembles of proteins based on backbone geometry"
authors: ["Nicolas Wolf", "Leif Seute", "Vsevolod Viliuga", "Simon Wagner", "Jan Stühmer", "Frauke Gräter"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "1frqf6iY4v"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/67c4b6cf7d7a96663ccc956530fffdd1c61edffb.pdf"
published: "2025"
categories: []
keywords: ["Proteins", "Boltzmann", "Flow Matching", "Protein structure", "Protein conformation", "Molecular Dynamics", "Generative models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:42+09:00"
---

# Learning conformational ensembles of proteins based on backbone geometry

## Abstract
Deep generative models have recently been proposed for sampling protein conformations from the Boltzmann distribution, as an alternative to often prohibitively expensive Molecular Dynamics simulations. However, current state-of-the-art approaches rely on fine-tuning pre-trained folding models and evolutionary sequence information, limiting their applicability and efficiency, and introducing potential biases. In this work, we propose a flow matching model for sampling protein conformations based solely on backbone geometry - BBFlow. We introduce a geometric encoding of the backbone equilibrium structure as input and propose to condition not only the flow but also the prior distribution on the respective equilibrium structure, eliminating the need for evolutionary information. The resulting model is orders of magnitudes faster than current state-of-the-art approaches at comparable accuracy, is transferable to multi-chain proteins, and can be trained from scratch in a few GPU days. In our experiments, we demonstrate that the proposed model achieves competitive performance with reduced inference time, across not only an established benchmark of naturally occurring proteins but also de novo proteins, for which evolutionary information is scarce or absent. BBFlow is available at https://github.com/graeter-group/bbflow.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Nicolas Wolf, Leif Seute, Vsevolod Viliuga, Simon Wagner, Jan Stühmer, Frauke Gräter
- arxiv_id: 
- openreview_id: 1frqf6iY4v
- anthology_id: 
- pdf_url: https://openreview.net/pdf/67c4b6cf7d7a96663ccc956530fffdd1c61edffb.pdf
- published: 2025
- keywords: Proteins, Boltzmann, Flow Matching, Protein structure, Protein conformation, Molecular Dynamics, Generative models

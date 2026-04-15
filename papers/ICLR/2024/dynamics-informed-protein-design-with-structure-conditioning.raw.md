---
title: "Dynamics-Informed Protein Design with Structure Conditioning"
authors: ["Urszula Julia Komorowska", "Simon V Mathis", "Kieran Didi", "Francisco Vargas", "Pietro Lio", "Mateja Jamnik"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "jZPqf2G9Sw"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0ffbbb38174d8802162c0bef4914451f67318f38.pdf"
published: "2024"
categories: []
keywords: ["Diffusion Models", "Generative Modeling", "Protein Design", "Normal Mode Analysis"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:55+09:00"
---

# Dynamics-Informed Protein Design with Structure Conditioning

## Abstract
Current protein generative models are able to design novel backbones with desired shapes or functional motifs. However, despite the importance of a protein’s dynamical properties for its function, conditioning on dynamical properties remains elusive. We present a new approach to protein generative modeling by leveraging Normal Mode Analysis that enables us to capture dynamical properties too. We introduce a method for conditioning the diffusion probabilistic models on protein dynamics, specifically on the lowest non-trivial normal mode of oscillation. Our method, similar to the classifier guidance conditioning, formulates the sampling process as being driven by conditional and unconditional terms. However, unlike previous works, we approximate the conditional term with a simple analytical function rather than an external neural network, thus making the eigenvector calculations approachable. We present the corresponding SDE theory as a formal justification of our approach. We extend our framework to conditioning on structure and dynamics at the same time, enabling scaffolding of the dynamical motifs. We demonstrate the empirical effectiveness of our method by turning the open-source unconditional protein diffusion model Genie into the conditional model with no retraining. Generated proteins exhibit the desired dynamical and structural properties while still being biologically plausible. Our work represents a first step towards incorporating dynamical behaviour in protein design and may open the door to designing more flexible and functional proteins in the future.

## Metadata
- venue: ICLR
- year: 2024
- authors: Urszula Julia Komorowska, Simon V Mathis, Kieran Didi, Francisco Vargas, Pietro Lio, Mateja Jamnik
- arxiv_id: 
- openreview_id: jZPqf2G9Sw
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0ffbbb38174d8802162c0bef4914451f67318f38.pdf
- published: 2024
- keywords: Diffusion Models, Generative Modeling, Protein Design, Normal Mode Analysis

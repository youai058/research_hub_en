---
title: "SIM: Surface-based fMRI Analysis for Inter-Subject Multimodal Decoding from Movie-Watching Experiments"
authors: ["Simon Dahan", "Gabriel Bénédict", "Logan Zane John Williams", "Yourong Guo", "Daniel Rueckert", "Robert Leech", "Emma Claire Robinson"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "OJsMGsO6yn"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/5b868cf68017a22e06f1daa0aa4a4f14e7efd563.pdf"
published: "2025"
categories: []
keywords: ["movie-watching experiment", "fMRI", "cortical analysis", "surface-based transformers", "multimodal learning", "contrastive learning", "self-supervised learning", "generalization", "encoding/decoding"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:56+09:00"
---

# SIM: Surface-based fMRI Analysis for Inter-Subject Multimodal Decoding from Movie-Watching Experiments

## Abstract
Current AI frameworks for brain decoding and encoding, typically train and test models within the same datasets. This limits their utility for cognitive training (neurofeedback) for which it would be useful to pool experiences across individuals to better simulate stimuli not sampled during training. A key obstacle to model generalisation is the degree of variability of inter-subject cortical organisation, which makes it difficult to align or compare cortical signals across participants. In this paper we address this through use of surface vision transformers, which build a generalisable model of cortical functional dynamics, through encoding the topography of cortical networks and their interactions as a moving image across a surface. This is then combined with tri-modal self-supervised contrastive (CLIP) alignment of audio, video, and fMRI modalities to enable the retrieval of visual and auditory stimuli from patterns of cortical activity (and vice-versa).  We validate our approach on 7T task-fMRI data from 174 healthy participants engaged in the movie-watching experiment from the Human Connectome Project (HCP). Results show that it is possible to detect which movie clips an individual is watching purely from their brain activity, even for individuals and movies *not seen during training*. Further analysis of attention maps reveals that our model captures individual patterns of brain activity that reflect semantic and visual systems. This opens the door to future personalised simulations of brain function. Code \& pre-trained models will be made available at https://github.com/metrics-lab/sim.

## Metadata
- venue: ICLR
- year: 2025
- authors: Simon Dahan, Gabriel Bénédict, Logan Zane John Williams, Yourong Guo, Daniel Rueckert, Robert Leech, Emma Claire Robinson
- arxiv_id: 
- openreview_id: OJsMGsO6yn
- anthology_id: 
- pdf_url: https://openreview.net/pdf/5b868cf68017a22e06f1daa0aa4a4f14e7efd563.pdf
- published: 2025
- keywords: movie-watching experiment, fMRI, cortical analysis, surface-based transformers, multimodal learning, contrastive learning, self-supervised learning, generalization, encoding/decoding

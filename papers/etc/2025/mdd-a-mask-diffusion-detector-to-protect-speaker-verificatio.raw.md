---
title: "MDD: a Mask Diffusion Detector to Protect Speaker Verification Systems from Adversarial Perturbations"
authors: ["Yibo Bai", "Sizhou Chen", "Michele Panariello", "Xiao-Lei Zhang", "Massimiliano Todisco", "Nicholas Evans"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2508.19180"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2508.19180v1"
published: "2025-08-26"
categories: ["eess.AS", "cs.SD"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:29+09:00"
---

# MDD: a Mask Diffusion Detector to Protect Speaker Verification Systems from Adversarial Perturbations

## Abstract
Speaker verification systems are increasingly deployed in security-sensitive applications but remain highly vulnerable to adversarial perturbations. In this work, we propose the Mask Diffusion Detector (MDD), a novel adversarial detection and purification framework based on a \textit{text-conditioned masked diffusion model}. During training, MDD applies partial masking to Mel-spectrograms and progressively adds noise through a forward diffusion process, simulating the degradation of clean speech features. A reverse process then reconstructs the clean representation conditioned on the input transcription. Unlike prior approaches, MDD does not require adversarial examples or large-scale pretraining. Experimental results show that MDD achieves strong adversarial detection performance and outperforms prior state-of-the-art methods, including both diffusion-based and neural codec-based approaches. Furthermore, MDD effectively purifies adversarially-manipulated speech, restoring speaker verification performance to levels close to those observed under clean conditions. These findings demonstrate the potential of diffusion-based masking strategies for secure and reliable speaker verification systems.

## Metadata
- venue: arXiv
- year: 2025
- authors: Yibo Bai, Sizhou Chen, Michele Panariello, Xiao-Lei Zhang, Massimiliano Todisco, Nicholas Evans
- arxiv_id: 2508.19180
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2508.19180v1
- published: 2025-08-26

---
title: "Unlocking the Power of Spatial and Temporal Information in Medical Multimodal Pre-training"
authors: ["Jinxia Yang", "Bing Su", "Xin Zhao", "Ji-Rong Wen"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "87ZrVHDqmR"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/fc308e57a9225cbeaf51e4e561fdb488ef4fb77a.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:43+09:00"
---

# Unlocking the Power of Spatial and Temporal Information in Medical Multimodal Pre-training

## Abstract
Medical vision-language pre-training methods mainly leverage the correspondence between paired medical images and radiological reports. Although multi-view spatial images and temporal sequences of image-report pairs are available in off-the-shelf multi-modal medical datasets, most existing methods have not thoroughly tapped into such extensive supervision signals. In this paper, we introduce the Med-ST framework for fine-grained spatial and temporal modeling to exploit information from multiple spatial views of chest radiographs and temporal historical records. For spatial modeling, Med-ST employs the *Mixture of View Expert (MoVE)* architecture to integrate different visual features from both frontal and lateral views. To achieve a more comprehensive alignment, Med-ST not only establishes the global alignment between whole images and texts but also introduces modality-weighted local alignment between text tokens and spatial regions of images. For temporal modeling, we propose a novel cross-modal bidirectional cycle consistency objective by forward mapping classification (FMC) and reverse mapping regression (RMR). By perceiving temporal information from simple to complex, Med-ST can learn temporal semantics. Experimental results across four distinct tasks demonstrate the effectiveness of Med-ST, especially in temporal classification tasks. Our code and model are available at https://github.com/SVT-Yang/MedST.

## Metadata
- venue: ICML
- year: 2024
- authors: Jinxia Yang, Bing Su, Xin Zhao, Ji-Rong Wen
- arxiv_id: 
- openreview_id: 87ZrVHDqmR
- anthology_id: 
- pdf_url: https://openreview.net/pdf/fc308e57a9225cbeaf51e4e561fdb488ef4fb77a.pdf
- published: 2024

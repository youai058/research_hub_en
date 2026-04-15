---
title: "Ensembling Diffusion Models via Adaptive Feature Aggregation"
authors: ["Cong Wang", "Kuan Tian", "Yonghang Guan", "Fei Shen", "Zhiwei Jiang", "Qing Gu", "Jun Zhang"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "e32cI4r8Eo"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/de153c66d053dcb62e654dba69c42c802d46ce1a.pdf"
published: "2025"
categories: []
keywords: ["Image Generation", "Diffusion Models", "Model Ensembling"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:00+09:00"
---

# Ensembling Diffusion Models via Adaptive Feature Aggregation

## Abstract
The success of the text-guided diffusion model has inspired the development and release of numerous powerful diffusion models within the open-source community. These models are typically fine-tuned on various expert datasets, showcasing diverse denoising capabilities. Leveraging multiple high-quality models to produce stronger generation ability is valuable, but has not been extensively studied. Existing methods primarily adopt parameter merging strategies to produce a new static model. However, they overlook the fact that the divergent denoising capabilities of the models may dynamically change across different states, such as when experiencing different prompts, initial noises, denoising steps, and spatial locations. In this paper, we propose a novel ensembling method, Adaptive Feature Aggregation (AFA), which dynamically adjusts the contributions of multiple models at the feature level according to various states (i.e., prompts, initial noises, denoising steps, and spatial locations), thereby keeping the advantages of multiple diffusion models, while suppressing their disadvantages. Specifically, we design a lightweight Spatial-Aware Block-Wise (SABW) feature aggregator that adaptive aggregates the block-wise intermediate features from multiple U-Net denoisers into a unified one. The core idea lies in dynamically producing an individual attention map for each model's features by comprehensively considering various states. It is worth noting that only SABW is trainable with about 50 million parameters, while other models are frozen. Both the quantitative and qualitative experiments demonstrate the effectiveness of our proposed method.

## Metadata
- venue: ICLR
- year: 2025
- authors: Cong Wang, Kuan Tian, Yonghang Guan, Fei Shen, Zhiwei Jiang, Qing Gu, Jun Zhang
- arxiv_id: 
- openreview_id: e32cI4r8Eo
- anthology_id: 
- pdf_url: https://openreview.net/pdf/de153c66d053dcb62e654dba69c42c802d46ce1a.pdf
- published: 2025
- keywords: Image Generation, Diffusion Models, Model Ensembling

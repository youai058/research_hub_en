---
title: "DiffCLIP: Few-shot Language-driven Multimodal Classifier"
authors: ["Jiaqing Zhang", "Mingxiang Cao", "Xue Yang", "Kai Jiang", "Yunsong Li"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2412.07119"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2412.07119v1"
published: "2024-12-10"
categories: ["cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:05+09:00"
---

# DiffCLIP: Few-shot Language-driven Multimodal Classifier

## Abstract
Visual language models like Contrastive Language-Image Pretraining (CLIP) have shown impressive performance in analyzing natural images with language information. However, these models often encounter challenges when applied to specialized domains such as remote sensing due to the limited availability of image-text pairs for training. To tackle this issue, we introduce DiffCLIP, a novel framework that extends CLIP to effectively convey comprehensive language-driven semantic information for accurate classification of high-dimensional multimodal remote sensing images. DiffCLIP is a few-shot learning method that leverages unlabeled images for pretraining. It employs unsupervised mask diffusion learning to capture the distribution of diverse modalities without requiring labels. The modality-shared image encoder maps multimodal data into a unified subspace, extracting shared features with consistent parameters across modalities. A well-trained image encoder further enhances learning by aligning visual representations with class-label text information from CLIP. By integrating these approaches, DiffCLIP significantly boosts CLIP performance using a minimal number of image-text pairs. We evaluate DiffCLIP on widely used high-dimensional multimodal datasets, demonstrating its effectiveness in addressing few-shot annotated classification tasks. DiffCLIP achieves an overall accuracy improvement of 10.65% across three remote sensing datasets compared with CLIP, while utilizing only 2-shot image-text pairs. The code has been released at https://github.com/icey-zhang/DiffCLIP.

## Metadata
- venue: arXiv
- year: 2024
- authors: Jiaqing Zhang, Mingxiang Cao, Xue Yang, Kai Jiang, Yunsong Li
- arxiv_id: 2412.07119
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2412.07119v1
- published: 2024-12-10

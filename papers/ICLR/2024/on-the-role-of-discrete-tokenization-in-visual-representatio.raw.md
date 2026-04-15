---
title: "On the Role of Discrete Tokenization in Visual Representation Learning"
authors: ["Tianqi Du", "Yifei Wang", "Yisen Wang"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "WNLAkjUm19"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/df6a2badfb1ca27a043b219c9e61e43688458fdf.pdf"
published: "2024"
categories: []
keywords: ["Self-supervised learning", "Masked image modeling", "Discrete visual token"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:09+09:00"
---

# On the Role of Discrete Tokenization in Visual Representation Learning

## Abstract
In the realm of self-supervised learning (SSL), masked image modeling (MIM) has gained popularity alongside contrastive learning methods. MIM involves reconstructing masked regions of input images using their unmasked portions. A notable subset of MIM methodologies employs discrete tokens as the reconstruction target, but the theoretical underpinnings of this choice remain underexplored. In this paper, we explore the role of these discrete tokens, aiming to unravel their benefits and limitations. Building upon the connection between MIM and contrastive learning, we provide a comprehensive theoretical understanding on how discrete tokenization affects the model's generalization capabilities. Furthermore, we propose a novel metric named TCAS, which is specifically designed to assess the effectiveness of discrete tokens within the MIM framework. Inspired by this metric, we contribute an innovative tokenizer design and propose a corresponding MIM method named ClusterMIM. It demonstrates superior performance on a variety of benchmark datasets and ViT backbones. Code is available at \url{https://github.com/PKU-ML/ClusterMIM}.

## Metadata
- venue: ICLR
- year: 2024
- authors: Tianqi Du, Yifei Wang, Yisen Wang
- arxiv_id: 
- openreview_id: WNLAkjUm19
- anthology_id: 
- pdf_url: https://openreview.net/pdf/df6a2badfb1ca27a043b219c9e61e43688458fdf.pdf
- published: 2024
- keywords: Self-supervised learning, Masked image modeling, Discrete visual token

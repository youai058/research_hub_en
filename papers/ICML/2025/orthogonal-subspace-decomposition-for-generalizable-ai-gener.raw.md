---
title: "Orthogonal Subspace Decomposition for Generalizable AI-Generated Image Detection"
authors: ["Zhiyuan Yan", "Jiangming Wang", "Peng Jin", "Ke-Yue Zhang", "Chengchun Liu", "Shen Chen", "Taiping Yao", "Shouhong Ding", "Baoyuan Wu", "Li Yuan"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "GFpjO8S8Po"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/97f641d9bd750ec47459852772e2288378e85448.pdf"
published: "2025"
categories: []
keywords: ["AI-Generated Image Detection", "Face Forgery Detection", "Deepfake Detection", "Media Forensics"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:32+09:00"
---

# Orthogonal Subspace Decomposition for Generalizable AI-Generated Image Detection

## Abstract
Detecting AI-generated images (AIGIs), such as natural images or face images, has become increasingly important yet challenging. In this paper, we start from a new perspective to excavate the reason behind the failure generalization in AIGI detection, named the asymmetry phenomenon, where a naively trained detector tends to favor overfitting to the limited and monotonous fake patterns, causing the feature space to become highly constrained and low-ranked, which is proved seriously limiting the expressivity and generalization. One potential remedy is incorporating the pre-trained knowledge within the vision foundation models (higher-ranked) to expand the feature space, alleviating the model's overfitting to fake. To this end, we employ Singular Value Decomposition (SVD) to decompose the original feature space into two orthogonal subspaces. By freezing the principal components and adapting only the remained components, we preserve the pre-trained knowledge while learning fake patterns. Compared to existing full-parameters and LoRA-based tuning methods, we explicitly ensure orthogonality, enabling the higher rank of the whole feature space, effectively minimizing overfitting and enhancing generalization. We finally identify a crucial insight: our method implicitly learns a vital prior that fakes are actually derived from the real, indicating a hierarchical relationship rather than independence. Modeling this prior, we believe, is essential for achieving superior generalization. Our codes are publicly available at https://github.com/YZY-stack/Effort-AIGI-Detection.

## Metadata
- venue: ICML
- year: 2025
- authors: Zhiyuan Yan, Jiangming Wang, Peng Jin, Ke-Yue Zhang, Chengchun Liu, Shen Chen, Taiping Yao, Shouhong Ding, Baoyuan Wu, Li Yuan
- arxiv_id: 
- openreview_id: GFpjO8S8Po
- anthology_id: 
- pdf_url: https://openreview.net/pdf/97f641d9bd750ec47459852772e2288378e85448.pdf
- published: 2025
- keywords: AI-Generated Image Detection, Face Forgery Detection, Deepfake Detection, Media Forensics

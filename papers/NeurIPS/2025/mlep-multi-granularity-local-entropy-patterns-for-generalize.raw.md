---
title: "MLEP: Multi-granularity Local Entropy Patterns for Generalized AI-generated Image Detection"
authors: ["Lin Yuan", "Xiaowan Li", "Yan Zhang", "Jiawei Zhang", "Hongbo Li", "Xinbo Gao"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Bsska2ayiy"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2e39809559010fe1710b05b716a55b819843a96c.pdf"
published: "2025"
categories: []
keywords: ["AI-generated image detection", "entropy", "multi-granularity", "deepfake detection"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:28+09:00"
---

# MLEP: Multi-granularity Local Entropy Patterns for Generalized AI-generated Image Detection

## Abstract
Advances in image generation technologies have raised growing concerns about their potential misuse, particularly in producing misinformation and deepfakes. This creates an urgent demand for effective methods to detect AI-generated images (AIGIs). While progress has been made, achieving reliable performance across diverse generative models and scenarios remains challenging due to the absence of source-invariant features and the limited generalization of existing approaches. In this study, we investigate the potential of using image entropy as a discriminative cue for AIGI detection and propose Multi-granularity Local Entropy Patterns (MLEP), a set of feature maps computed based on Shannon entropy from shuffled small patches at multiple image scales. MLEP effectively captures pixel dependencies across scales and dimensions while disrupting semantic content, thereby reducing potential content bias. Based on MLEP, we can easily build a robust CNN-based classifier capable of detecting AIGIs with enhanced reliability. Extensive experiments in an open-world setting, involving images synthesized by 32 distinct generative models, demonstrate that our approach achieves substantial improvements over state-of-the-art methods in both accuracy and generalization. Our code and models are available at https://www.github.com/fkeufss/MLEP/.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Lin Yuan, Xiaowan Li, Yan Zhang, Jiawei Zhang, Hongbo Li, Xinbo Gao
- arxiv_id: 
- openreview_id: Bsska2ayiy
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2e39809559010fe1710b05b716a55b819843a96c.pdf
- published: 2025
- keywords: AI-generated image detection, entropy, multi-granularity, deepfake detection

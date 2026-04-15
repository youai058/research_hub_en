---
title: "TS-MOF: Two-Stage Multi-Objective Fine-tuning for Long-Tailed Recognition"
authors: ["Zhe Zhao", "Zhiheng Gong", "Pengkun Wang", "HaiBin Wen", "Cankun Guo", "Bo Xue", "Xi Lin", "Zhenkun Wang", "Qingfu Zhang", "Yang Wang"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "S82Afyfbj3"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/3c28350522191fa926c941bcb25cbb9ef7c110d1.pdf"
published: "2025"
categories: []
keywords: ["Long-tailed learning", "Multi-objective optimization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:56+09:00"
---

# TS-MOF: Two-Stage Multi-Objective Fine-tuning for Long-Tailed Recognition

## Abstract
Long-Tailed Recognition (LTR) presents a significant challenge due to extreme class imbalance, where existing methods often struggle to balance performance across head and tail classes. Directly applying multi-objective optimization (MOO) to leverage multiple LTR strategies can be complex and unstable. To address this, we propose TS-MOF (Two-Stage Multi-Objective Fine-tuning), a novel framework that strategically decouples feature learning from classifier adaptation. After standard pre-training, TS-MOF freezes the feature backbone and focuses on an efficient multi-objective fine-tuning of specialized classifier heads. The core of TS-MOF's second stage lies in two innovations: Refined Performance Level Agreement for adaptive task weighting based on real-time per-class performance, and Robust Deterministic Projective Conflict Gradient for stable gradient conflict resolution and constructive fusion. This approach enables effective synergy between diverse LTR strategies, leading to significant and balanced performance improvements. Extensive experiments on CIFAR100-LT, ImageNet-LT, and iNaturalist 2018 demonstrate that TS-MOF achieves state-of-the-art results, particularly enhancing tail class accuracy (e.g., +3.3\% on CIFAR100-LT IR=100 tail) while improving head class performance, all within a remarkably short fine-tuning period of 20 epochs.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Zhe Zhao, Zhiheng Gong, Pengkun Wang, HaiBin Wen, Cankun Guo, Bo Xue, Xi Lin, Zhenkun Wang, Qingfu Zhang, Yang Wang
- arxiv_id: 
- openreview_id: S82Afyfbj3
- anthology_id: 
- pdf_url: https://openreview.net/pdf/3c28350522191fa926c941bcb25cbb9ef7c110d1.pdf
- published: 2025
- keywords: Long-tailed learning, Multi-objective optimization

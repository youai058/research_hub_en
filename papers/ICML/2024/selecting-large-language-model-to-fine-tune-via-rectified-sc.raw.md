---
title: "Selecting Large Language Model to Fine-tune via Rectified Scaling Law"
authors: ["Haowei Lin", "Baizhou Huang", "Haotian Ye", "Qinyu Chen", "Zihao Wang", "Sujian Li", "Jianzhu Ma", "Xiaojun Wan", "James Zou", "Yitao Liang"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Bq2THeNXRr"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f344b50c3e744f5a18efa4de6ce1df94be962d17.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:39+09:00"
---

# Selecting Large Language Model to Fine-tune via Rectified Scaling Law

## Abstract
The ever-growing ecosystem of LLMs has posed a challenge in selecting the most appropriate pre-trained model to fine-tune amidst a sea of options. Given constrained resources, fine-tuning all models and making selections afterward is unrealistic. In this work, we formulate this resource-constrained selection task into predicting fine-tuning performance and illustrate its natural connection with Scaling Law. Unlike pre-training, we find that the fine-tuning scaling curve includes not just the well-known "power phase" but also the previously unobserved "pre-power phase". We also explain why existing Scaling Law fails to capture this phase transition phenomenon both theoretically and empirically. To address this, we introduce the concept of "pre-learned data size" into our Rectified Scaling Law, which overcomes theoretical limitations and fits experimental results much better. By leveraging our law, we propose a novel LLM selection algorithm that selects the near-optimal model with hundreds of times less resource consumption, while other methods may provide negatively correlated selection. The project page is available at rectified-scaling-law.github.io.

## Metadata
- venue: ICML
- year: 2024
- authors: Haowei Lin, Baizhou Huang, Haotian Ye, Qinyu Chen, Zihao Wang, Sujian Li, Jianzhu Ma, Xiaojun Wan, James Zou, Yitao Liang
- arxiv_id: 
- openreview_id: Bq2THeNXRr
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f344b50c3e744f5a18efa4de6ce1df94be962d17.pdf
- published: 2024

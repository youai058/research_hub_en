---
title: "No Preference Left Behind: Group Distributional Preference Optimization"
authors: ["Binwei Yao", "Zefan Cai", "Yun-Shiuan Chuang", "Shanglin Yang", "Ming Jiang", "Diyi Yang", "Junjie Hu"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "bgpNJBD6Va"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6a97a75f830cfa76a1e56a22dc79655861112103.pdf"
published: "2025"
categories: []
keywords: ["preference alignment; large language model; fairness; group preferences"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:07+09:00"
---

# No Preference Left Behind: Group Distributional Preference Optimization

## Abstract
Preferences within a group of people are not uniform but follow a distribution. While existing alignment methods like Direct Preference Optimization (DPO) attempt to steer models to reflect human preferences, they struggle to capture the distributional pluralistic preferences within a group. These methods often skew toward dominant preferences, overlooking the diversity of opinions, especially when conflicting preferences arise. To address this issue, we propose Group Distributional Preference Optimization (GDPO), a novel framework that aligns language models with the distribution of preferences within a group by incorporating the concept of beliefs that shape individual preferences. GDPO calibrates a language model using statistical estimation of the group's belief distribution and aligns the model with belief-conditioned preferences, offering a more inclusive alignment framework than traditional methods. In experiments using both synthetic controllable opinion generation and real-world movie review datasets, we show that DPO fails to align with the targeted belief distributions, while GDPO consistently reduces this alignment gap during training. Additionally, our evaluation metrics demonstrate that GDPO outperforms existing approaches in aligning with group distributional preferences, marking a significant advance in pluralistic alignment.

## Metadata
- venue: ICLR
- year: 2025
- authors: Binwei Yao, Zefan Cai, Yun-Shiuan Chuang, Shanglin Yang, Ming Jiang, Diyi Yang, Junjie Hu
- arxiv_id: 
- openreview_id: bgpNJBD6Va
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6a97a75f830cfa76a1e56a22dc79655861112103.pdf
- published: 2025
- keywords: preference alignment; large language model; fairness; group preferences

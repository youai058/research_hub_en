---
title: "Fair and Efficient Contribution Valuation for Vertical Federated Learning"
authors: ["Zhenan Fan", "Huang Fang", "Xinglu Wang", "Zirui Zhou", "Jian Pei", "Michael Friedlander", "Yong Zhang"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "sLQb8q0sUi"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6a7f95c7baec41005e195a24ebc51afc7ef5acbf.pdf"
published: "2024"
categories: []
keywords: ["Vertical federated learning", "Contribution valuation", "Fairness"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:57+09:00"
---

# Fair and Efficient Contribution Valuation for Vertical Federated Learning

## Abstract
Federated learning is an emerging technology for training machine learning models across decentralized data sources without sharing data. Vertical federated learning, also known as feature-based federated learning, applies to scenarios where data sources have the same sample IDs but different feature sets. To ensure fairness among data owners, it is critical to objectively assess the contributions from different data sources and compensate the corresponding data owners accordingly. The Shapley value is a provably fair contribution valuation metric originating from cooperative game theory. However, its straight-forward computation requires extensively retraining a model on each potential combination of data sources, leading to prohibitively high communication and computation overheads due to multiple rounds of federated learning. To tackle this challenge, we propose a contribution valuation metric called vertical federated Shapley value (VerFedSV) based on the classic Shapley value. We show that VerFedSV not only satisfies many desirable properties of fairness but is also efficient to compute. Moreover, VerFedSV can be adapted to both synchronous and asynchronous vertical federated learning algorithms. Both theoretical analysis and extensive experimental results demonstrate the fairness, efficiency, adaptability, and effectiveness of VerFedSV.

## Metadata
- venue: ICLR
- year: 2024
- authors: Zhenan Fan, Huang Fang, Xinglu Wang, Zirui Zhou, Jian Pei, Michael Friedlander, Yong Zhang
- arxiv_id: 
- openreview_id: sLQb8q0sUi
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6a7f95c7baec41005e195a24ebc51afc7ef5acbf.pdf
- published: 2024
- keywords: Vertical federated learning, Contribution valuation, Fairness

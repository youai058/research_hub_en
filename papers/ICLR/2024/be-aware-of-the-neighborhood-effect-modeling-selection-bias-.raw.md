---
title: "Be Aware of the Neighborhood Effect: Modeling Selection Bias under Interference"
authors: ["Haoxuan Li", "Chunyuan Zheng", "Sihao Ding", "Peng Wu", "Zhi Geng", "Fuli Feng", "Xiangnan He"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "52fz5sUAy2"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9205f9cf9861ea57ce78d3007b54e1bcec2e5df6.pdf"
published: "2024"
categories: []
keywords: ["Selection Bias", "Neighborhood effect", "Recommender system"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:06+09:00"
---

# Be Aware of the Neighborhood Effect: Modeling Selection Bias under Interference

## Abstract
Selection bias in recommender system arises from the recommendation process of system filtering and the interactive process of user selection. Many previous studies have focused on addressing selection bias to achieve unbiased learning of the prediction model, but ignore the fact that potential outcomes for a given user-item pair may vary with the treatments assigned to other user-item pairs, named neighborhood effect. To fill the gap, this paper formally formulates the neighborhood effect as an interference problem from the perspective of causal inference, and introduces a treatment representation to capture the neighborhood effect. On this basis, we propose a novel ideal loss that can be used to deal with selection bias in the presence of neighborhood effect. We further develop two new estimators for estimating the proposed ideal loss. We theoretically establish the connection between the proposed and previous debiasing methods ignoring the neighborhood effect, showing that the proposed methods can achieve unbiased learning when both selection bias and neighborhood effects are present, while the existing methods are biased. Extensive semi-synthetic and real-world experiments are conducted to demonstrate the effectiveness of the proposed methods.

## Metadata
- venue: ICLR
- year: 2024
- authors: Haoxuan Li, Chunyuan Zheng, Sihao Ding, Peng Wu, Zhi Geng, Fuli Feng, Xiangnan He
- arxiv_id: 
- openreview_id: 52fz5sUAy2
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9205f9cf9861ea57ce78d3007b54e1bcec2e5df6.pdf
- published: 2024
- keywords: Selection Bias, Neighborhood effect, Recommender system

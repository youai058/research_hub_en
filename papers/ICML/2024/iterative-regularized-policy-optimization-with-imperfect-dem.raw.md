---
title: "Iterative Regularized Policy Optimization with Imperfect Demonstrations"
authors: ["Gong Xudong", "Feng Dawei", "Kele Xu", "Yuanzhao Zhai", "Chengkang Yao", "Weijia Wang", "Bo Ding", "Huaimin Wang"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Gp5F6qzwGK"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/79dd55526bc3e140436143b1309a12ad70949078.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:31+09:00"
---

# Iterative Regularized Policy Optimization with Imperfect Demonstrations

## Abstract
Imitation learning heavily relies on the quality of provided demonstrations. In scenarios where demonstrations are imperfect and rare, a prevalent approach for refining policies is through online fine-tuning with reinforcement learning, in which a Kullback–Leibler (KL) regularization is often employed to stabilize the learning process. However, our investigation reveals that on the one hand, imperfect demonstrations can bias the online learning process, the KL regularization will further constrain the improvement of online policy exploration. To address the above issues, we propose Iterative Regularized Policy Optimization (IRPO), a framework that involves iterative offline imitation learning and online reinforcement exploration. Specifically, the policy learned online is used to serve as the demonstrator for successive learning iterations, with a demonstration boosting to consistently enhance the quality of demonstrations. Experimental validations conducted across widely used benchmarks and a novel fixed-wing UAV control task consistently demonstrate the effectiveness of IRPO in improving both the demonstration quality and the policy performance. Our code is available at https://github.com/GongXudong/IRPO.

## Metadata
- venue: ICML
- year: 2024
- authors: Gong Xudong, Feng Dawei, Kele Xu, Yuanzhao Zhai, Chengkang Yao, Weijia Wang, Bo Ding, Huaimin Wang
- arxiv_id: 
- openreview_id: Gp5F6qzwGK
- anthology_id: 
- pdf_url: https://openreview.net/pdf/79dd55526bc3e140436143b1309a12ad70949078.pdf
- published: 2024

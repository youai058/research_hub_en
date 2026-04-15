---
title: "Diffusion Models Demand Contrastive Guidance for Adversarial Purification to Advance"
authors: ["Mingyuan Bai", "Wei Huang", "Tenghui Li", "Andong Wang", "Junbin Gao", "Cesar F Caiafa", "Qibin Zhao"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "2NUGeV64y2"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e129797d5fe791c60d5387deec712eef4e58e0d7.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:17+09:00"
---

# Diffusion Models Demand Contrastive Guidance for Adversarial Purification to Advance

## Abstract
In adversarial defense, adversarial purification can be viewed as a special generation task with the purpose to remove adversarial attacks and diffusion models excel in adversarial purification for their strong generative power. With different predetermined generation requirements, various types of guidance have been proposed, but few of them focuses on adversarial purification. In this work, we propose to guide diffusion models for adversarial purification using contrastive guidance. We theoretically derive the proper noise level added in the forward process diffusion models for adversarial purification from a feature learning perspective. For the reverse process, it is implied that the role of contrastive loss guidance is to facilitate the evolution towards the signal direction. From the theoretical findings and implications, we design the forward process with the proper amount of Gaussian noise added and the reverse process with the gradient of contrastive loss as the guidance of diffusion models for adversarial purification. Empirically, extensive experiments on CIFAR-10, CIFAR-100, the German Traffic Sign Recognition Benchmark and ImageNet datasets with ResNet and WideResNet classifiers show that our method outperforms most of current adversarial training and adversarial purification methods by a large improvement.

## Metadata
- venue: ICML
- year: 2024
- authors: Mingyuan Bai, Wei Huang, Tenghui Li, Andong Wang, Junbin Gao, Cesar F Caiafa, Qibin Zhao
- arxiv_id: 
- openreview_id: 2NUGeV64y2
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e129797d5fe791c60d5387deec712eef4e58e0d7.pdf
- published: 2024

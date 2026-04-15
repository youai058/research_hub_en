---
title: "NetMoE: Accelerating MoE Training through Dynamic Sample Placement"
authors: ["Xinyi Liu", "Yujie Wang", "Fangcheng Fu", "Xupeng Miao", "Shenhan Zhu", "Xiaonan Nie", "Bin CUI"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "1qP3lsatCR"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b92193e3eb230e379ba2c07078799b70a54ecc40.pdf"
published: "2025"
categories: []
keywords: ["Mixture of Experts", "All-to-All communication", "Distributed training"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:50+09:00"
---

# NetMoE: Accelerating MoE Training through Dynamic Sample Placement

## Abstract
Mixture of Experts (MoE) is a widely used technique to expand model sizes for better model quality while maintaining the computation cost constant. In a nutshell, an MoE model consists of multiple experts in each model layer and routes the training tokens to only a fixed number of experts rather than all. In distributed training, as experts are distributed among different GPUs, All-to-All communication is necessary to exchange the training tokens among the GPUs after each time of expert routing. Due to the frequent and voluminous data exchanges, All-to-All communication has become a notable challenge to training efficiency.

In this paper, we manage to accelerate All-to-All communication in MoE models from the training sample perspective, which is unexplored so far. In particular, we put forward the observation that tokens in the same training sample have certain levels of locality in expert routing. Motivated by this, we develop NetMoE, which takes such locality into account and dynamically rearranges the placement of training samples to minimize All-to-All communication costs. Specifically, we model the All-to-All communication given the sample placement and formulate an integer programming problem to deduce the optimal placement in polynomial time. Experiments with 32 GPUs show that NetMoE achieves a maximum efficiency improvement of $1.67 \times$ compared with current MoE training frameworks.

## Metadata
- venue: ICLR
- year: 2025
- authors: Xinyi Liu, Yujie Wang, Fangcheng Fu, Xupeng Miao, Shenhan Zhu, Xiaonan Nie, Bin CUI
- arxiv_id: 
- openreview_id: 1qP3lsatCR
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b92193e3eb230e379ba2c07078799b70a54ecc40.pdf
- published: 2025
- keywords: Mixture of Experts, All-to-All communication, Distributed training

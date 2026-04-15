---
title: "Pruning then Reweighting: Towards Data-Efficient Training of Diffusion Models"
authors: ["Yize Li", "Yihua Zhang", "Sijia Liu", "Xue Lin"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2409.19128"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2409.19128v2"
published: "2024-09-27"
categories: ["cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:05+09:00"
---

# Pruning then Reweighting: Towards Data-Efficient Training of Diffusion Models

## Abstract
Despite the remarkable generation capabilities of Diffusion Models (DMs), conducting training and inference remains computationally expensive. Previous works have been devoted to accelerating diffusion sampling, but achieving data-efficient diffusion training has often been overlooked. In this work, we investigate efficient diffusion training from the perspective of dataset pruning. Inspired by the principles of data-efficient training for generative models such as generative adversarial networks (GANs), we first extend the data selection scheme used in GANs to DM training, where data features are encoded by a surrogate model, and a score criterion is then applied to select the coreset. To further improve the generation performance, we employ a class-wise reweighting approach, which derives class weights through distributionally robust optimization (DRO) over a pre-trained reference DM. For a pixel-wise DM (DDPM) on CIFAR-10, experiments demonstrate the superiority of our methodology over existing approaches and its effectiveness in image synthesis comparable to that of the original full-data model while achieving the speed-up between 2.34 times and 8.32 times. Additionally, our method could be generalized to latent DMs (LDMs), e.g., Masked Diffusion Transformer (MDT) and Stable Diffusion (SD), and achieves competitive generation capability on ImageNet. Code is available here (https://github.com/Yeez-lee/Data-Selection-and-Reweighting-for-Diffusion-Models).

## Metadata
- venue: arXiv
- year: 2024
- authors: Yize Li, Yihua Zhang, Sijia Liu, Xue Lin
- arxiv_id: 2409.19128
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2409.19128v2
- published: 2024-09-27

---
title: "Cross-Timestep: 3D Diffusion Model with Trans-temporal Memory LSTM and Adaptive Priori Decoding Strategy for Medical Segmentation"
authors: ["Shangqian Wu", "Siyuan Shen", "Yahan Li", "Zhijian Huang", "Ziyu Fan", "Yuanpeng Zhang", "YI WANG", "Lei Deng"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "TE3asYO8PQ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/544b09d03bd01bc550e72a2fc995dc99f08354cc.pdf"
published: "2026"
categories: []
keywords: ["Diffusion Models; Medical Image Segmentation; LSTM"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:43+09:00"
---

# Cross-Timestep: 3D Diffusion Model with Trans-temporal Memory LSTM and Adaptive Priori Decoding Strategy for Medical Segmentation

## Abstract
Diffusion models have recently demonstrated significant robustness in medical image segmentation, effectively accommodating variations across different imaging styles. However, their applications remain limited due to: (i) current successes being primarily confined to 2D segmentation tasks—we observe that diffusion models tend to collapse at the early stage when applied to 3D medical tasks; and (ii) the inherently isolated iteration along timesteps during training and inference. To tackle these limitations, we propose a novel framework named Cross-Timestep, which incorporates two key innovations: an Adaptive Priori Decoding Strategy (APDS) and a trans-temporal memory LSTM (tLSTM) mechanism. (i) The APDS provides prior guidance during the diffusion process by employing a Priori Decoder(PD) that focuses solely on the conditional branch, successfully stabilizing the reverse diffusion process. (ii) The tLSTM integrates convolution and linear layers into the LSTM gating structure, and enhances the memory cell mechanism to retain temporal state, explicitly preserving and propagating continuous temporal states across timesteps. Experimental results demonstrate that Cross-Timestep performs favorably on heterogeneous 3D medical datasets. Three experiments further analyze the collapse phenomenon in 3D medical diffusion models and validate that APDS effectively prevents initial-stage collapse without excessively constraining the model, while tLSTM facilitates the performance and scalability of diffusion models.

## Metadata
- venue: ICLR
- year: 2026
- authors: Shangqian Wu, Siyuan Shen, Yahan Li, Zhijian Huang, Ziyu Fan, Yuanpeng Zhang, YI WANG, Lei Deng
- arxiv_id: 
- openreview_id: TE3asYO8PQ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/544b09d03bd01bc550e72a2fc995dc99f08354cc.pdf
- published: 2026
- keywords: Diffusion Models; Medical Image Segmentation; LSTM

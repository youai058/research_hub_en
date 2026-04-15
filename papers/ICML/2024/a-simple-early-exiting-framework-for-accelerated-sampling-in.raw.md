---
title: "A Simple Early Exiting Framework for Accelerated Sampling in Diffusion Models"
authors: ["Taehong Moon", "Moonseok Choi", "EungGu Yun", "Jongmin Yoon", "Gayoung Lee", "Jaewoong Cho", "Juho Lee"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "OnOaj3g9fi"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/24df0919176b5696bc4115b874852599216a19ec.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:22+09:00"
---

# A Simple Early Exiting Framework for Accelerated Sampling in Diffusion Models

## Abstract
Diffusion models have shown remarkable performance in generation problems over various domains including images, videos, text, and audio. A practical bottleneck of diffusion models is their sampling speed, due to the repeated evaluation of score estimation networks during the inference. In this work, we propose a novel framework capable of adaptively allocating compute required for the score estimation, thereby reducing the overall sampling time of diffusion models. We observe that the amount of computation required for the score estimation may vary along the time step for which the score is estimated. Based on this observation, we propose an early-exiting scheme, where we skip the subset of parameters in the score estimation network during the inference, based on a time-dependent exit schedule. Using the diffusion models for image synthesis, we show that our method could significantly improve the sampling throughput of the diffusion models without compromising image quality. Furthermore, we also demonstrate that our method seamlessly integrates with various types of solvers for faster sampling, capitalizing on their compatibility to enhance overall efficiency.

## Metadata
- venue: ICML
- year: 2024
- authors: Taehong Moon, Moonseok Choi, EungGu Yun, Jongmin Yoon, Gayoung Lee, Jaewoong Cho, Juho Lee
- arxiv_id: 
- openreview_id: OnOaj3g9fi
- anthology_id: 
- pdf_url: https://openreview.net/pdf/24df0919176b5696bc4115b874852599216a19ec.pdf
- published: 2024

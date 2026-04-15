---
title: "CAT: Contrastive Adversarial Training for Evaluating the Robustness of Protective Perturbations in Latent Diffusion Models"
authors: ["Sen Peng", "Mingyue Wang", "Jianfei He", "Jijia Yang", "Xiaohua Jia"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "5of0l7eUau"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b529e78039c362fde986fce103969e6379b8ab2a.pdf"
published: "2025"
categories: []
keywords: ["Latent Diffusion Models", "Protective Perturbations", "Adversarial Training"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:31+09:00"
---

# CAT: Contrastive Adversarial Training for Evaluating the Robustness of Protective Perturbations in Latent Diffusion Models

## Abstract
Latent diffusion models have recently demonstrated superior capabilities in many downstream image synthesis tasks. 
However, customization of latent diffusion models using unauthorized data can severely compromise the privacy and intellectual property rights of data owners.
Adversarial examples as protective perturbations have been developed to defend against unauthorized data usage by introducing imperceptible noise to customization samples, preventing diffusion models from effectively learning them.
In this paper, we first reveal that the primary reason adversarial examples are effective as protective perturbations in latent diffusion models is the distortion of their latent representations, as demonstrated through qualitative and quantitative experiments.
We then propose the Contrastive Adversarial Training (CAT) utilizing lightweight adapters as an adaptive attack against these protection methods, highlighting their lack of robustness. 
Extensive experiments demonstrate that our CAT method significantly reduces the effectiveness of protective perturbations in customization, urging the community to reconsider and improve the robustness of existing protective perturbations. 
The code is available at \url{https://github.com/senp98/CAT}.

## Metadata
- venue: ICML
- year: 2025
- authors: Sen Peng, Mingyue Wang, Jianfei He, Jijia Yang, Xiaohua Jia
- arxiv_id: 
- openreview_id: 5of0l7eUau
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b529e78039c362fde986fce103969e6379b8ab2a.pdf
- published: 2025
- keywords: Latent Diffusion Models, Protective Perturbations, Adversarial Training

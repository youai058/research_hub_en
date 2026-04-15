---
title: "Perturb a Model, Not an Image: Towards Robust Privacy Protection via Anti-Personalized Diffusion Models"
authors: ["Tae-Young Lee", "Juwon Seo", "Jong Hwan Ko", "Gyeong-Moon Park"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "5XoqKCmkS7"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/af600c6e27691bf86fed8e0f1dca1bb8a444a2f5.pdf"
published: "2025"
categories: []
keywords: ["text-to-image diffusion models", "personalization", "privacy"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:37+09:00"
---

# Perturb a Model, Not an Image: Towards Robust Privacy Protection via Anti-Personalized Diffusion Models

## Abstract
Recent advances in diffusion models have enabled high-quality synthesis of specific subjects, such as identities or objects. This capability, while unlocking new possibilities in content creation, also introduces significant privacy risks, as personalization techniques can be misused by malicious users to generate unauthorized images. Although several studies have attempted to counter this by generating adversarially perturbed samples designed to disrupt personalization, they rely on unrealistic assumptions and become ineffective in the presence of even a few clean images or under simple image transformations. To address these challenges, we shift the protection target from the images to the diffusion model itself to hinder the personalization of specific subjects, through our novel framework called $\textbf{A}$nti-$\textbf{P}$ersonalized $\textbf{D}$iffusion $\textbf{M}$odels ($\textbf{APDM}$). We first provide a theoretical analysis demonstrating that a naive approach of existing loss functions to diffusion models is inherently incapable of ensuring convergence for robust anti-personalization. Motivated by this finding, we introduce Direct Protective Optimization (DPO), a novel loss function that effectively disrupts subject personalization in the target model without compromising generative quality. Moreover, we propose a new dual-path optimization strategy, coined Learning to Protect (L2P). By alternating between personalization and protection paths, L2P simulates future personalization trajectories and adaptively reinforces protection at each step.
Experimental results demonstrate that our framework outperforms existing methods, achieving state-of-the-art performance in preventing unauthorized personalization.
The code is available at https://github.com/KU-VGI/APDM.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Tae-Young Lee, Juwon Seo, Jong Hwan Ko, Gyeong-Moon Park
- arxiv_id: 
- openreview_id: 5XoqKCmkS7
- anthology_id: 
- pdf_url: https://openreview.net/pdf/af600c6e27691bf86fed8e0f1dca1bb8a444a2f5.pdf
- published: 2025
- keywords: text-to-image diffusion models, personalization, privacy

---
title: "FastDiSS: Few-step Match Many-step Diffusion Language Model on Sequence-to-Sequence Generation--Full Version"
authors: ["Dat Nguyen-Cong", "Tung Kieu", "Hoang Thanh-Tung"]
venue: "ACL"
year: 2026
venue_class: "whitelist"
arxiv_id: "2604.05551"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2604.05551v1"
published: "2026-04-07"
categories: ["cs.CL", "cs.AI", "cs.LG"]
keywords: []
venue_source: "arxiv-comment"
hunter_fetched: "2026-04-15T05:13:54+09:00"
---

# FastDiSS: Few-step Match Many-step Diffusion Language Model on Sequence-to-Sequence Generation--Full Version

## Abstract
Self-conditioning has been central to the success of continuous diffusion language models, as it allows models to correct previous errors. Yet its ability degrades precisely in the regime where diffusion is most attractive for deployment: few-step sampling for fast inference. In this study, we show that when models only have a few denoising steps, inaccurate self-conditioning induces a substantial approximation gap; this mistake compounds across denoising steps and ultimately dominate the sample quality. To address this, we propose a novel training framework that handles these errors during learning by perturbing the self-conditioning signal to match inference noise, improving robustness to prior estimation errors. In addition, we introduce a token-level noise-awareness mechanism that prevents training from saturation, hence improving optimization. Extensive experiments across conditional generation benchmarks demonstrate that our framework surpasses standard continuous diffusion models while providing up to 400x faster inference speed, and remains competitive against other one-step diffusion frameworks.

## Metadata
- venue: ACL
- year: 2026
- authors: Dat Nguyen-Cong, Tung Kieu, Hoang Thanh-Tung
- arxiv_id: 2604.05551
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2604.05551v1
- published: 2026-04-07

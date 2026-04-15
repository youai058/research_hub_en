---
title: "MDiff4STR: Mask Diffusion Model for Scene Text Recognition"
authors: ["Yongkun Du", "Miaomiao Zhao", "Songlin Fan", "Zhineng Chen", "Caiyan Jia", "Yu-Gang Jiang"]
venue: "AAAI"
year: 2026
venue_class: "whitelist"
arxiv_id: "2512.01422"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2512.01422v1"
published: "2025-12-01"
categories: ["cs.CV"]
keywords: []
venue_source: "arxiv-comment"
hunter_fetched: "2026-04-15T05:17:19+09:00"
---

# MDiff4STR: Mask Diffusion Model for Scene Text Recognition

## Abstract
Mask Diffusion Models (MDMs) have recently emerged as a promising alternative to auto-regressive models (ARMs) for vision-language tasks, owing to their flexible balance of efficiency and accuracy. In this paper, for the first time, we introduce MDMs into the Scene Text Recognition (STR) task. We show that vanilla MDM lags behind ARMs in terms of accuracy, although it improves recognition efficiency. To bridge this gap, we propose MDiff4STR, a Mask Diffusion model enhanced with two key improvement strategies tailored for STR. Specifically, we identify two key challenges in applying MDMs to STR: noising gap between training and inference, and overconfident predictions during inference. Both significantly hinder the performance of MDMs. To mitigate the first issue, we develop six noising strategies that better align training with inference behavior. For the second, we propose a token-replacement noise mechanism that provides a non-mask noise type, encouraging the model to reconsider and revise overly confident but incorrect predictions. We conduct extensive evaluations of MDiff4STR on both standard and challenging STR benchmarks, covering diverse scenarios including irregular, artistic, occluded, and Chinese text, as well as whether the use of pretraining. Across these settings, MDiff4STR consistently outperforms popular STR models, surpassing state-of-the-art ARMs in accuracy, while maintaining fast inference with only three denoising steps. Code: https://github.com/Topdu/OpenOCR.

## Metadata
- venue: AAAI
- year: 2026
- authors: Yongkun Du, Miaomiao Zhao, Songlin Fan, Zhineng Chen, Caiyan Jia, Yu-Gang Jiang
- arxiv_id: 2512.01422
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2512.01422v1
- published: 2025-12-01

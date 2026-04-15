---
title: "Training Diffusion Models with Reinforcement Learning"
authors: ["Kevin Black", "Michael Janner", "Yilun Du", "Ilya Kostrikov", "Sergey Levine"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "YCWjhGrJFD"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/39611b93653580f659f3d4d491f00250c4874376.pdf"
published: "2024"
categories: []
keywords: ["reinforcement learning", "RLHF", "diffusion models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:15+09:00"
---

# Training Diffusion Models with Reinforcement Learning

## Abstract
Diffusion models are a class of flexible generative models trained with an approximation to the log-likelihood objective. However, most use cases of diffusion models are not concerned with likelihoods, but instead with downstream objectives such as human-perceived image quality or drug effectiveness. In this paper, we investigate reinforcement learning methods for directly optimizing diffusion models for such objectives. We describe how posing denoising as a multi-step decision-making problem enables a class of policy gradient algorithms, which we refer to as denoising diffusion policy optimization ( DDPO), that are more effective than alternative reward-weighted likelihood approaches. Empirically, DDPO can adapt text-to-image diffusion models to objectives that are difficult to express via prompting, such as image compressibility, and those derived from human feedback, such as aesthetic quality. Finally, we show that DDPO can improve prompt-image alignment using feedback from a vision-language model without the need for additional data collection or human annotation. The project’s website can be found at http://rl-diffusion.github.io.

## Metadata
- venue: ICLR
- year: 2024
- authors: Kevin Black, Michael Janner, Yilun Du, Ilya Kostrikov, Sergey Levine
- arxiv_id: 
- openreview_id: YCWjhGrJFD
- anthology_id: 
- pdf_url: https://openreview.net/pdf/39611b93653580f659f3d4d491f00250c4874376.pdf
- published: 2024
- keywords: reinforcement learning, RLHF, diffusion models

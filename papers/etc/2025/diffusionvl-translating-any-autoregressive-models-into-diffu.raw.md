---
title: "DiffusionVL: Translating Any Autoregressive Models into Diffusion Vision Language Models"
authors: ["Lunbin Zeng", "Jingfeng Yao", "Bencheng Liao", "Hongyuan Tao", "Wenyu Liu", "Xinggang Wang"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2512.15713"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2512.15713v3"
published: "2025-12-17"
categories: ["cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:03+09:00"
---

# DiffusionVL: Translating Any Autoregressive Models into Diffusion Vision Language Models

## Abstract
Diffusion-based decoding has recently emerged as an appealing alternative to autoregressive (AR) generation, offering the potential to update multiple tokens in parallel and reduce latency. However, diffusion vision language models (dVLMs) still lag significantly behind mainstream autoregressive vision language models. This is due to the scarcity and weaker performance of base diffusion language models (dLLMs) compared with their autoregressive counterparts. This raises a natural question: Can we build high-performing dVLMs directly from existing powerful AR models, without relying on dLLMs? We propose DiffusionVL, a family of dVLMs obtained by translating pretrained AR models into the diffusion paradigm via an efficient diffusion finetuning procedure that changes the training objective and decoding process while keeping the backbone architecture intact. Through an efficient diffusion finetuning strategy, we successfully adapt AR pretrained models into the diffusion paradigm. This approach yields two key observations: (1) The paradigm shift from AR-based multimodal models to diffusion is remarkably effective. (2) Direct conversion of an AR language model to a dVLM is also feasible, achieving performance comparable to that of the same AR model finetuned with standard autoregressive visual instruction tuning. To enable practical open-ended generation, we further integrate block decoding, which supports arbitrary-length outputs and KV-cache reuse for faster inference. Our experiments demonstrate that despite training with less than 5% of the data required by prior methods, DiffusionVL achieves a comprehensive performance improvement, with a 34.4% gain on the MMMU-Pro (vision) benchmark and 37.5% gain on the MME (Cog.) benchmark, alongside a 2x inference speedup. The model and code are released at https://github.com/hustvl/DiffusionVL.

## Metadata
- venue: arXiv
- year: 2025
- authors: Lunbin Zeng, Jingfeng Yao, Bencheng Liao, Hongyuan Tao, Wenyu Liu, Xinggang Wang
- arxiv_id: 2512.15713
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2512.15713v3
- published: 2025-12-17

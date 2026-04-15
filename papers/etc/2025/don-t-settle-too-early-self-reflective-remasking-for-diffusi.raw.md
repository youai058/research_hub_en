---
title: "Don't Settle Too Early: Self-Reflective Remasking for Diffusion Language Models"
authors: ["Zemin Huang", "Yuhang Wang", "Zhiyang Chen", "Guo-Jun Qi"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2509.23653"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2509.23653v1"
published: "2025-09-28"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:14+09:00"
---

# Don't Settle Too Early: Self-Reflective Remasking for Diffusion Language Models

## Abstract
Mask-based Diffusion Language Models (DLMs) struggle to revise incorrect tokens: once a token is generated, it typically remains fixed. The key challenge is to identify potential errors in the inputs. In this paper, we propose \emph{\underline{Rem}asking-\underline{e}nabled \underline{Di}ffusion Language Model (RemeDi}, a mask-based DLM that introduces \emph{remasking} as another fundamental mechanism, enabling more flexible text refinement in diffusion-based text generation. To achieve this, RemeDi jointly predicts token distributions and per-token confidence scores at each step. The confidence scores determine which tokens to be unmasked after the current step, allowing the model to identify tokens with low quality and remask them. These remasked tokens can be resampled with richer context in subsequent steps. We design a remask-aware pipeline to train this ability, including supervised fine-tuning which teaches the model to detect and remask incorrect tokens in addition to predict mask tokens, and reinforcement learning which optimizes full generation trajectories toward higher rewards. Experiments show that RemeDi achieves the state-of-the-art results among open-source DLMs on multiple datasets.

## Metadata
- venue: arXiv
- year: 2025
- authors: Zemin Huang, Yuhang Wang, Zhiyang Chen, Guo-Jun Qi
- arxiv_id: 2509.23653
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2509.23653v1
- published: 2025-09-28

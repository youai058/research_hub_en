---
title: "Diffusion-State Policy Optimization for Masked Diffusion Language Models"
authors: ["Daisuke Oba", "Hiroki Furuta", "Naoaki Okazaki"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.06462"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.06462v2"
published: "2026-02-06"
categories: ["cs.CL", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:05+09:00"
---

# Diffusion-State Policy Optimization for Masked Diffusion Language Models

## Abstract
Masked diffusion language models generate by iteratively filling masked tokens over multiple denoising steps, so learning only from a terminal reward on the final completion yields coarse credit assignment over intermediate decisions. We propose DiSPO (Diffusion-State Policy Optimization), a plug-in credit-assignment layer that directly optimizes intermediate filling decisions. At selected intermediate masked states, DiSPO branches by resampling fillings for the currently masked positions from rollout-cached logits, scores the resulting completions, and updates only the newly filled tokens -- without additional multi-step diffusion rollouts. We formalize a fixed-state objective for branched completions and derive a policy-gradient estimator that can be combined with terminal-feedback policy optimization using the same rollouts. On LLaDA-8B-Instruct, DiSPO consistently improves over the terminal-feedback diffu-GRPO baseline on math and planning benchmarks under matched rollout compute and optimizer steps. Our code will be available at https://daioba.github.io/dispo .

## Metadata
- venue: arXiv
- year: 2026
- authors: Daisuke Oba, Hiroki Furuta, Naoaki Okazaki
- arxiv_id: 2602.06462
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.06462v2
- published: 2026-02-06

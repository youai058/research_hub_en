---
title: "Self-Purification Mitigates Backdoors in Multimodal Diffusion Language Models"
authors: ["Guangnian Wan", "Qi Li", "Gongfan Fang", "Xinyin Ma", "Xinchao Wang"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.22246"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.22246v1"
published: "2026-02-24"
categories: ["cs.CR", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:02+09:00"
---

# Self-Purification Mitigates Backdoors in Multimodal Diffusion Language Models

## Abstract
Multimodal Diffusion Language Models (MDLMs) have recently emerged as a competitive alternative to their autoregressive counterparts. Yet their vulnerability to backdoor attacks remains largely unexplored. In this work, we show that well-established data-poisoning pipelines can successfully implant backdoors into MDLMs, enabling attackers to manipulate model behavior via specific triggers while maintaining normal performance on clean inputs. However, defense strategies effective to these models are yet to emerge. To bridge this gap, we introduce a backdoor defense framework for MDLMs named DiSP (Diffusion Self-Purification). DiSP is driven by a key observation: selectively masking certain vision tokens at inference time can neutralize a backdoored model's trigger-induced behaviors and restore normal functionality. Building on this, we purify the poisoned dataset using the compromised model itself, then fine-tune the model on the purified data to recover it to a clean one. Given such a specific design, DiSP can remove backdoors without requiring any auxiliary models or clean reference data. Extensive experiments demonstrate that our approach effectively mitigates backdoor effects, reducing the attack success rate (ASR) from over 90% to typically under 5%, while maintaining model performance on benign tasks.

## Metadata
- venue: arXiv
- year: 2026
- authors: Guangnian Wan, Qi Li, Gongfan Fang, Xinyin Ma, Xinchao Wang
- arxiv_id: 2602.22246
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.22246v1
- published: 2026-02-24

---
title: "Improving LLM Safety Alignment with Dual-Objective Optimization"
authors: ["Xuandong Zhao", "Will Cai", "Tianneng Shi", "David Huang", "Licong Lin", "Song Mei", "Dawn Song"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Kjivk5OPtL"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/665b2e7317372910957a65d33566d3686cea0f9a.pdf"
published: "2025"
categories: []
keywords: ["LLM Safety", "Alignment", "DPO"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:35+09:00"
---

# Improving LLM Safety Alignment with Dual-Objective Optimization

## Abstract
Existing training-time safety alignment techniques for large language models (LLMs) remain vulnerable to jailbreak attacks. Direct preference optimization (DPO), a widely deployed alignment method, exhibits limitations in both experimental and theoretical contexts as its loss function proves suboptimal for refusal learning. Through gradient-based analysis, we identify these shortcomings and propose an improved safety alignment that disentangles DPO objectives into two components: (1) robust refusal training, which encourages refusal even when partial unsafe generations are produced, and (2) targeted unlearning of harmful knowledge. This approach significantly increases LLM robustness against a wide range of jailbreak attacks, including prefilling, suffix, and multi-turn attacks across both in-distribution and out-of-distribution scenarios. Furthermore, we introduce a method to emphasize critical refusal tokens by incorporating a reward-based token-level weighting mechanism for refusal learning, which further improves the robustness against adversarial exploits. Our research also suggests that robustness to jailbreak attacks is correlated with token distribution shifts in the training process and internal representations of refusal and harmful tokens, offering valuable directions for future research in LLM safety alignment. The code is available at https://github.com/wicai24/DOOR-Alignment.

## Metadata
- venue: ICML
- year: 2025
- authors: Xuandong Zhao, Will Cai, Tianneng Shi, David Huang, Licong Lin, Song Mei, Dawn Song
- arxiv_id: 
- openreview_id: Kjivk5OPtL
- anthology_id: 
- pdf_url: https://openreview.net/pdf/665b2e7317372910957a65d33566d3686cea0f9a.pdf
- published: 2025
- keywords: LLM Safety, Alignment, DPO

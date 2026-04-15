---
title: "Reinforcement Learning Fine-Tuning Enhances Activation Intensity and Diversity in the Internal Circuitry of LLMs"
authors: ["Honglin Zhang", "Qianyue Hao", "Fengli Xu", "Yong Li"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "tzS9roOTdj"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0ce95dcadce19f02453ae79e8b9a8220e4700dcb.pdf"
published: "2026"
categories: []
keywords: ["Large Language Models; Reinforcement Learning Fine-Tuning; Edge Attribution Patching"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:23+09:00"
---

# Reinforcement Learning Fine-Tuning Enhances Activation Intensity and Diversity in the Internal Circuitry of LLMs

## Abstract
Large language models (LLMs) acquire extensive prior knowledge through large-scale pretraining and can be further enhanced via supervised fine-tuning (SFT) or reinforcement learning (RL)-based post-training.
A growing body of evidence has shown that RL fine-tuning improves the capability of LLMs beyond what SFT alone achieves.
However, the underlying mechanisms why RL fine-tuning is able to enhance the capability of various LLMs with distinct intrinsic characteristics remain underexplored.
In this study, we draw inspiration from prior work on edge attribution patching (EAP) to investigate the internal differences of LLMs before and after RL fine-tuning.
Our analysis across multiple model families and mathematical datasets shows two robust effects of online RL post-training: (i) an overall increase in average activation intensity, indicating that more internal pathways are engaged and their signals become stronger, and (ii) greater diversity in activation patterns, reflected by higher entropy and less concentrated edge distributions. These changes suggest that RL reshapes information flow to be both more redundant and more flexible, which may explain its advantage in mathematical generalization. Notably, models fine-tuned with Direct Preference Optimization (DPO) deviate from these trends, exhibiting substantially weaker or inconsistent internal changes compared to PPO- and GRPO-based training. Together, our findings provide a unified view of how RL fine-tuning systematically alters the internal circuitry of LLMs and highlight the methodological distinctions between online RL and preference-based approaches.
Our code is open source at https://github.com/tsinghua-fib-lab/llm_rl_probing_analysis.

## Metadata
- venue: ICLR
- year: 2026
- authors: Honglin Zhang, Qianyue Hao, Fengli Xu, Yong Li
- arxiv_id: 
- openreview_id: tzS9roOTdj
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0ce95dcadce19f02453ae79e8b9a8220e4700dcb.pdf
- published: 2026
- keywords: Large Language Models; Reinforcement Learning Fine-Tuning; Edge Attribution Patching

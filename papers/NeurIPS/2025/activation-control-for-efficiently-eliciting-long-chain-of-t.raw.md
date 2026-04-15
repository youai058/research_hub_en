---
title: "Activation Control for Efficiently Eliciting Long Chain-of-thought Ability of Language Models"
authors: ["Zekai Zhao", "Qi Liu", "Kun Zhou", "Zihan Liu", "Yifei Shao", "Zhiting Hu", "Biwei Huang"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "XNo4yS9n1k"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2b62626f959a636707dfb61efe094e4dcd7bd32f.pdf"
published: "2025"
categories: []
keywords: ["Large Language Models", "Long Chain of Thoughts"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:39+09:00"
---

# Activation Control for Efficiently Eliciting Long Chain-of-thought Ability of Language Models

## Abstract
Despite the remarkable reasoning performance, eliciting the long chain-of-thought(CoT) ability in large language models(LLMs) typically requires costly reinforcement learning or supervised fine-tuning on high-quality distilled data. We investigate the internal mechanisms behind this capability and show that a small set of high-impact activations in the last few layers, greatly govern the long-form reasoning attributes, e.g. output length and self-reflection. Through simply amplifying these activations and adding ``wait'' tokens, the long CoT ability can be invoked without training, leading to significantly increased self-reflection rate and accuracy. In addition, we also find that the activation changes follow predictable trajectories, i.e. a sharp rise after special tokens and a subsequent exponential decay. Based on these insights, we introduce a general training-free activation control technique. It utilizes a few contrastive examples to identify the relevant activations, and then incorporates simple analytic functions to adjust their values at inference time to elicit long CoTs. Extensive experiments have verified the effectiveness of our methods in efficiently eliciting the long CoT ability of LLMs and improving the performance. Besides, we further propose a parameter-efficient fine-tuning method that trains only the last-layer activation amplification module and a few LoRA layers, outperforming LoRA on reasoning benchmarks with much fewer parameters. Our code and data will be fully public released.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Zekai Zhao, Qi Liu, Kun Zhou, Zihan Liu, Yifei Shao, Zhiting Hu, Biwei Huang
- arxiv_id: 
- openreview_id: XNo4yS9n1k
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2b62626f959a636707dfb61efe094e4dcd7bd32f.pdf
- published: 2025
- keywords: Large Language Models, Long Chain of Thoughts

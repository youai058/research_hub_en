---
title: "ContextIF: Enhancing Instruction-Following through Context Reward"
authors: ["Yule Zhong", "Jiacheng Yao", "Guoxiu He"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "IuscGSmfEf"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/238b9fec6aef551b0e4157ee68856d14f663cf9c.pdf"
published: "2026"
categories: []
keywords: ["Large Language Models", "Instruction-Following", "Reinforcement Learning", "In-Context Learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:31+09:00"
---

# ContextIF: Enhancing Instruction-Following through Context Reward

## Abstract
While supervised fine-tuning (SFT) and preference learning (PL) are widely used to enhance the instruction-following ability of Large Language Models (LLMs), they often struggle to generalize to novel or complex instructions and may compromise the models' general capabilities. In-Context Learning (ICL) emerges as a promising alternative due to its strong generalization without modifying the model's parameters, but its effectiveness is constrained by the reliance on high-quality, manually curated demonstration pools. To overcome this limitation, we propose ContextIF, a reinforcement learning (RL) framework for automatic context generation. Guided by comprehensive context reward, ContextIF is optimized by Group Relative Policy Optimization (GRPO). It aims to generate precise constraint summaries and optimal context demonstrations tailored to given instructions, thereby improving the instruction-following performance of target LLMs. We evaluate ContextIF on multiple representative instruction-following benchmarks using popular open-source LLMs. Experimental results demonstrate that ContextIF achieves substantial performance gains over existing SFT and ICL methods, while also generalizing effectively to unseen constraint conditions. Moreover, ContextIF preserves the parameters and general capabilities of the target models, offering strong adaptability and scalability. Our code is available at https://github.com/ECNU-Text-Computing/ContextIF.

## Metadata
- venue: ICLR
- year: 2026
- authors: Yule Zhong, Jiacheng Yao, Guoxiu He
- arxiv_id: 
- openreview_id: IuscGSmfEf
- anthology_id: 
- pdf_url: https://openreview.net/pdf/238b9fec6aef551b0e4157ee68856d14f663cf9c.pdf
- published: 2026
- keywords: Large Language Models, Instruction-Following, Reinforcement Learning, In-Context Learning

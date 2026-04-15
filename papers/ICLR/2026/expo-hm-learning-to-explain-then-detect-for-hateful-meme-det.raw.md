---
title: "ExPO-HM: Learning to Explain-then-Detect for Hateful Meme Detection"
authors: ["Jingbiao Mei", "Mingsheng Sun", "Jinghong Chen", "Pengda Qin", "Yuhong Li", "Da Chen", "Bill Byrne"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "bEejbORUI5"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/76fc218119052f27cfd6e05126eccc4ca7a2cc73.pdf"
published: "2026"
categories: []
keywords: ["Hateful Meme Detection"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:21+09:00"
---

# ExPO-HM: Learning to Explain-then-Detect for Hateful Meme Detection

## Abstract
Hateful memes have emerged as a particularly challenging form of online abuse, motivating the development of automated detection systems. Most prior approaches rely on direct detection, producing only binary predictions. Such models fail to provide the context and explanations that real-world moderation requires. Recent Explain-then-Detect approaches, using Chain-of-Thought prompting or LMM agents, perform worse than simple SFT baselines, and even advanced post-training methods such as GRPO fail to close the gap. Our analysis identifies two key issues of such systems: important policy-relevant cues such as targets and attack types are not hypothesized by the model as a likely explanation; and the binary reward signal is insufficient to guide reasoning. To address these challenges, we propose ExPO-HM (Explain-then-Detect Policy Optimization for Hateful Memes), inspired by the training and evaluation process of human annotators. ExPO-HM combines SFT warmup, GRPO with curriculum learning, and Conditional Decision Entropy (CDE) as both metric and reward for reasoning quality. Across three hateful meme benchmarks, ExPO-HM achieves state-of-the-art performance on binary detection, fine-grained classification, and reasoning quality, with up to 15\% and 17\% F1 improvement over the GRPO and DPO baselines, respectively. By moving hateful meme detection from simple binary alarms to explanation-driven detection, ExPO-HM provides accurate, interpretable, and actionable moderation support. Code available at: https://github.com/JingbiaoMei/ExPO-HM

## Metadata
- venue: ICLR
- year: 2026
- authors: Jingbiao Mei, Mingsheng Sun, Jinghong Chen, Pengda Qin, Yuhong Li, Da Chen, Bill Byrne
- arxiv_id: 
- openreview_id: bEejbORUI5
- anthology_id: 
- pdf_url: https://openreview.net/pdf/76fc218119052f27cfd6e05126eccc4ca7a2cc73.pdf
- published: 2026
- keywords: Hateful Meme Detection

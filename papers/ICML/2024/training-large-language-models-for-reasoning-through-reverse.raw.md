---
title: "Training Large Language Models for Reasoning through Reverse Curriculum Reinforcement Learning"
authors: ["Zhiheng Xi", "Wenxiang Chen", "Boyang Hong", "Senjie Jin", "Rui Zheng", "Wei He", "Yiwen Ding", "Shichun Liu", "Xin Guo", "Junzhe Wang", "Honglin Guo", "Wei Shen", "Xiaoran Fan", "Yuhao Zhou", "Shihan Dou", "Xiao Wang", "Xinbo Zhang", "peng sun", "Tao Gui", "Qi Zhang", "Xuanjing Huang"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "t82Y3fmRtk"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/443b716a0c0c69bb4c7a02300bafbe1372c2d3ff.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:40+09:00"
---

# Training Large Language Models for Reasoning through Reverse Curriculum Reinforcement Learning

## Abstract
In this paper, we propose **R**$^3$: Learning **R**easoning through **R**everse Curriculum **R**einforcement Learning (RL), a novel method that employs only outcome supervision to achieve the benefits of process supervision for large language models. The core challenge in applying RL to complex reasoning is to identify a sequence of actions that result in positive rewards and provide appropriate supervision for optimization. Outcome supervision provides sparse rewards for final results without identifying error locations, whereas process supervision offers step-wise rewards but requires extensive manual annotation. **R**$^3$ overcomes these limitations by learning from correct demonstrations. Specifically, **R**$^3$ progressively slides the start state of reasoning from a demonstration's end to its beginning, facilitating easier model exploration at all stages. Thus, **R**$^3$ establishes a step-wise curriculum, allowing outcome supervision to offer step-level signals and precisely pinpoint errors. Using Llama2-7B, our method surpasses RL baseline on eight reasoning tasks by $4.1$ points on average. Notably, in program-based reasoning, 7B-scale models perform comparably to larger models or closed-source models with our **R**$^3$.

## Metadata
- venue: ICML
- year: 2024
- authors: Zhiheng Xi, Wenxiang Chen, Boyang Hong, Senjie Jin, Rui Zheng, Wei He, Yiwen Ding, Shichun Liu, Xin Guo, Junzhe Wang, Honglin Guo, Wei Shen, Xiaoran Fan, Yuhao Zhou, Shihan Dou, Xiao Wang, Xinbo Zhang, peng sun, Tao Gui, Qi Zhang, Xuanjing Huang
- arxiv_id: 
- openreview_id: t82Y3fmRtk
- anthology_id: 
- pdf_url: https://openreview.net/pdf/443b716a0c0c69bb4c7a02300bafbe1372c2d3ff.pdf
- published: 2024

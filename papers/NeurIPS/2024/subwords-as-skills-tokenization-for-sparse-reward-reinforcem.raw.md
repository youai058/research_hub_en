---
title: "Subwords as Skills: Tokenization for Sparse-Reward Reinforcement Learning"
authors: ["David Yunis", "Justin Jung", "Falcon Z Dai", "Matthew Walter"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "WfpvtH7oC1"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/29ca9fc7ad35281aef86bce7e34646cb55a83344.pdf"
published: "2024"
categories: []
keywords: ["Reinforcement Learning", "Deep Learning", "Exploration", "Hierarchical RL"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:05+09:00"
---

# Subwords as Skills: Tokenization for Sparse-Reward Reinforcement Learning

## Abstract
Exploration in sparse-reward reinforcement learning (RL) is difficult due to the need for long, coordinated sequences of actions in order to achieve any reward. Skill learning, from demonstrations or interaction, is a promising approach to address this, but skill extraction and inference are expensive for current methods. We present a novel method to extract skills from demonstrations for use in sparse-reward RL, inspired by the popular Byte-Pair Encoding (BPE) algorithm in natural language processing. With these skills, we show strong performance in a variety of tasks, 1000$\times$ acceleration for skill-extraction and 100$\times$ acceleration for policy inference. Given the simplicity of our method, skills extracted from 1\% of the demonstrations in one task can be transferred to a new loosely related task. We also note that such a method yields a finite set of interpretable behaviors. Our code is available at https://github.com/dyunis/subwords_as_skills.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: David Yunis, Justin Jung, Falcon Z Dai, Matthew Walter
- arxiv_id: 
- openreview_id: WfpvtH7oC1
- anthology_id: 
- pdf_url: https://openreview.net/pdf/29ca9fc7ad35281aef86bce7e34646cb55a83344.pdf
- published: 2024
- keywords: Reinforcement Learning, Deep Learning, Exploration, Hierarchical RL

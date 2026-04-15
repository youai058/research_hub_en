---
title: "GRAM: A Generative Foundation Reward Model for Reward Generalization"
authors: ["Chenglong Wang", "Yang Gan", "Yifu Huo", "Yongyu Mu", "Qiaozhi He", "MuRun Yang", "Bei Li", "Tong Xiao", "Chunliang Zhang", "Tongran Liu", "JingBo Zhu"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "rxKC8v2uHc"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ac25e3ac67051bec4c9bc17f03b190e458a4a373.pdf"
published: "2025"
categories: []
keywords: ["Large Language Model", "Reward Modeling", "RLHF"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:20+09:00"
---

# GRAM: A Generative Foundation Reward Model for Reward Generalization

## Abstract
In aligning large language models (LLMs), reward models have played an important role, but are standardly trained as discriminative models and rely only on labeled human preference data.  In this paper, we explore methods that train reward models using both unlabeled and labeled data.  Building on the generative models in LLMs, we develop a generative reward model that is first trained via large-scale unsupervised learning and then fine-tuned via supervised learning.  We also show that by using label smoothing, we are in fact optimizing a regularized pairwise ranking loss.  This result, in turn, provides a new view of training reward models, which links generative models and discriminative models under the same class of training objectives.  The outcome of these techniques is a foundation reward model, which can be applied to a wide range of tasks with little or no further fine-tuning effort.  Extensive experiments show that this model generalizes well across several tasks, including response ranking, reinforcement learning from human feedback, and task adaptation with fine-tuning, achieving significant performance improvements over several strong baseline models.

## Metadata
- venue: ICML
- year: 2025
- authors: Chenglong Wang, Yang Gan, Yifu Huo, Yongyu Mu, Qiaozhi He, MuRun Yang, Bei Li, Tong Xiao, Chunliang Zhang, Tongran Liu, JingBo Zhu
- arxiv_id: 
- openreview_id: rxKC8v2uHc
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ac25e3ac67051bec4c9bc17f03b190e458a4a373.pdf
- published: 2025
- keywords: Large Language Model, Reward Modeling, RLHF

---
title: "A Multi-Power Law for Loss Curve Prediction Across Learning Rate Schedules"
authors: ["Kairong Luo", "Haodong Wen", "Shengding Hu", "Zhenbo Sun", "Zhiyuan Liu", "Maosong Sun", "Kaifeng Lyu", "Wenguang Chen"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "KnoS9XxIlK"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/212cefb36307e11021cced0a49c98a00931e6431.pdf"
published: "2025"
categories: []
keywords: ["Large language model", "Learning rate scheduler", "Scaling Law", "Hyperparameter optimization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:53+09:00"
---

# A Multi-Power Law for Loss Curve Prediction Across Learning Rate Schedules

## Abstract
Training large models is both resource-intensive and time-consuming, making it crucial to understand the quantitative relationship between model performance and hyperparameters. In this paper, we derive an empirical law that predicts pretraining loss for large language models for every intermediate training step across various learning rate schedules, including constant, cosine, and step decay schedules. Our proposed law takes a multi-power form, combining a power law based on the sum of learning rates and additional power laws to account for a loss reduction effect as learning rate decays. We validate this law extensively on Llama-2 models of varying sizes and demonstrate that, after fitting on a few learning rate schedules, it accurately predicts the loss curves for unseen schedules of different shapes and horizons. Moreover, by minimizing the predicted final pretraining loss across learning rate schedules, we are able to find a schedule that outperforms the widely-used cosine learning rate schedule. Interestingly, this automatically discovered schedule bears some resemblance to the recently proposed Warmup-Stable-Decay (WSD) schedule (Hu et al, 2024) but achieves a slightly lower final loss. We believe these results could offer valuable insights for understanding the dynamics of pretraining and for designing learning rate schedules to improve efficiency.

## Metadata
- venue: ICLR
- year: 2025
- authors: Kairong Luo, Haodong Wen, Shengding Hu, Zhenbo Sun, Zhiyuan Liu, Maosong Sun, Kaifeng Lyu, Wenguang Chen
- arxiv_id: 
- openreview_id: KnoS9XxIlK
- anthology_id: 
- pdf_url: https://openreview.net/pdf/212cefb36307e11021cced0a49c98a00931e6431.pdf
- published: 2025
- keywords: Large language model, Learning rate scheduler, Scaling Law, Hyperparameter optimization

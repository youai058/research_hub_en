---
title: "Unveiling the Secret Recipe: A Guide For Supervised Fine-Tuning Small LLMs"
authors: ["Aldo Pareja", "Nikhil Shivakumar Nayak", "Hao Wang", "Krishnateja Killamsetty", "Shivchander Sudalairaj", "Wenlong Zhao", "Seungwook Han", "Abhishek Bhandwaldar", "Guangxuan Xu", "Kai Xu", "Ligong Han", "Luke Inglis", "Akash Srivastava"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "eENHKMTOfW"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6062bafab9f3bb337fdcbbc211b6fec41a70900a.pdf"
published: "2025"
categories: []
keywords: ["Machine Learning", "Generative Models", "Large Language Models", "Natural Language Processing", "Transformers", "Fine-Tuning", "Instruction Tuning", "Synthetic Data Generation", "Knowledge Data", "Skills Data", "Model Generalization", "Batch Size", "Hyperparameter Optimization", "Gradient Norm", "MMLU", "MTBench", "Stacked Training", "Phased Training", "Compute Efficiency", "Sample Efficiency", "Flash Attention", "Multipack Bucketing"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:10+09:00"
---

# Unveiling the Secret Recipe: A Guide For Supervised Fine-Tuning Small LLMs

## Abstract
The rise of large language models (LLMs) has created a significant disparity: industrial research labs with their computational resources, expert teams, and advanced infrastructures, can effectively fine-tune LLMs, while individual developers and small organizations face barriers due to limited resources to effectively explore the experiment space. In this paper, we aim to bridge this gap by presenting a comprehensive study on supervised fine-tuning of LLMs using instruction-tuning datasets spanning diverse knowledge domains and skills. We focus on small-sized LLMs (3B to 7B parameters) for their cost-efficiency and accessibility. We explore various training configurations and strategies across four open-source pre-trained models. We provide detailed documentation of these configurations, revealing findings that challenge several common training practices, including hyperparameter recommendations from TULU and phased training recommended by Orca. The code used for the experiments can be found here: https://github.com/instructlab/training.

Key insights from our work include: (i) larger batch sizes paired with lower learning rates lead to improved model performance on benchmarks such as MMLU, MTBench, and Open LLM Leaderboard; (ii) early-stage training dynamics, such as lower gradient norms and higher loss values, are strong indicators of better final model performance, allowing for early termination of sub-optimal runs and significant computational savings; (iii) through a thorough exploration of hyperparameters like warmup steps and learning rate schedules, we provide guidance for practitioners and find that certain simplifications do not compromise performance; and (iv) we observe no significant difference in performance between phased (sequentially training on data divided into phases) and stacked (training on the entire dataset at once) strategies, but stacked training is simpler and more sample efficient. With these findings holding robustly across datasets as well as model families and sizes, we hope this study serves as a guide for practitioners fine-tuning small LLMs and promotes a more inclusive research environment for LLM development.

## Metadata
- venue: ICLR
- year: 2025
- authors: Aldo Pareja, Nikhil Shivakumar Nayak, Hao Wang, Krishnateja Killamsetty, Shivchander Sudalairaj, Wenlong Zhao, Seungwook Han, Abhishek Bhandwaldar, Guangxuan Xu, Kai Xu, Ligong Han, Luke Inglis, Akash Srivastava
- arxiv_id: 
- openreview_id: eENHKMTOfW
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6062bafab9f3bb337fdcbbc211b6fec41a70900a.pdf
- published: 2025
- keywords: Machine Learning, Generative Models, Large Language Models, Natural Language Processing, Transformers, Fine-Tuning, Instruction Tuning, Synthetic Data Generation, Knowledge Data, Skills Data, Model Generalization, Batch Size, Hyperparameter Optimization, Gradient Norm, MMLU, MTBench, Stacked Training, Phased Training, Compute Efficiency, Sample Efficiency, Flash Attention, Multipack Bucketing

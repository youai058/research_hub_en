---
title: "Free Lunch for Pass@$k$? Low Cost Diverse Sampling for Diffusion Language Models"
authors: ["Sean Lamont", "Christian Walder", "Paul Montague", "Amir Dezfouli", "Michael Norrish"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.04893"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.04893v1"
published: "2026-03-05"
categories: ["cs.CL", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:13:58+09:00"
---

# Free Lunch for Pass@$k$? Low Cost Diverse Sampling for Diffusion Language Models

## Abstract
Diverse outputs in text generation are necessary for effective exploration in complex reasoning tasks, such as code generation and mathematical problem solving. Such Pass@$k$ problems benefit from distinct candidates covering the solution space. However, traditional sampling approaches often waste computational resources on repetitive failure modes. While Diffusion Language Models have emerged as a competitive alternative to the prevailing Autoregressive paradigm, they remain susceptible to this redundancy, with independent samples frequently collapsing into similar modes. To address this, we propose a training free, low cost intervention to enhance generative diversity in Diffusion Language Models. Our approach modifies intermediate samples in a batch sequentially, where each sample is repelled from the feature space of previous samples, actively penalising redundancy. Unlike prior methods that require retraining or beam search, our strategy incurs negligible computational overhead, while ensuring that each sample contributes a unique perspective to the batch. We evaluate our method on the HumanEval and GSM8K benchmarks using the LLaDA-8B-Instruct model. Our results demonstrate significantly improved diversity and Pass@$k$ performance across various temperature settings. As a simple modification to the sampling process, our method offers an immediate, low-cost improvement for current and future Diffusion Language Models in tasks that benefit from diverse solution search. We make our code available at https://github.com/sean-lamont/odd.

## Metadata
- venue: arXiv
- year: 2026
- authors: Sean Lamont, Christian Walder, Paul Montague, Amir Dezfouli, Michael Norrish
- arxiv_id: 2603.04893
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.04893v1
- published: 2026-03-05

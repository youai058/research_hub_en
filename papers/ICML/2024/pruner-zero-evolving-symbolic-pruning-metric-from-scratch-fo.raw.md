---
title: "Pruner-Zero: Evolving Symbolic Pruning Metric From Scratch for Large Language Models"
authors: ["Peijie Dong", "Lujun Li", "Zhenheng Tang", "Xiang Liu", "Xinglin Pan", "Qiang Wang", "Xiaowen Chu"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "1tRLxQzdep"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e5e887ca09a259b602b0c84466c6a6925bfa4d0b.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:24+09:00"
---

# Pruner-Zero: Evolving Symbolic Pruning Metric From Scratch for Large Language Models

## Abstract
Despite the remarkable capabilities, Large Language Models (LLMs) face deployment challenges due to their extensive size. Pruning methods drop a subset of weights to accelerate, but many of them require retraining, which is prohibitively expensive and computationally demanding. Recently, post-training pruning approaches introduced novel metrics, enabling the pruning of LLMs without retraining. However, these metrics require the involvement of human experts and tedious trial and error. To efficiently identify superior pruning metrics, we develop an automatic framework for searching symbolic pruning metrics using genetic programming. In particular, we devise an elaborate search space encompassing the existing pruning metrics to discover the potential symbolic pruning metric. We propose an opposing operation simplification strategy to increase the diversity of the population. In this way, Pruner-Zero allows auto-generation of symbolic pruning metrics. Based on the searched results, we explore the correlation between pruning metrics and performance after pruning and summarize some principles. Extensive experiments on LLaMA and LLaMA-2 on language modeling and zero-shot tasks demonstrate that our Pruner-Zero obtains superior performance than SOTA post-training pruning methods. Code at: https://github.com/pprp/Pruner-Zero.

## Metadata
- venue: ICML
- year: 2024
- authors: Peijie Dong, Lujun Li, Zhenheng Tang, Xiang Liu, Xinglin Pan, Qiang Wang, Xiaowen Chu
- arxiv_id: 
- openreview_id: 1tRLxQzdep
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e5e887ca09a259b602b0c84466c6a6925bfa4d0b.pdf
- published: 2024

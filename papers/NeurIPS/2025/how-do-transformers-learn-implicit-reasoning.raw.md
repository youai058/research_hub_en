---
title: "How do Transformers Learn Implicit Reasoning?"
authors: ["Jiaran Ye", "Zijun Yao", "Zhidian Huang", "Liangming Pan", "Jinxin Liu", "Yushi Bai", "Amy Xin", "Liu Weichuan", "Xiaoyin Che", "Lei Hou", "Juanzi Li"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "19ygs48nOa"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ad38d1ecc76e644507fb0bca76d2143a06260e52.pdf"
published: "2025"
categories: []
keywords: ["Implicit Reasoning", "Multi-hop Inference", "Transformer Models", "Interpretability"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:48+09:00"
---

# How do Transformers Learn Implicit Reasoning?

## Abstract
Recent work suggests that large language models (LLMs) can perform multi-hop reasoning implicitly---producing correct answers without explicitly verbalizing intermediate steps---but the underlying mechanisms remain poorly understood.
In this paper, we study how such implicit reasoning emerges by training transformers from scratch in a controlled symbolic environment.
Our analysis reveals a three-stage developmental trajectory: early memorization, followed by in-distribution generalization, and eventually cross-distribution generalization.
We find that training with atomic triples is not necessary but accelerates learning, and that second-hop generalization relies on query-level exposure to specific compositional structures.
To interpret these behaviors, we introduce two diagnostic tools: cross-query semantic patching, which identifies semantically reusable intermediate representations, and a cosine-based representational lens, which reveals that successful reasoning correlates with the cosine-base clustering in hidden space.
This clustering phenomenon in turn provides a coherent explanation for the behavioral dynamics observed across training, linking representational structure to reasoning capability. 
These findings provide new insights into the interpretability of implicit multi-hop reasoning in LLMs, helping to clarify how complex reasoning processes unfold internally and offering pathways to enhance the transparency of such models.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Jiaran Ye, Zijun Yao, Zhidian Huang, Liangming Pan, Jinxin Liu, Yushi Bai, Amy Xin, Liu Weichuan, Xiaoyin Che, Lei Hou, Juanzi Li
- arxiv_id: 
- openreview_id: 19ygs48nOa
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ad38d1ecc76e644507fb0bca76d2143a06260e52.pdf
- published: 2025
- keywords: Implicit Reasoning, Multi-hop Inference, Transformer Models, Interpretability

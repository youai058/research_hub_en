---
title: "BBox-Adapter: Lightweight Adapting for Black-Box Large Language Models"
authors: ["Haotian Sun", "Yuchen Zhuang", "Wei Wei", "Chao Zhang", "Bo Dai"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "jdRIaUu3xY"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9eebbe03f032b9b23ee8b8af464cb9c4ebb9675c.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:30+09:00"
---

# BBox-Adapter: Lightweight Adapting for Black-Box Large Language Models

## Abstract
Adapting state-of-the-art Large Language Models (LLMs) like GPT-4 and Gemini for specific tasks is challenging. Due to the opacity in their parameters, embeddings, and even output probabilities, existing fine-tuning adaptation methods are inapplicable. Consequently, adapting these black-box LLMs is only possible through their API services, raising concerns about transparency, privacy, and cost. To address these challenges, we introduce BBox-Adapter, a novel lightweight adapter for black-box LLMs. BBox-Adapter distinguishes target and source domain data by treating target data as positive and source data as negative. It employs a ranking-based Noise Contrastive Estimation (NCE) loss to promote the likelihood of target domain data while penalizing that of the source domain. Furthermore, it features an online adaptation mechanism, which incorporates real-time positive data sampling from ground-truth, human, or AI feedback, coupled with negative data from previous adaptations. Extensive experiments demonstrate BBox-Adapter's effectiveness and cost efficiency. It improves model performance by up to 6.77% across diverse tasks and domains, while reducing training and inference costs by 31.30x and 1.84x, respectively.

## Metadata
- venue: ICML
- year: 2024
- authors: Haotian Sun, Yuchen Zhuang, Wei Wei, Chao Zhang, Bo Dai
- arxiv_id: 
- openreview_id: jdRIaUu3xY
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9eebbe03f032b9b23ee8b8af464cb9c4ebb9675c.pdf
- published: 2024

---
title: "Context Steering: Controllable Personalization at Inference Time"
authors: ["Jerry Zhi-Yang He", "Sashrika Pandey", "Mariah L Schrum", "Anca Dragan"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "xQCXInDq0m"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a1d5a7a272bc905f6e9570df5ddf725a27cd7ef4.pdf"
published: "2025"
categories: []
keywords: ["personalization", "context", "large language model", "inference", "controllable generation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:04+09:00"
---

# Context Steering: Controllable Personalization at Inference Time

## Abstract
To deliver high-quality, personalized responses, large language models (LLMs) must effectively incorporate context — personal, demographic, and cultural information specific to an end-user. For example, asking the model to explain Newton's second law with the context "I am a toddler'' should produce a response different from when the context is "I am a physics professor''. However, leveraging the context in practice is a nuanced and challenging task, and is often dependent on the specific situation or user base. The model must strike a balance between providing specific, personalized responses and maintaining general applicability. Current solutions, such as prompt-engineering and fine-tuning, require collection of contextually appropriate responses as examples, making them time-consuming and less flexible to use across different contexts. In this work, we introduce Context Steering (CoS) —a simple, training-free decoding approach that amplifies the influence of the context in next token predictions. CoS computes contextual influence by comparing the output probabilities from two LLM forward passes: one that includes the context and one that does not. By linearly scaling the contextual influence, CoS allows practitioners to flexibly control the degree of personalization for different use cases. We show that CoS can be applied to autoregressive LLMs, and demonstrates strong performance in personalized recommendations. Additionally, we show that CoS can function as a Bayesian Generative model to infer and quantify correlations between open-ended texts, broadening its potential applications.

## Metadata
- venue: ICLR
- year: 2025
- authors: Jerry Zhi-Yang He, Sashrika Pandey, Mariah L Schrum, Anca Dragan
- arxiv_id: 
- openreview_id: xQCXInDq0m
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a1d5a7a272bc905f6e9570df5ddf725a27cd7ef4.pdf
- published: 2025
- keywords: personalization, context, large language model, inference, controllable generation

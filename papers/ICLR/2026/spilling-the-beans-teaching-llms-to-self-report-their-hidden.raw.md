---
title: "Spilling the Beans: Teaching LLMs to Self-Report Their Hidden Objectives"
authors: ["Chloe Li", "Mary Phuong", "Daniel Tan"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "sWs0cCuM8I"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0f59d6703432a82dc869e3f3e8a23942692bd8e6.pdf"
published: "2026"
categories: []
keywords: ["honesty", "honesty finetuning", "interrogation", "alignment auditing"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:15+09:00"
---

# Spilling the Beans: Teaching LLMs to Self-Report Their Hidden Objectives

## Abstract
As AI systems become more capable of complex agentic tasks, they also become more capable of pursuing undesirable objectives and causing harm. Previous work has attempted to catch these unsafe instances by interrogating models directly about their objectives and behaviors. However, the main weakness of trusting interrogations is that models can lie. We propose self-report fine-tuning (SRFT), a simple supervised fine-tuning technique that trains models to occasionally make factual mistakes, then admit them when asked. We show that the admission of factual errors in simple question-answering settings generalizes out-of-distribution (OOD) to the admission of hidden misaligned objectives in adversarial agentic settings. We evaluate SRFT in OOD stealth tasks, where models are instructed to complete a hidden misaligned objective alongside a user-specified objective without being caught by monitoring. After SRFT, models are more likely to confess the details of their hidden objectives when interrogated, even under strong pressure not to disclose them. Interrogation on SRFT models can detect hidden objectives with near-ceiling performance (F1 score = 0.98), while the baseline model lies when interrogated under the same conditions (F1 score = 0). Interrogation on SRFT models can further elicit the content of the hidden objective, recovering 28-100\% details, compared to 0\% details recovered in the baseline model and by prefilled assistant turn attacks. This provides a promising technique for promoting honesty propensity and incriminating misaligned AI systems.

## Metadata
- venue: ICLR
- year: 2026
- authors: Chloe Li, Mary Phuong, Daniel Tan
- arxiv_id: 
- openreview_id: sWs0cCuM8I
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0f59d6703432a82dc869e3f3e8a23942692bd8e6.pdf
- published: 2026
- keywords: honesty, honesty finetuning, interrogation, alignment auditing

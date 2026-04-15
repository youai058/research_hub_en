---
title: "Dissecting learning and forgetting in language model finetuning"
authors: ["Xiao Zhang", "Ji Wu"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "tmsqb6WpLz"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/11ec6e4f64662107e73511797d5b3135c9385ef5.pdf"
published: "2024"
categories: []
keywords: ["language models", "domain adaptation", "catastrophic forgetting"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:49+09:00"
---

# Dissecting learning and forgetting in language model finetuning

## Abstract
Finetuning language models on domain-specific corpus is a common approach to enhance their domain knowledge and capability. While improving performance on domain tasks, it often brings a side-effect of forgetting of the model's general abilities. In this study, we analyze the effects of finetuning on language models by dissecting its impacts on the modeling of topic, style, and factual knowledge in text. Our method uses instruction-following LLMs such as ChatGPT to auto-generate controlled-variable text examples which we use to probe the model. Our findings reveal that finetuning results in significant shifts in the language model's topic and style priors, while actual knowledge learning only contributes to a small fraction of the total probability change. Analysis shows that the adaptation of topic and style priors behave akin to learning simple features: they are learned rapidly and require little model capacity. They are also learned independently and primarily at the beginning of a text sequence. In contrast, factual knowledge is learned stably but slowly and requires significant model capacity to learn. The research offers insights and understanding into the finer dynamics of learning and forgetting in language models, and can potentially inform future research on improving domain adaptation and addressing the challenges of forgetting in continual learning of language models.

## Metadata
- venue: ICLR
- year: 2024
- authors: Xiao Zhang, Ji Wu
- arxiv_id: 
- openreview_id: tmsqb6WpLz
- anthology_id: 
- pdf_url: https://openreview.net/pdf/11ec6e4f64662107e73511797d5b3135c9385ef5.pdf
- published: 2024
- keywords: language models, domain adaptation, catastrophic forgetting

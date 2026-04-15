---
title: "Limits of Transformer Language Models on Learning to Compose Algorithms"
authors: ["Jonathan Thomm", "Giacomo Camposampiero", "Aleksandar Terzic", "Michael Hersche", "Bernhard Schölkopf", "Abbas Rahimi"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "x7AD0343Jz"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b5c608c4483d2ed10fc624c08dd00561cddf4f4c.pdf"
published: "2024"
categories: []
keywords: ["Few-shot Compositional Learning", "Compositionality", "Sample Efficiency", "Algorithmic Learning", "Large Language Models", "Transformers"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:30+09:00"
---

# Limits of Transformer Language Models on Learning to Compose Algorithms

## Abstract
We analyze the capabilities of Transformer language models in learning compositional discrete tasks. To this end, we evaluate training LLaMA models and prompting GPT-4 and Gemini on four tasks demanding to learn a composition of several discrete sub-tasks. In particular, we measure how well these models can reuse primitives observable in the sub-tasks to learn the composition task. Our results indicate that compositional learning in state-of-the-art Transformer language models is highly sample inefficient: LLaMA requires more data samples than relearning all sub-tasks from scratch to learn the compositional task; in-context prompting with few samples is unreliable and fails at executing the sub-tasks or correcting the errors in multi-round code generation. Further, by leveraging complexity theory, we support these findings with a theoretical analysis focused on the sample inefficiency of gradient descent in memorizing feedforward models. We open source our code at https://github.com/IBM/limitations-lm-algorithmic-compositional-learning.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Jonathan Thomm, Giacomo Camposampiero, Aleksandar Terzic, Michael Hersche, Bernhard Schölkopf, Abbas Rahimi
- arxiv_id: 
- openreview_id: x7AD0343Jz
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b5c608c4483d2ed10fc624c08dd00561cddf4f4c.pdf
- published: 2024
- keywords: Few-shot Compositional Learning, Compositionality, Sample Efficiency, Algorithmic Learning, Large Language Models, Transformers

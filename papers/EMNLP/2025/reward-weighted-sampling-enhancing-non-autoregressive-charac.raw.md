---
title: "Reward-Weighted Sampling: Enhancing Non-Autoregressive Characteristics in Masked Diffusion LLM s"
authors: ["Daehoon Gwak", "Minseo Jung", "Junwoo Park", "Minho Park", "ChaeHun Park", "Junha Hyung", "Jaegul Choo"]
venue: "EMNLP"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: ""
anthology_id: "2025.emnlp-main.1754"
pdf_url: "https://aclanthology.org/2025.emnlp-main.1754.pdf"
published: "2025"
categories: []
keywords: []
venue_source: "anthology"
hunter_fetched: "2026-04-15T05:16:59+09:00"
---

# Reward-Weighted Sampling: Enhancing Non-Autoregressive Characteristics in Masked Diffusion LLM s

## Abstract
Masked diffusion models (MDMs) offer a promising non-autoregressive alternative for large language modeling. Standard decoding methods for MDMs, such as confidence-based sampling, select tokens independently based on individual token confidences at each diffusion step. However, we observe that this independent token selection often results in generation orders resembling sequential autoregressive processes, limiting the advantages of non-autoregressive modeling. To mitigate this pheonomenon, we propose Reward-Weighted Sampling (RWS), a novel decoding strategy that leverages an external reward model to provide a principled global signal during the iterative diffusion process. Specifically, at each diffusion step, RWS evaluates the quality of the entire intermediate sequence and scales token logits accordingly, guiding token selection by integrating global sequence-level coherence. This method selectively increases the confidence of tokens that initially have lower scores, thereby promoting a more non-autoregressive generation order. Furthermore, we provide theoretical justification showing that reward-weighted logit scaling induces beneficial rank reversals in token selection and consistently improves expected reward. Experiments demonstrate that RWS significantly promotes non-autoregressive generation orders, leading to improvements across multiple evaluation metrics. These results highlight the effectiveness of integrating global signals in enhancing both the non-autoregressive properties and overall performance of MDMs.

## Metadata
- venue: EMNLP
- year: 2025
- authors: Daehoon Gwak, Minseo Jung, Junwoo Park, Minho Park, ChaeHun Park, Junha Hyung, Jaegul Choo
- arxiv_id: 
- openreview_id: 
- anthology_id: 2025.emnlp-main.1754
- pdf_url: https://aclanthology.org/2025.emnlp-main.1754.pdf
- published: 2025

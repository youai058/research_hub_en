---
title: "Bridging Vision and Language Spaces with Assignment Prediction"
authors: ["Jungin Park", "Jiyoung Lee", "Kwanghoon Sohn"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "lK2V2E2MNv"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f92c528b5ee0113caeb927bb8305b6afaaff0004.pdf"
published: "2024"
categories: []
keywords: ["Multimodal learning", "vision-language tasks", "frozen LLMs", "optimal transport", "assignment prediction"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:47+09:00"
---

# Bridging Vision and Language Spaces with Assignment Prediction

## Abstract
This paper introduces VLAP, a novel approach that bridges pretrained vision models and large language models (LLMs) to make frozen LLMs understand the visual world. VLAP transforms the embedding space of pretrained vision models into the LLMs' word embedding space using a single linear layer for efficient and general-purpose visual and language understanding. Specifically, we harness well-established word embeddings to bridge two modality embedding spaces. The visual and text representations are simultaneously assigned to a set of word embeddings within pretrained LLMs by formulating the assigning procedure as an optimal transport problem. We predict the assignment of one modality from the representation of another modality data, enforcing consistent assignments for paired multimodal data. This allows vision and language representations to contain the same information, grounding the frozen LLMs' word embedding space in visual data. Moreover, a robust semantic taxonomy of LLMs can be preserved with visual data since the LLMs interpret and reason linguistic information from correlations between word embeddings. Experimental results show that VLAP achieves substantial improvements over the previous linear transformation-based approaches across a range of vision-language tasks, including image captioning, visual question answering, and cross-modal retrieval. We also demonstrate the learned visual representations hold a semantic taxonomy of LLMs, making visual semantic arithmetic possible.

## Metadata
- venue: ICLR
- year: 2024
- authors: Jungin Park, Jiyoung Lee, Kwanghoon Sohn
- arxiv_id: 
- openreview_id: lK2V2E2MNv
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f92c528b5ee0113caeb927bb8305b6afaaff0004.pdf
- published: 2024
- keywords: Multimodal learning, vision-language tasks, frozen LLMs, optimal transport, assignment prediction

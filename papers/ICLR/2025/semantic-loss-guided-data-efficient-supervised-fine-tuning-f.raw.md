---
title: "Semantic Loss Guided Data Efficient Supervised Fine Tuning for Safe Responses in LLMs"
authors: ["Yuxiao Lu", "Arunesh Sinha", "Pradeep Varakantham"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "kO0DgO07hW"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/423703df9e3cce20127a48400d60d498f821fb53.pdf"
published: "2025"
categories: []
keywords: ["Large Language Model", "Safe Large Language Model", "Earth Mover Distance", "Supervised Fine-tuning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:04+09:00"
---

# Semantic Loss Guided Data Efficient Supervised Fine Tuning for Safe Responses in LLMs

## Abstract
Large Language Models (LLMs) generating unsafe responses to toxic prompts is a significant issue in their applications. While various efforts aim to address this safety concern, previous approaches often demand substantial human data collection or rely on the less dependable option of using another LLM to generate corrective data. In this paper, we aim to take this problem and overcome limitations of requiring significant high-quality human data. Our method requires only a small set of unsafe responses to toxic prompts, easily obtained from the unsafe LLM itself. By employing a semantic cost combined with a negative Earth Mover Distance (EMD) loss, we guide the LLM away from generating unsafe responses. Additionally, we propose a novel lower bound for EMD loss, enabling more efficient optimization. Our results demonstrate superior performance and data efficiency compared to baselines, and we further examine the nuanced effects of over-alignment and potential degradation of language capabilities when using contrastive data.

## Metadata
- venue: ICLR
- year: 2025
- authors: Yuxiao Lu, Arunesh Sinha, Pradeep Varakantham
- arxiv_id: 
- openreview_id: kO0DgO07hW
- anthology_id: 
- pdf_url: https://openreview.net/pdf/423703df9e3cce20127a48400d60d498f821fb53.pdf
- published: 2025
- keywords: Large Language Model, Safe Large Language Model, Earth Mover Distance, Supervised Fine-tuning

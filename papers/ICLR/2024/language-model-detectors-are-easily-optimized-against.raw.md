---
title: "Language Model Detectors Are Easily Optimized Against"
authors: ["Charlotte Nicks", "Eric Mitchell", "Rafael Rafailov", "Archit Sharma", "Christopher D Manning", "Chelsea Finn", "Stefano Ermon"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "4eJDMjYZZG"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9a04cc3f1effc953fdd1e29092804ea28ce0eb7f.pdf"
published: "2024"
categories: []
keywords: ["detector", "language model", "learning from preferences"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:18+09:00"
---

# Language Model Detectors Are Easily Optimized Against

## Abstract
The fluency and general applicability of large language models (LLMs) has motivated significant interest in detecting whether a piece of text was written by a language model. While both academic and commercial detectors have been deployed in some settings, particularly education, other research has highlighted the fragility of these systems. In this paper, we demonstrate a data-efficient attack that fine-tunes language models to confuse existing detectors, leveraging recent developments in reinforcement learning of language models. We use the `human-ness' score (often just a log probability) of various open-source and commercial detectors as a reward function for reinforcement learning, subject to a KL-divergence constraint that the resulting model does not differ significantly from the original. For a 7B parameter Llama-2 model, fine-tuning for under a day reduces the AUROC of the OpenAI RoBERTa-Large detector from 0.84 to 0.63, while perplexity on OpenWebText increases from 8.7 to only 9.0; with a larger perplexity budget, we can drive AUROC to 0.30 (worse than random). Similar to traditional adversarial attacks, we find that this increase in 'detector evasion' generalizes to other detectors not used during training. In light of our empirical results, we advise against continued reliance on LLM-generated text detectors. Models, datasets, and selected experiment code will be released at https://github.com/charlottttee/llm-detector-evasion.

## Metadata
- venue: ICLR
- year: 2024
- authors: Charlotte Nicks, Eric Mitchell, Rafael Rafailov, Archit Sharma, Christopher D Manning, Chelsea Finn, Stefano Ermon
- arxiv_id: 
- openreview_id: 4eJDMjYZZG
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9a04cc3f1effc953fdd1e29092804ea28ce0eb7f.pdf
- published: 2024
- keywords: detector, language model, learning from preferences

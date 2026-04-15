---
title: "An Emulator for Fine-tuning Large Language Models using Small Language Models"
authors: ["Eric Mitchell", "Rafael Rafailov", "Archit Sharma", "Chelsea Finn", "Christopher D Manning"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Eo7kv0sllr"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b0342e1462535a7e1a40bac079cefdfd493a9912.pdf"
published: "2024"
categories: []
keywords: ["pre-training", "fine-tuning", "decouple", "scale", "reward", "alignment"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:16+09:00"
---

# An Emulator for Fine-tuning Large Language Models using Small Language Models

## Abstract
Widely used language models (LMs) are typically built by scaling up a two-stage training pipeline: a pre-training stage that uses a very large, diverse dataset of text and a fine-tuning (sometimes, 'alignment') stage that uses targeted examples or other specifications of desired behaviors. While it has been hypothesized that knowledge and skills come from pre-training, and fine-tuning mostly filters this knowledge and skillset, this intuition has not been extensively tested. To aid in doing so, we introduce a novel technique for decoupling the knowledge and skills gained in these two stages, enabling a direct answer to the question, *What would happen if we combined the knowledge learned by a large model during pre-training with the knowledge learned by a small model during fine-tuning (or vice versa)?* Using an RL-based framework derived from recent developments in learning from human preferences, we introduce *emulated fine-tuning (EFT)*, a principled and practical method for sampling from a distribution that approximates (or 'emulates') the result of pre-training and fine-tuning at different scales. Our experiments with EFT show that scaling up fine-tuning tends to improve helpfulness, while scaling up pre-training tends to improve factuality. Beyond decoupling scale, we show that EFT enables test-time adjustment of competing behavioral traits like helpfulness and harmlessness without additional training. Finally, a special case of emulated fine-tuning, which we call LM *up-scaling*, avoids resource-intensive fine-tuning of large pre-trained models by ensembling them with small fine-tuned models, essentially emulating the result of fine-tuning the large pre-trained model. Up-scaling consistently improves helpfulness and factuality of instruction-following models in the Llama, Llama-2, and Falcon families, without additional hyperparameters or training. For reference implementation, see [https://github.com/eric-mitchell/emulated-fine-tuning](https://github.com/eric-mitchell/emulated-fine-tuning).

## Metadata
- venue: ICLR
- year: 2024
- authors: Eric Mitchell, Rafael Rafailov, Archit Sharma, Chelsea Finn, Christopher D Manning
- arxiv_id: 
- openreview_id: Eo7kv0sllr
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b0342e1462535a7e1a40bac079cefdfd493a9912.pdf
- published: 2024
- keywords: pre-training, fine-tuning, decouple, scale, reward, alignment

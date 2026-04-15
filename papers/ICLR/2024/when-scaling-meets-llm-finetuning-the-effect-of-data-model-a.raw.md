---
title: "When Scaling Meets LLM Finetuning: The Effect of Data, Model and Finetuning Method"
authors: ["Biao Zhang", "Zhongtao Liu", "Colin Cherry", "Orhan Firat"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "5HCnKDeTws"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c50285d47fae2fec5f5aa87de6d9e6a921de02b9.pdf"
published: "2024"
categories: []
keywords: ["LLM finetuning", "Scaling Laws", "Full-model finetuning", "Parameter efficient tuning", "Machine Translation", "Multilingual Summarization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:24+09:00"
---

# When Scaling Meets LLM Finetuning: The Effect of Data, Model and Finetuning Method

## Abstract
While large language models (LLMs) often adopt finetuning to unlock their capabilities for downstream applications, our understanding on the inductive biases (especially the scaling properties) of different finetuning methods is still limited. To fill this gap, we conduct systematic experiments studying whether and how different scaling factors, including LLM model size, pretraining data size, new finetuning parameter size and finetuning data size, affect the finetuning performance. We consider two types of finetuning – full-model tuning (FMT) and parameter efficient tuning (PET, including prompt tuning and LoRA), and explore their scaling behaviors in the data-limited regime where the LLM model size substantially outweighs the finetuning data size. Based on two sets of pretrained bilingual LLMs from 1B to 16B and experiments on bilingual machine translation and multilingual summarization benchmarks, we find that 1) LLM finetuning follows a powerbased multiplicative joint scaling law between finetuning data size and each other scaling factor; 2) LLM finetuning benefits more from LLM model scaling than pretraining data scaling, and PET parameter scaling is generally ineffective; and 3) the optimal finetuning method is highly task- and finetuning data-dependent. We hope our findings could shed light on understanding, selecting and developing LLM finetuning methods.

## Metadata
- venue: ICLR
- year: 2024
- authors: Biao Zhang, Zhongtao Liu, Colin Cherry, Orhan Firat
- arxiv_id: 
- openreview_id: 5HCnKDeTws
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c50285d47fae2fec5f5aa87de6d9e6a921de02b9.pdf
- published: 2024
- keywords: LLM finetuning, Scaling Laws, Full-model finetuning, Parameter efficient tuning, Machine Translation, Multilingual Summarization

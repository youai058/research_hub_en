---
title: "Improving Transformers with Dynamically Composable Multi-Head Attention"
authors: ["Da Xiao", "Qingye Meng", "Shengping Li", "xingyuan yuan"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "RbiBKPtuHp"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ff4c9fbb27e8d39271c90edee9bc164c464d96c9.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:40+09:00"
---

# Improving Transformers with Dynamically Composable Multi-Head Attention

## Abstract
Multi-Head Attention (MHA) is a key component of Transformer. In MHA, attention heads work independently, causing problems such as low-rank bottleneck of attention score matrices and head redundancy. We propose Dynamically Composable Multi-Head Attention (DCMHA), a parameter and computation efficient attention architecture that tackles the shortcomings of MHA and increases the expressive power of the model by dynamically composing attention heads. At the core of DCMHA is a Compose function that transforms the attention score and weight matrices in an input-dependent way. DCMHA can be used as a drop-in replacement of MHA in any transformer architecture to obtain the corresponding DCFormer. DCFormer significantly outperforms Transformer on different architectures and model scales in language modeling, matching the performance of models with 1.7x-2.0x compute. For example, DCPythia-6.9B outperforms open source Pythia-12B on both pretraining perplexity and downstream task evaluation.

## Metadata
- venue: ICML
- year: 2024
- authors: Da Xiao, Qingye Meng, Shengping Li, xingyuan yuan
- arxiv_id: 
- openreview_id: RbiBKPtuHp
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ff4c9fbb27e8d39271c90edee9bc164c464d96c9.pdf
- published: 2024

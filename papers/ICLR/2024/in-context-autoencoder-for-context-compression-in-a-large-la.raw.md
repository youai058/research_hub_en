---
title: "In-context Autoencoder for Context Compression in a Large Language Model"
authors: ["Tao Ge", "Hu Jing", "Lei Wang", "Xun Wang", "Si-Qing Chen", "Furu Wei"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "uREj4ZuGJE"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0cb80bedd6a43e1383e8fe4642b39105d27be261.pdf"
published: "2024"
categories: []
keywords: ["large language model", "context compression", "in-context autoencoder", "pretraining", "fine-tuning", "Llama", "GPT", "memorization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:56+09:00"
---

# In-context Autoencoder for Context Compression in a Large Language Model

## Abstract
We propose the In-context Autoencoder (ICAE), leveraging the power of a large language model (LLM) to compress a long context into short compact memory slots that can be directly conditioned on by the LLM for various purposes. ICAE is first pretrained using both autoencoding and language modeling objectives on massive text data, enabling it to generate memory slots that accurately and comprehensively represent the original context. Then, it is fine-tuned on instruction data for producing desirable responses to various prompts. Experiments demonstrate that our lightweight ICAE, introducing about 1% additional parameters, effectively achieves $4\times$ context compression based on Llama, offering advantages in both improved latency and GPU memory cost during inference, and showing an interesting insight in memorization as well as potential for scalability. These promising results imply a novel perspective on the connection between working memory in cognitive science and representation learning in LLMs, revealing ICAE's significant implications in addressing the long context problem and suggesting further research in LLM context management. Our data, code and models are available at https://github.com/getao/icae.

## Metadata
- venue: ICLR
- year: 2024
- authors: Tao Ge, Hu Jing, Lei Wang, Xun Wang, Si-Qing Chen, Furu Wei
- arxiv_id: 
- openreview_id: uREj4ZuGJE
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0cb80bedd6a43e1383e8fe4642b39105d27be261.pdf
- published: 2024
- keywords: large language model, context compression, in-context autoencoder, pretraining, fine-tuning, Llama, GPT, memorization

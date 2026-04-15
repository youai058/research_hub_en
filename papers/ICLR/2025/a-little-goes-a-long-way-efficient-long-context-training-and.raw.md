---
title: "A Little Goes a Long Way: Efficient Long Context Training and Inference with Partial Contexts"
authors: ["Suyu Ge", "Xihui Lin", "Yunan Zhang", "Jiawei Han", "Hao Peng"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "TrKRpaOk8y"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/7ceb04c0d77c64ee96e21953799a34b2a15a7ddc.pdf"
published: "2025"
categories: []
keywords: ["Long-Context LLM", "Efficient LLM", "Context Extension", "KV Cache Reduction"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:12+09:00"
---

# A Little Goes a Long Way: Efficient Long Context Training and Inference with Partial Contexts

## Abstract
Training and serving long-context large language models (LLMs) incurs substantial overhead. 
To address this, two critical steps are often required: a pretrained LLM typically undergoes a separate stage for context length extension by training on long-context data, followed by architectural modifications to reduce the overhead of KV cache during serving. 
This paper argues that integrating length extension with a GPU-friendly KV cache reduction architecture not only reduces training overhead during length extension, but also achieves better long-context performance. 
This leads to our proposed LongGen, which finetunes a pretrained LLM into an efficient architecture during length extension. 
LongGen builds on three key insights: 
(1) Sparse attention patterns, such as window attention (attending to recent tokens), attention sink (initial ones), and blockwise sparse attention (strided token blocks) are well-suited for building efficient long-context models, primarily due to their GPU-friendly memory access patterns, enabling efficiency gains not just theoretically but in practice as well. 
(2) It is essential for the model to have direct access to all tokens. 
A hybrid architecture with 1/3 full attention layers and 2/3 efficient ones achieves a balanced trade-off between efficiency and long-context performance.
(3) Lightweight training on 5B long-context data is sufficient to extend the hybrid model's context length from 4K to 128K.

We evaluate LongGen on both Llama-2 7B and Llama-2 70B, demonstrating its effectiveness across different scales. 
During training with 128K-long contexts, LongGen achieves 1.55x training speedup and reduces wall-clock time by 36%, compared to a full-attention baseline. 
During inference, LongGen reduces KV cache memory by 62%, achieving 1.67x prefilling speedup and 1.41x decoding speedup.
Compared to baselines that apply KV-cache reduction techniques to full-attention long-context LLMs, LongGen achieves substantially stronger performance not only on the Needle-in-a-Haystack retrieval task, but also on more challenging long-context reasoning tasks, including BABILong and RULER.

## Metadata
- venue: ICLR
- year: 2025
- authors: Suyu Ge, Xihui Lin, Yunan Zhang, Jiawei Han, Hao Peng
- arxiv_id: 
- openreview_id: TrKRpaOk8y
- anthology_id: 
- pdf_url: https://openreview.net/pdf/7ceb04c0d77c64ee96e21953799a34b2a15a7ddc.pdf
- published: 2025
- keywords: Long-Context LLM, Efficient LLM, Context Extension, KV Cache Reduction

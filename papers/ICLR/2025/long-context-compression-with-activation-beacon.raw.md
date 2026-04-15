---
title: "Long Context Compression with Activation Beacon"
authors: ["Peitian Zhang", "Zheng Liu", "Shitao Xiao", "Ninglu Shao", "Qiwei Ye", "Zhicheng Dou"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "1eQT9OzfNQ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2cb117a00ef812283da61295a1d36584936a89ef.pdf"
published: "2025"
categories: []
keywords: ["Context Compression", "Long Context LLMs", "LLM Memory"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:51+09:00"
---

# Long Context Compression with Activation Beacon

## Abstract
Long context compression is a critical research problem due to its significance in reducing the high computational and memory costs associated with LLMs. In this paper, we propose Activation Beacon, a plug-in module for transformer-based LLMs that targets effective, efficient, and flexible compression of long contexts. To achieve this, our method introduces the following technical designs. 
1) We directly compress the activations (i.e. keys and values at every layer), rather than leveraging soft prompts to relay information (which constitute a major bottleneck to encapsulate the complex information within long contexts).
2) We tailor the compression workflow, where each fine-grained input unit is progressively compressed, enabling high-quality compression and efficient computation during both training and inference. 
3) We train the model through compression-based auto-regression, making full use of plain texts and instructional data to optimize the model's compression performance.
4) During training, we randomly sample a compression ratio at each step, teaching the model to support a wide range of compression configurations. 

Extensive evaluations are conducted on various long-context tasks whose lengths (e.g., 128K) may far exceed the maximum training length (20K), such as document understanding, few-shot learning, and Needle-in-a-Haystack. Whilst existing methods struggle to handle these challenging tasks, Activation Beacon maintains a comparable performance to the uncompressed baseline across various scenarios, 
achieving a 2x acceleration in inference time and an 8x reduction of memory costs for KV cache.

## Metadata
- venue: ICLR
- year: 2025
- authors: Peitian Zhang, Zheng Liu, Shitao Xiao, Ninglu Shao, Qiwei Ye, Zhicheng Dou
- arxiv_id: 
- openreview_id: 1eQT9OzfNQ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2cb117a00ef812283da61295a1d36584936a89ef.pdf
- published: 2025
- keywords: Context Compression, Long Context LLMs, LLM Memory

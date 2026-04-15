---
title: "Communication Efficient Distributed Training with Distributed Lion"
authors: ["Bo Liu", "Lemeng Wu", "Lizhang Chen", "Kaizhao Liang", "Jiaxu Zhu", "Chen Liang", "Raghuraman Krishnamoorthi", "qiang liu"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "wDirCeTIoz"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/12306ef9133c7e08f53a436d98a8c343b914f091.pdf"
published: "2024"
categories: []
keywords: ["Distributed Optimization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:36+09:00"
---

# Communication Efficient Distributed Training with Distributed Lion

## Abstract
The Lion optimizer has been a promising competitor with the AdamW for training large AI models, with advantages in memory, computation, and sample efficiency. In this paper, we introduce Distributed Lion, an innovative adaptation of Lion for distributed training environments. Leveraging the sign operator in Lion, our Distributed Lion only requires to communicate binary or lower-precision vectors
between workers to the center server, significantly reducing the communication cost.  
Our theoretical analysis confirms Distributed Lion's convergence properties. Empirical results demonstrate its robustness across a range of tasks, worker counts, and batch sizes, on both vision and language problems. Notably, Distributed Lion attains comparable performance to standard Lion or AdamW optimizers applied on aggregated gradients, but with significantly reduced communication bandwidth. This feature is particularly advantageous for training large models. In addition, we also demonstrate that \mavolion{} presents a more favorable performance-bandwidth balance compared to existing efficient distributed methods such as deep gradient compression and ternary gradients.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Bo Liu, Lemeng Wu, Lizhang Chen, Kaizhao Liang, Jiaxu Zhu, Chen Liang, Raghuraman Krishnamoorthi, qiang liu
- arxiv_id: 
- openreview_id: wDirCeTIoz
- anthology_id: 
- pdf_url: https://openreview.net/pdf/12306ef9133c7e08f53a436d98a8c343b914f091.pdf
- published: 2024
- keywords: Distributed Optimization

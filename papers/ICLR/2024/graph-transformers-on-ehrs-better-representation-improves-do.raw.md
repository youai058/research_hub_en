---
title: "Graph Transformers on EHRs: Better Representation Improves Downstream Performance"
authors: ["Raphael Poulain", "Rahmatollah Beheshti"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "pe0Vdv7rsL"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/cc3e4cf0f1122fe0c256b5e62246f05026012d2a.pdf"
published: "2024"
categories: []
keywords: ["transformers", "graph neural networks", "electronic health records"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:09+09:00"
---

# Graph Transformers on EHRs: Better Representation Improves Downstream Performance

## Abstract
Following the success of transformer-based methods across various machine learning applications, their adoption for healthcare predictive tasks using electronic health records (EHRs)  has also expanded extensively. Similarly, graph-based methods have been shown to be very effective in capturing inherent graph-type relationships in EHRs, leading to improved downstream performance. Although integrating these two families of approaches seems like a natural next step, in practice, creating such a design is challenging and has not been done. This is partly due to known EHR problems, such as high sparsity, making extracting meaningful temporal representations of medical visits challenging. In this study, we propose GT-BEHRT, a new approach that leverages temporal visit embeddings extracted from a graph transformer and uses a BERT-based model to obtain more robust patient representations, especially on longer EHR sequences. The graph-based approach allows GT-BEHRT to implicitly capture the intrinsic graphical relationships between medical observations, while the BERT model extracts the temporal relationships between visits, loosely mimicking the clinicians' decision-making process. As part of our method, we also present a two-step pre-training strategy for learning better graphical and temporal representations. Our proposed method achieves state-of-the-art performance in a variety of standard medical predictive tasks, demonstrating the versatility of our approach.

## Metadata
- venue: ICLR
- year: 2024
- authors: Raphael Poulain, Rahmatollah Beheshti
- arxiv_id: 
- openreview_id: pe0Vdv7rsL
- anthology_id: 
- pdf_url: https://openreview.net/pdf/cc3e4cf0f1122fe0c256b5e62246f05026012d2a.pdf
- published: 2024
- keywords: transformers, graph neural networks, electronic health records

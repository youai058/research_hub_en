---
title: "When Kernels Multiply, Clusters Unify: Fusing Embeddings with the Kronecker Product"
authors: ["Youqi WU", "Jingwei Zhang", "Farzan Farnia"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "XougXwZAHI"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9797c9fb9def801bd5b211410e9937c30ec34e3c.pdf"
published: "2025"
categories: []
keywords: ["Embedding Fusion", "Multimodal Representations", "Kernel Methods", "Random Projection", "Kronecker Product"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:48+09:00"
---

# When Kernels Multiply, Clusters Unify: Fusing Embeddings with the Kronecker Product

## Abstract
State-of-the-art embeddings often capture distinct yet complementary discriminative features: For instance, one image embedding model may excel at distinguishing fine-grained textures, while another focuses on object-level structure. Motivated by this observation, we propose a principled approach to fuse such complementary representations through *kernel multiplication*. Multiplying the kernel similarity functions of two embeddings allows their discriminative structures to interact, producing a fused representation whose kernel encodes the union of the clusters identified by each parent embedding. This formulation also provides a natural way to construct *joint kernels* for paired multi-modal data (e.g., image–text tuples), where the product of modality-specific kernels inherits structure from both domains. We highlight that this kernel product is mathematically realized via the *Kronecker product* of the embedding feature maps, yielding our proposed *KrossFuse* framework for embedding fusion. To address the computational cost of the resulting high-dimensional Kronecker space, we further develop *RP-KrossFuse*, a scalable variant that leverages random projections for efficient approximation. As a key application, we use this framework to bridge the performance gap between cross-modal embeddings (e.g., CLIP, BLIP) and unimodal experts (e.g., DINOv2, E5). Experiments show that RP-KrossFuse effectively integrates these models, enhancing modality-specific performance while preserving cross-modal alignment. The project code is available at https://github.com/yokiwuuu/KrossFuse.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Youqi WU, Jingwei Zhang, Farzan Farnia
- arxiv_id: 
- openreview_id: XougXwZAHI
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9797c9fb9def801bd5b211410e9937c30ec34e3c.pdf
- published: 2025
- keywords: Embedding Fusion, Multimodal Representations, Kernel Methods, Random Projection, Kronecker Product

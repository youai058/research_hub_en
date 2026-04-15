---
title: "Drop-Upcycling: Training Sparse Mixture of Experts with Partial Re-initialization"
authors: ["Taishi Nakamura", "Takuya Akiba", "Kazuki Fujii", "Yusuke Oda", "Rio Yokota", "Jun Suzuki"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "gx1wHnf5Vp"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/161bbf8b9a237f60ba0aee05309543ab2c3f0b1b.pdf"
published: "2025"
categories: []
keywords: ["mixture of experts", "large language models", "continual pre-training"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:46+09:00"
---

# Drop-Upcycling: Training Sparse Mixture of Experts with Partial Re-initialization

## Abstract
The Mixture of Experts (MoE) architecture reduces the training and inference cost significantly compared to a dense model of equivalent capacity. Upcycling is an approach that initializes and trains an MoE model using a pre-trained dense model. While upcycling leads to initial performance gains, the training progresses slower than when trained from scratch, leading to suboptimal performance in the long term. We propose Drop-Upcycling - a method that effectively addresses this problem. Drop-Upcycling combines two seemingly contradictory approaches: utilizing the knowledge of pre-trained dense models while statistically re-initializing some parts of the weights. This approach strategically promotes expert specialization, significantly enhancing the MoE model's efficiency in knowledge acquisition. 
Extensive large-scale experiments demonstrate that Drop-Upcycling significantly outperforms previous MoE construction methods in the long term, specifically when training on hundreds of billions of tokens or more.
As a result, our MoE model with 5.9B active parameters achieves comparable performance to a 13B dense model in the same model family, while requiring approximately 1/4 of the training FLOPs.
All experimental resources, including source code, training data, model checkpoints and logs, are publicly available to promote reproducibility and future research on MoE.

## Metadata
- venue: ICLR
- year: 2025
- authors: Taishi Nakamura, Takuya Akiba, Kazuki Fujii, Yusuke Oda, Rio Yokota, Jun Suzuki
- arxiv_id: 
- openreview_id: gx1wHnf5Vp
- anthology_id: 
- pdf_url: https://openreview.net/pdf/161bbf8b9a237f60ba0aee05309543ab2c3f0b1b.pdf
- published: 2025
- keywords: mixture of experts, large language models, continual pre-training

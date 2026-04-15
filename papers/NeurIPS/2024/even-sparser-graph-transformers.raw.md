---
title: "Even Sparser Graph Transformers"
authors: ["Hamed Shirzad", "Honghao Lin", "Balaji Venkatachalam", "Ameya Velingker", "David Woodruff", "Danica J. Sutherland"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "K3k4bWuNnk"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/7fe926e5cadd2fed753b0d6286ae2410bb55f717.pdf"
published: "2024"
categories: []
keywords: ["Graph Transformers", "Expander Graphs", "Sparsification"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:54+09:00"
---

# Even Sparser Graph Transformers

## Abstract
Graph Transformers excel in long-range dependency modeling, but generally require quadratic memory complexity in the number of nodes in an input graph, and hence have trouble scaling to large graphs. Sparse attention variants such as Exphormer can help, but may require high-degree augmentations to the input graph for good performance, and do not attempt to sparsify an already-dense input graph. As the learned attention mechanisms tend to use few of these edges, however, such high-degree connections may be unnecessary. We show (empirically and with theoretical backing) that attention scores on graphs are usually quite consistent across network widths, and use this observation to propose a two-stage procedure, which we call Spexphormer: first, train a narrow network on the full augmented graph. Next, use only the active connections to train a wider network on a much sparser graph. We establish theoretical conditions when a narrow network's attention scores can match those of a wide network, and show that Spexphormer achieves good performance with drastically reduced memory requirements on various graph datasets.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Hamed Shirzad, Honghao Lin, Balaji Venkatachalam, Ameya Velingker, David Woodruff, Danica J. Sutherland
- arxiv_id: 
- openreview_id: K3k4bWuNnk
- anthology_id: 
- pdf_url: https://openreview.net/pdf/7fe926e5cadd2fed753b0d6286ae2410bb55f717.pdf
- published: 2024
- keywords: Graph Transformers, Expander Graphs, Sparsification

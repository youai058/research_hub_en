---
title: "Generalization Analysis for Supervised Contrastive Representation Learning under Non-IID Settings"
authors: ["Nong Minh Hieu", "Antoine Ledent"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "kWSRVtuIuH"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d75c2f93fcf6d1ba3badcb904d7bb261605f4ccf.pdf"
published: "2025"
categories: []
keywords: ["Contrastive Learning", "Generalization Analysis"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:24+09:00"
---

# Generalization Analysis for Supervised Contrastive Representation Learning under Non-IID Settings

## Abstract
Contrastive Representation Learning (CRL) has achieved impressive success in various domains in recent years. Nevertheless, the theoretical understanding of the generalization behavior of CRL has remained limited. Moreover, to the best of our knowledge, the current literature only analyzes generalization bounds under the assumption that the data tuples used for contrastive learning are independently and identically distributed. However, in practice, we are often limited to a fixed pool of reusable labeled data points, making it inevitable to recycle data across tuples to create sufficiently large datasets. Therefore, the tuple-wise independence condition imposed by previous works is invalidated. In this paper, we provide a generalization analysis for the CRL framework under non-$i.i.d.$ settings that adheres to practice more realistically. Drawing inspiration from the literature on U-statistics, we derive generalization bounds which indicate that the required number of samples in each class scales as the logarithm of the covering number of the class of learnable feature representations associated to that class. Next, we apply our main results to derive excess risk bounds for common function classes such as linear maps and neural networks.

## Metadata
- venue: ICML
- year: 2025
- authors: Nong Minh Hieu, Antoine Ledent
- arxiv_id: 
- openreview_id: kWSRVtuIuH
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d75c2f93fcf6d1ba3badcb904d7bb261605f4ccf.pdf
- published: 2025
- keywords: Contrastive Learning, Generalization Analysis

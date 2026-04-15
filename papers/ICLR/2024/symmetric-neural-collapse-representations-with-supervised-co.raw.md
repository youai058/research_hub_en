---
title: "Symmetric Neural-Collapse Representations with Supervised Contrastive Loss: The Impact of ReLU and Batching"
authors: ["Ganesh Ramachandra Kini", "Vala Vakilian", "Tina Behnia", "Jaidev Gill", "Christos Thrampoulidis"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "AyXIDfvYg8"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b40ab759531e71a4137172d4dca6019ea210d8d1.pdf"
published: "2024"
categories: []
keywords: ["Supervised contrastive learning", "neural collapse", "implicit bias", "class imbalance"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:55+09:00"
---

# Symmetric Neural-Collapse Representations with Supervised Contrastive Loss: The Impact of ReLU and Batching

## Abstract
Supervised contrastive loss (SCL) is a competitive and often superior alternative to the cross-entropy loss for classification. While prior studies have demonstrated that both losses yield symmetric training representations under balanced data, this symmetry breaks under class imbalances. This paper presents an intriguing discovery: the introduction of a ReLU activation at the final layer effectively restores the symmetry in SCL-learned representations. We arrive at this finding analytically, by establishing that the global minimizers of an unconstrained features model with SCL loss and entry-wise non-negativity constraints form an orthogonal frame. Extensive experiments conducted across various datasets, architectures, and imbalance scenarios corroborate our finding.  Importantly, our experiments reveal that the inclusion of the ReLU activation restores symmetry without compromising test accuracy. This constitutes the first geometry characterization of SCL under imbalances. Additionally, our analysis and experiments underscore the pivotal role of batch selection strategies in representation geometry. By proving necessary and sufficient conditions for mini-batch choices that ensure invariant symmetric representations, we introduce batch-binding as an efficient strategy that guarantees these conditions hold.

## Metadata
- venue: ICLR
- year: 2024
- authors: Ganesh Ramachandra Kini, Vala Vakilian, Tina Behnia, Jaidev Gill, Christos Thrampoulidis
- arxiv_id: 
- openreview_id: AyXIDfvYg8
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b40ab759531e71a4137172d4dca6019ea210d8d1.pdf
- published: 2024
- keywords: Supervised contrastive learning, neural collapse, implicit bias, class imbalance

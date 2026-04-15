---
title: "Self-Supervised Learning of Graph Representations for Network Intrusion Detection"
authors: ["Lorenzo Guerra", "Thomas Chapuis", "Guillaume Duc", "Pavlo Mozharovskyi", "Van-Tam Nguyen"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "5bu1IOOvf0"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/8deed34a93ce3ae14970c0d3048cfdb5c04f37c0.pdf"
published: "2025"
categories: []
keywords: ["Self-supervised learning", "Graph neural networks", "Masked autoencoder", "Anomaly detection", "Intrusion detection", "Network security", "Representation learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:26+09:00"
---

# Self-Supervised Learning of Graph Representations for Network Intrusion Detection

## Abstract
Detecting intrusions in network traffic is a challenging task, particularly under limited supervision and constantly evolving attack patterns. While recent works have leveraged graph neural networks for network intrusion detection, they often decouple representation learning from anomaly detection, limiting the utility of the embeddings for identifying attacks. We propose GraphIDS, a self-supervised intrusion detection model that unifies these two stages by learning local graph representations of normal communication patterns through a masked autoencoder. An inductive graph neural network embeds each flow with its local topological context to capture typical network behavior, while a Transformer‑based encoder-decoder reconstructs these embeddings, implicitly learning global co-occurrence patterns via self-attention without requiring explicit positional information. During inference, flows with unusually high reconstruction errors are flagged as potential intrusions. This end-to-end framework ensures that embeddings are directly optimized for the downstream task, facilitating the recognition of malicious traffic. On diverse NetFlow benchmarks, GraphIDS achieves up to 99.98% PR‑AUC and 99.61% macro F1-score, outperforming baselines by 5–25 percentage points.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Lorenzo Guerra, Thomas Chapuis, Guillaume Duc, Pavlo Mozharovskyi, Van-Tam Nguyen
- arxiv_id: 
- openreview_id: 5bu1IOOvf0
- anthology_id: 
- pdf_url: https://openreview.net/pdf/8deed34a93ce3ae14970c0d3048cfdb5c04f37c0.pdf
- published: 2025
- keywords: Self-supervised learning, Graph neural networks, Masked autoencoder, Anomaly detection, Intrusion detection, Network security, Representation learning

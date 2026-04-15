---
title: "Is Graph Unlearning Ready for Practice? A Benchmark on Efficiency, Utility, and Forgetting"
authors: ["Samyak Jain", "Ronak Kalvani", "sainyam galhotra", "Sayan Ranu"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "gSPkuTTWgU"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f6cbce2c9b8860e100d290f6bcff7f3e84c71f84.pdf"
published: "2026"
categories: []
keywords: ["graph unlearning", "GNN", "graph neural network"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:28+09:00"
---

# Is Graph Unlearning Ready for Practice? A Benchmark on Efficiency, Utility, and Forgetting

## Abstract
Graph Neural Networks (\textsc{Gnn}s) are increasingly being deployed in sensitive, user-centric applications where regulations such as the GDPR mandate the ability to remove data upon request. This has spurred interest in graph unlearning, the task of removing the influence of specific training data from a trained \textsc{Gnn}  without retraining from scratch. While several unlearning techniques have recently emerged, the field lacks a principled benchmark to assess whether these methods truly provide a practical alternative to retraining and, if so, how to choose among them for different workloads. In this work, we present the first systematic benchmark for \textsc{Gnn} unlearning, structured around three core desiderata: \emph{efficiency} (is unlearning faster than retraining?), \emph{utility} (does the unlearned model preserve predictive performance and align with the retrained gold standard?), and \emph{forgetting} (does the model genuinely eliminate the influence of removed data?). Through extensive experiments across diverse datasets and deletion scenarios, we deliver a unified assessment of existing approaches, surfacing their trade-offs and limitations. Crucially, our findings show that most unlearning techniques are not yet practical for large-scale graphs. At the same time, our benchmarking yields actionable guidelines on when unlearning can be a viable alternative to retraining and how to select among methods for different workloads, thereby charting a path for future research toward more practical, scalable, and trustworthy graph unlearning.

## Metadata
- venue: ICLR
- year: 2026
- authors: Samyak Jain, Ronak Kalvani, sainyam galhotra, Sayan Ranu
- arxiv_id: 
- openreview_id: gSPkuTTWgU
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f6cbce2c9b8860e100d290f6bcff7f3e84c71f84.pdf
- published: 2026
- keywords: graph unlearning, GNN, graph neural network

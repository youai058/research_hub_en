---
title: "Preference-driven Knowledge Distillation for Few-shot Node Classification"
authors: ["Xing Wei", "Chunchun Chen", "Rui Fan", "Xiaofeng Cao", "Sourav Medya", "Wei Ye"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "60I6TzuHOb"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/4781f3cd2c992afccba892ad3e58c12eb71d2c7e.pdf"
published: "2025"
categories: []
keywords: ["Preference-driven", "Knowledge distillation", "Large language models", "Few-shot node classification"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:53+09:00"
---

# Preference-driven Knowledge Distillation for Few-shot Node Classification

## Abstract
Graph neural networks (GNNs) can efficiently process text-attributed graphs (TAGs) due to their message-passing mechanisms, but their training heavily relies on the human-annotated labels. Moreover, the complex and diverse local topologies of nodes of real-world TAGs make it challenging for a single mechanism to handle. Large language models (LLMs) perform well in zero-/few-shot learning on TAGs but suffer from a scalability challenge. Therefore, we propose a preference-driven knowledge distillation (PKD) framework to synergize the complementary strengths of LLMs and various GNNs for few-shot node classification. Specifically, we develop a GNN-preference-driven node selector that effectively promotes prediction distillation from LLMs to teacher GNNs. To further tackle nodes' intricate local topologies, we develop a node-preference-driven GNN selector that identifies the most suitable teacher GNN for each node, thereby facilitating tailored knowledge distillation from teacher GNNs to the student GNN. Extensive experiments validate the efficacy of our proposed framework in few-shot node classification on real-world TAGs.
Our code can be available at <https://github.com/GEEX-Weixing/PKD>.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Xing Wei, Chunchun Chen, Rui Fan, Xiaofeng Cao, Sourav Medya, Wei Ye
- arxiv_id: 
- openreview_id: 60I6TzuHOb
- anthology_id: 
- pdf_url: https://openreview.net/pdf/4781f3cd2c992afccba892ad3e58c12eb71d2c7e.pdf
- published: 2025
- keywords: Preference-driven, Knowledge distillation, Large language models, Few-shot node classification

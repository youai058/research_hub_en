---
title: "Disentangled Graph Self-supervised Learning for Out-of-Distribution Generalization"
authors: ["Haoyang Li", "Xin Wang", "Zeyang Zhang", "Haibo Chen", "Ziwei Zhang", "Wenwu Zhu"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "OS0szhkPmF"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e019065b5cb3a789aa9665b6a7a629f89532a717.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:38+09:00"
---

# Disentangled Graph Self-supervised Learning for Out-of-Distribution Generalization

## Abstract
Graph out-of-distribution (OOD) generalization, aiming to generalize graph neural networks (GNNs) under distribution shifts between training and testing environments, has attracted ever-increasing attention recently. However, existing literature heavily relies on sufficient task-dependent graph labels, which are often scarce or even unavailable, limiting their applications in real-world scenarios. In this paper, we study the self-supervised graph OOD generalization problem, i.e., learning GNNs capable of achieving relatively stable performances under distribution shifts without graph labels. However, the problem remains largely unexplored, with the critical challenge that the invariant and variant information are highly entangled in graphs. To solve this problem, we propose an OOD generalized disentangled graph contrastive learning model (OOD-GCL), which is capable of learning disentangled graph-level representations with self-supervision that can handle distribution shifts between training and testing graph data. Specifically, we first introduce a disentangled graph encoder to map each input graph into the factorized graph representation. Then we propose a tailored disentangled invariant self-supervised learning module to maximize predictive ability of the representations and make sure the representations other than from one specific channel are invariant to the environments partitioned by this latent factor for excluding the information corresponding to this latent factor for disentanglement. Finally, the disentangled graph representations are fed into a linear predictor and finetuned for the downstream tasks. We provide comprehensive theoretical analyses to show that our model can learn disentangled graph representations and achieve OOD generalization. Extensive experiments on real-world datasets demonstrate the superiority of our model against state-of-the-art baselines under distribution shifts for graph classification tasks.

## Metadata
- venue: ICML
- year: 2024
- authors: Haoyang Li, Xin Wang, Zeyang Zhang, Haibo Chen, Ziwei Zhang, Wenwu Zhu
- arxiv_id: 
- openreview_id: OS0szhkPmF
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e019065b5cb3a789aa9665b6a7a629f89532a717.pdf
- published: 2024

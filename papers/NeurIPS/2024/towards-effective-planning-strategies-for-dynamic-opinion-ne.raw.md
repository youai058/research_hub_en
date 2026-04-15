---
title: "Towards Effective Planning Strategies for Dynamic Opinion Networks"
authors: ["Bharath Chandra Muppasani", "Protik Nag", "Vignesh Narayanan", "Biplav Srivastava", "Michael Huhns"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "LYivxMp5es"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b10f14226dad5c3f51e1b9938bb8b4f651a36809.pdf"
published: "2024"
categories: []
keywords: ["Opinion networks", "Dynamic Planning", "Misinformation Spread", "Network dynamics."]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:42+09:00"
---

# Towards Effective Planning Strategies for Dynamic Opinion Networks

## Abstract
In this study, we investigate the under-explored intervention planning aimed at disseminating accurate information within dynamic opinion networks by leveraging learning strategies. Intervention planning involves identifying key nodes (search) and exerting control (e.g., disseminating accurate/official information through the nodes) to mitigate the influence of misinformation. However, as the network size increases, the problem becomes computationally intractable. To address this, we first introduce a ranking algorithm to identify key nodes for disseminating accurate information, which facilitates the training of neural network (NN) classifiers that provide generalized solutions for the search and planning problems. Second, we mitigate the complexity of label generation—which becomes challenging as the network grows—by developing a reinforcement learning (RL)-based centralized dynamic planning framework. We analyze these NN-based planners for opinion networks governed by two dynamic propagation models. Each model incorporates both binary and continuous opinion and trust representations. Our experimental results demonstrate that the ranking algorithm-based classifiers provide plans that enhance infection rate control, especially with increased action budgets for small networks. Further, we observe that the reward strategies focusing on key metrics, such as the number of susceptible nodes and infection rates, outperform those prioritizing faster blocking strategies. Additionally, our findings reveal that graph convolutional network (GCN)-based planners facilitate scalable centralized plans that achieve lower infection rates (higher control) across various network configurations (e.g., Watts-Strogatz topology, varying action budgets, varying initial infected nodes, and varying degree of infected nodes).

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Bharath Chandra Muppasani, Protik Nag, Vignesh Narayanan, Biplav Srivastava, Michael Huhns
- arxiv_id: 
- openreview_id: LYivxMp5es
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b10f14226dad5c3f51e1b9938bb8b4f651a36809.pdf
- published: 2024
- keywords: Opinion networks, Dynamic Planning, Misinformation Spread, Network dynamics.

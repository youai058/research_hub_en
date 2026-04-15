---
title: "Brain network science modelling of sparse neural networks enables Transformers and LLMs to perform as fully connected"
authors: ["Yingtao Zhang", "Diego Cerretti", "Jialin Zhao", "Wenjing Wu", "Ziheng Liao", "Umberto Michieli", "Carlo Vittorio Cannistraci"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "OM0Qkq9xtY"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d4df0dbbaaa665a14d4e33596a9bec5cc6954c06.pdf"
published: "2025"
categories: []
keywords: ["dynamic sparse training", "network science", "epitopological Learning", "efficient training"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:28+09:00"
---

# Brain network science modelling of sparse neural networks enables Transformers and LLMs to perform as fully connected

## Abstract
This study aims to enlarge our current knowledge on the application of brain-inspired network science principles for training artificial neural networks (ANNs) with sparse connectivity. Dynamic sparse training (DST) emulates the synaptic turnover of real brain networks, reducing the computational demands of training and inference in ANNs. However, existing DST methods face difficulties in maintaining peak performance at high connectivity sparsity levels. The Cannistraci-Hebb training (CHT) is a brain-inspired method that is used in DST for growing synaptic connectivity in sparse neural networks. CHT leverages a gradient-free, topology-driven link regrowth mechanism, which has been shown to achieve ultra-sparse (1\% connectivity or lower) advantage across various tasks compared to fully connected networks. Yet, CHT suffers two main drawbacks: (i) its time complexity is $\mathcal{O}(N\cdot d^3)$- N node network size, d node degree - hence it can be efficiently applied only to ultra-sparse networks. (ii) it rigidly selects top link prediction scores, which is inappropriate for the early training epochs, when the network topology presents many unreliable connections. Here, we design the first brain-inspired network model - termed bipartite receptive field (BRF) - to initialize the connectivity of sparse artificial neural networks. Then, we propose a matrix multiplication GPU-friendly approximation of the CH link predictor, which reduces the computational complexity to $\mathcal{O}(N^3)$, enabling a fast implementation of link prediction in large-scale models. Moreover, we introduce the Cannistraci-Hebb training soft rule (CHTs), which adopts a flexible strategy for sampling connections in both link removal and regrowth, balancing the exploration and exploitation of network topology. Additionally, we propose a sigmoid-based gradual density decay strategy, leading to an advanced framework referred to as CHTss. Empirical results show that BRF offers performance advantages over previous network science models. Using 1\% of connections, CHTs outperforms fully connected networks in MLP architectures on visual classification tasks, compressing some networks to less than 30\% of the nodes. Using 5\% of the connections, CHTss outperforms fully connected networks in two Transformer-based machine translation tasks. Finally, with only 30\% of the connections, both CHTs and CHTss achieve superior performance over other dynamic sparse training methods, and perform on par with—or even surpass—their fully connected counterparts in language modeling across various sparsity levels within the LLaMA model family. The code is available at: https://github.com/biomedical-cybernetics/Cannistraci-Hebb-Training-Soft-Rule-.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Yingtao Zhang, Diego Cerretti, Jialin Zhao, Wenjing Wu, Ziheng Liao, Umberto Michieli, Carlo Vittorio Cannistraci
- arxiv_id: 
- openreview_id: OM0Qkq9xtY
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d4df0dbbaaa665a14d4e33596a9bec5cc6954c06.pdf
- published: 2025
- keywords: dynamic sparse training, network science, epitopological Learning, efficient training

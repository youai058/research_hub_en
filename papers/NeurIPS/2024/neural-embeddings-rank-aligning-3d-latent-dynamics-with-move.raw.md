---
title: "Neural Embeddings Rank: Aligning 3D latent dynamics with movements"
authors: ["Chenggang Chen", "Zhiyu Yang", "Xiaoqin Wang"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Hlcek7AYgP"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/54f83850c3b40bc4f2a7a39b90cba72e5a465bad.pdf"
published: "2024"
categories: []
keywords: ["Dimensionality reduction", "Latent dynamics", "Brain-machine interfaces", "Neural decoding", "Contrastive learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:32+09:00"
---

# Neural Embeddings Rank: Aligning 3D latent dynamics with movements

## Abstract
Aligning neural dynamics with movements is a fundamental goal in neuroscience and brain-machine interfaces. However, there is still a lack of dimensionality reduction methods that can effectively align low-dimensional latent dynamics with movements. To address this gap, we propose Neural Embeddings Rank (NER), a technique that embeds neural dynamics into a 3D latent space and contrasts the embeddings based on movement ranks. NER learns to regress continuous representations of neural dynamics (i.e., embeddings) on continuous movements. We apply NER and six other dimensionality reduction techniques to neurons in the primary motor cortex (M1), dorsal premotor cortex (PMd), and primary somatosensory cortex (S1) as monkeys perform reaching tasks. Only NER aligns latent dynamics with both hand position and direction, visualizable in 3D. NER reveals consistent latent dynamics in M1 and PMd across sixteen sessions over a year. Using a linear regression decoder, NER explains 86\% and 97\% of the variance in velocity and position, respectively. Linear models trained on data from one session successfully decode velocity, position, and direction in held-out test data from different dates and cortical areas (64\%, 88\%, and 90\%). NER also reveals distinct latent dynamics in S1 during consistent movements and in M1 during curved reaching tasks. The code is available at https://github.com/NeuroscienceAI/NER.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Chenggang Chen, Zhiyu Yang, Xiaoqin Wang
- arxiv_id: 
- openreview_id: Hlcek7AYgP
- anthology_id: 
- pdf_url: https://openreview.net/pdf/54f83850c3b40bc4f2a7a39b90cba72e5a465bad.pdf
- published: 2024
- keywords: Dimensionality reduction, Latent dynamics, Brain-machine interfaces, Neural decoding, Contrastive learning

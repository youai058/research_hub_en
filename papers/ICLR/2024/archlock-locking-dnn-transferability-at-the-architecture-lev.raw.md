---
title: "ArchLock: Locking DNN Transferability at the Architecture Level with a Zero-Cost Binary Predictor"
authors: ["Tong Zhou", "Shaolei Ren", "Xiaolin Xu"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "e2YOVTenU9"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c801da252c8a18ba94f5b374ffd9515a915c541d.pdf"
published: "2024"
categories: []
keywords: ["Defense; DNN Transferability; Neural Architecture Search"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:05+09:00"
---

# ArchLock: Locking DNN Transferability at the Architecture Level with a Zero-Cost Binary Predictor

## Abstract
Deep neural network (DNN) models, despite their impressive performance, are vulnerable to exploitation by attackers who attempt to transfer them to other tasks for their own benefit. Current defense strategies mainly address this vulnerability at the model parameter level, leaving the potential of architectural-level defense largely unexplored. This paper, for the first time, addresses the issue of model protection by reducing transferability at the architecture level. Specifically, we present a novel neural architecture search (NAS)-enabled algorithm that employs zero-cost proxies and evolutionary search, to explore model architectures with low transferability. Our method, namely ArchLock, aims to achieve high performance on the source task, while degrading the performance on potential target tasks, i.e., locking the transferability of a DNN model. To achieve efficient cross-task search without accurately knowing the training data owned by the attackers, we utilize zero-cost proxies to speed up architecture evaluation and simulate potential target task embeddings to assist cross-task search with a binary performance predictor. Extensive experiments on NAS-Bench-201 and TransNAS-Bench-101 demonstrate that ArchLock reduces transferability by up to 30% and 50%, respectively, with negligible performance degradation on source tasks (<2%). The code is available at https://github.com/Tongzhou0101/ArchLock.

## Metadata
- venue: ICLR
- year: 2024
- authors: Tong Zhou, Shaolei Ren, Xiaolin Xu
- arxiv_id: 
- openreview_id: e2YOVTenU9
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c801da252c8a18ba94f5b374ffd9515a915c541d.pdf
- published: 2024
- keywords: Defense; DNN Transferability; Neural Architecture Search

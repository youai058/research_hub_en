---
title: "PDUDT: Provable Decentralized Unlearning under Dynamic Topologies"
authors: ["Jing Qiao", "Yu Liu", "Zengzhe Chen", "Mingyi Li", "YUAN YUAN", "Xiao Zhang", "Dongxiao Yu"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "K0Vg8b7nyI"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e30583ea546b9040e551da5958ae7e1a0dd99826.pdf"
published: "2025"
categories: []
keywords: ["Decentralized unlearning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:26+09:00"
---

# PDUDT: Provable Decentralized Unlearning under Dynamic Topologies

## Abstract
This paper investigates decentralized unlearning, aiming to eliminate the impact of a specific client on the whole decentralized system. However, decentralized communication characterizations pose new challenges for effective unlearning: the indirect connections make it difficult to trace the specific client's impact, while the dynamic topology limits the scalability of retraining-based unlearning methods.
In this paper, we propose the first **P**rovable **D**ecentralized **U**nlearning algorithm under **D**ynamic **T**opologies called PDUDT. It allows clients to eliminate the influence of a specific client without additional communication or retraining. We provide rigorous theoretical guarantees for PDUDT, showing it is statistically indistinguishable from perturbed retraining. Additionally, it achieves an efficient convergence rate of $\mathcal{O}(\frac{1}{T})$ in subsequent learning, where $T$ is the total communication rounds. This rate matches state-of-the-art results. Experimental results show that compared with the Retrain method, PDUDT saves more than 99\% of unlearning time while achieving comparable unlearning performance.

## Metadata
- venue: ICML
- year: 2025
- authors: Jing Qiao, Yu Liu, Zengzhe Chen, Mingyi Li, YUAN YUAN, Xiao Zhang, Dongxiao Yu
- arxiv_id: 
- openreview_id: K0Vg8b7nyI
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e30583ea546b9040e551da5958ae7e1a0dd99826.pdf
- published: 2025
- keywords: Decentralized unlearning

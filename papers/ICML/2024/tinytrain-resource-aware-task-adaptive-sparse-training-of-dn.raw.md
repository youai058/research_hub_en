---
title: "TinyTrain: Resource-Aware Task-Adaptive Sparse Training of DNNs at the Data-Scarce Edge"
authors: ["Young D. Kwon", "Rui Li", "Stylianos Venieris", "Jagmohan Chauhan", "Nicholas Donald Lane", "Cecilia Mascolo"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "MWZWUyfFHC"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e4a15fac67165965a4eef25646f0f913b85d6e9b.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:36+09:00"
---

# TinyTrain: Resource-Aware Task-Adaptive Sparse Training of DNNs at the Data-Scarce Edge

## Abstract
On-device training is essential for user personalisation and privacy. With the pervasiveness of IoT devices and microcontroller units (MCUs), this task becomes more challenging due to the constrained memory and compute resources, and the limited availability of labelled user data. Nonetheless, prior works neglect the data scarcity issue, require excessively long training time ($\textit{e.g.}$ a few hours), or induce substantial accuracy loss ($\geq$10%). In this paper, we propose TinyTrain, an on-device training approach that drastically reduces training time by selectively updating parts of the model and explicitly coping with data scarcity. TinyTrain introduces a task-adaptive sparse-update method that $\textit{dynamically}$ selects the layer/channel to update based on a multi-objective criterion that jointly captures user data, the memory, and the compute capabilities of the target device, leading to high accuracy on unseen tasks with reduced computation and memory footprint. TinyTrain outperforms vanilla fine-tuning of the entire network by 3.6-5.0% in accuracy, while reducing the backward-pass memory and computation cost by up to 1,098$\times$ and 7.68$\times$, respectively. Targeting broadly used real-world edge devices, TinyTrain achieves 9.5$\times$ faster and 3.5$\times$ more energy-efficient training over status-quo approaches, and 2.23$\times$ smaller memory footprint than SOTA methods, while remaining within the 1 MB memory envelope of MCU-grade platforms.

## Metadata
- venue: ICML
- year: 2024
- authors: Young D. Kwon, Rui Li, Stylianos Venieris, Jagmohan Chauhan, Nicholas Donald Lane, Cecilia Mascolo
- arxiv_id: 
- openreview_id: MWZWUyfFHC
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e4a15fac67165965a4eef25646f0f913b85d6e9b.pdf
- published: 2024

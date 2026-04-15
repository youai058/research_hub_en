---
title: "Unified Insights: Harnessing Multi-modal Data for Phenotype Imputation via View Decoupling"
authors: ["Qiannan Zhang", "Weishen Pan", "Zilong Bai", "Chang Su", "Fei Wang"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "8B3sAX889P"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/38a4a7cc918c6d4799b2de3589f1186ac0d322fe.pdf"
published: "2024"
categories: []
keywords: ["Phenotype Imputation", "Graph Neural Networks", "Biological Multi-modal data"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:43+09:00"
---

# Unified Insights: Harnessing Multi-modal Data for Phenotype Imputation via View Decoupling

## Abstract
Phenotype imputation plays a crucial role in improving comprehensive and accurate medical evaluation, which in turn can optimize patient treatment and bolster the reliability of clinical research. Despite the adoption of various techniques, multi-modal biological data, which can provide crucial insights into a patient's overall health, is often overlooked. With multi-modal biological data, patient characterization can be enriched from two distinct views: the biological view and the phenotype view. However, the heterogeneity and imprecise nature of the multimodal data still pose challenges in developing an effective method to model from two views. In this paper, we propose a novel framework to incorporate multi-modal biological data via view decoupling. Specifically, we segregate the modeling of biological data from phenotype data in a graph-based learning framework. From the biological view, the latent factors in biological data are discovered to model patient correlation. From the phenotype view, phenotype co-occurrence can be modeled to reveal patterns across patients. Then patients are encoded from these two distinct views. To mitigate the influence of noise and irrelevant information in biological data, we devise a cross-view contrastive knowledge distillation aimed at distilling insights from the biological view to enhance phenotype imputation. We show that phenotype imputation with the proposed model significantly outperforms the state-of-the-art models on the real-world biomedical database.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Qiannan Zhang, Weishen Pan, Zilong Bai, Chang Su, Fei Wang
- arxiv_id: 
- openreview_id: 8B3sAX889P
- anthology_id: 
- pdf_url: https://openreview.net/pdf/38a4a7cc918c6d4799b2de3589f1186ac0d322fe.pdf
- published: 2024
- keywords: Phenotype Imputation, Graph Neural Networks, Biological Multi-modal data

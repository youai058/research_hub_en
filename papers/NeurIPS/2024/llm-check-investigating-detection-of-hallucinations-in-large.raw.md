---
title: "LLM-Check: Investigating Detection of Hallucinations in Large Language Models"
authors: ["Gaurang Sriramanan", "Siddhant Bharti", "Vinu Sankar Sadasivan", "Shoumik Saha", "Priyatham Kattakinda", "Soheil Feizi"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "LYx4w3CAgy"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/4d3d91355b8770b4a9a630a2348963ddd775ffc4.pdf"
published: "2024"
categories: []
keywords: ["Large Language Models", "Hallucinations in Language Models", "Hallucination Detection", "Eigen-analysis of LM Embeddings"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:58+09:00"
---

# LLM-Check: Investigating Detection of Hallucinations in Large Language Models

## Abstract
While Large Language Models (LLMs) have become immensely popular due to their outstanding performance on a broad range of tasks, these models are prone to producing hallucinations— outputs that are fallacious or fabricated yet often appear plausible or tenable at a glance. In this paper, we conduct a comprehensive investigation into the nature of hallucinations within LLMs and furthermore explore effective techniques for detecting such inaccuracies in various real-world settings. Prior approaches to detect hallucinations in LLM outputs, such as consistency checks or retrieval-based methods, typically assume access to multiple model responses or large databases. These techniques, however, tend to be computationally expensive in practice, thereby limiting their applicability to real-time analysis. In contrast, in this work, we seek to identify hallucinations within a single response in both white-box and black-box settings by analyzing the internal hidden states, attention maps, and output prediction probabilities of an auxiliary LLM. In addition, we also study hallucination detection in scenarios where ground-truth references are also available, such as in the setting of Retrieval-Augmented Generation (RAG). We demonstrate that the proposed detection methods are extremely compute-efficient, with speedups of up to 45x and 450x over other baselines, while achieving significant improvements in detection performance over diverse datasets.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Gaurang Sriramanan, Siddhant Bharti, Vinu Sankar Sadasivan, Shoumik Saha, Priyatham Kattakinda, Soheil Feizi
- arxiv_id: 
- openreview_id: LYx4w3CAgy
- anthology_id: 
- pdf_url: https://openreview.net/pdf/4d3d91355b8770b4a9a630a2348963ddd775ffc4.pdf
- published: 2024
- keywords: Large Language Models, Hallucinations in Language Models, Hallucination Detection, Eigen-analysis of LM Embeddings

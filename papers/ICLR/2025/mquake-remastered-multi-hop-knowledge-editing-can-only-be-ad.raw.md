---
title: "MQuAKE-Remastered: Multi-Hop Knowledge Editing Can Only Be Advanced with Reliable Evaluations"
authors: ["Shaochen Zhong", "Yifan Lu", "Lize Shao", "Bhargav Bhushanam", "Xiaocong Du", "Yixin Wan", "Yucheng Shi", "Daochen Zha", "Yiwei Wang", "Ninghao Liu", "Kaixiong Zhou", "Shuai Xu", "Kai-Wei Chang", "Louis Feng", "Vipin Chaudhary", "Xia Hu"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "m9wG6ai2Xk"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/fe7f91cc31c4ed473c031ed36b6dc4a28d145c28.pdf"
published: "2025"
categories: []
keywords: ["knowledge edit", "model edit", "multi-hop", "question answering", "natural language processing", "dataset audit"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:09+09:00"
---

# MQuAKE-Remastered: Multi-Hop Knowledge Editing Can Only Be Advanced with Reliable Evaluations

## Abstract
Large language models (LLMs) can give out erroneous answers to factually rooted questions either as a result of undesired training outcomes or simply because the world has moved on after a certain knowledge cutoff date. Under such scenarios, *knowledge editing* often comes to the rescue by delivering efficient patches for such erroneous answers without significantly altering the rest, where many editing methods have seen reasonable success when the editing targets are simple and direct (e.g., *``what club does Lionel Messi currently play for?''*).

However, knowledge fragments like this are often deeply intertwined in the real world, making effectively propagating the editing effect to non-directly related questions a practical challenge (to entertain an extreme example: [*"What car did the wife of the owner of the club that Messi currently plays for used to get to school in the 80s?"*](youtube.com/watch?v=DbwiHC1Fu-E\&t=132s)). Prior arts have coined this task as *multi-hop knowledge editing* with the most popular dataset being MQuAKE, serving as the sole evaluation benchmark for many later proposed editing methods due to the expensive nature of constructing knowledge editing datasets at scale. 

In this work, we reveal that **up to 33\% or 76\% of \mquake{}'s questions and ground truth labels are, in fact, corrupted in various fashions due to some unintentional clerical or procedural oversights**. Our work provides a detailed audit of MQuAKE's error pattern and a comprehensive fix without sacrificing its dataset capacity. Additionally, we benchmarked almost all proposed MQuAKE-evaluated editing methods on our post-fix dataset, **MQuAKE-Remastered**. We observe that many methods try to overfit the original MQuAKE by exploiting some dataset idiosyncrasies of MQuAKE. We provide a guideline on how to approach such datasets faithfully and show that a simple, minimally invasive approach — **GWalk** — can offer beyond SOTA editing performance without such exploitation. The MQuAKE-Remastered datasets and utilities are available at [huggingface.co/datasets/henryzhongsc/MQuAKE-Remastered](https://huggingface.co/datasets/henryzhongsc/MQuAKE-Remastered) and [github.com/henryzhongsc/MQuAKE-Remastered](https://github.com/henryzhongsc/MQuAKE-Remastered), respectively.

## Metadata
- venue: ICLR
- year: 2025
- authors: Shaochen Zhong, Yifan Lu, Lize Shao, Bhargav Bhushanam, Xiaocong Du, Yixin Wan, Yucheng Shi, Daochen Zha, Yiwei Wang, Ninghao Liu, Kaixiong Zhou, Shuai Xu, Kai-Wei Chang, Louis Feng, Vipin Chaudhary, Xia Hu
- arxiv_id: 
- openreview_id: m9wG6ai2Xk
- anthology_id: 
- pdf_url: https://openreview.net/pdf/fe7f91cc31c4ed473c031ed36b6dc4a28d145c28.pdf
- published: 2025
- keywords: knowledge edit, model edit, multi-hop, question answering, natural language processing, dataset audit

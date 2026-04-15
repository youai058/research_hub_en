---
title: "Herald: A Natural Language Annotated Lean 4 Dataset"
authors: ["Guoxiong Gao", "Yutong Wang", "Jiedong Jiang", "Qi Gao", "Zihan Qin", "Tianyi Xu", "Bin Dong"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Se6MgCtRhz"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e85c4d47652d136c15eb27b10a2ab21a5f41919b.pdf"
published: "2025"
categories: []
keywords: ["Lean 4", "Autoformalizing", "LLM", "Retrieval Augmented Generation", "Dataset"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:48+09:00"
---

# Herald: A Natural Language Annotated Lean 4 Dataset

## Abstract
Verifiable formal languages like Lean have profoundly impacted mathematical reasoning, particularly through the use of large language models (LLMs) for automated reasoning. A significant challenge in training LLMs for these formal languages is the lack of parallel datasets that align natural language with formal language proofs. To address this challenge, this paper introduces a novel framework for translating the Mathlib4 corpus (a unified library of mathematics in formal language Lean 4) into natural language. Building upon this, we employ a dual augmentation strategy that combines tactic-based and informal-based approaches, leveraging the Lean-jixia system, a Lean 4 analyzer. We present the results of this pipeline on Mathlib4 as Herald (Hierarchy and Retrieval-based Translated Lean Dataset). We also propose the Herald Translator, which is fine-tuned on Herald. Herald translator achieves a 96.7\% accuracy (Pass@128) on formalizing statements in the miniF2F-test and a 23.5\% accuracy on our internal graduate-level textbook dataset, outperforming InternLM2-Math-Plus-7B (73.0\% and 7.5\%) and TheoremLlama (50.1\% and 4.0\%). Furthermore, we propose a section-level translation framework for real-world applications. As a direct application of Herald translator, we have successfully translated a template section in the Stack project, marking a notable progress in the automatic formalization of graduate-level mathematical literature. Our model, along with the datasets, are open-sourced to the public.

## Metadata
- venue: ICLR
- year: 2025
- authors: Guoxiong Gao, Yutong Wang, Jiedong Jiang, Qi Gao, Zihan Qin, Tianyi Xu, Bin Dong
- arxiv_id: 
- openreview_id: Se6MgCtRhz
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e85c4d47652d136c15eb27b10a2ab21a5f41919b.pdf
- published: 2025
- keywords: Lean 4, Autoformalizing, LLM, Retrieval Augmented Generation, Dataset

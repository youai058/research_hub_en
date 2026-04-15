---
title: "STAMP Your Content: Proving Dataset Membership via Watermarked Rephrasings"
authors: ["Saksham Rastogi", "Pratyush Maini", "Danish Pruthi"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "qF6mxani2X"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/77b2fbf41e73f784d273d228037d6ee0d19a52be.pdf"
published: "2025"
categories: []
keywords: ["LLM", "membership inference", "dataset inference", "watermarking", "test set contamination"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:20+09:00"
---

# STAMP Your Content: Proving Dataset Membership via Watermarked Rephrasings

## Abstract
Given how large parts of publicly available text are crawled to pretrain large language models (LLMs), data creators increasingly worry about the inclusion of their proprietary data for model training without attribution or licensing. Their concerns are also shared by benchmark curators whose test-sets might be compromised. In this paper, we present STAMP, a framework for detecting dataset membership—i.e., determining the inclusion of a dataset in the pretraining corpora of LLMs. Given an original piece of content, our proposal involves first generating multiple rephrases, each embedding a watermark with a unique secret key. One version is to be released publicly, while others are to be kept private. Subsequently, creators can compare model likelihoods between public and private versions using paired statistical tests to prove membership. We show that our framework can successfully detect contamination across four benchmarks which appear only once in the training data and constitute less than 0.001% of the total tokens, outperforming several contamination detection and dataset inference baselines. We verify that STAMP preserves both the semantic meaning and utility of the original data. We apply STAMP to two real-world scenarios to confirm the inclusion of paper abstracts and blog articles in the pretraining corpora.

## Metadata
- venue: ICML
- year: 2025
- authors: Saksham Rastogi, Pratyush Maini, Danish Pruthi
- arxiv_id: 
- openreview_id: qF6mxani2X
- anthology_id: 
- pdf_url: https://openreview.net/pdf/77b2fbf41e73f784d273d228037d6ee0d19a52be.pdf
- published: 2025
- keywords: LLM, membership inference, dataset inference, watermarking, test set contamination

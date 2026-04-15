---
title: "You Only Prune Once: Designing Calibration-Free Model Compression With Policy Learning"
authors: ["Ayan Sengupta", "Siddhant Chaudhary", "Tanmoy Chakraborty"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "5RZoYIT3u6"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a4ec37f08d2849b2cd4d8f203d00b3bf1aa3f16a.pdf"
published: "2025"
categories: []
keywords: ["Model Compression", "Large Language Models", "Structured Pruning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:59+09:00"
---

# You Only Prune Once: Designing Calibration-Free Model Compression With Policy Learning

## Abstract
The ever-increasing size of large language models (LLMs) presents significant challenges for deployment due to their heavy computational and memory requirements. Current model pruning techniques attempt to alleviate these issues by relying heavily on external calibration datasets to determine which parameters to prune or compress, thus limiting their flexibility and scalability across different compression ratios. Moreover, these methods often cause severe performance degradation, particularly in downstream tasks, when subjected to higher compression rates. In this paper, we propose *PruneNet*, a novel model compression method that addresses these limitations by reformulating model pruning as a policy learning process. PruneNet decouples the pruning process from the model architecture, eliminating the need for calibration datasets. It learns a stochastic pruning policy to assess parameter importance solely based on intrinsic model properties while preserving the spectral structure to minimize information loss. PruneNet can compress the LLaMA-2-7B model in just 15 minutes, achieving over 80\% retention of its zero-shot performance with a 30\% compression ratio, outperforming existing methods that retain only 75\% performance. Furthermore, on complex multitask language understanding tasks, PruneNet demonstrates its robustness by preserving up to 80\% performance of the original model, proving itself a superior alternative to conventional structured compression techniques.

## Metadata
- venue: ICLR
- year: 2025
- authors: Ayan Sengupta, Siddhant Chaudhary, Tanmoy Chakraborty
- arxiv_id: 
- openreview_id: 5RZoYIT3u6
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a4ec37f08d2849b2cd4d8f203d00b3bf1aa3f16a.pdf
- published: 2025
- keywords: Model Compression, Large Language Models, Structured Pruning

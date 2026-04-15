---
title: "Unveiling and Harnessing Hidden Attention Sinks: Enhancing Large Language Models without Training through Attention Calibration"
authors: ["Zhongzhi Yu", "Zheng Wang", "Yonggan Fu", "Huihong Shi", "Khalid Shaikh", "Yingyan Celine Lin"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "DLTjFFiuUJ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/40345a383990aaae81fe2b780c09093d87a48e09.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:14+09:00"
---

# Unveiling and Harnessing Hidden Attention Sinks: Enhancing Large Language Models without Training through Attention Calibration

## Abstract
Attention is a fundamental component behind the remarkable achievements of large language models (LLMs). However, our current understanding of the attention mechanism, especially regarding how attention distributions are established, remains limited. Inspired by recent studies that explore the presence of attention sink in the initial token, which receives disproportionately large attention scores despite their lack of semantic importance, this work delves deeper into this phenomenon. We aim to provide a more profound understanding of the existence of attention sinks within LLMs and to uncover ways to enhance the achievable accuracy of LLMs by directly optimizing the attention distributions, without the need for weight finetuning. Specifically, this work begins with comprehensive visualizations of the attention distributions in LLMs during inference across various inputs and tasks. Based on these visualizations, to the best of our knowledge, we are the first to discover that (1) attention sinks occur not only at the start of sequences but also within later tokens of the input, and (2) not all attention sinks have a positive impact on the achievable accuracy of LLMs. Building upon our findings, we propose a training-free Attention Calibration Technique (ACT) that automatically optimizes the attention distributions on the fly during inference in an input-adaptive manner. Extensive experiments validate that ACT consistently enhances the accuracy of various LLMs across different applications. Specifically, ACT achieves an average improvement of up to $7.30\%$ in accuracy across different datasets when applied to Llama-30B.

## Metadata
- venue: ICML
- year: 2024
- authors: Zhongzhi Yu, Zheng Wang, Yonggan Fu, Huihong Shi, Khalid Shaikh, Yingyan Celine Lin
- arxiv_id: 
- openreview_id: DLTjFFiuUJ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/40345a383990aaae81fe2b780c09093d87a48e09.pdf
- published: 2024

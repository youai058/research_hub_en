---
title: "Neuron-Aware Data Selection in Instruction Tuning for Large Language Models"
authors: ["Xin Chen", "Junchao Wu", "Shu Yang", "Runzhe Zhan", "Zeyu Wu", "Min Yang", "Shujian Huang", "Lidia S. Chao", "Derek F. Wong"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "uq6UWRgzMr"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/94b2fb34c4006a1b1b32b3467ba5194ed9fd9429.pdf"
published: "2026"
categories: []
keywords: ["Instruction Tuning", "Data Selection", "Large Language Models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:12+09:00"
---

# Neuron-Aware Data Selection in Instruction Tuning for Large Language Models

## Abstract
Instruction Tuning (IT) has been proven to be an effective approach to unlock the powerful capabilities of large language models (LLMs). 
Recent studies indicate that excessive IT data can degrade LLMs performance, while carefully selecting a small subset of high-quality IT data can significantly enhance their capabilities. Therefore, identifying the most efficient subset data from the IT dataset to effectively develop either specific or general abilities in LLMs has become a critical challenge.
To address this, we propose a novel and efficient framework called Nait. Nait evaluates the impact of IT data on LLMs performance by analyzing the similarity of neuron activation patterns between the IT dataset and the target domain capability. Specifically, Nait captures neuron activation patterns from in-domain datasets of target domain capabilities to construct reusable and transferable neuron activation features. It then evaluates and selects optimal samples based on the similarity between candidate samples and the expected activation features of the target capabilities.
Experimental results show that training on the 10\% Alpaca-GPT4 IT data subset selected by Nait consistently outperforms methods that rely on external advanced models or uncertainty-based features across various tasks. Our findings also reveal the transferability of neuron activation features across different capabilities of LLMs. In particular, IT data with more logical reasoning and programmatic features possesses strong general transferability, enabling models to develop stronger capabilities across multiple tasks, while a stable core subset of data is sufficient to consistently activate fundamental model capabilities and universally improve performance across diverse tasks.

## Metadata
- venue: ICLR
- year: 2026
- authors: Xin Chen, Junchao Wu, Shu Yang, Runzhe Zhan, Zeyu Wu, Min Yang, Shujian Huang, Lidia S. Chao, Derek F. Wong
- arxiv_id: 
- openreview_id: uq6UWRgzMr
- anthology_id: 
- pdf_url: https://openreview.net/pdf/94b2fb34c4006a1b1b32b3467ba5194ed9fd9429.pdf
- published: 2026
- keywords: Instruction Tuning, Data Selection, Large Language Models

---
title: "Bohdi: Heterogeneous LLM Fusion with Automatic Data Exploration"
authors: ["Junqi Gao", "Zhichang Guo", "Dazhi Zhang", "Dong Li", "Runze Liu", "Pengfei Li", "Kai Tian", "Biqing Qi"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "wVxIBvUAlj"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2450ff0c9195847a41ea55365386d55fb6357f6d.pdf"
published: "2025"
categories: []
keywords: ["Heterogeneous Model Fusion", "Large Language Models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:29+09:00"
---

# Bohdi: Heterogeneous LLM Fusion with Automatic Data Exploration

## Abstract
Heterogeneous Large Language Model (LLM) fusion integrates the strengths of multiple source LLMs with different architectures into a target LLM with low computational overhead. While promising, existing methods suffer from two major limitations: 1) **reliance on real data from limited domain** for knowledge fusion, preventing the target LLM from fully acquiring knowledge across diverse domains, and 2) **fixed data allocation proportions** across domains, failing to dynamically adjust according to the target LLM's varying capabilities across domains, leading to a capability imbalance. To overcome these limitations, we propose Bohdi, a synthetic-data-only heterogeneous LLM fusion framework. Through the organization of knowledge domains into a hierarchical tree structure, Bohdi enables automatic domain exploration and multi-domain data generation through multi-model collaboration, thereby comprehensively extracting knowledge from source LLMs. By formalizing domain expansion and data sampling proportion allocation on the knowledge tree as a Hierarchical Multi-Armed Bandit problem, Bohdi leverages the designed DynaBranches mechanism to adaptively adjust sampling proportions based on the target LLM's performance feedback across domains. Integrated with our proposed Introspection-Rebirth (IR) mechanism, DynaBranches dynamically tracks capability shifts during target LLM's updates via Sliding Window Binomial Likelihood Ratio Testing (SWBLRT), further enhancing its online adaptation capability. Comparative experimental results on a comprehensive suite of benchmarks demonstrate that Bohdi significantly outperforms existing baselines on multiple target LLMs, exhibits higher data efficiency, and virtually eliminates the imbalance in the target LLM's capabilities.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Junqi Gao, Zhichang Guo, Dazhi Zhang, Dong Li, Runze Liu, Pengfei Li, Kai Tian, Biqing Qi
- arxiv_id: 
- openreview_id: wVxIBvUAlj
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2450ff0c9195847a41ea55365386d55fb6357f6d.pdf
- published: 2025
- keywords: Heterogeneous Model Fusion, Large Language Models

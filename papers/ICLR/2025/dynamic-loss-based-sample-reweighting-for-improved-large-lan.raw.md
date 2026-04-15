---
title: "Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining"
authors: ["Daouda Sow", "Herbert Woisetschläger", "Saikiran Bulusu", "Shiqiang Wang", "Hans Arno Jacobsen", "Yingbin Liang"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "gU4ZgQNsOC"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c555e59407ab06c1d2bbfabea197b2ebbea4c16c.pdf"
published: "2025"
categories: []
keywords: ["sample reweighing", "large language models", "pretraining"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:08+09:00"
---

# Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining

## Abstract
Pretraining large language models (LLMs) on vast and heterogeneous datasets is crucial for achieving state-of-the-art performance across diverse downstream tasks. However, current training paradigms treat all samples equally, overlooking the importance or relevance of individual samples throughout the training process. Existing reweighting strategies, which primarily focus on group-level data importance, fail to leverage fine-grained instance-level information and do not adapt dynamically to individual sample importance as training progresses. In this paper, we introduce novel algorithms for dynamic, instance-level data reweighting aimed at improving both the efficiency and effectiveness of LLM pretraining. Our methods adjust the weight of each training sample based on its loss value in an online fashion, allowing the model to dynamically focus on more informative or important samples at the current training stage. In particular, our framework allows us to systematically devise reweighting strategies deprioritizing redundant or uninformative data, which we find tend to work best. 
Furthermore, we develop a new theoretical framework for analyzing the impact of loss-based reweighting on the convergence of gradient-based optimization, providing the first formal characterization of how these strategies affect convergence bounds. We empirically validate our approach across a spectrum of tasks, from pretraining 7B and 1.4B parameter LLMs to smaller-scale language models and linear regression problems, demonstrating that our loss-based reweighting approach can lead to faster convergence and significantly improved performance.

## Metadata
- venue: ICLR
- year: 2025
- authors: Daouda Sow, Herbert Woisetschläger, Saikiran Bulusu, Shiqiang Wang, Hans Arno Jacobsen, Yingbin Liang
- arxiv_id: 
- openreview_id: gU4ZgQNsOC
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c555e59407ab06c1d2bbfabea197b2ebbea4c16c.pdf
- published: 2025
- keywords: sample reweighing, large language models, pretraining

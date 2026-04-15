---
title: "IPAD: Inverse Prompt for AI Detection - A Robust and Interpretable LLM-Generated Text Detector"
authors: ["Zheng CHEN", "Yushi Feng", "Jisheng Dang", "Changyang He", "Yue Deng", "Hongxi Pu", "Haoxuan Li", "Bo Li"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "3JoQTGhUzz"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/334c4ba4801e17d429da93ef49f6544171555005.pdf"
published: "2025"
categories: []
keywords: ["AI Detection", "Prompt Inversion", "Large Language Models", "Explainability", "AI Safety"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:44+09:00"
---

# IPAD: Inverse Prompt for AI Detection - A Robust and Interpretable LLM-Generated Text Detector

## Abstract
Large Language Models (LLMs) have attained human-level fluency in text generation, which complicates the distinguishing between human-written and LLM generated texts. This increases the risk of misuse and highlights the need for reliable detectors. Yet, existing detectors exhibit poor robustness on out-of-distribution (OOD) data and attacked data, which is critical for real-world scenarios. Also, they struggle to provide interpretable evidence to support their decisions, thus undermining reliability. In light of these challenges, we propose IPAD (Inverse Prompt for AI Detection), a novel framework consisting of a Prompt Inverter that identifies predicted prompts that could have generated the input text, and two Distinguishers that examine the probability that the input texts align with the predicted prompts. Empirical evaluations demonstrate that IPAD outperforms the strongest baselines by 9.05% (Average Recall) on in-distribution data, 12.93% (AUROC) on out-of-distribution (OOD) data, and 5.48% (AUROC) on attacked data. IPAD also performs robust on structured datasets. Furthermore, an interpretability assessment is conducted to illustrate that IPAD enhances the AI detection trustworthiness by allowing users to directly examine the decision-making evidence, which provides interpretable support for its state-of-the-art detection results.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Zheng CHEN, Yushi Feng, Jisheng Dang, Changyang He, Yue Deng, Hongxi Pu, Haoxuan Li, Bo Li
- arxiv_id: 
- openreview_id: 3JoQTGhUzz
- anthology_id: 
- pdf_url: https://openreview.net/pdf/334c4ba4801e17d429da93ef49f6544171555005.pdf
- published: 2025
- keywords: AI Detection, Prompt Inversion, Large Language Models, Explainability, AI Safety

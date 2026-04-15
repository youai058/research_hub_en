---
title: "Scalable Multilingual Multimodal Machine Translation with Speech-Text Fusion"
authors: ["Yexing Du", "Youcheng Pan", "Zekun Wang", "Zheng Chu", "Yichong Huang", "Kaiyuan Liu", "Bo Yang", "Yang Xiang", "Ming Liu", "Bing Qin"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "HQMVRQUEaM"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f131e0ffedb813e966604690fcb85464423a3715.pdf"
published: "2026"
categories: []
keywords: ["Speech", "Multimodal Machine Translation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:26+09:00"
---

# Scalable Multilingual Multimodal Machine Translation with Speech-Text Fusion

## Abstract
Multimodal Large Language Models (MLLMs) have achieved notable success in enhancing translation performance by integrating multimodal information.
However, existing research primarily focuses on image-guided methods, whose applicability is constrained by the scarcity of multilingual image-text pairs.
The speech modality overcomes this limitation due to its natural alignment with text and the abundance of existing speech datasets, which enable scalable language coverage.
In this paper, we propose a Speech-guided Machine Translation (SMT) framework that integrates speech and text as fused inputs into an MLLM to improve translation quality.
To mitigate reliance on low-resource data, we introduce a Self-Evolution Mechanism.
The core components of this framework include a text-to-speech model, responsible for generating synthetic speech, and an MLLM capable of classifying synthetic speech samples and iteratively optimizing itself using positive samples.
Experimental results demonstrate that our framework surpasses all existing methods on the Multi30K multimodal machine translation benchmark, achieving new state-of-the-art results.
Furthermore, on general machine translation datasets, particularly the FLORES-200, it achieves average state-of-the-art performance in 108 translation directions. Ablation studies on CoVoST-2 confirms that differences between synthetic and authentic speech have negligible impact on translation quality. The code and models are released at https://github.com/yxduir/LLM-SRT.

## Metadata
- venue: ICLR
- year: 2026
- authors: Yexing Du, Youcheng Pan, Zekun Wang, Zheng Chu, Yichong Huang, Kaiyuan Liu, Bo Yang, Yang Xiang, Ming Liu, Bing Qin
- arxiv_id: 
- openreview_id: HQMVRQUEaM
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f131e0ffedb813e966604690fcb85464423a3715.pdf
- published: 2026
- keywords: Speech, Multimodal Machine Translation

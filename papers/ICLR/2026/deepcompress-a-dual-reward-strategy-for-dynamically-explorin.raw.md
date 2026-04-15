---
title: "DeepCompress: A Dual Reward Strategy for Dynamically Exploring and Compressing Reasoning Chains"
authors: ["Tian Liang", "Wenxiang Jiao", "Zhiwei He", "Jiahao Xu", "Haitao Mi", "Dong Yu"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "K5A2jBmEBK"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/bdbb8cb8f4b159aa5559325eb4bebd5a646aa2c6.pdf"
published: "2026"
categories: []
keywords: ["Large Reasoning Models", "Reasoning Efficiency", "Reinforcement Learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:19+09:00"
---

# DeepCompress: A Dual Reward Strategy for Dynamically Exploring and Compressing Reasoning Chains

## Abstract
Large Reasoning Models (LRMs) have demonstrated impressive capabilities but suffer from cognitive inefficiencies like ''overthinking'' simple problems and ''underthinking'' complex ones. While existing methods that use supervised fine-tuning (SFT) or reinforcement learning (RL) with token-length rewards can improve efficiency, they often do so at the cost of accuracy. This paper introduces DeepCompress, a novel framework that simultaneously enhances both the accuracy and efficiency of LRMs. We challenge the prevailing approach of consistently favoring shorter reasoning paths, showing that longer responses can contain a broader range of correct solutions for difficult problems. DeepCompress employs an adaptive length reward mechanism that dynamically classifies problems as "Simple" or "Hard" in real-time based on the model's evolving capability. It encourages shorter, more efficient reasoning for "Simple" problems while promoting longer, more exploratory thought chains for "Hard" problems. This dual-reward strategy enables the model to autonomously adjust its Chain-of-Thought (CoT) length, compressing reasoning for well-mastered problems and extending it for those it finds challenging. Experimental results on challenging mathematical benchmarks show that DeepCompress consistently outperforms baseline methods, achieving superior accuracy while significantly improving token efficiency.

## Metadata
- venue: ICLR
- year: 2026
- authors: Tian Liang, Wenxiang Jiao, Zhiwei He, Jiahao Xu, Haitao Mi, Dong Yu
- arxiv_id: 
- openreview_id: K5A2jBmEBK
- anthology_id: 
- pdf_url: https://openreview.net/pdf/bdbb8cb8f4b159aa5559325eb4bebd5a646aa2c6.pdf
- published: 2026
- keywords: Large Reasoning Models, Reasoning Efficiency, Reinforcement Learning

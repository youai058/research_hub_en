---
title: "Video Action Differencing"
authors: ["James Burgess", "Xiaohan Wang", "Yuhui Zhang", "Anita Rau", "Alejandro Lozano", "Lisa Dunlap", "Trevor Darrell", "Serena Yeung-Levy"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "3bcN6xlO6f"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/102482b5babaacddfd916de17bda7c15b2020db5.pdf"
published: "2025"
categories: []
keywords: ["Video", "Actions", "Differencing", "Zero-shot", "benchmark", "multimodal", "lmm", "llm"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:41+09:00"
---

# Video Action Differencing

## Abstract
How do two individuals differ when performing the same action? In this work, we introduce Video Action Differencing (VidDiff), the novel task of identifying subtle differences between videos of the same action, which has numerous applications, such as coaching and skill learning. To enable development on this new task, we first create VidDiffBench, a benchmark dataset containing 549 video pairs, with human annotations of 4,469 fine-grained action differences and 2,075 timestamps indicating where these differences occur. Our experiments demonstrate that VidDiffBench poses a significant challenge for state-of-the-art large multimodal models (LMMs), such as GPT-4o and Qwen2-VL. By analyzing the failure cases of LMMs on VidDiffBench, we highlight two key challenges for this task: localizing relevant sub-actions over two videos and fine-grained frame comparison. To overcome these, we propose the VidDiff method, an agentic workflow that breaks the task into three stages: action difference proposal, keyframe localization, and frame differencing, each stage utilizing specialized foundation models. To encourage future research in this new task, we release the benchmark and code.

## Metadata
- venue: ICLR
- year: 2025
- authors: James Burgess, Xiaohan Wang, Yuhui Zhang, Anita Rau, Alejandro Lozano, Lisa Dunlap, Trevor Darrell, Serena Yeung-Levy
- arxiv_id: 
- openreview_id: 3bcN6xlO6f
- anthology_id: 
- pdf_url: https://openreview.net/pdf/102482b5babaacddfd916de17bda7c15b2020db5.pdf
- published: 2025
- keywords: Video, Actions, Differencing, Zero-shot, benchmark, multimodal, lmm, llm

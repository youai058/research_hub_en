---
title: "ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification"
authors: ["Hyunseok Lee", "Seunghyuk Oh", "Jaehyung Kim", "Jinwoo Shin", "Jihoon Tack"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "cBtsxtJqEK"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/52f22a929b2b4c4f7e021a6b49ea98593fdbd41c.pdf"
published: "2025"
categories: []
keywords: ["Self-correct", "Test-time compute", "Large Language Model", "Self-verify", "Self-awareness"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:37+09:00"
---

# ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification

## Abstract
Self-awareness, i.e., the ability to assess and correct one's generation, is a fundamental aspect of human intelligence, making its replication in large language models (LLMs) an important yet challenging task. Previous works tackle this by employing extensive reinforcement learning or relying on large external verifiers. In this work, we propose Refine via Intrinsic Self-Verification (ReVISE), an efficient and effective framework that enables LLMs to self-correct their outputs through self-verification. The core idea of ReVISE is to enable LLMs to verify their reasoning processes and continually rethink reasoning trajectories based on its verification. To implement this efficiently, we introduce a structured curriculum based on preference learning. Specifically, as ReVISE involves two challenging tasks (i.e., self-verification and reasoning correction), we tackle each task sequentially using curriculum learning, collecting both failed and successful reasoning paths to construct preference pairs for efficient training. During inference, our approach enjoys natural test-time scaling by integrating self-verification and correction capabilities, further enhanced by our proposed confidence-aware decoding mechanism. Our experiments on various reasoning tasks demonstrate that ReVISE achieves efficient self-correction and significantly improves the reasoning performance of LLMs.

## Metadata
- venue: ICML
- year: 2025
- authors: Hyunseok Lee, Seunghyuk Oh, Jaehyung Kim, Jinwoo Shin, Jihoon Tack
- arxiv_id: 
- openreview_id: cBtsxtJqEK
- anthology_id: 
- pdf_url: https://openreview.net/pdf/52f22a929b2b4c4f7e021a6b49ea98593fdbd41c.pdf
- published: 2025
- keywords: Self-correct, Test-time compute, Large Language Model, Self-verify, Self-awareness

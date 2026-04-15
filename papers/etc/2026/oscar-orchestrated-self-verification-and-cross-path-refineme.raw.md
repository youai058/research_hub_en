---
title: "OSCAR: Orchestrated Self-verification and Cross-path Refinement"
authors: ["Yash Shah", "Abhijit Chakraborty", "Naresh Kumar Devulapally", "Vishnu Lokhande", "Vivek Gupta"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2604.01624"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2604.01624v2"
published: "2026-04-02"
categories: ["cs.AI", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:13:54+09:00"
---

# OSCAR: Orchestrated Self-verification and Cross-path Refinement

## Abstract
Diffusion language models (DLMs) expose their denoising trajectories, offering a natural handle for inference-time control; accordingly, an ideal hallucination mitigation framework should intervene during generation using this model-native signal rather than relying on an externally trained hallucination classifier. Toward this, we formulate commitment uncertainty localization: given a denoising trajectory, identify token positions whose cross-chain entropy exceeds an unsupervised threshold before factually unreliable commitments propagate into self-consistent but incorrect outputs. We introduce a suite of trajectory-level assessments, including a cross-chain divergence-at-hallucination (CDH) metric, for principled comparison of localization methods. We also introduce OSCAR, a training-free inference-time framework operationalizing this formulation. OSCAR runs N parallel denoising chains with randomized reveal orders, computes cross-chain Shannon entropy to detect high-uncertainty positions, and then performs targeted remasking conditioned on retrieved evidence. Ablations confirm that localization and correction contribute complementary gains, robust across N in {4, 8, 16}. On TriviaQA, HotpotQA, RAGTruth, and CommonsenseQA using LLaDA-8B and Dream-7B, OSCAR enhances generation quality by significantly reducing hallucinated content and improving factual accuracy through uncertainty-guided remasking, which also facilitates more effective integration of retrieved evidence. Its native entropy-based uncertainty signal surpasses that of specialized trained detectors, highlighting an inherent capacity of diffusion language models to identify factual uncertainty that is not present in the sequential token commitment structure of autoregressive models.

## Metadata
- venue: arXiv
- year: 2026
- authors: Yash Shah, Abhijit Chakraborty, Naresh Kumar Devulapally, Vishnu Lokhande, Vivek Gupta
- arxiv_id: 2604.01624
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2604.01624v2
- published: 2026-04-02

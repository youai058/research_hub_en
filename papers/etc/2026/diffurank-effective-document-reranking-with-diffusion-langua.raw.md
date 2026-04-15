---
title: "DiffuRank: Effective Document Reranking with Diffusion Language Models"
authors: ["Qi Liu", "Kun Ai", "Jiaxin Mao", "Yanzhao Zhang", "Mingxin Li", "Dingkun Long", "Pengjun Xie", "Fengbin Zhu", "Ji-Rong Wen"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.12528"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.12528v1"
published: "2026-02-13"
categories: ["cs.IR", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:02+09:00"
---

# DiffuRank: Effective Document Reranking with Diffusion Language Models

## Abstract
Recent advances in large language models (LLMs) have inspired new paradigms for document reranking. While this paradigm better exploits the reasoning and contextual understanding capabilities of LLMs, most existing LLM-based rerankers rely on autoregressive generation, which limits their efficiency and flexibility. In particular, token-by-token decoding incurs high latency, while the fixed left-to-right generation order causes early prediction errors to propagate and is difficult to revise. To address these limitations, we explore the use of diffusion language models (dLLMs) for document reranking and propose DiffuRank, a reranking framework built upon dLLMs. Unlike autoregressive models, dLLMs support more flexible decoding and generation processes that are not constrained to a left-to-right order, and enable parallel decoding, which may lead to improved efficiency and controllability. Specifically, we investigate three reranking strategies based on dLLMs: (1) a pointwise approach that uses dLLMs to estimate the relevance of each query-document pair; (2) a logit-based listwise approach that prompts dLLMs to jointly assess the relevance of multiple documents and derives ranking lists directly from model logits; and (3) a permutation-based listwise approach that adapts the canonical decoding process of dLLMs to the reranking tasks. For each approach, we design corresponding training methods to fully exploit the advantages of dLLMs. We evaluate both zero-shot and fine-tuned reranking performance on multiple benchmarks. Experimental results show that dLLMs achieve performance comparable to, and in some cases exceeding, that of autoregressive LLMs with similar model sizes. These findings demonstrate the promise of diffusion-based language models as a compelling alternative to autoregressive architectures for document reranking.

## Metadata
- venue: arXiv
- year: 2026
- authors: Qi Liu, Kun Ai, Jiaxin Mao, Yanzhao Zhang, Mingxin Li, Dingkun Long, Pengjun Xie, Fengbin Zhu, Ji-Rong Wen
- arxiv_id: 2602.12528
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.12528v1
- published: 2026-02-13

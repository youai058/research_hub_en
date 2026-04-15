---
title: "Chain of Thought Empowers Transformers to Solve Inherently Serial Problems"
authors: ["Zhiyuan Li", "Hong Liu", "Denny Zhou", "Tengyu Ma"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "3EWTEy9MTM"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2c3e913d1014164603f487f70dace6570bb0a1d0.pdf"
published: "2024"
categories: []
keywords: ["Chain of thought", "language modeling", "circuit complexity", "deep learning theory"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:12+09:00"
---

# Chain of Thought Empowers Transformers to Solve Inherently Serial Problems

## Abstract
Generating a sequence of intermediate steps, \emph{a.k.a.}, a chain of thought (CoT), is a highly effective method to improve the accuracy of large language models (LLMs) on arithmetics and symbolic reasoning tasks. However, the mechanism behind CoT remains unclear. 
This work provides a theoretical understanding of the power of CoT for decoder-only transformers through the lens of expressiveness. Conceptually, CoT empowers the model with the ability to perform inherently serial computation, which is otherwise lacking in transformers, especially when depth is low. Given input length $n$, previous works have constant-depth transformers with finite precision $\mathsf{poly}(n)$ embedding size can only solve problems in $\mathsf{TC}^0$ without CoT. We first show an even tighter expressiveness upper bound for constant-depth transformers with constant-bit precision, which can only solve problems in $\mathsf{AC}^0$, a proper subset of $ \mathsf{TC}^0$. However, with $T$ steps of CoT, constant-depth transformers using constant-bit precision and $O(\log n)$ embedding size can solve any problem solvable by boolean circuits of size $T$. Empirically, enabling CoT dramatically improves the accuracy for tasks that are hard for parallel computation, including the composition of permutation groups, iterated squaring, and circuit value problems, especially for low-depth transformers.

## Metadata
- venue: ICLR
- year: 2024
- authors: Zhiyuan Li, Hong Liu, Denny Zhou, Tengyu Ma
- arxiv_id: 
- openreview_id: 3EWTEy9MTM
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2c3e913d1014164603f487f70dace6570bb0a1d0.pdf
- published: 2024
- keywords: Chain of thought, language modeling, circuit complexity, deep learning theory

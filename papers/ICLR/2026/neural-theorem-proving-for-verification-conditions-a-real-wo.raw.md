---
title: "Neural Theorem Proving for Verification Conditions: A Real-World Benchmark"
authors: ["Qiyuan Xu", "Xiaokun Luan", "Renxi Wang", "Joshua Ong Jun Leang", "Peixin Wang", "Haonan Li", "Wenda Li", "Conrad Watt"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "MfDyickxQA"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/87b904ec7ddbd16d69c16e4e16002feef63ba109.pdf"
published: "2026"
categories: []
keywords: ["Neural Theorem Proving", "Program Verification", "AI for Verification", "Automated Theorem Proving", "Lean", "Isabelle", "Rocq"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:46+09:00"
---

# Neural Theorem Proving for Verification Conditions: A Real-World Benchmark

## Abstract
Theorem proving is fundamental to program verification, where the automated proof of Verification Conditions (VCs) remains a primary bottleneck. Real-world program verification frequently encounters hard VCs that existing Automated Theorem Provers cannot prove, leading to a critical need for extensive manual proofs that burden practical application. While Neural Theorem Proving (NTP) has achieved significant success in mathematical competitions, demonstrating the potential of machine learning approaches to formal reasoning, its application to program verification—particularly VC proving—remains largely unexplored. 
Despite existing work on annotation synthesis and verification-related theorem proving, no benchmark has specifically targeted this fundamental bottleneck: automated VC proving.
This work introduces Neural Theorem Proving for Verification Conditions (NTP4VC) and presents the first real-world multi-lingual benchmark for this task. Specifically, from real-world projects such as Linux and Contiki-OS kernel, our benchmark leverages industrial pipelines (Why3 and Frama-C) to generate semantically equivalent test cases across formal languages of Isabelle, Lean, and Rocq. We evaluate large language models (LLMs), both general-purpose and those fine-tuned for theorem proving, on NTP4VC. Results indicate that although LLMs show promise in VC proving, significant challenges remain for program verification, highlighting a large gap and opportunity for future research.

## Metadata
- venue: ICLR
- year: 2026
- authors: Qiyuan Xu, Xiaokun Luan, Renxi Wang, Joshua Ong Jun Leang, Peixin Wang, Haonan Li, Wenda Li, Conrad Watt
- arxiv_id: 
- openreview_id: MfDyickxQA
- anthology_id: 
- pdf_url: https://openreview.net/pdf/87b904ec7ddbd16d69c16e4e16002feef63ba109.pdf
- published: 2026
- keywords: Neural Theorem Proving, Program Verification, AI for Verification, Automated Theorem Proving, Lean, Isabelle, Rocq

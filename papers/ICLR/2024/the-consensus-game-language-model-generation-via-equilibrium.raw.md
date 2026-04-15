---
title: "The Consensus Game: Language Model Generation via Equilibrium Search"
authors: ["Athul Paul Jacob", "Yikang Shen", "Gabriele Farina", "Jacob Andreas"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "n9xeGcI4Yg"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6a766aa0bf6a7a4f5d339309db677987d04377ce.pdf"
published: "2024"
categories: []
keywords: ["language models", "decoding", "planning", "game theory"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:12+09:00"
---

# The Consensus Game: Language Model Generation via Equilibrium Search

## Abstract
When applied to question answering and other text generation tasks, language models (LMs) may be queried generatively (by sampling answers from their output distribution) or discriminatively (by using them to score or rank a set of candidate answers). These procedures sometimes yield very different predictions. How do we reconcile mutually incompatible scoring procedures to obtain coherent LM predictions? We introduce a new, a training-free, game-theoretic procedure for language model decoding. Our approach casts language model decoding as a regularized imperfect-information sequential signaling game—which we term the concensus game—in which a generator seeks to communicate an abstract correctness parameter using natural language sentences to a discriminator. We develop computational procedures for finding approximate equilibria of this game, resulting in a decoding algorithm we call equilibrium-ranking. Applied to a large number of tasks (including reading comprehension, commonsense reasoning, mathematical problem-solving, and assistive dialog), equilibrium-ranking consistently improves performance over existing LM decoding procedures. These improvements are sometimes substantial—on multiple benchmarks, we observe that applying equilibrium-ranking to LLaMA-7B outperforms the much larger LLaMA-65B and PaLM-540B models.

## Metadata
- venue: ICLR
- year: 2024
- authors: Athul Paul Jacob, Yikang Shen, Gabriele Farina, Jacob Andreas
- arxiv_id: 
- openreview_id: n9xeGcI4Yg
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6a766aa0bf6a7a4f5d339309db677987d04377ce.pdf
- published: 2024
- keywords: language models, decoding, planning, game theory

---
title: "Stop the Flip-Flop: Context-Preserving Verification for Fast Revocable Diffusion Decoding"
authors: ["Yanzheng Xiang", "Lan Wei", "Yizhen Yao", "Qinglin Zhu", "Hanqi Yan", "Chen Jin", "Philip Alexander Teare", "Dandan Zhang", "Lin Gui", "Amrutha Saseendran", "Yulan He"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.06161"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.06161v1"
published: "2026-02-05"
categories: ["cs.CL", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:05+09:00"
---

# Stop the Flip-Flop: Context-Preserving Verification for Fast Revocable Diffusion Decoding

## Abstract
Parallel diffusion decoding can accelerate diffusion language model inference by unmasking multiple tokens per step, but aggressive parallelism often harms quality. Revocable decoding mitigates this by rechecking earlier tokens, yet we observe that existing verification schemes frequently trigger flip-flop oscillations, where tokens are remasked and later restored unchanged. This behaviour slows inference in two ways: remasking verified positions weakens the conditioning context for parallel drafting, and repeated remask cycles consume the revision budget with little net progress. We propose COVER (Cache Override Verification for Efficient Revision), which performs leave-one-out verification and stable drafting within a single forward pass. COVER constructs two attention views via KV cache override: selected seeds are masked for verification, while their cached key value states are injected for all other queries to preserve contextual information, with a closed form diagonal correction preventing self leakage at the seed positions. COVER further prioritises seeds using a stability aware score that balances uncertainty, downstream influence, and cache drift, and it adapts the number of verified seeds per step. Across benchmarks, COVER markedly reduces unnecessary revisions and yields faster decoding while preserving output quality.

## Metadata
- venue: arXiv
- year: 2026
- authors: Yanzheng Xiang, Lan Wei, Yizhen Yao, Qinglin Zhu, Hanqi Yan, Chen Jin, Philip Alexander Teare, Dandan Zhang, Lin Gui, Amrutha Saseendran, Yulan He
- arxiv_id: 2602.06161
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.06161v1
- published: 2026-02-05

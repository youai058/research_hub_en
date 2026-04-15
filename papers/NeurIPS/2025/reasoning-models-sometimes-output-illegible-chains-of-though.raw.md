---
title: "Reasoning Models Sometimes Output Illegible Chains of Thought"
authors: ["Arun Jose"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "w1TjXJk846"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/05e549afc051441256cf30951d01249a053c7ab0.pdf"
published: "2025"
categories: []
keywords: ["Reasoning Models Sometimes Output Illegible Chains of Thought"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:29+09:00"
---

# Reasoning Models Sometimes Output Illegible Chains of Thought

## Abstract
Language models trained via outcome-based reinforcement learning (RL) to reason using chain-of-thought (CoT) have shown remarkable performance. Monitoring such a model's CoT may allow us to understand its intentions and detect potential malicious behavior. However, to be effective, this requires that CoTs are legible and faithful. We evaluate the legibility of CoTs in state-of-the-art reasoning models. We find that R1, R1-Zero, and QwQ often produce illegible CoTs (mixing nonsensical phrases, random words, and non-English characters) before returning to perfect coherence in their final responses, while Claude models notably exhibit higher legibility. Across 14 models, we observe that larger models within the same training paradigm tend to produce more illegible reasoning. Prefill experiments show that truncating reasoning at a legibility threshold reduces accuracy by 53\%, suggesting that illegible portions contribute to performance despite being difficult to monitor. Illegibility increases with question difficulty, suggesting that CoT monitoring may be less reliable precisely when most needed. We discuss potential hypotheses for these results, including steganography, vestigial tokens, and training artifacts. Our findings suggest that current approaches to CoT monitoring may be vulnerable to the emergence of outcome-based RL, particularly as models face increasingly complex tasks.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Arun Jose
- arxiv_id: 
- openreview_id: w1TjXJk846
- anthology_id: 
- pdf_url: https://openreview.net/pdf/05e549afc051441256cf30951d01249a053c7ab0.pdf
- published: 2025
- keywords: Reasoning Models Sometimes Output Illegible Chains of Thought

---
title: "Causal Order: The Key to Leveraging Imperfect Experts in Causal Inference"
authors: ["Aniket Vashishtha", "Abbavaram Gowtham Reddy", "Abhinav Kumar", "Saketh Bachu", "Vineeth N. Balasubramanian", "Amit Sharma"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "9juyeCqL0u"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/19538e9c6965f0b37491c400db41cbc256d992c2.pdf"
published: "2025"
categories: []
keywords: ["Causal Order", "Imperfect Experts", "Causal Inference", "LLMs"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:17+09:00"
---

# Causal Order: The Key to Leveraging Imperfect Experts in Causal Inference

## Abstract
Large Language Models (LLMs) have recently been used as experts to infer causal graphs, often by repeatedly applying a pairwise prompt that asks about the causal relationship of each variable pair. However, such experts, including human domain experts, cannot distinguish between direct and indirect effects given a pairwise prompt. Therefore, instead of the graph, we propose that causal order be used as a more stable output interface for utilizing expert knowledge. When querying a perfect expert with a pairwise prompt, we show that the inferred graph can have significant errors whereas the causal order is always correct. In practice, however, LLMs are imperfect experts and we find that pairwise prompts lead to multiple cycles and do not yield a valid order. Hence, we propose a prompting strategy that introduces an auxiliary variable for every variable pair and instructs the LLM to avoid cycles within this triplet. We show, both theoretically and empirically, that such a triplet prompt leads to fewer cycles than the pairwise prompt. Across multiple real-world graphs, the triplet prompt yields a more accurate order using both LLMs and human annotators as experts. By querying the expert with different auxiliary variables for the same variable pair, it also increases robustness---triplet method with much smaller models such as Phi-3 and Llama-3 8B outperforms a pairwise prompt with GPT-4. For practical usage, we show how the estimated causal order from the triplet method  can be used to reduce error in downstream discovery and effect inference tasks.

## Metadata
- venue: ICLR
- year: 2025
- authors: Aniket Vashishtha, Abbavaram Gowtham Reddy, Abhinav Kumar, Saketh Bachu, Vineeth N. Balasubramanian, Amit Sharma
- arxiv_id: 
- openreview_id: 9juyeCqL0u
- anthology_id: 
- pdf_url: https://openreview.net/pdf/19538e9c6965f0b37491c400db41cbc256d992c2.pdf
- published: 2025
- keywords: Causal Order, Imperfect Experts, Causal Inference, LLMs

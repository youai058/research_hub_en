---
title: "Rapid Selection and Ordering of In-Context Demonstrations via Prompt Embedding Clustering"
authors: ["Kha Pham", "Hung Le", "Man Ngo", "Truyen Tran"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "1Iu2Yte5N6"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/5cec8d826e3c9e64289a5798fbe936ce23a51973.pdf"
published: "2025"
categories: []
keywords: ["in-context learning", "order sensitivity", "LLMs", "clustering", "cluster-based search", "positional encoding", "attention mask", "serial-position effect", "cluster-based search"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:50+09:00"
---

# Rapid Selection and Ordering of In-Context Demonstrations via Prompt Embedding Clustering

## Abstract
While Large Language Models (LLMs) excel at in-context learning (ICL) using just a few demonstrations, their performances are sensitive to demonstration orders. The reasons behind this sensitivity remain poorly understood. In this paper, we investigate the prompt embedding space to bridge the gap between the order sensitivity of ICL with inner workings of decoder-only LLMs, uncovering the clustering property: prompts sharing the first and last demonstrations have closer embeddings, with first-demonstration clustering usually being stronger in practice. We explain this property through extensive theoretical analyses and empirical evidences. Our finding suggests that the positional encoding and the causal attention mask are key contributors to the clustering phenomenon. Leveraging this clustering insight, we introduce Cluster-based Search, a novel method that accelerates the selection and ordering of demonstrations in self-adaptive ICL settings. Our approach substantially decreases the time complexity from factorial to quadratic, saving 92% to nearly 100% execution time while maintaining comparable performance to exhaustive search.

## Metadata
- venue: ICLR
- year: 2025
- authors: Kha Pham, Hung Le, Man Ngo, Truyen Tran
- arxiv_id: 
- openreview_id: 1Iu2Yte5N6
- anthology_id: 
- pdf_url: https://openreview.net/pdf/5cec8d826e3c9e64289a5798fbe936ce23a51973.pdf
- published: 2025
- keywords: in-context learning, order sensitivity, LLMs, clustering, cluster-based search, positional encoding, attention mask, serial-position effect, cluster-based search

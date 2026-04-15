---
title: "Tree Reward-Aligned Search for TReASURe in Masked Diffusion Language Models"
authors: ["Zichao Yu", "Ming Li", "Wenyi Zhang", "Weiguo Gao"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2509.23146"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2509.23146v1"
published: "2025-09-27"
categories: ["cs.CL", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:14+09:00"
---

# Tree Reward-Aligned Search for TReASURe in Masked Diffusion Language Models

## Abstract
Tree search has recently emerged as a powerful framework for aligning generative models with task-specific rewards at test time. Applying tree search to Masked Diffusion Language Models, however, introduces two key challenges: (i) parallel unmasking yields highly correlated branches, limiting exploration, and (ii) reward evaluation via sampled completions produces high-variance estimates, making pruning unstable. We propose TReASURe, a tree-search test-time alignment method that addresses these issues. It introduces (i) UnmaskBranch, a branching strategy based on first-hitting unmasking that diversifies both token content and reveal order with a single model call per parent node, and (ii) ResubstituteScore, a pruning rule that uses deterministic resubstitution to score partially masked sequences with low-variance proxy completions. Theoretically, we quantify branching efficiency gains in NFEs (number of function evaluations), show that the scoring rule approximates the true reward with error bounded by predictive uncertainty, and prove improvements with larger tree widths. Empirically, TReASURe achieves state-of-the-art results on perplexity, linguistic acceptability, and control of sentiment and toxicity, outperforming prior methods under matched compute budgets, with especially strong gains in low-NFE regimes.

## Metadata
- venue: arXiv
- year: 2025
- authors: Zichao Yu, Ming Li, Wenyi Zhang, Weiguo Gao
- arxiv_id: 2509.23146
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2509.23146v1
- published: 2025-09-27

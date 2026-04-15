---
title: "Importance Sampling for Multi-Negative Multimodal Direct Preference Optimization"
authors: ["Xintong Li", "Chuhan Wang", "Junda Wu", "Rohan Surana", "Tong Yu", "Julian McAuley", "Jingbo Shang"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "HEFPwoGtTj"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/43d70e32e570f77cef2ff55761b2e425f561e7d0.pdf"
published: "2026"
categories: []
keywords: ["Multimodal", "Importance Sampling", "Direct Preference Optimization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:34+09:00"
---

# Importance Sampling for Multi-Negative Multimodal Direct Preference Optimization

## Abstract
Direct Preference Optimization (DPO) has recently been extended from text-only models to vision-language models. However, existing methods rely on oversimplified pairwise comparisons, generating a single negative image via basic perturbations or similarity-based retrieval, which fail to capture the complex nature of multimodal preferences, inducing optimization bias and hallucinations. To address this issue, we propose MISP-DPO, the first framework to incorporate \emph{multiple}, semantically \emph{diverse} negative images in multimodal DPO via the Plackett-Luce model. Our method embeds prompts and candidate images in CLIP (Contrastive Language–Image Pre-training) space and applies a sparse autoencoder to uncover semantic deviations into interpretable factors. Negative samples are selected based on reconstruction difficulty, semantic deviation from the positive, and mutual diversity, yielding broader and more informative supervision. To handle multi-negative comparisons, we adopt a Plackett–Luce objective and introduce an importance sampling strategy that improves training efficiency. Experiments across five diverse benchmarks demonstrate that MISP-DPO consistently improves multimodal alignment over prior methods, validating the effectiveness of semantic-aware, multi-negative sampling in preference-based learning.

## Metadata
- venue: ICLR
- year: 2026
- authors: Xintong Li, Chuhan Wang, Junda Wu, Rohan Surana, Tong Yu, Julian McAuley, Jingbo Shang
- arxiv_id: 
- openreview_id: HEFPwoGtTj
- anthology_id: 
- pdf_url: https://openreview.net/pdf/43d70e32e570f77cef2ff55761b2e425f561e7d0.pdf
- published: 2026
- keywords: Multimodal, Importance Sampling, Direct Preference Optimization

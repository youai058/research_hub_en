---
title: "Achievable distributional robustness when the robust risk is only partially identified"
authors: ["Julia Kostin", "Nicola Gnecco", "Fanny Yang"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "G2dYZJO4BE"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f0a97354a32a4d2740af16644da6aca758f5c318.pdf"
published: "2024"
categories: []
keywords: ["distributional robustness", "domain generalization", "causal inference", "partial identification"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:53+09:00"
---

# Achievable distributional robustness when the robust risk is only partially identified

## Abstract
In safety-critical applications, machine learning models should generalize well under worst-case distribution shifts, that is, have a small robust risk. Invariance-based algorithms can provably take advantage of structural assumptions on the shifts when the training distributions are heterogeneous enough to identify the robust risk. However, in practice, such identifiability conditions are rarely satisfied – a scenario so far underexplored in the theoretical literature. In this paper, we aim to fill the gap and propose to study the more general setting of partially identifiable robustness. In particular, we define a new risk measure, the identifiable robust risk, and its corresponding (population) minimax quantity that is an algorithm-independent measure for the best achievable robustness under partial identifiability. We introduce these concepts broadly, and then study them within the framework of linear structural causal models for concreteness of the presentation. We use the introduced minimax quantity to show how previous approaches provably achieve suboptimal robustness in the partially identifiable case. We confirm our findings through empirical simulations and real-world experiments and demonstrate how the test error of existing robustness methods grows increasingly suboptimal as the proportion of previously unseen test directions increases.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Julia Kostin, Nicola Gnecco, Fanny Yang
- arxiv_id: 
- openreview_id: G2dYZJO4BE
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f0a97354a32a4d2740af16644da6aca758f5c318.pdf
- published: 2024
- keywords: distributional robustness, domain generalization, causal inference, partial identification

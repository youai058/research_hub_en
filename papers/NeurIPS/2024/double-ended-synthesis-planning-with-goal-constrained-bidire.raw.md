---
title: "Double-Ended Synthesis Planning with Goal-Constrained Bidirectional Search"
authors: ["Kevin Yu", "Jihye Roh", "Ziang Li", "Wenhao Gao", "Runzhong Wang", "Connor W. Coley"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "LJNqVIKSCr"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/28a84c7beddeea0844e294d5a0ccea7ea6314dc5.pdf"
published: "2024"
categories: []
keywords: ["Retrosynthesis", "synthesis planning", "chemistry", "bidirectional search"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:47+09:00"
---

# Double-Ended Synthesis Planning with Goal-Constrained Bidirectional Search

## Abstract
Computer-aided synthesis planning (CASP) algorithms have demonstrated expert-level abilities in planning retrosynthetic routes to molecules of low to moderate complexity. However, current search methods assume the sufficiency of reaching arbitrary building blocks, failing to address the common real-world constraint where using specific molecules is desired. To this end, we present a formulation of synthesis planning with starting material constraints. Under this formulation, we propose Double-Ended Synthesis Planning ($\texttt{DESP}$), a novel CASP algorithm under a _bidirectional graph search_ scheme that interleaves expansions from the target and from the goal starting materials to ensure constraint satisfiability. The search algorithm is guided by a goal-conditioned cost network learned offline from a partially observed hypergraph of valid chemical reactions. We demonstrate the utility of $\texttt{DESP}$ in improving solve rates and reducing the number of search expansions by biasing synthesis planning towards expert goals on multiple new benchmarks. $\texttt{DESP}$ can make use of existing one-step retrosynthesis models, and we anticipate its performance to scale as these one-step model capabilities improve.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Kevin Yu, Jihye Roh, Ziang Li, Wenhao Gao, Runzhong Wang, Connor W. Coley
- arxiv_id: 
- openreview_id: LJNqVIKSCr
- anthology_id: 
- pdf_url: https://openreview.net/pdf/28a84c7beddeea0844e294d5a0ccea7ea6314dc5.pdf
- published: 2024
- keywords: Retrosynthesis, synthesis planning, chemistry, bidirectional search

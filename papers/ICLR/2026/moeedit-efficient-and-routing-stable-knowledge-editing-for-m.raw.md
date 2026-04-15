---
title: "MoEEdit: Efficient and Routing-Stable Knowledge Editing for Mixture-of-Experts LLMs"
authors: ["Yupu Gu", "Rongzhe Wei", "Andy Zhu", "Pan Li"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "BV4oHxGBx7"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/db9338b78cbfecdd2237489c96f136b418d452ca.pdf"
published: "2026"
categories: []
keywords: ["Knowledge Editing; Mixture-of-Experts; Large Language Models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:41+09:00"
---

# MoEEdit: Efficient and Routing-Stable Knowledge Editing for Mixture-of-Experts LLMs

## Abstract
Knowledge editing (KE) is crucial for making precise modifications to factual knowledge within large language models (LLMs). Existing KE methods, however, are primarily designed for dense architectures, limiting their applicability to the increasingly popular sparse Mixture-of-Experts (MoE) models that power modern scalable LLMs. While MoEs offer remarkable efficiency and capacity scaling, their unique structure introduces new challenges for KE. Naively adapting dense-model editors to MoEs is not only computationally expensive but also induces routing distribution shifts that degrade model stability and consistency. To address these challenges, we introduce MoEEdit, the first systematic framework for routing-stable knowledge editing in MoE LLMs. Our approach reparameterizes expert updates through per-expert null-space projections, ensuring router inputs remain invariant to suppress these shifts, and solves the resulting block-structured optimization with an efficient block coordinate descent (BCD) solver. Experiments demonstrate that MoEEdit achieves state-of-the-art efficacy and generalization, while maintaining high specificity, routing stability, and superior computational and memory efficiency. Our work establishes a robust foundation for scalable and precise knowledge editing in modern sparse LLMs by highlighting the necessity of routing-stable interventions.

## Metadata
- venue: ICLR
- year: 2026
- authors: Yupu Gu, Rongzhe Wei, Andy Zhu, Pan Li
- arxiv_id: 
- openreview_id: BV4oHxGBx7
- anthology_id: 
- pdf_url: https://openreview.net/pdf/db9338b78cbfecdd2237489c96f136b418d452ca.pdf
- published: 2026
- keywords: Knowledge Editing; Mixture-of-Experts; Large Language Models

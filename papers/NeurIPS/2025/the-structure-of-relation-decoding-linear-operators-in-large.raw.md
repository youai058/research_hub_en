---
title: "The Structure of Relation Decoding Linear Operators in Large Language Models"
authors: ["Miranda Anna Christ", "Adrián Csiszárik", "Gergely Becsó", "Dániel Varga"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "XsBzmJzJ2l"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ed3dd009ac0424ecb2d27ab9be7041714b6d8359.pdf"
published: "2025"
categories: []
keywords: ["large language models", "relations", "tensor networks", "interpretability"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:21+09:00"
---

# The Structure of Relation Decoding Linear Operators in Large Language Models

## Abstract
This paper investigates the structure of linear operators introduced in Hernandez et al. [2023] that decode specific relational facts in transformer language models. We extend their single-relation findings to a collection of relations and systematically chart their organization. We show that such collections of relation decoders can be highly compressed by simple order-3 tensor networks without significant loss in decoding accuracy. To explain this surprising redundancy, we develop a cross-evaluation protocol, in which we apply each linear decoder operator to the subjects of every other relation. Our results reveal that these linear maps do not encode distinct relations, but extract recurring, coarse-grained semantic properties (e.g., country of capital city and country of food are both in the country-of-X property). This property-centric structure clarifies both the operators' compressibility and highlights why they generalize only to new relations that are semantically close. Our findings thus interpret linear relational decoding in transformer language models as primarily property-based, rather than relation-specific.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Miranda Anna Christ, Adrián Csiszárik, Gergely Becsó, Dániel Varga
- arxiv_id: 
- openreview_id: XsBzmJzJ2l
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ed3dd009ac0424ecb2d27ab9be7041714b6d8359.pdf
- published: 2025
- keywords: large language models, relations, tensor networks, interpretability

---
title: "Neural Rule Lists: Learning Discretizations, Rules, and Order in One Go"
authors: ["Sascha Xu", "Nils Philipp Walter", "Jilles Vreeken"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "oBf5eZSeBT"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a23351a0489c8110bc79b5f47ae7c643be9d0725.pdf"
published: "2025"
categories: []
keywords: ["interpretability", "rule lists", "differentiable relaxation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:54+09:00"
---

# Neural Rule Lists: Learning Discretizations, Rules, and Order in One Go

## Abstract
Interpretable machine learning is essential in high-stakes domains like healthcare. Rule lists are a
popular choice due to their transparency and accuracy, but learning them effectively remains a challenge.
Existing methods require feature pre-discretization, constrain rule complexity or ordering, or struggle
to scale. We present NeuRules, a novel end-to-end framework that overcomes these limitations. At its
core, NeuRules transforms the inherently combinatorial task of rule list learning into a differentiable
optimization problem, enabling gradient-based learning. It simultaneously discovers feature conditions,
assembles them into conjunctive rules, and determines their order—without pre-processing or manual
constraints. A key contribution here is a gradient shaping technique that steers learning toward sparse
rules with strong predictive performance.  To produce ordered lists, we introduce a differentiable relaxation
that, through simulated annealing, converges to a strict rule list. Extensive experiments show
that NeuRules consistently outperforms combinatorial and neural baselines on binary as well as
multi-class classification tasks across a wide range of datasets.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Sascha Xu, Nils Philipp Walter, Jilles Vreeken
- arxiv_id: 
- openreview_id: oBf5eZSeBT
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a23351a0489c8110bc79b5f47ae7c643be9d0725.pdf
- published: 2025
- keywords: interpretability, rule lists, differentiable relaxation

---
title: "Explicit Preference Optimization: No Need for an Implicit Reward Model"
authors: ["Xiangkun Hu", "Lemin Kong", "Tong He", "David Wipf"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "iXvm0zvspb"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f2175a7a8c39a32a7472d0def60d39bb9f20a901.pdf"
published: "2025"
categories: []
keywords: ["direct preference optimization", "reinforcement learning from human feedback", "preference alignment", "regularized regression"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:14+09:00"
---

# Explicit Preference Optimization: No Need for an Implicit Reward Model

## Abstract
The generated responses of large language models (LLMs) are often fine-tuned to human preferences through a process called reinforcement learning from human feedback (RLHF).  As RLHF relies on a challenging training sequence, whereby a separate reward model is independently learned and then later applied to LLM policy updates, ongoing research effort has targeted more straightforward alternatives. In this regard, direct preference optimization (DPO) and its many offshoots circumvent the need for a separate reward training step.  Instead, through the judicious use of a reparameterization trick that induces an implicit reward, DPO and related methods consolidate learning to the minimization of a single loss function.  And yet despite demonstrable success in some real-world settings, we prove that DPO-based objectives are nonetheless subject to sub-optimal regularization and counter-intuitive interpolation behaviors, underappreciated  artifacts of the reparameterizations upon which they are based.  To this end, we introduce an explicit preference optimization framework termed EXPO that requires no analogous reparameterization to achieve an implicit reward.  Quite differently, we merely posit intuitively-appealing regularization factors from scratch that transparently avoid the potential pitfalls of key DPO variants, provably satisfying regularization desiderata that prior methods do not.  Empirical results serve to corroborate our analyses and showcase the efficacy of EXPO.

## Metadata
- venue: ICML
- year: 2025
- authors: Xiangkun Hu, Lemin Kong, Tong He, David Wipf
- arxiv_id: 
- openreview_id: iXvm0zvspb
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f2175a7a8c39a32a7472d0def60d39bb9f20a901.pdf
- published: 2025
- keywords: direct preference optimization, reinforcement learning from human feedback, preference alignment, regularized regression

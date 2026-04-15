---
title: "The mechanistic basis of data dependence and abrupt learning in an in-context classification task"
authors: ["Gautam Reddy"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "aN4Jf6Cx69"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/4de2c24997e6d25adcda68f174ed540f41a217e8.pdf"
published: "2024"
categories: []
keywords: ["in-context learning", "mechanistic interpretability", "language models", "induction heads"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:18+09:00"
---

# The mechanistic basis of data dependence and abrupt learning in an in-context classification task

## Abstract
Transformer models exhibit in-context learning: the ability to accurately predict the response to a novel query based on illustrative examples in the input sequence, which contrasts with traditional in-weights learning of query-output relationships. What aspects of the training data distribution and architecture favor in-context vs in-weights learning? Recent work has shown that specific distributional properties inherent in language, such as burstiness, large dictionaries and skewed rank-frequency distributions, control the trade-off or simultaneous appearance of these two forms of learning. We first show that these results are recapitulated in a minimal attention-only network trained on a simplified dataset. In-context learning (ICL) is driven by the abrupt emergence of an induction head, which subsequently competes with in-weights learning. By identifying progress measures that precede in-context learning and targeted experiments, we construct a two-parameter model of an induction head which emulates the full data distributional dependencies displayed by the attention-based network. A phenomenological model of induction head formation traces its abrupt emergence to the sequential learning of three nested logits enabled by an intrinsic curriculum. We propose that the sharp transitions in attention-based networks arise due to a specific chain of multi-layer operations necessary to achieve ICL, which is implemented by nested nonlinearities sequentially learned during training.

## Metadata
- venue: ICLR
- year: 2024
- authors: Gautam Reddy
- arxiv_id: 
- openreview_id: aN4Jf6Cx69
- anthology_id: 
- pdf_url: https://openreview.net/pdf/4de2c24997e6d25adcda68f174ed540f41a217e8.pdf
- published: 2024
- keywords: in-context learning, mechanistic interpretability, language models, induction heads

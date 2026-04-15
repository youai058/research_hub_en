---
title: "Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition"
authors: ["Aliyah R. Hsu", "Georgia Zhou", "Yeshwanth Cherapanamjeri", "Yaxuan Huang", "Anobel Odisho", "Peter R. Carroll", "Bin Yu"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "41HlN8XYM5"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a99a07e7b8fea3e243e0aa4fc594b5908bb86c24.pdf"
published: "2025"
categories: []
keywords: ["Automated Circuit Discovery", "Explainable AI", "Interpretation", "Machine Learning", "Language Models", "Transformers"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:58+09:00"
---

# Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition

## Abstract
Automated mechanistic interpretation research has attracted great interest due to its potential to scale explanations of neural network internals to large models. Existing automated circuit discovery work relies on activation patching or its approximations to identify subgraphs in models for specific tasks (circuits). They often suffer from slow runtime, approximation errors, and specific requirements of metrics, such as non-zero gradients.
In this work, we introduce contextual decomposition for transformers (CD-T) to build interpretable circuits in large language models. CD-T can produce circuits at any level of abstraction and is the first to efficiently produce circuits as fine-grained as attention heads at specific sequence positions.
CD-T is compatible to all transformer types, and requires no training or manually-crafted examples.
CD-T consists of a set of mathematical equations to isolate contribution of model features. Through recursively computing contribution of all nodes in a computational graph of a model using CD-T followed by pruning, we are able to reduce circuit discovery runtime from hours to seconds compared to state-of-the-art baselines.
On three standard circuit evaluation datasets (indirect object identification, greater-than comparisons, and docstring completion),
we demonstrate that CD-T outperforms ACDC and EAP by better recovering the manual circuits with an average of 97% ROC AUC under low runtimes.
In addition, we provide evidence that faithfulness of CD-T circuits is not due to random chance by showing our circuits are 80% more faithful than random circuits of up to 60% of the original model size. 
Finally, we show CD-T circuits are able to perfectly replicate original models' behavior(faithfulness  = 1) using fewer nodes than the baselines for all tasks.
Our results underscore the great promise of CD-T for efficient automated mechanistic interpretability, paving the way for new insights into the workings of large language models.

## Metadata
- venue: ICLR
- year: 2025
- authors: Aliyah R. Hsu, Georgia Zhou, Yeshwanth Cherapanamjeri, Yaxuan Huang, Anobel Odisho, Peter R. Carroll, Bin Yu
- arxiv_id: 
- openreview_id: 41HlN8XYM5
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a99a07e7b8fea3e243e0aa4fc594b5908bb86c24.pdf
- published: 2025
- keywords: Automated Circuit Discovery, Explainable AI, Interpretation, Machine Learning, Language Models, Transformers

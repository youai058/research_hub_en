---
title: "Steering Language Models with Weight Arithmetic"
authors: ["Constanza Fierro", "Fabien Roger"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "S0D3EFWohd"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/cb38509eb8f87561c083de50a429be908415fa5d.pdf"
published: "2026"
categories: []
keywords: ["steering", "alignment", "safety", "model editing", "merging models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:38+09:00"
---

# Steering Language Models with Weight Arithmetic

## Abstract
Providing high-quality feedback to Large Language Models (LLMs) on a diverse training distribution can be difficult and expensive, and providing feedback only on a narrow distribution can result in unintended generalizations. To better leverage narrow training data, we propose *contrastive weight steering*, a simple post-training method that edits the model parameters using weight arithmetic. We isolate a behavior direction in weight-space by subtracting the weight deltas from two small fine-tunes---one that induces the desired behavior and another that induces its opposite---and then add or remove this direction to modify the model's weights. We apply this technique to mitigate sycophancy and induce misalignment, and find that weight steering often generalizes further than activation steering, achieving stronger out-of-distribution behavioral control before degrading general capabilities. We also show that, in the context of task-specific fine-tuning, weight steering can partially mitigate undesired behavioral drift: it can reduce sycophancy and under-refusals introduced during fine-tuning while preserving task performance gains. Finally, we provide preliminary evidence that emergent misalignment can be detected by measuring the similarity between fine-tuning updates and an "evil" weight direction, suggesting that it may be possible to monitor the evolution of weights during training and detect rare misaligned behaviors that never manifest during training or evaluations.

## Metadata
- venue: ICLR
- year: 2026
- authors: Constanza Fierro, Fabien Roger
- arxiv_id: 
- openreview_id: S0D3EFWohd
- anthology_id: 
- pdf_url: https://openreview.net/pdf/cb38509eb8f87561c083de50a429be908415fa5d.pdf
- published: 2026
- keywords: steering, alignment, safety, model editing, merging models

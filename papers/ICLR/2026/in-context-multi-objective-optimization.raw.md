---
title: "In-Context Multi-Objective Optimization"
authors: ["Xinyu Zhang", "Conor Hassan", "Julien Martinelli", "Daolang Huang", "Samuel Kaski"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "odmeUlWta8"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/8dd024273507acb18827876a24b27d1148a2126b.pdf"
published: "2026"
categories: []
keywords: ["Multi-Objective Optimization", "Bayesian Optimization", "Transformers", "Neural Processes"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:43+09:00"
---

# In-Context Multi-Objective Optimization

## Abstract
Balancing competing objectives is omnipresent across disciplines, from drug design to autonomous systems. Multi-objective Bayesian optimization is a promising solution for such expensive, black-box problems: it fits probabilistic surrogates and selects new designs via an acquisition function that balances exploration and exploitation. In practice, it requires tailored choices of surrogate and acquisition that rarely transfer to the next problem, is myopic when multi-step planning is often required, and adds refitting overhead, particularly in parallel or time-sensitive loops. We present TAMO, a fully amortized, universal policy for multi-objective black-box optimization. TAMO uses a transformer architecture that operates across varying input and objective dimensions, enabling pretraining on diverse corpora and transfer to new problems without retraining: at test time, the pretrained model proposes the next design with a single forward pass. We pretrain the policy with reinforcement learning to maximize cumulative hypervolume improvement over full trajectories, conditioning on the entire query history to approximate the Pareto frontier. Across synthetic benchmarks and real tasks, TAMO produces fast proposals, reducing proposal time by 50–1000× versus alternatives while matching or improving Pareto quality under tight evaluation budgets. These results show that transformers can perform multi-objective optimization entirely in-context, eliminating per-task surrogate fitting and acquisition engineering, and open a path to foundation-style, plug-and-play optimizers for scientific discovery workflows.

## Metadata
- venue: ICLR
- year: 2026
- authors: Xinyu Zhang, Conor Hassan, Julien Martinelli, Daolang Huang, Samuel Kaski
- arxiv_id: 
- openreview_id: odmeUlWta8
- anthology_id: 
- pdf_url: https://openreview.net/pdf/8dd024273507acb18827876a24b27d1148a2126b.pdf
- published: 2026
- keywords: Multi-Objective Optimization, Bayesian Optimization, Transformers, Neural Processes

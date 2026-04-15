---
title: "Study of Training Dynamics for Memory-Constrained Fine-Tuning"
authors: ["Aël Quélennec", "Nour Hezbri", "Pavlo Mozharovskyi", "Van-Tam Nguyen", "Enzo Tartaglione"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "BhfIg0tuti"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d0d1b2452a069e6fc7d3a1fc5612c6a40bea1e30.pdf"
published: "2026"
categories: []
keywords: ["Efficient Learning", "Energy Saving"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:35+09:00"
---

# Study of Training Dynamics for Memory-Constrained Fine-Tuning

## Abstract
Memory-efficient training of deep neural networks has become increasingly important as models grow larger while deployment environments impose strict resource constraints. We propose TraDy, a novel transfer learning scheme leveraging two key insights: layer importance for updates is architecture-dependent and determinable a priori, while dynamic stochastic channel selection provides superior gradient approximation compared to static approaches. We introduce a dynamic channel selection approach that stochastically resamples channels between epochs within preselected layers. Extensive experiments demonstrate TraDy achieves state-of-the-art performance across various downstream tasks and architectures while maintaining strict memory constraints, achieving up to 99\% activation sparsity, 95\% weight derivative sparsity, and 97\% reduction in FLOPs for weight derivative computation.

## Metadata
- venue: ICLR
- year: 2026
- authors: Aël Quélennec, Nour Hezbri, Pavlo Mozharovskyi, Van-Tam Nguyen, Enzo Tartaglione
- arxiv_id: 
- openreview_id: BhfIg0tuti
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d0d1b2452a069e6fc7d3a1fc5612c6a40bea1e30.pdf
- published: 2026
- keywords: Efficient Learning, Energy Saving

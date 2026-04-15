---
title: "Doubly Robust Instance-Reweighted Adversarial Training"
authors: ["Daouda Sow", "Sen Lin", "Zhangyang Wang", "Yingbin Liang"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "OF5x1dzWSS"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c8cb1e0f5f66335caae7b2b8cebef4a72602b4ad.pdf"
published: "2024"
categories: []
keywords: ["adversarial training", "distributionally robust optimization", "bilevel optimization", "instance reweighting"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:15+09:00"
---

# Doubly Robust Instance-Reweighted Adversarial Training

## Abstract
Assigning importance weights to adversarial data has achieved great success in training adversarially robust networks under limited model capacity. However, existing instance-reweighted adversarial training (AT) methods heavily depend on heuristics and/or geometric interpretations to determine those importance weights, making these algorithms lack rigorous theoretical justification/guarantee. Moreover, recent research has shown that adversarial training suffers from a severe non-uniform robust performance across the training distribution, e.g., data points belonging to some classes can be much more vulnerable to adversarial attacks than others. To address both issues, in this paper, we propose a novel doubly-robust instance reweighted AT framework, which allows to obtain the importance weights via exploring distributionally robust optimization (DRO) techniques, and at the same time boosts the robustness on the most vulnerable examples. In particular, our importance weights are obtained by optimizing the KL-divergence regularized loss function, which allows us to devise new algorithms with a theoretical convergence guarantee. 
Experiments on standard classification datasets demonstrate that our proposed approach outperforms related state-of-the-art baseline methods in terms of average robust performance, and at the same time improves the robustness against attacks on the weakest data points. Codes can be found in the Supplement.

## Metadata
- venue: ICLR
- year: 2024
- authors: Daouda Sow, Sen Lin, Zhangyang Wang, Yingbin Liang
- arxiv_id: 
- openreview_id: OF5x1dzWSS
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c8cb1e0f5f66335caae7b2b8cebef4a72602b4ad.pdf
- published: 2024
- keywords: adversarial training, distributionally robust optimization, bilevel optimization, instance reweighting

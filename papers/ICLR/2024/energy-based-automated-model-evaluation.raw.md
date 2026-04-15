---
title: "Energy-based Automated Model Evaluation"
authors: ["Ru Peng", "Heming Zou", "Haobo Wang", "Yawen Zeng", "Zenan Huang", "Junbo Zhao"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "CHGcP6lVWd"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b67cd952981636bb89569bc035666d70b30d02bc.pdf"
published: "2024"
categories: []
keywords: ["Automated Model Evalutaion", "Energy", "Meta-distribution", "Distribution shift"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:02+09:00"
---

# Energy-based Automated Model Evaluation

## Abstract
The conventional evaluation protocols on machine learning models rely heavily on a labeled, i.i.d-assumed testing dataset, which is not often present in real-world applications.
The Automated Model Evaluation (AutoEval) shows an alternative to this traditional workflow, by forming a proximal prediction pipeline of the testing performance without the presence of ground-truth labels.
Despite its recent successes, the AutoEval frameworks still suffer from an overconfidence issue, substantial storage and computational cost.
In that regard, we propose a novel measure --- Meta-Distribution Energy (MDE) that allows the AutoEval framework to be both more efficient and effective.
The core of the MDE is to establish a meta-distribution statistic, on the information (energy) associated with individual samples, then offer a smoother representation enabled by energy-based learning.
We further provide our theoretical insights by connecting the MDE with the classification loss.
We provide extensive experiments across modalities, datasets and different architectural backbones to validate MDE's validity, together with its superiority compared with prior approaches.
We also prove MDE's versatility by showing its seamless integration with large-scale models, and easy adaption to learning scenarios with noisy- or imbalanced- labels.

## Metadata
- venue: ICLR
- year: 2024
- authors: Ru Peng, Heming Zou, Haobo Wang, Yawen Zeng, Zenan Huang, Junbo Zhao
- arxiv_id: 
- openreview_id: CHGcP6lVWd
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b67cd952981636bb89569bc035666d70b30d02bc.pdf
- published: 2024
- keywords: Automated Model Evalutaion, Energy, Meta-distribution, Distribution shift

---
title: "Group-robust Sample Reweighting for Subpopulation Shifts via Influence Functions"
authors: ["Rui Qiao", "Zhaoxuan Wu", "Jingtan Wang", "Pang Wei Koh", "Bryan Kian Hsiang Low"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "aQj9Ifxrl6"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d515e0e55f2ab6ff10f0cacb4293a02a7654528a.pdf"
published: "2025"
categories: []
keywords: ["distribution shift", "subpopulation shift", "spurious correlation", "influence function", "sample reweighting", "data selection"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:57+09:00"
---

# Group-robust Sample Reweighting for Subpopulation Shifts via Influence Functions

## Abstract
Machine learning models often have uneven performance among subpopulations
(a.k.a., groups) in the data distributions. This poses a significant challenge for the
models to generalize when the proportions of the groups shift during deployment.
To improve robustness to such shifts, existing approaches have developed strategies
that train models or perform hyperparameter tuning using the group-labeled data
to minimize the worst-case loss over groups. However, a non-trivial amount of
high-quality labels is often required to obtain noticeable improvements. Given
the costliness of the labels, we propose to adopt a different paradigm to enhance
group label efficiency: utilizing the group-labeled data as a target set to optimize
the weights of other group-unlabeled data. We introduce Group-robust Sample
Reweighting (GSR), a two-stage approach that first learns the representations from
group-unlabeled data, and then tinkers the model by iteratively retraining its last
layer on the reweighted data using influence functions. Our GSR is theoretically
sound, practically lightweight, and effective in improving the robustness to sub-
population shifts. In particular, GSR outperforms the previous state-of-the-art
approaches that require the same amount or even more group labels. Our code is
available at https://github.com/qiaoruiyt/GSR.

## Metadata
- venue: ICLR
- year: 2025
- authors: Rui Qiao, Zhaoxuan Wu, Jingtan Wang, Pang Wei Koh, Bryan Kian Hsiang Low
- arxiv_id: 
- openreview_id: aQj9Ifxrl6
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d515e0e55f2ab6ff10f0cacb4293a02a7654528a.pdf
- published: 2025
- keywords: distribution shift, subpopulation shift, spurious correlation, influence function, sample reweighting, data selection

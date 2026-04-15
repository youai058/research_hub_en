---
title: "Beware of Calibration Data for Pruning Large Language Models"
authors: ["Yixin Ji", "Yang Xiang", "Juntao Li", "Qingrong Xia", "Ping Li", "Xinyu Duan", "Zhefeng Wang", "Min Zhang"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "x83w6yGIWb"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/75e829c0ab0ccd4d7b93f8eabc80e93e243e1ee9.pdf"
published: "2025"
categories: []
keywords: ["calibration data", "post-training pruning", "large language models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:48+09:00"
---

# Beware of Calibration Data for Pruning Large Language Models

## Abstract
As large language models (LLMs) are widely applied across various fields, model
compression has become increasingly crucial for reducing costs and improving
inference efficiency. Post-training pruning is a promising method that does not
require resource-intensive iterative training and only needs a small amount of
calibration data to assess the importance of parameters. Recent research has enhanced post-training pruning from different aspects but few of them systematically
explore the effects of calibration data, and it is unclear if there exist better calibration data construction strategies. We fill this blank and surprisingly observe that
calibration data is also crucial to post-training pruning, especially for high sparsity. Through controlled experiments on important influence factors of calibration
data, including the pruning settings, the amount of data, and its similarity with
pre-training data, we observe that a small size of data is adequate, and more similar data to its pre-training stage can yield better performance. As pre-training data
is usually inaccessible for advanced LLMs, we further provide a self-generating
calibration data synthesis strategy to construct feasible calibration data. Experimental results on recent strong open-source LLMs (e.g., DCLM, and LLaMA-3)
show that the proposed strategy can enhance the performance of strong pruning
methods (e.g., Wanda, DSnoT, OWL) by a large margin (up to 2.68%).

## Metadata
- venue: ICLR
- year: 2025
- authors: Yixin Ji, Yang Xiang, Juntao Li, Qingrong Xia, Ping Li, Xinyu Duan, Zhefeng Wang, Min Zhang
- arxiv_id: 
- openreview_id: x83w6yGIWb
- anthology_id: 
- pdf_url: https://openreview.net/pdf/75e829c0ab0ccd4d7b93f8eabc80e93e243e1ee9.pdf
- published: 2025
- keywords: calibration data, post-training pruning, large language models

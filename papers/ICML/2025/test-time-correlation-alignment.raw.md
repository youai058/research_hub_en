---
title: "Test-time Correlation Alignment"
authors: ["Linjing You", "Jiabao Lu", "Xiayuan Huang"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "0dualJz9OI"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/3eeb6a4eb5396d8f1115b183a8e9bfda6d9eb87d.pdf"
published: "2025"
categories: []
keywords: ["Test-time adaptation", "Correlation alignment"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:40+09:00"
---

# Test-time Correlation Alignment

## Abstract
Deep neural networks often degrade under distribution shifts. Although domain adaptation offers a solution, privacy constraints often prevent access to source data, making Test-Time Adaptation (TTA)—which adapts using only unlabeled test data—increasingly attractive. However, current TTA methods still face practical challenges: (1) a primary focus on instance-wise alignment, overlooking CORrelation ALignment (CORAL) due to missing source correlations; (2) complex backpropagation operations for model updating, resulting in overhead computation and (3) domain forgetting. To address these challenges, we provide a theoretical analysis to investigate the feasibility of **T**est-time **C**orrelation **A**lignment (**TCA**), demonstrating that correlation alignment between high-certainty instances and test instances can enhance test performances with a theoretical guarantee. Based on this, we propose two simple yet effective algorithms: LinearTCA and LinearTCA+. LinearTCA applies a simple linear transformation to achieve both instance and correlation alignment without additional model updates, while LinearTCA+ serves as a plug-and-play module that can easily boost existing TTA methods. Extensive experiments validate our theoretical insights and show that TCA methods significantly outperforms baselines across various tasks, benchmarks and backbones. Notably, LinearTCA achieves higher accuracy with only 4\% GPU memory and 0.6\% computation time compared to the best TTA baseline. It also outperforms existing methods on CLIP over 1.86\%. Code: https://github.com/youlj109/TCA

## Metadata
- venue: ICML
- year: 2025
- authors: Linjing You, Jiabao Lu, Xiayuan Huang
- arxiv_id: 
- openreview_id: 0dualJz9OI
- anthology_id: 
- pdf_url: https://openreview.net/pdf/3eeb6a4eb5396d8f1115b183a8e9bfda6d9eb87d.pdf
- published: 2025
- keywords: Test-time adaptation, Correlation alignment

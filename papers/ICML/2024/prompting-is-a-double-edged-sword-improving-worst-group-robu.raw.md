---
title: "Prompting is a Double-Edged Sword: Improving Worst-Group Robustness of Foundation Models"
authors: ["Amrith Setlur", "Saurabh Garg", "Virginia Smith", "Sergey Levine"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "fdroxYsgzQ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d25344fb7af2158a8be8ee1f31292d9d77ec77f4.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:15+09:00"
---

# Prompting is a Double-Edged Sword: Improving Worst-Group Robustness of Foundation Models

## Abstract
Machine learning models fail catastrophically under distribution shift, but a surprisingly effective way to empirically improve robustness to some types of shift (*e.g.*, Imagenet-A/C) is to use stronger open-vocabulary classifiers derived from foundation models. In this work, we first note that for shifts governed by spurious correlations (features spuriously correlated with the label on the training data, but not on test), the zero-shot and few-shot performance of foundation models is no better than ERM models, and remains unchanged when pretrained data/model size is scaled. Secondly, even in these situations, foundation models are quite accurate at predicting the value of the spurious feature. In a simplified setup, we theoretically analyze both these findings. Specifically, we show that during contrastive pretraining, the simplicity bias of foundation models tends to result in the learning of features that mostly rely on the spurious attribute, compared to more robust features. We leverage these observations to propose Prompting for Robustness (PfR) which first uses foundation models to zero-shot predict the spurious attribute on labeled examples, and then learns a classifier with balanced performance across different groups of labels and spurious attribute. Across 5 vision and language tasks, we show that PfR's performance nearly equals that of an oracle algorithm (group DRO) that leverages human labeled spurious attributes.

## Metadata
- venue: ICML
- year: 2024
- authors: Amrith Setlur, Saurabh Garg, Virginia Smith, Sergey Levine
- arxiv_id: 
- openreview_id: fdroxYsgzQ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d25344fb7af2158a8be8ee1f31292d9d77ec77f4.pdf
- published: 2024

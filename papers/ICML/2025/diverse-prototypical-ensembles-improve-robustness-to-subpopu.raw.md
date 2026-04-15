---
title: "Diverse Prototypical Ensembles Improve Robustness to Subpopulation Shift"
authors: ["Nguyen Nhat Minh To", "Paul F R Wilson", "Viet Nguyen", "Mohamed Harmanani", "Michael Cooper", "Fahimeh Fooladgar", "Purang Abolmaesumi", "Parvin Mousavi", "Rahul Krishnan"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "qUTiOeM57J"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/cc64d35f0b4197cb87024aafcd275555499bfcdb.pdf"
published: "2025"
categories: []
keywords: ["distribution shift", "subpopulation shift", "spurious correlation", "class imbalance", "attribute imbalance"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:27+09:00"
---

# Diverse Prototypical Ensembles Improve Robustness to Subpopulation Shift

## Abstract
Subpopulation shift, characterized by a disparity in subpopulation distribution between the training and target datasets, can significantly degrade the performance of machine learning models. Current solutions to subpopulation shift involve modifying empirical risk minimization with re-weighting strategies to improve generalization. This strategy relies on assumptions about the number and nature of subpopulations and annotations on group membership, which are unavailable for many real-world datasets. Instead, we propose using an ensemble of diverse classifiers to adaptively capture risk associated with subpopulations. Given a feature extractor network, we replace its standard linear classification layer with a mixture of prototypical classifiers, where each member is trained to classify the data while focusing on different features and samples from other members. In empirical evaluation on nine real-world datasets, covering diverse domains and kinds of subpopulation shift, our method of Diverse Prototypical Ensembles (DPEs) often outperforms the prior state-of-the-art in worst-group accuracy. The code is available at https://github.com/minhto2802/dpe4subpop.

## Metadata
- venue: ICML
- year: 2025
- authors: Nguyen Nhat Minh To, Paul F R Wilson, Viet Nguyen, Mohamed Harmanani, Michael Cooper, Fahimeh Fooladgar, Purang Abolmaesumi, Parvin Mousavi, Rahul Krishnan
- arxiv_id: 
- openreview_id: qUTiOeM57J
- anthology_id: 
- pdf_url: https://openreview.net/pdf/cc64d35f0b4197cb87024aafcd275555499bfcdb.pdf
- published: 2025
- keywords: distribution shift, subpopulation shift, spurious correlation, class imbalance, attribute imbalance

---
title: "Mitigating Spurious Features in Contrastive Learning with Spectral Regularization"
authors: ["Naghmeh Ghanooni", "Waleed Mustafa", "Dennis Wagner", "Sophie Fellenz", "Anthony Widjaja Lin", "Marius Kloft"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "TPMsCus3r0"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0ac576f6512c1085d6d2122eb95e8ee0fd5a1703.pdf"
published: "2025"
categories: []
keywords: ["Contrastive Learning", "Spurious Correlation", "Self-supervised Learning", "Representation Learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:35+09:00"
---

# Mitigating Spurious Features in Contrastive Learning with Spectral Regularization

## Abstract
Neural networks generally prefer simple and easy-to-learn features. When these features are spuriously correlated with the labels, the network's performance can suffer, particularly for underrepresented classes or concepts. Self-supervised representation learning methods, such as contrastive learning, are especially prone to this issue, often resulting in worse performance on downstream tasks. 
We identify a key spectral signature of this failure: early reliance on dominant singular modes of the learned feature matrix. To mitigate this, we propose a novel framework that promotes a uniform eigenspectrum of the feature covariance matrix, encouraging diverse and semantically rich representations. Our method operates in a fully self-supervised setting, without relying on ground-truth labels or any additional information. Empirical results on SimCLR and SimSiam demonstrate consistent gains in robustness and transfer performance, suggesting broad applicability across self-supervised learning paradigms. Code: https://github.com/NaghmehGh/SpuriousCorrelation_SSRL

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Naghmeh Ghanooni, Waleed Mustafa, Dennis Wagner, Sophie Fellenz, Anthony Widjaja Lin, Marius Kloft
- arxiv_id: 
- openreview_id: TPMsCus3r0
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0ac576f6512c1085d6d2122eb95e8ee0fd5a1703.pdf
- published: 2025
- keywords: Contrastive Learning, Spurious Correlation, Self-supervised Learning, Representation Learning

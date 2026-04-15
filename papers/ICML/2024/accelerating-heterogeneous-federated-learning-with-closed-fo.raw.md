---
title: "Accelerating Heterogeneous Federated Learning with Closed-form Classifiers"
authors: ["Eros Fanì", "Raffaello Camoriano", "Barbara Caputo", "Marco Ciccone"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "cMige5MK1N"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/03b6498ca05d28ae78b8c544f772fb2a0f99a054.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:31+09:00"
---

# Accelerating Heterogeneous Federated Learning with Closed-form Classifiers

## Abstract
Federated Learning (FL) methods often struggle in highly statistically heterogeneous settings. Indeed, non-IID data distributions cause client drift and biased local solutions, particularly pronounced in the final classification layer, negatively impacting convergence speed and accuracy. To address this issue, we introduce *Federated Recursive Ridge Regression* (Fed3R). Our method fits a Ridge Regression classifier computed in closed form leveraging pre-trained features. Fed3R is immune to statistical heterogeneity and is invariant to the sampling order of the clients. Therefore, it proves particularly effective in cross-device scenarios. Furthermore, it is fast and efficient in terms of communication and computation costs, requiring up to two orders of magnitude fewer resources than the competitors. Finally, we propose to leverage the Fed3R parameters as an initialization for a softmax classifier and subsequently fine-tune the model using any FL algorithm (Fed3R with Fine-Tuning, Fed3R+FT). Our findings also indicate that maintaining a fixed classifier aids in stabilizing the training and learning more discriminative features in cross-device settings. Official website: https://fed-3r.github.io/.

## Metadata
- venue: ICML
- year: 2024
- authors: Eros Fanì, Raffaello Camoriano, Barbara Caputo, Marco Ciccone
- arxiv_id: 
- openreview_id: cMige5MK1N
- anthology_id: 
- pdf_url: https://openreview.net/pdf/03b6498ca05d28ae78b8c544f772fb2a0f99a054.pdf
- published: 2024

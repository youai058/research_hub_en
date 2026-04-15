---
title: "Model Reconstruction Using Counterfactual Explanations: A Perspective From Polytope Theory"
authors: ["Pasan Dissanayake", "Sanghamitra Dutta"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "9uolDxbYLm"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/708c74d99fd16672bfdf796b1716a1ae581a8869.pdf"
published: "2024"
categories: []
keywords: ["model extraction", "counterfactual explanations", "decision boundary shift", "query complexity"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:36+09:00"
---

# Model Reconstruction Using Counterfactual Explanations: A Perspective From Polytope Theory

## Abstract
Counterfactual explanations provide ways of achieving a favorable model outcome with minimum input perturbation. However, counterfactual explanations can also be leveraged to reconstruct the model by strategically training a surrogate model to give similar predictions as the original (target) model. In this work, we analyze how model reconstruction using counterfactuals can be improved by
further leveraging the fact that the counterfactuals also lie quite close to the decision boundary. Our main contribution is to derive novel theoretical relationships between the error in model reconstruction and the number of counterfactual queries required using polytope theory. Our theoretical analysis leads us to propose a strategy for model reconstruction that we call Counterfactual Clamping Attack (CCA) which trains a surrogate model using a unique loss function that treats counterfactuals differently than ordinary instances. Our approach also alleviates the related problem of decision boundary shift that arises in existing model reconstruction approaches when counterfactuals are treated as ordinary instances. Experimental results demonstrate that our strategy improves fidelity between the target and surrogate model predictions on several datasets.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Pasan Dissanayake, Sanghamitra Dutta
- arxiv_id: 
- openreview_id: 9uolDxbYLm
- anthology_id: 
- pdf_url: https://openreview.net/pdf/708c74d99fd16672bfdf796b1716a1ae581a8869.pdf
- published: 2024
- keywords: model extraction, counterfactual explanations, decision boundary shift, query complexity

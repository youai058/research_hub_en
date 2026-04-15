---
title: "How Data Mixing Shapes In-Context Learning: Asymptotic Equivalence for Transformers with MLPs"
authors: ["Samet Demir", "Zafer Dogan"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "615vk8hmeH"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ba423faf770195f239b5b88c0a32bfac0ffea0f4.pdf"
published: "2025"
categories: []
keywords: ["Transformer", "in-context learning", "nonlinear MLP", "data mixing", "Gaussian universality"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:25+09:00"
---

# How Data Mixing Shapes In-Context Learning: Asymptotic Equivalence for Transformers with MLPs

## Abstract
Pretrained Transformers demonstrate remarkable in-context learning (ICL) capabilities, enabling them to adapt to new tasks from demonstrations without parameter updates. However, theoretical studies often rely on simplified architectures (e.g., omitting MLPs), plain data models (e.g., linear regression with isotropic inputs), and single-source training—limiting their relevance to realistic settings. In this work, we study ICL in pretrained Transformers with nonlinear MLP heads on nonlinear tasks drawn from multiple data sources with heterogeneous input, task, and noise distributions. We analyze a model where the MLP comprises two layers, with the first layer trained via a single gradient step and the second layer fully optimized. Under high-dimensional asymptotics, we prove that such models are equivalent in ICL error to structured polynomial predictors, leveraging results from the theory of Gaussian universality and orthogonal polynomials. This equivalence reveals that nonlinear MLPs meaningfully enhance ICL performance—particularly on nonlinear tasks—compared to linear baselines. It also enables a precise analysis of data mixing effects: we identify key properties of high-quality data sources (low noise, structured covariances) and show that feature learning emerges only when the task covariance exhibits sufficient structure. These results are validated empirically across various activation functions, model sizes, and data distributions. Finally, we experiment with a real-world scenario involving multilingual sentiment analysis where each language is treated as a different source. Our experimental results for this case exemplify how our findings extend to real-world cases. Overall, our work advances the theoretical foundations of ICL in Transformers and provides actionable insight into the role of architecture and data in ICL.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Samet Demir, Zafer Dogan
- arxiv_id: 
- openreview_id: 615vk8hmeH
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ba423faf770195f239b5b88c0a32bfac0ffea0f4.pdf
- published: 2025
- keywords: Transformer, in-context learning, nonlinear MLP, data mixing, Gaussian universality

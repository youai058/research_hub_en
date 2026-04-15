---
title: "$t^3$-Variational Autoencoder: Learning Heavy-tailed Data with Student's t and Power Divergence"
authors: ["Juno Kim", "Jaehyuk Kwon", "Mincheol Cho", "Hyunjong Lee", "Joong-Ho Won"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "RzNlECeoOB"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/456160753ce7ca91fd5d14c5ba07b1183322d395.pdf"
published: "2024"
categories: []
keywords: ["Variational autoencoder", "Information geometry", "Heavy-tail learning", "Generative model"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:51+09:00"
---

# $t^3$-Variational Autoencoder: Learning Heavy-tailed Data with Student's t and Power Divergence

## Abstract
The variational autoencoder (VAE) typically employs a standard normal prior as a regularizer for the probabilistic latent encoder. However, the Gaussian tail often decays too quickly to effectively accommodate the encoded points, failing to preserve crucial structures hidden in the data. In this paper, we explore the use of heavy-tailed models to combat over-regularization. Drawing upon insights from information geometry, we propose $t^3$VAE, a modified VAE framework that incorporates Student's t-distributions for the prior, encoder, and decoder. This results in a joint model distribution of a power form which we argue can better fit real-world datasets. We derive a new objective by reformulating the evidence lower bound as joint optimization of KL divergence between two statistical manifolds and replacing with $\gamma$-power divergence, a natural alternative for power families. $t^3$VAE demonstrates superior generation of low-density regions when trained on heavy-tailed synthetic data. Furthermore, we show that $t^3$VAE significantly outperforms other models on CelebA and imbalanced CIFAR-100 datasets.

## Metadata
- venue: ICLR
- year: 2024
- authors: Juno Kim, Jaehyuk Kwon, Mincheol Cho, Hyunjong Lee, Joong-Ho Won
- arxiv_id: 
- openreview_id: RzNlECeoOB
- anthology_id: 
- pdf_url: https://openreview.net/pdf/456160753ce7ca91fd5d14c5ba07b1183322d395.pdf
- published: 2024
- keywords: Variational autoencoder, Information geometry, Heavy-tail learning, Generative model

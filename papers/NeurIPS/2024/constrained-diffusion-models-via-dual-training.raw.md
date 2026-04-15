---
title: "Constrained Diffusion Models via Dual Training"
authors: ["Shervin Khalafi", "Dongsheng Ding", "Alejandro Ribeiro"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Es2Ey2tGmM"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d43fdd872a442e9ba28976fd8889abab85d31c02.pdf"
published: "2024"
categories: []
keywords: ["Constrained diffusion model", "constrained optimization", "Lagrangian method", "dual algorithm"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:30+09:00"
---

# Constrained Diffusion Models via Dual Training

## Abstract
Diffusion models have attained prominence for their ability to synthesize a probability distribution for a given dataset via a diffusion process,  enabling the generation of new data points with high fidelity. However, diffusion processes are prone to generating samples that reflect biases in a training dataset. To address this issue, we develop constrained diffusion models by imposing diffusion constraints based on desired distributions that are informed by requirements. Specifically, we cast the training of diffusion models under requirements as a constrained distribution optimization problem that aims to reduce the distribution difference between original and generated data while obeying constraints on the distribution of generated data. We show that our constrained diffusion models generate new data from a mixture data distribution that achieves the optimal trade-off among objective and constraints. To train constrained diffusion models, we develop a dual training algorithm and characterize the optimality of the trained constrained diffusion model. We empirically demonstrate the effectiveness of our constrained models in two constrained generation tasks: (i) we consider a dataset with one or more underrepresented classes where we train the model with constraints to ensure fairly sampling from all classes during inference; (ii) we fine-tune a pre-trained diffusion model to sample from a new dataset while avoiding overfitting.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Shervin Khalafi, Dongsheng Ding, Alejandro Ribeiro
- arxiv_id: 
- openreview_id: Es2Ey2tGmM
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d43fdd872a442e9ba28976fd8889abab85d31c02.pdf
- published: 2024
- keywords: Constrained diffusion model, constrained optimization, Lagrangian method, dual algorithm

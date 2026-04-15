---
title: "Interpreting the Weight Space of Customized Diffusion Models"
authors: ["Amil Dravid", "Yossi Gandelsman", "Kuan-Chieh Wang", "Rameen Abdal", "Gordon Wetzstein", "Alexei A Efros", "Kfir Aberman"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "DAO2BFzMfy"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e9e7b92f125c0fd5ff999af81ef312225e1fa74a.pdf"
published: "2024"
categories: []
keywords: ["Weight Space", "Model Editing", "Diffusion Models", "Latent Space", "Personalization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:45+09:00"
---

# Interpreting the Weight Space of Customized Diffusion Models

## Abstract
We investigate the space of weights spanned by a large collection of customized diffusion models. We populate this space by creating a dataset of over 60,000 models, each of which is a base model fine-tuned to insert a different person's visual identity. We model the underlying manifold of these weights as a subspace, which we term $\textit{weights2weights}$. We demonstrate three immediate applications of this space that result in new diffusion models -- sampling, editing, and inversion. First, sampling a set of weights from this space results in a new model encoding a novel identity. Next, we find linear directions in this space corresponding to semantic edits of the identity (e.g., adding a beard), resulting in a new model with the original identity edited. Finally, we show that inverting a single image into this space encodes a realistic identity into a model, even if the input image is out of distribution (e.g., a painting). We further find that these linear properties of the diffusion model weight space extend to other visual concepts. Our results indicate that the weight space of fine-tuned diffusion models can behave as an interpretable $\textit{meta}$-latent space producing new models.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Amil Dravid, Yossi Gandelsman, Kuan-Chieh Wang, Rameen Abdal, Gordon Wetzstein, Alexei A Efros, Kfir Aberman
- arxiv_id: 
- openreview_id: DAO2BFzMfy
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e9e7b92f125c0fd5ff999af81ef312225e1fa74a.pdf
- published: 2024
- keywords: Weight Space, Model Editing, Diffusion Models, Latent Space, Personalization

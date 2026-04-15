---
title: "AdjointDEIS: Efficient Gradients for Diffusion Models"
authors: ["Zander W. Blasingame", "Chen Liu"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "fAlcxvrOEX"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/665fceaa54c0a1b607a0200306e29645b422a96b.pdf"
published: "2024"
categories: []
keywords: ["continuous adjoint equations", "neural differential equations", "neural ODEs", "adjoint sensitivity method", "diffusion models", "guided generation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:02+09:00"
---

# AdjointDEIS: Efficient Gradients for Diffusion Models

## Abstract
The optimization of the latents and parameters of diffusion models with respect to some differentiable metric defined on the output of the model is a challenging and complex problem. The sampling for diffusion models is done by solving either the *probability flow* ODE or diffusion SDE wherein a neural network approximates the score function allowing a numerical ODE/SDE solver to be used. However, naive backpropagation techniques are memory intensive, requiring the storage of all intermediate states, and face additional complexity in handling the injected noise from the diffusion term of the diffusion SDE. We propose a novel family of bespoke ODE solvers to the continuous adjoint equations for diffusion models, which we call *AdjointDEIS*. We exploit the unique construction of diffusion SDEs to further simplify the formulation of the continuous adjoint equations using *exponential integrators*. Moreover, we provide convergence order guarantees for our bespoke solvers. Significantly, we show that continuous adjoint equations for diffusion SDEs actually simplify to a simple ODE. Lastly, we demonstrate the effectiveness of AdjointDEIS for guided generation with an adversarial attack in the form of the face morphing problem. Our code will be released on our project page [https://zblasingame.github.io/AdjointDEIS/](https://zblasingame.github.io/AdjointDEIS/)

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Zander W. Blasingame, Chen Liu
- arxiv_id: 
- openreview_id: fAlcxvrOEX
- anthology_id: 
- pdf_url: https://openreview.net/pdf/665fceaa54c0a1b607a0200306e29645b422a96b.pdf
- published: 2024
- keywords: continuous adjoint equations, neural differential equations, neural ODEs, adjoint sensitivity method, diffusion models, guided generation

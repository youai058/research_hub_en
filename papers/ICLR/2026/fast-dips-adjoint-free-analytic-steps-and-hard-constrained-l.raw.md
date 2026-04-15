---
title: "FAST‑DIPS: Adjoint‑Free Analytic Steps and Hard‑Constrained Likelihood Correction for Diffusion‑Prior Inverse Problems"
authors: ["Minwoo Kim", "Seunghyeok Shin", "Hongki Lim"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "voMeZVAkKL"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6ca5776373b8d6228ab331938595ce24365697dd.pdf"
published: "2026"
categories: []
keywords: ["Inverse problem", "Image reconstruction", "Diffusion models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:42+09:00"
---

# FAST‑DIPS: Adjoint‑Free Analytic Steps and Hard‑Constrained Likelihood Correction for Diffusion‑Prior Inverse Problems

## Abstract
Training-free diffusion priors enable inverse-problem solvers without retraining, but for nonlinear forward operators data consistency often relies on repeated derivatives or inner optimization/MCMC loops with conservative step sizes, incurring many iterations and denoiser/score evaluations. We propose a training-free solver that replaces these inner loops with a hard measurement-space feasibility constraint (closed-form projection) and an analytic, model-optimal step size, enabling a small, fixed compute budget per noise level. Anchored at the denoiser prediction, the correction is approximated via an adjoint-free, ADMM-style splitting with projection and a few steepest-descent updates, using one VJP and either one JVP or a forward-difference probe, followed by backtracking and decoupled re-annealing. We prove local model optimality and descent under backtracking for the step-size rule, and derive an explicit KL bound for mode-substitution re-annealing under a local Gaussian conditional surrogate. We also develop a latent variant and a one-parameter pixel$\rightarrow$latent hybrid schedule. Experiments achieve competitive PSNR/SSIM/LPIPS with up to 19.5$\times$ speedup, without hand-coded adjoints or inner MCMC. Code and data: [here](https://github.com/ququlza/FAST-DIPS)

## Metadata
- venue: ICLR
- year: 2026
- authors: Minwoo Kim, Seunghyeok Shin, Hongki Lim
- arxiv_id: 
- openreview_id: voMeZVAkKL
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6ca5776373b8d6228ab331938595ce24365697dd.pdf
- published: 2026
- keywords: Inverse problem, Image reconstruction, Diffusion models

---
title: "SafeFlowMatcher: Safe and Fast Planning using Flow Matching with Control Barrier Functions"
authors: ["Jeongyong Yang", "Seunghwan Jang", "SooJean Han"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "refcXHU1Nh"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/99ee83db0dfdfc621c41f0e3b502065f0a644e7f.pdf"
published: "2026"
categories: []
keywords: ["Flow matching", "Control Barrier Functions", "Planning", "Control"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:47+09:00"
---

# SafeFlowMatcher: Safe and Fast Planning using Flow Matching with Control Barrier Functions

## Abstract
Generative planners based on flow matching (FM) produce high-quality paths in a single or a few ODE steps, but their sampling dynamics offer no formal safety guarantees and can yield incomplete paths near constraints. We present SafeFlowMatcher, a planning framework that couples FM with control barrier functions (CBFs) to achieve both real-time efficiency and certified safety. SafeFlowMatcher uses a two-phase prediction-correction (PC) integrator: (i) a prediction phase integrates the learned FM once (or a few steps) to obtain a candidate path without intervention; (ii) a correction phase refines this path with a vanishing time‑scaled vector field and a CBF-based quadratic program that minimally perturbs the vector field. We prove a barrier certificate for the resulting flow system, establishing forward invariance of a robust safe set and finite-time convergence to the safe set. In addition, by enforcing safety only on the executed path—rather than all intermediate latent paths—SafeFlowMatcher avoids distributional drift and mitigates local trap problems. Moreover, SafeFlowMatcher attains faster, smoother, and safer paths than diffusion- and FM-based baselines on maze navigation, locomotion, and robot manipulation tasks. Extensive ablations corroborate the contributions of the PC integrator and the barrier certificate.

## Metadata
- venue: ICLR
- year: 2026
- authors: Jeongyong Yang, Seunghwan Jang, SooJean Han
- arxiv_id: 
- openreview_id: refcXHU1Nh
- anthology_id: 
- pdf_url: https://openreview.net/pdf/99ee83db0dfdfc621c41f0e3b502065f0a644e7f.pdf
- published: 2026
- keywords: Flow matching, Control Barrier Functions, Planning, Control

---
title: "Dynamic Regret Reduces to Kernelized Static Regret"
authors: ["Andrew Jacobsen", "Alessandro Rudi", "Francesco Orabona", "Nicolò Cesa-Bianchi"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "4LSulRbbeL"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d08b7a2ccef3df4296b5858ac491f714369daf39.pdf"
published: "2025"
categories: []
keywords: ["dynamic regret", "online learning", "parameter-free", "non-stationary", "kernels", "reproducing kernel hilbert space", "RKHS"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:47+09:00"
---

# Dynamic Regret Reduces to Kernelized Static Regret

## Abstract
We study dynamic regret in online convex optimization, where the objective is to achieve low cumulative loss relative to an arbitrary benchmark sequence. By observing that competing with an arbitrary sequence of comparators $u_{1},\ldots,u_{T}$ in $\mathcal{W}\subseteq\mathbb{R}^{d}$ can be reframed as competing with a  *fixed* comparator *function* $u:[1,T]\to \mathcal{W}$,  we cast dynamic regret minimization as a *static regret* problem in a *function space*. By carefully constructing a suitable function space in the form of a Reproducing Kernel Hilbert Space (RKHS), our reduction enables us to recover the optimal $R_{T}(u_{1},\ldots,u_{T}) = \mathcal{O}(\sqrt{\sum_{t}\\|u_{t}-u_{t-1}\\|T})$ dynamic regret guarantee in the setting of linear losses, and yields new scale-free and directionally-adaptive dynamic regret guarantees. Moreover, unlike prior dynamic-to-static reductions---which are valid only for linear losses---our reduction holds for *any* sequence of losses, allowing us to recover $\mathcal{O}\big(\\|u\\|^2_{\mathcal{H}}+d_{\mathrm{eff}}(\lambda)\ln T\big)$ bounds when the losses have meaningful curvature, where $d_{\mathrm{eff}}(\lambda)$ is a measure of complexity of the RKHS. Despite working in an infinite-dimensional space, the resulting reduction leads to algorithms that are computable in practice, due to the reproducing property of RKHSs.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Andrew Jacobsen, Alessandro Rudi, Francesco Orabona, Nicolò Cesa-Bianchi
- arxiv_id: 
- openreview_id: 4LSulRbbeL
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d08b7a2ccef3df4296b5858ac491f714369daf39.pdf
- published: 2025
- keywords: dynamic regret, online learning, parameter-free, non-stationary, kernels, reproducing kernel hilbert space, RKHS

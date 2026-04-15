---
title: "SafeDiffuser: Safe Planning with Diffusion Probabilistic Models"
authors: ["Wei Xiao", "Tsun-Hsuan Wang", "Chuang Gan", "Ramin Hasani", "Mathias Lechner", "Daniela Rus"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ig2wk7kK9J"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/97b1bd5e50999f2d4d388a86da1b1b72e9d6e545.pdf"
published: "2025"
categories: []
keywords: ["Diffusion model", "Safety guarantees", "Planning and control"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:01+09:00"
---

# SafeDiffuser: Safe Planning with Diffusion Probabilistic Models

## Abstract
Diffusion models have shown promise in data-driven planning. While these planners are commonly employed in applications where decisions are critical, they still lack established safety guarantees. In this paper, we address this limitation by introducing SafeDiffuser, a method to equip diffusion models with safety guarantees via control barrier functions. The key idea of our approach is to embed finite-time diffusion invariance, i.e., a form of specification consisting of safety constraints, into the denoising diffusion procedure. This way we enable data generation under safety constraints. We show that SafeDiffusers maintain the generative performance of diffusion models while also providing robustness in safe data generation. We evaluate our method on a series of tasks, including maze path generation, legged robot locomotion, and 3D space manipulation, and demonstrate the advantages of robustness over vanilla diffusion models.

## Metadata
- venue: ICLR
- year: 2025
- authors: Wei Xiao, Tsun-Hsuan Wang, Chuang Gan, Ramin Hasani, Mathias Lechner, Daniela Rus
- arxiv_id: 
- openreview_id: ig2wk7kK9J
- anthology_id: 
- pdf_url: https://openreview.net/pdf/97b1bd5e50999f2d4d388a86da1b1b72e9d6e545.pdf
- published: 2025
- keywords: Diffusion model, Safety guarantees, Planning and control

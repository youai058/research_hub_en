---
title: "Kinetic Langevin Diffusion for Crystalline Materials Generation"
authors: ["François R J Cornet", "Federico Bergamin", "Arghya Bhowmik", "Juan Maria Garcia-Lastra", "Jes Frellsen", "Mikkel N. Schmidt"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "7J1kwZY72h"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/abfdf81ba18699d7b8a237d2a1f911f486e45fdc.pdf"
published: "2025"
categories: []
keywords: ["generative models", "diffusion models", "crystals", "materials"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:05+09:00"
---

# Kinetic Langevin Diffusion for Crystalline Materials Generation

## Abstract
Generative modeling of crystalline materials using diffusion models presents a series of challenges: the data distribution is characterized by inherent symmetries and involves multiple modalities, with some defined on specific manifolds. Notably, the treatment of fractional coordinates representing atomic positions in the unit cell requires careful consideration, as they lie on a hypertorus. In this work, we introduce Kinetic Langevin Diffusion for Materials (KLDM), a novel diffusion model for crystalline materials generation, where the key innovation resides in the modeling of the coordinates. Instead of resorting to Riemannian diffusion on the hypertorus directly, we generalize Trivialized Diffusion Model (TDM) to account for the symmetries inherent to crystals. By coupling coordinates with auxiliary Euclidean variables representing velocities, the diffusion process is now offset to a flat space. This allows us to effectively perform diffusion on the hypertorus while providing a training objective that accounts for the periodic translation symmetry of the true data distribution. We evaluate KLDM on both Crystal Structure Prediction (CSP) and De-novo Generation (DNG) tasks, demonstrating its competitive performance with current state-of-the-art models.

## Metadata
- venue: ICML
- year: 2025
- authors: François R J Cornet, Federico Bergamin, Arghya Bhowmik, Juan Maria Garcia-Lastra, Jes Frellsen, Mikkel N. Schmidt
- arxiv_id: 
- openreview_id: 7J1kwZY72h
- anthology_id: 
- pdf_url: https://openreview.net/pdf/abfdf81ba18699d7b8a237d2a1f911f486e45fdc.pdf
- published: 2025
- keywords: generative models, diffusion models, crystals, materials

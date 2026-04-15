---
title: "Inverse problems with experiment-guided AlphaFold"
authors: ["Sai Advaith Maddipatla", "Nadav Bojan", "Meital Bojan", "Sanketh Vedula", "Paul Schanda", "Ailie Marx", "Alexander Bronstein"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "qzM37nOy3N"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/4851973ad7a0af3ee84445f1dc248b20a01234be.pdf"
published: "2025"
categories: []
keywords: ["protein structure prediction", "alphafold", "protein generative models", "experiment-grounded generative models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:21+09:00"
---

# Inverse problems with experiment-guided AlphaFold

## Abstract
Proteins exist as a dynamic ensemble of multiple conformations, and these motions are often crucial for their functions. However, current structure prediction methods predominantly yield a single  conformation, overlooking the conformational heterogeneity revealed by diverse experimental modalities. Here, we present a framework for building experiment-grounded protein structure generative models that infer conformational ensembles consistent with measured experimental data. The key idea is to treat state-of-the-art protein structure predictors (e.g., AlphaFold3) as sequence-conditioned structural priors, and cast ensemble modeling as posterior inference of protein structures given experimental measurements. Through extensive real-data experiments, we demonstrate the generality of our method to incorporate a variety of experimental measurements. In particular, our framework uncovers previously unmodeled conformational heterogeneity from crystallographic densities, generates high-accuracy NMR ensembles orders of magnitude faster than status quo, and incorporates pairwise cross-link constraints. Notably, we demonstrate that our ensembles outperform AlphaFold3 and sometimes better fit experimental data than publicly deposited structures to the protein database (PDB). We believe that this approach will unlock building predictive models that fully embrace experimentally observed conformational diversity.

## Metadata
- venue: ICML
- year: 2025
- authors: Sai Advaith Maddipatla, Nadav Bojan, Meital Bojan, Sanketh Vedula, Paul Schanda, Ailie Marx, Alexander Bronstein
- arxiv_id: 
- openreview_id: qzM37nOy3N
- anthology_id: 
- pdf_url: https://openreview.net/pdf/4851973ad7a0af3ee84445f1dc248b20a01234be.pdf
- published: 2025
- keywords: protein structure prediction, alphafold, protein generative models, experiment-grounded generative models

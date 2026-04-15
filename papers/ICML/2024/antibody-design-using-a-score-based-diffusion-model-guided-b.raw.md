---
title: "Antibody Design Using a Score-based Diffusion Model Guided by Evolutionary, Physical and Geometric Constraints"
authors: ["Tian Zhu", "Milong Ren", "Haicang Zhang"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "1YsQI04KaN"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/796235a4ba2d4cd37c4bd249f841f29243adf136.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:46+09:00"
---

# Antibody Design Using a Score-based Diffusion Model Guided by Evolutionary, Physical and Geometric Constraints

## Abstract
Antibodies are central proteins in adaptive immune responses, responsible for protecting against viruses and other pathogens. Rational antibody design has proven effective in the diagnosis and treatment of various diseases like cancers and virus infections. While recent diffusion-based generative models show promise in designing antigen-specific antibodies, the primary challenge lies in the scarcity of labeled antibody-antigen complex data and binding affinity data. We present AbX, a new score-based diffusion generative model guided by evolutionary, physical, and geometric constraints for antibody design. These constraints serve to narrow the search space and provide priors for plausible antibody sequences and structures. Specifically, we leverage a pre-trained protein language model as priors for evolutionary plausible antibodies and introduce additional training objectives for geometric and physical constraints like van der Waals forces. Furthermore, as far as we know, AbX is the first score-based diffusion model with continuous timesteps for antibody design, jointly modeling the discrete sequence space and the $\mathrm{SE}(3)$ structure space. Evaluated on two independent testing sets, we show that AbX outperforms other published methods, achieving higher accuracy in sequence and structure generation and enhanced antibody-antigen binding affinity. Ablation studies highlight the clear contributions of the introduced constraints to antibody design.

## Metadata
- venue: ICML
- year: 2024
- authors: Tian Zhu, Milong Ren, Haicang Zhang
- arxiv_id: 
- openreview_id: 1YsQI04KaN
- anthology_id: 
- pdf_url: https://openreview.net/pdf/796235a4ba2d4cd37c4bd249f841f29243adf136.pdf
- published: 2024

---
title: "Token-Level Guided Discrete Diffusion for Membrane Protein Design"
authors: ["Shrey Goel", "Peregrine M. Schray", "Yinuo Zhang", "Sophia Vincoff", "Huong T. Kratochvil", "Pranam Chatterjee"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2410.16735"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2410.16735v2"
published: "2024-10-22"
categories: ["q-bio.BM"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:02+09:00"
---

# Token-Level Guided Discrete Diffusion for Membrane Protein Design

## Abstract
Reparameterized diffusion models (RDMs) have recently matched autoregressive methods in protein generation, motivating their use for challenging tasks such as designing membrane proteins, which possess interleaved soluble and transmembrane (TM) regions. We introduce the Membrane Diffusion Language Model (MemDLM), a fine-tuned RDM-based protein language model that enables controllable membrane protein sequence design. MemDLM-generated sequences recapitulate the TM residue density and structural features of natural membrane proteins, achieving comparable biological plausibility and outperforming state-of-the-art diffusion baselines in motif scaffolding tasks by producing lower perplexity, higher BLOSUM-62 scores, and improved pLDDT confidence. To enhance controllability, we develop Per-Token Guidance (PET), a novel classifier-guided sampling strategy that selectively solubilizes residues while preserving conserved TM domains, yielding sequences with reduced TM density but intact functional cores. Importantly, MemDLM designs validated in TOXCAT beta-lactamase growth assays demonstrate successful TM insertion, distinguishing high-quality generated sequences from poor ones. Together, our framework establishes the first experimentally-validated diffusion-based model for rational membrane protein generation, integrating de novo design, motif scaffolding, and targeted property optimization.

## Metadata
- venue: arXiv
- year: 2024
- authors: Shrey Goel, Peregrine M. Schray, Yinuo Zhang, Sophia Vincoff, Huong T. Kratochvil, Pranam Chatterjee
- arxiv_id: 2410.16735
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2410.16735v2
- published: 2024-10-22

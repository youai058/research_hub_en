---
title: "Text-Guided Molecule Generation with Diffusion Language Model"
authors: ["Haisong Gong", "Qiang Liu", "Shu Wu", "Liang Wang"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2402.13040"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2402.13040v1"
published: "2024-02-20"
categories: ["cs.LG", "cs.AI", "cs.CE", "cs.CL", "q-bio.BM"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:02+09:00"
---

# Text-Guided Molecule Generation with Diffusion Language Model

## Abstract
Text-guided molecule generation is a task where molecules are generated to match specific textual descriptions. Recently, most existing SMILES-based molecule generation methods rely on an autoregressive architecture. In this work, we propose the Text-Guided Molecule Generation with Diffusion Language Model (TGM-DLM), a novel approach that leverages diffusion models to address the limitations of autoregressive methods. TGM-DLM updates token embeddings within the SMILES string collectively and iteratively, using a two-phase diffusion generation process. The first phase optimizes embeddings from random noise, guided by the text description, while the second phase corrects invalid SMILES strings to form valid molecular representations. We demonstrate that TGM-DLM outperforms MolT5-Base, an autoregressive model, without the need for additional data resources. Our findings underscore the remarkable effectiveness of TGM-DLM in generating coherent and precise molecules with specific properties, opening new avenues in drug discovery and related scientific domains. Code will be released at: https://github.com/Deno-V/tgm-dlm.

## Metadata
- venue: arXiv
- year: 2024
- authors: Haisong Gong, Qiang Liu, Shu Wu, Liang Wang
- arxiv_id: 2402.13040
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2402.13040v1
- published: 2024-02-20

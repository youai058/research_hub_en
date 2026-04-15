---
title: "A Diffusion Model to Shrink Proteins While Maintaining Their Function"
authors: ["Ethan Baron", "Alan N. Amin", "Ruben Weitzman", "Debora Marks", "Andrew Gordon Wilson"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2511.07390"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2511.07390v2"
published: "2025-11-10"
categories: ["cs.LG", "q-bio.QM"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:37+09:00"
---

# A Diffusion Model to Shrink Proteins While Maintaining Their Function

## Abstract
Many proteins useful in modern medicine or bioengineering are challenging to make in the lab, fuse with other proteins in cells, or deliver to tissues in the body, because their sequences are too long. Shortening these sequences typically involves costly, time-consuming experimental campaigns. Ideally, we could instead use modern models of massive databases of sequences from nature to learn how to propose shrunken proteins that resemble sequences found in nature. Unfortunately, these models struggle to efficiently search the combinatorial space of all deletions, and are not trained with inductive biases to learn how to delete. To address this gap, we propose SCISOR, a novel discrete diffusion model that deletes letters from sequences to generate protein samples that resemble those found in nature. To do so, SCISOR trains a de-noiser to reverse a forward noising process that adds random insertions to natural sequences. As a generative model, SCISOR fits evolutionary sequence data competitively with previous large models. In evaluation, SCISOR achieves state-of-the-art predictions of the functional effects of deletions on ProteinGym. Finally, we use the SCISOR de-noiser to shrink long protein sequences, and show that its suggested deletions result in significantly more realistic proteins and more often preserve functional motifs than previous models of evolutionary sequences.

## Metadata
- venue: arXiv
- year: 2025
- authors: Ethan Baron, Alan N. Amin, Ruben Weitzman, Debora Marks, Andrew Gordon Wilson
- arxiv_id: 2511.07390
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2511.07390v2
- published: 2025-11-10

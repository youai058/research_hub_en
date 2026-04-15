---
title: "MADGEN: Mass-Spec attends to De Novo Molecular generation"
authors: ["Yinkai Wang", "Xiaohui Chen", "Liping Liu", "Soha Hassoun"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "78tc3EiUrN"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6edc9aac27c89b06672fd3d16efbaa1dc13b9f96.pdf"
published: "2025"
categories: []
keywords: ["AI4Science", "Biology Discovery", "Metabolomics", "MS/MS spectra"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:15+09:00"
---

# MADGEN: Mass-Spec attends to De Novo Molecular generation

## Abstract
The annotation (assigning structural chemical identities) of MS/MS spectra remains a significant challenge due to the enormous molecular diversity in biological samples and the limited scope of reference databases.  Currently, the vast majority of spectral measurements remain in the "dark chemical space" without structural annotations.  To improve annotation, we propose MADGEN (Mass-spec Attends to De Novo Molecular GENeration), a scaffold-based method for de novo molecular structure generation guided by mass spectrometry data. MADGEN operates in two stages: scaffold retrieval and spectra-conditioned molecular generation starting with the scaffold. In the first stage, given an MS/MS spectrum, we formulate scaffold retrieval as a ranking problem and employ contrastive learning to align mass spectra with candidate molecular scaffolds. In the second stage, starting from the retrieved scaffold, we employ the MS/MS spectrum to guide an attention-based generative model to generate the final molecule. Our approach constrains the molecular generation search space, reducing its complexity and improving generation accuracy. We evaluate MADGEN on three datasets (NIST23, CANOPUS, and MassSpecGym) and  evaluate MADGEN's performance with a predictive scaffold retriever and with an oracle retriever. We demonstrate the effectiveness of using  attention to integrate spectral information throughout the generation process to achieve strong results with the oracle retriever.

## Metadata
- venue: ICLR
- year: 2025
- authors: Yinkai Wang, Xiaohui Chen, Liping Liu, Soha Hassoun
- arxiv_id: 
- openreview_id: 78tc3EiUrN
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6edc9aac27c89b06672fd3d16efbaa1dc13b9f96.pdf
- published: 2025
- keywords: AI4Science, Biology Discovery, Metabolomics, MS/MS spectra

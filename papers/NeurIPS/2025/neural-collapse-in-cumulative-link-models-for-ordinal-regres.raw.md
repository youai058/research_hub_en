---
title: "Neural Collapse in Cumulative Link Models for Ordinal Regression: An Analysis with Unconstrained Feature Model"
authors: ["Chuang Ma", "Tomoyuki Obuchi", "Toshiyuki Tanaka"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "pjTbFuv9ET"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/137fb6b27adf100746ffde0bec27b657235632ed.pdf"
published: "2025"
categories: []
keywords: ["neural collapse", "unconstrained feature model", "ordinal regression", "cumulative link model", "deep learning theory"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:59+09:00"
---

# Neural Collapse in Cumulative Link Models for Ordinal Regression: An Analysis with Unconstrained Feature Model

## Abstract
A phenomenon known as ``Neural Collapse (NC)'' in deep classification tasks, in which the penultimate-layer features and the final classifiers exhibit an extremely simple geometric structure, has recently attracted considerable attention, with the expectation that it can deepen our understanding of how deep neural networks behave. The Unconstrained Feature Model (UFM) has been proposed to explain NC theoretically, and there emerges a growing body of work that extends NC to tasks other than classification and leverages it for practical applications. In this study, we investigate whether a similar phenomenon arises in deep Ordinal Regression (OR) tasks, via combining the cumulative link model for OR and UFM. We show that a phenomenon we call Ordinal Neural Collapse (ONC) indeed emerges and is characterized by the following three properties: (ONC1) all optimal features in the same class collapse to their within-class mean when regularization is applied; (ONC2) these class means align with the classifier, meaning that they collapse onto a one-dimensional subspace; (ONC3) the optimal latent variables (corresponding to logits or preactivations in classification tasks) are aligned according to the class order, and in particular, in the zero-regularization limit, a highly local and simple geometric relationship emerges between the latent variables and the threshold values. We prove these properties analytically within the UFM framework with fixed threshold values and corroborate them empirically across a variety of datasets. We also discuss how these insights can be leveraged in OR, highlighting the use of fixed thresholds.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Chuang Ma, Tomoyuki Obuchi, Toshiyuki Tanaka
- arxiv_id: 
- openreview_id: pjTbFuv9ET
- anthology_id: 
- pdf_url: https://openreview.net/pdf/137fb6b27adf100746ffde0bec27b657235632ed.pdf
- published: 2025
- keywords: neural collapse, unconstrained feature model, ordinal regression, cumulative link model, deep learning theory

---
title: "Finite Smoothing Algorithm for High-Dimensional Support Vector Machines and Quantile Regression"
authors: ["Qian Tang", "Yikai Zhang", "Boxiang Wang"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "RvwMTDYTOb"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f3af96cb801b8c75254407f4414eccb9c77732cf.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:28+09:00"
---

# Finite Smoothing Algorithm for High-Dimensional Support Vector Machines and Quantile Regression

## Abstract
This paper introduces a finite smoothing algorithm (FSA), a novel approach to tackle computational challenges in applying support vector machines (SVM) and quantile regression to high-dimensional data. The critical issue with these methods is the non-smooth nature of their loss functions, which traditionally limits the use of highly efficient coordinate descent techniques in high-dimensional settings. FSA innovatively addresses this issue by transforming these loss functions into their smooth counterparts, thereby facilitating more efficient computation. A distinctive feature of FSA is its theoretical foundation: FSA can yield exact solutions, not just approximations, despite the smoothing approach. Our simulation and benchmark tests demonstrate that FSA significantly outpaces its competitors in speed, often by orders of magnitude, while improving or at least maintaining precision. We have implemented FSA in two open-source R packages: hdsvm for high-dimensional SVM and hdqr for high-dimensional quantile regression.

## Metadata
- venue: ICML
- year: 2024
- authors: Qian Tang, Yikai Zhang, Boxiang Wang
- arxiv_id: 
- openreview_id: RvwMTDYTOb
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f3af96cb801b8c75254407f4414eccb9c77732cf.pdf
- published: 2024

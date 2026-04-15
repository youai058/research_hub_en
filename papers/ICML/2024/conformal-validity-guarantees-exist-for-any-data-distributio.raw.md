---
title: "Conformal Validity Guarantees Exist for Any Data Distribution (and How to Find Them)"
authors: ["Drew Prinster", "Samuel Don Stanton", "Anqi Liu", "Suchi Saria"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "F3936hVwQa"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/8d122e5aa12fe2d49a1b2ec5eb72eb76b9e95b0e.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:19+09:00"
---

# Conformal Validity Guarantees Exist for Any Data Distribution (and How to Find Them)

## Abstract
As artificial intelligence (AI) / machine learning (ML) gain widespread adoption, practitioners are increasingly seeking means to quantify and control the risk these systems incur. This challenge is especially salient when such systems have autonomy to collect their own data, such as in black-box optimization and active learning, where their actions induce sequential feedback-loop shifts in the data distribution. Conformal prediction is a promising approach to uncertainty and risk quantification, but prior variants' validity guarantees have assumed some form of ``quasi-exchangeability'' on the data distribution, thereby excluding many types of sequential shifts. In this paper we prove that conformal prediction can theoretically be extended to *any* joint data distribution, not just exchangeable or quasi-exchangeable ones. Although the most general case is exceedingly impractical to compute, for concrete practical applications we outline a procedure for deriving specific conformal algorithms for any data distribution, and we use this procedure to derive tractable algorithms for a series of AI/ML-agent-induced covariate shifts. We evaluate the proposed algorithms empirically on synthetic black-box optimization and active learning tasks.

## Metadata
- venue: ICML
- year: 2024
- authors: Drew Prinster, Samuel Don Stanton, Anqi Liu, Suchi Saria
- arxiv_id: 
- openreview_id: F3936hVwQa
- anthology_id: 
- pdf_url: https://openreview.net/pdf/8d122e5aa12fe2d49a1b2ec5eb72eb76b9e95b0e.pdf
- published: 2024

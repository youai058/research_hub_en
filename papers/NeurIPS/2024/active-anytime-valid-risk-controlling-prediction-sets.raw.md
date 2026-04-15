---
title: "Active, anytime-valid risk controlling prediction sets"
authors: ["Ziyu Xu", "Nikos Karampatziakis", "Paul Mineiro"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "4ZH48aGD60"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9809df27c7a7e37e240b7d1cb1de1d54e9e5389e.pdf"
published: "2024"
categories: []
keywords: ["distribution free", "conformal prediction", "e-process", "confidence sequence"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:34+09:00"
---

# Active, anytime-valid risk controlling prediction sets

## Abstract
Rigorously establishing the safety of black-box machine learning models with respect to critical risk measures is important for providing guarantees about the behavior of the model.
Recently, a notion of a risk controlling prediction set (RCPS) has been introduced by Bates et. al. (JACM '24) for producing prediction sets that are statistically guaranteed to have low risk from machine learning models.
Our method extends this notion to the sequential setting, where we provide guarantees even when the data is collected adaptively, and ensures the risk guarantee is anytime-valid, i.e., simultaneously holds at all time steps. Further, we propose a framework for constructing RCPSes for active labeling, i.e., allowing one to use a labeling policy that chooses whether to query the true label for each received data point, and ensures the expected proportion data points whose labels are queried are below a predetermined label budget. We also describe how to use predictors (e.g., the machine learning model we are providing risk control guarantees for) to further improve the utility of our RCPSes by estimating the expected risk conditioned on the covariates.
We characterize the optimal choices of label policy under a fixed label budget, and predictor, and show a regret result that relates the estimation error of the optimal labeling policy and predictor to the wealth process that underlies our RCPSes.
Lastly, we present practical ways of formulating label policies and we empirically show that our label policies use fewer labels to reach higher utility than naive baseline labeling strategies on both simulations and real data.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Ziyu Xu, Nikos Karampatziakis, Paul Mineiro
- arxiv_id: 
- openreview_id: 4ZH48aGD60
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9809df27c7a7e37e240b7d1cb1de1d54e9e5389e.pdf
- published: 2024
- keywords: distribution free, conformal prediction, e-process, confidence sequence

---
title: "Measuring Stochastic Data Complexity with Boltzmann Influence Functions"
authors: ["Nathan Hoyen Ng", "Roger Baker Grosse", "Marzyeh Ghassemi"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "JNN6QHhLHB"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/08639556e5e24d1f5ff1999c68151a71307ad7f3.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:34+09:00"
---

# Measuring Stochastic Data Complexity with Boltzmann Influence Functions

## Abstract
Estimating the uncertainty of a model’s prediction on a test point is a crucial part of ensuring reliability and calibration under distribution shifts.A minimum description length approach to this problem uses the predictive normalized maximum likelihood (pNML) distribution, which considers every possible label for a data point, and decreases confidence in a prediction if other labels are also consistent with the model and training data. In this work we propose IF-COMP, a scalable and efficient approximation of the pNML distribution that linearizes the model with a temperature-scaled Boltzmann influence function. IF-COMP can be used to produce well-calibrated predictions on test points as well as measure complexity in both labelled and unlabelled settings. We experimentally validate IF-COMP on uncertainty calibration, mislabel detection, and OOD detection tasks, where it consistently matches or beats strong baseline methods.

## Metadata
- venue: ICML
- year: 2024
- authors: Nathan Hoyen Ng, Roger Baker Grosse, Marzyeh Ghassemi
- arxiv_id: 
- openreview_id: JNN6QHhLHB
- anthology_id: 
- pdf_url: https://openreview.net/pdf/08639556e5e24d1f5ff1999c68151a71307ad7f3.pdf
- published: 2024

---
title: "Quantifying Uncertainty in Error Consistency: Towards Reliable Behavioral Comparison of Classifiers"
authors: ["Thomas Klein", "Sascha Meyen", "Wieland Brendel", "Felix A. Wichmann", "Kristof Meding"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ngBOb9wSYN"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/7bf54c8b54f40f7cbbd69288ba503077a8e2d64a.pdf"
published: "2025"
categories: []
keywords: ["Error Consistency", "Behavioral Alignment", "Vision"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:58+09:00"
---

# Quantifying Uncertainty in Error Consistency: Towards Reliable Behavioral Comparison of Classifiers

## Abstract
Benchmarking models is a key factor for the rapid progress in machine learning (ML) research. Thus, further progress depends on improving benchmarking metrics. A standard metric to measure the behavioral alignment between ML models and human observers is error consistency (EC). EC allows for more fine-grained comparisons of behavior than other metrics such as accuracy, and has been used in the influential Brain-Score benchmark to rank different DNNs by their behavioral consistency with humans.  Previously, EC values have been reported without confidence intervals. However, empirically measured EC values are typically noisy - thus, without confidence intervals, valid benchmarking conclusions are problematic. Here we improve on standard EC in two ways: First, we show how to obtain confidence intervals for EC using a bootstrapping technique, allowing us to derive significance tests for EC. Second, we propose a new computational model relating the EC between two classifiers to the implicit probability that one of them copies responses from the other. This view of EC allows us to give practical guidance to scientists regarding the number of trials required for sufficiently powerful, conclusive experiments.
Finally, we use our methodology to revisit popular NeuroAI-results. We find that while the general trend of behavioral differences between humans and machines holds up to scrutiny, many reported differences between deep vision models are statistically insignificant. Our methodology enables researchers to design adequately powered experiments that can reliably detect behavioral differences between models, providing a foundation for more rigorous benchmarking of behavioral alignment.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Thomas Klein, Sascha Meyen, Wieland Brendel, Felix A. Wichmann, Kristof Meding
- arxiv_id: 
- openreview_id: ngBOb9wSYN
- anthology_id: 
- pdf_url: https://openreview.net/pdf/7bf54c8b54f40f7cbbd69288ba503077a8e2d64a.pdf
- published: 2025
- keywords: Error Consistency, Behavioral Alignment, Vision

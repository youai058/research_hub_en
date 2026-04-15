---
title: "Meta-Learners for Partially-Identified Treatment Effects Across Multiple Environments"
authors: ["Jonas Schweisthal", "Dennis Frauen", "Mihaela van der Schaar", "Stefan Feuerriegel"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "s5PLISyNyP"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/34ea9c3fa3c6fa8bdfb07e59a8f69df81138e9d5.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:18+09:00"
---

# Meta-Learners for Partially-Identified Treatment Effects Across Multiple Environments

## Abstract
Estimating the conditional average treatment effect (CATE) from observational data is relevant for many applications such as personalized medicine. Here, we focus on the widespread setting where the observational data come from multiple environments, such as different hospitals, physicians, or countries. Furthermore, we allow for violations of standard causal assumptions, namely, overlap within the environments and unconfoundedness. To this end, we move away from point identification and focus on partial identification. Specifically, we show that current assumptions from the literature on multiple environments allow us to interpret the environment as an instrumental variable (IV). This allows us to adapt bounds from the IV literature for partial identification of CATE by leveraging treatment assignment mechanisms across environments. Then, we propose different model-agnostic learners (so-called meta-learners) to estimate the bounds that can be used in combination with arbitrary machine learning models. We further demonstrate the effectiveness of our meta-learners across various experiments using both simulated and real-world data. Finally, we discuss the applicability of our meta-learners to partial identification in instrumental variable settings, such as randomized controlled trials with non-compliance.

## Metadata
- venue: ICML
- year: 2024
- authors: Jonas Schweisthal, Dennis Frauen, Mihaela van der Schaar, Stefan Feuerriegel
- arxiv_id: 
- openreview_id: s5PLISyNyP
- anthology_id: 
- pdf_url: https://openreview.net/pdf/34ea9c3fa3c6fa8bdfb07e59a8f69df81138e9d5.pdf
- published: 2024

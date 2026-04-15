---
title: "Fair Bilevel Neural Network (FairBiNN): On Balancing fairness and accuracy via Stackelberg Equilibrium"
authors: ["Mehdi Yazdani-Jahromi", "Ali Khodabandeh Yalabadi", "Amirarsalan Rajabi", "Aida Tayebi", "Ivan Garibay", "Ozlem Garibay"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "e2R4WNHHGQ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/765865233846f4ebe77c181a0f9c143b3f98755c.pdf"
published: "2024"
categories: []
keywords: ["Fairness", "Bilevel optimization", "Pareto optimal", "Stackelberg", "Demographic parity", "Fairness-accuracy trade-off"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:52+09:00"
---

# Fair Bilevel Neural Network (FairBiNN): On Balancing fairness and accuracy via Stackelberg Equilibrium

## Abstract
The persistent challenge of bias in machine learning models necessitates robust solutions to ensure parity and equal treatment across diverse groups, particularly in classification tasks. Current methods for mitigating bias often result in information loss and an inadequate balance between accuracy and fairness. To address this, we propose a novel methodology grounded in bilevel optimization principles. Our deep learning-based approach concurrently optimizes for both accuracy and fairness objectives, and under certain assumptions, achieving proven Pareto optimal solutions while mitigating bias in the trained model. Theoretical analysis indicates that the upper bound on the loss incurred by this method is less than or equal to the loss of the Lagrangian approach, which involves adding a regularization term to the loss function. We demonstrate the efficacy of our model primarily on tabular datasets such as UCI Adult and Heritage Health. When benchmarked against state-of-the-art fairness methods, our model exhibits superior performance, advancing fairness-aware machine learning solutions and bridging the accuracy-fairness gap. The implementation of FairBiNN is available on https://github.com/yazdanimehdi/FairBiNN.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Mehdi Yazdani-Jahromi, Ali Khodabandeh Yalabadi, Amirarsalan Rajabi, Aida Tayebi, Ivan Garibay, Ozlem Garibay
- arxiv_id: 
- openreview_id: e2R4WNHHGQ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/765865233846f4ebe77c181a0f9c143b3f98755c.pdf
- published: 2024
- keywords: Fairness, Bilevel optimization, Pareto optimal, Stackelberg, Demographic parity, Fairness-accuracy trade-off

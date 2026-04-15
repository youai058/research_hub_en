---
title: "Safe Time-Varying Optimization based on Gaussian Processes with Spatio-Temporal Kernel"
authors: ["Jialin Li", "Marta Zagorowska", "Giulia De Pasquale", "Alisa Rupenyan", "John Lygeros"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "yKvHJJE9le"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/8ccc16f75fc2b8ad413d7dc3ee80d673efeeab6c.pdf"
published: "2024"
categories: []
keywords: ["Safe learning", "Bayesian optimization", "Time-varying optimization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:46+09:00"
---

# Safe Time-Varying Optimization based on Gaussian Processes with Spatio-Temporal Kernel

## Abstract
Ensuring safety is a key aspect in sequential decision making problems, such as robotics or process control. The complexity of the underlying systems often makes finding the optimal decision challenging, especially when the safety-critical system is time-varying. Overcoming the problem of optimizing an unknown time-varying reward subject to unknown time-varying safety constraints, we propose TVSAFEOPT, a new algorithm built on Bayesian optimization with a spatio-temporal kernel. The algorithm is capable of safely tracking a time-varying safe region without the need for explicit change detection. Optimality guarantees are also provided for the algorithm when the optimization problem becomes stationary. We show that TVSAFEOPT compares favorably against SAFEOPT on synthetic data, both regarding safety and optimality. Evaluation on a realistic case study with gas compressors confirms that TVSAFEOPT ensures safety when solving time-varying optimization problems with unknown reward and safety functions.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Jialin Li, Marta Zagorowska, Giulia De Pasquale, Alisa Rupenyan, John Lygeros
- arxiv_id: 
- openreview_id: yKvHJJE9le
- anthology_id: 
- pdf_url: https://openreview.net/pdf/8ccc16f75fc2b8ad413d7dc3ee80d673efeeab6c.pdf
- published: 2024
- keywords: Safe learning, Bayesian optimization, Time-varying optimization

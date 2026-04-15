---
title: "Optimal Sensor Scheduling and Selection for Continuous-Discrete Kalman Filtering with Auxiliary Dynamics"
authors: ["Mohamad Al Ahdab", "John Leth", "Zheng-Hua Tan"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "CAPNgWkEEk"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d6b68e07c0055deec6936d644c06db0989adb22e.pdf"
published: "2025"
categories: []
keywords: ["Kalman Filtering", "Sensor Scheduling", "Bayesian State-Space Models", "Control"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:11+09:00"
---

# Optimal Sensor Scheduling and Selection for Continuous-Discrete Kalman Filtering with Auxiliary Dynamics

## Abstract
We study the Continuous-Discrete Kalman Filter (CD-KF) for State-Space Models (SSMs) where continuous-time dynamics are observed via multiple sensors with discrete, irregularly timed measurements. Our focus extends to scenarios in which the measurement process is coupled with the states of an auxiliary SSM. For instance, higher measurement rates may increase energy consumption or heat generation, while a sensor’s accuracy can depend on its own spatial trajectory or that of the measured target. Each sensor thus carries distinct costs and constraints associated with its measurement rate and additional constraints and costs on the auxiliary state. We model measurement occurrences as independent Poisson processes with sensor-specific rates and derive an upper bound on the mean posterior covariance matrix of the CD-KF along the mean auxiliary state. The bound is continuously differentiable with respect to the measurement rates, which enables efficient gradient-based optimization. Exploiting this bound, we propose a finite-horizon optimal control framework to optimize measurement rates and auxiliary-state dynamics jointly. We further introduce a deterministic method for scheduling measurement times from the optimized rates. Empirical results in state-space filtering and dynamic temporal Gaussian process regression demonstrate that our approach achieves improved trade-offs between resource usage and estimation accuracy.

## Metadata
- venue: ICML
- year: 2025
- authors: Mohamad Al Ahdab, John Leth, Zheng-Hua Tan
- arxiv_id: 
- openreview_id: CAPNgWkEEk
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d6b68e07c0055deec6936d644c06db0989adb22e.pdf
- published: 2025
- keywords: Kalman Filtering, Sensor Scheduling, Bayesian State-Space Models, Control

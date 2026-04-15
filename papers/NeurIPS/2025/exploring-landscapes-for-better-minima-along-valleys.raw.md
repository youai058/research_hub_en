---
title: "Exploring Landscapes for Better Minima along Valleys"
authors: ["Tong Zhao", "Jiacheng Li", "Yuanchang Zhou", "Guangming Tan", "Weile Jia"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "XxRKqFsvoK"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/51bd5362c80600873cb8b70a7a35cf208e6e03eb.pdf"
published: "2025"
categories: []
keywords: ["optimization", "landscape", "exploration", "local minimum", "convergence", "exponential moving average"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:30+09:00"
---

# Exploring Landscapes for Better Minima along Valleys

## Abstract
Finding lower and better-generalizing minima is crucial for deep learning. However, most existing optimizers stop searching the parameter space once they reach a local minimum. Given the complex geometric properties of the loss landscape, it is difficult to guarantee that such a point is the lowest or provides the best generalization. To address this, we propose an adaptor "E" for gradient-based optimizers. The adapted optimizer tends to continue exploring along landscape valleys (areas with low and nearly identical losses) in order to search for potentially better local minima even after reaching a local minimum. This approach increases the likelihood of finding a lower and flatter local minimum, which is often associated with better generalization. We also provide a proof of convergence for the adapted optimizers in both convex and non-convex scenarios for completeness. Finally, we demonstrate their effectiveness in an important but notoriously difficult training scenario, large-minibatch training, where Lamb is the benchmark optimizer. Our testing results show that the adapted Lamb, ALTO, increases the test accuracy (generalization) of the current state-of-the-art optimizer by an average of 2.5\% across a variety of large-batch training tasks. This work potentially opens a new research direction in the design of optimization algorithms.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Tong Zhao, Jiacheng Li, Yuanchang Zhou, Guangming Tan, Weile Jia
- arxiv_id: 
- openreview_id: XxRKqFsvoK
- anthology_id: 
- pdf_url: https://openreview.net/pdf/51bd5362c80600873cb8b70a7a35cf208e6e03eb.pdf
- published: 2025
- keywords: optimization, landscape, exploration, local minimum, convergence, exponential moving average

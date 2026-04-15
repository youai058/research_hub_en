---
title: "Self-Supervised Coarsening of Unstructured Grid with Automatic Differentiation"
authors: ["Sergei Shumilin", "Alexander Ryabov", "Nikolay Yavich", "Evgeny Burnaev", "Vladimir Vanovskiy"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "kMBvZ40Iu9"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c8277e98462d412e31c95d7ba1c89741ec2700e4.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:27+09:00"
---

# Self-Supervised Coarsening of Unstructured Grid with Automatic Differentiation

## Abstract
Due to the high computational load of modern numerical simulation, there is a demand for approaches that would reduce the size of discrete problems while keeping the accuracy reasonable. In this work, we present an original algorithm to coarsen an unstructured grid based on the concepts of differentiable physics. We achieve this by employing $k$-means clustering, autodifferentiation and stochastic minimization algorithms. We demonstrate performance of the designed algorithm on two PDEs: a linear parabolic equation which governs slightly compressible fluid flow in porous media and the wave equation. Our results show that in the considered scenarios, we reduced the number of grid points up to 10 times while preserving the modeled variable dynamics in the points of interest. The proposed approach can be applied to the simulation of an arbitrary system described by evolutionary partial differential equations.

## Metadata
- venue: ICML
- year: 2024
- authors: Sergei Shumilin, Alexander Ryabov, Nikolay Yavich, Evgeny Burnaev, Vladimir Vanovskiy
- arxiv_id: 
- openreview_id: kMBvZ40Iu9
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c8277e98462d412e31c95d7ba1c89741ec2700e4.pdf
- published: 2024

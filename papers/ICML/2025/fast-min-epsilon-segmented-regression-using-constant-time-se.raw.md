---
title: "Fast Min-$\\epsilon$ Segmented Regression using Constant-Time Segment Merging"
authors: ["Ansgar Lößer", "Max Schlecht", "Florian Schintke", "Joel Witzke", "Matthias Weidlich", "Björn Scheuermann"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "w2QNIkcwWw"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d20f8efb3c7c1f67cb0933bfba1373703fbfaa90.pdf"
published: "2025"
categories: []
keywords: ["Regression", "Segmented Regression", "Time-Series Analysis"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:04+09:00"
---

# Fast Min-$\epsilon$ Segmented Regression using Constant-Time Segment Merging

## Abstract
Segmented regression is a statistical method that approximates a function $f$ by a piecewise function $\hat{f}$ using noisy data samples.
*Min-$\epsilon$* approaches aim to reduce the regression function's mean squared error (MSE) for a given number of $k$ segments.
An optimal solution for *min-$\epsilon$* segmented regression is found in $\mathcal{O}(n^2)$ time (Bai & Perron, 1998; Yamamoto & Perron, 2013) for $n$ samples. For large datasets, current heuristics improve time complexity to $\mathcal{O}(n\log{n})$ (Acharya et al., 2016) but can result in large errors, especially when exactly $k$ segments are used.
We present a method for *min-$\epsilon$* segmented regression that combines the scalability of top existing heuristic solutions with a statistical efficiency similar to the optimal solution. This is achieved by using a new method to merge an initial set of segments using precomputed matrices from samples, allowing both merging and error calculation in constant time.
Our approach, using the same samples and parameter $k$, produces segments with up to 1,000 times lower MSE compared to Acharya et al. (2016) in about 100 times less runtime on data sets over $10^4$ samples.

## Metadata
- venue: ICML
- year: 2025
- authors: Ansgar Lößer, Max Schlecht, Florian Schintke, Joel Witzke, Matthias Weidlich, Björn Scheuermann
- arxiv_id: 
- openreview_id: w2QNIkcwWw
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d20f8efb3c7c1f67cb0933bfba1373703fbfaa90.pdf
- published: 2025
- keywords: Regression, Segmented Regression, Time-Series Analysis

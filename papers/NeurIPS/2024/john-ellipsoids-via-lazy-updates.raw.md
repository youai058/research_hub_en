---
title: "John Ellipsoids via Lazy Updates"
authors: ["David Woodruff", "Taisuke Yasuda"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "lCj0Rvr4D6"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/387c461aca4700294414362d200e7093395878a9.pdf"
published: "2024"
categories: []
keywords: ["John ellipsoid", "sketching", "sampling", "fast matrix multiplication"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:56+09:00"
---

# John Ellipsoids via Lazy Updates

## Abstract
We give a faster algorithm for computing an approximate John ellipsoid around $n$ points in $d$ dimensions. The best known prior algorithms are based on repeatedly computing the leverage scores of the points and reweighting them by these scores (Cohen et al., 2019). We show that this algorithm can be substantially sped up by delaying the computation of high accuracy leverage scores by using sampling, and then later computing multiple batches of high accuracy leverage scores via fast rectangular matrix multiplication. We also give low-space streaming algorithms for John ellipsoids using similar ideas.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: David Woodruff, Taisuke Yasuda
- arxiv_id: 
- openreview_id: lCj0Rvr4D6
- anthology_id: 
- pdf_url: https://openreview.net/pdf/387c461aca4700294414362d200e7093395878a9.pdf
- published: 2024
- keywords: John ellipsoid, sketching, sampling, fast matrix multiplication

---
title: "Efficient Minimum Bayes Risk Decoding using Low-Rank Matrix Completion Algorithms"
authors: ["Firas Trabelsi", "David Vilar", "Mara Finkelstein", "Markus Freitag"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "8iPobEKUUA"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9bbcf58c2b598d872745a424ff5012c33ff28ad7.pdf"
published: "2024"
categories: []
keywords: ["Machine Translation", "Minimum Bayes Risk", "Natural Language Processing", "Low-Rank Matrix Completion"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:38+09:00"
---

# Efficient Minimum Bayes Risk Decoding using Low-Rank Matrix Completion Algorithms

## Abstract
Minimum Bayes Risk (MBR) decoding is a powerful decoding strategy widely used for text generation tasks but its quadratic computational complexity limits its practical application. This paper presents a novel approach for approximating MBR decoding using matrix completion techniques, focusing on a machine translation task. We formulate MBR decoding as a matrix completion problem, where the utility metric scores between candidate hypotheses and reference translations form a low-rank matrix. First we empirically show that the scores matrices indeed have a low-rank structure. Then we exploit this by only computing a random subset of the scores and efficiently recover the missing entries in the matrix by applying the Alternating Least Squares (ALS) algorithm, thereby enabling fast approximation of the MBR decoding process. Our experimental results on machine translation tasks demonstrate that the proposed method requires 1/16 utility metric computations compared to the vanilla MBR decoding while achieving equal translation quality measured by COMET on the WMT22 dataset (en<>de, en<>ru). We also benchmark our method against other approximation methods and we show significant gains in quality.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Firas Trabelsi, David Vilar, Mara Finkelstein, Markus Freitag
- arxiv_id: 
- openreview_id: 8iPobEKUUA
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9bbcf58c2b598d872745a424ff5012c33ff28ad7.pdf
- published: 2024
- keywords: Machine Translation, Minimum Bayes Risk, Natural Language Processing, Low-Rank Matrix Completion

---
title: "Best-of-Infinity: Asymptotic Performance of Test-Time LLM Ensembling"
authors: ["Junpei Komiyama", "Daisuke Oba", "Masafumi Oyamada"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "3qiCnLf3jf"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f74b2d70426b4d8107a2176742dc728dcbe513eb.pdf"
published: "2026"
categories: []
keywords: ["LLM", "test-time compute", "majority voting", "LLM ensemble"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:24+09:00"
---

# Best-of-Infinity: Asymptotic Performance of Test-Time LLM Ensembling

## Abstract
We study best-of-$N$ for large language models (LLMs) where the selection is based on majority voting. In particular, we analyze the limit $N \to \infty$, which we denote as best-of-$\infty$. While this approach achieves impressive performance in the limit, it requires an infinite test-time budget. To address this, we propose an adaptive generation scheme that selects $N$ based on answer agreement, thereby efficiently allocating inference-time computation. Beyond adaptivity, we extend the framework to weighted ensembles of multiple LLMs, showing that such mixtures can outperform any individual model. The optimal ensemble weighting is formulated and efficiently computed as a mixed-integer linear program. Extensive experiments demonstrate the effectiveness of our approach. Our code is available at https://github.com/jkomiyama/BoInf-code-publish/.

## Metadata
- venue: ICLR
- year: 2026
- authors: Junpei Komiyama, Daisuke Oba, Masafumi Oyamada
- arxiv_id: 
- openreview_id: 3qiCnLf3jf
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f74b2d70426b4d8107a2176742dc728dcbe513eb.pdf
- published: 2026
- keywords: LLM, test-time compute, majority voting, LLM ensemble

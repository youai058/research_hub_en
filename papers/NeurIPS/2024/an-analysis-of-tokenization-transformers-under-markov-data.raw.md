---
title: "An Analysis of Tokenization: Transformers under Markov Data"
authors: ["Nived Rajaraman", "Jiantao Jiao", "Kannan Ramchandran"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "wm9JZq7RCe"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d6c78ee455f5fe6feda13258c2c22ffcc162624c.pdf"
published: "2024"
categories: []
keywords: ["Tokenization", "LLMs", "interpretability"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:35+09:00"
---

# An Analysis of Tokenization: Transformers under Markov Data

## Abstract
While there has been a large body of research attempting to circumvent tokenization for language modeling (Clark et al. 2022, Xue et al. 2022), the current consensus is that it is a necessary initial step for designing state-of-the-art performant language models. In this paper, we investigate tokenization from a theoretical point of view by studying the behavior of transformers on simple data generating processes. When trained on data drawn from certain simple $k^{\text{th}}$-order Markov processes for $k > 1$, transformers exhibit a surprising phenomenon - in the absence of tokenization, they empirically are incredibly slow or fail to learn the right distribution and predict characters according to a unigram model (Makkuva et al. 2024). With the addition of tokenization, however, we empirically observe that transformers break through this barrier and are able to model the probabilities of sequences drawn from the source near-optimally, achieving small cross-entropy loss. With this observation as starting point, we study the end-to-end cross-entropy loss achieved by transformers with and without tokenization. With the appropriate tokenization, we show that even the simplest unigram models (over tokens) learnt by transformers are able to model the probability of sequences drawn from $k^{\text{th}}$-order Markov sources near optimally. Our analysis provides a justification for the use of tokenization in practice through studying the behavior of transformers on Markovian data.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Nived Rajaraman, Jiantao Jiao, Kannan Ramchandran
- arxiv_id: 
- openreview_id: wm9JZq7RCe
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d6c78ee455f5fe6feda13258c2c22ffcc162624c.pdf
- published: 2024
- keywords: Tokenization, LLMs, interpretability

---
title: "Transformers as Unsupervised Learning Algorithms: A study on Gaussian Mixtures"
authors: ["Zhiheng Chen", "Ruofan Wu", "Guanhua Fang"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "4hKNGmjXVQ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f47649845352287db0fb61f1aebaa05fe4f251c2.pdf"
published: "2026"
categories: []
keywords: ["In-context learning", "Gaussian Mixture Models", "Theory"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:16+09:00"
---

# Transformers as Unsupervised Learning Algorithms: A study on Gaussian Mixtures

## Abstract
The transformer architecture has demonstrated remarkable capabilities in modern artificial intelligence, among which the capability of implicitly learning an internal model during inference time is widely believed to play a key role in the understanding of pre-trained large language models. However, most recent works have been focusing on studying supervised learning topics such as in-context learning, leaving the field of unsupervised learning largely unexplored.
    This paper investigates the capabilities of transformers in solving Gaussian Mixture Models (GMMs), a fundamental unsupervised learning problem through the lens of statistical estimation.
    We propose a transformer-based learning framework called Transformer for Gaussian Mixture Models (TGMM) that simultaneously learns to solve multiple GMM tasks using a shared transformer backbone. The learned models are empirically demonstrated to effectively mitigate the limitations of classical methods such as Expectation-Maximization (EM) or spectral algorithms, at the same time exhibit reasonable robustness to distribution shifts.
    Theoretically, we prove that transformers can efficiently approximate both the Expectation-Maximization (EM) algorithm and a core component of spectral methods—namely, cubic tensor power iterations. These results not only improve upon prior work on approximating the EM algorithm,
    but also provide, to our knowledge, the first theoretical guarantee that transformers can approximate high-order tensor operations.
    Our study bridges the gap between practical success and theoretical understanding, positioning transformers as versatile tools for unsupervised learning.

## Metadata
- venue: ICLR
- year: 2026
- authors: Zhiheng Chen, Ruofan Wu, Guanhua Fang
- arxiv_id: 
- openreview_id: 4hKNGmjXVQ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f47649845352287db0fb61f1aebaa05fe4f251c2.pdf
- published: 2026
- keywords: In-context learning, Gaussian Mixture Models, Theory

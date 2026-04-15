---
title: "Implicit Regularization of SGD Reduces Shortcut Learning"
authors: ["Nahal Mirzaie", "Alireza Alipanah", "Ali Abbasi", "Amirmahdi Farzane", "Hossein Jafarinia", "Erfan Sobhaei", "Mahdi Ghaznavi", "Amir Najafi", "Mahdieh Soleymani Baghshah", "Mohammad Hossein Rohban"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "CPdAB7H8mU"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b0b93bbd3cd4e530c700b9fa486af5bc67f70426.pdf"
published: "2026"
categories: []
keywords: ["Spurious Correlations", "Stochastic Gradient Descent (SGD)", "Implicit Regularization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:50+09:00"
---

# Implicit Regularization of SGD Reduces Shortcut Learning

## Abstract
Training with stochastic gradient descent (SGD) at moderately large learning rates has been observed to improve robustness against spurious correlations, strong correlation between non-predictive features and target labels. Yet, the mechanism underlying this effect remains unclear. In this work, we identify batch size as an additional critical factor and show that robustness gains arise from the implicit regularization of SGD, which intensifies with larger learning rates and smaller batch sizes. This implicit regularization reduces reliance on spurious or shortcut features, thereby enhancing robustness while preserving accuracy. Importantly, this effect appears unique to SGD: gradient descent (GD) does not confer the same benefit and may even exacerbate shortcut reliance. Theoretically, we establish this phenomenon in linear models by leveraging statistical formulations of spurious correlations, proving that SGD systematically suppresses spurious feature dependence. Empirically, we demonstrate that the effect extends to deep neural networks across multiple benchmarks. Our code is available at
\href{https://github.com/mirzanahal/sgd-implicit-regularization-shortcuts}{https://github.com/mirzanahal/sgd-implicit-regularization-shortcuts}.

## Metadata
- venue: ICLR
- year: 2026
- authors: Nahal Mirzaie, Alireza Alipanah, Ali Abbasi, Amirmahdi Farzane, Hossein Jafarinia, Erfan Sobhaei, Mahdi Ghaznavi, Amir Najafi, Mahdieh Soleymani Baghshah, Mohammad Hossein Rohban
- arxiv_id: 
- openreview_id: CPdAB7H8mU
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b0b93bbd3cd4e530c700b9fa486af5bc67f70426.pdf
- published: 2026
- keywords: Spurious Correlations, Stochastic Gradient Descent (SGD), Implicit Regularization

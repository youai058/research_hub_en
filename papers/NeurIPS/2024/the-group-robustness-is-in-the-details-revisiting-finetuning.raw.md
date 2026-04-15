---
title: "The Group Robustness is in the Details: Revisiting Finetuning under Spurious Correlations"
authors: ["Tyler LaBonte", "John Collins Hill", "Xinchen zhang", "Vidya Muthukumar", "Abhishek Kumar"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "eHzIwAhj06"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/de43893b167ffd92fa7be295fbe3cc22ed9d8d07.pdf"
published: "2024"
categories: []
keywords: ["spurious correlations", "group robustness", "distribution shift", "class balancing"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:30+09:00"
---

# The Group Robustness is in the Details: Revisiting Finetuning under Spurious Correlations

## Abstract
Modern machine learning models are prone to over-reliance on spurious correlations, which can often lead to poor performance on minority groups. In this paper, we identify surprising and nuanced behavior of finetuned models on worst-group accuracy via comprehensive experiments on four well-established benchmarks across vision and language tasks. We first show that the commonly used class-balancing techniques of mini-batch upsampling and loss upweighting can induce a decrease in worst-group accuracy (WGA) with training epochs, leading to performance no better than without class-balancing. While in some scenarios, removing data to create a class-balanced subset is more effective, we show this depends on group structure and propose a mixture method which can outperform both techniques. Next, we show that scaling pretrained models is generally beneficial for worst-group accuracy, but only in conjunction with appropriate class-balancing. Finally, we identify spectral imbalance in finetuning features as a potential source of group disparities --- minority group covariance matrices incur a larger spectral norm than majority groups once conditioned on the classes. Our results show more nuanced interactions of modern finetuned models with group robustness than was previously known. Our code is available at https://github.com/tmlabonte/revisiting-finetuning.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Tyler LaBonte, John Collins Hill, Xinchen zhang, Vidya Muthukumar, Abhishek Kumar
- arxiv_id: 
- openreview_id: eHzIwAhj06
- anthology_id: 
- pdf_url: https://openreview.net/pdf/de43893b167ffd92fa7be295fbe3cc22ed9d8d07.pdf
- published: 2024
- keywords: spurious correlations, group robustness, distribution shift, class balancing

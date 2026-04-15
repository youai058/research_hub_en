---
title: "Offline Model-Based Optimization by Learning to Rank"
authors: ["Rong-Xi Tan", "Ke Xue", "Shen-Huan Lyu", "Haopu Shang", "yaowang", "Yaoyuan Wang", "Fu Sheng", "Chao Qian"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "sb1HgVDLjN"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/cab089fdc71f81b0b8706e716323b829292e6eca.pdf"
published: "2025"
categories: []
keywords: ["Offline model-based optimization", "black-box optimization", "learning to rank", "learning to optimize"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:42+09:00"
---

# Offline Model-Based Optimization by Learning to Rank

## Abstract
Offline model-based optimization (MBO) aims to identify a design that maximizes a black-box function using only a fixed, pre-collected dataset of designs and their corresponding scores. This problem has garnered significant attention from both scientific and industrial domains. A common approach in offline MBO is to train a regression-based surrogate model by minimizing mean squared error (MSE) and then find the best design within this surrogate model by different optimizers (e.g., gradient ascent). However, a critical challenge is the risk of out-of-distribution errors, i.e., the surrogate model may typically overestimate the scores and mislead the optimizers into suboptimal regions. Prior works have attempted to address this issue in various ways, such as using regularization techniques and ensemble learning to enhance the robustness of the model, but it still remains. In this paper, we argue that regression models trained with MSE are not well-aligned with the primary goal of offline MBO, which is to \textit{select} promising designs rather than to predict their scores precisely. Notably, if a surrogate model can maintain the order of candidate designs based on their relative score relationships, it can produce the best designs even without precise predictions. To validate it, we conduct experiments to compare the relationship between the quality of the final designs and MSE, finding that the correlation is really very weak. In contrast, a metric that measures order-maintaining quality shows a significantly stronger correlation. Based on this observation, we propose learning a ranking-based model that leverages learning to rank techniques to prioritize promising designs based on their relative scores. We show that the generalization error on ranking loss can be well bounded. Empirical results across diverse tasks demonstrate the superior performance of our proposed ranking-based method than twenty existing methods. Our implementation is available at \url{https://github.com/lamda-bbo/Offline-RaM}.

## Metadata
- venue: ICLR
- year: 2025
- authors: Rong-Xi Tan, Ke Xue, Shen-Huan Lyu, Haopu Shang, yaowang, Yaoyuan Wang, Fu Sheng, Chao Qian
- arxiv_id: 
- openreview_id: sb1HgVDLjN
- anthology_id: 
- pdf_url: https://openreview.net/pdf/cab089fdc71f81b0b8706e716323b829292e6eca.pdf
- published: 2025
- keywords: Offline model-based optimization, black-box optimization, learning to rank, learning to optimize

---
title: "SOO-Bench: Benchmarks for Evaluating the Stability of Offline Black-Box Optimization"
authors: ["Hong Qian", "Yiyi Zhu", "Xiang Shu", "Shuo Liu", "Yaolin Wen", "Xin An", "Huakang Lu", "Aimin Zhou", "Ke Tang", "Yang Yu"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "bqf0aCF3Dd"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e86dbcf6bf5499508368c5309f8fce475e024730.pdf"
published: "2025"
categories: []
keywords: ["Offline Optimization", "Black-Box Optimization", "Stability", "Benchmarks"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:51+09:00"
---

# SOO-Bench: Benchmarks for Evaluating the Stability of Offline Black-Box Optimization

## Abstract
Black-box optimization aims to find the optima through building a model close to the black-box objective function based on function value evaluation. However, in many real-world tasks, such as the design of molecular formulas and mechanical structures, it is perilous, costly, or even infeasible to evaluate the objective function value of an actively sampled solution. In this situation, optimization can only be conducted via utilizing offline historical data, which yields offline black-box optimization. Different from the traditional goal that is to pursue the optimal solution, this paper emphasizes that the goal of offline optimization is to stably surpass the offline dataset during optimization procedure. Although benchmarks called Design-Bench already exist in this emerging field, it can hardly evaluate the stability of offline optimization and mainly provides real-world offline tasks and the corresponding offline datasets. To this end, this paper proposes benchmarks named SOO-Bench (i.e., Stable Offline Optimization Benchmarks) for offline black-box optimization algorithms, so as to systematically evaluate the stability of surpassing the offline dataset under different data distributions. Along with SOO-Bench, we also propose a stability indicator to measure the degree of stability. Specifically, SOO-Bench includes various real-world offline optimization tasks and offline datasets under different data distributions, involving the fields of satellites, materials science, structural mechanics, and automobile manufacturing. Empirically, baseline and state-of-the-art algorithms are tested and analyzed on SOO-Bench. Hopefully, SOO-Bench is expected to serve as a catalyst for the rapid developments of more novel and stable offline optimization methods. The code is available at \url{https://github.com/zhuyiyi-123/SOO-Bench}.

## Metadata
- venue: ICLR
- year: 2025
- authors: Hong Qian, Yiyi Zhu, Xiang Shu, Shuo Liu, Yaolin Wen, Xin An, Huakang Lu, Aimin Zhou, Ke Tang, Yang Yu
- arxiv_id: 
- openreview_id: bqf0aCF3Dd
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e86dbcf6bf5499508368c5309f8fce475e024730.pdf
- published: 2025
- keywords: Offline Optimization, Black-Box Optimization, Stability, Benchmarks

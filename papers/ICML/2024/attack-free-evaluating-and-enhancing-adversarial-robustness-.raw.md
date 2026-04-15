---
title: "Attack-free Evaluating and Enhancing Adversarial Robustness on Categorical Data"
authors: ["Yujun Zhou", "Yufei Han", "Haomin Zhuang", "Hongyan Bao", "Xiangliang Zhang"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "8ERo4jph0A"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/4dc758229d714078981a8087218739a3ef67b03d.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:33+09:00"
---

# Attack-free Evaluating and Enhancing Adversarial Robustness on Categorical Data

## Abstract
Research on adversarial robustness has predominantly focused on continuous inputs, leaving categorical inputs, especially tabular attributes, less examined. To echo this challenge, our work aims to evaluate and enhance the robustness of classification over categorical attributes against adversarial perturbations through efficient attack-free approaches. We propose a robustness evaluation metric named Integrated Gradient-Smoothed Gradient (IGSG). It is designed to evaluate the attributional sensitivity of each feature and the decision boundary of the classifier, two aspects that significantly influence adversarial risk, according to our theoretical analysis. Leveraging this metric, we develop an IGSG-based regularization to reduce adversarial risk by suppressing the sensitivity of categorical attributes. We conduct extensive empirical studies over categorical datasets of various application domains. The results affirm the efficacy of both IGSG and IGSG-based regularization. Notably, IGSG-based regularization surpasses the state-of-the-art robust training methods by a margin of approximately 0.4% to 12.2% on average in terms of adversarial accuracy, especially on high-dimension datasets. The code is available at https://github.com/YujunZhou/IGSG.

## Metadata
- venue: ICML
- year: 2024
- authors: Yujun Zhou, Yufei Han, Haomin Zhuang, Hongyan Bao, Xiangliang Zhang
- arxiv_id: 
- openreview_id: 8ERo4jph0A
- anthology_id: 
- pdf_url: https://openreview.net/pdf/4dc758229d714078981a8087218739a3ef67b03d.pdf
- published: 2024

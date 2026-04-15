---
title: "Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning"
authors: ["Michal Nauman", "Michał Bortkiewicz", "Piotr Miłoś", "Tomasz Trzcinski", "Mateusz Ostaszewski", "Marek Cygan"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "5vZzmCeTYu"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d561885e9c79779a955cf26ffe88fc4616faa08a.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:10+09:00"
---

# Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning

## Abstract
Recent advancements in off-policy Reinforcement Learning (RL) have significantly improved sample efficiency, primarily due to the incorporation of various forms of regularization that enable more gradient update steps than traditional agents. However, many of these techniques have been tested in limited settings, often on tasks from single simulation benchmarks and against well-known algorithms rather than a range of regularization approaches. This limits our understanding of the specific mechanisms driving RL improvements. To address this, we implemented over 60 different off-policy agents, each integrating established regularization techniques from recent state-of-the-art algorithms. We tested these agents across 14 diverse tasks from 2 simulation benchmarks, measuring training metrics related to overestimation, overfitting, and plasticity loss — issues that motivate the examined regularization techniques. Our findings reveal that while the effectiveness of a specific regularization setup varies with the task, certain combinations consistently demonstrate robust and superior performance. Notably, a simple Soft Actor-Critic agent, appropriately regularized, reliably finds a better-performing policy within the training regime, which previously was achieved mainly through model-based approaches.

## Metadata
- venue: ICML
- year: 2024
- authors: Michal Nauman, Michał Bortkiewicz, Piotr Miłoś, Tomasz Trzcinski, Mateusz Ostaszewski, Marek Cygan
- arxiv_id: 
- openreview_id: 5vZzmCeTYu
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d561885e9c79779a955cf26ffe88fc4616faa08a.pdf
- published: 2024

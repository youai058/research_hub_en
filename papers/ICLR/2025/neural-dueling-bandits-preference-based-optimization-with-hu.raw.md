---
title: "Neural Dueling Bandits: Preference-Based Optimization with Human Feedback"
authors: ["Arun Verma", "Zhongxiang Dai", "Xiaoqiang Lin", "Patrick Jaillet", "Bryan Kian Hsiang Low"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "VELhv9BBfn"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/875613f857a562bc6de9f80ec0421b5e179060b8.pdf"
published: "2025"
categories: []
keywords: ["Contextual Dueling Bandits", "Preferences Learning", "Human Feedback", "Neural Bandits", "Thompson Sampling"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:55+09:00"
---

# Neural Dueling Bandits: Preference-Based Optimization with Human Feedback

## Abstract
Contextual dueling bandit is used to model the bandit problems, where a learner's goal is to find the best arm for a given context using observed noisy human preference feedback over the selected arms for the past contexts. However, existing algorithms assume the reward function is linear, which can be complex and non-linear in many real-life applications like online recommendations or ranking web search results. To overcome this challenge, we use a neural network to estimate the reward function using preference feedback for the previously selected arms. We propose upper confidence bound- and Thompson sampling-based algorithms with sub-linear regret guarantees that efficiently select arms in each round. We also extend our theoretical results to contextual bandit problems with binary feedback, which is in itself a non-trivial contribution. Experimental results on the problem instances derived from synthetic datasets corroborate our theoretical results.

## Metadata
- venue: ICLR
- year: 2025
- authors: Arun Verma, Zhongxiang Dai, Xiaoqiang Lin, Patrick Jaillet, Bryan Kian Hsiang Low
- arxiv_id: 
- openreview_id: VELhv9BBfn
- anthology_id: 
- pdf_url: https://openreview.net/pdf/875613f857a562bc6de9f80ec0421b5e179060b8.pdf
- published: 2025
- keywords: Contextual Dueling Bandits, Preferences Learning, Human Feedback, Neural Bandits, Thompson Sampling

---
title: "Probabilistic Inference in Language Models via Twisted Sequential Monte Carlo"
authors: ["Stephen Zhao", "Rob Brekelmans", "Alireza Makhzani", "Roger Baker Grosse"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "frA0NNBS1n"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/eada04b50249701256b116303609e5684dc2beff.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:13+09:00"
---

# Probabilistic Inference in Language Models via Twisted Sequential Monte Carlo

## Abstract
Numerous capability and safety techniques of Large Language Models (LLMs), including RLHF, automated red-teaming, prompt engineering, and infilling, can be cast as sampling from an unnormalized target distribution defined by a given reward or potential function over the full sequence. In this work, we leverage the rich toolkit of Sequential Monte Carlo (SMC) for these probabilistic inference problems. In particular, we use learned twist functions to estimate the expected future value of the potential at each timestep, which enables us to focus inference-time computation on promising partial sequences. We propose a novel contrastive method for learning the twist functions, and establish connections with the rich literature of soft reinforcement learning. As a complementary application of our twisted SMC framework, we present methods for evaluating the accuracy of language model inference techniques using novel bidirectional SMC bounds on the log partition function. These bounds can be used to estimate the KL divergence between the inference and target distributions in both directions. We apply our inference evaluation techniques to show that twisted SMC is effective for sampling undesirable outputs from a pretrained model (a useful component of harmlessness training and automated red-teaming), generating reviews with varied sentiment, and performing infilling tasks.

## Metadata
- venue: ICML
- year: 2024
- authors: Stephen Zhao, Rob Brekelmans, Alireza Makhzani, Roger Baker Grosse
- arxiv_id: 
- openreview_id: frA0NNBS1n
- anthology_id: 
- pdf_url: https://openreview.net/pdf/eada04b50249701256b116303609e5684dc2beff.pdf
- published: 2024

---
title: "MuRating: A High Quality Data Selecting Approach to Multilingual Large Language Model Pretraining"
authors: ["Zhixun Chen", "Ping Guo", "Wenhan Han", "Yifan Zhang", "BINBINLIU", "Haobin Lin", "Fengze Liu", "Yan Zhao", "Bingni Zhang", "Taifeng Wang", "Yin Zheng", "Trevor Cohn", "Meng Fang"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "jHWCeU39Ft"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a40675df6170e80abf10600ec2e5716efe6e4785.pdf"
published: "2025"
categories: []
keywords: ["Natural Language Processing"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:39+09:00"
---

# MuRating: A High Quality Data Selecting Approach to Multilingual Large Language Model Pretraining

## Abstract
Data quality is a critical driver of large language model performance, yet existing model-based selection methods focus almost exclusively on English, neglecting other languages that are essential in the training mix for multilingual LLMs. We introduce MuRating, a scalable framework that transfers high-quality English data-quality signals into a multilingual autorater, capable of handling 17 languages. MuRating aggregates multiple English autoraters via pairwise comparisons to learn unified document quality scores, then projects these judgments through translation to train a multilingual evaluator on monolingual, cross-lingual, and parallel text pairs. Applied to web data, MuRating selects balanced subsets of English and multilingual content to pretrain LLaMA-architecture models of 1.2B and 7B parameters. Compared to strong baselines, including QuRater, FineWeb2-HQ, AskLLM, DCLM, our approach increases average accuracy on both English benchmarks and multilingual evaluations. Extensive analyses further validate that pairwise training provides greater stability and robustness than pointwise scoring, underscoring the effectiveness of MuRating as a general multilingual data-selection framework.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Zhixun Chen, Ping Guo, Wenhan Han, Yifan Zhang, BINBINLIU, Haobin Lin, Fengze Liu, Yan Zhao, Bingni Zhang, Taifeng Wang, Yin Zheng, Trevor Cohn, Meng Fang
- arxiv_id: 
- openreview_id: jHWCeU39Ft
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a40675df6170e80abf10600ec2e5716efe6e4785.pdf
- published: 2025
- keywords: Natural Language Processing

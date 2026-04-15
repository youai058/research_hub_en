---
title: "Language Imbalance Driven Rewarding for Multilingual Self-improving"
authors: ["Wen Yang", "Junhong Wu", "Chen Wang", "Chengqing Zong", "Jiajun Zhang"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Kak2ZH5Itp"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/71dfe2eb2ee164604eb4a4aaf296676ccd65f0db.pdf"
published: "2025"
categories: []
keywords: ["Large Language Model", "Self-Improving", "Multilinguality"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:49+09:00"
---

# Language Imbalance Driven Rewarding for Multilingual Self-improving

## Abstract
Large Language Models (LLMs) have achieved state-of-the-art performance across numerous tasks. However, these advancements have predominantly benefited "first-class" languages such as English and Chinese, leaving many other languages underrepresented. This imbalance, while limiting broader applications, generates a natural preference ranking between languages, offering an opportunity to bootstrap the multilingual capabilities of LLM in a self-improving manner. Thus, we propose $\textit{Language Imbalance Driven Rewarding}$, where the inherent imbalance between dominant and non-dominant languages within LLMs is leveraged as a reward signal. Iterative DPO training demonstrates that this approach not only enhances LLM performance in non-dominant languages but also improves the dominant language's capacity, thereby yielding an iterative reward signal. Fine-tuning Meta-Llama-3-8B-Instruct over two iterations of this approach results in continuous improvements in multilingual performance across instruction-following and arithmetic reasoning tasks, evidenced by an average improvement of 7.46\% win rate on the X-AlpacaEval leaderboard and 13.9\% accuracy on the MGSM benchmark. This work serves as an initial exploration, paving the way for multilingual self-improvement of LLMs.

## Metadata
- venue: ICLR
- year: 2025
- authors: Wen Yang, Junhong Wu, Chen Wang, Chengqing Zong, Jiajun Zhang
- arxiv_id: 
- openreview_id: Kak2ZH5Itp
- anthology_id: 
- pdf_url: https://openreview.net/pdf/71dfe2eb2ee164604eb4a4aaf296676ccd65f0db.pdf
- published: 2025
- keywords: Large Language Model, Self-Improving, Multilinguality

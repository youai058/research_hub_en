---
title: "Large language models can learn and generalize steganographic chain-of-thought under process supervision"
authors: ["Robert McCarthy", "Joey SKAF", "Luis Ibanez-Lissen", "Vasil Georgiev", "Connor Watts", "Hannes Whittingham", "Lorena Gonzalez-Manzano", "Cameron Tice", "Edward James Young", "Puria Radmard", "David Lindner"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "2g5cJqX15Y"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a4499bf01db396810920b93ba85dec92e6ac6e43.pdf"
published: "2025"
categories: []
keywords: ["AI Safety", "AI Control", "Steganography", "Encoded Reasoning", "Chain-of-Thought", "Reinforcement Learning", "LLMs"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:38+09:00"
---

# Large language models can learn and generalize steganographic chain-of-thought under process supervision

## Abstract
Chain-of-thought (CoT) reasoning not only enhances large language model performance but also provides critical insights into decision-making processes, marking it as a useful tool for monitoring model intent and planning. By proactively preventing models from acting on CoT indicating misaligned or harmful intent, CoT monitoring can be used to reduce risks associated with deploying models. However, developers may be incentivized to train away the appearance of harmful intent from CoT traces, by either customer preferences or regulatory requirements. However, recent works have shown that banning the mention of a specific example of reward hacking causes obfuscation of the undesired reasoning traces but the persistence of the undesired behavior, threatening the reliability of CoT monitoring. However, obfuscation of reasoning can be due to its internalization to latent space computation, or its encoding within the CoT. We provide an extension to these results with regard to the ability of models to learn a specific type of obfuscated reasoning: steganography. First, we show that penalizing the use of specific strings within load-bearing reasoning traces causes models to substitute alternative strings. Crucially, this does not alter the underlying method by which the model performs the task, demonstrating that the model can learn to steganographically encode its reasoning. This is an example of models learning to encode their reasoning. We further demonstrate that models can generalize an encoding scheme. When the penalized strings belong to an overarching class, the model learns not only to substitute strings seen in training, but also develops a general encoding scheme for all members of the class which it can apply to held-out testing strings.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Robert McCarthy, Joey SKAF, Luis Ibanez-Lissen, Vasil Georgiev, Connor Watts, Hannes Whittingham, Lorena Gonzalez-Manzano, Cameron Tice, Edward James Young, Puria Radmard, David Lindner
- arxiv_id: 
- openreview_id: 2g5cJqX15Y
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a4499bf01db396810920b93ba85dec92e6ac6e43.pdf
- published: 2025
- keywords: AI Safety, AI Control, Steganography, Encoded Reasoning, Chain-of-Thought, Reinforcement Learning, LLMs

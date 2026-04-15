---
title: "SafeAuto: Knowledge-Enhanced Safe Autonomous Driving with Multimodal Foundation Models"
authors: ["Jiawei Zhang", "Xuan Yang", "Taiqi Wang", "Yu Yao", "Aleksandr Petiushko", "Bo Li"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "nKJGjovmZz"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/5022d626a5436513ba5cbe6a32e6c4b74cfbb7d9.pdf"
published: "2025"
categories: []
keywords: ["Autonomous Driving; Multimodal Large Language Models; Multimodal Retrieval-Augmented Generation; Probabilistic Graph Model; Markov Logic Network"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:26+09:00"
---

# SafeAuto: Knowledge-Enhanced Safe Autonomous Driving with Multimodal Foundation Models

## Abstract
Traditional autonomous driving systems often struggle to connect high-level reasoning with low-level control, leading to suboptimal and sometimes unsafe behaviors. Recent advances in multimodal large language models (MLLMs), which process both visual and textual data, offer an opportunity to unify perception and reasoning. However, effectively embedding precise safety knowledge into MLLMs for autonomous driving remains a significant challenge.
To address this, we propose SafeAuto, a framework that enhances MLLM-based autonomous driving by incorporating both unstructured and structured knowledge. First, we introduce a Position-Dependent Cross-Entropy (PDCE) loss to improve low-level control signal predictions when values are represented as text. Second, to explicitly integrate safety knowledge, we develop a reasoning component that translates traffic rules into first-order logic (e.g., "red light => stop") and embeds them into a probabilistic graphical model (e.g., Markov Logic Network) to verify predicted actions using recognized environmental attributes.
Additionally, our Multimodal Retrieval-Augmented Generation (RAG) model leverages video, control signals, and environmental attributes to learn from past driving experiences. Integrating PDCE, MLN, and Multimodal RAG, SafeAuto outperforms existing baselines across multiple datasets, enabling more accurate, reliable, and safer autonomous driving. The code is available at https://github.com/AI-secure/SafeAuto.

## Metadata
- venue: ICML
- year: 2025
- authors: Jiawei Zhang, Xuan Yang, Taiqi Wang, Yu Yao, Aleksandr Petiushko, Bo Li
- arxiv_id: 
- openreview_id: nKJGjovmZz
- anthology_id: 
- pdf_url: https://openreview.net/pdf/5022d626a5436513ba5cbe6a32e6c4b74cfbb7d9.pdf
- published: 2025
- keywords: Autonomous Driving; Multimodal Large Language Models; Multimodal Retrieval-Augmented Generation; Probabilistic Graph Model; Markov Logic Network

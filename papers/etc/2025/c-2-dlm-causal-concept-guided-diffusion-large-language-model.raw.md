---
title: "C$^2$DLM: Causal Concept-Guided Diffusion Large Language Models"
authors: ["Kairong Han", "Nuanqiao Shan", "Ziyu Zhao", "Zijing Hu", "Xinpeng Dong", "Junjian Ye", "Lujia Pan", "Fei Wu", "Kun Kuang"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2511.22146"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2511.22146v1"
published: "2025-11-27"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:03+09:00"
---

# C$^2$DLM: Causal Concept-Guided Diffusion Large Language Models

## Abstract
Autoregressive (AR) language models and Diffusion Language Models (DLMs) constitute the two principal paradigms of large language models. However, both paradigms suffer from insufficient reasoning capabilities. Human reasoning inherently relies on causal knowledge and thought, which are reflected in natural language. But in the AR paradigm, language is modeled as next token prediction (a strictly left-to-right, token-by-token order), whereas natural language itself exhibits more flexible causal structures. In the DLM paradigm, the attention mechanism is fully connected, which entirely disregards causal order. To fill this gap, we propose a \underline{\textbf{C}}ausal \underline{\textbf{C}}oncept-Guided \underline{\textbf{D}}iffusion \underline{\textbf{L}}anguage \underline{\textbf{M}}odel (C$^2$DLM). Starting from DLM's fully connected attention, C$^2$DLM first obtains a concept-level causal graph from the teacher model, and then explicitly guides attention to learn causal relationships between concepts. By focusing on causal relationships and avoiding interference from difficult subgoals involving causal inversion, C$^2$DLM improves 12\% with about 3.2 times training speedup in the COT-OrderPerturb task, and achieves an average gain of 1.31\% across six downstream reasoning tasks. More details in the repository ~\href{https://github.com/Kairong-Han/C-2-DLM}{here}.

## Metadata
- venue: arXiv
- year: 2025
- authors: Kairong Han, Nuanqiao Shan, Ziyu Zhao, Zijing Hu, Xinpeng Dong, Junjian Ye, Lujia Pan, Fei Wu, Kun Kuang
- arxiv_id: 2511.22146
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2511.22146v1
- published: 2025-11-27

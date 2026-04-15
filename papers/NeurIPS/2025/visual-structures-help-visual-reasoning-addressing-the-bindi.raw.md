---
title: "Visual Structures Help Visual Reasoning:  Addressing the Binding Problem in LVLMs"
authors: ["Amirmohammad Izadi", "Mohammadali Banayeeanzade", "Fatemeh Askari", "Ali Rahimiakbar", "Mohammad Mahdi Vahedi", "Hosein Hasani", "Mahdieh Soleymani Baghshah"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "T52hZeT7rn"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9aa6856102d8ec332673e3b3497a2c653885bfee.pdf"
published: "2025"
categories: []
keywords: ["Visual Reasoning", "Large Vision-Language Models", "Cognitive Science", "Binding Problem"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:00+09:00"
---

# Visual Structures Help Visual Reasoning:  Addressing the Binding Problem in LVLMs

## Abstract
Despite progress in Large Vision-Language Models (LVLMs), their capacity for visual reasoning is often limited by the binding problem: the failure to reliably associate perceptual features with their correct visual referents. This limitation underlies persistent errors in tasks such as counting, visual search, scene description, and spatial relationship understanding. A key factor is that current LVLMs process visual features largely in parallel, lacking mechanisms for spatially grounded, serial attention.
This paper introduces Visual Input Structure for Enhanced Reasoning (VISER), a simple, effective method that augments visual inputs with low-level spatial structures and pairs them with a textual prompt that encourages sequential, spatially-aware parsing. We empirically demonstrate substantial performance improvements across core visual reasoning tasks, using only a single-query inference. Specifically, VISER improves GPT-4o performance on visual search, counting, and spatial relationship tasks by 25.0%, 26.8%, and 9.5%, respectively, and reduces edit distance error in scene description by 0.32 on 2D datasets.
Furthermore, we find that the visual modification is essential for these gains; purely textual strategies, including Chain-of-Thought prompting, are insufficient and can even degrade performance. VISER underscores the importance of visual input design over purely linguistically based reasoning strategies and suggests that visual structuring is a powerful and general approach for enhancing compositional and spatial reasoning in LVLMs.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Amirmohammad Izadi, Mohammadali Banayeeanzade, Fatemeh Askari, Ali Rahimiakbar, Mohammad Mahdi Vahedi, Hosein Hasani, Mahdieh Soleymani Baghshah
- arxiv_id: 
- openreview_id: T52hZeT7rn
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9aa6856102d8ec332673e3b3497a2c653885bfee.pdf
- published: 2025
- keywords: Visual Reasoning, Large Vision-Language Models, Cognitive Science, Binding Problem

---
title: "Look Before You Leap: Universal Emergent Mechanism for Retrieval in Language Models"
authors: ["Alexandre Variengien", "Eric Winsor"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "eIB1UZFcFg"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/854c18cf8ac4beef857c5bc89c8b149d2aad222b.pdf"
published: "2025"
categories: []
keywords: ["Interpretability", "LLM", "Universality"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:53+09:00"
---

# Look Before You Leap: Universal Emergent Mechanism for Retrieval in Language Models

## Abstract
When solving challenging problems, language models (LMs) are able to identify relevant information from long and complicated contexts. To study how LMs solve retrieval tasks in diverse situations, we introduce ORION, a collection of structured retrieval tasks spanning six domains, from text understanding to coding. Each task in ORION can be represented abstractly by a request (e.g. a question) that retrieves an attribute (e.g. the character name) from a context (e.g. a story). We apply causal analysis on 18 open-source language models with sizes ranging from 125 million to 70 billion parameters. We find that LMs internally decompose retrieval tasks in a modular way: middle layers at the last token position process the request, while late layers retrieve the correct entity from the context. After causally enforcing this decomposition, models are still able to solve the original task, preserving 70% of the original correct token probability in 98 of the 106 studied model-task pairs. We connect our macroscopic decomposition with a microscopic description by performing a fine-grained case study of a question-answering task on Pythia-2.8b. Building on our high-level understanding, we demonstrate a proof of concept application for scalable internal oversight of LMs to mitigate prompt-injection while requiring human supervision on only a single input. Our solution improves accuracy drastically (from 15.5% to 97.5% on Pythia-12b). This work presents evidence of a universal emergent modular processing of tasks across varied domains and models and is a pioneering effort in applying interpretability for scalable internal oversight of LMs.

## Metadata
- venue: ICLR
- year: 2025
- authors: Alexandre Variengien, Eric Winsor
- arxiv_id: 
- openreview_id: eIB1UZFcFg
- anthology_id: 
- pdf_url: https://openreview.net/pdf/854c18cf8ac4beef857c5bc89c8b149d2aad222b.pdf
- published: 2025
- keywords: Interpretability, LLM, Universality

---
title: "ICLR: In-Context Learning of Representations"
authors: ["Core Francisco Park", "Andrew Lee", "Ekdeep Singh Lubana", "Yongyi Yang", "Maya Okawa", "Kento Nishi", "Martin Wattenberg", "Hidenori Tanaka"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "pXlmOmlHJZ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/68f0954324b0bb9a57a8d23b52d90953165dd8a1.pdf"
published: "2025"
categories: []
keywords: ["In-Context Learning", "Representational Geometry", "World Models", "Emergence", "Percolation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:00+09:00"
---

# ICLR: In-Context Learning of Representations

## Abstract
Recent work demonstrates that structured patterns in pretraining data influence how representations of different concepts are organized in a large language model’s (LLM) internals, with such representations then driving downstream abilities. Given the open-ended nature of LLMs, e.g., their ability to in-context learn novel tasks, we ask whether models can flexibly alter their semantically grounded organization of concepts. Specifically, if we provide in-context exemplars wherein a concept plays a different role than what the pretraining data suggests, can models infer these novel semantics and reorganize representations in accordance with them? To answer this question, we define a toy “graph tracing” task wherein the nodes of the graph are referenced via concepts seen during training (e.g., apple, bird, etc.), and the connectivity of the graph is defined via some predefined structure (e.g., a square grid). Given exemplars that indicate traces of random walks on the graph, we analyze intermediate representations of the model and find that as the amount of context is scaled, there is a sudden re-organization of representations according to the graph’s structure. Further, we find that when reference concepts have correlations in their semantics (e.g., Monday, Tuesday, etc.), the context-specified graph structure is still present in the representations, but is unable to dominate the pretrained structure. To explain these results, we analogize our task to energy minimization for a predefined graph topology, which shows getting non-trivial performance on the task requires for the model to infer a connected component. Overall, our findings indicate context-size may be an underappreciated scaling axis that can flexibly re-organize model representations, unlocking novel capabilities.

## Metadata
- venue: ICLR
- year: 2025
- authors: Core Francisco Park, Andrew Lee, Ekdeep Singh Lubana, Yongyi Yang, Maya Okawa, Kento Nishi, Martin Wattenberg, Hidenori Tanaka
- arxiv_id: 
- openreview_id: pXlmOmlHJZ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/68f0954324b0bb9a57a8d23b52d90953165dd8a1.pdf
- published: 2025
- keywords: In-Context Learning, Representational Geometry, World Models, Emergence, Percolation

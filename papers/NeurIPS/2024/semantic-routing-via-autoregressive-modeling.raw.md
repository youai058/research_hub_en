---
title: "Semantic Routing via Autoregressive Modeling"
authors: ["Eric Zhao", "Pranjal Awasthi", "Zhengdao Chen", "Sreenivas Gollapudi", "Daniel Delling"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "JvlrUFJMbI"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/8635a8893063868aa7a04c8d886ed7646a01c21d.pdf"
published: "2024"
categories: []
keywords: ["semantic routing", "routing on graphs", "autoregressive modeling"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:58+09:00"
---

# Semantic Routing via Autoregressive Modeling

## Abstract
We study learning-based approaches to semantic route planning, which concerns producing routes in response to rich queries that specify various criteria and preferences. Semantic routing is already widely found in industry applications, especially navigational services like Google Maps; however, existing implementations only support limited route criteria and narrow query sets as they rely on repurposing classical route optimization algorithms. We argue for a learning-based approach to semantic routing as a more scalable and general alternative. To foster interest in this important application of graph learning, we are releasing a large-scale publicly-licensed benchmark for semantic routing consisting of real-world multi-objective navigation problems---expressed via natural language queries---on the richly annotated road networks of US cities. In addition to being intractable with existing approaches to semantic routing, our benchmark poses a significant scaling challenge for graph learning methods. As a proof-of-concept, we show that---at scale---even a standard transformer network is a powerful semantic routing system and achieves non-trivial performance on our benchmark. In the process, we demonstrate a simple solution to the challenge of scaling up graph learning: an autoregressive approach that decomposes semantic routing into smaller ``next-edge'' prediction problems.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Eric Zhao, Pranjal Awasthi, Zhengdao Chen, Sreenivas Gollapudi, Daniel Delling
- arxiv_id: 
- openreview_id: JvlrUFJMbI
- anthology_id: 
- pdf_url: https://openreview.net/pdf/8635a8893063868aa7a04c8d886ed7646a01c21d.pdf
- published: 2024
- keywords: semantic routing, routing on graphs, autoregressive modeling

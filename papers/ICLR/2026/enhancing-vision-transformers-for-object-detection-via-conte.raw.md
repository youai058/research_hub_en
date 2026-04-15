---
title: "Enhancing Vision Transformers for Object Detection via Context-Aware Token Selection and Packing"
authors: ["Tianyi Zhang", "Baoxin Li", "Jae-sun Seo", "Yu Cao"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Q1LVcZ1PWc"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c7b2ff1bee7d67554a154727f4184b9bf8910432.pdf"
published: "2026"
categories: []
keywords: ["vision transformer", "object detection"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:49+09:00"
---

# Enhancing Vision Transformers for Object Detection via Context-Aware Token Selection and Packing

## Abstract
In recent years, the long-range attention mechanism of vision transformers has driven significant performance breakthroughs across various computer vision tasks. However, these advancements come at the cost of inefficiency and substantial computational expense, especially when dealing with sparse data. While sparse attention mechanisms have been introduced to mitigate these issues by pruning tokens involved in attention, they often lack context-awareness and intelligence, frequently limiting the number of selected tokens uniformly across different inputs. To address these challenges, we propose a novel algorithm: Select and Pack Attention (SPA). SPA dynamically selects informative tokens using a low-cost gating layer and packs these selected tokens into new batches, allowing for a variable number of tokens to be used in GPU batch training and inference. Through extensive experiments on diverse datasets and multiple computer vision tasks, our method demonstrates superior performance and efficiency, including a 0.5-2.7 AP improvement in object detection and a 10.9%-24.9% reduction in computation.

## Metadata
- venue: ICLR
- year: 2026
- authors: Tianyi Zhang, Baoxin Li, Jae-sun Seo, Yu Cao
- arxiv_id: 
- openreview_id: Q1LVcZ1PWc
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c7b2ff1bee7d67554a154727f4184b9bf8910432.pdf
- published: 2026
- keywords: vision transformer, object detection

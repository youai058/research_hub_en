---
title: "Boosting Neural Combinatorial Optimization for Large-Scale Vehicle Routing Problems"
authors: ["Fu Luo", "Xi Lin", "Yaoxin Wu", "Zhenkun Wang", "Tong Xialiang", "Mingxuan Yuan", "Qingfu Zhang"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "TbTJJNjumY"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ba45c4b0897675dfcbfb88a538bcd7c390375a89.pdf"
published: "2025"
categories: []
keywords: ["Neural Combinatorial Optimization", "Large-Scale Vehicle Routing Problem"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:44+09:00"
---

# Boosting Neural Combinatorial Optimization for Large-Scale Vehicle Routing Problems

## Abstract
Neural Combinatorial Optimization (NCO) methods have exhibited promising performance in solving Vehicle Routing Problems (VRPs). However, most NCO methods rely on the conventional self-attention mechanism that induces excessive computational complexity, thereby struggling to contend with large-scale VRPs and hindering their practical applicability. In this paper, we propose a lightweight cross-attention mechanism with linear complexity, by which a Transformer network is developed to learn efficient and favorable solutions for large-scale VRPs. We also propose a Self-Improved Training (SIT) algorithm that enables direct model training on large-scale VRP instances, bypassing extensive computational overhead for attaining labels. By iterating solution reconstruction, the Transformer network itself can generate improved partial solutions as pseudo-labels to guide the model training. Experimental results on the Travelling Salesman Problem (TSP) and the Capacitated Vehicle Routing Problem (CVRP) with up to 100K nodes indicate that our method consistently achieves superior performance for synthetic and real-world benchmarks, significantly boosting the scalability of NCO methods.

## Metadata
- venue: ICLR
- year: 2025
- authors: Fu Luo, Xi Lin, Yaoxin Wu, Zhenkun Wang, Tong Xialiang, Mingxuan Yuan, Qingfu Zhang
- arxiv_id: 
- openreview_id: TbTJJNjumY
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ba45c4b0897675dfcbfb88a538bcd7c390375a89.pdf
- published: 2025
- keywords: Neural Combinatorial Optimization, Large-Scale Vehicle Routing Problem

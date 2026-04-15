---
title: "Optimizing Neural Network Representations of Boolean Networks"
authors: ["Joshua Russell", "Ignacio Gavier", "Devdhar Patel", "Edward Rietman", "Hava T Siegelmann"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "1H90Gb9rJ9"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/122a7853d998069ab163d155bec1ceac11319045.pdf"
published: "2025"
categories: []
keywords: ["Neural Networks", "Boolean Networks", "Lossless Optimization", "Integer Linear Programming", "NPN Classification"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:17+09:00"
---

# Optimizing Neural Network Representations of Boolean Networks

## Abstract
Neural networks are known to be universal computers for Boolean functions. Recent advancements in hardware have significantly reduced matrix multiplication times, making neural network simulation both fast and efficient. Consequently, functions defined by complex Boolean networks are increasingly viable candidates for simulation through their neural network representation. Prior research has introduced a general method for deriving neural network representations of Boolean networks. However, the resulting neural networks are often suboptimal in terms of the number of neurons and connections, leading to slower simulation performance. Optimizing them while preserving functional equivalence --lossless optimization-- is an NP-hard problem, and current methods only provide lossy solutions. In this paper, we present a deterministic algorithm to optimize such neural networks in terms of neurons and connections while preserving functional equivalence. Moreover, to accelerate the compression of the neural network, we introduce an objective-aware algorithm that exploits representations that are shared among subproblems of the overall optimization. We demonstrate experimentally that we are able to reduce connections and neurons by up to 70% and 60%, respectively, in comparison to state-of-the-art. We also find that our objective-aware algorithm results in consistent speedups in optimization time, achieving up to 34.3x and 5.9x speedup relative to naive and caching solutions, respectively. Our methods are of practical relevance to applications such as high-throughput circuit simulation and placing neurosymbolic systems on the same hardware architecture.

## Metadata
- venue: ICLR
- year: 2025
- authors: Joshua Russell, Ignacio Gavier, Devdhar Patel, Edward Rietman, Hava T Siegelmann
- arxiv_id: 
- openreview_id: 1H90Gb9rJ9
- anthology_id: 
- pdf_url: https://openreview.net/pdf/122a7853d998069ab163d155bec1ceac11319045.pdf
- published: 2025
- keywords: Neural Networks, Boolean Networks, Lossless Optimization, Integer Linear Programming, NPN Classification

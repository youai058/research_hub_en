---
title: "Compositional Flows for 3D Molecule and Synthesis Pathway Co-design"
authors: ["Tony Shen", "Seonghwan Seo", "Ross Irwin", "Kieran Didi", "Simon Olsson", "Woo Youn Kim", "Martin Ester"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "4aXfSLfM0Z"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/244d8124865e242a22a5f494a1624c39fb2a15b1.pdf"
published: "2025"
categories: []
keywords: ["drug discovery", "synthesizable molecular design", "GFlowNets", "flow matching"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:41+09:00"
---

# Compositional Flows for 3D Molecule and Synthesis Pathway Co-design

## Abstract
Many generative applications, such as synthesis-based 3D molecular design, involve constructing compositional objects with continuous features.
Here, we introduce Compositional Generative Flows (CGFlow), a novel framework that extends flow matching to generate objects in compositional steps while modeling continuous states. 
Our key insight is that modeling compositional state transitions can be formulated as a straightforward extension of the flow matching interpolation process.
We further build upon the theoretical foundations of generative flow networks (GFlowNets), enabling reward-guided sampling of compositional structures. 
We apply CGFlow to synthesizable drug design by jointly designing the molecule's synthetic pathway with its 3D binding pose.
Our approach achieves state-of-the-art binding affinity and synthesizability on all 15 targets from the LIT-PCBA benchmark, and 4.2x improvement in sampling efficiency compared to 2D synthesis-based baseline.
To our best knowledge, our method is also the first to achieve state of-art-performance in both Vina Dock (-9.42) and AiZynth success rate (36.1\%) on the CrossDocked2020 benchmark.

## Metadata
- venue: ICML
- year: 2025
- authors: Tony Shen, Seonghwan Seo, Ross Irwin, Kieran Didi, Simon Olsson, Woo Youn Kim, Martin Ester
- arxiv_id: 
- openreview_id: 4aXfSLfM0Z
- anthology_id: 
- pdf_url: https://openreview.net/pdf/244d8124865e242a22a5f494a1624c39fb2a15b1.pdf
- published: 2025
- keywords: drug discovery, synthesizable molecular design, GFlowNets, flow matching

---
title: "CombiMOTS: Combinatorial Multi-Objective Tree Search for Dual-Target Molecule Generation"
authors: ["Thibaud Southiratn", "Bonil Koo", "Yijingxiu Lu", "Sun Kim"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "FSlTEObdLl"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/28bbf6e4e551d760dc2420b58e3e4ad675bb40d0.pdf"
published: "2025"
categories: []
keywords: ["Dual-target Molecule Generation", "Fragment-based Drug Discovery", "Monte-Carlo Tree Search", "Pareto Optimization", "Search Space Reduction"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:05+09:00"
---

# CombiMOTS: Combinatorial Multi-Objective Tree Search for Dual-Target Molecule Generation

## Abstract
Dual-target molecule generation, which focuses on discovering compounds capable of interacting with two target proteins, has garnered significant attention due to its potential for improving therapeutic efficiency, safety and resistance mitigation.
Existing approaches face two critical challenges.
First, by simplifying the complex dual-target optimization problem to scalarized combinations of individual objectives, they fail to capture important trade-offs between target engagement and molecular properties. 
Second, they typically do not integrate synthetic planning into the generative process.
This highlights a need for more appropriate objective function design and synthesis-aware methodologies tailored to the dual-target molecule generation task.
In this work, we propose CombiMOTS, a Pareto Monte Carlo Tree Search (PMCTS) framework that generates dual-target molecules.
CombiMOTS is designed to explore a synthesizable fragment space while employing vectorized optimization constraints to encapsulate target affinity and physicochemical properties.
Extensive experiments on real-world databases demonstrate that CombiMOTS produces novel dual-target molecules with high docking scores, enhanced diversity, and balanced pharmacological characteristics, showcasing its potential as a powerful tool for dual-target drug discovery.
The code and data is accessible through \url{https://github.com/Tibogoss/CombiMOTS}.

## Metadata
- venue: ICML
- year: 2025
- authors: Thibaud Southiratn, Bonil Koo, Yijingxiu Lu, Sun Kim
- arxiv_id: 
- openreview_id: FSlTEObdLl
- anthology_id: 
- pdf_url: https://openreview.net/pdf/28bbf6e4e551d760dc2420b58e3e4ad675bb40d0.pdf
- published: 2025
- keywords: Dual-target Molecule Generation, Fragment-based Drug Discovery, Monte-Carlo Tree Search, Pareto Optimization, Search Space Reduction

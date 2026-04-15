---
title: "HeurekaBench: A Benchmarking Framework for AI Co-scientist"
authors: ["Siba Smarak Panigrahi", "Jovana Videnović", "Maria Brbic"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Y7xCdFuFw7"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a0cd04faa1803c9665422e360d6ede26fac83559.pdf"
published: "2026"
categories: []
keywords: ["agents", "benchmarks for agents", "LLMs", "single-cell biology"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:32+09:00"
---

# HeurekaBench: A Benchmarking Framework for AI Co-scientist

## Abstract
LLM-based reasoning models have enabled the development of agentic systems that act as co-scientists, assisting in multi-step scientific analysis. However, evaluating these systems is challenging, as it requires realistic, end-to-end research scenarios that integrate data analysis, interpretation, and the generation of new insights from the experimental data. To address this limitation, we introduce HeurekaBench, a framework to create benchmarks with *exploratory, open-ended research questions* for experimental datasets.
Each such question is grounded in a scientific study and its corresponding code repository, and is created using a semi-automated pipeline that leverages multiple LLMs to extract insights and generate candidate workflows, which are then verified against reported findings. We instantiate the framework in single-cell biology to obtain sc-HeurekaBench benchmark and use it to compare state-of-the-art single-cell agents. We further showcase the benefits of our benchmark for quantitatively analyzing current design choices in agentic systems. We find that the addition of a *critic* module can improve ill-formed responses for open-source LLM-based agents by up to 22% and close the gap with their closed-source counterparts. Overall, HeurekaBench sets a path toward rigorous, end-to-end evaluation of scientific agents, grounding benchmark construction in real scientific workflows.

## Metadata
- venue: ICLR
- year: 2026
- authors: Siba Smarak Panigrahi, Jovana Videnović, Maria Brbic
- arxiv_id: 
- openreview_id: Y7xCdFuFw7
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a0cd04faa1803c9665422e360d6ede26fac83559.pdf
- published: 2026
- keywords: agents, benchmarks for agents, LLMs, single-cell biology

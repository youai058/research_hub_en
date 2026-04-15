---
title: "Diverse Preference Learning for Capabilities and Alignment"
authors: ["Stewart Slocum", "Asher Parker-Sartori", "Dylan Hadfield-Menell"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "pOq9vDIYev"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2c1b1d62f868031970a42629ecefb76a107db304.pdf"
published: "2025"
categories: []
keywords: ["alignment", "diversity", "natural language processing", "reinforcement learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:02+09:00"
---

# Diverse Preference Learning for Capabilities and Alignment

## Abstract
As LLMs increasingly impact society, their ability to represent diverse perspectives is critical.  However, recent studies reveal that alignment algorithms such as RLHF and DPO significantly reduce the diversity of LLM outputs. Not only do aligned LLMs generate text with repetitive structure and word choice, they also approach problems in more uniform ways, and their responses reflect a narrower range of societal perspectives. We attribute this problem to the KL divergence regularizer employed in preference learning algorithms. This causes the model to overweight majority opinions and sacrifice diversity in exchange for optimal reward. To address this, we propose Soft Preference Learning, which decouples the entropy and cross-entropy terms in the KL penalty — allowing for fine-grained control over LLM generation diversity. From a capabilities perspective, LLMs trained using Soft Preference Learning attain higher accuracy on difficult repeated sampling tasks and produce outputs with greater semantic and lexical diversity. From an alignment perspective, they are capable of representing a wider range of societal viewpoints and display improved logit calibration. Notably, Soft Preference Learning resembles, but is a Pareto improvement over, standard temperature scaling.

## Metadata
- venue: ICLR
- year: 2025
- authors: Stewart Slocum, Asher Parker-Sartori, Dylan Hadfield-Menell
- arxiv_id: 
- openreview_id: pOq9vDIYev
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2c1b1d62f868031970a42629ecefb76a107db304.pdf
- published: 2025
- keywords: alignment, diversity, natural language processing, reinforcement learning

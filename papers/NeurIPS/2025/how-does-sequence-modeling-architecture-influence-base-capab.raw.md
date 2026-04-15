---
title: "How Does Sequence Modeling Architecture Influence Base Capabilities of Pre-trained Language Models? Exploring Key Architecture Design Principles to Avoid Base Capabilities Degradation"
authors: ["Xin Lu", "Yanyan Zhao", "Si Wei", "Shijin Wang", "Bing Qin", "Ting Liu"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "vMkJWaa02n"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/7c47469b00c95e45f5fa5fe51764887757f9486f.pdf"
published: "2025"
categories: []
keywords: ["Pre-trained Language Models", "Base Capabilities", "Sequence Modeling"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:29+09:00"
---

# How Does Sequence Modeling Architecture Influence Base Capabilities of Pre-trained Language Models? Exploring Key Architecture Design Principles to Avoid Base Capabilities Degradation

## Abstract
Pre-trained language models represented by the Transformer have been proven to possess strong base capabilities, and the representative self-attention mechanism in the Transformer has become a classic in sequence modeling architectures. Different from the work of proposing sequence modeling architecture to improve the efficiency of attention mechanism, this work focuses on the impact of sequence modeling architectures on base capabilities. Specifically, our concern is: How exactly do sequence modeling architectures affect the base capabilities of pre-trained language models? In this work, we first point out that the mixed domain pre-training setting commonly adopted in existing architecture design works fails to adequately reveal the differences in base capabilities among various architectures. To address this, we propose a limited domain pre-training setting with out-of-distribution testing, which successfully uncovers significant differences in base capabilities among architectures at an early stage. Next, we analyze the base capabilities of stateful sequence modeling architectures, and find that they exhibit significant degradation in base capabilities compared to the Transformer. Then, through a series of architecture component analysis, we summarize a key architecture design principle: A sequence modeling architecture need possess full-sequence arbitrary selection capability to avoid degradation in base capabilities. Finally, we empirically validate this principle using an extremely simple Top-1 element selection architecture and further generalize it to a more practical Top-1 chunk selection architecture. Experimental results demonstrate our proposed sequence modeling architecture design principle and suggest that our work can serve as a valuable reference for future architecture improvements and novel designs.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Xin Lu, Yanyan Zhao, Si Wei, Shijin Wang, Bing Qin, Ting Liu
- arxiv_id: 
- openreview_id: vMkJWaa02n
- anthology_id: 
- pdf_url: https://openreview.net/pdf/7c47469b00c95e45f5fa5fe51764887757f9486f.pdf
- published: 2025
- keywords: Pre-trained Language Models, Base Capabilities, Sequence Modeling

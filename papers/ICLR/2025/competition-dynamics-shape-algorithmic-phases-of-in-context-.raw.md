---
title: "Competition Dynamics Shape Algorithmic Phases of In-Context Learning"
authors: ["Core Francisco Park", "Ekdeep Singh Lubana", "Hidenori Tanaka"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "XgH1wfHSX8"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/7b36616ba9974b20a298d44d2a315d9c5918e6cb.pdf"
published: "2025"
categories: []
keywords: ["In-Context Learning", "Circuit Competition", "Markov Chains", "Training Dynamics", "Generalization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:13+09:00"
---

# Competition Dynamics Shape Algorithmic Phases of In-Context Learning

## Abstract
In-Context Learning (ICL) has significantly expanded the general-purpose nature of large language models, allowing them to adapt to novel tasks using merely the inputted context. This has motivated a series of papers that analyze tractable synthetic domains and postulate precise mechanisms that may underlie ICL. However, the use of relatively distinct setups that often lack a sequence modeling nature to them makes it unclear how general the reported insights from such studies are. Motivated by this, we propose a synthetic sequence modeling task that involves learning to simulate a finite mixture of Markov chains. As we show, models trained on this task reproduce most well-known results on ICL, hence offering a unified setting for studying the concept. Building on this setup, we demonstrate we can explain a model’s behavior by decomposing it into four broad algorithms that combine a fuzzy retrieval vs. inference approach with either unigram or bigram statistics of the context. These algorithms engage in a competitive dynamics to dominate model behavior, with the precise experimental conditions dictating which algorithm ends up superseding others: e.g., we find merely varying context size or amount of training yields (at times sharp) transitions between which algorithm dictates the model behavior, revealing a mechanism that explains the transient nature of ICL. In this sense, we argue ICL is best thought of as a mixture of different algorithms, each with its own peculiarities, instead of a monolithic capability. This also implies that making general claims about ICL that hold universally across all settings may be infeasible.

## Metadata
- venue: ICLR
- year: 2025
- authors: Core Francisco Park, Ekdeep Singh Lubana, Hidenori Tanaka
- arxiv_id: 
- openreview_id: XgH1wfHSX8
- anthology_id: 
- pdf_url: https://openreview.net/pdf/7b36616ba9974b20a298d44d2a315d9c5918e6cb.pdf
- published: 2025
- keywords: In-Context Learning, Circuit Competition, Markov Chains, Training Dynamics, Generalization

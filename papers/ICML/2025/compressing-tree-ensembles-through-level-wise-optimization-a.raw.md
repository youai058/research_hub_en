---
title: "Compressing tree ensembles through Level-wise Optimization and Pruning"
authors: ["Laurens Devos", "Timo Martens", "Deniz Can Oruc", "Wannes Meert", "Hendrik Blockeel", "Jesse Davis"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "9Klg7ce8D7"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c34b1111d176eaa5d456c548e5688d2a71df111b.pdf"
published: "2025"
categories: []
keywords: ["ensembles", "decision forests", "model efficiency", "energy efficiency", "verification", "compression"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:10+09:00"
---

# Compressing tree ensembles through Level-wise Optimization and Pruning

## Abstract
Tree ensembles (e.g., gradient boosting decision trees) are often used in practice because they offer excellent predictive performance while still being easy and efficient to learn. In some contexts, it is important to additionally optimize their size: this is specifically the case when models need to have verifiable properties (verification of fairness, robustness, etc. is often exponential in the ensemble's size), or when models run on battery-powered devices (smaller ensembles consume less energy, increasing battery autonomy).  For this reason, compression of tree ensembles is worth studying.  This paper presents LOP, a method for compressing a given tree ensemble by pruning or entirely removing trees in it, while updating leaf predictions in such a  way that predictive accuracy is mostly unaffected. Empirically, LOP achieves compression factors that are often 10 to 100 times better than that of competing methods.

## Metadata
- venue: ICML
- year: 2025
- authors: Laurens Devos, Timo Martens, Deniz Can Oruc, Wannes Meert, Hendrik Blockeel, Jesse Davis
- arxiv_id: 
- openreview_id: 9Klg7ce8D7
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c34b1111d176eaa5d456c548e5688d2a71df111b.pdf
- published: 2025
- keywords: ensembles, decision forests, model efficiency, energy efficiency, verification, compression

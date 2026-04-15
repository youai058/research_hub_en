---
title: "A Dense Subset Index for Collective Query Coverage"
authors: ["Kartik Nair", "Pritish Chakraborty", "Atharva Abhijit Tambat", "Indradyumna Roy", "Soumen Chakrabarti", "Anirban Dasgupta", "Abir De"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "cUdODCFjUM"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/54f4fd7a2d7da7e462da33a369b9d1f6cdb56080.pdf"
published: "2026"
categories: []
keywords: ["collective retrieval", "subset search", "submodular functions"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:37+09:00"
---

# A Dense Subset Index for Collective Query Coverage

## Abstract
In traditional information retrieval, corpus items compete with each other to occupy top ranks in response to a query.  In contrast, in many recent retrieval scenarios associated with complex, multi-hop question answering or text-to-SQL, items are not self-complete: they must instead collaborate, i.e., information from multiple items must be combined to respond to the query. In the context of modern dense retrieval, this need translates into finding a small collection of corpus items whose contextual word vectors collectively cover the contextual word vectors of the query. The central challenge is to retrieve a near-optimal collection of covering items in time that is sublinear in corpus size. By establishing coverage as a submodular objective, we enable successive dense index probes to quickly assemble an item collection that achieves near-optimal coverage.  Successive query vectors are iteratively `edited', and the dense index is built using random projections of a novel, lifted dense vector space. Beyond rigorous theoretical guarantees, we report on a scalable implementation of this new form of vector database. Extensive experiments establish the empirical success of DISCo, in terms of the best coverage vs. query latency tradeoffs.

## Metadata
- venue: ICLR
- year: 2026
- authors: Kartik Nair, Pritish Chakraborty, Atharva Abhijit Tambat, Indradyumna Roy, Soumen Chakrabarti, Anirban Dasgupta, Abir De
- arxiv_id: 
- openreview_id: cUdODCFjUM
- anthology_id: 
- pdf_url: https://openreview.net/pdf/54f4fd7a2d7da7e462da33a369b9d1f6cdb56080.pdf
- published: 2026
- keywords: collective retrieval, subset search, submodular functions

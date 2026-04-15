---
title: "Designing Rules to Pick a Rule: Aggregation by Consistency"
authors: ["Ratip Emin Berker", "Ben Armstrong", "Vincent Conitzer", "Nihar B Shah"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "xxsacQ3tdb"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6f4ab4c3cf74069bd81a16d9b448fb72b592ed7e.pdf"
published: "2026"
categories: []
keywords: ["rank aggregation", "rule picking rules", "consistency"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:39+09:00"
---

# Designing Rules to Pick a Rule: Aggregation by Consistency

## Abstract
Rank aggregation has critical applications for developing AI agents, as well as for evaluating them. However, different methods can give rise to significantly different aggregate rankings, impacting these applications. Indeed, work in social choice and statistics has produced many rank aggregation methods, each with its desirable properties, but also with its limitations. Given this trade-off, how do we decide which aggregation rule to use, _i.e._, what is a good _rule picking rule (RPR)_? In this paper, we design a data-driven RPR that identifies the best method for each dataset without assuming a generative model. The principle behind our RPR is to maximize consistency if the data collection process was repeated. We show that our method satisfies several consistency-related axioms failed by a wide class of natural RPRs. While we prove that the computational problem of maximizing consistency is hard, we provide a sampling-based implementation that is efficient in practice. We run this implementation on known statistical models to experimentally demonstrate its desirable properties, as well as on real-world data where our method provides important insights into how to improve consistency.

## Metadata
- venue: ICLR
- year: 2026
- authors: Ratip Emin Berker, Ben Armstrong, Vincent Conitzer, Nihar B Shah
- arxiv_id: 
- openreview_id: xxsacQ3tdb
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6f4ab4c3cf74069bd81a16d9b448fb72b592ed7e.pdf
- published: 2026
- keywords: rank aggregation, rule picking rules, consistency

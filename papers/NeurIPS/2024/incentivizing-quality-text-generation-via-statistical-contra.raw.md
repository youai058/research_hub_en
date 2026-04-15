---
title: "Incentivizing Quality Text Generation via Statistical Contracts"
authors: ["Eden Saig", "Ohad Einav", "Inbal Talgam-Cohen"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "wZgw4CrxwK"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/1fdf8e5ba7d29e7866528df491d68f17a90f0e68.pdf"
published: "2024"
categories: []
keywords: ["Contract Theory", "Contract Design", "Moral Hazard", "Natural Language Generation", "LLM evaluation", "Hypothesis Testing"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:43+09:00"
---

# Incentivizing Quality Text Generation via Statistical Contracts

## Abstract
While the success of large language models (LLMs) increases demand for machine-generated text, current pay-per-token pricing schemes create a misalignment of incentives known in economics as moral hazard: Text-generating agents have strong incentive to cut costs by preferring a cheaper model over the cutting-edge one, and this can be done “behind the scenes” since the agent performs inference internally. In this work, we approach this issue from an economic perspective, by proposing a pay-for-performance, contract-based framework for incentivizing quality. We study a principal-agent game where the agent generates text using costly inference, and the contract determines the principal’s payment for the text according to an automated quality evaluation. Since standard contract theory is inapplicable when internal inference costs are unknown, we introduce cost-robust contracts. As our main theoretical contribution, we characterize optimal cost-robust contracts through a direct correspondence to optimal composite hypothesis tests from statistics, generalizing a result of Saig et al. (NeurIPS’23). We evaluate our framework empirically by deriving contracts for a range of objectives and LLM evaluation benchmarks, and find that cost-robust contracts sacrifice only a marginal increase in objective value compared to their cost-aware counterparts.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Eden Saig, Ohad Einav, Inbal Talgam-Cohen
- arxiv_id: 
- openreview_id: wZgw4CrxwK
- anthology_id: 
- pdf_url: https://openreview.net/pdf/1fdf8e5ba7d29e7866528df491d68f17a90f0e68.pdf
- published: 2024
- keywords: Contract Theory, Contract Design, Moral Hazard, Natural Language Generation, LLM evaluation, Hypothesis Testing

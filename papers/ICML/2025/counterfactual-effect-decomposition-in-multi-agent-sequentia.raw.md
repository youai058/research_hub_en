---
title: "Counterfactual Effect Decomposition in Multi-Agent Sequential Decision Making"
authors: ["Stelios Triantafyllou", "Aleksa Sukovic", "Yasaman Zolfimoselo", "Goran Radanovic"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "jHLSnYNt1m"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2f7d4d2bfa2d4174af3cfb3e5252d97c84dea050.pdf"
published: "2025"
categories: []
keywords: ["counterfactual reasoning", "causal explanation formula", "multi-agent Markov decision processes", "accountability"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:20+09:00"
---

# Counterfactual Effect Decomposition in Multi-Agent Sequential Decision Making

## Abstract
We address the challenge of explaining counterfactual outcomes in multi-agent Markov decision processes. In particular, we aim to explain the total counterfactual effect of an agent's action on the outcome of a realized scenario through its influence on the environment dynamics and the agents' behavior. To achieve this, we introduce a novel causal explanation formula that decomposes the counterfactual effect by attributing to each agent and state variable a score reflecting their respective contributions to the effect. First, we show that the total counterfactual effect of an agent's action can be decomposed into two components: one measuring the effect that propagates through all subsequent agents' actions and another related to the effect that propagates through the state transitions. Building on recent advancements in causal contribution analysis, we further decompose these two effects as follows. For the former, we consider agent-specific effects -- a causal concept that quantifies the counterfactual effect of an agent's action that propagates through a subset of agents. Based on this notion, we use Shapley value to attribute the effect to individual agents. For the latter, we consider the concept of structure-preserving interventions and attribute the effect to state variables based on their "intrinsic'' contributions. Through extensive experimentation, we demonstrate the interpretability of our approach in a Gridworld environment with LLM-assisted agents and a sepsis management simulator.

## Metadata
- venue: ICML
- year: 2025
- authors: Stelios Triantafyllou, Aleksa Sukovic, Yasaman Zolfimoselo, Goran Radanovic
- arxiv_id: 
- openreview_id: jHLSnYNt1m
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2f7d4d2bfa2d4174af3cfb3e5252d97c84dea050.pdf
- published: 2025
- keywords: counterfactual reasoning, causal explanation formula, multi-agent Markov decision processes, accountability

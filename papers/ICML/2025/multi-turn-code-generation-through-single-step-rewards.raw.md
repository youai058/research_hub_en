---
title: "Multi-Turn Code Generation Through Single-Step Rewards"
authors: ["Arnav Kumar Jain", "Gonzalo Gonzalez-Pumariega", "Wayne Chen", "Alexander M Rush", "Wenting Zhao", "Sanjiban Choudhury"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "aJeLhLcsh0"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a0694f554eebc1ceeed0763be980698c9def09fe.pdf"
published: "2025"
categories: []
keywords: ["Code Generation", "Language Models", "Reinforcement Learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:37+09:00"
---

# Multi-Turn Code Generation Through Single-Step Rewards

## Abstract
We address the problem of code generation from multi-turn execution feedback. 
Existing methods either generate code without feedback or use complex, hierarchical reinforcement learning to optimize multi-turn rewards.
We propose a simple yet scalable approach, $\mu$CODE, that solves multi-turn code generation using only single-step rewards.
Our key insight is that code generation is a one-step recoverable MDP, where the correct code can be recovered from any intermediate code state in a single turn.
$\mu$CODE iteratively trains both a generator to provide  code solutions conditioned on multi-turn execution feedback and a verifier to score the newly generated code.
Experimental evaluations show that our approach achieves significant improvements over state-of-the-art baselines. 
We provide analysis of the design choices of the reward models and policy, and show the efficacy of $\mu$CODE at utilizing the execution feedback.

## Metadata
- venue: ICML
- year: 2025
- authors: Arnav Kumar Jain, Gonzalo Gonzalez-Pumariega, Wayne Chen, Alexander M Rush, Wenting Zhao, Sanjiban Choudhury
- arxiv_id: 
- openreview_id: aJeLhLcsh0
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a0694f554eebc1ceeed0763be980698c9def09fe.pdf
- published: 2025
- keywords: Code Generation, Language Models, Reinforcement Learning

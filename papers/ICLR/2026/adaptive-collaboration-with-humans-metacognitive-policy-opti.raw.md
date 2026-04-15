---
title: "Adaptive Collaboration with Humans: Metacognitive Policy Optimization for Multi-Agent LLMs with Continual Learning"
authors: ["Wei Yang", "Defu Cao", "Jiacheng Pang", "Muyan Weng", "Yan Liu"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "IKVUB9Exuc"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/613f6a4bc4a675744c4d10bedec2c21e46b53207.pdf"
published: "2026"
categories: []
keywords: ["Multi-Agent", "Adaptive Collaboration", "Policy Optimization", "Large Language Models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:45+09:00"
---

# Adaptive Collaboration with Humans: Metacognitive Policy Optimization for Multi-Agent LLMs with Continual Learning

## Abstract
While scaling individual Large Language Models (LLMs) has delivered remarkable progress, the next frontier lies in scaling collaboration through multi-agent systems (MAS). However, purely autonomous MAS remain ``closed-world'' systems, constrained by the static knowledge horizon of pre-trained models. This limitation makes them brittle on tasks requiring knowledge beyond training data, often leading to collective failure under novel challenges. To address this, we propose the Human-In-the-Loop Multi-Agent Collaboration (HILA) framework, a principled paradigm for human--agent collaboration. HILA trains agents to learn a metacognitive policy that governs when to solve problems autonomously and when to defer to a human expert. To operationalize this policy, we introduce Dual-Loop Policy Optimization, which disentangles immediate decision-making from long-term capability growth. The inner loop applies Group Relative Policy Optimization (GRPO) with a cost-aware reward to optimize deferral decisions, while the outer loop implements continual learning, transforming expert feedback into high-quality supervised signals that strengthen the agent's reasoning ability. Experiments on challenging mathematical and problem-solving benchmarks show that HILA, equipped with Dual-Loop Policy Optimization, consistently outperforms advanced MAS, establishing a principled foundation for collaborative and continually improving agentic systems.

## Metadata
- venue: ICLR
- year: 2026
- authors: Wei Yang, Defu Cao, Jiacheng Pang, Muyan Weng, Yan Liu
- arxiv_id: 
- openreview_id: IKVUB9Exuc
- anthology_id: 
- pdf_url: https://openreview.net/pdf/613f6a4bc4a675744c4d10bedec2c21e46b53207.pdf
- published: 2026
- keywords: Multi-Agent, Adaptive Collaboration, Policy Optimization, Large Language Models

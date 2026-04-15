---
title: "Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation"
authors: ["Hyungjoo Chae", "Namyoung Kim", "Kai Tzu-iunn Ong", "Minju Gwak", "Gwanwoo Song", "Jihoon Kim", "Sunghwan Kim", "Dongha Lee", "Jinyoung Yeo"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "moWiYJuSGF"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f707cdce9564aa4399e705eb27b4f3681c601ad8.pdf"
published: "2025"
categories: []
keywords: ["Web Agent", "World Model", "Digital Agent", "Planning", "LLM"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:49+09:00"
---

# Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation

## Abstract
Large language models (LLMs) have recently gained much attention in building autonomous agents. However, performance of current LLM-based web agents in long-horizon tasks is far from optimal, often yielding errors such as repeatedly buying a non-refundable flight ticket. By contrast, humans can avoid such an irreversible mistake, as we have an awareness of the potential outcomes (e.g., losing money) of our actions, also known as the "world model". Motivated by this, our study first starts with preliminary analyses, confirming the absence of world models in current LLMs (e.g., GPT-4o, Claude-3.5-Sonnet, etc.). Then, we present a World-model-augmented (WMA) web agent, which simulates the outcomes of its actions for better decision-making. To overcome the challenges in training LLMs as world models predicting next observations, such as repeated elements across observations and long HTML inputs, we propose a transition-focused observation abstraction, where the prediction objectives are free-form natural language descriptions exclusively highlighting important state differences between time steps. Experiments on WebArena and Mind2Web show that our world models improve agents' policy selection without training and demonstrate our agents' cost- and time-efficiency compared to recent tree-search-based agents.

## Metadata
- venue: ICLR
- year: 2025
- authors: Hyungjoo Chae, Namyoung Kim, Kai Tzu-iunn Ong, Minju Gwak, Gwanwoo Song, Jihoon Kim, Sunghwan Kim, Dongha Lee, Jinyoung Yeo
- arxiv_id: 
- openreview_id: moWiYJuSGF
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f707cdce9564aa4399e705eb27b4f3681c601ad8.pdf
- published: 2025
- keywords: Web Agent, World Model, Digital Agent, Planning, LLM

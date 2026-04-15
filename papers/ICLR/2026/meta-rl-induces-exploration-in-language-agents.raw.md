---
title: "Meta-RL Induces Exploration in Language Agents"
authors: ["Yulun Jiang", "Liangze Jiang", "Damien Teney", "Michael Moor", "Maria Brbic"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "4GiBscHW1k"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d66d653b1b5a7f274d64a5533945da445bc88bdb.pdf"
published: "2026"
categories: []
keywords: ["Large Language Model", "Agent", "Reinforcement Learning", "Meta Learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:29+09:00"
---

# Meta-RL Induces Exploration in Language Agents

## Abstract
Reinforcement learning (RL) has enabled the training of Large Language Model (LLM) agents to interact with the environment and to solve multi-turn longhorizon tasks. However, the RL-trained agents often struggle in tasks that require active exploration and fail to efficiently adapt from trial-and-error experiences. In this paper, we present LaMer, a general Meta-RL framework that enables LLM agents to actively explore and learn from the environment feedback at test time. LaMer consists of two key components: (i) a cross-episode training framework to encourage exploration and long term rewards optimization; and (ii) in-context policy adaptation via reflection, allowing the agent to adapt their policy from task feedback signal without gradient update. Experiments across diverse environments show that LaMer significantly improves performance over RL baselines, with 11\%, 14\%, and 19\%  performance gains on Sokoban, MineSweeper and Webshop, respectively. Moreover, LaMer also demonstrates better generalization to more challenging or previously unseen tasks compared to the RL-trained agents. Overall, our results demonstrate that meta-reinforcement learning provides a principled approach to induce exploration in language agents, enabling more robust adaptation to novel environments through learned exploration strategies.

## Metadata
- venue: ICLR
- year: 2026
- authors: Yulun Jiang, Liangze Jiang, Damien Teney, Michael Moor, Maria Brbic
- arxiv_id: 
- openreview_id: 4GiBscHW1k
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d66d653b1b5a7f274d64a5533945da445bc88bdb.pdf
- published: 2026
- keywords: Large Language Model, Agent, Reinforcement Learning, Meta Learning

---
title: "MEM1: Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents"
authors: ["Zijian Zhou", "Ao Qu", "Zhaoxuan Wu", "Sunghwan Kim", "Alok Prakash", "Daniela Rus", "Bryan Kian Hsiang Low", "Paul Pu Liang"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "XY8AaxDSLb"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/36eac8ef9d7e5dfc6d0d147b1a124868efec9514.pdf"
published: "2026"
categories: []
keywords: ["deep research", "reasoning", "context compression"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:43+09:00"
---

# MEM1: Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents

## Abstract
Modern language agents often need to solve long-horizon tasks requiring multiple turns of interactions with the environment, where they retrieve external information, adapt to observations, and answer interdependent queries. Yet, most LLM systems rely on full-context prompting, appending all past turns regardless of their relevance. This leads to un-bounded memory growth, increased computational costs, and degraded reasoning performance on out-of-distribution input lengths due to LLM forgetting the context. We introduce MEM1, an end-to-end reinforcement learning framework that enables agents to operate with near constant context size when solving long-horizon tasks. At each turn, MEM1 updates a compact shared internal state that jointly supports memory consolidation and reasoning. Leveraging reinforcement learning (RL) and rollout trajectory truncation, we train a MEM1 agent to develop internal states that integrate prior memory with new observations from the environment while strategically discarding irrelevant or redundant information. Experiments across three domains, including internal retrieval QA, open-domain web QA, and multi-turn web shopping, show that MEM1-7B improves performance by 3.5$\times$ while reducing memory usage by 3.7$\times$ compared to Qwen2.5-14B-Instruct on an augmented multi-hop QA dataset with 16 objectives in each task, and generalizes beyond the training horizon. Our results demonstrate the promise of reasoning-driven memory consolidation as a scalable alternative to existing solutions for training long-horizon task-solving agents that involve multiple interactions, where both efficiency and performance are optimized. Code can be found at https://github.com/MIT-MI/MEM1.

## Metadata
- venue: ICLR
- year: 2026
- authors: Zijian Zhou, Ao Qu, Zhaoxuan Wu, Sunghwan Kim, Alok Prakash, Daniela Rus, Bryan Kian Hsiang Low, Paul Pu Liang
- arxiv_id: 
- openreview_id: XY8AaxDSLb
- anthology_id: 
- pdf_url: https://openreview.net/pdf/36eac8ef9d7e5dfc6d0d147b1a124868efec9514.pdf
- published: 2026
- keywords: deep research, reasoning, context compression

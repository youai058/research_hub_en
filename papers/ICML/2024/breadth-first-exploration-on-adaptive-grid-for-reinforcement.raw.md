---
title: "Breadth-First Exploration on Adaptive Grid for Reinforcement Learning"
authors: ["Youngsik Yoon", "Gangbok Lee", "Sungsoo Ahn", "Jungseul Ok"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "59MYoLghyk"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/7a7f0e108caa9962cefaa092bf13c2b6279a09e1.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:21+09:00"
---

# Breadth-First Exploration on Adaptive Grid for Reinforcement Learning

## Abstract
Graph-based planners have gained significant attention for goal-conditioned reinforcement learning (RL), where they construct a graph consisting of confident transitions between *subgoals* as edges and run shortest path algorithms to exploit the confident edges. Meanwhile, identifying and avoiding unattainable transitions are also crucial yet overlooked by the previous graph-based planners, leading to wasting an excessive number of attempts at unattainable subgoals. To address this oversight, we propose a graph construction method that efficiently manages all the achieved and unattained subgoals on a grid graph adaptively discretizing the goal space. This enables a breadth-first exploration strategy, grounded in the local adaptive grid refinement, that prioritizes broad probing of subgoals on a coarse grid over meticulous one on a dense grid. We conducted a theoretical analysis and demonstrated the effectiveness of our approach through empirical evidence, showing that only BEAG succeeds in complex environments under the proposed fixed-goal setting.

## Metadata
- venue: ICML
- year: 2024
- authors: Youngsik Yoon, Gangbok Lee, Sungsoo Ahn, Jungseul Ok
- arxiv_id: 
- openreview_id: 59MYoLghyk
- anthology_id: 
- pdf_url: https://openreview.net/pdf/7a7f0e108caa9962cefaa092bf13c2b6279a09e1.pdf
- published: 2024

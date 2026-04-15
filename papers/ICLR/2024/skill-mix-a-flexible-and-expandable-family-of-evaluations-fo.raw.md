---
title: "SKILL-MIX: a Flexible and Expandable Family of Evaluations for AI Models"
authors: ["Dingli Yu", "Simran Kaur", "Arushi Gupta", "Jonah Brown-Cohen", "Anirudh Goyal", "Sanjeev Arora"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Jf5gplvglq"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2f6d42f9e2ebcdc95ea494a075e5cd3fc7e5e119.pdf"
published: "2024"
categories: []
keywords: ["Large language model", "skill evaluation", "LLM benchmark", "emergence"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:05+09:00"
---

# SKILL-MIX: a Flexible and Expandable Family of Evaluations for AI Models

## Abstract
With LLMs shifting their role from statistical modeling of language to serving as general-purpose AI agents, how should LLM evaluations change? Arguably, a key ability of an AI agent is to flexibly combine, as needed, the basic skills it has learned. The capability to combine skills plays an important role in (human) pedagogy and also in a paper on emergence phenomena (Arora & Goyal, 2023).

This work introduces SKILL-MIX, a new evaluation to measure ability to combine skills. Using a list of $N$  skills the evaluator repeatedly picks random subsets of $k$ skills and asks the LLM to produce text combining that subset of skills. Since the number of subsets grows like $N^k$, for even modest $k$ this evaluation will, with high probability, require the LLM to produce text significantly different from any text in the training set. 
The paper develops a methodology for (a) designing and administering such an evaluation, and (b) automatic grading (plus spot-checking by humans) of the results using GPT-4 as well as the open LLaMA-2 70B model. 

Administering a version of SKILL-MIX to popular chatbots gave results that,  while generally in line with prior expectations, contained surprises. Sizeable differences exist among model capabilities that are not captured by their ranking on popular LLM leaderboards ("cramming for the leaderboard"). Furthermore, simple probability calculations indicate that GPT-4's reasonable performance on $k=5$ is suggestive of going beyond "stochastic parrot" behavior (Bender et al., 2021), i.e., it combines skills in ways that it had not seen during training.

We sketch how the methodology can lead to a SKILL-MIX based eco-system of open evaluations for AI capabilities of future models. We maintain a leaderboard of SKILL-MIX at [https://skill-mix.github.io](https://skill-mix.github.io).

## Metadata
- venue: ICLR
- year: 2024
- authors: Dingli Yu, Simran Kaur, Arushi Gupta, Jonah Brown-Cohen, Anirudh Goyal, Sanjeev Arora
- arxiv_id: 
- openreview_id: Jf5gplvglq
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2f6d42f9e2ebcdc95ea494a075e5cd3fc7e5e119.pdf
- published: 2024
- keywords: Large language model, skill evaluation, LLM benchmark, emergence

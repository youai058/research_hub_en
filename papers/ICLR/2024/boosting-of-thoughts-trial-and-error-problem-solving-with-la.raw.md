---
title: "Boosting of Thoughts: Trial-and-Error Problem Solving with Large Language Models"
authors: ["Sijia Chen", "Baochun Li", "Di Niu"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "qBL04XXex6"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a30673a601700226be14c851d887cc7181f4c78f.pdf"
published: "2024"
categories: []
keywords: ["Large Language Models; Prompt Engineering; Boosting Mechanism;"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:46+09:00"
---

# Boosting of Thoughts: Trial-and-Error Problem Solving with Large Language Models

## Abstract
The reasoning performance of Large Language Models (LLMs) on a wide range of problems critically relies on chain-of-thought prompting, which involves providing a few chain of thought demonstrations as exemplars in prompts. Recent work, e.g., Tree of Thoughts, has pointed out the importance of exploration and self-evaluation in reasoning step selection for complex problem solving. In this paper, we present Boosting of Thoughts (BoT), an automated prompting framework for problem solving with LLMs by iteratively exploring and self-evaluating many trees of thoughts in order to acquire an ensemble of trial-and-error reasoning experiences, which will serve as a new form of prompting to solve the complex problem. Starting from a simple prompt without requiring examples, BoT iteratively explores and evaluates a large collection of reasoning steps, and more importantly, uses error analysis obtained from the LLM on them to explicitly revise prompting, which in turn enhances reasoning step generation, until a final answer is attained. Our experiments with GPT-4 and Llama2 across extensive complex mathematical problems demonstrate that BoT consistently achieves higher or comparable problem-solving rates than other advanced prompting approaches.

## Metadata
- venue: ICLR
- year: 2024
- authors: Sijia Chen, Baochun Li, Di Niu
- arxiv_id: 
- openreview_id: qBL04XXex6
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a30673a601700226be14c851d887cc7181f4c78f.pdf
- published: 2024
- keywords: Large Language Models; Prompt Engineering; Boosting Mechanism;

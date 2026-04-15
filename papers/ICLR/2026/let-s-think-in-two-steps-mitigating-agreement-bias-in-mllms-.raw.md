---
title: "Let's Think in Two Steps: Mitigating Agreement Bias in MLLMs with Self-Grounded Verification"
authors: ["Moises Andrade", "Joonhyuk Cha", "Brandon Ho", "Vriksha Srihari", "Karmesh Yadav", "Zsolt Kira"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "rwo7bVlnzo"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/11f28eacfa67d124de8a3ee8cc8c6afef3c6eb64.pdf"
published: "2026"
categories: []
keywords: ["Verifiers", "Verification", "Digital Agents", "Web Agents", "GUI Agents", "Robotics", "Large Language Models", "Test Time Scaling", "WebArena", "OSWorld", "Reward Models", "open-endedness", "LLMs-as-judges", "Vision Language Models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:28+09:00"
---

# Let's Think in Two Steps: Mitigating Agreement Bias in MLLMs with Self-Grounded Verification

## Abstract
Verifiers—functions assigning rewards to agent behavior—have been key to AI progress in domains such as math, code, and games. However, extending these gains to domains without clear-cut success criteria (e.g., computer use) remains a challenge: while humans can recognize desired outcomes, translating this intuition into scalable rules is nontrivial. Multimodal LLMs (MLLMs) emerge as a promising solution, given vast world knowledge, human-preference alignment, and reasoning capabilities. We evaluate MLLMs as verifiers across web navigation, computer use, and robotics, spanning 13+ model families, 28+ evaluation templates, curated trajectories from diverse agents and of varying lengths, and distinct verifier applications. We identify a critical limitation: a strong tendency for MLLMs to over-validate agent behavior—a phenomenon we term agreement bias. This bias is pervasive across models, resilient to test-time scaling, and can harm methods relying on MLLM evaluations, such as filtered behavior cloning and self-improvement. We provide guidance on the design and evaluation of MLLM verifiers, and introduce Self-Grounded Verification (SGV), a lightweight method that harnesses MLLMs' own sampling mechanisms by modulating (un)conditional generation to better leverage their knowledge, alignment, and reasoning. SGV operates in two steps: first, the MLLM is elicited to generate broad priors about desired behavior, independent of the data under evaluation. Then, conditioned on self-generated priors, it reasons over and evaluates a candidate trajectory. Our methods yield gains across models and environments, improving failure detection by up to 25pp and accuracy by 14pp, with benefits extending to downstream applications. In self-improvement and online supervision, SGV boosts task completion of a GUI specialist in OSWorld, a diffusion policy in robomimic, and a ReAct agent in VisualWebArena—setting a new state of the art, surpassing the previous best by 20pp. Finally, we release an updated version of VisualWebArena featuring strong agent baselines, more human-aligned evaluators, high-fidelity environment parallelism, runtime speedups exceeding 10x, and VisualWebArena-Lite, a 1/3-scale subset with comparable evaluation fidelity. Our code, models, and data are publicly available at [our project page](https://mshalimay.github.io/agreement-bias-sgv/).

## Metadata
- venue: ICLR
- year: 2026
- authors: Moises Andrade, Joonhyuk Cha, Brandon Ho, Vriksha Srihari, Karmesh Yadav, Zsolt Kira
- arxiv_id: 
- openreview_id: rwo7bVlnzo
- anthology_id: 
- pdf_url: https://openreview.net/pdf/11f28eacfa67d124de8a3ee8cc8c6afef3c6eb64.pdf
- published: 2026
- keywords: Verifiers, Verification, Digital Agents, Web Agents, GUI Agents, Robotics, Large Language Models, Test Time Scaling, WebArena, OSWorld, Reward Models, open-endedness, LLMs-as-judges, Vision Language Models

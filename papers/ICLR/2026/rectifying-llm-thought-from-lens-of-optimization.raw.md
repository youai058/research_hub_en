---
title: "Rectifying LLM Thought from Lens of Optimization"
authors: ["Junnan Liu", "Hongwei Liu", "Songyang Zhang", "Kai Chen"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "bOMQmyR492"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c846607ce47e3309ce02f0289328bb9b7814b297.pdf"
published: "2026"
categories: []
keywords: ["Large Lanugae Model", "Large Lanugae Model Reasoning", "Reinforcement Learning with Verifiable Rewards"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:50+09:00"
---

# Rectifying LLM Thought from Lens of Optimization

## Abstract
Recent advancements in large language models (LLMs) have been driven by their emergent reasoning capabilities, particularly through long chain-of-thought (CoT) prompting, which enables thorough exploration and deliberation. Despite these advances, long-CoT LLMs often exhibit suboptimal reasoning behaviors, such as overthinking and excessively protracted reasoning chains, which can impair performance. In this paper, we analyze reasoning processes through an optimization lens, framing CoT as a gradient descent procedure where each reasoning step constitutes an update toward problem resolution. Building on this perspective, we introduce RePro (**Re**ctifying **Pro**cess-level Reward), a novel approach to refine LLM reasoning during post-training. RePro defines a surrogate objective function to assess the optimization process underlying CoT, utilizing a dual scoring mechanism to quantify its intensity and stability. These scores are aggregated into a composite process-level reward, seamlessly integrated into reinforcement learning with verifiable rewards (RLVR) pipelines to optimize LLMs. Extensive experiments across multiple reinforcement learning algorithms and diverse LLMs, evaluated on benchmarks spanning mathematics, science, and coding, demonstrate that RePro consistently enhances reasoning performance and mitigates suboptimal reasoning behaviors.

## Metadata
- venue: ICLR
- year: 2026
- authors: Junnan Liu, Hongwei Liu, Songyang Zhang, Kai Chen
- arxiv_id: 
- openreview_id: bOMQmyR492
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c846607ce47e3309ce02f0289328bb9b7814b297.pdf
- published: 2026
- keywords: Large Lanugae Model, Large Lanugae Model Reasoning, Reinforcement Learning with Verifiable Rewards

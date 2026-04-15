---
title: "OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models"
authors: ["Junda Wu", "Xintong Li", "Ruoyu Wang", "Yu Xia", "Yuxin Xiong", "Jianing Wang", "Tong Yu", "Xiang Chen", "Branislav Kveton", "Lina Yao", "Jingbo Shang", "Julian McAuley"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "rlgplAuN2p"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c7da56491c73e5c2aa992a5fd538e0b3d04bcaca.pdf"
published: "2025"
categories: []
keywords: ["chain-of-thought", "large language models", "offline policy evaluation", "agentic"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:51+09:00"
---

# OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models

## Abstract
Offline evaluation of LLMs is crucial in understanding their capacities, though current methods remain underexplored in existing research. In this work, we focus on the offline evaluation of the chain-of-thought capabilities and show how to optimize LLMs based on the proposed evaluation method. To enable offline feedback with rich knowledge and reasoning paths, we use knowledge graphs (KGs) (e.g., Wikidata5M) to provide feedback on the generated chain of thoughts. Due to the heterogeneity between LLM reasoning and KG structures, direct interaction and feedback from knowledge graphs on LLM behavior are challenging, as they require accurate entity linking and grounding of LLM-generated chains of thought in the KG. To address the above challenge, we propose an offline chain-of-thought evaluation framework, OCEAN, which models chain-of-thought reasoning in LLMs as a Markov Decision Process (MDP), and evaluate the policy’s alignment with KG preference modeling. To overcome the reasoning heterogeneity and grounding problems, we leverage on-policy KG exploration and reinforcement learning to model a KG policy that generates token-level likelihood distributions for LLM-generated chain-of-thought reasoning paths, simulating KG reasoning preference. Then we incorporate the knowledge-graph feedback on the validity and alignment of the generated reasoning paths into inverse propensity scores and propose KG-IPS estimator. Theoretically, we prove the unbiasedness of the proposed KG-IPS estimator and provide a lower bound on its variance. With the off-policy evaluated value function, we can directly enable off-policy optimization to further enhance chain-of-thought alignment. Our empirical study shows that OCEAN can be efficiently optimized for generating chain-of-thought reasoning paths with higher estimated values without affecting LLMs’ general abilities in downstream tasks or their internal knowledge.

## Metadata
- venue: ICLR
- year: 2025
- authors: Junda Wu, Xintong Li, Ruoyu Wang, Yu Xia, Yuxin Xiong, Jianing Wang, Tong Yu, Xiang Chen, Branislav Kveton, Lina Yao, Jingbo Shang, Julian McAuley
- arxiv_id: 
- openreview_id: rlgplAuN2p
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c7da56491c73e5c2aa992a5fd538e0b3d04bcaca.pdf
- published: 2025
- keywords: chain-of-thought, large language models, offline policy evaluation, agentic

---
title: "Selective Visual Representations Improve Convergence and Generalization for Embodied AI"
authors: ["Ainaz Eftekhar", "Kuo-Hao Zeng", "Jiafei Duan", "Ali Farhadi", "Aniruddha Kembhavi", "Ranjay Krishna"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "kC5nZDU5zf"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2fbfaec8070dacca6ff1916307768a1f7ce97be6.pdf"
published: "2024"
categories: []
keywords: ["Embodied-AI", "Task-conditioned Representations", "Visual Navigation", "Reinforcement Learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:01+09:00"
---

# Selective Visual Representations Improve Convergence and Generalization for Embodied AI

## Abstract
Embodied AI models often employ off the shelf vision backbones like CLIP to encode their visual observations. Although such general purpose representations encode rich syntactic and semantic information about the scene, much of this information is often irrelevant to the specific task at hand. This introduces noise within the learning process and distracts the agent's focus from task-relevant visual cues.
Inspired by selective attention in humans—the process through which people filter their perception based on their experiences, knowledge, and the task at hand—we introduce a parameter-efficient approach to filter visual stimuli for embodied AI.
Our approach induces a task-conditioned bottleneck using a small learnable codebook module. This codebook is trained jointly to optimize task reward and acts as a task-conditioned selective filter over the visual observation.
Our experiments showcase state-of-the-art performance for object goal navigation and object displacement across $5$ benchmarks, ProcTHOR, ArchitecTHOR, RoboTHOR, AI2-iTHOR, and ManipulaTHOR. The filtered representations produced by the codebook are also able generalize better and converge faster when adapted to other simulation environments such as Habitat. Our qualitative analyses show that agents explore their environments more effectively and their representations retain task-relevant information like target object recognition while ignoring superfluous information about other objects.

## Metadata
- venue: ICLR
- year: 2024
- authors: Ainaz Eftekhar, Kuo-Hao Zeng, Jiafei Duan, Ali Farhadi, Aniruddha Kembhavi, Ranjay Krishna
- arxiv_id: 
- openreview_id: kC5nZDU5zf
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2fbfaec8070dacca6ff1916307768a1f7ce97be6.pdf
- published: 2024
- keywords: Embodied-AI, Task-conditioned Representations, Visual Navigation, Reinforcement Learning

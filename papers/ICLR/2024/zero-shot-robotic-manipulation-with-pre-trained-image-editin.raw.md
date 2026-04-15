---
title: "Zero-Shot Robotic Manipulation with Pre-Trained Image-Editing Diffusion Models"
authors: ["Kevin Black", "Mitsuhiko Nakamoto", "Pranav Atreya", "Homer Rich Walke", "Chelsea Finn", "Aviral Kumar", "Sergey Levine"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "c0chJTSbci"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c0ae16a0a57aa4ec4f933f90e44a5e9f250f076e.pdf"
published: "2024"
categories: []
keywords: ["robot learning", "diffusion model"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:18+09:00"
---

# Zero-Shot Robotic Manipulation with Pre-Trained Image-Editing Diffusion Models

## Abstract
If generalist robots are to operate in truly unstructured environments, they need to be able to recognize and reason about novel objects and scenarios. Such objects and scenarios might not be present in the robot’s own training data. We propose SuSIE, a method that leverages an image-editing diffusion model to act as a high-level planner by proposing intermediate subgoals that a low-level controller can accomplish. Specifically, we finetune InstructPix2Pix on video data, consisting of both human videos and robot rollouts, such that it outputs hypothetical future “subgoal” observations given the robot’s current observation and a language command. We also use the robot data to train a low-level goal-conditioned policy to act as the aforementioned low-level controller. We find that the high-level subgoal predictions can utilize Internet scale pretraining and visual understanding to guide the low-level goal-conditioned policy, achieving significantly better generalization and precision than conventional language-conditioned policies. We achieve state-of-the-art results on the CALVIN benchmark, and also demonstrate robust generalization on real-world manipulation tasks, beating strong baselines that have access to privileged information or that utilize orders of magnitude more compute and training data. The project website can be found at http://rail-berkeley.github.io/susie.

## Metadata
- venue: ICLR
- year: 2024
- authors: Kevin Black, Mitsuhiko Nakamoto, Pranav Atreya, Homer Rich Walke, Chelsea Finn, Aviral Kumar, Sergey Levine
- arxiv_id: 
- openreview_id: c0chJTSbci
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c0ae16a0a57aa4ec4f933f90e44a5e9f250f076e.pdf
- published: 2024
- keywords: robot learning, diffusion model

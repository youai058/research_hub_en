---
title: "Overcoming Slow Decision Frequencies in Continuous Control: Model-Based Sequence Reinforcement Learning for Model-Free Control"
authors: ["Devdhar Patel", "Hava T Siegelmann"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "w3iM4WLuvy"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/abfe1c87402290180e7b38a8d53684d723b99fc6.pdf"
published: "2025"
categories: []
keywords: ["Decision Frequency", "Action Sequence Generation", "Model-Based Training", "Model-Free Control", "Efficient Learning", "Reinforcement Learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:16+09:00"
---

# Overcoming Slow Decision Frequencies in Continuous Control: Model-Based Sequence Reinforcement Learning for Model-Free Control

## Abstract
Reinforcement learning (RL) is rapidly reaching and surpassing human-level control capabilities. However, state-of-the-art RL algorithms often require timesteps and reaction times significantly faster than human capabilities, which is impractical in real-world settings and typically necessitates specialized hardware. We introduce Sequence Reinforcement Learning (SRL), an RL algorithm designed to produce a sequence of actions for a given input state, enabling effective control at lower decision frequencies. SRL addresses the challenges of learning action sequences by employing both a model and an actor-critic architecture operating at different temporal scales. We propose a "temporal recall" mechanism, where the critic uses the model to estimate intermediate states between primitive actions, providing a learning signal for each individual action within the sequence. Once training is complete, the actor can generate action sequences independently of the model, achieving model-free control at a slower frequency. We evaluate SRL on a suite of continuous control tasks, demonstrating that it achieves performance comparable to state-of-the-art algorithms while significantly reducing actor sample complexity. To better assess performance across varying decision frequencies, we introduce the Frequency-Averaged Score (FAS) metric. Our results show that SRL significantly outperforms traditional RL algorithms in terms of FAS, making it particularly suitable for applications requiring variable decision frequencies. Furthermore, we compare SRL with model-based online planning, showing that SRL achieves comparable FAS while leveraging the same model during training that online planners use for planning.

## Metadata
- venue: ICLR
- year: 2025
- authors: Devdhar Patel, Hava T Siegelmann
- arxiv_id: 
- openreview_id: w3iM4WLuvy
- anthology_id: 
- pdf_url: https://openreview.net/pdf/abfe1c87402290180e7b38a8d53684d723b99fc6.pdf
- published: 2025
- keywords: Decision Frequency, Action Sequence Generation, Model-Based Training, Model-Free Control, Efficient Learning, Reinforcement Learning

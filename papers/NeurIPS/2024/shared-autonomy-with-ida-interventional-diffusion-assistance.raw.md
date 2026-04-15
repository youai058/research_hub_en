---
title: "Shared Autonomy with IDA: Interventional Diffusion Assistance"
authors: ["Brandon J McMahan", "Zhenghao Peng", "Bolei Zhou", "Jonathan Kao"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "nJvkQSu9Z5"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f15789848abf5e6972bd32102c5f084f4e28b8e6.pdf"
published: "2024"
categories: []
keywords: ["Shared Autonomy", "Diffusion Models", "copilots", "intervention reinforcement learning", "reinforcement learning", "lunar lander", "Mujoco"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:48+09:00"
---

# Shared Autonomy with IDA: Interventional Diffusion Assistance

## Abstract
The rapid development of artificial intelligence (AI) has unearthed the potential to assist humans in controlling advanced technologies. Shared autonomy (SA) facilitates control by combining inputs from a human pilot and an AI copilot. In prior SA studies, the copilot is constantly active in determining the action played at each time step. This limits human autonomy that may have deleterious effects on performance. In general, the amount of helpful copilot assistance varies greatly depending on the task dynamics. We therefore hypothesized that human autonomy and SA performance improves through dynamic and selective copilot intervention. To address this, we develop a goal-agnostic intervention assistance (IA) that dynamically shares control by having the copilot intervene only when the expected value of the copilot’s action exceeds that of the human’s action. We implement IA with a diffusion copilot (termed IDA) trained on expert demonstrations with goal masking. We prove that IDA performance is lower bounded by human performance, so that IDA does not negatively impact human control. In experiments with simulated human pilots, we show that IDA achieves higher performance than both pilot-only and traditional SA control in variants of the Reacher environment and Lunar Lander. We then demonstrate with human-in the-loop experiments that IDA achieves better control in Lunar Lander and that human participants experience greater autonomy and prefer IDA over pilot-only and traditional SA control. We attribute the success of IDA to preserving human autonomy while simultaneously offering assistance to prevent the human from entering universally bad states.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Brandon J McMahan, Zhenghao Peng, Bolei Zhou, Jonathan Kao
- arxiv_id: 
- openreview_id: nJvkQSu9Z5
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f15789848abf5e6972bd32102c5f084f4e28b8e6.pdf
- published: 2024
- keywords: Shared Autonomy, Diffusion Models, copilots, intervention reinforcement learning, reinforcement learning, lunar lander, Mujoco

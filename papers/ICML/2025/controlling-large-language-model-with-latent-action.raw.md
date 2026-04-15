---
title: "Controlling Large Language Model with Latent Action"
authors: ["Chengxing Jia", "Ziniu Li", "Pengyuan Wang", "Yi-Chen Li", "Zhenyu Hou", "Yuxiao Dong", "Yang Yu"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "cEKrGCFXPA"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/052fcec9980fa1a38e34fc1728ebdc517929d547.pdf"
published: "2025"
categories: []
keywords: ["Controllable language model", "latent action model"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:09+09:00"
---

# Controlling Large Language Model with Latent Action

## Abstract
Adapting Large Language Models (LLMs) to downstream tasks using Reinforcement Learning (RL) has proven to be an effective approach. However, LLMs do not inherently define the structure of an agent for RL training, particularly in terms of specifying the action space. This paper studies learning a compact latent action space to enhance the controllability and exploration of RL for LLMs. Inspired by reinforcement learning from observations, we propose **Co**ntrolling Large Language Models with **L**atent **A**ctions **CoLA**, a framework that integrates a latent action space into pre-trained LLMs. **CoLA** employs an \emph{inverse dynamics model} to extract latent actions conditioned on future tokens, ensuring that the next token prediction is partially influenced by these actions. Simultaneously, **CoLA** fine-tunes the pre-trained LLM to function as a \emph{language world model}, capable of incorporating latent actions as inputs. Additionally, **CoLA** trains a \emph{policy model} to generate actions within this language world model. The policy model can be trained via behavior cloning to mimic a standard language model or through RL to maximize task-specific rewards. In this work, we apply **CoLA** to the Llama-3.1-8B model. Our experiments demonstrate that, compared to RL with token-level actions, **CoLA**'s latent actions enable greater semantic diversity. For enhancing downstream tasks, we show that **CoLA** with RL achieves a score of 42.4 on the \emph{math500} benchmark, surpassing the baseline score of 38.2, and reaches 68.2 when augmented with a Monte Carlo Tree Search variant. Furthermore, **CoLA** with RL consistently improves performance on agent-based tasks without degrading the pre-trained LLM's capabilities, unlike the baseline. Finally, **CoLA** reduces computation time by half in tasks involving enhanced thinking prompts for LLMs via RL. These results highlight **CoLA**'s potential to advance RL-based adaptation of LLMs for downstream applications. The CoLA model is available at  \url{https://huggingface.co/LAMDA-RL/Llama-3.1-CoLA-10B}.

## Metadata
- venue: ICML
- year: 2025
- authors: Chengxing Jia, Ziniu Li, Pengyuan Wang, Yi-Chen Li, Zhenyu Hou, Yuxiao Dong, Yang Yu
- arxiv_id: 
- openreview_id: cEKrGCFXPA
- anthology_id: 
- pdf_url: https://openreview.net/pdf/052fcec9980fa1a38e34fc1728ebdc517929d547.pdf
- published: 2025
- keywords: Controllable language model, latent action model

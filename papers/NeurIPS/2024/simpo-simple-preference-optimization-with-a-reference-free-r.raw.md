---
title: "SimPO: Simple Preference Optimization with a Reference-Free Reward"
authors: ["Yu Meng", "Mengzhou Xia", "Danqi Chen"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "3Tzcot1LKb"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/40f44a07f44c9b3d40557fba05a4b062c702b4de.pdf"
published: "2024"
categories: []
keywords: ["Language Models", "Preference Optimization", "Reinforcement Learning from Human Feedback"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:01+09:00"
---

# SimPO: Simple Preference Optimization with a Reference-Free Reward

## Abstract
Direct Preference Optimization (DPO) is a widely used offline preference optimization algorithm that reparameterizes reward functions in reinforcement learning from human feedback (RLHF) to enhance simplicity and training stability. In this work, we propose SimPO, a simpler yet more effective approach. The effectiveness of SimPO is attributed to a key design: using the _average_ log probability of a sequence as the implicit reward. This reward formulation better aligns with model generation and eliminates the need for a reference model, making it more compute and memory efficient. Additionally, we introduce a target reward margin to the Bradley-Terry objective to encourage a larger margin between the winning and losing responses, further improving the algorithm's performance. We compare SimPO to DPO and its latest variants across various state-of-the-art training setups, including both base and instruction-tuned models such as Mistral, Llama 3, and Gemma 2. We evaluate on extensive chat-based evaluation benchmarks, including AlpacaEval 2, MT-Bench, and Arena-Hard. Our results demonstrate that SimPO consistently and significantly outperforms existing approaches without substantially increasing response length. Specifically, SimPO outperforms DPO by up to 6.4 points on AlpacaEval 2 and by up to 7.5 points on Arena-Hard. Our top-performing model, built on Gemma-2-9B-it, achieves a 72.4\% length-controlled win rate on AlpacaEval 2, a 59.1\% win rate on Arena-Hard, and ranks 1st on Chatbot Arena among $<$10B models with real user votes.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Yu Meng, Mengzhou Xia, Danqi Chen
- arxiv_id: 
- openreview_id: 3Tzcot1LKb
- anthology_id: 
- pdf_url: https://openreview.net/pdf/40f44a07f44c9b3d40557fba05a4b062c702b4de.pdf
- published: 2024
- keywords: Language Models, Preference Optimization, Reinforcement Learning from Human Feedback

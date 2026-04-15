---
title: "Improving Generalization of Alignment with Human Preferences through Group Invariant Learning"
authors: ["Rui Zheng", "Wei Shen", "Yuan Hua", "Wenbin Lai", "Shihan Dou", "Yuhao Zhou", "Zhiheng Xi", "Xiao Wang", "Haoran Huang", "Tao Gui", "Qi Zhang", "Xuanjing Huang"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "fwCoLe3TAX"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/db0a7ea3470e4d33a4ea3826659ef675921bc697.pdf"
published: "2024"
categories: []
keywords: ["alignment", "language model", "invariant learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:02+09:00"
---

# Improving Generalization of Alignment with Human Preferences through Group Invariant Learning

## Abstract
The success of AI assistants based on language models (LLMs) hinges crucially on Reinforcement Learning from Human Feedback (RLHF), which enables the generation of responses more aligned with human preferences. 
As universal AI assistants, there's a growing expectation for them to perform consistently across various domains. 
However, previous work shows that Reinforcement Learning (RL) often exploits shortcuts to attain high rewards and overlooks challenging samples.
This focus on quick reward gains undermines both the stability in training and the model's ability to generalize to new, unseen data.
In this work, we propose a novel approach that can learn a consistent policy via RL across various data groups or domains. 
Given the challenges associated with acquiring group annotations, our method automatically classifies data into different groups, deliberately maximizing performance variance.
Then, we optimize the policy to perform well on challenging groups. 
Lastly, leveraging the established groups, our approach adaptively adjusts the exploration space, allocating more learning capacity to more challenging data and preventing the model from over-optimizing on simpler data. Experimental results indicate that our approach significantly enhances training stability and model generalization.

## Metadata
- venue: ICLR
- year: 2024
- authors: Rui Zheng, Wei Shen, Yuan Hua, Wenbin Lai, Shihan Dou, Yuhao Zhou, Zhiheng Xi, Xiao Wang, Haoran Huang, Tao Gui, Qi Zhang, Xuanjing Huang
- arxiv_id: 
- openreview_id: fwCoLe3TAX
- anthology_id: 
- pdf_url: https://openreview.net/pdf/db0a7ea3470e4d33a4ea3826659ef675921bc697.pdf
- published: 2024
- keywords: alignment, language model, invariant learning

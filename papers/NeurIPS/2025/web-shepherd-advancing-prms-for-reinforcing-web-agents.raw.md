---
title: "Web-Shepherd: Advancing PRMs for Reinforcing Web Agents"
authors: ["Hyungjoo Chae", "Sunghwan Kim", "Junhee Cho", "Seungone Kim", "Seungjun Moon", "Gyeom Hwangbo", "Dongha Lim", "Minjin Kim", "Yeonjun Hwang", "Minju Gwak", "Dongwook Choi", "Minseok Kang", "Gwanhoon Im", "ByeongUng Cho", "Hyojun Kim", "Jun Hee Han", "Taeyoon Kwon", "Minju Kim", "Beong-woo Kwak", "Dongjin Kang", "Jinyoung Yeo"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "G2kMroO9UV"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/db46564195dad40b9b174514d7d03b0336d2a8eb.pdf"
published: "2025"
categories: []
keywords: ["Web Agent", "Reward Model", "LLM"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:47+09:00"
---

# Web-Shepherd: Advancing PRMs for Reinforcing Web Agents

## Abstract
Web navigation is a unique domain that can automate many repetitive real-life tasks and is challenging as it requires long-horizon sequential decision making beyond typical multimodal large language model (MLLM) tasks.
Yet, specialized reward models for web navigation that can be utilized during both training and test-time have been absent until now. Despite the importance of speed and cost-effectiveness, prior works have utilized MLLMs as reward models, which poses significant constraints for real-world deployment. To address this, in this work, we propose the first process reward model (PRM) called Web-Shepherd which could assess web navigation trajectories in a step-level. To achieve this, we first construct the WebPRM Collection, a large-scale dataset with 40K step-level preference pairs and annotated checklists spanning diverse domains and difficulty levels. Next, we also introduce the WebRewardBench, the first meta-evaluation benchmark for evaluating PRMs. In our experiments, we observe that our Web-Shepherd achieves about 30 points better accuracy compared to using GPT-4o on WebRewardBench. 
Furthermore, when testing on WebArena-lite by using GPT-4o-mini as the policy and Web-Shepherd as the verifier, we achieve 10.9 points better performance, in 10x less cost compared to using GPT-4o-mini as the verifier. 
Our model, dataset, and code are publicly available at https://github.com/kyle8581/Web-Shepherd.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Hyungjoo Chae, Sunghwan Kim, Junhee Cho, Seungone Kim, Seungjun Moon, Gyeom Hwangbo, Dongha Lim, Minjin Kim, Yeonjun Hwang, Minju Gwak, Dongwook Choi, Minseok Kang, Gwanhoon Im, ByeongUng Cho, Hyojun Kim, Jun Hee Han, Taeyoon Kwon, Minju Kim, Beong-woo Kwak, Dongjin Kang, Jinyoung Yeo
- arxiv_id: 
- openreview_id: G2kMroO9UV
- anthology_id: 
- pdf_url: https://openreview.net/pdf/db46564195dad40b9b174514d7d03b0336d2a8eb.pdf
- published: 2025
- keywords: Web Agent, Reward Model, LLM

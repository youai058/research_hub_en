---
title: "AgentRefine: Enhancing Agent Generalization through Refinement Tuning"
authors: ["Dayuan Fu", "Keqing He", "Yejie Wang", "Wentao Hong", "Zhuoma GongQue", "Weihao Zeng", "Wei Wang", "Jingang Wang", "Xunliang Cai", "Weiran Xu"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "FDimWzmcWn"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ed23bb725e8e83d171ff039e600322fa09ee6de9.pdf"
published: "2025"
categories: []
keywords: ["agent", "self-refine", "diversity", "generalization", "data synthesis"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:39+09:00"
---

# AgentRefine: Enhancing Agent Generalization through Refinement Tuning

## Abstract
Large Language Model (LLM) based agents have proved their ability to perform complex tasks like humans. However, there is still a large gap between open-sourced LLMs and commercial models like the GPT series. In this paper, we focus on improving the agent generalization capabilities of LLMs via instruction tuning. We first observe that the existing agent training corpus exhibits satisfactory results on held-in evaluation sets but fails to generalize to held-out sets. These agent-tuning works face severe formatting errors and are frequently stuck in the same mistake for a long while. We analyze that the poor generalization ability comes from overfitting to several manual agent environments and a lack of adaptation to new situations. They struggle with the wrong action steps and can not learn from the experience but just memorize existing observation-action relations. Inspired by the insight, we propose a novel AgentRefine framework for agent-tuning. The core idea is to enable the model to learn to correct its mistakes via observation in the trajectory. Specifically, we propose an agent synthesis framework to encompass a diverse array of environments and tasks and prompt a strong LLM to refine its error action according to the environment feedback. AgentRefine significantly outperforms state-of-the-art agent-tuning work in terms of generalization ability on diverse agent tasks. It also has better robustness facing perturbation and can generate diversified thought in inference. Our findings establish the correlation between agent generalization and self-refinement and provide a new paradigm for future research.

## Metadata
- venue: ICLR
- year: 2025
- authors: Dayuan Fu, Keqing He, Yejie Wang, Wentao Hong, Zhuoma GongQue, Weihao Zeng, Wei Wang, Jingang Wang, Xunliang Cai, Weiran Xu
- arxiv_id: 
- openreview_id: FDimWzmcWn
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ed23bb725e8e83d171ff039e600322fa09ee6de9.pdf
- published: 2025
- keywords: agent, self-refine, diversity, generalization, data synthesis

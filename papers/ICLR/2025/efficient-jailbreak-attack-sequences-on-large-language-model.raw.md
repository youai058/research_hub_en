---
title: "EFFICIENT JAILBREAK ATTACK SEQUENCES ON LARGE LANGUAGE MODELS VIA MULTI-ARMED BANDIT-BASED CONTEXT SWITCHING"
authors: ["Aditya Ramesh", "Shivam Bhardwaj", "Aditya Saibewar", "Manohar Kaul"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "jCDF7G3LpF"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/bc16e7d0bc5f4d8c4b1a1d6e943556544f77ff36.pdf"
published: "2025"
categories: []
keywords: ["JailBreak", "AI Security", "LLM Vunlnerability"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:12+09:00"
---

# EFFICIENT JAILBREAK ATTACK SEQUENCES ON LARGE LANGUAGE MODELS VIA MULTI-ARMED BANDIT-BASED CONTEXT SWITCHING

## Abstract
Content warning: This paper contains examples of harmful language and content.
Recent advances in large language models (LLMs) have made them increasingly vulnerable to jailbreaking attempts, where malicious users manipulate models into generating harmful content. While existing approaches rely on either single-step attacks that trigger immediate safety responses or multi-step methods that inefficiently iterate prompts using other LLMs, we introduce ``Sequence of Context" (SoC) attacks that systematically alter conversational context through strategically crafted context-switching queries (CSQs). We formulate this as a multi-armed bandit (MAB) optimization problem, automatically learning optimal sequences of CSQs that gradually weaken the model's safety boundaries. Our theoretical analysis provides tight bounds on both the expected sequence length until successful jailbreak and the convergence of cumulative rewards. Empirically, our method achieves a 95\% attack success rate, surpassing PAIR by 63.15\%, AutoDAN by 60\%, and ReNeLLM by 50\%. We evaluate our attack across multiple open-source LLMs including Llama and Mistral variants. Our findings highlight critical vulnerabilities in current LLM safeguards and emphasize the need for defenses that consider sequential attack patterns rather than relying solely on static prompt filtering or iterative refinement.

## Metadata
- venue: ICLR
- year: 2025
- authors: Aditya Ramesh, Shivam Bhardwaj, Aditya Saibewar, Manohar Kaul
- arxiv_id: 
- openreview_id: jCDF7G3LpF
- anthology_id: 
- pdf_url: https://openreview.net/pdf/bc16e7d0bc5f4d8c4b1a1d6e943556544f77ff36.pdf
- published: 2025
- keywords: JailBreak, AI Security, LLM Vunlnerability

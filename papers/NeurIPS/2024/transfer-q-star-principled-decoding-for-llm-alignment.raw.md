---
title: "Transfer Q-star : Principled Decoding for LLM Alignment"
authors: ["Souradip Chakraborty", "Soumya Suvra Ghosal", "Ming Yin", "Dinesh Manocha", "Mengdi Wang", "Amrit Bedi", "Furong Huang"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "5PrShrKxoX"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0b107f4dab3fc053e007ba6aed8b411f2fcb5373.pdf"
published: "2024"
categories: []
keywords: ["RLHF", "AI Alignment", "Decoding", "LLM", "Transfer Decoding"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:03+09:00"
---

# Transfer Q-star : Principled Decoding for LLM Alignment

## Abstract
Aligning foundation models is essential for their safe and trustworthy deployment. However, traditional fine-tuning methods are computationally intensive and require updating billions of model parameters. A promising alternative, alignment via decoding, adjusts the response distribution directly without model updates to maximize a target reward $r$, thus providing a lightweight and adaptable framework for alignment. However, principled decoding methods rely on oracle access to an optimal Q-function ($Q^*$), which is often unavailable in practice. Hence, prior SoTA methods either approximate this $Q^*$ using $Q^{\pi_{\text{sft}}}$ (derived from the reference $\texttt{SFT}$ model) or rely on short-term rewards, resulting in sub-optimal decoding performance. In this work, we propose $\texttt{Transfer Q}^*$, which implicitly estimates the optimal value function for a target reward $r$ through a baseline model $\rho_{\texttt{BL}}$  aligned with a baseline reward $r_{\texttt{BL}}$ (which can be different from the target reward $r$). Theoretical analyses of $\texttt{Transfer Q}^*$ provide a rigorous characterization of its optimality, deriving an upper bound on the sub-optimality gap and identifying a hyperparameter to control the deviation from the pre-trained reference $\texttt{SFT}$ model based on user needs. Our approach significantly reduces the sub-optimality gap observed in prior SoTA methods and demonstrates superior empirical performance across key metrics such as coherence, diversity, and quality in extensive tests on several synthetic and real datasets.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Souradip Chakraborty, Soumya Suvra Ghosal, Ming Yin, Dinesh Manocha, Mengdi Wang, Amrit Bedi, Furong Huang
- arxiv_id: 
- openreview_id: 5PrShrKxoX
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0b107f4dab3fc053e007ba6aed8b411f2fcb5373.pdf
- published: 2024
- keywords: RLHF, AI Alignment, Decoding, LLM, Transfer Decoding

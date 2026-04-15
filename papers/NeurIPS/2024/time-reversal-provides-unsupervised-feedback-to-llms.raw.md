---
title: "Time-Reversal Provides Unsupervised Feedback to LLMs"
authors: ["Yerram Varun", "Rahul Madhavan", "Sravanti Addepalli", "Arun Suggala", "Karthikeyan Shanmugam", "Prateek Jain"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "nY0BrZdqLt"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/08ee7a3ea3b3fd8e7bf896a4e8fac2fc695aab87.pdf"
published: "2024"
categories: []
keywords: ["LLMs", "Reranking", "reverse LLMs", "reverse scoring", "defenses", "generative models", "sequence reversal"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:49+09:00"
---

# Time-Reversal Provides Unsupervised Feedback to LLMs

## Abstract
Large Language Models (LLMs) are typically trained to predict in the forward direction of time. However, recent works have shown that prompting these models to look back and critique their own generations can produce useful feedback. Motivated by this, we explore the question of whether LLMs can be empowered to think (predict and score) backwards to provide unsupervised feedback that complements forward LLMs. Towards this, we introduce Time Reversed Language Models (TRLMs), which can score and generate queries when conditioned on responses, effectively functioning in the reverse direction of time. Further, to effectively infer in the response to query direction, we pre-train and fine-tune a language model (TRLM-Ba) in the reverse token order from scratch. We show empirically (and theoretically in a stylized setting) that time-reversed models can indeed complement forward model predictions when used to score the query given response for re-ranking multiple forward generations. We obtain up to 5\% improvement on the widely used AlpacaEval Leaderboard over the competent baseline of best-of-N re-ranking using self log-perplexity scores. We further show that TRLM scoring outperforms conventional forward scoring of response given query, resulting in significant gains in applications such as citation generation and passage retrieval. We next leverage the generative ability of TRLM to augment or provide unsupervised feedback to input safety filters of LLMs, demonstrating a drastic reduction in false negative rate with negligible impact on false positive rates against several attacks published on the popular JailbreakBench leaderboard.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Yerram Varun, Rahul Madhavan, Sravanti Addepalli, Arun Suggala, Karthikeyan Shanmugam, Prateek Jain
- arxiv_id: 
- openreview_id: nY0BrZdqLt
- anthology_id: 
- pdf_url: https://openreview.net/pdf/08ee7a3ea3b3fd8e7bf896a4e8fac2fc695aab87.pdf
- published: 2024
- keywords: LLMs, Reranking, reverse LLMs, reverse scoring, defenses, generative models, sequence reversal

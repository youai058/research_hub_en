---
title: "Model Editing as a Robust and Denoised variant of DPO: A Case Study on Toxicity"
authors: ["Rheeya Uppaal", "Apratim Dey", "Yiting He", "Yiqiao Zhong", "Junjie Hu"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "lOi6FtIwR8"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/028aaa9270c6160e41479d39a2d6a02eaf95964d.pdf"
published: "2025"
categories: []
keywords: ["model editing", "mechanistic interpretability", "ai safety", "alignment", "toxicity", "llms"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:11+09:00"
---

# Model Editing as a Robust and Denoised variant of DPO: A Case Study on Toxicity

## Abstract
Recent alignment algorithms such as direct preference optimization (DPO) have been developed to improve the safety of large language models (LLMs) by training these models to match human behaviors exemplified by preference data. However, these methods are 
both computationally intensive and lacking in controllability and transparency, inhibiting their widespread use. Furthermore, these tuning-based methods require large-scale preference data for training and are susceptible to noisy preference data. In this paper, we introduce a tuning-free alignment alternative, ProFS (Projection Filter for Subspaces), and demonstrate its effectiveness under the use case of toxicity reduction. Grounded on theory from factor analysis, ProFS is a sample-efficient model editing approach that identifies a toxic subspace in the model parameter space and reduces model toxicity by projecting away the detected subspace. The toxic subspace is identified by extracting preference data embeddings from the language model, and removing non-toxic information from these embeddings. We show that ProFS is more sample-efficient than DPO, further showcasing greater robustness to noisy data. Finally, we attempt to connect tuning based alignment with editing, by establishing both theoretical and empirical connections between ProFS and DPO, showing that ProFS can be interpreted as a denoised version of a single DPO step.

## Metadata
- venue: ICLR
- year: 2025
- authors: Rheeya Uppaal, Apratim Dey, Yiting He, Yiqiao Zhong, Junjie Hu
- arxiv_id: 
- openreview_id: lOi6FtIwR8
- anthology_id: 
- pdf_url: https://openreview.net/pdf/028aaa9270c6160e41479d39a2d6a02eaf95964d.pdf
- published: 2025
- keywords: model editing, mechanistic interpretability, ai safety, alignment, toxicity, llms

---
title: "RAEE: A Robust Retrieval-Augmented Early Exit Framework for Efficient Inference"
authors: ["LIANMING HUANG", "Shangyu Wu", "Yufei Cui", "Ying Xiong", "Haibo Hu", "Xue Liu", "Tei-Wei Kuo", "Nan Guan", "Chun Jason Xue"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "GPGwKpRMRA"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ad9f4b7b84432dbad032b85615d14f25a6992a34.pdf"
published: "2026"
categories: []
keywords: ["Early Exit; Retrieval Augmentation; Large Language Model"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:33+09:00"
---

# RAEE: A Robust Retrieval-Augmented Early Exit Framework for Efficient Inference

## Abstract
Deploying large language model inference remains challenging due to their high computational overhead.
Early exit optimizes model inference by adaptively reducing the number of inference layers.
Current methods typically train internal classifiers or use heuristic methods to determine the exit layer.
However, those methods either introduce significant training overheads or lead to performance degradation.
To address these limitations, this paper proposes RAEE, a robust Retrieval-Augmented Early Exit framework that not only enables early exit but also enhances model performance through corrective exit information at intermediate layers.
This paper first demonstrates that the early exit problem can be effectively modeled as a distribution prediction problem, in which the distribution can be further approximated through the exit information of similar data. 
Subsequently, this paper introduces the process of collecting exit information of correct predictions and the steps to construct the retrieval database.
Finally, leveraging the pre-constructed retrieval database, RAEE utilizes the exit information from retrieved similar data to guide the backbone model's exit.
Experimental results demonstrate that RAEE can not only accelerate inference while achieving robust zero-shot performance across eight downstream tasks.

## Metadata
- venue: ICLR
- year: 2026
- authors: LIANMING HUANG, Shangyu Wu, Yufei Cui, Ying Xiong, Haibo Hu, Xue Liu, Tei-Wei Kuo, Nan Guan, Chun Jason Xue
- arxiv_id: 
- openreview_id: GPGwKpRMRA
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ad9f4b7b84432dbad032b85615d14f25a6992a34.pdf
- published: 2026
- keywords: Early Exit; Retrieval Augmentation; Large Language Model

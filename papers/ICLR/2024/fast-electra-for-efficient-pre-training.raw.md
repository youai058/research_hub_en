---
title: "Fast-ELECTRA for Efficient Pre-training"
authors: ["Chengyu Dong", "Liyuan Liu", "Hao Cheng", "Jingbo Shang", "Jianfeng Gao", "Xiaodong Liu"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "8OBuqbLb8h"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/1d4b13edd818d04501c0e1edf4751b54a5858f09.pdf"
published: "2024"
categories: []
keywords: ["Language model Pre-training", "ELECTRA", "Efficiency"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:17+09:00"
---

# Fast-ELECTRA for Efficient Pre-training

## Abstract
ELECTRA pre-trains language models by detecting tokens in a sequence that have been replaced by an auxiliary model. Although ELECTRA offers a significant boost in efficiency, its potential is constrained by the training cost brought by the auxiliary model. Notably, this model, which is jointly trained with the main model, only serves to assist the training of the main model and is discarded post-training. This results in a substantial amount of training cost being expended in vain. To mitigate this issue, we propose Fast-ELECTRA, which leverages an existing language model as the auxiliary model. To construct a learning curriculum for the main model, we smooth its output distribution via temperature scaling following a descending schedule. Our approach rivals the performance of state-of-the-art ELECTRA-style pre-training methods, while significantly eliminating the computation and memory cost brought by the joint training of the auxiliary model. Our method also reduces the sensitivity to hyper-parameters and enhances the pre-training stability.

## Metadata
- venue: ICLR
- year: 2024
- authors: Chengyu Dong, Liyuan Liu, Hao Cheng, Jingbo Shang, Jianfeng Gao, Xiaodong Liu
- arxiv_id: 
- openreview_id: 8OBuqbLb8h
- anthology_id: 
- pdf_url: https://openreview.net/pdf/1d4b13edd818d04501c0e1edf4751b54a5858f09.pdf
- published: 2024
- keywords: Language model Pre-training, ELECTRA, Efficiency

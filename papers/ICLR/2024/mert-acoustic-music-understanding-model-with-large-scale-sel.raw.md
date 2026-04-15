---
title: "MERT: Acoustic Music Understanding Model with Large-Scale Self-supervised Training"
authors: ["Yizhi LI", "Ruibin Yuan", "Ge Zhang", "Yinghao Ma", "Xingran Chen", "Hanzhi Yin", "Chenghao Xiao", "Chenghua Lin", "Anton Ragni", "Emmanouil Benetos", "Norbert Gyenge", "Roger Dannenberg", "Ruibo Liu", "Wenhu Chen", "Gus Xia", "Yemin Shi", "Wenhao Huang", "Zili Wang", "Yike Guo", "Jie Fu"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "w3YZ9MSlBu"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b0691ff4b8bef0f41861ce3bd2ea50491707b93c.pdf"
published: "2024"
categories: []
keywords: ["self-supervised learning", "music", "audio", "language model"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:25+09:00"
---

# MERT: Acoustic Music Understanding Model with Large-Scale Self-supervised Training

## Abstract
Self-supervised learning (SSL) has recently emerged as a promising paradigm for training generalisable models on large-scale data in the fields of vision, text, and speech. 
Although SSL has been proven effective in speech and audio, its application to music audio has yet to be thoroughly explored. This is partially due to the distinctive challenges associated with modelling musical knowledge, particularly tonal and pitched characteristics of music.
To address this research gap, we propose an acoustic **M**usic und**ER**standing model with large-scale self-supervised **T**raining (**MERT**), which incorporates teacher models to provide pseudo labels in the masked language modelling (MLM) style acoustic pre-training.
In our exploration, we identified an effective combination of teacher models, which outperforms conventional speech and audio approaches in terms of performance. 
This combination includes an acoustic teacher based on Residual Vector Quantization - Variational AutoEncoder (RVQ-VAE) and a musical teacher based on the Constant-Q Transform (CQT). 
Furthermore, we explore a wide range of settings to overcome the instability in acoustic language model pre-training, which allows our designed paradigm to scale from 95M to 330M parameters.
Experimental results indicate that our model can generalise and perform well on 14 music understanding tasks and attain state-of-the-art (SOTA) overall scores.

## Metadata
- venue: ICLR
- year: 2024
- authors: Yizhi LI, Ruibin Yuan, Ge Zhang, Yinghao Ma, Xingran Chen, Hanzhi Yin, Chenghao Xiao, Chenghua Lin, Anton Ragni, Emmanouil Benetos, Norbert Gyenge, Roger Dannenberg, Ruibo Liu, Wenhu Chen, Gus Xia, Yemin Shi, Wenhao Huang, Zili Wang, Yike Guo, Jie Fu
- arxiv_id: 
- openreview_id: w3YZ9MSlBu
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b0691ff4b8bef0f41861ce3bd2ea50491707b93c.pdf
- published: 2024
- keywords: self-supervised learning, music, audio, language model

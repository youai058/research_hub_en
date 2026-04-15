---
title: "Any-step Generation via N-th Order Recursive Consistent Velocity Field Estimation"
authors: ["Peng Sun", "Tao Lin"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "GnawtLKGkP"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/494c5aac1137087d98223cbca5e7250db9410478.pdf"
published: "2026"
categories: []
keywords: ["Generative Models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:17+09:00"
---

# Any-step Generation via N-th Order Recursive Consistent Velocity Field Estimation

## Abstract
Recent advances in few-step generative models (typically $1$-$8$ steps), such as consistency models, have yielded impressive performance. However, their broader adoption is hindered by significant challenges, including substantial computational overhead, the reliance on complex multi-component loss functions, and intricate multi-stage training strategies that lack end-to-end simplicity. These limitations impede their scalability and stability, especially when applied to large-scale models.

To address these issues, we introduce **$N$-th order Recursive Consistent velocity field estimation for Generative Modeling (RCGM)**, a novel framework that unifies many existing approaches. Within this framework, we reveal that conventional one-step methods, such as consistency and MeanFlow models, are special cases of 1st-order RCGM. This insight enables a natural extension to higher-order scenarios ($N \geq 2$), which exhibit markedly improved training stability and achieve state-of-the-art (SOTA) performance.

For instance, on ImageNet $256\times256$, RCGM enables a $675\text{M}$ parameter diffusion transformer to achieve a $1.48$ FID score in just $2$ sampling steps. Crucially, RCGM facilitates the stable full-parameter training of a large-scale ($20\textrm{B}$) unified multi-modal model, attaining a $0.86$ GenEval score in $2$ steps. In contrast, conventional 1st-order approaches, such as consistency and MeanFlow models, typically suffer from training instability, model collapse, or memory constraints under comparable settings.

Code is available at: https://github.com/LINs-lab/RCGM.

## Metadata
- venue: ICLR
- year: 2026
- authors: Peng Sun, Tao Lin
- arxiv_id: 
- openreview_id: GnawtLKGkP
- anthology_id: 
- pdf_url: https://openreview.net/pdf/494c5aac1137087d98223cbca5e7250db9410478.pdf
- published: 2026
- keywords: Generative Models

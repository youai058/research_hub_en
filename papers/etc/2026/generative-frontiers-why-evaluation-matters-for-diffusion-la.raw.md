---
title: "Generative Frontiers: Why Evaluation Matters for Diffusion Language Models"
authors: ["Patrick Pynadath", "Jiaxin Shi", "Ruqi Zhang"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2604.02718"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2604.02718v1"
published: "2026-04-03"
categories: ["cs.LG", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:13:54+09:00"
---

# Generative Frontiers: Why Evaluation Matters for Diffusion Language Models

## Abstract
Diffusion language models have seen exciting recent progress, offering far more flexibility in generative trajectories than autoregressive models. This flexibility has motivated a growing body of research into new approaches to diffusion language modeling, which typically begins at the scale of GPT-2 small (150 million parameters). However, these advances introduce new issues with evaluation methodology. In this technical note, we discuss the limitations of current methodology and propose principled augmentations to ensure reliable comparisons. We first discuss why OpenWebText has become the standard benchmark, and why alternatives such as LM1B are inherently less meaningful. We then discuss the limitations of likelihood evaluations for diffusion models, and explain why relying on generative perplexity alone as a metric can lead to uninformative results. To address this, we show that generative perplexity and entropy are two components of the KL divergence to a reference distribution. This decomposition explains generative perplexity's sensitivity to entropy, and naturally suggests generative frontiers as a principled method for evaluating model generative quality. We conclude with empirical observations on model quality at this scale. We include a blog post with interactive content to illustrate the argument at https://patrickpynadath1.github.io/blog/eval_methodology/.

## Metadata
- venue: arXiv
- year: 2026
- authors: Patrick Pynadath, Jiaxin Shi, Ruqi Zhang
- arxiv_id: 2604.02718
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2604.02718v1
- published: 2026-04-03

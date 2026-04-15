---
title: "$ρ$-$\\texttt{EOS}$: Training-free Bidirectional Variable-Length Control for Masked Diffusion LLMs"
authors: ["Jingyi Yang", "Yuxian Jiang", "Jing Shao"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2601.22527"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2601.22527v2"
published: "2026-01-30"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:21+09:00"
---

# $ρ$-$\texttt{EOS}$: Training-free Bidirectional Variable-Length Control for Masked Diffusion LLMs

## Abstract
Beyond parallel generation and global context modeling, current masked diffusion large language models (masked dLLMs, i.e., LLaDA) suffer from a fundamental limitation: they require a predefined, fixed generation length, which lacks flexibility and forces an inevitable trade-off between output quality and computational efficiency. To address this, we study the denoising dynamics and find that the implicit density ($ρ$) of end-of-sequence ($\texttt{EOS}$) tokens serves as a reliable signal of generation sufficiency. In particular, the evolving implicit $\texttt{EOS}$ density during denoising reveals whether the current masked space is excessive or insufficient, thereby guiding the adjustment direction for generation length. Building on this insight, we propose $\textbf{$ρ$-$\texttt{EOS}$}$, a training-free, single-stage strategy that enables bidirectional variable-length generation for masked dLLMs. Unlike prior two-stage approaches--which require separate length adjustment and iterative mask insertion phases while supporting only unidirectional expansion--$\textbf{$ρ$-$\texttt{EOS}$}$ achieves bidirectional length adjustment within a unified denoising process by continuously estimating the implicit $\texttt{EOS}$ density: excessively high density triggers $\texttt{MASK}$ token contraction, while insufficient density induces expansion. Extensive experiments on mathematics and code benchmarks demonstrate that $\textbf{$ρ$-$\texttt{EOS}$}$ achieves comparable performance while substantially improving inference efficiency and token utilization. Code is available at https://github.com/yjyddq/rho-EOS.

## Metadata
- venue: arXiv
- year: 2026
- authors: Jingyi Yang, Yuxian Jiang, Jing Shao
- arxiv_id: 2601.22527
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2601.22527v2
- published: 2026-01-30

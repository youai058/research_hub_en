---
title: "ASDSV: Multimodal Generation Made Efficient with Approximate Speculative Diffusion and Speculative Verification"
authors: ["Kaijun Zhou", "Xingyu Yan", "Xingda Wei", "Xijun Li", "Jinyu Gu"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "IIGiVRKJYa"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/7f77d98874d16e33aff891767f68baa13602adb0.pdf"
published: "2025"
categories: []
keywords: ["Speculative Diffusion", "Diffusion model", "Multimodel Generation", "Inference acceleration"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:36+09:00"
---

# ASDSV: Multimodal Generation Made Efficient with Approximate Speculative Diffusion and Speculative Verification

## Abstract
Diffusion in transformer is central to advances in high-quality multimodal generation 
but suffer from high inference latency due to their iterative nature. 
Inspired by speculative decoding's success in accelerating large language models, 
we propose Approximate Speculative Diffusion with Speculative Verification (ASDSV), 
a novel method to enhance the efficiency of diffusion models. 
Adapting speculative execution to diffusion processes presents unique challenges. 

First, the substantial computational cost of verifying numerous speculative steps 
for continuous, high-dimensional outputs makes traditional full verification prohibitively expensive. 
Second, determining the optimal number of speculative steps $K$ 
involves a trade-off between potential acceleration and verification success rates. 

To address these, ASDSV introduces two key innovations: 
1) A speculative verification technique, which leverages the observed temporal correlation between draft and target model outputs, 
efficiently validates $K$ speculative steps by only checking the alignment of the initial and final states, significantly reducing verification overhead. 
2) A multi-stage speculative strategy that adjusts $K$ according to the denoising phase—employing smaller $K$ during volatile early stages 
and larger $K$ during more stable later stages to optimize the balance between speed and quality. 

We apply ASDSV to state-of-the-art diffusion transformers, 
including Flux.1-dev for image generation and Wan2.1 for video generation. 
Extensive experiments demonstrate that ASDSV achieves up to 1.77$\times$-3.01$\times$ speedup 
in model inference with a minimal 0.3\%-0.4\% drop in VBench score, 
showcasing its effectiveness in accelerating multimodal diffusion models without significant quality degradation. 
The code will be publicly available once the acceptance of the paper.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Kaijun Zhou, Xingyu Yan, Xingda Wei, Xijun Li, Jinyu Gu
- arxiv_id: 
- openreview_id: IIGiVRKJYa
- anthology_id: 
- pdf_url: https://openreview.net/pdf/7f77d98874d16e33aff891767f68baa13602adb0.pdf
- published: 2025
- keywords: Speculative Diffusion, Diffusion model, Multimodel Generation, Inference acceleration

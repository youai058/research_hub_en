---
title: "Flow2GAN: Hybrid Flow Matching and GAN with Multi-Resolution Network for Few-step High-Fidelity Audio Generation"
authors: ["Zengwei Yao", "Wei Kang", "Han Zhu", "Liyong Guo", "Lingxuan Ye", "Fangjun Kuang", "Weiji Zhuang", "Zhaoqing Li", "Zhifeng Han", "Long Lin", "Daniel Povey"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "5eTpRIULtb"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/88ad8ab4c077125ab8e8212c31b6c9e347a6fbc9.pdf"
published: "2026"
categories: []
keywords: ["Flow2GAN", "audio generation", "Flow Matching", "GAN", "multi-resolution"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:30+09:00"
---

# Flow2GAN: Hybrid Flow Matching and GAN with Multi-Resolution Network for Few-step High-Fidelity Audio Generation

## Abstract
Existing dominant methods for audio generation include Generative Adversarial Networks (GANs) and diffusion-based methods like Flow Matching. GANs suffer from slow convergence during training, while diffusion methods require multi-step inference that introduces considerable computational overhead. In this work, we introduce Flow2GAN, a two-stage framework that combines Flow Matching training for learning generative capabilities with GAN fine-tuning for efficient few-step inference. Specifically, given audio's unique properties, we first improve Flow Matching for audio modeling through: 1) reformulating the objective as endpoint estimation, avoiding velocity estimation difficulties when involving empty regions; 2) applying spectral energy-based loss scaling to emphasize perceptually salient quieter regions. Building on these Flow Matching adaptations, we demonstrate that a further stage of lightweight GAN fine-tuning enables us to obtain few-step (e.g., 1/2/4 steps) generators that produce high-quality audio. In addition, we develop a multi-branch network architecture that processes Fourier coefficients at different time-frequency resolutions, which improves the modeling capabilities compared to prior single-resolution designs. Experimental results indicate that our Flow2GAN delivers high-fidelity audio generation from Mel-spectrograms or discrete audio tokens, achieving highly favorable quality-efficiency trade-offs compared to existing state-of-the-art GAN-based and Flow Matching-based methods. Online demo samples are available at \url{https://flow2gan.github.io}, and the source code is released at \url{https://github.com/k2-fsa/Flow2GAN}.

## Metadata
- venue: ICLR
- year: 2026
- authors: Zengwei Yao, Wei Kang, Han Zhu, Liyong Guo, Lingxuan Ye, Fangjun Kuang, Weiji Zhuang, Zhaoqing Li, Zhifeng Han, Long Lin, Daniel Povey
- arxiv_id: 
- openreview_id: 5eTpRIULtb
- anthology_id: 
- pdf_url: https://openreview.net/pdf/88ad8ab4c077125ab8e8212c31b6c9e347a6fbc9.pdf
- published: 2026
- keywords: Flow2GAN, audio generation, Flow Matching, GAN, multi-resolution

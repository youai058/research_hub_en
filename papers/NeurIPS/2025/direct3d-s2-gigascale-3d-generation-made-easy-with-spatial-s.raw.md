---
title: "Direct3D-S2: Gigascale 3D Generation Made Easy with Spatial Sparse Attention"
authors: ["Shuang Wu", "Youtian Lin", "Feihu Zhang", "Yifei Zeng", "Yikang Yang", "yajie bao", "Jiachen Qian", "Siyu Zhu", "Xun Cao", "Philip Torr", "Yao Yao"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ZYHzcZFEGD"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a6dd5ab1b1cbfa98bf4822e57d833199fe9cdcc3.pdf"
published: "2025"
categories: []
keywords: ["AIGC", "3D Generation", "Diffusion"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:52+09:00"
---

# Direct3D-S2: Gigascale 3D Generation Made Easy with Spatial Sparse Attention

## Abstract
Generating high-resolution 3D shapes using volumetric representations such as Signed Distance Functions (SDFs) presents substantial computational and memory challenges. We introduce Direct3D-S2, a scalable 3D generation framework based on sparse volumes that achieves superior output quality with dramatically reduced training costs.
Our key innovation is the Spatial Sparse Attention (SSA) mechanism, which greatly enhances the efficiency of Diffusion Transformer (DiT) computations on sparse volumetric data. SSA allows the model to effectively process large token sets within sparse volumes, significantly reducing computational overhead and achieving a 3.9$\times$ speedup in the forward pass and a 9.6$\times$ speedup in the backward pass.
Our framework also includes a variational autoencoder (VAE) that maintains a consistent sparse volumetric format across input, latent, and output stages. Compared to previous methods with heterogeneous representations in 3D VAE, this unified design significantly improves training efficiency and stability.
Our model is trained on public datasets, and experiments demonstrate that Direct3D-S2 not only surpasses state-of-the-art methods in generation quality and efficiency, but also enables training at 1024³ resolution using only 8 GPUs—a task typically requiring at least 32 GPUs for volumetric representations at $256^3$ resolution, thus making gigascale 3D generation both practical and accessible. Project page: https://www.neural4d.com/research-page/direct3d-s2.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Shuang Wu, Youtian Lin, Feihu Zhang, Yifei Zeng, Yikang Yang, yajie bao, Jiachen Qian, Siyu Zhu, Xun Cao, Philip Torr, Yao Yao
- arxiv_id: 
- openreview_id: ZYHzcZFEGD
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a6dd5ab1b1cbfa98bf4822e57d833199fe9cdcc3.pdf
- published: 2025
- keywords: AIGC, 3D Generation, Diffusion

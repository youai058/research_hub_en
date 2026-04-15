---
title: "Implicit 4D Gaussian Splatting for Fast Motion with Large Inter-Frame Displacements"
authors: ["Seung-gyeom Kim", "Areum Kim", "Yongjae Yoo", "Sukmin Yun"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "MWtXs60n38"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ac377cc6073c1c40cf6a0c207ce069d3cc23f196.pdf"
published: "2026"
categories: []
keywords: ["4D Gaussian splatting", "4D reconstruction", "Dynamic rendering"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:19+09:00"
---

# Implicit 4D Gaussian Splatting for Fast Motion with Large Inter-Frame Displacements

## Abstract
Recent 4D Gaussian Splatting (4DGS) methods often fail under fast motion with large inter-frame displacements, where Gaussian attributes are poorly learned during training, and fast-moving objects are often lost from the reconstruction. In this work, we introduce Spatiotemporal Position Implicit Network for 4DGS, coined SPIN-4DGS, which learns Gaussian attributes from explicitly collected spatiotemporal positions rather than modeling temporal displacements, thereby enabling more faithful splatting under fast motions with large inter-frame displacements. To avoid the heavy memory overhead of explicitly optimizing attributes across all spatiotemporal positions, we instead predict them with a lightweight feed-forward network trained under a rasterization-based reconstruction loss. Consequently, SPIN-4DGS learns shared representations across Gaussians, effectively capturing spatiotemporal consistency and enabling stable high-quality Gaussian splatting even under challenging motions. Across extensive experiments, SPIN-4DGS consistently achieves higher fidelity under large displacements, with clear improvements in PSNR and SSIM on challenging sports scenes from the CMU Panoptic dataset. For example, SPIN-4DGS notably outperforms the strongest baseline, D3DGS, by achieving +1.83 higher PSNR on the Basketball scene.

## Metadata
- venue: ICLR
- year: 2026
- authors: Seung-gyeom Kim, Areum Kim, Yongjae Yoo, Sukmin Yun
- arxiv_id: 
- openreview_id: MWtXs60n38
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ac377cc6073c1c40cf6a0c207ce069d3cc23f196.pdf
- published: 2026
- keywords: 4D Gaussian splatting, 4D reconstruction, Dynamic rendering

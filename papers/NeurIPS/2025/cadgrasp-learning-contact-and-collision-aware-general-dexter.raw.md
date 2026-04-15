---
title: "CADGrasp: Learning Contact and Collision Aware General Dexterous Grasping in Cluttered Scenes"
authors: ["Jiyao Zhang", "Zhiyuan Ma", "Tianhao Wu", "Zeyuan Chen", "Hao Dong"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "CB8jwNE2vV"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/adac0cb755f3a9f9086a4a62c38b5f41cc58206b.pdf"
published: "2025"
categories: []
keywords: ["Dexterous Hand", "General Grasping"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:22+09:00"
---

# CADGrasp: Learning Contact and Collision Aware General Dexterous Grasping in Cluttered Scenes

## Abstract
Dexterous grasping in cluttered environments presents substantial challenges due to the high degrees of freedom of dexterous hands, occlusion, and potential collisions arising from diverse object geometries and complex layouts. To address these challenges, we propose CADGrasp, a two-stage algorithm for general dexterous grasping using single-view point cloud inputs. In the first stage, we predict a scene-decoupled, contact- and collision-aware representation—sparse IBS—as the optimization target. Sparse IBS compactly encodes the geometric and contact relationships between the dexterous hand and the scene, enabling stable and collision-free dexterous grasp pose optimization. To enhance the prediction of this high-dimensional representation, we introduce an occupancy-diffusion model with voxel-level conditional guidance and force closure score filtering. In the second stage, we develop several energy functions and ranking strategies for optimization based on sparse IBS to generate high-quality dexterous grasp poses. Extensive experiments in both simulated and real-world settings validate the effectiveness of our approach, demonstrating its capability to mitigate collisions while maintaining a high grasp success rate across diverse objects and complex scenes.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Jiyao Zhang, Zhiyuan Ma, Tianhao Wu, Zeyuan Chen, Hao Dong
- arxiv_id: 
- openreview_id: CB8jwNE2vV
- anthology_id: 
- pdf_url: https://openreview.net/pdf/adac0cb755f3a9f9086a4a62c38b5f41cc58206b.pdf
- published: 2025
- keywords: Dexterous Hand, General Grasping

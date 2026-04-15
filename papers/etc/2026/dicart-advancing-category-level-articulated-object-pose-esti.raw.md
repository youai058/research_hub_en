---
title: "DICArt: Advancing Category-level Articulated Object Pose Estimation in Discrete State-Spaces"
authors: ["Li Zhang", "Mingyu Mei", "Ailing Wang", "Xianhui Meng", "Yan Zhong", "Xinyuan Song", "Liu Liu", "Rujing Wang", "Zaixing He", "Cewu Lu"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.19565"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.19565v2"
published: "2026-02-23"
categories: ["cs.CV", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:32+09:00"
---

# DICArt: Advancing Category-level Articulated Object Pose Estimation in Discrete State-Spaces

## Abstract
Articulated object pose estimation is a core task in embodied AI. Existing methods typically regress poses in a continuous space, but often struggle with 1) navigating a large, complex search space and 2) failing to incorporate intrinsic kinematic constraints. In this work, we introduce DICArt (DIsCrete Diffusion for Articulation Pose Estimation), a novel framework that formulates pose estimation as a conditional discrete diffusion process. Instead of operating in a continuous domain, DICArt progressively denoises a noisy pose representation through a learned reverse diffusion procedure to recover the GT pose. To improve modeling fidelity, we propose a flexible flow decider that dynamically determines whether each token should be denoised or reset, effectively balancing the real and noise distributions during diffusion. Additionally, we incorporate a hierarchical kinematic coupling strategy, estimating the pose of each rigid part hierarchically to respect the object's kinematic structure. We validate DICArt on both synthetic and real-world datasets. Experimental results demonstrate its superior performance and robustness. By integrating discrete generative modeling with structural priors, DICArt offers a new paradigm for reliable category-level 6D pose estimation in complex environments.

## Metadata
- venue: arXiv
- year: 2026
- authors: Li Zhang, Mingyu Mei, Ailing Wang, Xianhui Meng, Yan Zhong, Xinyuan Song, Liu Liu, Rujing Wang, Zaixing He, Cewu Lu
- arxiv_id: 2602.19565
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.19565v2
- published: 2026-02-23

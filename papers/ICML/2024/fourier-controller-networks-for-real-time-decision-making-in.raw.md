---
title: "Fourier Controller Networks for Real-Time Decision-Making in Embodied Learning"
authors: ["Hengkai Tan", "Songming Liu", "Kai Ma", "Chengyang Ying", "Xingxing Zhang", "Hang Su", "Jun Zhu"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "nDps3Q8j2l"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c4b23ea3b2a5c8b61db19feaa7ee3d7ec093de57.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:32+09:00"
---

# Fourier Controller Networks for Real-Time Decision-Making in Embodied Learning

## Abstract
Transformer has shown promise in reinforcement learning to model time-varying features for obtaining generalized low-level robot policies on diverse robotics datasets in embodied learning. However, it still suffers from the issues of low data efficiency and high inference latency. In this paper, we propose to investigate the task from a new perspective of the frequency domain. We first observe that the energy density in the frequency domain of a robot's trajectory is mainly concentrated in the low-frequency part. Then, we present the Fourier Controller Network (FCNet), a new network that uses Short-Time Fourier Transform (STFT) to extract and encode time-varying features through frequency domain interpolation. In order to do real-time decision-making, we further adopt FFT and Sliding DFT methods in the model architecture to achieve parallel training and efficient recurrent inference. Extensive results in both simulated (e.g., D4RL) and real-world environments (e.g., robot locomotion) demonstrate FCNet's substantial efficiency and effectiveness over existing methods such as Transformer, e.g., FCNet outperforms Transformer on multi-environmental robotics datasets of all types of sizes (from 1.9M to 120M). The project page and code can be found https://thkkk.github.io/fcnet.

## Metadata
- venue: ICML
- year: 2024
- authors: Hengkai Tan, Songming Liu, Kai Ma, Chengyang Ying, Xingxing Zhang, Hang Su, Jun Zhu
- arxiv_id: 
- openreview_id: nDps3Q8j2l
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c4b23ea3b2a5c8b61db19feaa7ee3d7ec093de57.pdf
- published: 2024

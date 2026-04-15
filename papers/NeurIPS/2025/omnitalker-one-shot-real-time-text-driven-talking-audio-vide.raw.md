---
title: "OmniTalker: One-shot Real-time Text-Driven Talking Audio-Video Generation With Multimodal Style Mimicking"
authors: ["Zhongjian Wang", "Peng Zhang", "Jinwei Qi", "wang guang yuan", "Sheng Xu", "Bang Zhang"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "eK31JidsTN"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/1c3ee3cd7deef3a0306332032797800370df2665.pdf"
published: "2025"
categories: []
keywords: ["talking head", "audiovisual generation", "text-driven talking head"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:56+09:00"
---

# OmniTalker: One-shot Real-time Text-Driven Talking Audio-Video Generation With Multimodal Style Mimicking

## Abstract
Although significant progress has been made in audio-driven talking head generation, text-driven methods remain underexplored. In this work, we present OmniTalker, a unified framework that jointly generates synchronized talking audio-video content from input text while emulating the target identity's speaking and facial movement styles, including speech characteristics, head motion, and facial dynamics. Our framework adopts a dual-branch diffusion transformer (DiT) architecture, with one branch dedicated to audio generation and the other to video synthesis.
At the shallow layers, cross-modal fusion modules are introduced to integrate information between the two modalities. In deeper layers, each modality is processed independently, with the generated audio decoded by a vocoder and the video rendered using a GAN-based high-quality visual renderer. Leveraging DiT’s in-context learning capability through a masked-infilling strategy, our model can simultaneously capture both audio and visual styles without requiring explicit style extraction modules.  Thanks to the efficiency of the DiT backbone and the optimized visual renderer, OmniTalker achieves real-time inference at 25 FPS.
To the best of our knowledge, OmniTalker is the first one-shot framework capable of jointly modeling speech and facial styles in real time. Extensive experiments demonstrate its superiority over existing methods in terms of generation quality, particularly in preserving style consistency and ensuring precise audio-video synchronization, all while maintaining efficient inference.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Zhongjian Wang, Peng Zhang, Jinwei Qi, wang guang yuan, Sheng Xu, Bang Zhang
- arxiv_id: 
- openreview_id: eK31JidsTN
- anthology_id: 
- pdf_url: https://openreview.net/pdf/1c3ee3cd7deef3a0306332032797800370df2665.pdf
- published: 2025
- keywords: talking head, audiovisual generation, text-driven talking head

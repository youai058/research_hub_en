---
title: "MDT-A2G: Exploring Masked Diffusion Transformers for Co-Speech Gesture Generation"
authors: ["Xiaofeng Mao", "Zhengkai Jiang", "Qilin Wang", "Chencan Fu", "Jiangning Zhang", "Jiafu Wu", "Yabiao Wang", "Chengjie Wang", "Wei Li", "Mingmin Chi"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2408.03312"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2408.03312v1"
published: "2024-08-06"
categories: ["cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:05+09:00"
---

# MDT-A2G: Exploring Masked Diffusion Transformers for Co-Speech Gesture Generation

## Abstract
Recent advancements in the field of Diffusion Transformers have substantially improved the generation of high-quality 2D images, 3D videos, and 3D shapes. However, the effectiveness of the Transformer architecture in the domain of co-speech gesture generation remains relatively unexplored, as prior methodologies have predominantly employed the Convolutional Neural Network (CNNs) or simple a few transformer layers. In an attempt to bridge this research gap, we introduce a novel Masked Diffusion Transformer for co-speech gesture generation, referred to as MDT-A2G, which directly implements the denoising process on gesture sequences. To enhance the contextual reasoning capability of temporally aligned speech-driven gestures, we incorporate a novel Masked Diffusion Transformer. This model employs a mask modeling scheme specifically designed to strengthen temporal relation learning among sequence gestures, thereby expediting the learning process and leading to coherent and realistic motions. Apart from audio, Our MDT-A2G model also integrates multi-modal information, encompassing text, emotion, and identity. Furthermore, we propose an efficient inference strategy that diminishes the denoising computation by leveraging previously calculated results, thereby achieving a speedup with negligible performance degradation. Experimental results demonstrate that MDT-A2G excels in gesture generation, boasting a learning speed that is over 6$\times$ faster than traditional diffusion transformers and an inference speed that is 5.7$\times$ than the standard diffusion model.

## Metadata
- venue: arXiv
- year: 2024
- authors: Xiaofeng Mao, Zhengkai Jiang, Qilin Wang, Chencan Fu, Jiangning Zhang, Jiafu Wu, Yabiao Wang, Chengjie Wang, Wei Li, Mingmin Chi
- arxiv_id: 2408.03312
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2408.03312v1
- published: 2024-08-06

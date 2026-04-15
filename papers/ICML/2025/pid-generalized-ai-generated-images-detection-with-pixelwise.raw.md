---
title: "PiD: Generalized AI-Generated Images Detection with Pixelwise Decomposition Residuals"
authors: ["Xinghe Fu", "Zhiyuan Yan", "Zheng Yang", "Taiping Yao", "Yandan Zhao", "Shouhong Ding", "Xi Li"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "gye2zYytx6"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0b6cbce9e5fcc533e9b8fd580283de93f75beabd.pdf"
published: "2025"
categories: []
keywords: ["AIGC detection", "Generative models", "Deepfakes", "Deep learning", "Image representation", "Low-level vision"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:31+09:00"
---

# PiD: Generalized AI-Generated Images Detection with Pixelwise Decomposition Residuals

## Abstract
Fake images, created by recently advanced generative models, have become increasingly indistinguishable from real ones, making their detection crucial, urgent, and challenging. This paper introduces PiD (Pixelwise Decomposition Residuals), a novel detection method that focuses on residual signals within images. Generative models are designed to optimize high-level semantic content (principal components), often overlooking low-level signals (residual components). PiD leverages this observation by disentangling residual components from images, encouraging the model to uncover more underlying and general forgery clues independent of semantic content. Compared to prior approaches that rely on reconstruction techniques or high-frequency information, PiD is computationally efficient and does not rely on any generative models for reconstruction. Specifically, PiD operates at the pixel level, mapping the pixel vector to another color space (e.g., YUV) and then quantizing the vector. The pixel vector is mapped back to the RGB space and the quantization loss is taken as the residual for AIGC detection. Our experiment results are striking and highly surprising: PiD achieves 98% accuracy on the widely used GenImage benchmark, highlighting the effectiveness and generalization performance.

## Metadata
- venue: ICML
- year: 2025
- authors: Xinghe Fu, Zhiyuan Yan, Zheng Yang, Taiping Yao, Yandan Zhao, Shouhong Ding, Xi Li
- arxiv_id: 
- openreview_id: gye2zYytx6
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0b6cbce9e5fcc533e9b8fd580283de93f75beabd.pdf
- published: 2025
- keywords: AIGC detection, Generative models, Deepfakes, Deep learning, Image representation, Low-level vision

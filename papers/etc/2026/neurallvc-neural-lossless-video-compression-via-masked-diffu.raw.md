---
title: "NeuralLVC: Neural Lossless Video Compression via Masked Diffusion with Temporal Conditioning"
authors: ["Tiberio Uricchio", "Marco Bertini"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2604.03353"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2604.03353v1"
published: "2026-04-03"
categories: ["eess.IV", "cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:09+09:00"
---

# NeuralLVC: Neural Lossless Video Compression via Masked Diffusion with Temporal Conditioning

## Abstract
While neural lossless image compression has advanced significantly with learned entropy models, lossless video compression remains largely unexplored in the neural setting. We present NeuralLVC, a neural lossless video codec that combines masked diffusion with an I/P-frame architecture for exploiting temporal redundancy. Our I-frame model compresses individual frames using bijective linear tokenization that guarantees exact pixel reconstruction. The P-frame model compresses temporal differences between consecutive frames, conditioned on the previous decoded frame via a lightweight reference embedding that adds only 1.3% trainable parameters. Group-wise decoding enables controllable speed-compression trade-offs. Our codec is lossless in the input domain: for video, it reconstructs YUV420 planes exactly; for image evaluation, RGB channels are reconstructed exactly. Experiments on 9 Xiph CIF sequences show that NeuralLVC outperforms H.264 and H.265 lossless by a significant margin. We verify exact reconstruction through end-to-end encode-decode testing with arithmetic coding. These results suggest that masked diffusion with temporal conditioning is a promising direction for neural lossless video compression.

## Metadata
- venue: arXiv
- year: 2026
- authors: Tiberio Uricchio, Marco Bertini
- arxiv_id: 2604.03353
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2604.03353v1
- published: 2026-04-03

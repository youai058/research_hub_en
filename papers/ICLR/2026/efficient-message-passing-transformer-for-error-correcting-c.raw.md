---
title: "Efficient Message-Passing Transformer for Error Correcting Codes"
authors: ["Seong-Joon Park", "Taewoo Park", "Hee-Youl Kwak", "Sang-Hyo Kim", "Yongjune Kim", "Jong-Seon No"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Xk8cwnwu2e"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/4202f9b35ce1aee26ab50097668a0b03a995719d.pdf"
published: "2026"
categories: []
keywords: ["Channel coding", "Error correcting codes", "Transformer-based decoder", "Message-passing decoder", "Neural decoder", "Transformer", "Efficient attention module"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:51+09:00"
---

# Efficient Message-Passing Transformer for Error Correcting Codes

## Abstract
Error correcting codes (ECCs) are a fundamental technique for ensuring reliable communication over noisy channels. Recent advances in deep learning have enabled transformer-based decoders to achieve state-of-the-art performance on short codes; however, their computational complexity remains significantly higher than that of classical decoders due to the attention mechanism. To address this challenge, we propose EfficientMPT, an efficient message-passing transformer that significantly reduces computational complexity while preserving decoding performance. A key feature of EfficientMPT is the Efficient Error Correcting (EEC) attention mechanism, which replaces expensive matrix multiplications with lightweight vector-based element-wise operations. Unlike standard attention, EEC attention relies only on query-key interaction using global query vector, efficiently encode global contextual information for ECC decoding. Furthermore, EfficientMPT can serve as a foundation model, capable of decoding various code classes and long codes by fine-tuning. In particular, EfficientMPT achieves 85% and 91% of significant memory reduction and 47% and 57% of FLOPs reduction compared to ECCT for $(648,540)$ and $(1056,880)$ standard LDPC code, respectively.

## Metadata
- venue: ICLR
- year: 2026
- authors: Seong-Joon Park, Taewoo Park, Hee-Youl Kwak, Sang-Hyo Kim, Yongjune Kim, Jong-Seon No
- arxiv_id: 
- openreview_id: Xk8cwnwu2e
- anthology_id: 
- pdf_url: https://openreview.net/pdf/4202f9b35ce1aee26ab50097668a0b03a995719d.pdf
- published: 2026
- keywords: Channel coding, Error correcting codes, Transformer-based decoder, Message-passing decoder, Neural decoder, Transformer, Efficient attention module

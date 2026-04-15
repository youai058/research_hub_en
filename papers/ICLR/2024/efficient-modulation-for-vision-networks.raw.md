---
title: "Efficient Modulation for Vision Networks"
authors: ["Xu Ma", "Xiyang Dai", "Jianwei Yang", "Bin Xiao", "Yinpeng Chen", "Yun Fu", "Lu Yuan"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ip5LHJs6QX"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/60b84aa807789b9bf4b5e8f2ff637e481c3cd2c8.pdf"
published: "2024"
categories: []
keywords: ["EfficientMod", "Efficient Networks"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:16+09:00"
---

# Efficient Modulation for Vision Networks

## Abstract
In this work, we present efficient modulation, a novel design for efficient vision networks. We revisit the modulation mechanism, which operates input through convolutional context modeling and feature projection layers, and fuses features via element-wise multiplication and an MLP block. We demonstrate that the abstracted modulation mechanism is particularly well suited for efficient networks and further tailor the modulation design by proposing the efficient modulation (EfficientMod) block, which is considered the essential building block for our networks. Bene- fiting from the prominent representational ability of modulation mechanism and the efficiency of efficient modulation design, our network can accomplish better accuracy-efficiency trade-offs and set new state-of-the-art performance for efficient networks. When integrating EfficientMod block with the vanilla self-attention block, we obtain the hybrid architecture and further improve the performance without sacrificing the efficiency. We carry out comprehensive experiments to verify EfficientMod’s performance. With fewer parameters, our EfficientMod-s performs 0.6 top-1 accuracy better than the prior state-of-the-art approach EfficientFormerV2-s2 without any training tricks and is 25% faster on GPU. Additionally, our method presents a notable improvement in downstream tasks, outperforming EfficientFormerV2-s by 3.6 mIoU on the ADE20K benchmark. Code and checkpoints are available at https://github.com/ma-xu/EfficientMod.

## Metadata
- venue: ICLR
- year: 2024
- authors: Xu Ma, Xiyang Dai, Jianwei Yang, Bin Xiao, Yinpeng Chen, Yun Fu, Lu Yuan
- arxiv_id: 
- openreview_id: ip5LHJs6QX
- anthology_id: 
- pdf_url: https://openreview.net/pdf/60b84aa807789b9bf4b5e8f2ff637e481c3cd2c8.pdf
- published: 2024
- keywords: EfficientMod, Efficient Networks

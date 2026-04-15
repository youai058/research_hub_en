---
title: "Large Displacement Motion Transfer with Unsupervised Anytime Interpolation"
authors: ["Guixiang Wang", "Jianjun Li"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "rMCyR6VSOM"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/45429d1cf993299673b76ff229ab45ff9a4d9d66.pdf"
published: "2025"
categories: []
keywords: ["Image animation", "action generation", "Unsupervised Interpolation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:37+09:00"
---

# Large Displacement Motion Transfer with Unsupervised Anytime Interpolation

## Abstract
Motion transfer is to transfer pose in driving video to object of source image, so that object of source image moves. Although great progress has been made recently in unsupervised motion transfer, many unsupervised methods still struggle to accurately model large displacement motions when large motion differences occur between source and driving images. To solve the problem, we propose an unsupervised anytime interpolation based large displacement motion transfer method, which can generate a series of anytime interpolated images between source and driving images. By decomposing large displacement motion into many small displacement motions, difficulty of large displacement motion estimation is reduced. In the process, we design a selector that can select optimal interpolated image from generated interpolated images for downstream tasks. Since there are no real images as labels in the interpolation process, we propose a bidirectional training strategy. Some constraints are added to optimal interpolated image to generate a reasonable interpolated image. To encourage network to generate high-quality images, a pre-trained Vision Transformer model is used to design constraint losses. Finally, experiments show that compared with the large displacement motion between source and driving images, small displacement motion between interpolated and driving images is easier to realize motion transfer. Compared with existing state-of-art methods, our method has significant improvements in motion-related metrics.

## Metadata
- venue: ICML
- year: 2025
- authors: Guixiang Wang, Jianjun Li
- arxiv_id: 
- openreview_id: rMCyR6VSOM
- anthology_id: 
- pdf_url: https://openreview.net/pdf/45429d1cf993299673b76ff229ab45ff9a4d9d66.pdf
- published: 2025
- keywords: Image animation, action generation, Unsupervised Interpolation

---
title: "GTR: A General, Multi-View, and Dynamic Framework for Trajectory Representation Learning"
authors: ["Xiangheng Wang", "Ziquan Fang", "Chenglong Huang", "Danlei Hu", "Lu Chen", "Yunjun Gao"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ehcWKZ2nEn"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/cae16f9a69f957790f303e75bc95c372b0ec8b9c.pdf"
published: "2025"
categories: []
keywords: ["Trajectory representation learning", "mobility learning", "spatio-temporal learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:32+09:00"
---

# GTR: A General, Multi-View, and Dynamic Framework for Trajectory Representation Learning

## Abstract
Trajectory representation learning aims to transform raw trajectory data into compact and low-dimensional vectors that are suitable for downstream analysis. However, most existing methods adopt either a free-space view or a road-network view during the learning process, which limits their ability to capture the complex, multi-view spatiotemporal features inherent in trajectory data. Moreover, these approaches rely on task-specific model training, restricting their generalizability and effectiveness for diverse analysis tasks. To this end, we propose GTR, a general, multi-view, and dynamic Trajectory Representation framework built on a pre-train and fine-tune architecture. Specifically, GTR introduces a multi-view encoder that captures the intrinsic multi-view spatiotemporal features. Based on the pre-train and fine-tune architecture, we provide the spatio-temporal fusion pre-training with a spatio-temporal mixture of experts to dynamically combine spatial and temporal features, enabling seamless adaptation to diverse trajectory analysis tasks. Furthermore, we propose an online frozen-hot updating strategy to efficiently update the representation model, accommodating the dynamic nature of trajectory data. Extensive experiments on two real-world datasets demonstrate that GTR consistently outperforms 15 state-of-the-art methods across 6 mainstream trajectory analysis tasks. All source code and data are available at https://github.com/ZJU-DAILY/GTR.

## Metadata
- venue: ICML
- year: 2025
- authors: Xiangheng Wang, Ziquan Fang, Chenglong Huang, Danlei Hu, Lu Chen, Yunjun Gao
- arxiv_id: 
- openreview_id: ehcWKZ2nEn
- anthology_id: 
- pdf_url: https://openreview.net/pdf/cae16f9a69f957790f303e75bc95c372b0ec8b9c.pdf
- published: 2025
- keywords: Trajectory representation learning, mobility learning, spatio-temporal learning

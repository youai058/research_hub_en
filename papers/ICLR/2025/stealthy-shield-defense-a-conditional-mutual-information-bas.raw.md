---
title: "Stealthy Shield Defense: A Conditional Mutual Information-Based Approach against Black-Box Model Inversion Attacks"
authors: ["Tianqu Zhuang", "Hongyao Yu", "Yixiang Qiu", "Hao Fang", "Bin Chen", "Shu-Tao Xia"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "p0DjhjPXl3"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/31d2f9468bd3648529d3006f7d3b84b885257997.pdf"
published: "2025"
categories: []
keywords: ["AI security", "model inversion attack", "information bottleneck", "conditional mutual information"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:52+09:00"
---

# Stealthy Shield Defense: A Conditional Mutual Information-Based Approach against Black-Box Model Inversion Attacks

## Abstract
Model inversion attacks (MIAs) aim to reconstruct the private training data by accessing the public model, raising concerns about privacy leakage. Black-box MIAs, where attackers can only query the model and obtain outputs, are closer to real-world scenarios. The latest black-box attacks have outperformed state-of-the-art white-box attacks, and existing defenses cannot resist them effectively. To fill this gap, we propose Stealthy Shield Defense (SSD), a post-processing algorithm against black-box MIAs. Our idea is to modify the model's outputs to minimize the conditional mutual information (CMI). We mathematically prove that CMI is a special case of Information Bottleneck (IB), and thus inherits the benefits of IB---making predictions less dependent on inputs and more dependent on ground truths. This theoretically guarantees our effectiveness, both in resisting MIAs and preserving utility. To minimize CMI, we formulate a convex optimization problem and solve it via the water-filling method. Without the need to retrain the model, our defense is plug-and-play and easy to deploy. Experimental results indicate that SSD outperforms existing defenses, in terms of MIA resistance and model's utility, across various attack algorithms, private datasets, and model architectures. Our code is available at https://github.com/ZhuangQu/Stealthy-Shield-Defense.

## Metadata
- venue: ICLR
- year: 2025
- authors: Tianqu Zhuang, Hongyao Yu, Yixiang Qiu, Hao Fang, Bin Chen, Shu-Tao Xia
- arxiv_id: 
- openreview_id: p0DjhjPXl3
- anthology_id: 
- pdf_url: https://openreview.net/pdf/31d2f9468bd3648529d3006f7d3b84b885257997.pdf
- published: 2025
- keywords: AI security, model inversion attack, information bottleneck, conditional mutual information

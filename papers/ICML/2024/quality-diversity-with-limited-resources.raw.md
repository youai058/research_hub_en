---
title: "Quality-Diversity with Limited Resources"
authors: ["Ren-Jian Wang", "Ke Xue", "Cong Guan", "Chao Qian"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "64I29YeQdt"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2f38ee1fc028d9178c066d52e3fcaec0a5b97e44.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:31+09:00"
---

# Quality-Diversity with Limited Resources

## Abstract
Quality-Diversity (QD) algorithms have emerged as a powerful optimization paradigm with the aim of generating a set of high-quality and diverse solutions. To achieve such a challenging goal, QD algorithms require maintaining a large archive and a large population in each iteration, which brings two main issues, sample and resource efficiency. Most advanced QD algorithms focus on improving the sample efficiency, while the resource efficiency is overlooked to some extent. Particularly, the resource overhead during the training process has not been touched yet, hindering the wider application of QD algorithms. In this paper, we highlight this important research question, i.e., how to efficiently train QD algorithms with limited resources, and propose a novel and effective method called RefQD to address it. RefQD decomposes a neural network into representation and decision parts, and shares the representation part with all decision parts in the archive to reduce the resource overhead. It also employs a series of strategies to address the mismatch issue between the old decision parts and the newly updated representation part. Experiments on different types of tasks from small to large resource consumption demonstrate the excellent performance of RefQD: it not only uses significantly fewer resources (e.g., 16% GPU memories on QDax and 3.7% on Atari) but also achieves comparable or better performance compared to sample-efficient QD algorithms. Our code is available at [https://github.com/lamda-bbo/RefQD](https://github.com/lamda-bbo/RefQD).

## Metadata
- venue: ICML
- year: 2024
- authors: Ren-Jian Wang, Ke Xue, Cong Guan, Chao Qian
- arxiv_id: 
- openreview_id: 64I29YeQdt
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2f38ee1fc028d9178c066d52e3fcaec0a5b97e44.pdf
- published: 2024

---
title: "Enhancing Tail Performance in Extreme Classifiers by Label Variance Reduction"
authors: ["Anirudh Buvanesh", "Rahul Chand", "Jatin Prakash", "Bhawna Paliwal", "Mudit Dhawan", "Neelabh Madan", "Deepesh Hada", "Vidit Jain", "SONU MEHTA", "Yashoteja Prabhu", "Manish Gupta", "Ramachandran Ramjee", "Manik Varma"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "6ARlSgun7J"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a20d3764489727d5956f74f1b28ba95a1d848575.pdf"
published: "2024"
categories: []
keywords: ["Extreme Classification", "Extreme Multi-Label Learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:50+09:00"
---

# Enhancing Tail Performance in Extreme Classifiers by Label Variance Reduction

## Abstract
Extreme Classification (XC) architectures, which utilize a massive One-vs-All (OvA) classifier layer at the output, have demonstrated remarkable performance on problems with large label sets. Nonetheless, these architectures falter on tail labels with few representative samples. This phenomenon has been attributed to factors such as classifier over-fitting and missing label bias, and solutions involving regularization and loss re-calibration have been developed. This paper explores the impact of label variance - a previously unexamined factor - on the tail performance in extreme classifiers. It also develops a method to systematically reduce label variance in XC by transferring the knowledge from a specialized tail-robust teacher model to the OvA classifiers. For this purpose, it proposes a principled knowledge distillation framework, LEVER, which enhances the tail performance in extreme classifiers with formal guarantees on generalization. Comprehensive experiments are conducted on a diverse set of XC datasets, demonstrating that LEVER can enhance tail performance by around 5\% and 6\% points in PSP and coverage metrics, respectively, when integrated with leading extreme classifiers. Moreover, it establishes a new state-of-the-art when added to the top-performing Renee classifier. Extensive ablations and analyses substantiate the efficacy of our design choices. Another significant contribution is the release of two new XC datasets that are different from and more challenging than the available benchmark datasets, thereby encouraging more rigorous algorithmic evaluation in the future. Code for LEVER is available at: aka.ms/lever.

## Metadata
- venue: ICLR
- year: 2024
- authors: Anirudh Buvanesh, Rahul Chand, Jatin Prakash, Bhawna Paliwal, Mudit Dhawan, Neelabh Madan, Deepesh Hada, Vidit Jain, SONU MEHTA, Yashoteja Prabhu, Manish Gupta, Ramachandran Ramjee, Manik Varma
- arxiv_id: 
- openreview_id: 6ARlSgun7J
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a20d3764489727d5956f74f1b28ba95a1d848575.pdf
- published: 2024
- keywords: Extreme Classification, Extreme Multi-Label Learning

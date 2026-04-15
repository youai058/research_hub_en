---
title: "Entropy-Reinforced Planning with Large Language Models for Drug Discovery"
authors: ["Xuefeng Liu", "Chih-chan Tien", "Peng Ding", "Songhao Jiang", "Rick L. Stevens"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "F3Ds71Xgo1"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d15efb1d4168c26d4d8750e3aef0621b0109f343.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:44+09:00"
---

# Entropy-Reinforced Planning with Large Language Models for Drug Discovery

## Abstract
The objective of drug discovery is to identify chemical compounds that possess specific pharmaceutical properties toward a binding target. Existing large language models (LLMS) can achieve high token matching scores in terms of likelihood for molecule generation. However, relying solely on LLM decoding often results in the generation of molecules that are either invalid due to a single misused token, or suboptimal due to unbalanced exploration and exploitation as a consequence of the LLM’s prior experience. Here we propose ERP, Entropy-Reinforced Planning for Transformer Decoding, which employs an entropy-reinforced planning algorithm to enhance the Transformer decoding process and strike a balance between exploitation and exploration. ERP aims to achieve improvements in multiple properties compared to direct sampling from the Transformer. We evaluated ERP on the SARS-CoV-2 virus (3CLPro) and human cancer cell target protein (RTCB) benchmarks and demonstrated that, in both benchmarks, ERP consistently outperforms the current state-of-the-art algorithm by 1-5 percent, and baselines by 5-10 percent, respectively. Moreover, such improvement is robust across Transformer models trained with different objectives. Finally, to further illustrate the capabilities of ERP, we tested our algorithm on three code generation benchmarks and outperformed the current state-of-the-art approach as well. Our code is publicly available at: https://github.com/xuefeng-cs/ERP.

## Metadata
- venue: ICML
- year: 2024
- authors: Xuefeng Liu, Chih-chan Tien, Peng Ding, Songhao Jiang, Rick L. Stevens
- arxiv_id: 
- openreview_id: F3Ds71Xgo1
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d15efb1d4168c26d4d8750e3aef0621b0109f343.pdf
- published: 2024

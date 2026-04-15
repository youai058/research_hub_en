---
title: "DynaMath: A Dynamic Visual Benchmark for Evaluating Mathematical Reasoning Robustness of Vision Language Models"
authors: ["Chengke Zou", "Xingang Guo", "Rui Yang", "Junyu Zhang", "Bin Hu", "Huan Zhang"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "VOAMTA8jKu"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/dfd2c46a07f4c2541b1b52bff3a77b0b1f88d778.pdf"
published: "2025"
categories: []
keywords: ["Visual Mathematical Benchmark", "Vision Language Models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:11+09:00"
---

# DynaMath: A Dynamic Visual Benchmark for Evaluating Mathematical Reasoning Robustness of Vision Language Models

## Abstract
The rapid advancements in Vision-Language Models (VLMs) have shown great potential in tackling mathematical reasoning tasks that involve visual context. Unlike humans who can reliably apply solution steps to similar problems with minor modifications, we found that state-of-the-art VLMs like GPT-4o can consistently fail in these scenarios, revealing limitations in their mathematical reasoning capabilities. In this paper, we investigate the **mathematical reasoning robustness** in VLMs and evaluate how well these models perform under different variants of the same question, such as changes in visual numerical values or function graphs.
While several vision-based math benchmarks have been developed to assess VLMs' problem-solving capabilities, these benchmarks contain only static sets of problems and cannot easily evaluate mathematical reasoning robustness.
To fill this gap, we introduce **DynaMath**, a dynamic visual math benchmark designed for in-depth assessment of VLMs. **DynaMath** includes 501 high-quality, multi-topic *seed* questions, *each represented as a Python program*. Those programs are carefully designed and annotated to enable the automatic generation of a much larger set of *concrete* questions, including many different types of visual and textual variations. 
**DynaMath** allows us to evaluate the generalization ability of VLMs, by assessing their performance under varying input conditions of a seed question. We evaluated 14 state-of-the-art VLMs with 5,010 generated concrete questions (10 per seed question). Our results show that the worst-case model accuracy, defined as the percentage of correctly answered seed questions in all 10 variants, is significantly lower than the average-case accuracy. In addition, many models show high consistency in answering these questions -- the incorrectness of a certain variant of a seed question is not only due to inherent randomness. Our analysis emphasizes the need to study the robustness of VLMs' reasoning abilities, and **DynaMath** provides valuable insights to guide the development of more reliable models for mathematical reasoning.

## Metadata
- venue: ICLR
- year: 2025
- authors: Chengke Zou, Xingang Guo, Rui Yang, Junyu Zhang, Bin Hu, Huan Zhang
- arxiv_id: 
- openreview_id: VOAMTA8jKu
- anthology_id: 
- pdf_url: https://openreview.net/pdf/dfd2c46a07f4c2541b1b52bff3a77b0b1f88d778.pdf
- published: 2025
- keywords: Visual Mathematical Benchmark, Vision Language Models

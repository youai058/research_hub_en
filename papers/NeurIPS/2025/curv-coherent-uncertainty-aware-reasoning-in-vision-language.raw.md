---
title: "CURV: Coherent Uncertainty-Aware Reasoning in Vision-Language Models for X-Ray Report Generation"
authors: ["Ziao Wang", "Sixing Yan", "Kejing Yin", "Xiaofeng Zhang", "William K. Cheung"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "3BTqvtwZYY"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e26d7b613c5dbd8d52329e1b41756f52db6da76e.pdf"
published: "2025"
categories: []
keywords: ["Chest X-Ray Report Generation", "Vision Language Models", "Uncertainty-Aware Reasoning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:45+09:00"
---

# CURV: Coherent Uncertainty-Aware Reasoning in Vision-Language Models for X-Ray Report Generation

## Abstract
Vision-language models have been explored for radiology report generation with promising results. Yet, uncertainty elaborated in findings and the reasoning process for reaching clinical impressions are seldom explicitly modeled, reducing the clinical accuracy and trustworthiness of the generated reports. We present CURV, a novel framework that alleviates the limitations through integrated awareness of uncertainty and explicit reasoning capabilities. Our approach consists of three key components: (1) an uncertainty modeling mechanism that teaches the model to recognize and express appropriate levels of diagnostic confidence, (2) a structured reasoning framework that generates intermediate explanatory steps connecting visual findings to clinical impressions, and (3) a reasoning coherence reward that ensures logical consistency among findings, reasoning, and impressions. We implement CURV through a three-stage training pipeline that combines uncertainty-aware fine-tuning, reasoning initialization, and reinforcement learning. In particular, we adopt a comprehensive reward function addresses multiple aspects of report quality, incorporating medical term matching, uncertainty expression evaluation, and semantic coherence evaluation. Experimental results demonstrate that CURV generates clinically relevant reports with appropriate uncertainty expressions and transparent reasoning traces, significantly outperforming previous methods. CURV represents a substantial advancement toward interpretable and trustworthy AI-generated radiology reports, with broader implications for the deployment of vision-language models in high-stakes clinical environments where uncertainty awareness and reasoning transparency are essential.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Ziao Wang, Sixing Yan, Kejing Yin, Xiaofeng Zhang, William K. Cheung
- arxiv_id: 
- openreview_id: 3BTqvtwZYY
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e26d7b613c5dbd8d52329e1b41756f52db6da76e.pdf
- published: 2025
- keywords: Chest X-Ray Report Generation, Vision Language Models, Uncertainty-Aware Reasoning

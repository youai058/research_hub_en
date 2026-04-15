---
title: "OpenRCA: Can Large Language Models Locate the Root Cause of Software Failures?"
authors: ["Junjielong Xu", "Qinan Zhang", "Zhiqing Zhong", "Shilin He", "Chaoyun Zhang", "Qingwei Lin", "Dan Pei", "Pinjia He", "Dongmei Zhang", "Qi Zhang"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "M4qNIzQYpd"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/388fe964a16cdde844404051497859daabbf6fe0.pdf"
published: "2025"
categories: []
keywords: ["Language models", "Natural language processing", "Software engineering"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:06+09:00"
---

# OpenRCA: Can Large Language Models Locate the Root Cause of Software Failures?

## Abstract
Large language models (LLMs) are driving substantial advancements in software engineering, with successful applications like Copilot and Cursor transforming real-world development practices. However, current research predominantly focuses on the early stages of development, such as code generation, while overlooking the post-development phases that are crucial to user experience. To explore the potential of LLMs in this direction, we propose OpenRCA, a benchmark dataset and evaluation framework for assessing LLMs’ ability to identify the root cause of software failures. OpenRCA includes 335 failures from three enterprise software systems, along with over 68 GB of telemetry data (logs, metrics, and traces). Given a failure case and its associated telemetry, the LLM is tasked to identify the root cause that triggered the failure, requiring comprehension of software dependencies and reasoning over heterogeneous, long-context telemetry data. Our results show substantial room for improvement, as current models can only handle the simplest cases. Even with the specially designed RCA-agent, the best-performing model, Claude 3.5, solved only 11.34% failure cases. Our work paves the way for future research in this direction.

## Metadata
- venue: ICLR
- year: 2025
- authors: Junjielong Xu, Qinan Zhang, Zhiqing Zhong, Shilin He, Chaoyun Zhang, Qingwei Lin, Dan Pei, Pinjia He, Dongmei Zhang, Qi Zhang
- arxiv_id: 
- openreview_id: M4qNIzQYpd
- anthology_id: 
- pdf_url: https://openreview.net/pdf/388fe964a16cdde844404051497859daabbf6fe0.pdf
- published: 2025
- keywords: Language models, Natural language processing, Software engineering

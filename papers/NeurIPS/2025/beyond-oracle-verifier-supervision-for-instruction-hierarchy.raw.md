---
title: "Beyond Oracle: Verifier-Supervision for Instruction Hierarchy in Reasoning and Instruction-Tuned LLMs"
authors: ["Sian-Yao Huang", "Li-Hsien Chang", "Che-Yu Lin", "Cheng-Lin Yang"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "IQ513IX1G5"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d576f2caa769be21da3d38e86e6ef480862f10ec.pdf"
published: "2025"
categories: []
keywords: ["instruction hierarchy", "verifiable supervision", "reasoning LLMs", "instruction-tuned LLMs", "programmatic verification", "oracle-free alignment", "safety generalization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:36+09:00"
---

# Beyond Oracle: Verifier-Supervision for Instruction Hierarchy in Reasoning and Instruction-Tuned LLMs

## Abstract
Large language models (LLMs) are often prompted with multi-level directives, such as system instructions and user queries, that imply a hierarchy of authority. Yet models frequently fail to enforce this structure, especially in multi-step reasoning where errors propagate across intermediate steps. Existing methods rely on oracle completions but lack verifiable reward signals or intermediate traces, limiting their applicability. We introduce a unified supervision framework that embeds programmatically verifiable checkers into synthesized instruction-conflict instances. Each instance pairs a compliance directive with a conflicting one, along with an executable verifier that deterministically checks output adherence. This enables alignment without oracle labels or reasoning traces, supporting both instruction-tuned and reasoning models. The framework is instantiated via a synthesis pipeline that includes unit-test–based validation, LLM-assisted repair, and a probabilistic analysis of cleaning reliability. Fine-tuning on the resulting data improves instruction hierarchy adherence and boosts safety robustness, generalizing to adversarial safety benchmarks without task-specific supervision. This highlights verifiable supervision as a scalable foundation for robust alignment. All code, dataset, and verifier pipeline are publicly available at: https://github.com/cycraft-corp/BeyondOracle.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Sian-Yao Huang, Li-Hsien Chang, Che-Yu Lin, Cheng-Lin Yang
- arxiv_id: 
- openreview_id: IQ513IX1G5
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d576f2caa769be21da3d38e86e6ef480862f10ec.pdf
- published: 2025
- keywords: instruction hierarchy, verifiable supervision, reasoning LLMs, instruction-tuned LLMs, programmatic verification, oracle-free alignment, safety generalization

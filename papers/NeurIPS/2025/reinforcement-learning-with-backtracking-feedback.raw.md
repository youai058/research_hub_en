---
title: "Reinforcement Learning with Backtracking Feedback"
authors: ["Bilgehan Sel", "Vaishakh Keshava", "Phillip Wallis", "Lukas Rutishauser", "Ming Jin", "Dingcheng Li"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "14B5d6NEaH"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/238b73fa0aa8697d940827f6657973777e3770bd.pdf"
published: "2025"
categories: []
keywords: ["large language models", "safety alignment", "reinforcement learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:30+09:00"
---

# Reinforcement Learning with Backtracking Feedback

## Abstract
Addressing the critical need for robust safety in Large Language Models (LLMs), particularly against adversarial attacks and in-distribution errors, we introduce Reinforcement Learning with Backtracking Feedback (RLBF). This framework advances upon prior methods, such as BSAFE, by primarily leveraging a Reinforcement Learning (RL) stage where models learn to dynamically correct their own generation errors. Through RL with critic feedback on the model's live outputs, LLMs are trained to identify and recover from their actual, emergent safety violations by emitting an efficient "backtrack by x tokens" signal, then continuing generation autoregressively. This RL process is crucial for instilling resilience against sophisticated adversarial strategies, including middle filling, Greedy Coordinate Gradient (GCG) attacks, and decoding parameter manipulations. To further support the acquisition of this backtracking capability, we also propose an enhanced Supervised Fine-Tuning (SFT) data generation strategy (BSAFE+). This method improves upon previous data creation techniques by injecting violations into coherent, originally safe text, providing more effective initial training for the backtracking mechanism. Comprehensive empirical evaluations demonstrate that RLBF significantly reduces attack success rates across diverse benchmarks and model scales, achieving superior safety outcomes while critically preserving foundational model utility.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Bilgehan Sel, Vaishakh Keshava, Phillip Wallis, Lukas Rutishauser, Ming Jin, Dingcheng Li
- arxiv_id: 
- openreview_id: 14B5d6NEaH
- anthology_id: 
- pdf_url: https://openreview.net/pdf/238b73fa0aa8697d940827f6657973777e3770bd.pdf
- published: 2025
- keywords: large language models, safety alignment, reinforcement learning

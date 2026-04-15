---
title: "Linguistic Calibration of Long-Form Generations"
authors: ["Neil Band", "Xuechen Li", "Tengyu Ma", "Tatsunori Hashimoto"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "rJVjQSQ8ye"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/190f6f7e3cf110213c6509db5399ced52f6f3bab.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:19+09:00"
---

# Linguistic Calibration of Long-Form Generations

## Abstract
Language models (LMs) may lead their users to make suboptimal downstream decisions when they confidently hallucinate. This issue can be mitigated by having the LM verbally convey the probability that its claims are correct, but existing models cannot produce long-form text with calibrated confidence statements. Through the lens of decision-making, we define linguistic calibration for long-form generations: an LM is linguistically calibrated if its generations enable its users to make calibrated probabilistic predictions. This definition enables a training framework where a supervised finetuning step bootstraps an LM to emit long-form generations with confidence statements such as "I estimate a 30% chance of..." or "I am certain that...", followed by a reinforcement learning step which rewards generations that enable a user to provide calibrated answers to related questions. We linguistically calibrate Llama 2 7B and find in automated and human evaluations of long-form generations that it is significantly more calibrated than strong finetuned factuality baselines with comparable accuracy. These findings generalize under significant domain shifts to scientific and biomedical questions and to an entirely held-out person biography generation task. Our results demonstrate that long-form generations may be calibrated end-to-end by constructing an objective in the space of the predictions that users make in downstream decision-making.

## Metadata
- venue: ICML
- year: 2024
- authors: Neil Band, Xuechen Li, Tengyu Ma, Tatsunori Hashimoto
- arxiv_id: 
- openreview_id: rJVjQSQ8ye
- anthology_id: 
- pdf_url: https://openreview.net/pdf/190f6f7e3cf110213c6509db5399ced52f6f3bab.pdf
- published: 2024

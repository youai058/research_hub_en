---
title: "Endless Jailbreaks with Bijection Learning"
authors: ["Brian R.Y. Huang", "Maximilian Li", "Leonard Tang"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "xP1radUi32"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/af895e970cc73ca7ef723e0e8be29e7afefa84d8.pdf"
published: "2025"
categories: []
keywords: ["jailbreaking", "redteaming", "AI safety", "AI alignment", "adversarial robustness", "adversarial attacks"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:57+09:00"
---

# Endless Jailbreaks with Bijection Learning

## Abstract
Despite extensive safety measures, LLMs are vulnerable to adversarial inputs, or jailbreaks, which can elicit unsafe behaviors. In this work, we introduce bijection learning, a powerful attack algorithm which automatically fuzzes LLMs for safety vulnerabilities using randomly-generated encodings whose complexity can be tightly controlled. We leverage in-context learning to teach models bijective encodings, pass encoded queries to the model to bypass built-in safety mechanisms, and finally decode responses back into English. Our attack is extremely effective on a wide range of frontier language models. By controlling complexity parameters such as number of key-value mappings in the encodings, we find a close relationship between the capability level of the attacked LLM and the average complexity of the most effective bijection attacks. Our work highlights that new vulnerabilities in frontier models can emerge with scale: more capable models are more severely jailbroken by bijection attacks.

## Metadata
- venue: ICLR
- year: 2025
- authors: Brian R.Y. Huang, Maximilian Li, Leonard Tang
- arxiv_id: 
- openreview_id: xP1radUi32
- anthology_id: 
- pdf_url: https://openreview.net/pdf/af895e970cc73ca7ef723e0e8be29e7afefa84d8.pdf
- published: 2025
- keywords: jailbreaking, redteaming, AI safety, AI alignment, adversarial robustness, adversarial attacks

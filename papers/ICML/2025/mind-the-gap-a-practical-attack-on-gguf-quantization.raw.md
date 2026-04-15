---
title: "Mind the Gap: A Practical Attack on GGUF Quantization"
authors: ["Kazuki Egashira", "Robin Staab", "Mark Vero", "Jingxuan He", "Martin Vechev"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "TV17MLZGuA"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ccd3dbcff58c23331acc1fac370a868ca4fd721e.pdf"
published: "2025"
categories: []
keywords: ["quantization", "large language models", "security", "poisoning", "gguf"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:18+09:00"
---

# Mind the Gap: A Practical Attack on GGUF Quantization

## Abstract
With the increasing size of frontier LLMs, post-training quantization has become the standard for memory-efficient deployment. Recent work has shown that basic rounding-based quantization schemes pose security risks, as they can be exploited to inject malicious behaviors into quantized models that remain hidden in full precision. However, existing attacks cannot be applied to more complex quantization methods, such as the GGUF family used in the popular ollama and llama.cpp frameworks. In this work, we address this gap by introducing the first attack on GGUF. Our key insight is that the quantization error -- the difference between the full-precision weights and their (de-)quantized version -- provides sufficient flexibility to construct malicious quantized models that appear benign in full precision. Leveraging this, we develop an attack that trains the target malicious LLM while constraining its weights based on quantization errors. We demonstrate the effectiveness of our attack on three popular LLMs across nine GGUF quantization data types on three diverse attack scenarios: insecure code generation ($\Delta$=$88.7\%$), targeted content injection ($\Delta$=$85.0\%$), and benign instruction refusal ($\Delta$=$30.1\%$). Our attack highlights that (1) the most widely used post-training quantization method is susceptible to adversarial interferences, and (2) the complexity of quantization schemes alone is insufficient as a defense.

## Metadata
- venue: ICML
- year: 2025
- authors: Kazuki Egashira, Robin Staab, Mark Vero, Jingxuan He, Martin Vechev
- arxiv_id: 
- openreview_id: TV17MLZGuA
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ccd3dbcff58c23331acc1fac370a868ca4fd721e.pdf
- published: 2025
- keywords: quantization, large language models, security, poisoning, gguf

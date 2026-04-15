---
title: "Instruction Tuning for Secure Code Generation"
authors: ["Jingxuan He", "Mark Vero", "Gabriela Krasnopolska", "Martin Vechev"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "MgTzMaYHvG"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/168f6d4a96b831e2fa9d7ae6ed64b703443ee8af.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:16+09:00"
---

# Instruction Tuning for Secure Code Generation

## Abstract
Modern language models (LMs) have gained widespread acceptance in everyday and professional contexts, particularly in programming. An essential procedure enabling this adoption is instruction tuning, which substantially enhances LMs' practical utility by training them to follow user instructions and human preferences. However, existing instruction tuning schemes overlook a crucial aspect: the security of generated code. As a result, even the state-of-the-art instruction-tuned LMs frequently produce unsafe code, posing significant security risks. In this work, we introduce SafeCoder to address this gap. SafeCoder performs security-centric fine-tuning using a diverse and high-quality dataset that we collected using an automated pipeline. We integrate the security fine-tuning with standard instruction tuning, to facilitate a joint optimization of both security and utility. Despite its simplicity, we show that SafeCoder is effective across a variety of popular LMs and datasets. It is able to drastically improve security (by about 30%), while preserving utility.

## Metadata
- venue: ICML
- year: 2024
- authors: Jingxuan He, Mark Vero, Gabriela Krasnopolska, Martin Vechev
- arxiv_id: 
- openreview_id: MgTzMaYHvG
- anthology_id: 
- pdf_url: https://openreview.net/pdf/168f6d4a96b831e2fa9d7ae6ed64b703443ee8af.pdf
- published: 2024

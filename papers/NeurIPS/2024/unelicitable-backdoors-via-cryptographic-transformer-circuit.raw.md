---
title: "Unelicitable Backdoors via Cryptographic Transformer Circuits"
authors: ["Andis Draguns", "Andrew Gritsevskiy", "Sumeet Ramesh Motwani", "Christian Schroeder de Witt"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "a560KLF3v5"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/4d20cad2b78694121ff0c20c54acee8926e86a31.pdf"
published: "2024"
categories: []
keywords: ["Backdoor attacks", "Transformers", "handcrafting model parameters", "cryptographic circuits"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:31+09:00"
---

# Unelicitable Backdoors via Cryptographic Transformer Circuits

## Abstract
The rapid proliferation of open-source language models significantly increases the risks of downstream backdoor attacks. These backdoors can introduce dangerous behaviours during model deployment and can evade detection by conventional cybersecurity monitoring systems. In this paper, we introduce a novel class of backdoors in transformer models, that, in contrast to prior art, are unelicitable in nature. Unelicitability prevents the defender from triggering the backdoor, making it impossible to properly evaluate ahead of deployment even if given full white-box access and using automated techniques, such as red-teaming or certain formal verification methods. We show that our novel construction is not only unelicitable thanks to using cryptographic techniques, but also has favourable robustness properties.
We confirm these properties in empirical investigations, and provide evidence that our backdoors can withstand state-of-the-art mitigation strategies. Additionally, we expand on previous work by showing that our universal backdoors, while not completely undetectable in white-box settings, can be harder to detect than some existing designs. By demonstrating the feasibility of seamlessly integrating backdoors into transformer models, this paper fundamentally questions the efficacy of pre-deployment detection strategies. This offers new insights into the offence-defence balance in AI safety and security.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Andis Draguns, Andrew Gritsevskiy, Sumeet Ramesh Motwani, Christian Schroeder de Witt
- arxiv_id: 
- openreview_id: a560KLF3v5
- anthology_id: 
- pdf_url: https://openreview.net/pdf/4d20cad2b78694121ff0c20c54acee8926e86a31.pdf
- published: 2024
- keywords: Backdoor attacks, Transformers, handcrafting model parameters, cryptographic circuits

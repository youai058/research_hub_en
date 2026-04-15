---
title: "Quantum-PEFT: Ultra parameter-efficient fine-tuning"
authors: ["Toshiaki Koike-Akino", "Francesco Tonin", "Yongtao Wu", "Frank Zhengqing Wu", "Leyla Naz Candogan", "Volkan Cevher"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "dgR6i4TSng"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/3007fb7ad498e8cf02a02e31c8b7b737d81ec792.pdf"
published: "2025"
categories: []
keywords: ["parameter-efficient fine-tuning", "lora", "quantum machine learning", "orthogonality constraints"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:49+09:00"
---

# Quantum-PEFT: Ultra parameter-efficient fine-tuning

## Abstract
This paper introduces Quantum-PEFT that leverages quantum computations for parameter-efficient fine-tuning (PEFT). Unlike other additive PEFT methods, such as low-rank adaptation (LoRA), Quantum-PEFT exploits an underlying full-rank yet surprisingly parameter efficient _quantum unitary parameterization_. With the use of Pauli parameterization, the number of trainable parameters grows only logarithmically with the ambient dimension, as opposed to linearly as in LoRA-based PEFT methods. Quantum-PEFT achieves vanishingly smaller number of trainable parameters than the lowest-rank LoRA as dimensions grow, enhancing parameter efficiency while maintaining a competitive performance. We apply Quantum-PEFT to several transfer learning benchmarks in language and vision, demonstrating significant advantages in parameter efficiency.

## Metadata
- venue: ICLR
- year: 2025
- authors: Toshiaki Koike-Akino, Francesco Tonin, Yongtao Wu, Frank Zhengqing Wu, Leyla Naz Candogan, Volkan Cevher
- arxiv_id: 
- openreview_id: dgR6i4TSng
- anthology_id: 
- pdf_url: https://openreview.net/pdf/3007fb7ad498e8cf02a02e31c8b7b737d81ec792.pdf
- published: 2025
- keywords: parameter-efficient fine-tuning, lora, quantum machine learning, orthogonality constraints

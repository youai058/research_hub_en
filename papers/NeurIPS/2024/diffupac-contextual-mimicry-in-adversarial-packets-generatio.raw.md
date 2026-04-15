---
title: "DiffuPac: Contextual Mimicry in Adversarial Packets Generation via Diffusion Model"
authors: ["Abdullah Bin Jasni", "Akiko Manada", "Kohei Watabe"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "KYHVBsEHuC"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c7b8fafa48ce5420354e0e23fae881bde7211d0e.pdf"
published: "2024"
categories: []
keywords: ["Network Intrusion Detection System", "Adversarial Machine Learning", "Cybersecurity", "Adversarial Sample Generation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:02+09:00"
---

# DiffuPac: Contextual Mimicry in Adversarial Packets Generation via Diffusion Model

## Abstract
In domains of cybersecurity, recent advancements in Machine Learning (ML) and Deep Learning (DL) have significantly enhanced Network Intrusion Detection Systems (NIDS), improving the effectiveness of cybersecurity operations. However, attackers have also leveraged ML/DL to develop sophisticated models that generate adversarial packets capable of evading NIDS detection. Consequently, defenders must study and analyze these models to prepare for the evasion attacks that exploit NIDS detection mechanisms. Unfortunately, conventional generation models often rely on unrealistic assumptions about attackers' knowledge of NIDS components, making them impractical for real-world scenarios. To address this issue, we present DiffuPac, a first-of-its-kind generation model designed to generate adversarial packets that evade detection without relying on specific NIDS components. DiffuPac integrates a pre-trained Bidirectional Encoder Representations from Transformers (BERT) with diffusion model, which, through its capability for conditional denoising and classifier-free guidance, effectively addresses the real-world constraint of limited attacker knowledge. By concatenating malicious packets with contextually relevant normal packets and applying targeted noising only to the malicious packets, DiffuPac seamlessly blends adversarial packets into genuine network traffic. Through evaluations on real-world datasets, we demonstrate that DiffuPac achieves strong evasion capabilities against sophisticated NIDS, outperforming conventional methods by an average of 6.69 percentage points, while preserving the functionality and practicality of the generated adversarial packets.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Abdullah Bin Jasni, Akiko Manada, Kohei Watabe
- arxiv_id: 
- openreview_id: KYHVBsEHuC
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c7b8fafa48ce5420354e0e23fae881bde7211d0e.pdf
- published: 2024
- keywords: Network Intrusion Detection System, Adversarial Machine Learning, Cybersecurity, Adversarial Sample Generation

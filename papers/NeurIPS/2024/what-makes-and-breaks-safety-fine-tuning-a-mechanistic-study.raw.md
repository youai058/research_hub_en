---
title: "What Makes and Breaks Safety Fine-tuning? A Mechanistic Study"
authors: ["Samyak Jain", "Ekdeep Singh Lubana", "Kemal Oksuz", "Tom Joy", "Philip Torr", "Amartya Sanyal", "Puneet K. Dokania"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "JEflV4nRlH"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/81116601d33b2f8062d8349ffea18be421ec92bf.pdf"
published: "2024"
categories: []
keywords: ["Mechanistic Interpretability", "AI Safety", "Safety fine tuning", "Large Language Models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:34+09:00"
---

# What Makes and Breaks Safety Fine-tuning? A Mechanistic Study

## Abstract
Safety fine-tuning helps align Large Language Models (LLMs) with human preferences for their safe deployment. To better understand the underlying factors that make models safe via safety fine-tuning, we design a synthetic data generation framework that captures salient aspects of an unsafe input by modeling the interaction between the task the model is asked to perform (e.g., “design”) versus the specific concepts the task is asked to be performed upon (e.g., a “cycle” vs. a “bomb”). Using this, we investigate three well-known safety fine-tuning methods—supervised safety fine-tuning, direct preference optimization, and unlearning—and provide significant evidence demonstrating that these methods minimally transform MLP weights to specifically align unsafe inputs into its weights’ null space. This yields a clustering of inputs based on whether the model deems them safe or not. Correspondingly, when an adversarial input (e.g., a jailbreak) is provided, its activations are closer to safer samples, leading to the model processing such an input as if it were safe. Code is available at https://github.com/fiveai/understanding_safety_finetuning.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Samyak Jain, Ekdeep Singh Lubana, Kemal Oksuz, Tom Joy, Philip Torr, Amartya Sanyal, Puneet K. Dokania
- arxiv_id: 
- openreview_id: JEflV4nRlH
- anthology_id: 
- pdf_url: https://openreview.net/pdf/81116601d33b2f8062d8349ffea18be421ec92bf.pdf
- published: 2024
- keywords: Mechanistic Interpretability, AI Safety, Safety fine tuning, Large Language Models

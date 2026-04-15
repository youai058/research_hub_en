---
title: "AutoMix: Automatically Mixing Language Models"
authors: ["Pranjal Aggarwal", "Aman Madaan", "Ankit Anand", "Srividya Pranavi Potharaju", "Swaroop Mishra", "Pei Zhou", "Aditya Gupta", "Dheeraj Rajagopal", "Karthik Kappaganthu", "Yiming Yang", "Shyam Upadhyay", "Manaal Faruqui", "Mausam ."]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "e6WrwIvgzX"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f99d5e58580a4ddb7a4d60eef66db492cfafb4d9.pdf"
published: "2024"
categories: []
keywords: ["Few-shot learning", "Zero-shot learning", "Self-Verification", "cost-quality optimization", "Decision making", "Prompting", "LLMs"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:59+09:00"
---

# AutoMix: Automatically Mixing Language Models

## Abstract
Large language models (LLMs) are now available from cloud API providers in various sizes and configurations. While this diversity offers a broad spectrum of choices, effectively leveraging the options to optimize computational cost and performance remains challenging. In this work, we present AutoMix, an approach that strategically routes queries to larger LMs, based on the approximate correctness of outputs from a smaller LM. Central to AutoMix are two key technical contributions. First, it has a few-shot self-verification mechanism, which estimates the reliability of its own outputs without requiring extensive training. Second, given that self-verification can be noisy, it employs a POMDP based router that can effectively select an appropriately sized model, based on answer confidence. Experiments across five language models and five challenging datasets show that Automix consistently surpasses strong baselines, reducing computational cost by over 50\% for comparable performance.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Pranjal Aggarwal, Aman Madaan, Ankit Anand, Srividya Pranavi Potharaju, Swaroop Mishra, Pei Zhou, Aditya Gupta, Dheeraj Rajagopal, Karthik Kappaganthu, Yiming Yang, Shyam Upadhyay, Manaal Faruqui, Mausam .
- arxiv_id: 
- openreview_id: e6WrwIvgzX
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f99d5e58580a4ddb7a4d60eef66db492cfafb4d9.pdf
- published: 2024
- keywords: Few-shot learning, Zero-shot learning, Self-Verification, cost-quality optimization, Decision making, Prompting, LLMs

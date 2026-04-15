---
title: "Self-contradictory Hallucinations of Large Language Models: Evaluation, Detection and Mitigation"
authors: ["Niels Mündler", "Jingxuan He", "Slobodan Jenko", "Martin Vechev"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "EmQSOi1X2f"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9087c7d18bb7707f5f8b47046499f922b5c47af3.pdf"
published: "2024"
categories: []
keywords: ["language model", "hallucination", "trustworthy artificial intelligence", "reasoning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:55+09:00"
---

# Self-contradictory Hallucinations of Large Language Models: Evaluation, Detection and Mitigation

## Abstract
Large language models (large LMs) are susceptible to producing text that contains hallucinated content. An important instance of this problem is self-contradiction, where the LM generates two contradictory sentences within the same context. In this work, we present a comprehensive investigation into self-contradiction for various instruction-tuned LMs, covering evaluation, detection, and mitigation. Our primary evaluation task is open-domain text generation, but we also demonstrate the applicability of our approach to shorter question answering. Our analysis reveals the prevalence of self-contradictions, e.g., in 17.7% of all sentences produced by ChatGPT. We then propose a novel prompting-based framework designed to effectively detect and mitigate self-contradictions. Our detector achieves high accuracy, e.g., around 80% F1 score when prompting ChatGPT. The mitigation algorithm iteratively refines the generated text to remove contradictory information while preserving text fluency and informativeness. Importantly, our entire framework is applicable to black-box LMs and does not require retrieval of external knowledge. Rather, our method complements retrieval-based methods, as a large portion of self-contradictions (e.g., 35.2% for ChatGPT) cannot be verified using online text. Our approach is practically effective and has been released as a push-button tool to benefit the public at https://chatprotect.ai/.

## Metadata
- venue: ICLR
- year: 2024
- authors: Niels Mündler, Jingxuan He, Slobodan Jenko, Martin Vechev
- arxiv_id: 
- openreview_id: EmQSOi1X2f
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9087c7d18bb7707f5f8b47046499f922b5c47af3.pdf
- published: 2024
- keywords: language model, hallucination, trustworthy artificial intelligence, reasoning

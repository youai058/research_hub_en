---
title: "Model merging with SVD to tie the Knots"
authors: ["George Stoica", "Pratik Ramesh", "Boglarka Ecsedi", "Leshem Choshen", "Judy Hoffman"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "67X93aZHII"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2ebbc779ddc6d4858a34bb3b25a80d2829c1bb9f.pdf"
published: "2025"
categories: []
keywords: ["model merging; lora PEFT; computer vision;"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:01+09:00"
---

# Model merging with SVD to tie the Knots

## Abstract
Recent model merging methods demonstrate that the parameters of fully-finetuned models specializing in distinct tasks can be combined into one model capable of solving all tasks without retraining. Yet, this success does not transfer well when merging LoRA finetuned models. We study this phenomenon and observe that the weights of LoRA finetuned models showcase a lower degree of alignment compared to their fully-finetuned counterparts. We hypothesize that improving this alignment is key to obtaining better LoRA model merges, and propose KnOTS to address this problem. KnOTS uses the SVD to jointly transform the weights of different LoRA models into an aligned space, where existing merging methods can be applied. In addition, we introduce a new benchmark that explicitly evaluates whether merged models are general models. Notably, KnOTS consistently improves LoRA merging by up to 4.3% across several vision and language benchmarks, including our new setting. We release our code at: https://github.com/gstoica27/KnOTS.

## Metadata
- venue: ICLR
- year: 2025
- authors: George Stoica, Pratik Ramesh, Boglarka Ecsedi, Leshem Choshen, Judy Hoffman
- arxiv_id: 
- openreview_id: 67X93aZHII
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2ebbc779ddc6d4858a34bb3b25a80d2829c1bb9f.pdf
- published: 2025
- keywords: model merging; lora PEFT; computer vision;

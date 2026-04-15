---
title: "Kosmos-G: Generating Images in Context with Multimodal Large Language Models"
authors: ["Xichen Pan", "Li Dong", "Shaohan Huang", "Zhiliang Peng", "Wenhu Chen", "Furu Wei"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "he6mX9LTyE"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/8ffe0cc3c3fb4e1f945894b836d9a97b0dbaf9b5.pdf"
published: "2024"
categories: []
keywords: ["Diffusion Models", "Vision-Language", "Multimodal Large Language Model", "Image Generation", "Subject-Driven Generation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:01+09:00"
---

# Kosmos-G: Generating Images in Context with Multimodal Large Language Models

## Abstract
Recent advancements in subject-driven image generation have made significant strides. However, current methods still fall short in diverse application scenarios, as they require test-time tuning and cannot accept interleaved multi-image and text input. These limitations keep them far from the ultimate goal of "image as a foreign language in image generation." This paper presents Kosmos-G, a model that leverages the advanced multimodal perception capabilities of Multimodal Large Language Models (MLLMs) to tackle the aforementioned challenge. Our approach aligns the output space of MLLM with CLIP using the textual modality as an anchor and performs compositional instruction tuning on curated data. Kosmos-G demonstrates an impressive capability of zero-shot subject-driven generation with interleaved multi-image and text input. Notably, the score distillation instruction tuning requires no modifications to the image decoder. This allows for a seamless substitution of CLIP and effortless integration with a myriad of U-Net techniques ranging from fine-grained controls to personalized image decoder variants. We posit Kosmos-G as an initial attempt towards the goal of "image as a foreign language in image generation."

## Metadata
- venue: ICLR
- year: 2024
- authors: Xichen Pan, Li Dong, Shaohan Huang, Zhiliang Peng, Wenhu Chen, Furu Wei
- arxiv_id: 
- openreview_id: he6mX9LTyE
- anthology_id: 
- pdf_url: https://openreview.net/pdf/8ffe0cc3c3fb4e1f945894b836d9a97b0dbaf9b5.pdf
- published: 2024
- keywords: Diffusion Models, Vision-Language, Multimodal Large Language Model, Image Generation, Subject-Driven Generation

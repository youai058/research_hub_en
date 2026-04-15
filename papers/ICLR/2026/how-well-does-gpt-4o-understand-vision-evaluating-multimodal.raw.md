---
title: "How Well Does GPT-4o Understand Vision? Evaluating Multimodal Foundation Models on Standard Computer Vision Tasks"
authors: ["Rahul Ramachandran", "Ali Garjani", "Roman Bachmann", "Andrei Atanov", "Oğuzhan Fatih Kar", "Amir Zamir"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Oq3yRhFp0t"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/86bb432ddb3e7540dbec62b37ec09ec5c64d42aa.pdf"
published: "2026"
categories: []
keywords: ["vision benchmark", "multimodal foundation models", "vision language models", "standard computer vision tasks"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:14+09:00"
---

# How Well Does GPT-4o Understand Vision? Evaluating Multimodal Foundation Models on Standard Computer Vision Tasks

## Abstract
Multimodal foundation models, such as GPT-4o, have recently made remarkable progress, but it is not clear where exactly these models stand in terms of understanding vision. In this paper, we benchmark the performance of popular multimodal foundation models (GPT-4o, o4-mini, Gemini 1.5 Pro and Gemini 2.0 Flash, Claude 3.5 Sonnet, Qwen2-VL, Llama 3.2) on standard computer vision tasks (semantic segmentation, object detection, image classification, depth and surface normal prediction) and using established datasets (e.g., COCO, ImageNet and its variants, etc).

The main challenges to performing this are: 1) most models are trained to output text and cannot natively express versatile domains, such as segments or 3D geometry, and 2) many leading models are proprietary and accessible only at an API level, i.e., there is no weight access to adapt them. We address these challenges by translating standard vision tasks into equivalent text-promptable and API-compatible tasks via prompt chaining to create a standardized benchmarking framework.

We observe that 1) the models are not close to the state-of-the-art specialist models at any tasks, and 2) they perform semantic tasks notably better than geometric ones. However, 3) they are respectable generalists; this is remarkable as they are presumably trained on primarily image-text-based tasks. 4) While the prompt-chaining techniques affect performance, better models exhibit less sensitivity to prompt variations. 5) GPT-4o performs the best among non-reasoning models, securing the top position in 4 out of 6 tasks and 6) reasoning models, e.g. o3, show improvements in geometric tasks.

## Metadata
- venue: ICLR
- year: 2026
- authors: Rahul Ramachandran, Ali Garjani, Roman Bachmann, Andrei Atanov, Oğuzhan Fatih Kar, Amir Zamir
- arxiv_id: 
- openreview_id: Oq3yRhFp0t
- anthology_id: 
- pdf_url: https://openreview.net/pdf/86bb432ddb3e7540dbec62b37ec09ec5c64d42aa.pdf
- published: 2026
- keywords: vision benchmark, multimodal foundation models, vision language models, standard computer vision tasks

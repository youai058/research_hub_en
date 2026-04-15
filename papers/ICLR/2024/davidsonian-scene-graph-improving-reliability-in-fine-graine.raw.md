---
title: "Davidsonian Scene Graph: Improving Reliability in Fine-grained Evaluation for Text-to-Image Generation"
authors: ["Jaemin Cho", "Yushi Hu", "Jason Michael Baldridge", "Roopal Garg", "Peter Anderson", "Ranjay Krishna", "Mohit Bansal", "Jordi Pont-Tuset", "Su Wang"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ITq4ZRUT4a"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/713250bdf458c9b54444d2bf78bfd594a06adead.pdf"
published: "2024"
categories: []
keywords: ["text-to-image generation", "text-to-image evaluation", "Davidsonian semantics", "large language models", "scene graphs", "visual question answering", "question generation", "benchmark"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:11+09:00"
---

# Davidsonian Scene Graph: Improving Reliability in Fine-grained Evaluation for Text-to-Image Generation

## Abstract
Evaluating text-to-image models is notoriously difficult. A strong recent approach for assessing text-image faithfulness is based on QG/A (question generation and answering), which uses pre-trained foundational models to automatically generate a set of questions and answers from the prompt, and output images are scored based on whether these answers extracted with a visual question answering model are consistent with the prompt-based answers. This kind of evaluation is naturally dependent on the quality of the underlying QG and VQA models. We identify and address several reliability challenges in existing QG/A work: (a) QG questions should respect the prompt (avoiding hallucinations, duplications, and omissions) and (b) VQA answers should be consistent (not asserting that there is no motorcycle in an image while also claiming the motorcycle is blue). We address these issues with Davidsonian Scene Graph (DSG), an empirically grounded evaluation framework inspired by formal semantics, which is adaptable to any QG/A frameworks. DSG produces atomic and unique questions organized in dependency graphs, which (i) ensure appropriate semantic coverage and (ii) sidestep inconsistent answers. With extensive experimentation and human evaluation on a range of model configurations (LLM, VQA, and T2I), we empirically demonstrate that DSG addresses the challenges noted above. Finally, we present DSG-1k, an open-sourced evaluation benchmark that includes 1,060 prompts, covering a wide range of fine-grained semantic categories with a balanced distribution. We release the DSG-1k prompts and the corresponding DSG questions.

## Metadata
- venue: ICLR
- year: 2024
- authors: Jaemin Cho, Yushi Hu, Jason Michael Baldridge, Roopal Garg, Peter Anderson, Ranjay Krishna, Mohit Bansal, Jordi Pont-Tuset, Su Wang
- arxiv_id: 
- openreview_id: ITq4ZRUT4a
- anthology_id: 
- pdf_url: https://openreview.net/pdf/713250bdf458c9b54444d2bf78bfd594a06adead.pdf
- published: 2024
- keywords: text-to-image generation, text-to-image evaluation, Davidsonian semantics, large language models, scene graphs, visual question answering, question generation, benchmark

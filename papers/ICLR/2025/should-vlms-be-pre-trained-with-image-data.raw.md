---
title: "Should VLMs be Pre-trained with Image Data?"
authors: ["Sedrick Keh", "Jean Mercat", "Samir Yitzhak Gadre", "Kushal Arora", "Igor Vasiljevic", "Benjamin Burchfiel", "Shuran Song", "Russ Tedrake", "Thomas Kollar", "Ludwig Schmidt", "Achal Dave"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Pj4Aid3XqL"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ec02fe2f9842f3eaab66103c80443fd305e469f9.pdf"
published: "2025"
categories: []
keywords: ["vision language models", "pre-training", "fine-tuning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:11+09:00"
---

# Should VLMs be Pre-trained with Image Data?

## Abstract
Pre-trained LLMs that are further trained with image data perform well on vision-language tasks. 
While adding images during a second training phase effectively unlocks this capability, it is unclear how much of a gain or loss this two-step pipeline gives over VLMs which integrate images earlier into the training process. 
To investigate this, we train models spanning various datasets, scales, image-text ratios, and amount of pre-training done before introducing vision tokens.
We then fine-tune these models and evaluate their downstream performance on a suite of vision-language and text-only tasks.
We find that pre-training with a mixture of image and text data allows models to perform better on vision-language tasks while maintaining strong performance on text-only evaluations.
On an average of 6 diverse tasks, we find that for a 1B model, introducing visual tokens 80\% of the way through pre-training results in a 2\% average improvement over introducing visual tokens to a fully pre-trained model.

## Metadata
- venue: ICLR
- year: 2025
- authors: Sedrick Keh, Jean Mercat, Samir Yitzhak Gadre, Kushal Arora, Igor Vasiljevic, Benjamin Burchfiel, Shuran Song, Russ Tedrake, Thomas Kollar, Ludwig Schmidt, Achal Dave
- arxiv_id: 
- openreview_id: Pj4Aid3XqL
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ec02fe2f9842f3eaab66103c80443fd305e469f9.pdf
- published: 2025
- keywords: vision language models, pre-training, fine-tuning

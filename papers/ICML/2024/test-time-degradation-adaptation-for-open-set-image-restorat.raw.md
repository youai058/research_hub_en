---
title: "Test-Time Degradation Adaptation for Open-Set Image Restoration"
authors: ["Yuanbiao Gou", "Haiyu Zhao", "Boyun Li", "Xinyan Xiao", "Xi Peng"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "XLlQb24X2o"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/cbe8a535cb6ad39d7f4315b6eaedd1bcc36a0a4d.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:35+09:00"
---

# Test-Time Degradation Adaptation for Open-Set Image Restoration

## Abstract
In contrast to close-set scenarios that restore images from a predefined set of degradations, open-set image restoration aims to handle the unknown degradations that were unforeseen during the pretraining phase, which is less-touched as far as we know. This work study this challenging problem and reveal its essence as unidentified distribution shifts between the test and training data. Recently, test-time adaptation has emerged as a fundamental method to address this inherent disparities. Inspired by it, we propose a test-time degradation adaptation framework for open-set image restoration, which consists of three components, *i.e.*, i) a pre-trained and degradation-agnostic diffusion model for generating clean images, ii) a test-time degradation adapter adapts the unknown degradations based on the input image during the testing phase, and iii) the adapter-guided image restoration guides the model through the adapter to produce the corresponding clean image. Through experiments on multiple degradations, we show that our method achieves comparable even better performance than those task-specific methods. The code is available at https://github.com/XLearning-SCU/2024-ICML-TAO.

## Metadata
- venue: ICML
- year: 2024
- authors: Yuanbiao Gou, Haiyu Zhao, Boyun Li, Xinyan Xiao, Xi Peng
- arxiv_id: 
- openreview_id: XLlQb24X2o
- anthology_id: 
- pdf_url: https://openreview.net/pdf/cbe8a535cb6ad39d7f4315b6eaedd1bcc36a0a4d.pdf
- published: 2024

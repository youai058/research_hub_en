---
title: "4M-21: An Any-to-Any Vision Model for Tens of Tasks and Modalities"
authors: ["Roman Bachmann", "Oğuzhan Fatih Kar", "David Mizrahi", "Ali Garjani", "Mingfei Gao", "David Griffiths", "Jiaming Hu", "Afshin Dehghan", "Amir Zamir"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "qRnmLJQHgx"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/727e1b1b115255a1630016a67956056a2b237be2.pdf"
published: "2024"
categories: []
keywords: ["multimodal learning", "multitask learning", "representation learning", "transfer learning", "foundation models", "generative models", "computer vision"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:59+09:00"
---

# 4M-21: An Any-to-Any Vision Model for Tens of Tasks and Modalities

## Abstract
Current multimodal and multitask foundation models, like 4M or UnifiedIO, show promising results. However, their out-of-the-box abilities to accept diverse inputs and perform diverse tasks are limited by the (usually small) number of modalities and tasks they are trained on. In this paper, we develop a single any-to-any model trained on tens of highly diverse modalities and by performing co-training on large-scale multimodal datasets and text corpora. This includes training on images and text along with several semantic and geometric modalities, feature maps from recent state of the art models like DINOv2 and ImageBind, pseudo labels of specialist models like SAM and 4DHumans, and a range of new modalities that allow for novel ways to interact with the model and steer the generation, for example, image metadata or color palettes.

A crucial step in this process is performing discrete tokenization on various modalities, whether they are image-like, neural network feature maps, vectors, structured data like instance segmentation or human poses, or data that can be represented as text.
    
Through this, we show the possibility of training one model to solve at least 3x more tasks/modalities than existing models and doing so without a loss in performance. In addition, this enables more fine-grained and controllable multimodal generation capabilities and allows studying the distillation of models trained on diverse data and objectives into one unified model.
We scale the training to a three billion parameter and different datasets. The multimodal models and training code are open sourced at https://4m.epfl.ch/.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Roman Bachmann, Oğuzhan Fatih Kar, David Mizrahi, Ali Garjani, Mingfei Gao, David Griffiths, Jiaming Hu, Afshin Dehghan, Amir Zamir
- arxiv_id: 
- openreview_id: qRnmLJQHgx
- anthology_id: 
- pdf_url: https://openreview.net/pdf/727e1b1b115255a1630016a67956056a2b237be2.pdf
- published: 2024
- keywords: multimodal learning, multitask learning, representation learning, transfer learning, foundation models, generative models, computer vision

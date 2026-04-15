---
title: "HyperFace: Generating Synthetic Face Recognition Datasets by Exploring Face Embedding Hypersphere"
authors: ["Hatef Otroshi Shahreza", "Sébastien Marcel"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "4YzVF9isgD"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2d7784b7b85159b61527b71a37708ef7ebfd2127.pdf"
published: "2025"
categories: []
keywords: ["Face Recognition", "Hypersphere Optimization", "Privacy", "Synthetic Data"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:49+09:00"
---

# HyperFace: Generating Synthetic Face Recognition Datasets by Exploring Face Embedding Hypersphere

## Abstract
Face recognition datasets are often collected by crawling Internet and without individuals' consents, raising  ethical and privacy concerns. Generating synthetic datasets for training face recognition models has emerged as a promising alternative. However, the generation of synthetic datasets remains  challenging as it entails adequate inter-class and intra-class variations. While advances in generative models have made it easier to increase intra-class variations in face datasets (such as pose, illumination, etc.), generating sufficient inter-class variation is still a difficult task. In this paper, we formulate the dataset generation as a packing problem on the embedding space (represented on a hypersphere) of a face recognition model and propose a new synthetic dataset generation approach, called HyperFace. We formalize our packing problem as an optimization problem and solve it with a gradient descent-based approach. Then, we use a conditional face generator model to synthesize face images from the optimized embeddings. We use our generated datasets to train face recognition models and evaluate the trained models on several benchmarking real datasets. Our experimental results show that models trained with HyperFace achieve state-of-the-art performance in training face recognition using synthetic datasets. Project page: https://www.idiap.ch/paper/hyperface

## Metadata
- venue: ICLR
- year: 2025
- authors: Hatef Otroshi Shahreza, Sébastien Marcel
- arxiv_id: 
- openreview_id: 4YzVF9isgD
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2d7784b7b85159b61527b71a37708ef7ebfd2127.pdf
- published: 2025
- keywords: Face Recognition, Hypersphere Optimization, Privacy, Synthetic Data

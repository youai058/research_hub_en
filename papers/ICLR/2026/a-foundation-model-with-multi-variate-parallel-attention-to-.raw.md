---
title: "A foundation model with multi-variate parallel attention to generate neuronal activity"
authors: ["Francesco S. Carzaniga", "Michael Hersche", "Abu Sebastian", "Kaspar Schindler", "Abbas Rahimi"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "5M1YOW3bRq"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/729b73af1971819b50f0db8e964c075bb8613c35.pdf"
published: "2026"
categories: []
keywords: ["time-series", "ieeg", "neurology", "foundation model", "attention", "transformer"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:40+09:00"
---

# A foundation model with multi-variate parallel attention to generate neuronal activity

## Abstract
Learning from multi-variate time-series with heterogeneous channel configurations remains a fundamental challenge for deep neural networks, particularly in clinical domains such as intracranial electroencephalography (iEEG), where channel setups vary widely across subjects. In this work, we introduce multi-variate parallel attention (MVPA), a novel self-attention mechanism that disentangles content, temporal, and spatial attention, enabling flexible, generalizable, and efficient modeling of time-series data with varying channel counts and configurations. We use MVPA to build MVPFormer, a generative foundation model for human electrophysiology, trained to predict the evolution of iEEG signals across diverse subjects. To support this and future efforts by the community, we release the SWEC iEEG dataset, the largest publicly available iEEG dataset to date, comprising nearly 10,000 hours of recordings from heterogeneous clinical sources. MVPFormer leverages MVPA to achieve strong generalization across subjects, demonstrating expert-level performance in several iEEG tasks. MVPFormer surpasses state-of-the-art (SOTA) Transformer baselines in seizure detection across the SWEC, the MAYO, and the FNUSA datasets, while also achieving SOTA performance on four Brain TreeBank iEEG decoding tasks (volume, pitch, onset, and speech). We further validate MVPA on standard time-series forecasting and classification tasks, where it matches or exceeds the performance of existing attention-based models. Together, our contributions establish MVPA as a general-purpose attention mechanism for heterogeneous time-series and MVPFormer as the first open-source, open-weights, and open-data iEEG foundation model with SOTA clinical performance. The code and weights are available at https://github.com/IBM/multi-variate-parallel-transformer. The SWEC iEEG dataset is available at https://huggingface.co/datasets/NeuroTec/SWEC_iEEG_Dataset.

## Metadata
- venue: ICLR
- year: 2026
- authors: Francesco S. Carzaniga, Michael Hersche, Abu Sebastian, Kaspar Schindler, Abbas Rahimi
- arxiv_id: 
- openreview_id: 5M1YOW3bRq
- anthology_id: 
- pdf_url: https://openreview.net/pdf/729b73af1971819b50f0db8e964c075bb8613c35.pdf
- published: 2026
- keywords: time-series, ieeg, neurology, foundation model, attention, transformer

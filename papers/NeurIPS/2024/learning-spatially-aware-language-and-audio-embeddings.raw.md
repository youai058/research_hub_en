---
title: "Learning Spatially-Aware Language and Audio Embeddings"
authors: ["Bhavika Suresh Devnani", "Skyler Seto", "Zakaria Aldeneh", "Alessandro Toso", "YELENA MENYAYLENKO", "Barry-John Theobald", "Jonathan Sheaffer", "Miguel Sarabia"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "wDDvJzvvBR"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a2ecfb85ce32cb9d1d5454e92a10f65a79ed4f7d.pdf"
published: "2024"
categories: []
keywords: ["multimodal embeddings", "spatial audio", "contrastive learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:54+09:00"
---

# Learning Spatially-Aware Language and Audio Embeddings

## Abstract
Humans can picture a sound scene given an imprecise natural language description. For example, it is easy to imagine an acoustic environment given a phrase like "the lion roar came from right behind me!". For a machine to have the same degree of comprehension,  the machine must know what a lion is (semantic attribute), what the concept of "behind" is (spatial attribute) and how these pieces of linguistic information align with the semantic and spatial attributes of the sound (what a roar sounds like when its coming from behind). 
State-of-the-art audio foundation models, such as CLAP, which learn to map between audio scenes and natural textual descriptions, are trained on non-spatial audio and text pairs, and hence lack spatial awareness. In contrast, sound event localization and detection models are limited to recognizing sounds from a fixed number of classes, and they localize the source to absolute position (e.g., 0.2m) rather than a position described using natural language (e.g., "next to me"). To address these gaps, we present ELSA (Embeddings for Language and Spatial Audio), a spatially aware-audio and text embedding model trained using multimodal contrastive learning. ELSA supports non-spatial audio, spatial audio, and open vocabulary text captions describing both the spatial and semantic components of sound. To train ELSA: (a) we spatially augment  the audio and captions of three open-source audio datasets totaling 4,738 hours and 890,038 samples of audio comprised from 8,972 simulated spatial configurations, and (b) we design an encoder to capture the semantics of non-spatial audio, and the semantics and spatial attributes of spatial audio using contrastive learning. ELSA is a single model that is competitive with state-of-the-art for both semantic retrieval and 3D source localization.  In particular, ELSA achieves +2.8\% mean audio-to-text and text-to-audio R@1 above the LAION-CLAP baseline, and outperforms by -11.6° mean-absolute-error in 3D source localization over the SeldNET baseline on the TUT Sound Events 2018 benchmark. Moreover, we show that the representation-space of ELSA is structured, enabling swapping of direction of audio via vector arithmetic of two directional text embeddings.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Bhavika Suresh Devnani, Skyler Seto, Zakaria Aldeneh, Alessandro Toso, YELENA MENYAYLENKO, Barry-John Theobald, Jonathan Sheaffer, Miguel Sarabia
- arxiv_id: 
- openreview_id: wDDvJzvvBR
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a2ecfb85ce32cb9d1d5454e92a10f65a79ed4f7d.pdf
- published: 2024
- keywords: multimodal embeddings, spatial audio, contrastive learning

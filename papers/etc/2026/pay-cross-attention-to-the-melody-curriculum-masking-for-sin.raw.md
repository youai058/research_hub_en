---
title: "Pay (Cross) Attention to the Melody: Curriculum Masking for Single-Encoder Melodic Harmonization"
authors: ["Maximos Kaliakatsos-Papakostas", "Dimos Makris", "Konstantinos Soiledis", "Konstantinos-Theodoros Tsamis", "Vassilis Katsouros", "Emilios Cambouropoulos"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2601.16150"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2601.16150v1"
published: "2026-01-22"
categories: ["cs.SD", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:36+09:00"
---

# Pay (Cross) Attention to the Melody: Curriculum Masking for Single-Encoder Melodic Harmonization

## Abstract
Melodic harmonization, the task of generating harmonic accompaniments for a given melody, remains a central challenge in computational music generation. Recent single encoder transformer approaches have framed harmonization as a masked sequence modeling problem, but existing training curricula inspired by discrete diffusion often result in weak (cross) attention between melody and harmony. This leads to limited exploitation of melodic cues, particularly in out-of-domain contexts. In this work, we introduce a training curriculum, FF (full-to-full), which keeps all harmony tokens masked for several training steps before progressively unmasking entire sequences during training to strengthen melody-harmony interactions. We systematically evaluate this approach against prior curricula across multiple experimental axes, including temporal quantization (quarter vs. sixteenth note), bar-level vs. time-signature conditioning, melody representation (full range vs. pitch class), and inference-time unmasking strategies. Models are trained on the HookTheory dataset and evaluated both in-domain and on a curated collection of jazz standards, using a comprehensive set of metrics that assess chord progression structure, harmony-melody alignment, and rhythmic coherence. Results demonstrate that the proposed FF curriculum consistently outperforms baselines in nearly all metrics, with particularly strong gains in out-of-domain evaluations where harmonic adaptability to novel melodic queues is crucial. We further find that quarter-note quantization, intertwining of bar tokens, and pitch-class melody representations are advantageous in the FF setting. Our findings highlight the importance of training curricula in enabling effective melody conditioning and suggest that full-to-full unmasking offers a robust strategy for single encoder harmonization.

## Metadata
- venue: arXiv
- year: 2026
- authors: Maximos Kaliakatsos-Papakostas, Dimos Makris, Konstantinos Soiledis, Konstantinos-Theodoros Tsamis, Vassilis Katsouros, Emilios Cambouropoulos
- arxiv_id: 2601.16150
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2601.16150v1
- published: 2026-01-22

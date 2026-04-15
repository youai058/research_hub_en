---
title: "MotionTTT: 2D Test-Time-Training Motion Estimation for 3D Motion Corrected MRI"
authors: ["Tobit Klug", "Kun Wang", "Stefan Ruschke", "Reinhard Heckel"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "aUHSwmHRVb"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f5a7386557b925b38510cffd237c30490992faa8.pdf"
published: "2024"
categories: []
keywords: ["deep learning based motion estimation", "3D imaging", "MRI", "motion artifacts", "medical imaging", "test-time-training", "motion correction"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:02+09:00"
---

# MotionTTT: 2D Test-Time-Training Motion Estimation for 3D Motion Corrected MRI

## Abstract
A major challenge of the long measurement times in magnetic resonance imaging (MRI), an important medical imaging technology, is that patients may move during data acquisition. This leads to severe motion artifacts in the reconstructed images and volumes. In this paper, we propose MotionTTT a deep learning-based test-time-training (TTT) method for accurate motion estimation. The key idea is that a neural network trained for motion-free reconstruction has a small loss if there is no motion, thus optimizing over motion parameters passed through the reconstruction network enables accurate estimation of motion. The estimated motion parameters enable to correct for the motion and to reconstruct accurate motion-corrected images. Our method uses 2D reconstruction networks to estimate rigid motion in 3D, and constitutes the first deep learning based method for 3D rigid motion estimation towards 3D-motion-corrected MRI. We show that our method can provably reconstruct motion parameters for a simple signal and neural network model. We demonstrate the effectiveness of our method for both retrospectively simulated motion and prospectively collected real motion-corrupted data. Code is available at \url{https://github.com/MLI-lab/MRI_MotionTTT}.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Tobit Klug, Kun Wang, Stefan Ruschke, Reinhard Heckel
- arxiv_id: 
- openreview_id: aUHSwmHRVb
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f5a7386557b925b38510cffd237c30490992faa8.pdf
- published: 2024
- keywords: deep learning based motion estimation, 3D imaging, MRI, motion artifacts, medical imaging, test-time-training, motion correction

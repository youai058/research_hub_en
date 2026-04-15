---
title: "Distilling Dataset into Neural Field"
authors: ["Donghyeok Shin", "HeeSun Bae", "Gyuwon Sim", "Wanmo Kang", "Il-chul Moon"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "nCrJD7qPJN"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6e92b5dd21f95a8dcae9d1d51a427c09da5b2e4b.pdf"
published: "2025"
categories: []
keywords: ["Dataset distillation", "Dataset condensation", "Neural field"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:55+09:00"
---

# Distilling Dataset into Neural Field

## Abstract
Utilizing a large-scale dataset is essential for training high-performance deep learning models, but it also comes with substantial computation and storage costs. To overcome these challenges, dataset distillation has emerged as a promising solution by compressing the large-scale dataset into a smaller synthetic dataset that retains the essential information needed for training. This paper proposes a novel parameterization framework for dataset distillation, coined Distilling Dataset into Neural Field (DDiF), which leverages the neural field to store the necessary information of the large-scale dataset. Due to the unique nature of the neural field, which takes coordinates as input and output quantity, DDiF effectively preserves the information and easily generates various shapes of data. We theoretically confirm that DDiF exhibits greater expressiveness than some previous literature when the utilized budget for a single synthetic instance is the same. Through extensive experiments, we demonstrate that DDiF achieves superior performance on several benchmark datasets, extending beyond the image domain to include video, audio, and 3D voxel. We release the code at \url{https://github.com/aailab-kaist/DDiF}.

## Metadata
- venue: ICLR
- year: 2025
- authors: Donghyeok Shin, HeeSun Bae, Gyuwon Sim, Wanmo Kang, Il-chul Moon
- arxiv_id: 
- openreview_id: nCrJD7qPJN
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6e92b5dd21f95a8dcae9d1d51a427c09da5b2e4b.pdf
- published: 2025
- keywords: Dataset distillation, Dataset condensation, Neural field

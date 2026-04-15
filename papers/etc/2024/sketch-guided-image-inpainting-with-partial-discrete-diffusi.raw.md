---
title: "Sketch-guided Image Inpainting with Partial Discrete Diffusion Process"
authors: ["Nakul Sharma", "Aditay Tripathi", "Anirban Chakraborty", "Anand Mishra"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2404.11949"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2404.11949v1"
published: "2024-04-18"
categories: ["cs.CV", "cs.AI", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:17+09:00"
---

# Sketch-guided Image Inpainting with Partial Discrete Diffusion Process

## Abstract
In this work, we study the task of sketch-guided image inpainting. Unlike the well-explored natural language-guided image inpainting, which excels in capturing semantic details, the relatively less-studied sketch-guided inpainting offers greater user control in specifying the object's shape and pose to be inpainted. As one of the early solutions to this task, we introduce a novel partial discrete diffusion process (PDDP). The forward pass of the PDDP corrupts the masked regions of the image and the backward pass reconstructs these masked regions conditioned on hand-drawn sketches using our proposed sketch-guided bi-directional transformer. The proposed novel transformer module accepts two inputs -- the image containing the masked region to be inpainted and the query sketch to model the reverse diffusion process. This strategy effectively addresses the domain gap between sketches and natural images, thereby, enhancing the quality of inpainting results. In the absence of a large-scale dataset specific to this task, we synthesize a dataset from the MS-COCO to train and extensively evaluate our proposed framework against various competent approaches in the literature. The qualitative and quantitative results and user studies establish that the proposed method inpaints realistic objects that fit the context in terms of the visual appearance of the provided sketch. To aid further research, we have made our code publicly available at https://github.com/vl2g/Sketch-Inpainting .

## Metadata
- venue: arXiv
- year: 2024
- authors: Nakul Sharma, Aditay Tripathi, Anirban Chakraborty, Anand Mishra
- arxiv_id: 2404.11949
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2404.11949v1
- published: 2024-04-18

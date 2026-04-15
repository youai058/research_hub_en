---
title: "HyperDiffusionFields (HyDiF): Diffusion-Guided Hypernetworks for Learning Implicit Molecular Neural Fields"
authors: ["Sudarshan Babu", "Phillip Lo", "Xiao Zhang", "Aadi Srivastava", "Ali Davariashtiyani", "Jason Perera", "Michael Maire", "Aly A. Khan"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.18122"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.18122v1"
published: "2025-10-20"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:22+09:00"
---

# HyperDiffusionFields (HyDiF): Diffusion-Guided Hypernetworks for Learning Implicit Molecular Neural Fields

## Abstract
We introduce HyperDiffusionFields (HyDiF), a framework that models 3D molecular conformers as continuous fields rather than discrete atomic coordinates or graphs. At the core of our approach is the Molecular Directional Field (MDF), a vector field that maps any point in space to the direction of the nearest atom of a particular type. We represent MDFs using molecule-specific neural implicit fields, which we call Molecular Neural Fields (MNFs). To enable learning across molecules and facilitate generalization, we adopt an approach where a shared hypernetwork, conditioned on a molecule, generates the weights of the given molecule's MNF. To endow the model with generative capabilities, we train the hypernetwork as a denoising diffusion model, enabling sampling in the function space of molecular fields. Our design naturally extends to a masked diffusion mechanism to support structure-conditioned generation tasks, such as molecular inpainting, by selectively noising regions of the field. Beyond generation, the localized and continuous nature of MDFs enables spatially fine-grained feature extraction for molecular property prediction, something not easily achievable with graph or point cloud based methods. Furthermore, we demonstrate that our approach scales to larger biomolecules, illustrating a promising direction for field-based molecular modeling.

## Metadata
- venue: arXiv
- year: 2025
- authors: Sudarshan Babu, Phillip Lo, Xiao Zhang, Aadi Srivastava, Ali Davariashtiyani, Jason Perera, Michael Maire, Aly A. Khan
- arxiv_id: 2510.18122
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.18122v1
- published: 2025-10-20

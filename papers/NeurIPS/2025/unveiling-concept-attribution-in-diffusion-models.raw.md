---
title: "Unveiling Concept Attribution in Diffusion Models"
authors: ["Quang H Nguyen", "Hoang Phan", "Khoa D Doan"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "dVIx32Lq7J"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a45ba64f442d7aebc3a6cd8a365b5b75d2cbd1db.pdf"
published: "2025"
categories: []
keywords: ["generative models", "diffusion models", "interpretability", "concept erasure"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:27+09:00"
---

# Unveiling Concept Attribution in Diffusion Models

## Abstract
Diffusion models have shown remarkable abilities in generating realistic and high-quality images from text prompts. However, a trained model remains largely black-box; little do we know about the roles of its components in exhibiting a concept such as objects or styles. Recent works employ causal tracing to localize knowledge-storing layers in generative models without showing how other layers contribute to the target concept. In this work, we approach diffusion models' interpretability problem from a more general perspective and pose a question: \textit{``How do model components work jointly to demonstrate knowledge?''}. To answer this question, we decompose diffusion models using component attribution, systematically unveiling the importance of each component (specifically the model parameter) in generating a concept. The proposed framework, called \textbf{C}omponent \textbf{A}ttribution for \textbf{D}iffusion Model (CAD), discovers the localization of concept-inducing (positive) components, while interestingly uncovers another type of components that contribute negatively to generating a concept, which is missing in the previous knowledge localization work. Based on this holistic understanding of diffusion models, we present and empirically evaluate one utility of component attribution in controlling the generation process. Specifically, we introduce two fast, inference-time model editing algorithms, CAD-Erase and CAD-Amplify; in particular, CAD-Erase enables erasure and CAD-Amplify allows amplification of a generated concept by ablating the positive and negative components, respectively, while retaining knowledge of other concepts. Extensive experimental results validate the significance of both positive and negative components pinpointed by our framework, demonstrating the potential of providing a complete view of interpreting generative models.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Quang H Nguyen, Hoang Phan, Khoa D Doan
- arxiv_id: 
- openreview_id: dVIx32Lq7J
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a45ba64f442d7aebc3a6cd8a365b5b75d2cbd1db.pdf
- published: 2025
- keywords: generative models, diffusion models, interpretability, concept erasure

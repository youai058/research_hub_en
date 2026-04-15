---
title: "Vector Grimoire: Codebook-based Shape Generation under Raster Image Supervision"
authors: ["Marco Cipriano", "Moritz Feuerpfeil", "Gerard de Melo"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "xYtLsWiUli"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/77541e6d5ee0112c8c6ff0221aa257c5b86382ff.pdf"
published: "2025"
categories: []
keywords: ["Image Generation", "Scalable Vector Graphics", "VQ-VAE", "Differentiable Rasterizer"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:15+09:00"
---

# Vector Grimoire: Codebook-based Shape Generation under Raster Image Supervision

## Abstract
Scalable Vector Graphics (SVG) is a popular format on the web and in the design industry. However, despite the great strides made in generative modeling, SVG has remained underexplored due to the discrete and complex nature of such data. We introduce GRIMOIRE, a text-guided SVG generative model that is comprised of two modules: A Visual Shape Quantizer (VSQ) learns to map raster images onto a discrete codebook by reconstructing them as vector shapes, and an Auto-Regressive Transformer (ART) models the joint probability distribution over shape tokens, positions and textual descriptions, allowing us to generate vector graphics from natural language. Unlike existing models that require direct supervision from SVG data, GRIMOIRE learns shape image patches using only raster image supervision which opens up vector generative modeling to significantly more data. We demonstrate the effectiveness of our method by fitting GRIMOIRE for closed filled shapes on the MNIST and Emoji, and for outline strokes on icon and font data, surpassing previous image-supervised methods in generative quality and vector-supervised approach in flexibility.

## Metadata
- venue: ICML
- year: 2025
- authors: Marco Cipriano, Moritz Feuerpfeil, Gerard de Melo
- arxiv_id: 
- openreview_id: xYtLsWiUli
- anthology_id: 
- pdf_url: https://openreview.net/pdf/77541e6d5ee0112c8c6ff0221aa257c5b86382ff.pdf
- published: 2025
- keywords: Image Generation, Scalable Vector Graphics, VQ-VAE, Differentiable Rasterizer

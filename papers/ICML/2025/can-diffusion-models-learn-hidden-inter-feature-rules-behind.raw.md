---
title: "Can Diffusion Models Learn Hidden Inter-Feature Rules Behind Images?"
authors: ["Yujin Han", "Andi Han", "Wei Huang", "Chaochao Lu", "Difan Zou"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ERU7QgD6gc"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/069dfc1e42a40b21762178bb3698973e69b8fdd9.pdf"
published: "2025"
categories: []
keywords: ["Diffusion Model", "Deep Generative Model"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:36+09:00"
---

# Can Diffusion Models Learn Hidden Inter-Feature Rules Behind Images?

## Abstract
Despite the remarkable success of diffusion models (DMs) in data generation, they exhibit specific failure cases with unsatisfactory outputs. We focus on one such limitation: the ability of DMs to learn hidden rules between image features. Specifically, for image data with dependent features ($\mathbf{x}$) and ($\mathbf{y}$) (e.g., the height of the sun ($\mathbf{x}$) and the length of the shadow ($\mathbf{y}$)), we investigate whether DMs can accurately capture the inter-feature rule ($p(\mathbf{y}|\mathbf{x})$). Empirical evaluations on mainstream DMs (e.g., Stable Diffusion 3.5) reveal consistent failures, such as inconsistent lighting-shadow relationships and mismatched object-mirror reflections. Inspired by these findings, we design four synthetic tasks with strongly correlated features to assess DMs' rule-learning abilities. Extensive experiments show that while DMs can identify coarse-grained rules, they struggle with fine-grained ones. Our theoretical analysis demonstrates that DMs trained via denoising score matching (DSM) exhibit constant errors in learning hidden rules, as the DSM objective is not compatible with rule conformity. To mitigate this, we introduce a common technique - incorporating additional classifier guidance during sampling, which achieves (limited) improvements. Our analysis reveals that the subtle signals of fine-grained rules are challenging for the classifier to capture, providing insights for future exploration.

## Metadata
- venue: ICML
- year: 2025
- authors: Yujin Han, Andi Han, Wei Huang, Chaochao Lu, Difan Zou
- arxiv_id: 
- openreview_id: ERU7QgD6gc
- anthology_id: 
- pdf_url: https://openreview.net/pdf/069dfc1e42a40b21762178bb3698973e69b8fdd9.pdf
- published: 2025
- keywords: Diffusion Model, Deep Generative Model

---
title: "Planning with Diffusion Models for Target-Oriented Dialogue Systems"
authors: ["Hanwen Du", "Bo Peng", "Xia Ning"]
venue: "ACL"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: ""
anthology_id: "2025.acl-long.993"
pdf_url: "https://aclanthology.org/2025.acl-long.993.pdf"
published: "2025"
categories: []
keywords: []
venue_source: "anthology"
hunter_fetched: "2026-04-16T12:30:38+09:00"
---

# Planning with Diffusion Models for Target-Oriented Dialogue Systems

## Abstract
Target-Oriented Dialogue (TOD) remains a significant challenge in the LLM era, where strategic dialogue planning is crucial for directing conversations toward specific targets. However, existing dialogue planning methods generate dialogue plans in a step-by-step sequential manner, and may suffer from compounding errors and myopic actions. To address these limitations, we introduce a novel dialogue planning framework, DiffTOD, which leverages diffusion models to enable non-sequential dialogue planning. DiffTOD formulates dialogue planning as a trajectory generation problem with conditional guidance, and leverages a diffusion language model to estimate the likelihood of the dialogue trajectory. To optimize the dialogue action strategies, DiffTOD introduces three tailored guidance mechanisms for different target types, offering flexible guidance toward diverse TOD targets at test time. Extensive experiments across three diverse TOD settings show that DiffTOD can effectively perform non-myopic lookahead exploration and optimize action strategies over a long horizon through non-sequential dialogue planning, and demonstrates strong flexibility across complex and diverse dialogue scenarios. Our code and data are accessible through https://github.com/ninglab/DiffTOD.

## Metadata
- venue: ACL
- year: 2025
- authors: Hanwen Du, Bo Peng, Xia Ning
- arxiv_id: 
- openreview_id: 
- anthology_id: 2025.acl-long.993
- pdf_url: https://aclanthology.org/2025.acl-long.993.pdf
- published: 2025

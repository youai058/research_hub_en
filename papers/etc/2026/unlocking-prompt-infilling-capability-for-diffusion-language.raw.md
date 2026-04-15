---
title: "Unlocking Prompt Infilling Capability for Diffusion Language Models"
authors: ["Yoshinari Fujinuma", "Keisuke Sakaguchi"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2604.03677"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2604.03677v1"
published: "2026-04-04"
categories: ["cs.CL", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:13:54+09:00"
---

# Unlocking Prompt Infilling Capability for Diffusion Language Models

## Abstract
Masked diffusion language models (dLMs) generate text through bidirectional denoising, yet this capability remains locked for infilling prompts. This limitation is an artifact of the current supervised finetuning (SFT) convention of applying response-only masking. To unlock this capability, we extend full-sequence masking during SFT, where both prompts and responses are masked jointly. Once unlocked, the model infills masked portions of a prompt template conditioned on few-shot examples. We show that such model-infilled prompts match or surpass manually designed templates, transfer effectively across models, and are complementary to existing prompt optimization methods. Our results suggest that training practices, not architectural limitations, are the primary bottleneck preventing masked diffusion language models from infilling effective prompts

## Metadata
- venue: arXiv
- year: 2026
- authors: Yoshinari Fujinuma, Keisuke Sakaguchi
- arxiv_id: 2604.03677
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2604.03677v1
- published: 2026-04-04

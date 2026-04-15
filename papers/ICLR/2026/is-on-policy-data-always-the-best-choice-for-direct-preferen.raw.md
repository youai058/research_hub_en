---
title: "Is On-Policy Data always the Best Choice for Direct Preference Optimization-Based LM Alignment?"
authors: ["Zetian Sun", "Dongfang Li", "Xuhui Chen", "Baotian Hu", "Min Zhang"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "tz9mJmgrdM"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b9ed7e5cdbac5d305b972fabfbf6c1ff266fb47d.pdf"
published: "2026"
categories: []
keywords: ["DPO", "Preference Candidates", "On-policy Sampling"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:41+09:00"
---

# Is On-Policy Data always the Best Choice for Direct Preference Optimization-Based LM Alignment?

## Abstract
The alignment of language models (LMs) with human preferences is critical for building reliable AI systems. The problem is typically framed as optimizing an LM policy to maximize the expected reward that reflects human preferences. Recently, Direct Preference Optimization (DPO) was proposed as an LM alignment method that directly optimizes the policy from static preference data, and further improved by incorporating on-policy sampling (i.e., preference candidates generated during the training loop) for better LM alignment. However, we show on-policy data is not always optimal, with systematic effectiveness difference emerging between static and on-policy preference candidates. For example, on-policy data can result in a  $3\times$ effectiveness compared with static data for Llama-3, and a $0.4\times$ effectiveness for Zephyr. To explain the phenomenon, we propose the alignment stage assumption, which divides the alignment process into two distinct stages: the preference injection stage, which benefits from diverse data, and the preference fine-tuning stage, which favors high-quality data. Through theoretical and empirical analysis, we characterize these stages and propose an effective algorithm to identify the boundaries between them. We perform experiments on $5$ models (Llama, Zephyr, Phi-2, Qwen, Pythia) and 
$2$ alignment methods (DPO, SLiC-HF) to show the generalizability of alignment stage assumption and boundary measurement.

## Metadata
- venue: ICLR
- year: 2026
- authors: Zetian Sun, Dongfang Li, Xuhui Chen, Baotian Hu, Min Zhang
- arxiv_id: 
- openreview_id: tz9mJmgrdM
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b9ed7e5cdbac5d305b972fabfbf6c1ff266fb47d.pdf
- published: 2026
- keywords: DPO, Preference Candidates, On-policy Sampling

---
title: "Provably Robust DPO: Aligning Language Models with Noisy Feedback"
authors: ["Sayak Ray Chowdhury", "Anush Kini", "Nagarajan Natarajan"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "yhpDKSw7yA"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/3f1185c2cb457015bf09600ef1508b8737fcf2a4.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:44+09:00"
---

# Provably Robust DPO: Aligning Language Models with Noisy Feedback

## Abstract
Learning from preference-based feedback has recently gained traction as a promising approach to align language models with human interests. While these aligned generative models have demonstrated impressive capabilities across various tasks, their dependence on high-quality human preference data poses a bottleneck in practical applications. Specifically, noisy (incorrect and ambiguous) preference pairs in the dataset might restrict the language models from capturing human intent accurately. While practitioners have recently proposed heuristics to mitigate the effect of noisy preferences, a complete theoretical understanding of their workings remain elusive. In this work, we aim to bridge this gap by introducing a general framework for policy optimization in the presence of random preference flips. We focus on the direct preference optimization (DPO) algorithm in particular since it assumes that preferences adhere to the Bradley-Terry-Luce (BTL) model, raising concerns about the impact of noisy data on the learned policy. We design a novel loss function, which de-bias the effect of noise on average, making a policy trained by minimizing that loss robust to the noise. Under log-linear parameterization of the policy class and assuming good feature coverage of the SFT policy, we prove that the sub-optimality gap of the proposed robust DPO (rDPO) policy compared to the optimal policy is of the order $O(\frac{1}{1-2\epsilon}\sqrt{\frac{d}{n}})$, where $\epsilon < 1/2$ is flip rate of labels, $d$ is policy parameter dimension and $n$ is size of dataset. Our experiments on IMDb sentiment generation and Anthropic's helpful-harmless dataset shows that rDPO is robust to noise in preference labels compared to vanilla DPO and other heuristics proposed by practitioners.

## Metadata
- venue: ICML
- year: 2024
- authors: Sayak Ray Chowdhury, Anush Kini, Nagarajan Natarajan
- arxiv_id: 
- openreview_id: yhpDKSw7yA
- anthology_id: 
- pdf_url: https://openreview.net/pdf/3f1185c2cb457015bf09600ef1508b8737fcf2a4.pdf
- published: 2024

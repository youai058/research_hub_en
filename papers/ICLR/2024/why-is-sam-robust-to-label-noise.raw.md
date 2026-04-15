---
title: "Why is SAM Robust to Label Noise?"
authors: ["Christina Baek", "J Zico Kolter", "Aditi Raghunathan"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "3aZCPl3ZvR"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/71206b659a568dfd25c11ddc958dfbf262274392.pdf"
published: "2024"
categories: []
keywords: ["generalization", "sharpness", "robustness", "SAM"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:19+09:00"
---

# Why is SAM Robust to Label Noise?

## Abstract
Sharpness-Aware Minimization (SAM) is most known for achieving state-of the-art performances on natural image and language tasks. However, its most pronounced improvements (of tens of percent) is rather in the presence of label noise. Understanding SAM's label noise robustness requires a departure from characterizing the robustness of minimas lying in ``flatter'' regions of the loss landscape. In particular, the peak performance under label noise occurs with early stopping, far before the loss converges. We decompose SAM's robustness into two effects: one induced by changes to the logit term and the other induced by changes to the network Jacobian. The first can be observed in linear logistic regression where SAM provably up-weights the gradient contribution from clean examples. Although this explicit up-weighting is also observable in neural networks, when we intervene and modify SAM to remove this effect, surprisingly, we see no visible degradation in performance. We infer that SAM's effect in deeper networks is instead explained entirely by the effect SAM has on the network Jacobian. We theoretically derive the  implicit regularization induced by this Jacobian effect in two layer linear networks. Motivated by our analysis, we see that cheaper alternatives to SAM that explicitly induce these regularization effects largely recover the benefits in deep networks trained on real-world datasets.

## Metadata
- venue: ICLR
- year: 2024
- authors: Christina Baek, J Zico Kolter, Aditi Raghunathan
- arxiv_id: 
- openreview_id: 3aZCPl3ZvR
- anthology_id: 
- pdf_url: https://openreview.net/pdf/71206b659a568dfd25c11ddc958dfbf262274392.pdf
- published: 2024
- keywords: generalization, sharpness, robustness, SAM

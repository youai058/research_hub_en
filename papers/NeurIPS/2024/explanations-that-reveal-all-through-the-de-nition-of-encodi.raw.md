---
title: "Explanations that reveal all through the deﬁnition of encoding"
authors: ["Aahlad Manas Puli", "Nhi Nguyen", "Rajesh Ranganath"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "mkw6x0OExg"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/010d475110d04ae68686d4efff7d0b96a43730f5.pdf"
published: "2024"
categories: []
keywords: ["feature attributions", "model explanations", "evaluating explanations", "encoding the prediction", "interpretability"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:00+09:00"
---

# Explanations that reveal all through the deﬁnition of encoding

## Abstract
Feature attributions attempt to highlight what inputs drive predictive power. Good attributions or explanations are thus those that produce inputs that retain this predictive power; accordingly, evaluations of explanations score their quality of prediction. However, evaluations produce scores better than what appears possible from the values in the explanation for a class of explanations, called encoding explanations. Probing for encoding remains a challenge because there is no general characterization of what gives the extra predictive power. We develop a deﬁnition of encoding that identiﬁes this extra predictive power via conditional dependence and show that the deﬁnition ﬁts existing examples of encoding. This deﬁnition implies, in contrast to encoding explanations, that non-encoding explanations contain all the informative inputs used to produce the explanation, giving them a “what you see is what you get” property, which makes them transparent and simple to use. Next, we prove that existing scores (ROAR, FRESH, EVAL-X) do not rank non-encoding explanations above encoding ones, and develop STRIPE-X which ranks them correctly. After empirically demonstrating the theoretical insights, we use STRIPE-X to show that despite prompting an LLM to produce non-encoding explanations for a sentiment analysis task, the LLM-generated explanations encode.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Aahlad Manas Puli, Nhi Nguyen, Rajesh Ranganath
- arxiv_id: 
- openreview_id: mkw6x0OExg
- anthology_id: 
- pdf_url: https://openreview.net/pdf/010d475110d04ae68686d4efff7d0b96a43730f5.pdf
- published: 2024
- keywords: feature attributions, model explanations, evaluating explanations, encoding the prediction, interpretability

---
title: "To Believe or Not to Believe Your LLM: Iterative Prompting for Estimating Epistemic Uncertainty"
authors: ["Yasin Abbasi-Yadkori", "Ilja Kuzborskij", "András György", "Csaba Szepesvari"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "k6iyUfwdI9"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/57904b52970ba62ecbbe68e1d3c8e28b90f4d449.pdf"
published: "2024"
categories: []
keywords: ["uncertainty quantification", "large language models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:06+09:00"
---

# To Believe or Not to Believe Your LLM: Iterative Prompting for Estimating Epistemic Uncertainty

## Abstract
We explore uncertainty quantification in large language models (LLMs), with the goal to identify when uncertainty in responses given a query is large. We simultaneously consider both epistemic and aleatoric uncertainties, where the former comes from the lack of knowledge about the ground truth (such as about facts or the language), and the latter comes from irreducible randomness (such as multiple possible answers). In particular, we derive an information-theoretic metric that allows to reliably detect when only epistemic uncertainty is large, in which case the output of the model is unreliable. This condition can be computed based solely on the output of the model obtained simply by some special iterative prompting based on the previous responses. Such quantification, for instance, allows to detect hallucinations (cases when epistemic uncertainty is high) in both single- and multi-answer responses. This is in contrast to many standard uncertainty quantification strategies (such as thresholding the log-likelihood of a response) where hallucinations in the multi-answer case cannot be detected. We conduct a series of experiments which demonstrate the advantage of our formulation. Further, our investigations shed some light on how the probabilities assigned to a given output by an LLM can be amplified by iterative prompting, which might be of independent interest.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Yasin Abbasi-Yadkori, Ilja Kuzborskij, András György, Csaba Szepesvari
- arxiv_id: 
- openreview_id: k6iyUfwdI9
- anthology_id: 
- pdf_url: https://openreview.net/pdf/57904b52970ba62ecbbe68e1d3c8e28b90f4d449.pdf
- published: 2024
- keywords: uncertainty quantification, large language models

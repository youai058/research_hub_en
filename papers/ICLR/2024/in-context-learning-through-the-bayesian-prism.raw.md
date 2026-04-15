---
title: "In-Context Learning through the Bayesian Prism"
authors: ["Madhur Panwar", "Kabir Ahuja", "Navin Goyal"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "HX5ujdsSon"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/fc9aa29ea37339217577f61679622246ebfce078.pdf"
published: "2024"
categories: []
keywords: ["In-context Learning", "Transformers", "Inductive Biases", "Meta Learning", "Language Modelling", "Bayesian Inference"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:58+09:00"
---

# In-Context Learning through the Bayesian Prism

## Abstract
In-context learning (ICL) is one of the surprising and useful features of large language models and subject of intense research. Recently, stylized meta-learning-like ICL setups have been devised that train transformers on sequences of input-output pairs $(x, f(x))$. The function $f$ comes from a function class and generalization is checked by evaluating on sequences generated from unseen functions from the same class. One of the main discoveries in this line of research has been that for several function classes, such as linear regression, transformers successfully generalize to new functions in the class. However, the inductive biases of these models resulting in this behavior are not clearly understood. A model with unlimited training data and compute is a Bayesian predictor: it learns the pretraining distribution.
In this paper we empirically examine how far this Bayesian perspective can help us understand ICL. To this end, we generalize the previous meta-ICL setup to hierarchical meta-ICL setup which involve unions of multiple task families. We instantiate this setup on a diverse range of linear and nonlinear function families and find that transformers can do ICL in this setting as well. Where Bayesian inference is tractable, we find evidence that high-capacity transformers mimic the Bayesian predictor. The Bayesian perspective provides insights into the inductive bias of ICL and how transformers perform a particular task when they are trained on multiple tasks. We also find that transformers can learn to generalize to new function classes that were not seen during pretraining. This involves deviation from the Bayesian predictor. We examine these deviations in more depth offering new insights and hypotheses.

## Metadata
- venue: ICLR
- year: 2024
- authors: Madhur Panwar, Kabir Ahuja, Navin Goyal
- arxiv_id: 
- openreview_id: HX5ujdsSon
- anthology_id: 
- pdf_url: https://openreview.net/pdf/fc9aa29ea37339217577f61679622246ebfce078.pdf
- published: 2024
- keywords: In-context Learning, Transformers, Inductive Biases, Meta Learning, Language Modelling, Bayesian Inference

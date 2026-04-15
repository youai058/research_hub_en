---
title: "Brain-tuning Improves Generalizability and Efficiency of Brain Alignment in Speech Models"
authors: ["Omer Moussa", "Mariya Toneva"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "4jgsUhWWaF"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/20901e44e3f0c35e6660fde1e5927ca4c41f3585.pdf"
published: "2025"
categories: []
keywords: ["fMRI", "Alignment", "Brain Alignment", "Cognitive Neuroscience", "Encoding Models", "Speech Models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:31+09:00"
---

# Brain-tuning Improves Generalizability and Efficiency of Brain Alignment in Speech Models

## Abstract
Pretrained language models are remarkably effective in aligning with human brain responses elicited by natural language stimuli, positioning them as promising model organisms for studying language processing in the brain. However, existing approaches for both estimating and improving this brain alignment are participant-dependent and highly affected by the amount of data available per participant, hindering both generalization to new participants and population-level analyses. In this work, we address these limitations by introducing a scalable, generalizable brain-tuning method, in which we fine-tune pretrained speech language models to jointly predict fMRI responses from multiple participants. We demonstrate that the resulting brain-tuned models exhibit strong individual brain alignment while generalizing across participants. Specifically, our method leads to 1) a 5-fold decrease in the amount of fMRI data needed to predict brain data from new participants,  2) up to a 50\% increase in the overall brain alignment, and 3) strong generalization to new unseen datasets. Furthermore, this multi-participant brain-tuning additionally improves downstream performance on semantic tasks, suggesting that training using brain data from multiple participants leads to more generalizable semantic representations. Taken together, these findings demonstrate a bidirectional benefit between neuroscience and AI, helping bridge the gap between the two fields. We make our code and models publicly available at https://github.com/bridge-ai-neuro/multi-brain-tuning.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Omer Moussa, Mariya Toneva
- arxiv_id: 
- openreview_id: 4jgsUhWWaF
- anthology_id: 
- pdf_url: https://openreview.net/pdf/20901e44e3f0c35e6660fde1e5927ca4c41f3585.pdf
- published: 2025
- keywords: fMRI, Alignment, Brain Alignment, Cognitive Neuroscience, Encoding Models, Speech Models

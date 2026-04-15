---
title: "TabM: Advancing tabular deep learning with parameter-efficient ensembling"
authors: ["Yury Gorishniy", "Akim Kotelnikov", "Artem Babenko"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Sd4wYYOhmY"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/bebc365e6ad7a313ae48f559c61d88dcf595c492.pdf"
published: "2025"
categories: []
keywords: ["tabular", "tabular data", "deep learning", "architecture"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:40+09:00"
---

# TabM: Advancing tabular deep learning with parameter-efficient ensembling

## Abstract
Deep learning architectures for supervised learning on tabular data range from simple multilayer perceptrons (MLP) to sophisticated Transformers and retrieval-augmented methods.
This study highlights a major, yet so far overlooked opportunity for substantially improving tabular MLPs; namely, parameter-efficient ensembling -- a paradigm for imitating an ensemble of models with just one model.
We start by describing TabM -- a simple model based on MLP and BatchEnsemble (an existing technique), improved with our custom modifications.
Then, we perform a large scale evaluation of tabular DL architectures on public benchmarks in terms of both task performance and efficiency, which renders the landscape of tabular DL in a new light.
In particular, we find that TabM outperforms prior tabular DL models, while the complexity of attention- and retrieval-based methods does not pay off.
Lastly, we conduct a detailed empirical analysis, that sheds some light on the high performance of TabM.
For example, we show that parameter-efficient ensembling is not an arbitrary trick, but rather a highly effective way to reduce overfitting and improve optimization dynamics of tabular MLPs.
Overall, our work brings an impactful technique to tabular DL, analyses its behaviour, and advances the performance-efficiency tradeoff with TabM -- a simple and powerful baseline for researchers and practitioners.

## Metadata
- venue: ICLR
- year: 2025
- authors: Yury Gorishniy, Akim Kotelnikov, Artem Babenko
- arxiv_id: 
- openreview_id: Sd4wYYOhmY
- anthology_id: 
- pdf_url: https://openreview.net/pdf/bebc365e6ad7a313ae48f559c61d88dcf595c492.pdf
- published: 2025
- keywords: tabular, tabular data, deep learning, architecture

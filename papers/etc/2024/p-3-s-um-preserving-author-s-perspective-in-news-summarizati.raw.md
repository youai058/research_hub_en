---
title: "P 3 S um: Preserving Author’s Perspective in News Summarization with Diffusion Language Models"
authors: ["Yuhan Liu", "Shangbin Feng", "Xiaochuang Han", "Vidhisha Balachandran", "Chan Young Park", "Sachin Kumar", "Yulia Tsvetkov"]
venue: "NAACL"
year: 2024
venue_class: "etc"
arxiv_id: ""
openreview_id: ""
anthology_id: "2024.naacl-long.119"
pdf_url: "https://aclanthology.org/2024.naacl-long.119.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "anthology"
hunter_fetched: "2026-04-15T05:20:01+09:00"
---

# P 3 S um: Preserving Author’s Perspective in News Summarization with Diffusion Language Models

## Abstract
In this work, we take a first step towards designing summarization systems that are faithful to the author’s intent, not only the semantic content of the article. Focusing on a case study of preserving political perspectives in news summarization, we find that existing approaches alter the political opinions and stances of news articles in more than 50% of summaries, misrepresenting the intent and perspectives of the news authors. We thus propose P 3 Sum, a diffusion model-based summarization approach controlled by political perspective classifiers. In P 3 Sum, the political leaning of a generated summary is iteratively evaluated at each decoding step, and any drift from the article’s original stance incurs a loss back-propagated to the embedding layers, steering the political stance of the summary at inference time. Extensive experiments on three news summarization datasets demonstrate that P 3 Sum outperforms state-of-the-art summarization systems and large language models by up to 13.7% in terms of the success rate of stance preservation, with competitive performance on standard metrics of summarization quality. Our findings present a first analysis of preservation of pragmatic features in summarization, highlight the lacunae in existing summarization models—that even state-of-the-art models often struggle to preserve author’s intents—and develop new summarization systems that are more faithful to author’s perspectives.

## Metadata
- venue: NAACL
- year: 2024
- authors: Yuhan Liu, Shangbin Feng, Xiaochuang Han, Vidhisha Balachandran, Chan Young Park, Sachin Kumar, Yulia Tsvetkov
- arxiv_id: 
- openreview_id: 
- anthology_id: 2024.naacl-long.119
- pdf_url: https://aclanthology.org/2024.naacl-long.119.pdf
- published: 2024

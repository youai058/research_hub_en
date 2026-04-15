---
title: "JailNewsBench: Multi-Lingual and Regional Benchmark for Fake News Generation under Jailbreak Attacks"
authors: ["Masahiro Kaneko", "Ayana Niwa", "Timothy Baldwin"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "7dTqUaY2Kl"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/29c7759001ffc03f99f8a66e2d540f21901f5f50.pdf"
published: "2026"
categories: []
keywords: ["fake news", "jailbreak", "llm", "multilingual"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:18+09:00"
---

# JailNewsBench: Multi-Lingual and Regional Benchmark for Fake News Generation under Jailbreak Attacks

## Abstract
Fake news undermines societal trust and decision-making across politics, economics, health, and international relations, and in extreme cases threatens human lives and societal safety.
Because fake news reflects region-specific political, social, and cultural contexts and is expressed in language, evaluating the risks of large language models (LLMs) requires a multi-lingual and regional perspective.
Malicious users can bypass safeguards through jailbreak attacks, inducing LLMs to generate fake news.
However, no benchmark currently exists to systematically assess attack resilience across languages and regions.
Here, we propose JailNewsBench, the first benchmark for evaluating LLM robustness against jailbreak-induced fake news generation.
JailNewsBench spans 34 regions and 22 languages, covering 8 evaluation sub-metrics through LLM-as-a-Judge and 5 jailbreak attacks, with approximately 300k instances.
Our evaluation of 9 LLMs reveals that the maximum attack success rate (ASR) reached 86.3% and the maximum harmfulness score was 3.5 out of 5.
Notably, for English and U.S.-related topics, the defensive performance of typical multi-lingual LLMs was significantly lower than for other regions, highlighting substantial imbalances in safety across languages and regions.
In addition, our analysis shows that coverage of fake news in existing safety datasets is limited and less well defended than major categories such as toxicity and social bias.
Our dataset and code are available at https://github.com/kanekomasahiro/jail_news_bench.

## Metadata
- venue: ICLR
- year: 2026
- authors: Masahiro Kaneko, Ayana Niwa, Timothy Baldwin
- arxiv_id: 
- openreview_id: 7dTqUaY2Kl
- anthology_id: 
- pdf_url: https://openreview.net/pdf/29c7759001ffc03f99f8a66e2d540f21901f5f50.pdf
- published: 2026
- keywords: fake news, jailbreak, llm, multilingual

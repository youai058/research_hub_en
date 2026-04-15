---
title: "Emoji Attack: Enhancing Jailbreak Attacks Against Judge LLM Detection"
authors: ["Zhipeng Wei", "Yuqi Liu", "N. Benjamin Erichson"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Q0rKYiVEZq"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9c3c465a66876cc791e42e3c2a98df64e54519c6.pdf"
published: "2025"
categories: []
keywords: ["LLM safety; Jailbreaking Attacks; Judge LLMs; Token Segmentation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:03+09:00"
---

# Emoji Attack: Enhancing Jailbreak Attacks Against Judge LLM Detection

## Abstract
Jailbreaking techniques trick Large Language Models (LLMs) into producing restricted output, posing a potential threat. One line of defense is to use another LLM as a Judge to evaluate the harmfulness of generated text. However, we reveal that these Judge LLMs are vulnerable to token segmentation bias, an issue that arises when delimiters alter the tokenization process, splitting words into smaller sub-tokens. This alters the embeddings of the entire sequence, reducing detection accuracy and allowing harmful content to be misclassified as safe. In this paper, we introduce Emoji Attack, a novel strategy that amplifies existing jailbreak prompts by exploiting token segmentation bias. Our method leverages in-context learning to systematically insert emojis into text before it is evaluated by a Judge LLM, inducing embedding distortions that significantly lower the likelihood of detecting unsafe content. Unlike traditional delimiters, emojis also introduce semantic ambiguity, making them particularly effective in this attack. Through experiments on state-of-the-art Judge LLMs, we demonstrate that Emoji Attack substantially reduces the unsafe prediction rate, bypassing existing safeguards.

## Metadata
- venue: ICML
- year: 2025
- authors: Zhipeng Wei, Yuqi Liu, N. Benjamin Erichson
- arxiv_id: 
- openreview_id: Q0rKYiVEZq
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9c3c465a66876cc791e42e3c2a98df64e54519c6.pdf
- published: 2025
- keywords: LLM safety; Jailbreaking Attacks; Judge LLMs; Token Segmentation

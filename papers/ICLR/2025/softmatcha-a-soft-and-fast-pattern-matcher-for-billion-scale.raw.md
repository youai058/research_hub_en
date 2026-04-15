---
title: "SoftMatcha: A Soft and Fast Pattern Matcher for Billion-Scale Corpus Searches"
authors: ["Hiroyuki Deguchi", "Go Kamoda", "Yusuke Matsushita", "Chihiro Taguchi", "Kohei Suenaga", "Masaki Waga", "Sho Yokoi"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Q6PAnqYVpo"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9e329d6d8d6b019a23e1bf6e565ba27894464c62.pdf"
published: "2025"
categories: []
keywords: ["natural language processing", "full-text search", "word embeddings", "inverted index", "pattern match"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:01+09:00"
---

# SoftMatcha: A Soft and Fast Pattern Matcher for Billion-Scale Corpus Searches

## Abstract
Researchers and practitioners in natural language processing and computational linguistics frequently observe and analyze the real language usage in large-scale corpora.
For that purpose, they often employ off-the-shelf pattern-matching tools, such as grep, and keyword-in-context concordancers, which is widely used in corpus linguistics for gathering examples.
Nonetheless, these existing techniques rely on surface-level string matching, and thus they suffer from the major limitation of not being able to handle orthographic variations and paraphrasing---notable and common phenomena in any natural language.
In addition, existing continuous approaches such as dense vector search tend to be overly coarse, often retrieving texts that are unrelated but share similar topics.
Given these challenges, we propose a novel algorithm that achieves soft (or semantic) yet efficient pattern matching by relaxing a surface-level matching with word embeddings.
Our algorithm is highly scalable with respect to the size of the corpus text utilizing inverted indexes.
We have prepared an efficient implementation, and we provide an accessible web tool.
Our experiments demonstrate that the proposed method
(i) can execute searches on billion-scale corpora in less than a second, which is comparable in speed to surface-level string matching and dense vector search;
(ii) can extract harmful instances that semantically match queries from a large set of English and Japanese Wikipedia articles;
and (iii) can be effectively applied to corpus-linguistic analyses of Latin, a language with highly diverse inflections.

## Metadata
- venue: ICLR
- year: 2025
- authors: Hiroyuki Deguchi, Go Kamoda, Yusuke Matsushita, Chihiro Taguchi, Kohei Suenaga, Masaki Waga, Sho Yokoi
- arxiv_id: 
- openreview_id: Q6PAnqYVpo
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9e329d6d8d6b019a23e1bf6e565ba27894464c62.pdf
- published: 2025
- keywords: natural language processing, full-text search, word embeddings, inverted index, pattern match

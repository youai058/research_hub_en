---
title: "Proving Test Set Contamination in Black-Box Language Models"
authors: ["Yonatan Oren", "Nicole Meister", "Niladri S. Chatterji", "Faisal Ladhak", "Tatsunori Hashimoto"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "KS8mIvetg2"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/cfd79aaab7bdcd4f7c032c57fe7e607058042c80.pdf"
published: "2024"
categories: []
keywords: ["language modeling", "memorization", "dataset contamination"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:57+09:00"
---

# Proving Test Set Contamination in Black-Box Language Models

## Abstract
Large language models are trained on vast amounts of internet data, prompting concerns that they have memorized public benchmarks. Detecting this type of contamination is challenging because the pretraining data used by proprietary models are often not publicly accessible.

We propose a procedure for detecting test set contamination of language models with exact false positive guarantees and without access to pretraining data or model weights. Our approach leverages the fact that when there is no data contamination, all orderings of an exchangeable benchmark should be equally likely. In contrast, the tendency for language models to memorize example order means that a contaminated language model will find certain canonical orderings to be much more likely than others. Our test flags potential contamination whenever the likelihood of a canonically ordered benchmark dataset is significantly higher than the likelihood after shuffling the examples.

We demonstrate that our procedure is sensitive enough to reliably detect contamination in challenging situations, including models as small as 1.4 billion parameters, on small test sets only 1000 examples, and datasets that appear only a few times in the pretraining corpus. Finally, we evaluate LLaMA-2 to apply our test in a realistic setting and find our results to be consistent with existing contamination evaluations.

## Metadata
- venue: ICLR
- year: 2024
- authors: Yonatan Oren, Nicole Meister, Niladri S. Chatterji, Faisal Ladhak, Tatsunori Hashimoto
- arxiv_id: 
- openreview_id: KS8mIvetg2
- anthology_id: 
- pdf_url: https://openreview.net/pdf/cfd79aaab7bdcd4f7c032c57fe7e607058042c80.pdf
- published: 2024
- keywords: language modeling, memorization, dataset contamination

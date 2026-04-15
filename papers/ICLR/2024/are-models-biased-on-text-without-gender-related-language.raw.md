---
title: "Are Models Biased on Text without Gender-related Language?"
authors: ["Catarina G Belém", "Preethi Seshadri", "Yasaman Razeghi", "Sameer Singh"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "w1JanwReU6"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/bd1813ac5b333e7445f4c1a4ac8d3680ace9c572.pdf"
published: "2024"
categories: []
keywords: ["Large language models", "bias evaluation", "gender bias", "gender co-occurring words", "gender-invariant", "pretraining data statistics"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:13+09:00"
---

# Are Models Biased on Text without Gender-related Language?

## Abstract
Gender bias research has been pivotal in revealing undesirable behaviors in large language models, exposing serious gender stereotypes associated with occupations, and emotions. A key observation in prior work is that models reinforce stereotypes as a consequence of the gendered correlations that are present in the training data. In this paper, we focus on bias where the effect from training data is unclear, and instead address the question: *Do language models still exhibit gender bias in non-stereotypical settings?* To do so, we introduce **UnStereoEval (USE)**, a novel framework tailored for investigating gender bias in stereotype-free scenarios. USE defines a sentence-level score based on pretraining data statistics to determine if the sentence contain minimal word-gender associations. To systematically benchmark the fairness of popular language models in stereotype-free scenarios, we utilize USE to automatically generate benchmarks without any gender-related language.  By leveraging USE's sentence-level score, we also repurpose prior gender bias benchmarks (Winobias and Winogender) for non-stereotypical evaluation. Surprisingly, we find low fairness across all 28 tested models.  Concretely, models demonstrate fair behavior in only 9%-41% of  stereotype-free sentences, suggesting that bias does not solely stem from the presence of gender-related words. These results raise important questions about where underlying model biases come from and highlight the need for more systematic and comprehensive bias evaluation. We release the full dataset and code at [ucinlp.github.io/unstereo-eval](https://ucinlp.github.io/unstereo-eval).

## Metadata
- venue: ICLR
- year: 2024
- authors: Catarina G Belém, Preethi Seshadri, Yasaman Razeghi, Sameer Singh
- arxiv_id: 
- openreview_id: w1JanwReU6
- anthology_id: 
- pdf_url: https://openreview.net/pdf/bd1813ac5b333e7445f4c1a4ac8d3680ace9c572.pdf
- published: 2024
- keywords: Large language models, bias evaluation, gender bias, gender co-occurring words, gender-invariant, pretraining data statistics

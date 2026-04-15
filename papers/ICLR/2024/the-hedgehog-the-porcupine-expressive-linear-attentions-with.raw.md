---
title: "The Hedgehog & the Porcupine: Expressive Linear Attentions with Softmax Mimicry"
authors: ["Michael Zhang", "Kush Bhatia", "Hermann Kumbong", "Christopher Re"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "4g02l2N2Nx"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/253a4c0c2132cbb269cad956934997223cc2c5c0.pdf"
published: "2024"
categories: []
keywords: ["linear attention", "transformers"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:15+09:00"
---

# The Hedgehog & the Porcupine: Expressive Linear Attentions with Softmax Mimicry

## Abstract
Linear attentions have shown promise for improving Transformer efficiency, reducing attention's quadratic complexity to linear in sequence length. This holds exciting promise for (1) training linear Transformers from scratch, (2) `inetuned-conversion of task-specific Transformers into linear versions that recover task performance, and (3) pretrained-conversion of Transformers, such as language models, into linear versions readily finetunable on downstream tasks. However, linear attentions often underperform compared to standard softmax attention. To close this performance gap, we study the behaviors of softmax and linear attentions in various train-from-scratch and finetuned-conversion settings. We find prior linear attentions lack key properties of softmax attention tied to good performance: low-entropy (or spiky) weights and dot-product monotonicity. We further observe surprisingly simple feature maps that retain these properties match softmax performance, but are inefficient to compute in linear attention. We thus propose Hedgehog, a learnable linear attention that retains the spiky and monotonic properties of softmax attention while maintaining linear complexity. Hedgehog uses simple, trainable MLPs to produce attention weights mimicking softmax attention. Experiments show Hedgehog recovers over 99\% of standard Transformer performance in train-from-scratch and finetuned-conversion settings, outperforming prior linear attentions by up to 6 perplexity points on WikiText-103 when training causal GPT models from scratch, and up to 8.7 GLUE score points when converting finetuned bidirectional BERT models. Hedgehog also enables pretrained-conversion. Converting a pretrained GPT-2 into a linear attention variant achieves state-of-the-art 16.7 perplexity on WikiText-103 for 125M subquadratic decoder models. We finally turn a pretrained Llama-2 7B into a viable linear attention Llama. With low-rank adaptation, Hedgehog-Llama-2 7B achieves 28.1 higher ROUGE-1 points over the base standard attention model, where prior linear attentions lead to 16.5 point drops.

## Metadata
- venue: ICLR
- year: 2024
- authors: Michael Zhang, Kush Bhatia, Hermann Kumbong, Christopher Re
- arxiv_id: 
- openreview_id: 4g02l2N2Nx
- anthology_id: 
- pdf_url: https://openreview.net/pdf/253a4c0c2132cbb269cad956934997223cc2c5c0.pdf
- published: 2024
- keywords: linear attention, transformers

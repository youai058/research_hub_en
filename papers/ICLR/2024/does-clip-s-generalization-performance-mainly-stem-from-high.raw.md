---
title: "Does CLIP’s generalization performance mainly stem from high train-test similarity?"
authors: ["Prasanna Mayilvahanan", "Thaddäus Wiedemer", "Evgenia Rusak", "Matthias Bethge", "Wieland Brendel"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "tnBaiidobu"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/914ba616ab5450c89e489fa002bc6f6587152c84.pdf"
published: "2024"
categories: []
keywords: ["robustness", "foundation models", "CLIP", "LAION", "ImageNet", "generalization", "OOD robustness", "distribution shift", "vision language models", "self-supervised learning", "contrastive learning", "ObjectNet", "ImageNet-R", "ImageNet-Sketch", "ImageNet-A", "ImageNet-V2"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:23+09:00"
---

# Does CLIP’s generalization performance mainly stem from high train-test similarity?

## Abstract
Foundation models like CLIP are trained on hundreds of millions of samples and effortlessly generalize to new tasks and inputs. Out of the box, CLIP shows stellar zero-shot and few-shot capabilities on a wide range of out-of-distribution (OOD) benchmarks, which prior works attribute mainly to today's large and comprehensive training dataset (like LAION). However, it is questionable how meaningful terms like out-of-distribution generalization are for CLIP as it seems likely that web-scale datasets like LAION simply contain many samples that are similar to common OOD benchmarks originally designed for ImageNet. To test this hypothesis, we retrain CLIP on pruned LAION splits that replicate ImageNet’s train-test similarity with respect to common OOD benchmarks. While we observe a performance drop on some benchmarks, surprisingly, CLIP’s overall performance remains high. This shows that high train-test similarity is insufficient to explain CLIP’s OOD performance, and other properties of the training data must drive CLIP to learn more generalizable representations. Additionally, by pruning data points that are dissimilar to the OOD benchmarks, we uncover a 100M split of LAION (¼ of its original size) on which CLIP can be trained to match its original OOD performance.

## Metadata
- venue: ICLR
- year: 2024
- authors: Prasanna Mayilvahanan, Thaddäus Wiedemer, Evgenia Rusak, Matthias Bethge, Wieland Brendel
- arxiv_id: 
- openreview_id: tnBaiidobu
- anthology_id: 
- pdf_url: https://openreview.net/pdf/914ba616ab5450c89e489fa002bc6f6587152c84.pdf
- published: 2024
- keywords: robustness, foundation models, CLIP, LAION, ImageNet, generalization, OOD robustness, distribution shift, vision language models, self-supervised learning, contrastive learning, ObjectNet, ImageNet-R, ImageNet-Sketch, ImageNet-A, ImageNet-V2

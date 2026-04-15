---
title: "Portable Reward Tuning: Towards Reusable Fine-Tuning across Different Pretrained Models"
authors: ["Daiki Chijiwa", "Taku Hasegawa", "Kyosuke Nishida", "Kuniko Saito", "Susumu Takeuchi"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "cYNBsMTAVL"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/96167cb6e0a1397568d92e9feb79baa1dbaa2e3f.pdf"
published: "2025"
categories: []
keywords: ["inference-time tuning", "reward maximization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:22+09:00"
---

# Portable Reward Tuning: Towards Reusable Fine-Tuning across Different Pretrained Models

## Abstract
While foundation models have been exploited for various expert tasks with their fine-tuned parameters, any foundation model will be eventually outdated due to its old knowledge or limited capability, and thus should be replaced by a new foundation model. Subsequently, to benefit from its latest knowledge or improved capability, the new foundation model should be fine-tuned on each task again, which incurs not only the additional training cost but also the maintenance cost of the task-specific data. Existing work address this problem by inference-time tuning, i.e., modifying the output probability from the new foundation model by the outputs from the old foundation model and its fine-tuned model, which involves an additional inference cost by the latter two models. In this paper, we explore a new fine-tuning principle (which we call portable reward tuning; PRT) that reduces the inference cost by its nature, based on the reformulation of fine-tuning as the reward maximization with Kullback-Leibler regularization. Specifically, instead of fine-tuning parameters of the foundation models, PRT trains the reward model explicitly through the same loss as in fine-tuning. During inference, the reward model can be used with any foundation model (with the same set of vocabularies or labels) through the formulation of reward maximization. Experimental results, including both vision and language models, show that the PRT-trained model can achieve comparable accuracy with less inference cost, in comparison to the existing work of inference-time tuning.

## Metadata
- venue: ICML
- year: 2025
- authors: Daiki Chijiwa, Taku Hasegawa, Kyosuke Nishida, Kuniko Saito, Susumu Takeuchi
- arxiv_id: 
- openreview_id: cYNBsMTAVL
- anthology_id: 
- pdf_url: https://openreview.net/pdf/96167cb6e0a1397568d92e9feb79baa1dbaa2e3f.pdf
- published: 2025
- keywords: inference-time tuning, reward maximization

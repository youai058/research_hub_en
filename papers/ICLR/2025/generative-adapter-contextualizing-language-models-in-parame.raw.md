---
title: "Generative Adapter: Contextualizing Language Models in Parameters with A Single Forward Pass"
authors: ["Tong Chen", "Hao Fang", "Patrick Xia", "Xiaodong Liu", "Benjamin Van Durme", "Luke Zettlemoyer", "Jianfeng Gao", "Hao Cheng"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "bc3sUsS6ck"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2511dfdd2011b77782b62c70d9e3d9ffa074e512.pdf"
published: "2025"
categories: []
keywords: ["language model; efficient adaptation; fine-tuning; prompting"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:00+09:00"
---

# Generative Adapter: Contextualizing Language Models in Parameters with A Single Forward Pass

## Abstract
Large language models (LLMs) acquire substantial knowledge during pretraining but often need adaptation to new contexts, tasks, or domains, typically achieved through fine-tuning or prompting. However, fine-tuning incurs significant training costs, while prompting increases inference overhead. Inspired by fast weight memory, we introduce GenerativeAdapter, an effective and efficient adaptation method that encode test-time context into language model parameters with a single forward pass.
GenerativeAdapter augments a frozen pretrained LM with a lightweight adapter generator, trained via self-supervised learning, to produce parameter-efficient adapters.
Notably, our generator is general-purpose, i.e., one generator can adapt the corresponding base model for all langauge processing scenarios.
We apply GenerativeAdapter to two pretrained LMs (Mistral-7B-Instruct and Llama2-7B-Chat) and evaluate the adapted models across  knowledge acquisition from documents, learning from demonstrations, and personalization for users.
In StreamingQA, our approach is effective in injecting knowledge into the LM's parameters, achieving a 63.5\% improvement in F1 score over the model with supervised fine-tuning (from $19.5$ to $31.5$) for contexts as long as 32K tokens.
In the MetaICL in-context learning evaluation, our method achieves an average accuracy of $44.9$ across 26 tasks, outperforming the base model. 
On MSC, our method proves to be highly competitive in memorizing user information from conversations with a 4x reduction in computation and memory costs compared to 
prompting with full conversation history.
Overall, GenerativeAdapter provides a viable solution for adapting large LMs to evolving information and providing tailored user experience, while reducing training and inference costs relative to traditional fine-tuning and prompting techniques.

## Metadata
- venue: ICLR
- year: 2025
- authors: Tong Chen, Hao Fang, Patrick Xia, Xiaodong Liu, Benjamin Van Durme, Luke Zettlemoyer, Jianfeng Gao, Hao Cheng
- arxiv_id: 
- openreview_id: bc3sUsS6ck
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2511dfdd2011b77782b62c70d9e3d9ffa074e512.pdf
- published: 2025
- keywords: language model; efficient adaptation; fine-tuning; prompting

---
title: "Programming by Backprop: An Instruction is Worth 100 Examples When Finetuning LLMs"
authors: ["Jonathan Cook", "Silvia Sapora", "Arash Ahmadian", "Akbir Khan", "Tim Rocktäschel", "Jakob Nicolaus Foerster", "Laura Ruis"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "y1OWj26FCo"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/25554a5b52d5e0f85173726271f5483f13e44419.pdf"
published: "2026"
categories: []
keywords: ["Large Language Models", "Abstraction", "Procedural Knowledge"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:24+09:00"
---

# Programming by Backprop: An Instruction is Worth 100 Examples When Finetuning LLMs

## Abstract
Large language models (LLMs) are typically trained to acquire behaviours from demonstrations or experience, yet much of their training data is declarative: instructions, rules, and descriptions that specify behaviours without showing how to execute them. We introduce **Programming by Backprop (PBB)**: a training regime that enables LLMs to acquire *procedural* knowledge (i.e., reusable behaviours) from *declarative* instructions encountered during training. With PBB, instructions in training data provide an opportunity to "program" specific behaviours into model weights. The core principle underpinning PBB is the separation of learning how instructions map to behaviour from internalising new instructions. We devise two distinct PBB curricula that leverage this principle. Through controlled experiments across two domains (algorithmic execution from Python source code and text generation from context-free grammars), we demonstrate the benefit of these curricula over training on a homogeneous data mixture. Crucially, PBB is highly sample efficient, with *a single instruction substituting for up to 100 execution examples*. Though execution of instructions in training data remains less reliable than when instructions are given in-context, our results demonstrate that procedural knowledge can be noisily `programmed' into LLMs through PBB, with important implications for data curation and safety.

## Metadata
- venue: ICLR
- year: 2026
- authors: Jonathan Cook, Silvia Sapora, Arash Ahmadian, Akbir Khan, Tim Rocktäschel, Jakob Nicolaus Foerster, Laura Ruis
- arxiv_id: 
- openreview_id: y1OWj26FCo
- anthology_id: 
- pdf_url: https://openreview.net/pdf/25554a5b52d5e0f85173726271f5483f13e44419.pdf
- published: 2026
- keywords: Large Language Models, Abstraction, Procedural Knowledge

---
title: "Learning to Reason via Program Generation, Emulation, and Search"
authors: ["Nathaniel Weir", "Muhammad Khalifa", "Linlu Qiu", "Orion Weller", "Peter Clark"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "te6VagJf6G"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/3a26df6098d24990525e293f7f00b96ed7ee7344.pdf"
published: "2024"
categories: []
keywords: ["language models", "instruction tuning", "code generation", "reasoning", "program search", "program emulation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:29+09:00"
---

# Learning to Reason via Program Generation, Emulation, and Search

## Abstract
Program synthesis with language models (LMs) has unlocked a large set of reasoning abilities; code-tuned LMs have proven adept at generating programs that solve a wide variety of algorithmic symbolic manipulation tasks (e.g. word concatenation). However, not all reasoning tasks are easily expressible as code, e.g. tasks involving commonsense reasoning, moral decision-making, and sarcasm understanding. Our goal is to extend a LM’s program synthesis skills to such tasks and evaluate the results via pseudo-programs, namely Python programs where some leaf function calls are left undefined. To that end, we propose, Code Generation and Emulated EXecution (COGEX). COGEX works by (1) training LMs to generate pseudo-programs and (2) teaching them to emulate their generated program’s execution, including those leaf functions, allowing the LM’s knowledge to fill in the execution gaps; and (3) using them to search over many programs to find an optimal one. To adapt the COGEX model to a new task, we introduce a method for performing program search to find a single program whose pseudo-execution yields optimal performance when applied to all the instances of a given dataset. We show that our approach yields large improvements compared to standard in-context learning approaches on a battery of tasks, both algorithmic and soft reasoning. This result thus demonstrates that code synthesis can be applied to a much broader class of problems than previously considered.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Nathaniel Weir, Muhammad Khalifa, Linlu Qiu, Orion Weller, Peter Clark
- arxiv_id: 
- openreview_id: te6VagJf6G
- anthology_id: 
- pdf_url: https://openreview.net/pdf/3a26df6098d24990525e293f7f00b96ed7ee7344.pdf
- published: 2024
- keywords: language models, instruction tuning, code generation, reasoning, program search, program emulation

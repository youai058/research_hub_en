---
title: "What Makes Good Data for Alignment? A Comprehensive Study of Automatic Data Selection in Instruction Tuning"
authors: ["Wei Liu", "Weihao Zeng", "Keqing He", "Yong Jiang", "Junxian He"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "BTKAeLqLMw"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a617374cea846fefdd6511494d4f9722b000a237.pdf"
published: "2024"
categories: []
keywords: ["data selection", "instruction tuning", "large language models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:49+09:00"
---

# What Makes Good Data for Alignment? A Comprehensive Study of Automatic Data Selection in Instruction Tuning

## Abstract
Instruction tuning is a standard technique employed to align large language models to end tasks and user preferences after the initial pretraining phase. Recent research indicates the critical role of data engineering in instruction tuning -- when appropriately selected, only limited data is necessary to achieve superior performance. However, we still lack a principled understanding of what makes good instruction tuning data for alignment, and how we should select data automatically and effectively. In this work, we delve deeply into automatic data selection strategies for alignment. We start with controlled studies to measure data across three dimensions: complexity, quality, and diversity, along which we examine existing methods and introduce novel techniques for enhanced data measurement. Subsequently, we propose a simple strategy to select data samples based on the measurement. We present Deita (short for Data-Efficient Instruction Tuning for Alignment), a series of models fine-tuned from LLaMA models using data samples automatically selected with our proposed approach.  When assessed through both automatic metrics and human evaluation, Deita performs better or on par with the state-of-the-art open-source alignment models such as Vicuna and WizardLM with only 6K training data samples -- 10x less than the data used in the baselines. We anticipate this work to provide clear guidelines and tools on automatic data selection, aiding researchers and practitioners in achieving data-efficient alignment.

## Metadata
- venue: ICLR
- year: 2024
- authors: Wei Liu, Weihao Zeng, Keqing He, Yong Jiang, Junxian He
- arxiv_id: 
- openreview_id: BTKAeLqLMw
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a617374cea846fefdd6511494d4f9722b000a237.pdf
- published: 2024
- keywords: data selection, instruction tuning, large language models

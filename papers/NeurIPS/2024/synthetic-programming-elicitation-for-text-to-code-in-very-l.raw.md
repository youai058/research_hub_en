---
title: "Synthetic Programming Elicitation for Text-to-Code in Very Low-Resource Programming and Formal Languages"
authors: ["Federico Mora", "Justin Wong", "Haley Lepe", "Sahil Bhatia", "Karim Elmaaroufi", "George Varghese", "Joseph E. Gonzalez", "Elizabeth Polgreen", "Sanjit A. Seshia"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "kQPzFiwVIu"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/fb296b40f1d3c4fd79e6e3ea90f07eef6954f0ea.pdf"
published: "2024"
categories: []
keywords: ["Text-to-Code", "Low-Resource Programming Languages", "MAX-SAT", "Parsing", "Program Repair"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:50+09:00"
---

# Synthetic Programming Elicitation for Text-to-Code in Very Low-Resource Programming and Formal Languages

## Abstract
Recent advances in large language models (LLMs) for code applications have demonstrated remarkable zero-shot fluency and instruction following on challenging code related tasks ranging from test case generation to self-repair. Unsurprisingly, however, models struggle to compose syntactically valid programs in programming languages unrepresented in pre-training, referred to as very low-resource Programming Languages (VLPLs). VLPLs appear in crucial settings, including domain-specific languages for internal tools, tool-chains for legacy languages, and formal verification frameworks. Inspired by a technique called natural programming elicitation, we propose designing an intermediate language that LLMs ``naturally'' know how to use and which can be automatically compiled to a target VLPL. When LLMs generate code that lies outside of this intermediate language, we use compiler techniques to repair the code into programs in the intermediate language. Overall, we introduce _synthetic programming elicitation and compilation_ (SPEAC), an approach that enables LLMs to generate syntactically valid code even for VLPLs. We empirically evaluate the performance of SPEAC in a case study for the UCLID5 formal verification language and find that, compared to existing retrieval and fine-tuning baselines, SPEAC produces syntactically correct programs more frequently and without sacrificing semantic correctness.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Federico Mora, Justin Wong, Haley Lepe, Sahil Bhatia, Karim Elmaaroufi, George Varghese, Joseph E. Gonzalez, Elizabeth Polgreen, Sanjit A. Seshia
- arxiv_id: 
- openreview_id: kQPzFiwVIu
- anthology_id: 
- pdf_url: https://openreview.net/pdf/fb296b40f1d3c4fd79e6e3ea90f07eef6954f0ea.pdf
- published: 2024
- keywords: Text-to-Code, Low-Resource Programming Languages, MAX-SAT, Parsing, Program Repair

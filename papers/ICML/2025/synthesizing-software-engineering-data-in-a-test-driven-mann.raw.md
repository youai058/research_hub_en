---
title: "Synthesizing Software Engineering Data in a Test-Driven Manner"
authors: ["Lei Zhang", "Jiaxi Yang", "Min Yang", "Jian Yang", "Mouxiang Chen", "Jiajun Zhang", "Zeyu Cui", "Binyuan Hui", "Junyang Lin"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "P9DQ2IExgS"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2d182121aca3afc796101876991322370e53a173.pdf"
published: "2025"
categories: []
keywords: ["Large language Model", "Software Engineering", "Test-Driven Development", "Code Agent"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:21+09:00"
---

# Synthesizing Software Engineering Data in a Test-Driven Manner

## Abstract
We introduce **SWE-Flow**, a novel data synthesis framework grounded in Test-Driven Development (TDD).
Unlike existing software engineering data that rely on human-submitted issues, **SWE-Flow** automatically infers incremental development steps directly from unit tests, which inherently encapsulate high-level requirements.
The core of **SWE-Flow** is the construction of a Runtime Dependency Graph (RDG), which precisely captures function interactions, enabling the generation of a structured, step-by-step *development schedule*.
At each step, **SWE-Flow** produces a partial codebase, the corresponding unit tests, and the necessary code modifications, resulting in fully verifiable TDD tasks.
With this approach, we generated 16,061 training instances and 2,020 test instances from real-world GitHub projects, creating the **SWE-Flow-Eval** benchmark.
Our experiments show that fine-tuning open model on this dataset significantly improves performance in TDD-based coding.
To facilitate further research, we release all code, datasets, models, and Docker images at [Github](https://github.com/Hambaobao/SWE-Flow).

## Metadata
- venue: ICML
- year: 2025
- authors: Lei Zhang, Jiaxi Yang, Min Yang, Jian Yang, Mouxiang Chen, Jiajun Zhang, Zeyu Cui, Binyuan Hui, Junyang Lin
- arxiv_id: 
- openreview_id: P9DQ2IExgS
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2d182121aca3afc796101876991322370e53a173.pdf
- published: 2025
- keywords: Large language Model, Software Engineering, Test-Driven Development, Code Agent

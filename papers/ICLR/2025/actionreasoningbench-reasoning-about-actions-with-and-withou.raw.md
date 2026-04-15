---
title: "ActionReasoningBench: Reasoning about Actions with and without Ramification Constraints"
authors: ["Divij Handa", "Pavel Dolin", "Shrinidhi Kumbhar", "Tran Cao Son", "Chitta Baral"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "NUD03NBDOE"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/83736ef168f97ad552f160a8513145ada3403953.pdf"
published: "2025"
categories: []
keywords: ["Reasoning about Actions and Change (RAC)", "Benchmark", "Large Language Models (LLMs)"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:07+09:00"
---

# ActionReasoningBench: Reasoning about Actions with and without Ramification Constraints

## Abstract
Reasoning about Actions and Change (RAC) has historically played a pivotal role in solving foundational AI problems, such as the frame problem. It has driven advancements in AI fields, such as non-monotonic and commonsense reasoning. RAC remains crucial for AI systems that operate in dynamic environments, engage in interactive scenarios, or rely on commonsense reasoning. Despite substantial advances made by Large Language Models (LLMs) in various AI domains, their performance in RAC remains underexplored. To address this gap, we introduce a new diagnostic benchmark, $\textbf{ActionReasoningBench}$, which encompasses 8 domains and includes questions for up to 19 action sequences. This benchmark rigorously evaluates LLMs across six key RAC dimensions: $\textit{Fluent Tracking}$, $\textit{State Tracking}$, $\textit{Action Executability}$, $\textit{Effects of Actions}$, $\textit{Numerical RAC}$, and $\textit{Composite Questions}$. LLMs demonstrate average accuracy rates of 73.55%, 65.63%, 58.73%, and 62.38% on the former four dimensions, which are frequently discussed in RAC literature. However, the performance on the latter two dimensions, which introduce complex and novel reasoning questions, the average performance of LLMs is lowered to 33.16% and 51.19%, respectively, reflecting a 17.9% performance decline. We also introduce new ramification constraints to capture the indirect effects of actions, providing deeper insights into RAC challenges. Our evaluation of state-of-the-art LLMs, including both open-source and commercial models, reveals challenges across all RAC dimensions, particularly in handling ramifications, with GPT-4o failing to solve any question and o1-preview achieving a score of only 18.4%.

## Metadata
- venue: ICLR
- year: 2025
- authors: Divij Handa, Pavel Dolin, Shrinidhi Kumbhar, Tran Cao Son, Chitta Baral
- arxiv_id: 
- openreview_id: NUD03NBDOE
- anthology_id: 
- pdf_url: https://openreview.net/pdf/83736ef168f97ad552f160a8513145ada3403953.pdf
- published: 2025
- keywords: Reasoning about Actions and Change (RAC), Benchmark, Large Language Models (LLMs)

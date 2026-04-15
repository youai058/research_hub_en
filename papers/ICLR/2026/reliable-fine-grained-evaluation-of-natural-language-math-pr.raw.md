---
title: "Reliable Fine-Grained Evaluation of Natural Language Math Proofs"
authors: ["Wenjie Ma", "Andrei Cojocaru", "Neel Kolhe", "Haihan Zhang", "Vincent Zhuang", "Matei Zaharia", "Sewon Min"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ky5iqwZSXI"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9b622de8fbbd37c2317ba4b965bbfde1e3026ded.pdf"
published: "2026"
categories: []
keywords: ["automated proof evaluation; LLM-as-a-judge; LLM-generated math proofs; rubric-guided grading; prompt optimization; expert-annotated proof dataset; evaluator reliability; reward modeling"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:32+09:00"
---

# Reliable Fine-Grained Evaluation of Natural Language Math Proofs

## Abstract
Recent advances in large language models (LLMs) for mathematical reasoning have largely focused on tasks with easily verifiable final answers while generating and verifying natural language math proofs remains an open challenge. We identify the absence of a reliable, fine-grained evaluator for LLM-generated math proofs as a critical gap.
To address this, we propose a systematic methodology for developing and validating evaluators that assign fine-grained scores on a 0-7 scale to model-generated math proofs. 
To enable this study, we introduce ProofBench, the first expert-annotated dataset of fine-grained proof ratings, spanning 145 problems from six major math competitions (USAMO, IMO, Putnam, etc) and 435 LLM-generated solutions from Gemini-2.5-Pro, o3, and DeepSeek-R1. 
Using ProofBench as a testbed, we systematically explore the evaluator design space across key axes: the backbone model, input context, instructions and evaluation workflow.
Our analysis delivers ProofGrader, an evaluator that combines a strong reasoning backbone LM, rich context from reference solutions and marking schemes, and a simple ensembling method; it achieves a low Mean Absolute Error (MAE) of 0.926 against expert scores, significantly outperforming naive baselines.
Finally, we demonstrate its practical utility in a best-of-$n$ selection task: at $n=16$, ProofGrader achieves an average score of 4.14/7, closing 78\% of the gap between a naive binary evaluator (2.48) and the human oracle (4.62), highlighting its potential to advance downstream proof generation.

## Metadata
- venue: ICLR
- year: 2026
- authors: Wenjie Ma, Andrei Cojocaru, Neel Kolhe, Haihan Zhang, Vincent Zhuang, Matei Zaharia, Sewon Min
- arxiv_id: 
- openreview_id: ky5iqwZSXI
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9b622de8fbbd37c2317ba4b965bbfde1e3026ded.pdf
- published: 2026
- keywords: automated proof evaluation; LLM-as-a-judge; LLM-generated math proofs; rubric-guided grading; prompt optimization; expert-annotated proof dataset; evaluator reliability; reward modeling

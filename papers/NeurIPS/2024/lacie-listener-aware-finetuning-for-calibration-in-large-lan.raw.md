---
title: "LACIE: Listener-Aware Finetuning for Calibration in Large Language Models"
authors: ["Elias Stengel-Eskin", "Peter Hase", "Mohit Bansal"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "RnvgYd9RAh"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f8a8e27a01ca4571abfa7178680c07b0adb718e7.pdf"
published: "2024"
categories: []
keywords: ["LLM calibration", "uncertainty", "question answering", "pragmatics", "listener-speaker model", "LLM confidence estimation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:48+09:00"
---

# LACIE: Listener-Aware Finetuning for Calibration in Large Language Models

## Abstract
When answering questions, large language models (LLMs) can convey not only an answer to the question, but a level of confidence about the answer being correct. This includes explicit markers of confidence (e.g. giving a numeric confidence score) as well as implicit markers, like using an authoritative tone or elaborating with additional knowledge of a subject. For LLMs to be trustworthy sources of knowledge, the confidence they convey should match their actual expertise on a topic; however, this is currently not the case, with most models tending towards overconfidence. To calibrate both implicit and explicit confidence markers, we introduce a pragmatic, listener-aware finetuning method (LACIE) that directly models the listener, considering not only whether an answer is right, but whether it will be accepted by a listener. Specifically, we cast calibration as a preference optimization problem, creating data via a two-agent speaker-listener game, where a speaker model’s outputs are judged by a simulated listener. We then finetune three different LLMs (Mistral-7B, Llama3-8B, Llama3-70B) with LACIE, and show that the models resulting from this multi-agent optimization are better calibrated on TriviaQA with respect to a simulated listener. Crucially, these trends transfer to human listeners, helping them correctly predict model correctness: we conduct a human evaluation where annotators accept or reject an LLM’s answers to trivia questions, finding that training with LACIE results in 47% fewer incorrect answers being accepted while maintaining the same level of acceptance for correct answers. Furthermore, LACIE generalizes to another dataset, resulting in a large increase in truthfulness on TruthfulQA when trained on TriviaQA. Our analysis indicates that LACIE leads to a better separation in confidence between correct and incorrect examples. Qualitatively, we find that a LACIE-trained model hedges more when uncertain and adopts implicit cues to signal certainty when it is correct, such as using an authoritative tone or including details. Finally, finetuning with our listener- aware method leads to an emergent increase in model abstention (e.g. saying “I don’t know”) for answers that are likely to be wrong, trading recall for precision.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Elias Stengel-Eskin, Peter Hase, Mohit Bansal
- arxiv_id: 
- openreview_id: RnvgYd9RAh
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f8a8e27a01ca4571abfa7178680c07b0adb718e7.pdf
- published: 2024
- keywords: LLM calibration, uncertainty, question answering, pragmatics, listener-speaker model, LLM confidence estimation

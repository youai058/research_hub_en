---
title: "Context Clues: Evaluating Long Context Models for Clinical Prediction Tasks on EHR Data"
authors: ["Michael Wornow", "Suhana Bedi", "Miguel Angel Fuentes Hernandez", "Ethan Steinberg", "Jason Alan Fries", "Christopher Re", "Sanmi Koyejo", "Nigam Shah"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "zg3ec1TdAP"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b21eff6a613bf00fac9c545c0a6c7f2df1c9e5a0.pdf"
published: "2025"
categories: []
keywords: ["ehr", "foundation model", "long context", "clinical prediction making", "healthcare"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:18+09:00"
---

# Context Clues: Evaluating Long Context Models for Clinical Prediction Tasks on EHR Data

## Abstract
Foundation Models (FMs) trained on Electronic Health Records (EHRs) have achieved state-of-the-art results on numerous clinical prediction tasks. However, prior EHR FMs typically have context windows of $<$1k tokens, which prevents them from modeling full patient EHRs which can exceed 10k's of events. For making clinical predictions, both model performance and robustness to the unique properties of EHR data are crucial. Recent advancements in subquadratic long-context architectures (e.g. Mamba) offer a promising solution. However, their application to EHR data has not been well-studied. We address this gap by presenting the first systematic evaluation of the effect of context length on modeling EHR data. We find that longer context models improve predictive performance -- our Mamba-based model surpasses the prior state-of-the-art on 9/14 tasks on the EHRSHOT prediction benchmark. Additionally, we measure robustness to three unique, previously underexplored properties of EHR data: (1) the prevalence of ``copy-forwarded" diagnoses which create artificial token repetition in EHR sequences; (2) the irregular time intervals between EHR events which can lead to a wide range of timespans within a context window; and (3) the natural increase in disease complexity over time which makes later tokens in the EHR harder to predict than earlier ones. Stratifying our EHRSHOT results, we find that higher levels of each property correlate negatively with model performance (e.g., a 14% higher Brier loss between the least and most irregular patients), but that longer context models are more robust to more extreme levels of these properties. Our work highlights the potential for using long-context architectures to model EHR data, and offers a case study on how to identify and quantify new challenges in modeling sequential data motivated by domains outside of natural language. We release all of our model checkpoints and code.

## Metadata
- venue: ICLR
- year: 2025
- authors: Michael Wornow, Suhana Bedi, Miguel Angel Fuentes Hernandez, Ethan Steinberg, Jason Alan Fries, Christopher Re, Sanmi Koyejo, Nigam Shah
- arxiv_id: 
- openreview_id: zg3ec1TdAP
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b21eff6a613bf00fac9c545c0a6c7f2df1c9e5a0.pdf
- published: 2025
- keywords: ehr, foundation model, long context, clinical prediction making, healthcare

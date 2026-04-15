---
title: "Diagnosing Transformers: Illuminating Feature Spaces for Clinical Decision-Making"
authors: ["Aliyah R. Hsu", "Yeshwanth Cherapanamjeri", "Briton Park", "Tristan Naumann", "Anobel Odisho", "Bin Yu"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "k581sTMyPt"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/4396dc3858433d144c7809bad60e3be5f5a5ebae.pdf"
published: "2024"
categories: []
keywords: ["fine-tuning", "transformer-based language models", "feature analysis", "interpretation", "clinical classification"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:59+09:00"
---

# Diagnosing Transformers: Illuminating Feature Spaces for Clinical Decision-Making

## Abstract
Pre-trained transformers are often fine-tuned to aid clinical decision-making using limited clinical notes. Model interpretability is crucial, especially in high-stakes domains like medicine, to establish trust and ensure safety, which requires human engagement. We introduce SUFO, a systematic framework that enhances interpretability of fine-tuned transformer feature spaces. SUFO utilizes a range of analytic and visualization techniques, including Supervised probing, Unsupervised similarity analysis, Feature dynamics, and Outlier analysis to address key questions about model trust and interpretability (e.g. model suitability for a task, feature space evolution during fine-tuning, and interpretation of fine-tuned features and failure modes). We conduct a case study investigating the impact of pre-training data where we focus on real-world pathology classification tasks, and validate our findings on MedNLI. We evaluate five 110M-sized pre-trained transformer models, categorized into general-domain (BERT, TNLR), mixed-domain (BioBERT, Clinical BioBERT), and domain-specific (PubMedBERT) groups. Our SUFO analyses reveal that: (1) while PubMedBERT, the domain-specific model, contains valuable information for fine-tuning, it can overfit to minority classes when class imbalances exist. In contrast, mixed-domain models exhibit greater resistance to overfitting, suggesting potential improvements in domain-specific model robustness; (2) in-domain pre-training accelerates feature disambiguation during fine-tuning; and (3) feature spaces undergo significant sparsification during this process, enabling clinicians to identify common outlier modes among fine-tuned models as demonstrated in this paper. These findings showcase the utility of SUFO in enhancing trust and safety when using transformers in medicine, and we believe SUFO can aid practitioners in evaluating fine-tuned language models (LMs) for other applications in medicine and in more critical domains.

## Metadata
- venue: ICLR
- year: 2024
- authors: Aliyah R. Hsu, Yeshwanth Cherapanamjeri, Briton Park, Tristan Naumann, Anobel Odisho, Bin Yu
- arxiv_id: 
- openreview_id: k581sTMyPt
- anthology_id: 
- pdf_url: https://openreview.net/pdf/4396dc3858433d144c7809bad60e3be5f5a5ebae.pdf
- published: 2024
- keywords: fine-tuning, transformer-based language models, feature analysis, interpretation, clinical classification

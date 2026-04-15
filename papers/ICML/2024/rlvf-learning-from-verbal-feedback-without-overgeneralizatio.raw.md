---
title: "RLVF: Learning from Verbal Feedback without Overgeneralization"
authors: ["Moritz Pascal Stephan", "Alexander Khazatsky", "Eric Mitchell", "Annie S Chen", "Sheryl Hsu", "Archit Sharma", "Chelsea Finn"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ngcZhfXCBW"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/3eca80fa9e6241aa713fc70320a1221e314fa8c6.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:30+09:00"
---

# RLVF: Learning from Verbal Feedback without Overgeneralization

## Abstract
The diversity of contexts in which large language models (LLMs) are deployed requires the ability to modify or customize default model behaviors to incorporate nuanced requirements and preferences. A convenient interface to specify such model adjustments is high-level verbal feedback, such as “Don’t use emojis when drafting emails to my boss.” However, while writing high-level feedback is far simpler than collecting annotations for reinforcement learning from human feedback (RLHF), we find that simply prompting a model with such feedback leads to $\textbf{overgeneralization}$–applying feedback in contexts where it is not relevant. We propose a new method Contextualized Critiques with Constrained Preference Optimization (C3PO) to learn from high-level verbal feedback while reducing overgeneralization compared to current work. C3PO uses a piece of high-level feedback to generate a small synthetic preference dataset to specify when and how the feedback should (and should not) be applied. It then fine-tunes the model in accordance with the synthetic preference data while minimizing the divergence from the original model for prompts where the feedback does not apply. Our experimental results indicate that our approach effectively applies verbal feedback to relevant scenarios while preserving existing behaviors for other contexts more than current methods. For both human- and GPT-4-generated high-level feedback, C3PO effectively adheres to the given feedback comparably to in-context baselines while reducing overgeneralization by 30%.

## Metadata
- venue: ICML
- year: 2024
- authors: Moritz Pascal Stephan, Alexander Khazatsky, Eric Mitchell, Annie S Chen, Sheryl Hsu, Archit Sharma, Chelsea Finn
- arxiv_id: 
- openreview_id: ngcZhfXCBW
- anthology_id: 
- pdf_url: https://openreview.net/pdf/3eca80fa9e6241aa713fc70320a1221e314fa8c6.pdf
- published: 2024

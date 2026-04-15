---
title: "Provable Interactive Learning with Hindsight Instruction Feedback"
authors: ["Dipendra Misra", "Aldo Pacchiano", "Robert E. Schapire"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "CgO2cuWWLV"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0735abb7bf7cccff31f9eead95cfd02c4450334b.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:39+09:00"
---

# Provable Interactive Learning with Hindsight Instruction Feedback

## Abstract
We study interactive learning in a setting where the agent has to generate a response (e.g., an action or trajectory) given a context and an instruction. In contrast, to typical approaches that train the system using reward or expert supervision on response, we study _learning with hindsight labeling_ where a teacher provides an instruction that is most suitable for the agent's generated response. This hindsight labeling of instruction is often easier to provide than providing expert supervision of the optimal response which may require expert knowledge or can be impractical to elicit. We initiate the theoretical analysis of _interactive learning with hindsight labeling_. We first provide a lower bound showing that in general, the regret of any algorithm must scale with the size of the agent's response space. Next, we study a specialized setting where the underlying instruction-response distribution can be decomposed as a low-rank matrix. We introduce an algorithm called LORIL for this setting and show that it is a no-regret algorithm with the regret scaling with $\sqrt{T}$ and depends on the _intrinsic rank_ but does not depend on the agent's response space. We provide experiments showing the performance of LORIL in practice for 2 domains.

## Metadata
- venue: ICML
- year: 2024
- authors: Dipendra Misra, Aldo Pacchiano, Robert E. Schapire
- arxiv_id: 
- openreview_id: CgO2cuWWLV
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0735abb7bf7cccff31f9eead95cfd02c4450334b.pdf
- published: 2024

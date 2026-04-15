---
title: "Cycle Consistency Driven Object Discovery"
authors: ["Aniket Rajiv Didolkar", "Anirudh Goyal", "Yoshua Bengio"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "f1xnBr4WD6"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/18ace982ecbf580ad919f876edd9b3a6e1652550.pdf"
published: "2024"
categories: []
keywords: ["cycle consistency", "object discovery", "downstream RL"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:22+09:00"
---

# Cycle Consistency Driven Object Discovery

## Abstract
Developing deep learning models that effectively learn object-centric representations, akin to human cognition, remains a challenging task. Existing approaches facilitate object discovery by representing objects as fixed-size vectors, called ``slots'' or ``object files''. While these approaches have shown promise in certain scenarios, they still exhibit certain limitations. First, they rely on architectural priors which can be unreliable and usually require meticulous engineering to identify the correct objects. Second, there has been a notable gap in investigating the practical utility of these representations in downstream tasks. To address the first limitation, we introduce a method that explicitly optimizes the constraint that each object in a scene should be associated with a distinct slot. We formalize this constraint by introducing  consistency objectives which are cyclic in nature. By integrating these consistency objectives into various existing slot-based object-centric methods, we showcase substantial improvements in object-discovery performance. These enhancements consistently hold true across both synthetic and real-world scenes, underscoring the effectiveness and adaptability of the proposed approach. To tackle the second limitation, we apply the learned object-centric representations from the proposed method to two downstream reinforcement learning tasks, demonstrating considerable performance enhancements compared to conventional slot-based and monolithic representation learning methods. Our results suggest that the proposed approach not only improves object discovery, but also provides richer features for downstream tasks.

## Metadata
- venue: ICLR
- year: 2024
- authors: Aniket Rajiv Didolkar, Anirudh Goyal, Yoshua Bengio
- arxiv_id: 
- openreview_id: f1xnBr4WD6
- anthology_id: 
- pdf_url: https://openreview.net/pdf/18ace982ecbf580ad919f876edd9b3a6e1652550.pdf
- published: 2024
- keywords: cycle consistency, object discovery, downstream RL

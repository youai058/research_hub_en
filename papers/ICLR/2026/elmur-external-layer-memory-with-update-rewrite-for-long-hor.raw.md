---
title: "ELMUR: External Layer Memory with Update/Rewrite for Long-Horizon RL Problems"
authors: ["Egor Cherepanov", "Alexey Kovalev", "Aleksandr Panov"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "bm3rbtEMFj"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/41788012da634ffb97820032cc13784a4f6e18de.pdf"
published: "2026"
categories: []
keywords: ["RL", "POMDP", "Memory", "Transformer", "Robotics"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:23+09:00"
---

# ELMUR: External Layer Memory with Update/Rewrite for Long-Horizon RL Problems

## Abstract
Real-world robotic agents must act under partial observability and long horizons, where key cues may appear long before they affect decision making. However, most modern approaches rely solely on instantaneous information, without incorporating insights from the past. Standard recurrent or transformer models struggle with retaining and leveraging long-term dependencies: context windows truncate history, while naive memory extensions fail under scale and sparsity. 
We propose ELMUR (External Layer Memory with Update/Rewrite), a transformer architecture with structured external memory. Each layer maintains memory embeddings, interacts with them via bidirectional cross-attention, and updates them through an Least Recently Used (LRU) memory module using replacement or convex blending. 
ELMUR extends effective horizons up to 100,000 times beyond the attention window and achieves a 100% success rate on a synthetic T-Maze task with corridors up to one million steps. In POPGym, it outperforms baselines on more than half of the tasks. 
On MIKASA-Robo sparse-reward manipulation tasks with visual observations, it nearly doubles the performance of strong baselines, achieving the best success rate on 21 out of 23 tasks and improving the aggregate success rate across all tasks by about 70% over the previous best baseline.
These results demonstrate that structured, layer-local external memory offers a simple and scalable approach to decision making under partial observability.

## Metadata
- venue: ICLR
- year: 2026
- authors: Egor Cherepanov, Alexey Kovalev, Aleksandr Panov
- arxiv_id: 
- openreview_id: bm3rbtEMFj
- anthology_id: 
- pdf_url: https://openreview.net/pdf/41788012da634ffb97820032cc13784a4f6e18de.pdf
- published: 2026
- keywords: RL, POMDP, Memory, Transformer, Robotics

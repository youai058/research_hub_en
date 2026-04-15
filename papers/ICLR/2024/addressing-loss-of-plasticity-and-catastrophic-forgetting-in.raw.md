---
title: "Addressing Loss of Plasticity and Catastrophic Forgetting in Continual Learning"
authors: ["Mohamed Elsayed", "A. Rupam Mahmood"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "sKPzAXoylB"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/7eb81f1c1c4fea7fa434ebe26bbf3145d56b032f.pdf"
published: "2024"
categories: []
keywords: ["catastrophic forgetting", "loss of plasticity", "plasticity", "stability", "continual learning", "streaming learning", "online learning", "incremental learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:59+09:00"
---

# Addressing Loss of Plasticity and Catastrophic Forgetting in Continual Learning

## Abstract
Deep representation learning methods struggle with continual learning, suffering from both catastrophic forgetting of useful units and loss of plasticity, often due to rigid and unuseful units. While many methods address these two issues separately, only a few currently deal with both simultaneously. In this paper, we introduce Utility-based Perturbed Gradient Descent (UPGD) as a novel approach for the continual learning of representations. UPGD combines gradient updates with perturbations, where it applies smaller modifications to more useful units, protecting them from forgetting, and larger modifications to less useful units, rejuvenating their plasticity. We use a challenging streaming learning setup where continual learning problems have hundreds of non-stationarities and unknown task boundaries. We show that many existing methods suffer from at least one of the issues, predominantly manifested by their decreasing accuracy over tasks. On the other hand, UPGD continues to improve performance and surpasses or is competitive with all methods in all problems. Finally, in extended reinforcement learning experiments with PPO, we show that while Adam exhibits a performance drop after initial learning, UPGD avoids it by addressing both continual learning issues.

## Metadata
- venue: ICLR
- year: 2024
- authors: Mohamed Elsayed, A. Rupam Mahmood
- arxiv_id: 
- openreview_id: sKPzAXoylB
- anthology_id: 
- pdf_url: https://openreview.net/pdf/7eb81f1c1c4fea7fa434ebe26bbf3145d56b032f.pdf
- published: 2024
- keywords: catastrophic forgetting, loss of plasticity, plasticity, stability, continual learning, streaming learning, online learning, incremental learning

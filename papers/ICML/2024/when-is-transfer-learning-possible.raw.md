---
title: "When is Transfer Learning Possible?"
authors: ["My Phan", "Kianté Brantley", "Stephanie Milani", "Soroush Mehri", "Gokul Swamy", "Geoffrey J. Gordon"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "9yADTDHgGu"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/7d752dca6629c6052ff699ba3bbfbe4e34f94ee6.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:42+09:00"
---

# When is Transfer Learning Possible?

## Abstract
We present a general framework for transfer learning that is flexible enough to capture transfer in supervised, reinforcement, and imitation learning. Our framework enables new insights into the fundamental question of *when* we can successfully transfer learned information across problems. We model the learner as interacting with a sequence of problem instances, or *environments*, each of which is generated from a common structural causal model (SCM) by choosing the SCM's parameters from restricted sets. We derive a procedure that can propagate restrictions on SCM parameters through the SCM's graph structure to other parameters that we are trying to learn. The propagated restrictions then enable more efficient learning (i.e., transfer). By analyzing the procedure, we are able to challenge widely-held beliefs about transfer learning. First, we show that having *sparse* changes across environments is neither necessary nor sufficient for transfer. Second, we show an example where the common heuristic of *freezing* a layer in a network causes poor transfer performance. We then use our procedure to select a more refined set of parameters to freeze, leading to successful transfer learning.

## Metadata
- venue: ICML
- year: 2024
- authors: My Phan, Kianté Brantley, Stephanie Milani, Soroush Mehri, Gokul Swamy, Geoffrey J. Gordon
- arxiv_id: 
- openreview_id: 9yADTDHgGu
- anthology_id: 
- pdf_url: https://openreview.net/pdf/7d752dca6629c6052ff699ba3bbfbe4e34f94ee6.pdf
- published: 2024

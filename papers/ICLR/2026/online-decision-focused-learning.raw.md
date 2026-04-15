---
title: "Online Decision-Focused Learning"
authors: ["Aymeric Capitaine", "Maxime Haddouche", "Eric Moulines", "Michael I. Jordan", "Etienne Boursier", "Alain Oliviero Durmus"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "FJhtHBphCt"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0fc55727cecb9f7dd99ebcc14dcdcdceb2d0855b.pdf"
published: "2026"
categories: []
keywords: ["decision-focused learning", "integrated estimaton optimization", "predict-then-optimize", "online learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:39+09:00"
---

# Online Decision-Focused Learning

## Abstract
Decision-focused learning (DFL) is an increasingly popular paradigm for training predictive models whose outputs are used in decision-making tasks. Instead of merely optimizing for predictive accuracy, DFL trains models to directly minimize the loss associated with downstream decisions. However, existing studies focus solely on scenarios where a fixed batch of data is available and the objective function does not change over time. We instead investigate DFL in dynamic environments where the objective function and data distribution evolve over time. This setting is challenging for online learning because the objective function  has zero or undefined gradients, which prevents the use of standard first-order optimization methods, and is generally non-convex. To address these difficulties, we (i) regularize the objective to make it differentiable and (ii) use perturbation techniques along with a near-optimal oracle to overcome non-convexity. Combining those techniques yields two original online algorithms tailored for DFL, for which we establish respectively static and dynamic regret bounds. These are the first provable guarantees for the online decision-focused problem. Finally, we showcase the effectiveness of our algorithms on a knapsack experiment, where they outperform two standard benchmarks.

## Metadata
- venue: ICLR
- year: 2026
- authors: Aymeric Capitaine, Maxime Haddouche, Eric Moulines, Michael I. Jordan, Etienne Boursier, Alain Oliviero Durmus
- arxiv_id: 
- openreview_id: FJhtHBphCt
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0fc55727cecb9f7dd99ebcc14dcdcdceb2d0855b.pdf
- published: 2026
- keywords: decision-focused learning, integrated estimaton optimization, predict-then-optimize, online learning

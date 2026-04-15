---
title: "Use the Online Network If You Can: Towards Fast and Stable Reinforcement Learning"
authors: ["Ahmed Hendawy", "Henrik Metternich", "Théo Vincent", "Mahdi Kallel", "Jan Peters", "Carlo D'Eramo"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "rFLuaG9Yq6"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/5c0c123623b31f17a10faa1a52617cc73519ba06.pdf"
published: "2026"
categories: []
keywords: ["deep reinforcement learning", "q-learning", "actor-critic", "function approximation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:31+09:00"
---

# Use the Online Network If You Can: Towards Fast and Stable Reinforcement Learning

## Abstract
The use of target networks is a popular approach for estimating value functions in deep Reinforcement Learning (RL). While effective, the target network remains a compromise solution that preserves stability at the cost of slowly moving targets, thus delaying learning. Conversely, using the online network as a bootstrapped target is intuitively appealing, albeit well-known to lead to unstable learning. In this work, we aim to obtain the best out of both worlds by introducing a novel update rule that computes the target using the **MIN**imum estimate between the **T**arget and **O**nline network, giving rise to our method, **MINTO**. Through this simple, yet effective modification, we show that MINTO enables faster and stable value function learning, by mitigating the potential overestimation bias of using the online network for bootstrapping. Notably, MINTO can be seamlessly integrated into a wide range of value-based and actor-critic algorithms with a negligible cost. We evaluate MINTO extensively across diverse benchmarks, spanning online and offline RL, as well as discrete and continuous action spaces. Across all benchmarks, MINTO consistently improves performance, demonstrating its broad applicability and effectiveness.

## Metadata
- venue: ICLR
- year: 2026
- authors: Ahmed Hendawy, Henrik Metternich, Théo Vincent, Mahdi Kallel, Jan Peters, Carlo D'Eramo
- arxiv_id: 
- openreview_id: rFLuaG9Yq6
- anthology_id: 
- pdf_url: https://openreview.net/pdf/5c0c123623b31f17a10faa1a52617cc73519ba06.pdf
- published: 2026
- keywords: deep reinforcement learning, q-learning, actor-critic, function approximation

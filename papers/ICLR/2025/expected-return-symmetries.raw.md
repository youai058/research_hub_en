---
title: "Expected Return Symmetries"
authors: ["Darius Muglich", "Johannes Forkel", "Elise van der Pol", "Jakob Nicolaus Foerster"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "wFg0shwoRe"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/fb37f62e4840cb5b9cbabd10c3f21a9708e2b472.pdf"
published: "2025"
categories: []
keywords: ["multi-agent reinforcement learning", "zero-shot coordination"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:48+09:00"
---

# Expected Return Symmetries

## Abstract
Symmetry is an important inductive bias that can improve model robustness and generalization across many deep learning domains. In multi-agent settings, a priori known symmetries have been shown to address a fundamental coordination failure mode known as mutually incompatible symmetry breaking; e.g. in a game where two independent agents can choose to move "left" or "right", and where a reward of +1 or -1 is received when the agents choose the same action or different actions, respectively. However, the efficient and automatic discovery of environment symmetries, in particular for decentralized partially observable Markov decision processes, remains an open problem. Furthermore, environmental symmetry breaking constitutes only one type of coordination failure, which motivates the search for a more accessible and broader symmetry class. In this paper, we introduce such a broader group of previously unexplored symmetries, which we call expected return symmetries, which contains environment symmetries as a subgroup. We show that agents trained to be compatible under the group of expected return symmetries achieve better zero-shot coordination results than those using environment symmetries. As an additional benefit, our method makes minimal a priori assumptions about the structure of their environment and does not require access to ground truth symmetries.

## Metadata
- venue: ICLR
- year: 2025
- authors: Darius Muglich, Johannes Forkel, Elise van der Pol, Jakob Nicolaus Foerster
- arxiv_id: 
- openreview_id: wFg0shwoRe
- anthology_id: 
- pdf_url: https://openreview.net/pdf/fb37f62e4840cb5b9cbabd10c3f21a9708e2b472.pdf
- published: 2025
- keywords: multi-agent reinforcement learning, zero-shot coordination

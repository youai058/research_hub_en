---
title: "Demonstration-Regularized RL"
authors: ["Daniil Tiapkin", "Denis Belomestny", "Daniele Calandriello", "Eric Moulines", "Alexey Naumov", "Pierre Perrault", "Michal Valko", "Pierre Menard"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "lF2aip4Scn"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/7f93971543d7b1a26e607380315994e7f7ad3051.pdf"
published: "2024"
categories: []
keywords: ["reinforcement learning", "regularization in reinforcement leaning", "learning with demonstrations", "reinforcemenet learning with human feedback"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:51+09:00"
---

# Demonstration-Regularized RL

## Abstract
Incorporating expert demonstrations has empirically helped to improve the sample efficiency of reinforcement learning (RL). This paper quantifies theoretically to what extent this extra information reduces RL's sample complexity. In particular, we study the demonstration-regularized reinforcement learning framework that leverages the expert demonstrations by $\mathrm{KL}$-regularization for a policy learned by behavior cloning. Our findings reveal that using $N^{\mathrm{E}}$ expert demonstrations enables the identification of an optimal policy at a sample complexity of order $\widetilde{\mathcal{O}}(\mathrm{Poly}(S,A,H)/(\varepsilon^2 N^{\mathrm{E}}))$ in finite and $\widetilde{\mathcal{O}}(\mathrm{Poly}(d,H)/(\varepsilon^2 N^{\mathrm{E}}))$ in linear Markov decision processes, where $\varepsilon$is the target precision, $H$ the horizon, $A$ the number of action, $S$ the number of states in the finite case and $d$ the dimension of the feature space in the linear case. As a by-product, we provide tight convergence guarantees for the behavior cloning procedure under general assumptions on the policy classes. Additionally, we establish that demonstration-regularized methods are provably efficient for reinforcement learning from human feedback (RLHF). In this respect, we provide theoretical evidence showing the benefits of KL-regularization for RLHF  in tabular and linear MDPs. 
Interestingly, we avoid pessimism injection by employing computationally feasible regularization to handle reward estimation uncertainty, thus setting our approach apart from the prior works.

## Metadata
- venue: ICLR
- year: 2024
- authors: Daniil Tiapkin, Denis Belomestny, Daniele Calandriello, Eric Moulines, Alexey Naumov, Pierre Perrault, Michal Valko, Pierre Menard
- arxiv_id: 
- openreview_id: lF2aip4Scn
- anthology_id: 
- pdf_url: https://openreview.net/pdf/7f93971543d7b1a26e607380315994e7f7ad3051.pdf
- published: 2024
- keywords: reinforcement learning, regularization in reinforcement leaning, learning with demonstrations, reinforcemenet learning with human feedback

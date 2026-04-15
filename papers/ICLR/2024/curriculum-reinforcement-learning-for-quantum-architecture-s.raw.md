---
title: "Curriculum reinforcement learning for quantum architecture search under hardware errors"
authors: ["Yash J. Patel", "Akash Kundu", "Mateusz Ostaszewski", "Xavier Bonet-Monroig", "Vedran Dunjko", "Onur Danaci"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "rINBD8jPoP"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e6b75e0b94d3c31e7f0e5d1c7d11b4ccb1aca361.pdf"
published: "2024"
categories: []
keywords: ["Quantum Computing", "Reinforcement Learning", "Quantum Chemistry", "Quantum Architecture Search", "Optimization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:23+09:00"
---

# Curriculum reinforcement learning for quantum architecture search under hardware errors

## Abstract
The key challenge in the noisy intermediate-scale quantum era is finding useful circuits compatible with current device limitations.
Variational quantum algorithms (VQAs) offer a potential solution by fixing the circuit architecture and optimizing individual gate parameters in an external loop. However, parameter optimization can become intractable, and the overall performance of the algorithm depends heavily on the initially chosen circuit architecture. Several quantum architecture search (QAS) algorithms have been developed to design useful circuit architectures automatically. In the case of parameter optimization alone, noise effects have been observed to dramatically influence the performance of the optimizer and final outcomes, which is a key line of study. However, the effects of noise on the architecture search, which could be just as critical, are poorly understood. This work addresses this gap by introducing a curriculum-based reinforcement learning QAS (CRLQAS) algorithm designed to tackle challenges in realistic VQA deployment. The algorithm incorporates (i) a 3D architecture encoding and restrictions on environment dynamics to explore the search space of possible circuits efficiently, (ii) an episode halting scheme to steer the agent to find shorter circuits, and (iii) a novel variant of simultaneous perturbation stochastic approximation as an optimizer for faster convergence. To facilitate studies, we developed an optimized simulator for our algorithm, significantly improving computational efficiency in simulating noisy quantum circuits by employing the Pauli-transfer matrix formalism in the Pauli-Liouville basis. Numerical experiments focusing on quantum chemistry tasks demonstrate that CRLQAS outperforms existing QAS algorithms across several metrics in both noiseless and noisy environments.

## Metadata
- venue: ICLR
- year: 2024
- authors: Yash J. Patel, Akash Kundu, Mateusz Ostaszewski, Xavier Bonet-Monroig, Vedran Dunjko, Onur Danaci
- arxiv_id: 
- openreview_id: rINBD8jPoP
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e6b75e0b94d3c31e7f0e5d1c7d11b4ccb1aca361.pdf
- published: 2024
- keywords: Quantum Computing, Reinforcement Learning, Quantum Chemistry, Quantum Architecture Search, Optimization

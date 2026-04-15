---
title: "Gradual Optimization Learning for Conformational Energy Minimization"
authors: ["Artem Tsypin", "Leonid Anatolievich Ugadiarov", "Kuzma Khrabrov", "Alexander Telepov", "Egor Rumiantsev", "Alexey Skrynnik", "Aleksandr Panov", "Dmitry P. Vetrov", "Elena Tutubalina", "Artur Kadurin"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "FMMF1a9ifL"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/37b8c4267928b3f02b1f1f1c9df21956eb2c653c.pdf"
published: "2024"
categories: []
keywords: ["energy minimization", "conformational optimization", "geometry optimization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:52+09:00"
---

# Gradual Optimization Learning for Conformational Energy Minimization

## Abstract
Molecular conformation optimization is crucial to computer-aided drug discovery and materials design.
Traditional energy minimization techniques rely on iterative optimization methods that use molecular forces calculated by a physical simulator (oracle) as anti-gradients.
However, this is a computationally expensive approach that requires many interactions with a physical simulator.
One way to accelerate this procedure is to replace the physical simulator with a neural network.
Despite recent progress in neural networks for molecular conformation energy prediction, such models are prone to errors due to distribution shift, leading to inaccurate energy minimization.
We find that the quality of energy minimization with neural networks can be improved by providing optimization trajectories as additional training data.
Still, obtaining complete optimization trajectories demands a lot of additional computations.
To reduce the required additional data, we present the Gradual Optimization Learning Framework (GOLF) for energy minimization with neural networks.
The framework consists of an efficient data-collecting scheme and an external optimizer.
The external optimizer utilizes gradients from the energy prediction model to generate optimization trajectories, and the data-collecting scheme selects additional training data to be processed by the physical simulator. 
Our results demonstrate that the neural network trained with GOLF performs \textit{on par} with the oracle on a benchmark of diverse drug-like molecules using significantly less additional data.

## Metadata
- venue: ICLR
- year: 2024
- authors: Artem Tsypin, Leonid Anatolievich Ugadiarov, Kuzma Khrabrov, Alexander Telepov, Egor Rumiantsev, Alexey Skrynnik, Aleksandr Panov, Dmitry P. Vetrov, Elena Tutubalina, Artur Kadurin
- arxiv_id: 
- openreview_id: FMMF1a9ifL
- anthology_id: 
- pdf_url: https://openreview.net/pdf/37b8c4267928b3f02b1f1f1c9df21956eb2c653c.pdf
- published: 2024
- keywords: energy minimization, conformational optimization, geometry optimization

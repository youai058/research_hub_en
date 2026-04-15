---
title: "Dynamics of Supervised and Reinforcement Learning in the Non-Linear Perceptron"
authors: ["Christian Schmid", "James M Murray"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "doaJTihgIZ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/59eac6fb0a981866724855101ccb7e1ff6ce054a.pdf"
published: "2024"
categories: []
keywords: ["Learning Dynamics", "non-linear perceptron", "supervised learning", "reinforcement learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:34+09:00"
---

# Dynamics of Supervised and Reinforcement Learning in the Non-Linear Perceptron

## Abstract
The ability of a brain or a neural network to efficiently learn depends crucially on both the task structure and the learning rule.
Previous works have analyzed the dynamical equations describing learning in the relatively simplified context of the perceptron under assumptions of a student-teacher framework or a linearized output. 
While these assumptions have facilitated theoretical understanding, they have precluded a detailed understanding of the roles of the nonlinearity and input-data distribution in determining the learning dynamics, limiting the applicability of the theories to real biological or artificial neural networks.
Here, we use a stochastic-process approach to derive flow equations describing learning, applying this framework to the case of a nonlinear perceptron performing binary classification. 
We characterize the effects of the learning rule (supervised or reinforcement learning, SL/RL) and input-data distribution on the perceptron's learning curve and the forgetting curve as subsequent tasks are learned.
In particular, we find that the input-data noise differently affects the learning speed under SL vs. RL, as well as determines how quickly learning of a task is overwritten by subsequent learning. Additionally, we verify our approach with real data using the MNIST dataset.
This approach points a way toward analyzing learning dynamics for more-complex circuit architectures.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Christian Schmid, James M Murray
- arxiv_id: 
- openreview_id: doaJTihgIZ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/59eac6fb0a981866724855101ccb7e1ff6ce054a.pdf
- published: 2024
- keywords: Learning Dynamics, non-linear perceptron, supervised learning, reinforcement learning

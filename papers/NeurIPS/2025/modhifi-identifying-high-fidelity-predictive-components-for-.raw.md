---
title: "ModHiFi: Identifying High Fidelity predictive components for Model Modification"
authors: ["Dhruva Kashyap", "Chaitanya Murti", "Pranav K Nayak", "Tanay Narshana", "Chiranjib Bhattacharyya"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "lClK4uBxSG"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/540a7960e800d4bbd7de9a93e80daae00417007d.pdf"
published: "2025"
categories: []
keywords: ["Pruning", "Machine Unlearning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:21+09:00"
---

# ModHiFi: Identifying High Fidelity predictive components for Model Modification

## Abstract
Open weight models, which are ubiquitous, rarely provide access to their training data or loss function. This makes modifying such models for tasks such as pruning or unlearning, which are constrained by this unavailability, an active area of research. Existing techniques typically require gradients or ground-truth labels, rendering them infeasible in settings with limited computational resources.
In this work, we investigate the fundamental question of identifying components that are critical to the model's predictive performance, without access to either gradients or the loss function, and with only distributional access such as synthetic data. 
We theoretically demonstrate that the global error is linearly bounded by local reconstruction errors for Lipschitz-continuous networks such as CNNs and well-trained Transformers (which, contrary to existing literature, we find exhibit Lipschitz continuity).
This motivates using the locally reconstructive behavior of component subsets to quantify their global importance, via a metric that we term *Subset Fidelity*. 
In the uncorrelated features setting, selecting individual components based on their Subset Fidelity scores is optimal, which we utilize to propose **ModHiFi**, an algorithm for model modification that requires neither training data nor access to a loss function. 
**ModHiFi-P**, for structured pruning, achieves an 11\% speedup over the current state of the art on ImageNet models and competitive performance on language models. **ModHiFi-U**, for classwise unlearning, achieves complete unlearning on CIFAR-10 without fine-tuning and demonstrates competitive performance on Swin Transformers.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Dhruva Kashyap, Chaitanya Murti, Pranav K Nayak, Tanay Narshana, Chiranjib Bhattacharyya
- arxiv_id: 
- openreview_id: lClK4uBxSG
- anthology_id: 
- pdf_url: https://openreview.net/pdf/540a7960e800d4bbd7de9a93e80daae00417007d.pdf
- published: 2025
- keywords: Pruning, Machine Unlearning

---
title: "Solving New Tasks by Adapting Internet Video Knowledge"
authors: ["Calvin Luo", "Zilai Zeng", "Yilun Du", "Chen Sun"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "p01BR4njlY"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d63745d12848160974b823c4ca6436e20569bcd8.pdf"
published: "2025"
categories: []
keywords: ["Text-Conditioned Generalization", "Video Diffusion", "Adaptation", "Planning", "Policy Learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:01+09:00"
---

# Solving New Tasks by Adapting Internet Video Knowledge

## Abstract
Video generative models demonstrate great promise in robotics by serving as visual planners or as policy supervisors.  When pretrained on internet-scale data, such video models intimately understand alignment with natural language, and can thus facilitate generalization to novel downstream behavior through text-conditioning.  However, they may not be sensitive to the specificities of the particular environment the agent inhabits.  On the other hand, training video models on in-domain examples of robotic behavior naturally encodes environment-specific intricacies, but the scale of available demonstrations may not be sufficient to support generalization to unseen tasks via natural language specification.  In this work, we investigate different adaptation techniques that integrate in-domain information with large-scale pretrained video models, and explore the extent to which they enable novel text-conditioned generalization for robotic tasks, while also considering their independent data and resource considerations.  We successfully demonstrate across robotic environments that adapting powerful video models with small scales of example data can successfully facilitate generalization to novel behaviors.  In particular, we present a novel adaptation strategy, termed *Inverse Probabilistic Adaptation*, that not only consistently achieves strong generalization performance across robotic tasks and settings, but also exhibits robustness to the quality of adaptation data, successfully solving novel tasks even when only suboptimal in-domain demonstrations are available.

## Metadata
- venue: ICLR
- year: 2025
- authors: Calvin Luo, Zilai Zeng, Yilun Du, Chen Sun
- arxiv_id: 
- openreview_id: p01BR4njlY
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d63745d12848160974b823c4ca6436e20569bcd8.pdf
- published: 2025
- keywords: Text-Conditioned Generalization, Video Diffusion, Adaptation, Planning, Policy Learning

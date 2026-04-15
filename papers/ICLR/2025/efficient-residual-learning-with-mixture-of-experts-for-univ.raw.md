---
title: "Efficient Residual Learning with Mixture-of-Experts for Universal Dexterous Grasping"
authors: ["Ziye Huang", "Haoqi Yuan", "Yuhui Fu", "Zongqing Lu"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "BUj9VSCoET"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/801fe1621d182f06542cd8c64b197af44982eefe.pdf"
published: "2025"
categories: []
keywords: ["dexterous grasping", "residual policy learning", "reinforcement learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:48+09:00"
---

# Efficient Residual Learning with Mixture-of-Experts for Universal Dexterous Grasping

## Abstract
Universal dexterous grasping across diverse objects presents a fundamental yet formidable challenge in robot learning. Existing approaches using reinforcement learning (RL) to develop policies on extensive object datasets face critical limitations, including complex curriculum design for multi-task learning and limited generalization to unseen objects. 
To overcome these challenges, we introduce ResDex, a novel approach that integrates residual policy learning with a mixture-of-experts (MoE) framework. ResDex is distinguished by its use of geometry-agnostic base policies that are efficiently acquired on individual objects and capable of generalizing across a wide range of unseen objects. Our MoE framework incorporates several base policies to facilitate diverse grasping styles suitable for various objects. By learning residual actions alongside weights that combine these base policies, ResDex enables efficient multi-task RL for universal dexterous grasping.
ResDex achieves state-of-the-art performance on the DexGraspNet dataset comprising 3,200 objects with an 88.8% success rate. It exhibits no generalization gap with unseen objects and demonstrates superior training efficiency, mastering all tasks within only 12 hours on a single GPU. For further details and videos, visit our project page.

## Metadata
- venue: ICLR
- year: 2025
- authors: Ziye Huang, Haoqi Yuan, Yuhui Fu, Zongqing Lu
- arxiv_id: 
- openreview_id: BUj9VSCoET
- anthology_id: 
- pdf_url: https://openreview.net/pdf/801fe1621d182f06542cd8c64b197af44982eefe.pdf
- published: 2025
- keywords: dexterous grasping, residual policy learning, reinforcement learning

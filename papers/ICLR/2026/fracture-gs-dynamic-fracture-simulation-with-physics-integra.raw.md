---
title: "Fracture-GS: Dynamic Fracture Simulation with Physics-Integrated Gaussian Splatting"
authors: ["Xiaogang Wang", "Hongyu Wu", "Wenfeng Song", "Kai Xu"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "zcAwK50ft0"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/003495cbe40e10ee60de0f0d692afbf16028a737.pdf"
published: "2026"
categories: []
keywords: ["3D vision", "Physics-based Simulation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:13+09:00"
---

# Fracture-GS: Dynamic Fracture Simulation with Physics-Integrated Gaussian Splatting

## Abstract
This paper presents a unified framework for simulating and visualizing dynamic fracture phenomena in extreme mechanical collisions using multi-view image inputs. While existing methods primarily address elastic deformations at contact surfaces, they fail to capture the complex physics of extreme collisions, often producing non-physical artifacts and material adhesion at fracture interfaces. Our approach integrates two key innovations: (1) an enhanced Collision Material Point Method (Collision-MPM) with momentum-conserving interface forces derived from normalized mass distributions, which effectively eliminates unphysical adhesion in fractured solids; and (2) a fracture-aware 3D Gaussian continuum representation that enables physically plausible rendering without post-processing. The framework operates through three main stages: First, performing implicit reconstruction of collision objects from multi-view images while sampling both surface and internal particles and simultaneously learning surface particle Gaussian properties via splatting; Second, high-fidelity collision resolution using our improved Collision-MPM formulation; Third, dynamic fracture tracking with Gaussian attribute optimization for fracture surfaces rendering. Through comprehensive testing, our framework demonstrates significant improvements over existing methods in handling diverse scenarios, including homogeneous materials, heterogeneous composites, and complex multi-body collisions. The results confirm superior physical accuracy, while maintaining computational efficiency for rendering.

## Metadata
- venue: ICLR
- year: 2026
- authors: Xiaogang Wang, Hongyu Wu, Wenfeng Song, Kai Xu
- arxiv_id: 
- openreview_id: zcAwK50ft0
- anthology_id: 
- pdf_url: https://openreview.net/pdf/003495cbe40e10ee60de0f0d692afbf16028a737.pdf
- published: 2026
- keywords: 3D vision, Physics-based Simulation

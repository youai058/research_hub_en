---
title: "PolyhedronNet: Representation Learning for Polyhedra with Surface-attributed Graph"
authors: ["Dazhou Yu", "Genpei Zhang", "Liang Zhao"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "BpyHIrpUOL"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/102fcdb0c72f0df875e5652aa54f0525116052b3.pdf"
published: "2025"
categories: []
keywords: ["polygon", "polyhedron", "polygonal representation", "representation learning", "graph neural networks"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:01+09:00"
---

# PolyhedronNet: Representation Learning for Polyhedra with Surface-attributed Graph

## Abstract
Ubiquitous geometric objects can be precisely and efficiently represented as polyhedra. The transformation of a polyhedron into a vector, known as polyhedra representation learning, is crucial for manipulating these shapes with mathematical and statistical tools for tasks like classification, clustering, and generation. Recent years have witnessed significant strides in this domain, yet most efforts focus on the vertex sequence of a polyhedron, neglecting the complex surface modeling crucial in real-world polyhedral objects.
This study proposes \textbf{PolyhedronNet}, a general framework tailored for learning representations of 3D polyhedral objects.  We propose the concept of the surface-attributed graph to seamlessly model the vertices, edges, faces, and their geometric interrelationships within a polyhedron. 
To effectively learn the representation of the entire surface-attributed graph, we first propose to break it down into local rigid representations to effectively learn each local region's relative positions against the remaining regions without geometric information loss. Subsequently, we propose PolyhedronGNN to hierarchically aggregate the local rigid representation via intra-face and inter-face geometric message passing modules, to obtain a global representation that minimizes information loss while maintaining rotation and translation invariance.
Our experimental evaluations on four distinct datasets, encompassing both classification and retrieval tasks, substantiate PolyhedronNet's efficacy in capturing comprehensive and informative representations of 3D polyhedral objects.

## Metadata
- venue: ICLR
- year: 2025
- authors: Dazhou Yu, Genpei Zhang, Liang Zhao
- arxiv_id: 
- openreview_id: BpyHIrpUOL
- anthology_id: 
- pdf_url: https://openreview.net/pdf/102fcdb0c72f0df875e5652aa54f0525116052b3.pdf
- published: 2025
- keywords: polygon, polyhedron, polygonal representation, representation learning, graph neural networks

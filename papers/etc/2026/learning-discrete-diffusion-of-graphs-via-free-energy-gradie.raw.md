---
title: "Learning Discrete Diffusion of Graphs via Free-Energy Gradient Flows"
authors: ["Dario Rancati", "Jan Maas", "Francesco Locatello"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2604.11311"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2604.11311v1"
published: "2026-04-13"
categories: ["cs.LG", "stat.ML"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:24+09:00"
---

# Learning Discrete Diffusion of Graphs via Free-Energy Gradient Flows

## Abstract
Diffusion-based models on continuous spaces have seen substantial recent progress through the mathematical framework of gradient flows, leveraging the Wasserstein-2 (${W}_2$) metric via the Jordan-Kinderlehrer-Otto (JKO) scheme. Despite the increasing popularity of diffusion models on discrete spaces using continuous-time Markov chains, a parallel theoretical framework based on gradient flows has remained elusive due to intrinsic challenges in translating the ${W}_2$ distance directly into these settings. In this work, we propose the first computational approach addressing these challenges, leveraging an appropriate metric $W_K$ on the simplex of probability distributions, which enables us to interpret widely used discrete diffusion paths, such as the discrete heat equation, as gradient flows of specific free-energy functionals. Through this theoretical insight, we introduce a novel methodology for learning diffusion dynamics over discrete spaces, which recovers the underlying functional directly by leveraging first-order optimality conditions for the JKO scheme. The resulting method optimizes a simple quadratic loss, trains extremely fast, does not require individual sample trajectories, and only needs a numerical preprocessing computing $W_K$-geodesics. We validate our method through extensive numerical experiments on synthetic data, showing that we can recover the underlying functional for a variety of graph classes.

## Metadata
- venue: arXiv
- year: 2026
- authors: Dario Rancati, Jan Maas, Francesco Locatello
- arxiv_id: 2604.11311
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2604.11311v1
- published: 2026-04-13

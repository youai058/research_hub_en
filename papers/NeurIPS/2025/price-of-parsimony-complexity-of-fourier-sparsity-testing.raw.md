---
title: "Price of Parsimony: Complexity of Fourier Sparsity Testing"
authors: ["Arijit Ghosh", "Manmatha Roy"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "7bCPXHq8xV"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/acde65a135343c43d2f68964699708ec70bfe426.pdf"
published: "2025"
categories: []
keywords: ["Fourier Sparsity", "Boolean Function", "Fourier Analysis", "Computational Learning Theory", "Property Testing"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:34+09:00"
---

# Price of Parsimony: Complexity of Fourier Sparsity Testing

## Abstract
A function \( f : \mathbb{F}_2^n \to \mathbb{R} \) is said to be \( s \)-Fourier sparse if its Fourier expansion contains at most \( s \) nonzero coefficients. In general, the existence of a sparse representation in the Fourier basis serves as a key enabler for the design of efficient learning algorithms. However, most existing techniques assume prior knowledge of the function’s Fourier sparsity, with algorithmic parameters carefully tuned to this value. This motivates the following decision problem: given \( s > 0 \), determine whether a function is \( s \)-Fourier sparse.

In this work, we study the problem of tolerant testing of Fourier Sparsity for real-valued functions over \( \mathbb{F}_2^n \), accessed via oracle queries. The goal is to decide whether a given function is close to being \( s \)-Fourier sparse or far from every \( s \)-Fourier sparse function. Our algorithm provides an estimator that, given oracle access to the function, estimates its distance to the nearest \( s \)-Fourier sparse function with query complexity \( \widetilde{O}(s) \), for constant accuracy and confidence parameters.

A key structural ingredient in our analysis is a new spectral concentration result for real-valued functions over \( \mathbb{F}_2^n \) when restricted to small-dimensional random affine subspaces. We further complement our upper bound with a matching lower bound of \( \Omega(s) \), establishing that our tester is optimal up to logarithmic factors. The lower bound exploits spectral properties of a class of cryptographically hard functions, namely, the Maiorana--McFarland family, in a novel way.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Arijit Ghosh, Manmatha Roy
- arxiv_id: 
- openreview_id: 7bCPXHq8xV
- anthology_id: 
- pdf_url: https://openreview.net/pdf/acde65a135343c43d2f68964699708ec70bfe426.pdf
- published: 2025
- keywords: Fourier Sparsity, Boolean Function, Fourier Analysis, Computational Learning Theory, Property Testing

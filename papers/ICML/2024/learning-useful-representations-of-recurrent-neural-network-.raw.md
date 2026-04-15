---
title: "Learning Useful Representations of Recurrent Neural Network Weight Matrices"
authors: ["Vincent Herrmann", "Francesco Faccio", "Jürgen Schmidhuber"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "QBj7Uurdwf"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/abdd59b9022e26fa87966eb021c1a9debc4b9662.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:47+09:00"
---

# Learning Useful Representations of Recurrent Neural Network Weight Matrices

## Abstract
Recurrent Neural Networks (RNNs) are general-purpose parallel-sequential computers. The program of an RNN is its weight matrix. How to learn useful representations of RNN weights that facilitate RNN analysis as well as downstream tasks? While the _mechanistic approach_ directly looks at some RNN's weights to predict its behavior, the _functionalist approach_ analyzes its overall functionality–specifically, its input-output mapping. We consider several mechanistic approaches for RNN weights and adapt the permutation equivariant Deep Weight Space layer for RNNs. Our two novel functionalist approaches extract information from RNN weights by 'interrogating' the RNN through probing inputs. We develop a theoretical framework that demonstrates conditions under which the functionalist approach can generate rich representations that help determine RNN behavior. We create and release the first two 'model zoo' datasets for RNN weight representation learning. One consists of generative models of a class of formal languages, and the other one of classifiers of sequentially processed MNIST digits. With the help of an emulation-based self-supervised learning technique we compare and evaluate the different RNN weight encoding techniques on multiple downstream applications. On the most challenging one, namely predicting which exact task the RNN was trained on, functionalist approaches show clear superiority.

## Metadata
- venue: ICML
- year: 2024
- authors: Vincent Herrmann, Francesco Faccio, Jürgen Schmidhuber
- arxiv_id: 
- openreview_id: QBj7Uurdwf
- anthology_id: 
- pdf_url: https://openreview.net/pdf/abdd59b9022e26fa87966eb021c1a9debc4b9662.pdf
- published: 2024

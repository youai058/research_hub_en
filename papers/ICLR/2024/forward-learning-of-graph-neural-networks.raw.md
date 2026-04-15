---
title: "Forward Learning of Graph Neural Networks"
authors: ["Namyong Park", "Xing Wang", "Antoine Simoulin", "Shuai Yang", "Grey Yang", "Ryan A. Rossi", "Puja Trivedi", "Nesreen K. Ahmed"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Abr7dU98ME"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/78ce77aec3cb18418df9c216e801999677415163.pdf"
published: "2024"
categories: []
keywords: ["graph neural networks", "forward learning", "forward-forward algorithm"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:23+09:00"
---

# Forward Learning of Graph Neural Networks

## Abstract
Graph neural networks (GNNs) have achieved remarkable success across a wide range of applications, such as recommendation, drug discovery, and question answering. Behind the success of GNNs lies the backpropagation (BP) algorithm, which is the de facto standard for training deep neural networks (NNs). However, despite its effectiveness, BP imposes several constraints, which are not only biologically implausible, but also limit the scalability, parallelism, and flexibility in learning NNs. Examples of such constraints include storage of neural activities computed in the forward pass for use in the subsequent backward pass, and the dependence of parameter updates on non-local signals. To address these limitations, the forward-forward algorithm (FF) was recently proposed as an alternative to BP in the image classification domain, which trains NNs by performing two forward passes over positive and negative data. Inspired by this advance, we propose ForwardGNN in this work, a new forward learning procedure for GNNs, which avoids the constraints imposed by BP via an effective layer-wise local forward training. ForwardGNN extends the original FF to deal with graph data and GNNs, and makes it possible to operate without generating negative inputs (hence no longer forward-forward). Further, ForwardGNN enables each layer to learn from both the bottom-up and top-down signals without relying on the backpropagation of errors. Extensive experiments on real-world datasets show the effectiveness and generality of the proposed forward graph learning framework. We release our code at https://github.com/facebookresearch/forwardgnn.

## Metadata
- venue: ICLR
- year: 2024
- authors: Namyong Park, Xing Wang, Antoine Simoulin, Shuai Yang, Grey Yang, Ryan A. Rossi, Puja Trivedi, Nesreen K. Ahmed
- arxiv_id: 
- openreview_id: Abr7dU98ME
- anthology_id: 
- pdf_url: https://openreview.net/pdf/78ce77aec3cb18418df9c216e801999677415163.pdf
- published: 2024
- keywords: graph neural networks, forward learning, forward-forward algorithm

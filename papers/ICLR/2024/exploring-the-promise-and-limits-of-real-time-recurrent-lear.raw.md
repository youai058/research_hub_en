---
title: "Exploring the Promise and Limits of Real-Time Recurrent Learning"
authors: ["Kazuki Irie", "Anand Gopalakrishnan", "Jürgen Schmidhuber"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "V2cBKtdC3a"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9107e97b85399a8a37e9379bb2cdb2ef3e226b56.pdf"
published: "2024"
categories: []
keywords: ["recurrent neural networks", "real-time recurrent learning", "online recurrent learning", "reinforcement learning", "actor-critic", "policy gradients"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:10+09:00"
---

# Exploring the Promise and Limits of Real-Time Recurrent Learning

## Abstract
Real-time recurrent learning (RTRL) for sequence-processing recurrent neural networks (RNNs) offers certain conceptual advantages over backpropagation through time (BPTT). RTRL requires neither caching past activations nor truncating context, and enables online learning. However, RTRL's time and space complexity make it impractical. To overcome this problem, most recent work on RTRL focuses on approximation theories, while experiments are often limited to diagnostic settings. Here we explore the practical promise of RTRL in more realistic settings. We study actor-critic methods that combine RTRL and policy gradients, and test them in several subsets of DMLab-30, ProcGen, and Atari-2600 environments. On DMLab memory tasks, our system trained on fewer than 1.2B environmental frames is competitive with or outperforms well-known IMPALA and R2D2 baselines trained on 10B frames. To scale to such challenging tasks, we focus on certain well-known neural architectures with element-wise recurrence, allowing for tractable RTRL without approximation. Importantly, we also discuss rarely addressed limitations of RTRL in real-world applications, such as its complexity in the multi-layer case.

## Metadata
- venue: ICLR
- year: 2024
- authors: Kazuki Irie, Anand Gopalakrishnan, Jürgen Schmidhuber
- arxiv_id: 
- openreview_id: V2cBKtdC3a
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9107e97b85399a8a37e9379bb2cdb2ef3e226b56.pdf
- published: 2024
- keywords: recurrent neural networks, real-time recurrent learning, online recurrent learning, reinforcement learning, actor-critic, policy gradients

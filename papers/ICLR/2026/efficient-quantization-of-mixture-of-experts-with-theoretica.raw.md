---
title: "Efficient Quantization of Mixture-of-Experts with Theoretical Generalization Guarantees"
authors: ["Mohammed Nowaz Rabbani Chowdhury", "Kaoutar El Maghraoui", "Hsinyu Tsai", "Naigang Wang", "Geoffrey W. Burr", "Liu Liu", "Meng Wang"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "yiMlVBAoQi"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/dd52b79450b90e19483ff245a69f11e72dfe55c0.pdf"
published: "2026"
categories: []
keywords: ["Mixture-of-Experts", "Quantization", "Theoretical Generalization Guarantees"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:41+09:00"
---

# Efficient Quantization of Mixture-of-Experts with Theoretical Generalization Guarantees

## Abstract
Sparse Mixture-of-Experts (MoE) allows scaling of language and vision models efficiently by activating only a small subset of experts per input. While this reduces computation, the large number of parameters still incurs substantial memory overhead during inference. Post-training quantization has been explored to address this issue. Because uniform quantization suffers from significant accuracy loss at low bit-widths, mixed-precision methods have been recently explored; however, they often require substantial computation for bit-width allocation and overlook the varying sensitivity of model performance to the quantization of different experts. We propose a theoretically grounded expert-wise mixed-precision strategy that assigns bit-width to each expert primarily based on their *change in router’s* $l_2$ *norm* during training. Experts with smaller changes are shown to capture less frequent but critical features, and model performance is more sensitive to the quantization of these experts, thus requiring higher precision. Furthermore, to avoid allocating experts to lower precision that inject high quantization noise, experts with large *maximum intra-neuron variance* are also allocated higher precision. Experiments on large-scale MoE models, including Switch Transformer and Mixtral, show that our method achieves higher accuracy than existing approaches, while also reducing inference cost and incurring only negligible overhead for bit-width assignment.

## Metadata
- venue: ICLR
- year: 2026
- authors: Mohammed Nowaz Rabbani Chowdhury, Kaoutar El Maghraoui, Hsinyu Tsai, Naigang Wang, Geoffrey W. Burr, Liu Liu, Meng Wang
- arxiv_id: 
- openreview_id: yiMlVBAoQi
- anthology_id: 
- pdf_url: https://openreview.net/pdf/dd52b79450b90e19483ff245a69f11e72dfe55c0.pdf
- published: 2026
- keywords: Mixture-of-Experts, Quantization, Theoretical Generalization Guarantees

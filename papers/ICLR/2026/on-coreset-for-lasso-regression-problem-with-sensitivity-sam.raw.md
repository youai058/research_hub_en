---
title: "On Coreset for LASSO Regression Problem with Sensitivity Sampling"
authors: ["YuanBin Zou", "Junyu Huang", "Jianxin Wang", "Qilong Feng"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "aUlHK31TAz"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f0ee7a6ba471c6ff1cce90e17a45a711e77ac02a.pdf"
published: "2026"
categories: []
keywords: ["LASSO regression", "sampling algorithm"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:44+09:00"
---

# On Coreset for LASSO Regression Problem with Sensitivity Sampling

## Abstract
In this paper, we study coreset construction for LASSO regression, where a coreset is a small, weighted subset of the data that approximates the original problem with provable guarantees. For unregularized regression problems, sensitivity sampling is a successful and widely applied technique for constructing coresets. However, extending these methods to LASSO typically requires coreset size to scale with O(\mathcal{G}d), where d is the VC dimension and \mathcal{G} is the total sensitivity, following existing generalization bounds. A key challenge in improving upon this general bound lies in the difficulty of capturing the sparse and localized structure of the function space induced by the \ell_1 penalty in LASSO objective. To address this, we first provide an empirical process-based method of sensitivity sampling for LASSO, localizing the procedure by decomposing the functional space into separate components, which leads to tighter estimation error. By carefully leveraging the geometric properties of these localized spaces, we establish tight empirical process bounds on the required coreset size. These techniques enable us to achieve a coreset of size \tilde{O}(\epsilon^{-2}d\cdot(\log^3 d\cdot\min\{1,\log d/\lambda^2\}+\log(1/\delta))), which ensures a  (1\pm\epsilon)-approximation for any \epsilon,\delta\in(0,1) and \lambda > 0. Furthermore, we give a lower bound showing that any algorithm achieving a (1+\epsilon)-approximation must select at least $Omega(\frac{d\log{d}}{\epsilon^2}) rows in the regime where \lambda=O(d^{-1/2}). Empirical experiments show that our proposed algorithm is at least 4 times faster than the existing LASSO solver and more than 9 times faster on half of the datasets, while ensuring high solution quality and sparsity.

## Metadata
- venue: ICLR
- year: 2026
- authors: YuanBin Zou, Junyu Huang, Jianxin Wang, Qilong Feng
- arxiv_id: 
- openreview_id: aUlHK31TAz
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f0ee7a6ba471c6ff1cce90e17a45a711e77ac02a.pdf
- published: 2026
- keywords: LASSO regression, sampling algorithm

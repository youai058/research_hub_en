---
title: "Optimal bounds for $\\ell_p$ sensitivity sampling via $\\ell_2$ augmentation"
authors: ["Alexander Munteanu", "Simon Omlor"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ohH3sbUue2"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f1a75e5a8558f0fca82ccfd29490e03b356fe420.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:48+09:00"
---

# Optimal bounds for $\ell_p$ sensitivity sampling via $\ell_2$ augmentation

## Abstract
Data subsampling is one of the most natural methods to approximate a massively large data set by a small representative proxy. In particular, sensitivity sampling received a lot of attention, which samples points proportional to an individual importance measure called sensitivity. This framework reduces in very general settings the size of data to roughly the VC dimension $d$ times the total sensitivity $\mathfrak S$ while providing strong $(1\pm\varepsilon)$ guarantees on the quality of approximation. The recent work of Woodruff & Yasuda (2023c) improved substantially over the general $\tilde O(\varepsilon^{-2}\mathfrak Sd)$ bound for the important problem of $\ell_p$ subspace embeddings to $\tilde O(\varepsilon^{-2}\mathfrak S^{2/p})$ for $p\in[1,2]$. Their result was subsumed by an earlier $\tilde O(\varepsilon^{-2}\mathfrak Sd^{1-p/2})$ bound which was implicitly given in the work of Chen & Derezinski (2021). We show that their result is tight when sampling according to plain $\ell_p$ sensitivities. We observe that by augmenting the $\ell_p$ sensitivities by $\ell_2$ sensitivities, we obtain better bounds improving over the aforementioned results to optimal linear $\tilde O(\varepsilon^{-2}(\mathfrak S+d)) = \tilde O(\varepsilon^{-2}d)$ sampling complexity for all $p \in [1,2]$. In particular, this resolves an open question of Woodruff & Yasuda (2023c) in the affirmative for $p \in [1,2]$ and brings sensitivity subsampling into the regime that was previously only known to be possible using Lewis weights (Cohen & Peng, 2015). As an application of our main result, we also obtain an $\tilde O(\varepsilon^{-2}\mu d)$ sensitivity sampling bound for logistic regression, where $\mu$ is a natural complexity measure for this problem. This improves over the previous $\tilde O(\varepsilon^{-2}\mu^2 d)$ bound of Mai et al. (2021) which was based on Lewis weights subsampling.

## Metadata
- venue: ICML
- year: 2024
- authors: Alexander Munteanu, Simon Omlor
- arxiv_id: 
- openreview_id: ohH3sbUue2
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f1a75e5a8558f0fca82ccfd29490e03b356fe420.pdf
- published: 2024

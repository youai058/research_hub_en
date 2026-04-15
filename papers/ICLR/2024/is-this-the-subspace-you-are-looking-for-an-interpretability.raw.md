---
title: "Is This the Subspace You Are Looking for? An Interpretability Illusion for Subspace Activation Patching"
authors: ["Aleksandar Makelov", "Georg Lange", "Atticus Geiger", "Neel Nanda"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Ebt7JgMHv1"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/41767a08ea94dbfa362b4807a25ed21035e4dc0e.pdf"
published: "2024"
categories: []
keywords: ["Mechanistic Interpretability", "Natural Language Processing", "Large Language Models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:50+09:00"
---

# Is This the Subspace You Are Looking for? An Interpretability Illusion for Subspace Activation Patching

## Abstract
Mechanistic interpretability aims to attribute high-level model behaviors to specific, interpretable learned features. It is hypothesized that these features manifest as directions or low-dimensional subspaces within activation space. Accordingly, recent studies have explored the identification and manipulation of such subspaces to reverse-engineer computations, employing methods such as activation patching. In this work, we demonstrate that naïve approaches to subspace interventions can give rise to interpretability illusions.

Specifically, even if patching along a subspace has the intended end-to-end causal effect on model behavior, this effect may be achieved by activating \emph{a dormant parallel pathway} using a component that is \textit{causally disconnected} from the model output.
We demonstrate this in a mathematical example, realize the example empirically in two different settings (the Indirect Object Identification (IOI) task and factual recall), and argue that activating dormant pathways ought to be prevalent in practice.
In the context of factual recall, we further show that the illusion is related to rank-1 fact editing, providing a mechanistic explanation for previous work observing an inconsistency between fact editing performance and fact localisation.

However, this does not imply that activation patching of subspaces is intrinsically unfit for interpretability.
To contextualize our findings, we also show what a success case looks like in a task (IOI) where prior manual circuit analysis allows an understanding of the location of the ground truth feature. We explore the additional evidence needed to argue that a patched subspace is faithful.

## Metadata
- venue: ICLR
- year: 2024
- authors: Aleksandar Makelov, Georg Lange, Atticus Geiger, Neel Nanda
- arxiv_id: 
- openreview_id: Ebt7JgMHv1
- anthology_id: 
- pdf_url: https://openreview.net/pdf/41767a08ea94dbfa362b4807a25ed21035e4dc0e.pdf
- published: 2024
- keywords: Mechanistic Interpretability, Natural Language Processing, Large Language Models

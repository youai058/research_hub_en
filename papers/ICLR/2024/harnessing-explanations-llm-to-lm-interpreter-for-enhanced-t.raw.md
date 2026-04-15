---
title: "Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning"
authors: ["Xiaoxin He", "Xavier Bresson", "Thomas Laurent", "Adam Perold", "Yann LeCun", "Bryan Hooi"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "RXFVcynVe1"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0db04867c257dc081f5a8f03268da344deb07417.pdf"
published: "2024"
categories: []
keywords: ["large language models (LLM)", "feature learning", "text attributed graphs (TAG)", "graph neural networks (GNN)"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:00+09:00"
---

# Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning

## Abstract
Representation learning on text-attributed graphs (TAGs) has become a critical research problem in recent years. A typical example of a TAG is a paper citation graph, where the text of each paper serves as node attributes. Initial graph neural network (GNN) pipelines handled these text attributes by transforming them into shallow or hand-crafted features, such as skip-gram or bag-of-words features. Recent efforts have focused on enhancing these pipelines with language models (LMs), which typically demand intricate designs and substantial computational resources. With the advent of powerful large language models (LLMs) such as GPT or Llama2, which demonstrate an ability to reason and to utilize general knowledge, there is a growing need for techniques which combine the textual modelling abilities of LLMs with the structural learning capabilities of GNNs. Hence, in this work, we focus on leveraging LLMs to capture textual information as features, which can be used to boost GNN performance on downstream tasks. A key innovation is our use of \emph{explanations as features}: we prompt an LLM to perform zero-shot classification, request textual explanations for its decision-making process, and design an \emph{LLM-to-LM interpreter} to translate these explanations into informative features for downstream GNNs. Our experiments demonstrate that our method achieves state-of-the-art results on well-established TAG datasets, including \texttt{Cora}, \texttt{PubMed}, \texttt{ogbn-arxiv}, as well as our newly introduced dataset, \texttt{tape-arxiv23}. Furthermore, our method significantly speeds up training, achieving a 2.88 times improvement over the closest baseline on \texttt{ogbn-arxiv}. Lastly, we believe the versatility of the proposed method extends beyond TAGs and holds the potential to enhance other tasks involving graph-text data~\footnote{Our codes and datasets are available at: \url{https://github.com/XiaoxinHe/TAPE}}.

## Metadata
- venue: ICLR
- year: 2024
- authors: Xiaoxin He, Xavier Bresson, Thomas Laurent, Adam Perold, Yann LeCun, Bryan Hooi
- arxiv_id: 
- openreview_id: RXFVcynVe1
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0db04867c257dc081f5a8f03268da344deb07417.pdf
- published: 2024
- keywords: large language models (LLM), feature learning, text attributed graphs (TAG), graph neural networks (GNN)

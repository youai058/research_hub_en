---
title: "Detecting Bugs with Substantial Monetary Consequences by LLM and Rule-based Reasoning"
authors: ["Brian Zhang", "ZHUO ZHANG"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "hB5NkiET32"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/4051fe5c591c77d847d282e106761fe3f02e5522.pdf"
published: "2024"
categories: []
keywords: ["LLM", "rule based reasoning", "smart contract", "accounting bugs"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:44+09:00"
---

# Detecting Bugs with Substantial Monetary Consequences by LLM and Rule-based Reasoning

## Abstract
Financial transactions are increasingly being handled by automated programs called *smart contracts*. 
However, one challenge in the adaptation of smart contracts is the presence of vulnerabilities, which can cause significant monetary loss.
In  2024, $247.88 M was lost in 20 smart contract exploits.
According to a recent study, accounting bugs (i.e., incorrect implementations of domain-specific financial models) are the most prevalent type of vulnerability, 
and are one of the most difficult to find, requiring substantial human efforts.
While Large Language Models (LLMs) have shown promise in identifying these bugs, they often suffer from lack of generalization of vulnerability types, hallucinations, and problems with representing smart contracts in limited token context space.
This paper proposes a hybrid system combining LLMs and rule-based reasoning to detect accounting error vulnerabilities in smart contracts. 
In particular, it utilizes the understanding capabilities of LLMs to annotate the financial meaning of variables in smart contracts, and employs rule-based reasoning to propagate the information throughout a contract's logic and to validate potential vulnerabilities.
To remedy hallucinations, we propose a feedback loop where validation is performed by providing the reasoning trace of vulnerabilities to the LLM for iterative self-reflection. 
We achieve 75.6% accuracy on the labelling of financial meanings against human annotations. 
Furthermore, we achieve a recall of 90.5% from running on 23 real-world smart contract projects containing 21 accounting error vulnerabilities.
Finally, we apply the automated technique on 8 recent projects, finding 4 known and 2 unknown bugs.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Brian Zhang, ZHUO ZHANG
- arxiv_id: 
- openreview_id: hB5NkiET32
- anthology_id: 
- pdf_url: https://openreview.net/pdf/4051fe5c591c77d847d282e106761fe3f02e5522.pdf
- published: 2024
- keywords: LLM, rule based reasoning, smart contract, accounting bugs

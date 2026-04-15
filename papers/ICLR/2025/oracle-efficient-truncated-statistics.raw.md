---
title: "Oracle efficient truncated statistics"
authors: ["Konstantinos Karatapanis", "Vasilis Kontonis", "Christos Tzamos"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ZS7UEI3vG5"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/723e0e1485099706494f7e2b4c2ca51824b4950a.pdf"
published: "2025"
categories: []
keywords: ["truncated statistics", "exponential family", "statistical learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:45+09:00"
---

# Oracle efficient truncated statistics

## Abstract
We study the problem of learning from truncated samples: instead of observing
samples from some underlying population $p^\ast$, we observe only the examples that fall in some survival set $S \subset \mathbb{R}^d$ whose probability mass (measured with respect to $p^\ast$) is at least $\alpha$.  Assuming membership oracle access to the truncation set $S$, prior works obtained algorithms for the case where $p^\ast$ is Gaussian or more generally an exponential family with strongly convex likelihood --- albeit with a super-polynomial 
dependency on the (inverse) survival mass $1/\alpha$
both in terms of runtime and in number of oracle calls to the set $S$.  In this work we design a new learning method with runtime and query complexity polynomial in $1/\alpha$.  
Our result significantly improves over the prior works 
by focusing on efficiently solving the underlying optimization problem using a general
purpose optimization algorithm with minimal assumptions.

## Metadata
- venue: ICLR
- year: 2025
- authors: Konstantinos Karatapanis, Vasilis Kontonis, Christos Tzamos
- arxiv_id: 
- openreview_id: ZS7UEI3vG5
- anthology_id: 
- pdf_url: https://openreview.net/pdf/723e0e1485099706494f7e2b4c2ca51824b4950a.pdf
- published: 2025
- keywords: truncated statistics, exponential family, statistical learning

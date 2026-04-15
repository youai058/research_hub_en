---
title: "Correlation Clustering Beyond the Pivot Algorithm"
authors: ["Soheil Behnezhad", "Moses Charikar", "Vincent Cohen-Addad", "Alma Ghafari", "Weiyun ma"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "OzQLuoKMQZ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/06900a3ce7035fb636369c3a8a4642ca8bc66616.pdf"
published: "2025"
categories: []
keywords: ["Correlation Clustering"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:40+09:00"
---

# Correlation Clustering Beyond the Pivot Algorithm

## Abstract
We study the classic correlation clustering problem. Given $n$ objects and a complete labeling of the object-pairs as either “similar” or “dissimilar”, the goal is to partition the objects into
arbitrarily many clusters while minimizing disagreements with 
the labels.

A classic Pivot algorithm for this problem, due to [Ailon et al STOC'05], obtains a 3-approximation for this problem. Over the years, this algorithm has been successfully implemented in various settings. The downside of the Pivot algorithm is that the approximation analysis of 3 is tight for it. While better approximations have been achieved in some settings, these algorithms are often hard to implement in various settings. For example, [Behnezhad et al FOCS19] showed that the output of Pivot can be maintained in polylog time per update in a dynamic setting, a bound that was improved to constant by [Dalirrooyfard et al ICML'24]. But obtaining a better approximation remains open.

In this paper, we present Modified Pivot, an algorithm that locally improves the output of Pivot. Our Modified Pivot algorithm can be implemented just as efficiently as Pivot in various settings. Our experiments show that the output of Modified Pivot on average makes less than 77\% of the mistakes made by Pivot. More surprisingly, we prove theoretically that Modified Pivot has approximation ratio $3-\epsilon_0$ for some absolute constant $\epsilon_0 > 0$. This, e.g., leads to a better than 3 approximation in the dynamic setting in polylog time, improving the 3-approximation obtained by [Behnezhad et al FOCS'19] and [Dalirrooyfard et al ICML'24].

## Metadata
- venue: ICML
- year: 2025
- authors: Soheil Behnezhad, Moses Charikar, Vincent Cohen-Addad, Alma Ghafari, Weiyun ma
- arxiv_id: 
- openreview_id: OzQLuoKMQZ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/06900a3ce7035fb636369c3a8a4642ca8bc66616.pdf
- published: 2025
- keywords: Correlation Clustering

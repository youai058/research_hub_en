---
title: "Sample Complexity of Algorithm Selection Using Neural Networks and Its Applications to Branch-and-Cut"
authors: ["Hongyu Cheng", "Sammy Khalife", "Barbara Fiedorowicz", "Amitabh Basu"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "uOvrwVW1yA"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b7e10c38cee539331a5186b1d97e6369cb37e69b.pdf"
published: "2024"
categories: []
keywords: ["Integer programming", "branch-and-cut", "branch-and-bound", "sample complexity", "neural networks", "learning theory", "data-driven algorithm design"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:05+09:00"
---

# Sample Complexity of Algorithm Selection Using Neural Networks and Its Applications to Branch-and-Cut

## Abstract
Data-driven algorithm design is a paradigm that uses statistical and machine learning techniques to select from a class of algorithms for a computational problem an algorithm that has the best expected performance with respect to some (unknown) distribution on the instances of the problem. We build upon recent work in this line of research by considering the setup where, instead of selecting a single algorithm that has the best performance, we allow the possibility of selecting an algorithm based on the instance to be solved, using neural networks. In particular, given a representative sample of instances, we learn a neural network that maps an instance of the problem to the most appropriate algorithm *for that instance*. We formalize this idea and derive rigorous sample complexity bounds for this learning problem, in the spirit of recent work in data-driven algorithm design. We then apply this approach to the problem of making good decisions in the branch-and-cut framework for mixed-integer optimization (e.g., which cut to add?). In other words, the neural network will take as input a mixed-integer optimization instance and output a decision that will result in a small branch-and-cut tree for that instance. Our computational results provide evidence that our particular way of using neural networks for cut selection can make a significant impact in reducing branch-and-cut tree sizes, compared to previous data-driven approaches.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Hongyu Cheng, Sammy Khalife, Barbara Fiedorowicz, Amitabh Basu
- arxiv_id: 
- openreview_id: uOvrwVW1yA
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b7e10c38cee539331a5186b1d97e6369cb37e69b.pdf
- published: 2024
- keywords: Integer programming, branch-and-cut, branch-and-bound, sample complexity, neural networks, learning theory, data-driven algorithm design

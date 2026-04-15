---
title: "The Hot Mess of AI: How Does Misalignment Scale With Model Intelligence and Task Complexity?"
authors: ["Alexander Hägele", "Aryo Pradipta Gema", "Henry Sleight", "Ethan Perez", "Jascha Sohl-Dickstein"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "sIBwirjYlY"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ca22e5fd84bff64319374a88712c7ba086d9b8b4.pdf"
published: "2026"
categories: []
keywords: ["Large Language Models", "Scaling Laws", "Misalignment", "Bias-Variance"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:44+09:00"
---

# The Hot Mess of AI: How Does Misalignment Scale With Model Intelligence and Task Complexity?

## Abstract
As AI becomes more capable, we entrust it with more general and consequential tasks. The risks from failure grow more severe with increasing task scope. It is therefore important to understand 
the ways extremely capable AI models will fail: Will they fail by systematically pursuing goals we do not intend? Or will they fail by being a hot mess, and taking nonsensical actions that do not further any goal? We operationalize this question using a bias-variance decomposition of the errors made by AI models: An AI's *error incoherence* on a task is measured over test-time randomness as the fraction of its error that stems from variance rather than bias in task outcome. Across all tasks and frontier models we measure, we find that the longer models spend reasoning and taking actions, *the more incoherent* their failures become. We observe that error incoherence changes with model scale in a way that is task and experiment dependent. However, in several settings larger, more capable models are more incoherent than smaller models.
Consequently, scale alone seems unlikely to eliminate incoherence. Instead, as more capable AIs pursue harder tasks, requiring more sequential action and thought, our results predict failures to be accompanied by more incoherent behavior. 
This suggests a future where AIs sometimes cause industrial accidents (due to unpredictable misbehavior), but are less likely to exhibit consistent pursuit of a misaligned goal. 
This increases the relative importance of alignment research targeting reward hacking or goal misspecification.

## Metadata
- venue: ICLR
- year: 2026
- authors: Alexander Hägele, Aryo Pradipta Gema, Henry Sleight, Ethan Perez, Jascha Sohl-Dickstein
- arxiv_id: 
- openreview_id: sIBwirjYlY
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ca22e5fd84bff64319374a88712c7ba086d9b8b4.pdf
- published: 2026
- keywords: Large Language Models, Scaling Laws, Misalignment, Bias-Variance

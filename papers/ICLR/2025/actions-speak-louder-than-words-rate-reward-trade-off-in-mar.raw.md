---
title: "Actions Speak Louder Than Words: Rate-Reward Trade-off in Markov Decision Processes"
authors: ["Haotian Wu", "Gongpu Chen", "Deniz Gunduz"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Za3M6OZuCU"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/5e687a3e5348b6bc8afcefc437df93de011baf0e.pdf"
published: "2025"
categories: []
keywords: ["Markov Decision Process", "Channel coding", "Rate-Reward Trade-off", "Finite state channel"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:44+09:00"
---

# Actions Speak Louder Than Words: Rate-Reward Trade-off in Markov Decision Processes

## Abstract
The impact of communication on decision-making systems has been extensively studied under the assumption of dedicated communication channels. We instead consider communicating through actions, where the message is embedded into the actions of an agent which interacts with the environment in a Markov decision process (MDP) framework. We conceptualize the MDP environment as a finite-state channel (FSC), where the actions of the agent serve as the channel input, while the states of the MDP observed by another agent (i.e., receiver) serve as the channel output. Here, we treat the environment as a communication channel over which the agent communicates through its actions, while at the same time, trying to maximize its reward. We first characterize the optimal information theoretic trade-off between the average reward and the rate of reliable communication in the infinite-horizon regime. Then, we propose a novel framework to design a joint control/coding policy, termed Act2Comm, which seamlessly embeds messages into actions. From a communication perspective, Act2Comm functions as a learning-based channel coding scheme for non-differentiable FSCs under input-output constraints. From a control standpoint, Act2Comm learns an MDP policy that incorporates communication capabilities, though at the cost of some control performance. Overall, Act2Comm effectively balances the dual objectives of control and communication in this environment. Experimental results validate Act2Comm's capability to enable reliable communication while maintaining a certain level of control performance.

## Metadata
- venue: ICLR
- year: 2025
- authors: Haotian Wu, Gongpu Chen, Deniz Gunduz
- arxiv_id: 
- openreview_id: Za3M6OZuCU
- anthology_id: 
- pdf_url: https://openreview.net/pdf/5e687a3e5348b6bc8afcefc437df93de011baf0e.pdf
- published: 2025
- keywords: Markov Decision Process, Channel coding, Rate-Reward Trade-off, Finite state channel

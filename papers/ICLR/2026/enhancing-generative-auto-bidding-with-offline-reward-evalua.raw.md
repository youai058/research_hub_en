---
title: "Enhancing Generative Auto-bidding with Offline Reward Evaluation and Policy Search"
authors: ["Zhiyu Mou", "Yiqin Lv", "Miao Xu", "Cheems Wang", "Yixiu Mao", "Jinghao Chen", "Qichen Ye", "Chao Li", "Rongquan Bai", "Chuan Yu", "Jian Xu", "Bo Zheng"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "kMuQBgPIdg"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/fb33b81816ac97bae083fa6ee7dc27d9ed497bd2.pdf"
published: "2026"
categories: []
keywords: ["auto-bidding", "offline reinforcement learning", "generative decision making"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:35+09:00"
---

# Enhancing Generative Auto-bidding with Offline Reward Evaluation and Policy Search

## Abstract
Auto-bidding is a critical tool for advertisers to improve advertising performance. Recent progress has demonstrated that AI-Generated Bidding (AIGB), which learns a conditional generative planner from offline data, achieves superior performance compared to typical offline reinforcement learning (RL)-based auto-bidding methods. However, existing AIGB methods still face a performance bottleneck due to their inherent inability to explore beyond the static dataset with feedback. To address this, we propose AIGB-Pearl (Planning with EvaluAtor via RL), a novel method that integrates generative planning and policy optimization. The core of AIGB-Pearl lies in constructing a trajectory evaluator to assess the quality of generated scores and designing a provably sound KL-Lipschitz-constrained score-maximization scheme to ensure safe and efficient exploration beyond the offline dataset. A practical algorithm that incorporates the synchronous coupling technique is further developed to ensure the model regularity required by the proposed scheme. Extensive experiments on both simulated and real-world advertising systems demonstrate the state-of-the-art performance of our approach.

## Metadata
- venue: ICLR
- year: 2026
- authors: Zhiyu Mou, Yiqin Lv, Miao Xu, Cheems Wang, Yixiu Mao, Jinghao Chen, Qichen Ye, Chao Li, Rongquan Bai, Chuan Yu, Jian Xu, Bo Zheng
- arxiv_id: 
- openreview_id: kMuQBgPIdg
- anthology_id: 
- pdf_url: https://openreview.net/pdf/fb33b81816ac97bae083fa6ee7dc27d9ed497bd2.pdf
- published: 2026
- keywords: auto-bidding, offline reinforcement learning, generative decision making

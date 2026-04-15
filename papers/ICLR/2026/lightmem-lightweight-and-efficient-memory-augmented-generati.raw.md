---
title: "LightMem: Lightweight and Efficient Memory-Augmented Generation"
authors: ["Jizhan Fang", "Xinle Deng", "Haoming Xu", "Ziyan Jiang", "Yuqi Tang", "Ziwen Xu", "Shumin Deng", "Yunzhi Yao", "Mengru Wang", "Shuofei Qiao", "Huajun Chen", "Ningyu Zhang"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "dyJ0GWpjJB"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/305f44df1f1144b2f38b2d8dac328e8c6f4c6f08.pdf"
published: "2026"
categories: []
keywords: ["large language model", "LLM memory"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:30+09:00"
---

# LightMem: Lightweight and Efficient Memory-Augmented Generation

## Abstract
Despite their remarkable capabilities, Large Language Model (LLM) struggle to effectively leverage historical interaction information in dynamic and complex environments. Memory systems enable LLMs to move beyond stateless interactions by introducing persistent information storage, retrieval, and utilization mechanisms. However, existing memory systems often incur substantial time and computational overhead. To this end, we introduce a new memory system called LightMem, which strikes a balance between the performance and efficiency of memory systems. Inspired by the Atkinson–Shiffrin model of human memory, LightMem organizes memory into three complementary stages. First, cognitive-inspired sensory memory rapidly filters irrelevant information through lightweight compression and groups information according to their topics. Next, topic-aware short-term memory consolidates these topic-based groups, organizing and summarizing content for more structured access. Finally, long-term memory with sleep-time update employs an offline procedure that decouples consolidation from online inference. 
Experiments on LongMemEval with GPT and Qwen backbones show that LightMem outperforms strong baselines in accuracy (up to 10.9% gains) while reducing token usage by up to 117×, API calls by up to 159×, and runtime by over 12×. Code will be released on GitHub.

## Metadata
- venue: ICLR
- year: 2026
- authors: Jizhan Fang, Xinle Deng, Haoming Xu, Ziyan Jiang, Yuqi Tang, Ziwen Xu, Shumin Deng, Yunzhi Yao, Mengru Wang, Shuofei Qiao, Huajun Chen, Ningyu Zhang
- arxiv_id: 
- openreview_id: dyJ0GWpjJB
- anthology_id: 
- pdf_url: https://openreview.net/pdf/305f44df1f1144b2f38b2d8dac328e8c6f4c6f08.pdf
- published: 2026
- keywords: large language model, LLM memory

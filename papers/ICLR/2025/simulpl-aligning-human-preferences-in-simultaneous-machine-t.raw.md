---
title: "SimulPL: Aligning Human Preferences in Simultaneous Machine Translation"
authors: ["Donglei Yu", "Yang Zhao", "Jie Zhu", "Yangyifan Xu", "Yu Zhou", "Chengqing Zong"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "XBF63bHDZw"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f453526ab32bf14b0e2abf0216bf951c4601e7ef.pdf"
published: "2025"
categories: []
keywords: ["simultaneous machine translation", "simultaneous preference optimization", "human preferences"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:45+09:00"
---

# SimulPL: Aligning Human Preferences in Simultaneous Machine Translation

## Abstract
Simultaneous Machine Translation (SiMT) generates translations while receiving streaming source inputs. This requires the SiMT model to learn a read/write policy, deciding when to translate and when to wait for more source input. Numerous linguistic studies indicate that audiences in SiMT scenarios have distinct preferences, such as accurate translations, simpler syntax, and no unnecessary latency. Aligning SiMT models with these human preferences is crucial to improve their performances. However, this issue still remains unexplored. Additionally, preference optimization for SiMT task is also challenging. Existing methods focus solely on optimizing the generated responses, ignoring human preferences related to latency and the optimization of read/write policy during the preference optimization phase. To address these challenges, we propose Simultaneous Preference Learning (SimulPL), a preference learning framework tailored for the SiMT task. In the SimulPL framework, we categorize SiMT human preferences into five aspects: **translation quality preference**, **monotonicity preference**, **key point preference**, **simplicity preference**, and **latency preference**. By leveraging the first four preferences, we construct human preference prompts to efficiently guide GPT-4/4o in generating preference data for the SiMT task. In the preference optimization phase, SimulPL integrates **latency preference** into the optimization objective and enables SiMT models to improve the read/write policy, thereby aligning with human preferences more effectively. Experimental results indicate that SimulPL exhibits better alignment with human preferences across all latency levels in Zh$\rightarrow$En, De$\rightarrow$En and En$\rightarrow$Zh SiMT tasks.  Our data and code will be available at https://github.com/EurekaForNLP/SimulPL.

## Metadata
- venue: ICLR
- year: 2025
- authors: Donglei Yu, Yang Zhao, Jie Zhu, Yangyifan Xu, Yu Zhou, Chengqing Zong
- arxiv_id: 
- openreview_id: XBF63bHDZw
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f453526ab32bf14b0e2abf0216bf951c4601e7ef.pdf
- published: 2025
- keywords: simultaneous machine translation, simultaneous preference optimization, human preferences

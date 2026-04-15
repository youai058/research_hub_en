---
title: "Robust Root Cause Diagnosis using In-Distribution Interventions"
authors: ["Lokesh Nagalapatti", "Ashutosh Srivastava", "Sunita Sarawagi", "Amit Sharma"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "l11DZY5Nxu"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/704fab6788807803612ad2b12344cc35a2a74913.pdf"
published: "2025"
categories: []
keywords: ["Root Cause Diagnosis", "Causal Inference", "Interventional RCD"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:43+09:00"
---

# Robust Root Cause Diagnosis using In-Distribution Interventions

## Abstract
Diagnosing the root cause of an anomaly in a complex interconnected system is
a pressing problem in today’s cloud services and industrial operations. We propose In-Distribution Interventions (IDI), a novel algorithm that predicts root cause
as nodes that meet two criteria: 1) Anomaly: root cause nodes should take on
anomalous values; 2) Fix: had the root cause nodes assumed usual values, the
target node would not have been anomalous. Prior methods of assessing the fix
condition rely on counterfactuals inferred from a Structural Causal Model (SCM)
trained on historical data. But since anomalies are rare and fall outside the training distribution, the fitted SCMs yield unreliable counterfactual estimates. IDI
overcomes this by relying on interventional estimates obtained by solely probing the fitted SCM at in-distribution inputs. We present a theoretical analysis
comparing and bounding the errors in assessing the fix condition using interventional and counterfactual estimates. We then conduct experiments by systematically varying the SCM’s complexity to demonstrate the cases where IDI’s interventional approach outperforms the counterfactual approach and vice versa.
Experiments on both synthetic and PetShop RCD benchmark datasets demonstrate that IDI consistently identifies true root causes more accurately and robustly than nine existing state-of-the-art RCD baselines. Code will be released
at https://github.com/nlokeshiisc/IDI_release.

## Metadata
- venue: ICLR
- year: 2025
- authors: Lokesh Nagalapatti, Ashutosh Srivastava, Sunita Sarawagi, Amit Sharma
- arxiv_id: 
- openreview_id: l11DZY5Nxu
- anthology_id: 
- pdf_url: https://openreview.net/pdf/704fab6788807803612ad2b12344cc35a2a74913.pdf
- published: 2025
- keywords: Root Cause Diagnosis, Causal Inference, Interventional RCD

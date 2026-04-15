---
title: "Causal language modeling can elicit search and reasoning capabilities on logic puzzles"
authors: ["Kulin Shah", "Nishanth Dikkala", "Xin Wang", "Rina Panigrahy"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "i5PoejmWoC"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/41e4f4d76ff881e14c3d9db05978f9af25ee8739.pdf"
published: "2024"
categories: []
keywords: ["reasoning", "search", "planning", "sudoku", "world model", "transformers"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:52+09:00"
---

# Causal language modeling can elicit search and reasoning capabilities on logic puzzles

## Abstract
Causal language modeling using the Transformer architecture has yielded remarkable capabilities in Large Language Models (LLMs) over the last few years. However, the extent to which fundamental search and reasoning capabilities emerged within LLMs remains a topic of ongoing debate. In this work, we study if causal language modeling can learn a complex task such as solving Sudoku puzzles. To solve a Sudoku, the model is first required to search over all empty cells of the puzzle to decide on a cell to fill and then apply an appropriate strategy to fill the decided cell. Sometimes, the application of a strategy only results in thinning down the possible values in a cell rather than concluding the exact value of the cell. In such cases, multiple strategies are applied one after the other to fill a single cell. We observe that Transformer models trained on this synthetic task can indeed learn to solve Sudokus (our model solves $94.21\%$ of the puzzles fully correctly) when trained on a logical sequence of steps taken by a solver. We find that training Transformers with the logical sequence of steps is necessary and without such training, they fail to learn Sudoku. We also extend our analysis to Zebra puzzles (known as Einstein puzzles) and show that the model solves $92.04 \%$ of the puzzles fully correctly. In addition, we study the internal representations of the trained Transformer and find that through linear probing, we can decode information about the set of possible values in any given cell from them, pointing to the presence of a strong reasoning engine implicit in the Transformer weights.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Kulin Shah, Nishanth Dikkala, Xin Wang, Rina Panigrahy
- arxiv_id: 
- openreview_id: i5PoejmWoC
- anthology_id: 
- pdf_url: https://openreview.net/pdf/41e4f4d76ff881e14c3d9db05978f9af25ee8739.pdf
- published: 2024
- keywords: reasoning, search, planning, sudoku, world model, transformers

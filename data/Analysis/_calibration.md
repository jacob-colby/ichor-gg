# Signal-weight calibration

Guardrails: efficiency+fit ≥ 0.50, pick ≤ 0.15, sum = 1. Objective = 0.5·norm(Spearman) + 0.5·coverage.

**Current hand weights:** {'efficiency': 0.35, 'win': 0.3, 'pick': 0.15, 'fit': 0.2}

| eff | win | pick | fit | objective | Spearman | coverage |
|---|---|---|---|---|---|---|
| 0.35 | 0.35 | 0.15 | 0.15 | 0.695 | 0.38 | 70% |
| 0.4 | 0.35 | 0.15 | 0.1 | 0.694 | 0.38 | 70% |
| 0.3 | 0.35 | 0.15 | 0.2 | 0.679 | 0.40 | 66% |
| 0.2 | 0.35 | 0.15 | 0.3 | 0.668 | 0.40 | 64% |
| 0.35 | 0.4 | 0.1 | 0.15 | 0.663 | 0.45 | 60% |
| 0.4 | 0.3 | 0.15 | 0.15 | 0.662 | 0.33 | 66% |
| 0.35 | 0.3 | 0.15 | 0.2 | 0.661 | 0.32 | 66% |
| 0.3 | 0.4 | 0.1 | 0.2 | 0.661 | 0.44 | 60% |
| 0.15 | 0.35 | 0.15 | 0.35 | 0.661 | 0.37 | 64% |
| 0.2 | 0.4 | 0.1 | 0.3 | 0.650 | 0.44 | 58% |
| 0.25 | 0.35 | 0.15 | 0.25 | 0.650 | 0.40 | 60% |
| 0.4 | 0.4 | 0.1 | 0.1 | 0.650 | 0.44 | 58% |
| 0.1 | 0.35 | 0.15 | 0.4 | 0.644 | 0.35 | 62% |
| 0.3 | 0.3 | 0.15 | 0.25 | 0.642 | 0.33 | 62% |
| 0.25 | 0.4 | 0.1 | 0.25 | 0.642 | 0.45 | 56% |

## Leave-one-god-out winners

- without Agni: {'efficiency': 0.4, 'win': 0.35, 'pick': 0.15, 'fit': 0.1}
- without Cernunnos: {'efficiency': 0.4, 'win': 0.35, 'pick': 0.15, 'fit': 0.1}
- without Chiron: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Chronos: {'efficiency': 0.4, 'win': 0.35, 'pick': 0.15, 'fit': 0.1}
- without Hercules: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Morgan Le Fay: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Princess Bari: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Ra: {'efficiency': 0.4, 'win': 0.35, 'pick': 0.15, 'fit': 0.1}
- without Susano: {'efficiency': 0.4, 'win': 0.35, 'pick': 0.15, 'fit': 0.1}
- without Ullr: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Ymir: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}

**Stability:** 2 distinct fold-winner(s) across 11 folds — stable.

# Signal-weight calibration

> **Read the leakage probe before the grid.** Both of this metric's targets are also model inputs, so the grid's ranking is partly the metric grading its own input. See `calibrate.py`.

## 1. Leakage probe — what the objective actually maximises

Each row deletes the model and hands the metric one of its own inputs. A corner that beats the real blends means the objective cannot select weights.

| Weights | Spearman (pooled) | Within-god | Coverage |
|---|---|---|---|
| win only (Spearman's target verbatim) | 1.000 | +1.00 (positive on 87/87) | 45.0% |
| pick only (community membership) | 0.005 | -0.05 (positive on 38/87) | 93.7% |
| model only (efficiency + fit) | -0.016 | +0.04 (positive on 45/87) | 37.5% |

`win only` scores a perfect Spearman because the score *is* the target. `pick only` all but reproduces the community build. Neither contains any modeling.

## 2. Baseline — what coverage means

A **random** legal 6-item core, drawn 200x per god from the same candidate pool (median 95 items), covers **5.8%** of the community set. Every coverage number below is a multiple of that, not of zero.

## 3. Leakage-free sweep of the model signals

`win` and `pick` held at **zero**, so nothing from the target enters the score. This is the only sweep whose winner may be applied directly.

| efficiency | fit | coverage | 95% CI | vs chance |
|---|---|---|---|---|
| 0.00 | 1.00 | 26.0% | [21.1%, 31.2%] | 4.4x |
| 0.05 | 0.95 | 30.0% | [24.3%, 36.1%] | 5.1x |
| 0.10 | 0.90 | 30.1% | [24.4%, 36.1%] | 5.1x |
| 0.15 | 0.85 | 30.0% | [24.5%, 36.0%] | 5.1x |
| 0.20 | 0.80 | 31.6% | [26.3%, 37.4%] | 5.4x |
| 0.25 | 0.75 | 32.2% | [27.1%, 37.9%] | 5.5x |
| 0.30 | 0.70 | 33.7% | [28.6%, 39.2%] | 5.8x |
| 0.35 | 0.65 | 35.0% | [30.1%, 40.3%] | 6.0x |
| 0.40 | 0.60 | 35.1% | [30.1%, 40.4%] | 6.0x |
| 0.45 | 0.55 | 35.2% | [30.2%, 40.7%] | 6.0x |
| 0.50 | 0.50 | 34.3% | [29.1%, 39.8%] | 5.9x |
| 0.55 | 0.45 | 35.2% | [29.9%, 40.7%] | 6.0x |
| 0.60 | 0.40 | 36.2% | [31.2%, 41.6%] | 6.2x |
| 0.65 | 0.35 | 36.1% | [31.0%, 41.3%] | 6.2x |
| 0.70 | 0.30 | 37.5% | [32.5%, 42.5%] | 6.4x |
| 0.75 | 0.25 | 35.0% | [30.4%, 39.7%] | 6.0x |
| 0.80 | 0.20 | 32.6% | [28.4%, 36.8%] | 5.6x |
| 0.85 | 0.15 | 29.6% | [25.5%, 33.7%] | 5.1x |
| 0.90 | 0.10 | 25.3% | [21.4%, 29.5%] | 4.3x |
| 0.95 | 0.05 | 21.8% | [18.7%, 25.2%] | 3.7x |
| 1.00 | 0.00 | 18.0% | [14.5%, 21.5%] | 3.1x |

Best: efficiency 0.70 : fit 0.30 at 37.5%. **17 of 21 splits have a CI overlapping it** — treat a winner inside that band as noise and leave the shipped split alone.

## 4. Guardrailed grid — the trade-off frontier, not a winner

Guardrails: efficiency+fit ≥ 0.50, pick ≤ 0.15, sum = 1. Objective = 0.5·norm(Spearman) + 0.5·coverage. The guardrails are load-bearing: they are what keeps this search away from the degenerate corners above, so a row pressed against `pick ≤ 0.15` is the constraint speaking, not the data.

**Current hand weights:** eff 0.35 · win 0.45 · pick 0.05 · fit 0.15

| eff | win | pick | fit | objective | Spearman | coverage |
|---|---|---|---|---|---|---|
| 0.35 | 0.35 | 0.15 | 0.15 | 0.673 | 0.43 | 63% |
| 0.4 | 0.35 | 0.15 | 0.1 | 0.668 | 0.46 | 61% |
| 0.3 | 0.35 | 0.15 | 0.2 | 0.663 | 0.40 | 63% |
| 0.35 | 0.4 | 0.1 | 0.15 | 0.657 | 0.49 | 57% |
| 0.35 | 0.3 | 0.15 | 0.2 | 0.647 | 0.34 | 63% |
| 0.4 | 0.4 | 0.1 | 0.1 | 0.646 | 0.52 | 53% |
| 0.4 | 0.3 | 0.15 | 0.15 | 0.646 | 0.37 | 61% |
| 0.3 | 0.4 | 0.1 | 0.2 | 0.643 | 0.45 | 56% |
| 0.45 | 0.35 | 0.15 | 0.05 | 0.642 | 0.46 | 55% |
| 0.45 | 0.3 | 0.15 | 0.1 | 0.638 | 0.38 | 58% |
| 0.25 | 0.35 | 0.15 | 0.25 | 0.638 | 0.36 | 59% |
| 0.4 | 0.35 | 0.1 | 0.15 | 0.636 | 0.43 | 56% |
| 0.35 | 0.45 | 0.05 | 0.15 | 0.634 | 0.54 | 50% ←current |
| 0.4 | 0.25 | 0.15 | 0.2 | 0.631 | 0.28 | 62% |
| 0.3 | 0.3 | 0.15 | 0.25 | 0.629 | 0.31 | 60% |

## 5. Leave-one-god-out winners

_Stability only. A leaked objective leaks identically in every fold, so this cannot detect the problem in section 1._

- without Achilles: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Agni: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Ah Puch: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Aladdin: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Amaterasu: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Anhur: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Anubis: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Aphrodite: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Apollo: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Ares: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Artemis: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Artio: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Athena: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Atlas: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Awilix: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Bacchus: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Baron Samedi: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Bastet: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Bellona: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Cabrakan: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Cerberus: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Cernunnos: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Chaac: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Charon: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Chiron: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Chronos: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Cupid: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Da Ji: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Danzaburou: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Discordia: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Eset: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Fenrir: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Ganesha: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Geb: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Gilgamesh: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Guan Yu: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Hades: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Hecate: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Hercules: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Horus: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Hou Yi: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Hua Mulan: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Hun Batz: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Ishtar: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Izanami: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Janus: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Jing Wei: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Jormungandr: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Kali: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Khepri: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Kukulkan: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Loki: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Medusa: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Mercury: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Merlin: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Mordred: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Morgan Le Fay: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Ne Zha: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Neith: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Nemesis: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Nu Wa: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Nut: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Odin: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Osiris: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Pele: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Poseidon: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Princess Bari: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Ra: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Rama: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Ratatoskr: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Scylla: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Sobek: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Sol: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Sun Wukong: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Susano: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Sylvanus: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Thanatos: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without The Morrigan: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Thor: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Tsukuyomi: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Ullr: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Vulcan: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Xbalanque: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Xing Tian: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Yemoja: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Ymir: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Zeus: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15

**Stability:** 1 distinct fold-winner(s) across 87 folds — stable.

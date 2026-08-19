# Signal-weight calibration

> **Read the leakage probe before the grid.** Both of this metric's targets are also model inputs, so the grid's ranking is partly the metric grading its own input. See `calibrate.py`.

## 1. Leakage probe — what the objective actually maximises

Each row deletes the model and hands the metric one of its own inputs. A corner that beats the real blends means the objective cannot select weights.

| Weights | Spearman (pooled) | Within-god | Coverage |
|---|---|---|---|
| win only (Spearman's target verbatim) | 1.000 | +1.00 (positive on 89/89) | 43.0% |
| pick only (community membership) | -0.025 | -0.06 (positive on 39/89) | 90.3% |
| model only (efficiency + fit) | -0.070 | -0.02 (positive on 43/89) | 35.5% |

`win only` scores a perfect Spearman because the score *is* the target. `pick only` all but reproduces the community build. Neither contains any modeling.

## 2. Baseline — what coverage means

A **random** legal 6-item core, drawn 200x per god from the same candidate pool (median 99 items), covers **5.8%** of the community set. Every coverage number below is a multiple of that, not of zero.

## 3. Leakage-free sweep of the model signals

`win` and `pick` held at **zero**, so nothing from the target enters the score. This is the only sweep whose winner may be applied directly.

| efficiency | fit | coverage | 95% CI | vs chance |
|---|---|---|---|---|
| 0.00 | 1.00 | 27.9% | [22.7%, 33.3%] | 4.8x |
| 0.05 | 0.95 | 30.9% | [25.2%, 36.8%] | 5.3x |
| 0.10 | 0.90 | 30.8% | [25.1%, 36.9%] | 5.3x |
| 0.15 | 0.85 | 30.7% | [24.8%, 36.7%] | 5.2x |
| 0.20 | 0.80 | 32.2% | [26.4%, 38.1%] | 5.5x |
| 0.25 | 0.75 | 34.0% | [28.4%, 39.6%] | 5.8x |
| 0.30 | 0.70 | 35.0% | [29.7%, 40.6%] | 6.0x |
| 0.35 | 0.65 | 36.2% | [31.0%, 41.5%] | 6.2x |
| 0.40 | 0.60 | 36.6% | [31.4%, 42.1%] | 6.3x |
| 0.45 | 0.55 | 36.7% | [31.3%, 42.4%] | 6.3x |
| 0.50 | 0.50 | 35.4% | [29.9%, 41.1%] | 6.1x |
| 0.55 | 0.45 | 36.1% | [30.7%, 41.8%] | 6.2x |
| 0.60 | 0.40 | 36.3% | [30.9%, 41.8%] | 6.2x |
| 0.65 | 0.35 | 36.4% | [30.8%, 41.9%] | 6.2x |
| 0.70 | 0.30 | 35.5% | [30.2%, 40.8%] | 6.1x |
| 0.75 | 0.25 | 35.6% | [30.6%, 40.8%] | 6.1x |
| 0.80 | 0.20 | 31.1% | [26.8%, 35.5%] | 5.3x |
| 0.85 | 0.15 | 28.2% | [24.0%, 32.6%] | 4.8x |
| 0.90 | 0.10 | 23.8% | [20.1%, 27.6%] | 4.1x |
| 0.95 | 0.05 | 21.1% | [17.9%, 24.6%] | 3.6x |
| 1.00 | 0.00 | 16.5% | [13.2%, 19.9%] | 2.8x |

Best: efficiency 0.45 : fit 0.55 at 36.7%. **18 of 21 splits have a CI overlapping it** — treat a winner inside that band as noise and leave the shipped split alone.

## 4. Guardrailed grid — the trade-off frontier, not a winner

Guardrails: efficiency+fit ≥ 0.50, pick ≤ 0.15, sum = 1. Objective = 0.5·norm(Spearman) + 0.5·coverage. The guardrails are load-bearing: they are what keeps this search away from the degenerate corners above, so a row pressed against `pick ≤ 0.15` is the constraint speaking, not the data.

**Current hand weights:** eff 0.35 · win 0.45 · pick 0.05 · fit 0.15

| eff | win | pick | fit | objective | Spearman | coverage |
|---|---|---|---|---|---|---|
| 0.35 | 0.35 | 0.15 | 0.15 | 0.628 | 0.28 | 62% |
| 0.3 | 0.35 | 0.15 | 0.2 | 0.623 | 0.26 | 62% |
| 0.4 | 0.35 | 0.15 | 0.1 | 0.617 | 0.30 | 59% |
| 0.35 | 0.4 | 0.1 | 0.15 | 0.610 | 0.34 | 55% |
| 0.4 | 0.3 | 0.15 | 0.15 | 0.605 | 0.22 | 60% |
| 0.35 | 0.3 | 0.15 | 0.2 | 0.602 | 0.21 | 60% |
| 0.25 | 0.35 | 0.15 | 0.25 | 0.600 | 0.25 | 58% |
| 0.3 | 0.4 | 0.1 | 0.2 | 0.599 | 0.31 | 54% |
| 0.4 | 0.4 | 0.1 | 0.1 | 0.598 | 0.35 | 52% |
| 0.3 | 0.3 | 0.15 | 0.25 | 0.592 | 0.19 | 59% |
| 0.45 | 0.3 | 0.15 | 0.1 | 0.589 | 0.24 | 56% |
| 0.25 | 0.4 | 0.1 | 0.25 | 0.589 | 0.30 | 53% |
| 0.2 | 0.35 | 0.15 | 0.3 | 0.587 | 0.23 | 56% |
| 0.35 | 0.35 | 0.1 | 0.2 | 0.584 | 0.26 | 54% |
| 0.4 | 0.25 | 0.15 | 0.2 | 0.584 | 0.15 | 59% |

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
- without Cu Chulainn: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
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
- without Ix Chel: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
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

**Stability:** 1 distinct fold-winner(s) across 89 folds — stable.

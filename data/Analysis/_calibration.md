# Signal-weight calibration

> **Read the leakage probe before the grid.** Both of this metric's targets are also model inputs, so the grid's ranking is partly the metric grading its own input. See `calibrate.py`.

## 1. Leakage probe — what the objective actually maximises

Each row deletes the model and hands the metric one of its own inputs. A corner that beats the real blends means the objective cannot select weights.

| Weights | Spearman (pooled) | Within-god | Coverage |
|---|---|---|---|
| win only (Spearman's target verbatim) | 1.000 | +1.00 (positive on 87/87) | 42.2% |
| pick only (community membership) | 0.133 | -0.03 (positive on 35/87) | 92.5% |
| model only (efficiency + fit) | 0.019 | +0.06 (positive on 45/87) | 34.3% |

`win only` scores a perfect Spearman because the score *is* the target. `pick only` all but reproduces the community build. Neither contains any modeling.

## 2. Baseline — what coverage means

A **random** legal 6-item core, drawn 200x per god from the same candidate pool (median 95 items), covers **5.9%** of the community set. Every coverage number below is a multiple of that, not of zero.

## 3. Leakage-free sweep of the model signals

`win` and `pick` held at **zero**, so nothing from the target enters the score. This is the only sweep whose winner may be applied directly.

| efficiency | fit | coverage | 95% CI | vs chance |
|---|---|---|---|---|
| 0.00 | 1.00 | 26.1% | [21.3%, 31.9%] | 4.4x |
| 0.05 | 0.95 | 27.6% | [22.4%, 33.4%] | 4.7x |
| 0.10 | 0.90 | 28.1% | [22.8%, 33.8%] | 4.8x |
| 0.15 | 0.85 | 28.0% | [23.1%, 33.4%] | 4.7x |
| 0.20 | 0.80 | 28.9% | [24.1%, 34.5%] | 4.9x |
| 0.25 | 0.75 | 29.8% | [25.1%, 34.9%] | 5.0x |
| 0.30 | 0.70 | 29.8% | [25.1%, 34.9%] | 5.0x |
| 0.35 | 0.65 | 30.6% | [26.1%, 35.7%] | 5.2x |
| 0.40 | 0.60 | 30.9% | [26.3%, 36.0%] | 5.2x |
| 0.45 | 0.55 | 31.4% | [26.5%, 36.6%] | 5.3x |
| 0.50 | 0.50 | 31.8% | [27.0%, 37.0%] | 5.4x |
| 0.55 | 0.45 | 32.5% | [27.8%, 37.7%] | 5.5x |
| 0.60 | 0.40 | 32.8% | [27.9%, 38.2%] | 5.6x |
| 0.65 | 0.35 | 35.4% | [30.2%, 40.3%] | 6.0x |
| 0.70 | 0.30 | 34.3% | [29.3%, 39.6%] | 5.8x |
| 0.75 | 0.25 | 32.0% | [27.2%, 36.9%] | 5.4x |
| 0.80 | 0.20 | 29.8% | [25.2%, 34.4%] | 5.1x |
| 0.85 | 0.15 | 24.0% | [20.1%, 27.8%] | 4.1x |
| 0.90 | 0.10 | 21.6% | [17.8%, 25.3%] | 3.7x |
| 0.95 | 0.05 | 16.7% | [13.0%, 20.4%] | 2.8x |
| 1.00 | 0.00 | 16.1% | [12.6%, 19.6%] | 2.7x |

Best: efficiency 0.65 : fit 0.35 at 35.4%. **17 of 21 splits have a CI overlapping it** — treat a winner inside that band as noise and leave the shipped split alone.

## 4. Guardrailed grid — the trade-off frontier, not a winner

Guardrails: efficiency+fit ≥ 0.50, pick ≤ 0.15, sum = 1. Objective = 0.5·norm(Spearman) + 0.5·coverage. The guardrails are load-bearing: they are what keeps this search away from the degenerate corners above, so a row pressed against `pick ≤ 0.15` is the constraint speaking, not the data.

**Current hand weights:** eff 0.35 · win 0.45 · pick 0.05 · fit 0.15

| eff | win | pick | fit | objective | Spearman | coverage |
|---|---|---|---|---|---|---|
| 0.3 | 0.35 | 0.15 | 0.2 | 0.688 | 0.55 | 60% |
| 0.35 | 0.35 | 0.15 | 0.15 | 0.688 | 0.58 | 58% |
| 0.4 | 0.35 | 0.15 | 0.1 | 0.677 | 0.61 | 55% |
| 0.35 | 0.4 | 0.1 | 0.15 | 0.668 | 0.63 | 52% |
| 0.35 | 0.3 | 0.15 | 0.2 | 0.667 | 0.48 | 59% |
| 0.25 | 0.35 | 0.15 | 0.25 | 0.664 | 0.51 | 58% |
| 0.4 | 0.3 | 0.15 | 0.15 | 0.663 | 0.51 | 57% |
| 0.3 | 0.4 | 0.1 | 0.2 | 0.659 | 0.60 | 52% |
| 0.45 | 0.35 | 0.15 | 0.05 | 0.658 | 0.61 | 51% |
| 0.4 | 0.4 | 0.1 | 0.1 | 0.655 | 0.66 | 48% |
| 0.45 | 0.3 | 0.15 | 0.1 | 0.653 | 0.53 | 54% |
| 0.3 | 0.3 | 0.15 | 0.25 | 0.653 | 0.45 | 58% |
| 0.35 | 0.35 | 0.1 | 0.2 | 0.648 | 0.54 | 53% |
| 0.4 | 0.25 | 0.15 | 0.2 | 0.647 | 0.42 | 59% |
| 0.2 | 0.35 | 0.15 | 0.3 | 0.647 | 0.47 | 56% |

## 5. Leave-one-god-out winners

_Stability only. A leaked objective leaks identically in every fold, so this cannot detect the problem in section 1._

- without Achilles: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Agni: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Ah Puch: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Aladdin: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Amaterasu: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Anhur: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Anubis: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Aphrodite: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Apollo: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Ares: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Artemis: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Artio: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Athena: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Atlas: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Awilix: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Bacchus: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Baron Samedi: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Bastet: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Bellona: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Cabrakan: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Cerberus: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Cernunnos: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Chaac: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Charon: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Chiron: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Chronos: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Cupid: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Da Ji: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Danzaburou: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Discordia: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Eset: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Fenrir: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Ganesha: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Geb: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Gilgamesh: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Guan Yu: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Hades: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Hecate: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Hercules: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Horus: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Hou Yi: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Hua Mulan: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Hun Batz: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Ishtar: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Izanami: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Janus: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Jing Wei: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Jormungandr: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Kali: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Khepri: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Kukulkan: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Loki: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Medusa: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Mercury: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Merlin: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Mordred: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Morgan Le Fay: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Ne Zha: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Neith: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Nemesis: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Nu Wa: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Nut: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Odin: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Osiris: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Pele: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Poseidon: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Princess Bari: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Ra: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Rama: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Ratatoskr: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Scylla: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Sobek: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Sol: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Sun Wukong: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Susano: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Sylvanus: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Thanatos: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without The Morrigan: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Thor: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Tsukuyomi: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Ullr: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Vulcan: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Xbalanque: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Xing Tian: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Yemoja: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Ymir: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20
- without Zeus: eff 0.30 · win 0.35 · pick 0.15 · fit 0.20

**Stability:** 2 distinct fold-winner(s) across 87 folds — stable.

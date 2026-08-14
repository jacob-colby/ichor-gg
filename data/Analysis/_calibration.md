# Signal-weight calibration

> **Read the leakage probe before the grid.** Both of this metric's targets are also model inputs, so the grid's ranking is partly the metric grading its own input. See `calibrate.py`.

## 1. Leakage probe — what the objective actually maximises

Each row deletes the model and hands the metric one of its own inputs. A corner that beats the real blends means the objective cannot select weights.

| Weights | Spearman (pooled) | Within-god | Coverage |
|---|---|---|---|
| win only (Spearman's target verbatim) | 1.000 | +1.00 (positive on 86/86) | 44.4% |
| pick only (community membership) | 0.059 | -0.06 (positive on 37/86) | 94.7% |
| model only (efficiency + fit) | -0.071 | -0.03 (positive on 40/86) | 37.6% |

`win only` scores a perfect Spearman because the score *is* the target. `pick only` all but reproduces the community build. Neither contains any modeling.

## 2. Baseline — what coverage means

A **random** legal 6-item core, drawn 200x per god from the same candidate pool (median 95 items), covers **6.0%** of the community set. Every coverage number below is a multiple of that, not of zero.

## 3. Leakage-free sweep of the model signals

`win` and `pick` held at **zero**, so nothing from the target enters the score. This is the only sweep whose winner may be applied directly.

| efficiency | fit | coverage | 95% CI | vs chance |
|---|---|---|---|---|
| 0.00 | 1.00 | 26.1% | [21.1%, 31.5%] | 4.4x |
| 0.05 | 0.95 | 29.7% | [24.1%, 35.8%] | 5.0x |
| 0.10 | 0.90 | 29.7% | [24.0%, 35.7%] | 5.0x |
| 0.15 | 0.85 | 30.5% | [24.7%, 36.6%] | 5.1x |
| 0.20 | 0.80 | 31.4% | [25.8%, 37.3%] | 5.3x |
| 0.25 | 0.75 | 31.7% | [26.1%, 37.5%] | 5.3x |
| 0.30 | 0.70 | 32.5% | [26.9%, 38.2%] | 5.4x |
| 0.35 | 0.65 | 33.8% | [28.3%, 39.4%] | 5.6x |
| 0.40 | 0.60 | 34.3% | [29.0%, 39.8%] | 5.7x |
| 0.45 | 0.55 | 34.1% | [28.7%, 39.8%] | 5.7x |
| 0.50 | 0.50 | 33.8% | [28.1%, 39.6%] | 5.6x |
| 0.55 | 0.45 | 34.8% | [29.4%, 40.4%] | 5.8x |
| 0.60 | 0.40 | 36.5% | [31.2%, 42.1%] | 6.1x |
| 0.65 | 0.35 | 37.7% | [32.3%, 43.3%] | 6.3x |
| 0.70 | 0.30 | 37.6% | [32.7%, 42.6%] | 6.3x |
| 0.75 | 0.25 | 35.4% | [30.5%, 40.7%] | 5.9x |
| 0.80 | 0.20 | 31.4% | [27.2%, 35.7%] | 5.3x |
| 0.85 | 0.15 | 31.0% | [26.7%, 35.3%] | 5.2x |
| 0.90 | 0.10 | 24.9% | [21.3%, 28.5%] | 4.2x |
| 0.95 | 0.05 | 22.9% | [19.7%, 26.3%] | 3.8x |
| 1.00 | 0.00 | 22.1% | [18.9%, 25.6%] | 3.7x |

Best: efficiency 0.65 : fit 0.35 at 37.7%. **17 of 21 splits have a CI overlapping it** — treat a winner inside that band as noise and leave the shipped split alone.

## 4. Guardrailed grid — the trade-off frontier, not a winner

Guardrails: efficiency+fit ≥ 0.50, pick ≤ 0.15, sum = 1. Objective = 0.5·norm(Spearman) + 0.5·coverage. The guardrails are load-bearing: they are what keeps this search away from the degenerate corners above, so a row pressed against `pick ≤ 0.15` is the constraint speaking, not the data.

**Current hand weights:** eff 0.35 · win 0.45 · pick 0.05 · fit 0.15

| eff | win | pick | fit | objective | Spearman | coverage |
|---|---|---|---|---|---|---|
| 0.35 | 0.35 | 0.15 | 0.15 | 0.653 | 0.43 | 59% |
| 0.4 | 0.35 | 0.15 | 0.1 | 0.650 | 0.45 | 58% |
| 0.3 | 0.35 | 0.15 | 0.2 | 0.644 | 0.40 | 59% |
| 0.45 | 0.35 | 0.15 | 0.05 | 0.635 | 0.46 | 54% |
| 0.35 | 0.4 | 0.1 | 0.15 | 0.631 | 0.49 | 52% |
| 0.3 | 0.4 | 0.1 | 0.2 | 0.631 | 0.46 | 53% |
| 0.4 | 0.3 | 0.15 | 0.15 | 0.631 | 0.35 | 58% |
| 0.4 | 0.4 | 0.1 | 0.1 | 0.628 | 0.51 | 50% |
| 0.35 | 0.3 | 0.15 | 0.2 | 0.627 | 0.34 | 59% |
| 0.25 | 0.35 | 0.15 | 0.25 | 0.627 | 0.38 | 56% |
| 0.45 | 0.3 | 0.15 | 0.1 | 0.624 | 0.37 | 56% |
| 0.25 | 0.4 | 0.1 | 0.25 | 0.610 | 0.43 | 50% |
| 0.45 | 0.25 | 0.15 | 0.15 | 0.610 | 0.28 | 58% |
| 0.35 | 0.35 | 0.1 | 0.2 | 0.610 | 0.39 | 52% |
| 0.3 | 0.3 | 0.15 | 0.25 | 0.609 | 0.31 | 56% |

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

# Signal-weight calibration

> **Read the leakage probe before the grid.** Both of this metric's targets are also model inputs, so the grid's ranking is partly the metric grading its own input. See `calibrate.py`.

_Input fingerprint: `c85b909bc2a1` — items, gods, tags, community builds, weights. Check it against `python -m smite.calibrate --control` before quoting any number below._

## 1. Leakage probe — what the objective actually maximises

Each row deletes the model and hands the metric one of its own inputs. A corner that beats the real blends means the objective cannot select weights.

| Weights | Spearman (pooled) | Within-god | Coverage |
|---|---|---|---|
| win only (Spearman's target verbatim) | 1.000 | +1.00 (positive on 89/89) | 42.3% |
| pick only (community membership) | -0.001 | -0.09 (positive on 37/89) | 91.0% |
| model only (efficiency + fit) | -0.038 | +0.04 (positive on 43/89) | 38.7% |

`win only` scores a perfect Spearman because the score *is* the target. `pick only` all but reproduces the community build. Neither contains any modeling.

## 2. Baseline — what coverage means

A **random** legal 6-item core, drawn 200x per god from the same candidate pool (median 99 items), covers **5.6%** of the community set. Every coverage number below is a multiple of that, not of zero.

## 3. Leakage-free sweep of the model signals

`win` and `pick` held at **zero**, so nothing from the target enters the score. This is the only sweep whose winner may be applied directly.

| efficiency | fit | coverage | 95% CI | vs chance |
|---|---|---|---|---|
| 0.00 | 1.00 | 28.0% | [22.8%, 33.5%] | 5.0x |
| 0.05 | 0.95 | 32.6% | [27.1%, 38.4%] | 5.8x |
| 0.10 | 0.90 | 32.2% | [26.5%, 38.0%] | 5.8x |
| 0.15 | 0.85 | 33.0% | [27.4%, 38.7%] | 5.9x |
| 0.20 | 0.80 | 34.1% | [28.7%, 39.6%] | 6.1x |
| 0.25 | 0.75 | 35.9% | [30.6%, 41.1%] | 6.4x |
| 0.30 | 0.70 | 37.7% | [32.4%, 42.9%] | 6.7x |
| 0.35 | 0.65 | 38.6% | [33.4%, 43.6%] | 6.9x |
| 0.40 | 0.60 | 38.9% | [33.9%, 44.0%] | 7.0x |
| 0.45 | 0.55 | 39.6% | [34.6%, 44.6%] | 7.1x |
| 0.50 | 0.50 | 39.8% | [34.6%, 45.2%] | 7.1x |
| 0.55 | 0.45 | 38.5% | [33.1%, 43.9%] | 6.9x |
| 0.60 | 0.40 | 37.8% | [32.4%, 43.3%] | 6.8x |
| 0.65 | 0.35 | 37.5% | [32.0%, 42.9%] | 6.7x |
| 0.70 | 0.30 | 38.7% | [33.1%, 43.9%] | 6.9x |
| 0.75 | 0.25 | 40.9% | [35.5%, 46.1%] | 7.3x |
| 0.80 | 0.20 | 39.0% | [33.5%, 44.5%] | 7.0x |
| 0.85 | 0.15 | 33.7% | [28.7%, 38.8%] | 6.0x |
| 0.90 | 0.10 | 27.6% | [23.6%, 31.9%] | 4.9x |
| 0.95 | 0.05 | 23.3% | [19.8%, 26.9%] | 4.2x |
| 1.00 | 0.00 | 21.7% | [18.7%, 25.1%] | 3.9x |

Best: efficiency 0.75 : fit 0.25 at 40.9%. **17 of 21 splits have a CI overlapping it** — treat a winner inside that band as noise and leave the shipped split alone.

## 4. Guardrailed grid — the trade-off frontier, not a winner

Guardrails: efficiency+fit ≥ 0.50, pick ≤ 0.15, sum = 1. Objective = 0.5·norm(Spearman) + 0.5·coverage. The guardrails are load-bearing: they are what keeps this search away from the degenerate corners above, so a row pressed against `pick ≤ 0.15` is the constraint speaking, not the data.

**Current hand weights:** eff 0.35 · win 0.45 · pick 0.05 · fit 0.15

| eff | win | pick | fit | objective | Spearman | coverage |
|---|---|---|---|---|---|---|
| 0.4 | 0.35 | 0.15 | 0.1 | 0.634 | 0.33 | 61% |
| 0.35 | 0.35 | 0.15 | 0.15 | 0.633 | 0.30 | 61% |
| 0.3 | 0.35 | 0.15 | 0.2 | 0.620 | 0.29 | 60% |
| 0.45 | 0.3 | 0.15 | 0.1 | 0.619 | 0.27 | 60% |
| 0.35 | 0.4 | 0.1 | 0.15 | 0.616 | 0.36 | 55% |
| 0.4 | 0.4 | 0.1 | 0.1 | 0.614 | 0.38 | 54% |
| 0.4 | 0.3 | 0.15 | 0.15 | 0.614 | 0.25 | 60% |
| 0.45 | 0.35 | 0.15 | 0.05 | 0.611 | 0.34 | 55% |
| 0.3 | 0.4 | 0.1 | 0.2 | 0.610 | 0.33 | 55% |
| 0.35 | 0.3 | 0.15 | 0.2 | 0.606 | 0.23 | 59% |
| 0.25 | 0.35 | 0.15 | 0.25 | 0.602 | 0.26 | 57% |
| 0.5 | 0.25 | 0.15 | 0.1 | 0.602 | 0.22 | 59% |
| 0.35 | 0.45 | 0.05 | 0.15 | 0.598 | 0.41 | 49% ←current |
| 0.4 | 0.25 | 0.15 | 0.2 | 0.596 | 0.18 | 60% |
| 0.4 | 0.45 | 0.05 | 0.1 | 0.595 | 0.43 | 48% |

## 5. Leave-one-god-out winners

_Stability only. A leaked objective leaks identically in every fold, so this cannot detect the problem in section 1._

- without Achilles: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Agni: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Ah Puch: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Aladdin: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Amaterasu: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Anhur: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Anubis: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Aphrodite: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Apollo: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Ares: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Artemis: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Artio: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Athena: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Atlas: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Awilix: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Bacchus: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Baron Samedi: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Bastet: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Bellona: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Cabrakan: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Cerberus: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Cernunnos: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Chaac: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Charon: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Chiron: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Chronos: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Cu Chulainn: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Cupid: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Da Ji: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Danzaburou: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Discordia: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Eset: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Fenrir: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Ganesha: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Geb: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Gilgamesh: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Guan Yu: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Hades: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Hecate: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Hercules: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Horus: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Hou Yi: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Hua Mulan: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Hun Batz: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Ishtar: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Ix Chel: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Izanami: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Janus: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Jing Wei: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Jormungandr: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Kali: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Khepri: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Kukulkan: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Loki: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Medusa: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Mercury: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Merlin: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Mordred: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Morgan Le Fay: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Ne Zha: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Neith: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Nemesis: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Nu Wa: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Nut: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Odin: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Osiris: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Pele: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Poseidon: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Princess Bari: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Ra: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Rama: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Ratatoskr: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Scylla: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Sobek: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Sol: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Sun Wukong: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Susano: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Sylvanus: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Thanatos: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without The Morrigan: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Thor: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Tsukuyomi: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Ullr: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Vulcan: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Xbalanque: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Xing Tian: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Yemoja: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Ymir: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Zeus: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10

**Stability:** 2 distinct fold-winner(s) across 89 folds — stable.

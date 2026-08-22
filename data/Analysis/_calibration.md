# Signal-weight calibration

> **Read the leakage probe before the grid.** Both of this metric's targets are also model inputs, so the grid's ranking is partly the metric grading its own input. See `calibrate.py`.

_Input fingerprint: `ea30ca4c0735` — items, gods, tags, community builds, weights. Check it against `python -m smite.calibrate --control` before quoting any number below._

## 1. Leakage probe — what the objective actually maximises

Each row deletes the model and hands the metric one of its own inputs. A corner that beats the real blends means the objective cannot select weights.

| Weights | Spearman (pooled) | Within-god | Coverage |
|---|---|---|---|
| win only (Spearman's target verbatim) | 1.000 | +1.00 (positive on 89/89) | 42.3% |
| pick only (community membership) | -0.001 | -0.09 (positive on 37/89) | 91.0% |
| model only (efficiency + fit) | -0.022 | +0.06 (positive on 46/89) | 39.7% |

`win only` scores a perfect Spearman because the score *is* the target. `pick only` all but reproduces the community build. Neither contains any modeling.

## 2. Baseline — what coverage means

A **random** legal 6-item core, drawn 200x per god from the same candidate pool (median 99 items), covers **5.7%** of the community set. Every coverage number below is a multiple of that, not of zero.

## 3. Leakage-free sweep of the model signals

`win` and `pick` held at **zero**, so nothing from the target enters the score. This is the only sweep whose winner may be applied directly.

| efficiency | fit | coverage | 95% CI | vs chance |
|---|---|---|---|---|
| 0.00 | 1.00 | 29.5% | [24.3%, 34.9%] | 5.2x |
| 0.05 | 0.95 | 33.2% | [27.8%, 39.0%] | 5.8x |
| 0.10 | 0.90 | 33.0% | [27.6%, 38.9%] | 5.8x |
| 0.15 | 0.85 | 33.9% | [28.5%, 39.7%] | 5.9x |
| 0.20 | 0.80 | 35.7% | [30.4%, 41.0%] | 6.2x |
| 0.25 | 0.75 | 36.6% | [31.4%, 41.9%] | 6.4x |
| 0.30 | 0.70 | 38.6% | [33.6%, 43.6%] | 6.7x |
| 0.35 | 0.65 | 39.0% | [34.0%, 44.1%] | 6.8x |
| 0.40 | 0.60 | 40.2% | [35.3%, 45.2%] | 7.0x |
| 0.45 | 0.55 | 40.3% | [35.3%, 45.2%] | 7.0x |
| 0.50 | 0.50 | 40.3% | [35.1%, 45.6%] | 7.0x |
| 0.55 | 0.45 | 39.4% | [34.2%, 44.7%] | 6.9x |
| 0.60 | 0.40 | 38.5% | [33.3%, 43.9%] | 6.7x |
| 0.65 | 0.35 | 37.9% | [32.5%, 43.5%] | 6.6x |
| 0.70 | 0.30 | 39.7% | [34.3%, 44.9%] | 6.9x |
| 0.75 | 0.25 | 41.3% | [36.0%, 46.4%] | 7.2x |
| 0.80 | 0.20 | 39.3% | [34.0%, 44.6%] | 6.9x |
| 0.85 | 0.15 | 33.7% | [28.7%, 38.8%] | 5.9x |
| 0.90 | 0.10 | 27.6% | [23.6%, 31.9%] | 4.8x |
| 0.95 | 0.05 | 23.3% | [19.8%, 26.9%] | 4.1x |
| 1.00 | 0.00 | 21.7% | [18.7%, 25.1%] | 3.8x |

Best: efficiency 0.75 : fit 0.25 at 41.3%. **17 of 21 splits have a CI overlapping it** — treat a winner inside that band as noise and leave the shipped split alone.

## 4. Guardrailed grid — the trade-off frontier, not a winner

Guardrails: efficiency+fit ≥ 0.50, pick ≤ 0.15, sum = 1. Objective = 0.5·norm(Spearman) + 0.5·coverage. The guardrails are load-bearing: they are what keeps this search away from the degenerate corners above, so a row pressed against `pick ≤ 0.15` is the constraint speaking, not the data.

**Current hand weights:** eff 0.35 · win 0.45 · pick 0.05 · fit 0.15

| eff | win | pick | fit | objective | Spearman | coverage |
|---|---|---|---|---|---|---|
| 0.35 | 0.35 | 0.15 | 0.15 | 0.641 | 0.31 | 62% |
| 0.4 | 0.35 | 0.15 | 0.1 | 0.638 | 0.33 | 61% |
| 0.3 | 0.35 | 0.15 | 0.2 | 0.626 | 0.30 | 60% |
| 0.4 | 0.3 | 0.15 | 0.15 | 0.622 | 0.26 | 61% |
| 0.45 | 0.3 | 0.15 | 0.1 | 0.622 | 0.28 | 60% |
| 0.4 | 0.4 | 0.1 | 0.1 | 0.621 | 0.39 | 55% |
| 0.35 | 0.4 | 0.1 | 0.15 | 0.620 | 0.37 | 55% |
| 0.3 | 0.4 | 0.1 | 0.2 | 0.617 | 0.35 | 56% |
| 0.35 | 0.3 | 0.15 | 0.2 | 0.614 | 0.25 | 61% |
| 0.45 | 0.35 | 0.15 | 0.05 | 0.613 | 0.34 | 56% |
| 0.4 | 0.25 | 0.15 | 0.2 | 0.606 | 0.20 | 61% |
| 0.25 | 0.35 | 0.15 | 0.25 | 0.606 | 0.28 | 57% |
| 0.5 | 0.25 | 0.15 | 0.1 | 0.604 | 0.22 | 60% |
| 0.35 | 0.45 | 0.05 | 0.15 | 0.601 | 0.42 | 49% ←current |
| 0.4 | 0.35 | 0.1 | 0.15 | 0.601 | 0.31 | 54% |

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

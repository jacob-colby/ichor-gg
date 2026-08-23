# Signal-weight calibration

> **Read the leakage probe before the grid.** Both of this metric's targets are also model inputs, so the grid's ranking is partly the metric grading its own input. See `calibrate.py`.

_Input fingerprint: `527eb8f0a586` — items, gods, tags, community builds, weights. Check it against `python -m smite.calibrate --control` before quoting any number below._

## 1. Leakage probe — what the objective actually maximises

Each row deletes the model and hands the metric one of its own inputs. A corner that beats the real blends means the objective cannot select weights.

| Weights | Spearman (pooled) | Within-god | Coverage |
|---|---|---|---|
| win only (Spearman's target verbatim) | 1.000 | +1.00 (positive on 89/89) | 42.3% |
| pick only (community membership) | 0.019 | -0.07 (positive on 41/89) | 92.2% |
| model only (efficiency + fit) | -0.032 | -0.03 (positive on 37/89) | 43.6% |

`win only` scores a perfect Spearman because the score *is* the target. `pick only` all but reproduces the community build. Neither contains any modeling.

## 2. Baseline — what coverage means

A **random** legal 6-item core, drawn 200x per god from the same candidate pool (median 99 items), covers **5.8%** of the community set. Every coverage number below is a multiple of that, not of zero.

## 3. Leakage-free sweep of the model signals

`win` and `pick` held at **zero**, so nothing from the target enters the score. This is the only sweep whose winner may be applied directly.

| efficiency | fit | coverage | 95% CI | vs chance |
|---|---|---|---|---|
| 0.00 | 1.00 | 29.4% | [24.0%, 35.2%] | 5.1x |
| 0.05 | 0.95 | 33.0% | [27.4%, 39.1%] | 5.7x |
| 0.10 | 0.90 | 32.8% | [27.0%, 39.0%] | 5.7x |
| 0.15 | 0.85 | 33.6% | [27.9%, 39.6%] | 5.8x |
| 0.20 | 0.80 | 34.9% | [29.3%, 40.7%] | 6.1x |
| 0.25 | 0.75 | 36.7% | [31.2%, 42.4%] | 6.4x |
| 0.30 | 0.70 | 38.4% | [33.1%, 43.9%] | 6.6x |
| 0.35 | 0.65 | 37.9% | [32.7%, 43.5%] | 6.6x |
| 0.40 | 0.60 | 38.7% | [33.4%, 44.1%] | 6.7x |
| 0.45 | 0.55 | 39.4% | [34.2%, 44.9%] | 6.8x |
| 0.50 | 0.50 | 38.6% | [33.3%, 44.3%] | 6.7x |
| 0.55 | 0.45 | 38.0% | [32.5%, 43.6%] | 6.6x |
| 0.60 | 0.40 | 38.2% | [32.7%, 43.8%] | 6.6x |
| 0.65 | 0.35 | 41.1% | [35.8%, 46.3%] | 7.1x |
| 0.70 | 0.30 | 43.6% | [38.3%, 49.1%] | 7.6x |
| 0.75 | 0.25 | 43.1% | [37.3%, 48.8%] | 7.5x |
| 0.80 | 0.20 | 41.9% | [36.1%, 47.6%] | 7.3x |
| 0.85 | 0.15 | 41.2% | [35.3%, 46.9%] | 7.1x |
| 0.90 | 0.10 | 39.9% | [34.1%, 45.7%] | 6.9x |
| 0.95 | 0.05 | 40.4% | [34.6%, 46.0%] | 7.0x |
| 1.00 | 0.00 | 31.4% | [27.2%, 36.0%] | 5.4x |

Best: efficiency 0.70 : fit 0.30 at 43.6%. **19 of 21 splits have a CI overlapping it** — treat a winner inside that band as noise and leave the shipped split alone.

## 4. Guardrailed grid — the trade-off frontier, not a winner

Guardrails: efficiency+fit ≥ 0.50, pick ≤ 0.15, sum = 1. Objective = 0.5·norm(Spearman) + 0.5·coverage. The guardrails are load-bearing: they are what keeps this search away from the degenerate corners above, so a row pressed against `pick ≤ 0.15` is the constraint speaking, not the data.

**Current hand weights:** eff 0.35 · win 0.45 · pick 0.05 · fit 0.15

| eff | win | pick | fit | objective | Spearman | coverage |
|---|---|---|---|---|---|---|
| 0.35 | 0.35 | 0.15 | 0.15 | 0.623 | 0.28 | 61% |
| 0.4 | 0.35 | 0.15 | 0.1 | 0.623 | 0.28 | 60% |
| 0.4 | 0.4 | 0.1 | 0.1 | 0.611 | 0.33 | 56% |
| 0.35 | 0.4 | 0.1 | 0.15 | 0.609 | 0.33 | 55% |
| 0.4 | 0.3 | 0.15 | 0.15 | 0.607 | 0.23 | 60% |
| 0.3 | 0.35 | 0.15 | 0.2 | 0.606 | 0.27 | 58% |
| 0.45 | 0.35 | 0.15 | 0.05 | 0.605 | 0.28 | 57% |
| 0.45 | 0.3 | 0.15 | 0.1 | 0.604 | 0.23 | 59% |
| 0.35 | 0.45 | 0.05 | 0.15 | 0.597 | 0.37 | 51% ←current |
| 0.4 | 0.35 | 0.1 | 0.15 | 0.596 | 0.27 | 56% |
| 0.3 | 0.4 | 0.1 | 0.2 | 0.596 | 0.32 | 53% |
| 0.35 | 0.3 | 0.15 | 0.2 | 0.596 | 0.22 | 58% |
| 0.25 | 0.35 | 0.15 | 0.25 | 0.594 | 0.26 | 56% |
| 0.45 | 0.25 | 0.15 | 0.15 | 0.593 | 0.18 | 60% |
| 0.4 | 0.25 | 0.15 | 0.2 | 0.591 | 0.17 | 60% |

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
- without Bacchus: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Baron Samedi: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Bastet: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Bellona: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Cabrakan: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Cerberus: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Cernunnos: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Chaac: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Charon: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Chiron: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Chronos: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Cu Chulainn: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Cupid: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Da Ji: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Danzaburou: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Discordia: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Eset: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Fenrir: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Ganesha: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Geb: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Gilgamesh: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Guan Yu: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Hades: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Hecate: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Hercules: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Horus: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Hou Yi: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Hua Mulan: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Hun Batz: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Ishtar: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Ix Chel: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
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
- without Princess Bari: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
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
- without Tsukuyomi: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Ullr: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Vulcan: eff 0.40 · win 0.35 · pick 0.15 · fit 0.10
- without Xbalanque: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Xing Tian: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Yemoja: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Ymir: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15
- without Zeus: eff 0.35 · win 0.35 · pick 0.15 · fit 0.15

**Stability:** 2 distinct fold-winner(s) across 89 folds — stable.

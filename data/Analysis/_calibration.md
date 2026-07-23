# Signal-weight calibration

Guardrails: efficiency+fit ≥ 0.50, pick ≤ 0.15, sum = 1. Objective = 0.5·norm(Spearman) + 0.5·coverage.

**Current hand weights:** {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}

| eff | win | pick | fit | objective | Spearman | coverage |
|---|---|---|---|---|---|---|
| 0.35 | 0.35 | 0.15 | 0.15 | 0.586 | 0.21 | 57% |
| 0.4 | 0.35 | 0.15 | 0.1 | 0.582 | 0.21 | 56% |
| 0.35 | 0.4 | 0.1 | 0.15 | 0.581 | 0.28 | 52% |
| 0.3 | 0.35 | 0.15 | 0.2 | 0.579 | 0.20 | 56% |
| 0.3 | 0.4 | 0.1 | 0.2 | 0.573 | 0.26 | 52% |
| 0.3 | 0.45 | 0.05 | 0.2 | 0.566 | 0.33 | 47% |
| 0.4 | 0.4 | 0.1 | 0.1 | 0.566 | 0.28 | 49% |
| 0.35 | 0.45 | 0.05 | 0.15 | 0.565 | 0.34 | 46% |
| 0.25 | 0.35 | 0.15 | 0.25 | 0.565 | 0.19 | 53% |
| 0.25 | 0.4 | 0.1 | 0.25 | 0.562 | 0.25 | 50% |
| 0.4 | 0.45 | 0.05 | 0.1 | 0.562 | 0.36 | 44% |
| 0.45 | 0.35 | 0.15 | 0.05 | 0.561 | 0.20 | 52% |
| 0.4 | 0.5 | 0.0 | 0.1 | 0.559 | 0.43 | 40% |
| 0.35 | 0.5 | 0.0 | 0.15 | 0.559 | 0.41 | 41% |
| 0.3 | 0.5 | 0.0 | 0.2 | 0.558 | 0.38 | 42% |

## Leave-one-god-out winners

- without Achilles: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Agni: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Ah Puch: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Aladdin: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Amaterasu: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Anhur: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Anubis: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Aphrodite: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Apollo: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Ares: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Artemis: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Artio: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Athena: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Atlas: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Awilix: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Bacchus: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Baron Samedi: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Bastet: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Bellona: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Cabrakan: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Cerberus: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Cernunnos: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Chaac: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Charon: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Chiron: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Chronos: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Cupid: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Da Ji: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Danzaburou: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Discordia: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Eset: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Fenrir: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Ganesha: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Geb: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Gilgamesh: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Guan Yu: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Hades: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Hecate: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Hercules: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Horus: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Hou Yi: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Hua Mulan: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Hun Batz: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Ishtar: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Izanami: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Janus: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Jing Wei: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Jormungandr: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Kali: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Khepri: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Kukulkan: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Loki: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Medusa: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Mercury: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Merlin: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Mordred: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Morgan Le Fay: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Ne Zha: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Neith: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Nemesis: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Nu Wa: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Nut: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Odin: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Osiris: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Pele: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Poseidon: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Princess Bari: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Ra: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Rama: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Ratatoskr: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Scylla: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Sobek: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Sol: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Sun Wukong: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Susano: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Sylvanus: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Thanatos: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without The Morrigan: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Thor: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Tsukuyomi: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Ullr: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Vulcan: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Xbalanque: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Xing Tian: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Yemoja: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Ymir: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}
- without Zeus: {'efficiency': 0.35, 'win': 0.35, 'pick': 0.15, 'fit': 0.15}

**Stability:** 1 distinct fold-winner(s) across 87 folds — stable.

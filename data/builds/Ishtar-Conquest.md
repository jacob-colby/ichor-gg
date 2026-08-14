---
type: smite-build
god: Ishtar
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Passionate Storm
  aspect_pick_rate: 0.16
  aspect_win_rate: 0.67
  slot_order:
  - name: Tyrfing
    pick_rate: 0.42
    win_rate: 0.74
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.19
      win_rate: 0.71
    - name: Dominance
      pick_rate: 0.16
      win_rate: 0.5
  - name: Odysseus' Bow
    pick_rate: 0.22
    win_rate: 0.68
    alternates:
    - name: Toxic Blade
      pick_rate: 0.15
      win_rate: 0.65
    - name: Dagger of Frenzy
      pick_rate: 0.13
      win_rate: 0.53
  - name: Silverbranch Bow
    pick_rate: 0.23
    win_rate: 0.58
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.23
      win_rate: 0.77
    - name: Dominance
      pick_rate: 0.12
      win_rate: 0.46
  - name: The Executioner
    pick_rate: 0.2
    win_rate: 0.57
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.31
      win_rate: 0.67
    - name: Deathbringer
      pick_rate: 0.12
      win_rate: 0.54
  - name: Riptalon
    pick_rate: 0.2
    win_rate: 0.6
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.13
      win_rate: 0.92
    - name: Manchu Bow
      pick_rate: 0.1
      win_rate: 0.5
  - name: Hunter's Bow
    pick_rate: 0.1
    win_rate: 0.57
    alternates:
    - name: Riptalon
      pick_rate: 0.16
      win_rate: 0.75
    - name: Bow
      pick_rate: 0.07
      win_rate: 0.8
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.34
    win_rate: 0.63
  - name: Hunter's Cowl
    pick_rate: 0.2
    win_rate: 0.73
  - name: Gilded Arrow
    pick_rate: 0.16
    win_rate: 0.39
  source_url: https://smitebrain.com/gods/ishtar/
  last_verified: '2026-08-13'
  god_win_rate: 0.6339285714285714
  god_matches_won: 71
  god_matches_played: 112
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-13'
  god_matches_analyzed: 2102
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Berserker's Shield
  - Tyrfing
  - Riptalon
  - Damaru
  - The Crusher
  flex_slots:
  - Damaru
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Lernaean Bow, Berserker''s Shield, Damaru, The Crusher, Golden Blade,
    Jotunn''s Revenge, Demon Blade, Hydra''s Lament, Genji''s Guard, Pharaoh''s Curse,
    Runeforged Hammer, Tekko-Kagi, The Reaper, Breastplate of Valor, Shogun''s Ofuda,
    Musashi''s Dual Swords, Eros'' Bow, Kinetic Cuirass, Rage, Amanita Charm, Oni
    Hunter''s Garb, Avenging Blade, Barbed Carver, Shield Splitter.'
  slot_scores:
    Lernaean Bow:
      total: 0.55
      efficiency: 0.54
      win: 0.58
      pick: 0.0
      fit: 0.66
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.32
    Tyrfing:
      total: 0.61
      efficiency: 0.46
      win: 0.74
      pick: 0.42
      fit: 0.66
    Riptalon:
      total: 0.56
      efficiency: 0.56
      win: 0.6
      pick: 0.43
      fit: 0.45
    Damaru:
      total: 0.55
      efficiency: 0.58
      win: 0.58
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.34
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Berserker's Shield
  - Tyrfing
  - Riptalon
  - Damaru
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Demon Blade
  - Deathbringer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Damaru, Berserker''s Shield, Lernaean Bow, The Crusher, Golden Blade,
    Demon Blade, Jotunn''s Revenge, Genji''s Guard, Hydra''s Lament, Pharaoh''s Curse,
    Runeforged Hammer, Musashi''s Dual Swords, Breastplate of Valor, Tekko-Kagi, The
    Reaper, Shogun''s Ofuda, Rage, Kinetic Cuirass, Eros'' Bow, Amanita Charm, Oni
    Hunter''s Garb, Eye of Providence, Avenging Blade, Shield Splitter.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.3
    Tyrfing:
      total: 0.6
      efficiency: 0.46
      win: 0.74
      pick: 0.42
      fit: 0.6
    Riptalon:
      total: 0.55
      efficiency: 0.56
      win: 0.6
      pick: 0.43
      fit: 0.42
    Damaru:
      total: 0.55
      efficiency: 0.58
      win: 0.58
      pick: 0.0
      fit: 0.57
    Demon Blade:
      total: 0.52
      efficiency: 0.37
      win: 0.58
      pick: 0.0
      fit: 0.88
    Deathbringer:
      total: 0.5
      efficiency: 0.45
      win: 0.54
      pick: 0.2
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Tyrfing
  - Riptalon
  - Amanita Charm
  - Pharaoh's Curse
  flex_slots:
  - Kinetic Cuirass
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Kinetic Cuirass,
    Pharaoh''s Curse, Genji''s Guard, Golden Blade, Oni Hunter''s Garb, The Reaper,
    The Crusher, Shogun''s Ofuda, Lernaean Bow, Damaru, Runeforged Hammer, Chandra''s
    Grace, Jotunn''s Revenge, Breastplate of Valor, Phoenix Feather, Spectral Armor,
    Freya''s Tears, Shifter''s Shield, Erosion, Eye of the Storm, Umbral Link, Eye
    of Providence, Shield Splitter, Hydra''s Lament, Draconic Scale.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.51
    Tyrfing:
      total: 0.58
      efficiency: 0.46
      win: 0.74
      pick: 0.42
      fit: 0.43
    Riptalon:
      total: 0.57
      efficiency: 0.56
      win: 0.6
      pick: 0.43
      fit: 0.57
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.71
    Pharaoh's Curse:
      total: 0.53
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Silverbranch Bow
  - Toxic Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Jotunn''s Revenge, Berserker''s Shield, The Reaper,
    Tekko-Kagi, Lernaean Bow, Damaru, Avenging Blade, Genji''s Guard, Heartseeker,
    Golden Blade, Hydra''s Lament, Titan''s Bane, Screeching Gargoyle, Breastplate
    of Valor, Runeforged Hammer, Pharaoh''s Curse, Stone of Binding, Kinetic Cuirass,
    Void Shield, Amanita Charm, Pendulum Blade, Oni Hunter''s Garb, Eye of Providence.'
  slot_scores:
    Toxic Blade:
      total: 0.53
      efficiency: 0.42
      win: 0.65
      pick: 0.2
      fit: 0.55
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.58
      pick: 0.0
      fit: 0.51
    Tyrfing:
      total: 0.58
      efficiency: 0.46
      win: 0.74
      pick: 0.42
      fit: 0.47
    Riptalon:
      total: 0.58
      efficiency: 0.56
      win: 0.6
      pick: 0.43
      fit: 0.64
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.54
      win: 0.58
      pick: 0.36
      fit: 0.55
    The Crusher:
      total: 0.57
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.61
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Berserker's Shield
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Silverbranch Bow
  - Lernaean Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Golden Blade, Berserker''s Shield, Lernaean Bow, Damaru, The Crusher,
    Jotunn''s Revenge, Genji''s Guard, Pharaoh''s Curse, Hydra''s Lament, Demon Blade,
    Breastplate of Valor, Runeforged Hammer, Shogun''s Ofuda, Tekko-Kagi, Kinetic
    Cuirass, Eros'' Bow, Amanita Charm, Qin''s Blade, The Reaper, Oni Hunter''s Garb,
    Eye of Providence, Yogi''s Necklace.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.54
      win: 0.58
      pick: 0.0
      fit: 0.67
    Lernaean Bow:
      total: 0.53
      efficiency: 0.54
      win: 0.58
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.3
    Tyrfing:
      total: 0.63
      efficiency: 0.46
      win: 0.74
      pick: 0.42
      fit: 0.77
    Riptalon:
      total: 0.58
      efficiency: 0.56
      win: 0.6
      pick: 0.43
      fit: 0.6
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.54
      win: 0.58
      pick: 0.36
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Riptalon
  flex_slots:
  - Breastplate of Valor
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Jotunn''s Revenge,
    Hydra''s Lament, Breastplate of Valor, Berserker''s Shield, Freya''s Tears, The
    Crusher, Shield of the Phoenix, Lernaean Bow, Damaru, Screeching Gargoyle, Chandra''s
    Grace, Golden Blade, Arondight, Pharaoh''s Curse, Kinetic Cuirass, Runeforged
    Hammer, Amanita Charm, Oni Hunter''s Garb, Eye of Providence, Shogun''s Ofuda,
    Pendulum Blade, Gladiator''s Shield, The Reaper, Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.58
      pick: 0.0
      fit: 0.33
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.66
      win: 0.58
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.66
      win: 0.58
      pick: 0.0
      fit: 0.43
    Tyrfing:
      total: 0.57
      efficiency: 0.46
      win: 0.74
      pick: 0.42
      fit: 0.4
    Hydra's Lament:
      total: 0.54
      efficiency: 0.58
      win: 0.58
      pick: 0.0
      fit: 0.53
    Riptalon:
      total: 0.53
      efficiency: 0.56
      win: 0.6
      pick: 0.43
      fit: 0.28
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Damaru
  - The Crusher
  flex_slots:
  - Golden Blade
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Lernaean Bow, Berserker''s Shield, Damaru, The Crusher,
    Golden Blade, Jotunn''s Revenge, Demon Blade, Hydra''s Lament, Genji''s Guard,
    Pharaoh''s Curse, Runeforged Hammer, Tekko-Kagi, The Reaper, Breastplate of Valor,
    Shogun''s Ofuda, Musashi''s Dual Swords, Eros'' Bow, Kinetic Cuirass, Rage, Amanita
    Charm, Oni Hunter''s Garb, Avenging Blade, Barbed Carver, Shield Splitter.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.54
      win: 0.58
      pick: 0.0
      fit: 0.56
    Lernaean Bow:
      total: 0.55
      efficiency: 0.54
      win: 0.58
      pick: 0.0
      fit: 0.66
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.58
      pick: 0.0
      fit: 0.24
    Damaru:
      total: 0.55
      efficiency: 0.58
      win: 0.58
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.34
  starter: *id001
---

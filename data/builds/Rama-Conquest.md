---
type: smite-build
god: Rama
mode: Conquest
builds:
- source: community
  aspect: Aspect of Precision
  aspect_pick_rate: 0.04
  aspect_win_rate: 0.5
  slot_order:
  - name: Tyrfing
    pick_rate: 0.61
    win_rate: 0.54
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.2
      win_rate: 0.56
    - name: Avenging Blade
      pick_rate: 0.08
      win_rate: 0.52
  - name: Odysseus' Bow
    pick_rate: 0.31
    win_rate: 0.5
    alternates:
    - name: Toxic Blade
      pick_rate: 0.18
      win_rate: 0.66
    - name: Dagger of Frenzy
      pick_rate: 0.12
      win_rate: 0.5
  - name: Silverbranch Bow
    pick_rate: 0.17
    win_rate: 0.52
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.16
      win_rate: 0.67
    - name: Riptalon
      pick_rate: 0.13
      win_rate: 0.49
  - name: The Executioner
    pick_rate: 0.2
    win_rate: 0.52
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.23
      win_rate: 0.57
    - name: Riptalon
      pick_rate: 0.12
      win_rate: 0.53
  - name: Riptalon
    pick_rate: 0.12
    win_rate: 0.59
    alternates:
    - name: The Executioner
      pick_rate: 0.14
      win_rate: 0.51
    - name: Silverbranch Bow
      pick_rate: 0.14
      win_rate: 0.64
  - name: Manchu Bow
    pick_rate: 0.13
    win_rate: 0.49
    alternates:
    - name: Bow
      pick_rate: 0.11
      win_rate: 0.53
    - name: Hunter's Bow
      pick_rate: 0.09
      win_rate: 0.55
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.35
    win_rate: 0.57
  - name: Hunter's Cowl
    pick_rate: 0.2
    win_rate: 0.64
  - name: Gilded Arrow
    pick_rate: 0.15
    win_rate: 0.37
  source_url: https://smitebrain.com/gods/rama/
  last_verified: '2026-08-19'
  god_win_rate: 0.5456273764258555
  god_matches_won: 287
  god_matches_played: 526
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-19'
  god_matches_analyzed: 10108
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Toxic Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - The Crusher
  flex_slots:
  - Tyrfing
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Jotunn''s Revenge, Berserker''s Shield, Damaru, Lernaean
    Bow, Golden Blade, The Reaper, Genji''s Guard, Tekko-Kagi, Hydra''s Lament, Runeforged
    Hammer, Dominance, Pharaoh''s Curse, Demon Blade, Breastplate of Valor, Deathbringer,
    Kinetic Cuirass, Amanita Charm, Shogun''s Ofuda, Eye of Providence, Oni Hunter''s
    Garb, Musashi''s Dual Swords, Avenging Blade, Heartseeker, Freya''s Tears, Transcendence.'
  slot_scores:
    Toxic Blade:
      total: 0.52
      efficiency: 0.43
      win: 0.66
      pick: 0.25
      fit: 0.42
    Berserker's Shield:
      total: 0.5
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.38
    Tyrfing:
      total: 0.52
      efficiency: 0.46
      win: 0.54
      pick: 0.61
      fit: 0.54
    Riptalon:
      total: 0.54
      efficiency: 0.53
      win: 0.59
      pick: 0.26
      fit: 0.52
    The Crusher:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.44
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Toxic Blade
  - Genji's Guard
  - Jotunn's Revenge
  - Hydra's Lament
  - Riptalon
  - The Crusher
  flex_slots:
  - Genji's Guard
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, The Crusher, Genji''s Guard, Hydra''s Lament, Berserker''s Shield, Damaru,
    Breastplate of Valor, Lernaean Bow, Golden Blade, The Reaper, Runeforged Hammer,
    Dominance, Oni Hunter''s Garb, Tekko-Kagi, Kinetic Cuirass, Amanita Charm, Freya''s
    Tears, Transcendence, Pharaoh''s Curse, Eye of Providence, Heartseeker, Shield
    of the Phoenix, Avenging Blade, Yogi''s Necklace, Deathbringer, Arondight, Shield
    Splitter.'
  slot_scores:
    Toxic Blade:
      total: 0.5
      efficiency: 0.43
      win: 0.66
      pick: 0.25
      fit: 0.28
    Genji's Guard:
      total: 0.5
      efficiency: 0.69
      win: 0.53
      pick: 0.0
      fit: 0.15
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.44
    Hydra's Lament:
      total: 0.5
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.42
    Riptalon:
      total: 0.52
      efficiency: 0.53
      win: 0.59
      pick: 0.26
      fit: 0.34
    The Crusher:
      total: 0.52
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Toxic Blade
  - Riptalon
  - Damaru
  - Demon Blade
  - The Crusher
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Jotunn''s Revenge, Damaru, Berserker''s Shield, Lernaean
    Bow, Genji''s Guard, Golden Blade, The Reaper, Hydra''s Lament, Tekko-Kagi, Runeforged
    Hammer, Demon Blade, Breastplate of Valor, Pharaoh''s Curse, Dominance, Deathbringer,
    Kinetic Cuirass, Amanita Charm, Eye of Providence, Musashi''s Dual Swords, Oni
    Hunter''s Garb, Shogun''s Ofuda, Freya''s Tears, Heartseeker, Rage, Transcendence.'
  slot_scores:
    Toxic Blade:
      total: 0.52
      efficiency: 0.43
      win: 0.66
      pick: 0.25
      fit: 0.4
    Riptalon:
      total: 0.54
      efficiency: 0.53
      win: 0.59
      pick: 0.26
      fit: 0.5
    Damaru:
      total: 0.5
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.46
    Demon Blade:
      total: 0.46
      efficiency: 0.35
      win: 0.53
      pick: 0.0
      fit: 0.7
    The Crusher:
      total: 0.52
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.42
    Deathbringer:
      total: 0.46
      efficiency: 0.45
      win: 0.53
      pick: 0.0
      fit: 0.46
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Toxic Blade
  - Genji's Guard
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - The Crusher
  flex_slots:
  - Genji's Guard
  - Tyrfing
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, The Crusher, Genji''s Guard, Berserker''s Shield, Hydra''s
    Lament, Damaru, Breastplate of Valor, The Reaper, Lernaean Bow, Golden Blade,
    Tekko-Kagi, Runeforged Hammer, Freya''s Tears, Kinetic Cuirass, Amanita Charm,
    Shield of the Phoenix, Pharaoh''s Curse, Eye of Providence, Oni Hunter''s Garb,
    Pendulum Blade, Dominance, Heartseeker, Screeching Gargoyle, Arondight, Titan''s
    Bane, Chandra''s Grace.'
  slot_scores:
    Toxic Blade:
      total: 0.52
      efficiency: 0.43
      win: 0.66
      pick: 0.25
      fit: 0.37
    Genji's Guard:
      total: 0.5
      efficiency: 0.69
      win: 0.53
      pick: 0.0
      fit: 0.13
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.46
    Tyrfing:
      total: 0.49
      efficiency: 0.46
      win: 0.54
      pick: 0.61
      fit: 0.4
    Riptalon:
      total: 0.53
      efficiency: 0.53
      win: 0.59
      pick: 0.26
      fit: 0.43
    The Crusher:
      total: 0.52
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Toxic Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Riptalon
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - The Crusher
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Kinetic Cuirass,
    The Crusher, The Reaper, Genji''s Guard, Jotunn''s Revenge, Chandra''s Grace,
    Pharaoh''s Curse, Oni Hunter''s Garb, Golden Blade, Runeforged Hammer, Damaru,
    Breastplate of Valor, Phoenix Feather, Freya''s Tears, Spectral Armor, Shogun''s
    Ofuda, Lernaean Bow, Erosion, Shifter''s Shield, Hydra''s Lament, Eye of the Storm,
    Eye of Providence, Shield Splitter, Umbral Link, Leviathan''s Hide, Draconic Scale.'
  slot_scores:
    Toxic Blade:
      total: 0.52
      efficiency: 0.43
      win: 0.66
      pick: 0.25
      fit: 0.41
    Berserker's Shield:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.44
    Riptalon:
      total: 0.56
      efficiency: 0.53
      win: 0.59
      pick: 0.26
      fit: 0.64
    The Crusher:
      total: 0.51
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.33
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.64
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
  - Tyrfing
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
    for this god: The Crusher, Jotunn''s Revenge, The Reaper, Berserker''s Shield,
    Tekko-Kagi, Damaru, Avenging Blade, Genji''s Guard, Lernaean Bow, Golden Blade,
    Hydra''s Lament, Screeching Gargoyle, Heartseeker, Runeforged Hammer, Breastplate
    of Valor, Titan''s Bane, Stone of Binding, Pharaoh''s Curse, Kinetic Cuirass,
    Void Shield, Amanita Charm, Dominance, Pendulum Blade, Eye of Providence, Oni
    Hunter''s Garb, Void Stone.'
  slot_scores:
    Toxic Blade:
      total: 0.54
      efficiency: 0.43
      win: 0.66
      pick: 0.25
      fit: 0.53
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.5
    Tyrfing:
      total: 0.5
      efficiency: 0.46
      win: 0.54
      pick: 0.61
      fit: 0.46
    Riptalon:
      total: 0.56
      efficiency: 0.53
      win: 0.59
      pick: 0.26
      fit: 0.61
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.52
      win: 0.52
      pick: 0.26
      fit: 0.53
    The Crusher:
      total: 0.55
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Silverbranch Bow
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Golden Blade, Jotunn''s Revenge, Berserker''s Shield, Damaru,
    Lernaean Bow, Genji''s Guard, Hydra''s Lament, The Reaper, Tekko-Kagi, Pharaoh''s
    Curse, Breastplate of Valor, Runeforged Hammer, Kinetic Cuirass, Dominance, Amanita
    Charm, Eye of Providence, Oni Hunter''s Garb, Shogun''s Ofuda, Demon Blade, Freya''s
    Tears, Deathbringer, Eros'' Bow, Spectral Armor, Shield of the Phoenix, Qin''s
    Blade.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.54
    Toxic Blade:
      total: 0.54
      efficiency: 0.43
      win: 0.66
      pick: 0.25
      fit: 0.54
    Tyrfing:
      total: 0.53
      efficiency: 0.46
      win: 0.54
      pick: 0.61
      fit: 0.64
    Riptalon:
      total: 0.56
      efficiency: 0.53
      win: 0.59
      pick: 0.26
      fit: 0.62
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.52
      win: 0.52
      pick: 0.26
      fit: 0.54
    The Crusher:
      total: 0.51
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Toxic Blade
  - Genji's Guard
  - Jotunn's Revenge
  - Hydra's Lament
  - Riptalon
  - The Crusher
  flex_slots:
  - The Crusher
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    The Crusher, Hydra''s Lament, Breastplate of Valor, Berserker''s Shield, Freya''s
    Tears, Shield of the Phoenix, Damaru, Lernaean Bow, Screeching Gargoyle, Chandra''s
    Grace, Golden Blade, The Reaper, Kinetic Cuirass, Arondight, Runeforged Hammer,
    Amanita Charm, Pharaoh''s Curse, Eye of Providence, Pendulum Blade, Oni Hunter''s
    Garb, Tekko-Kagi, Dominance, Shogun''s Ofuda, Spectral Armor, Gladiator''s Shield.'
  slot_scores:
    Toxic Blade:
      total: 0.5
      efficiency: 0.43
      win: 0.66
      pick: 0.25
      fit: 0.3
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.53
      pick: 0.0
      fit: 0.28
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.48
    Hydra's Lament:
      total: 0.5
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.47
    Riptalon:
      total: 0.52
      efficiency: 0.53
      win: 0.59
      pick: 0.26
      fit: 0.37
    The Crusher:
      total: 0.5
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.3
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Riptalon
  - Damaru
  - The Crusher
  flex_slots:
  - Riptalon
  - Lernaean Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    Underrated for this god: The Crusher, Jotunn''s Revenge, Berserker''s Shield,
    Damaru, Lernaean Bow, Golden Blade, The Reaper, Genji''s Guard, Tekko-Kagi, Hydra''s
    Lament, Runeforged Hammer, Dominance, Pharaoh''s Curse, Demon Blade, Breastplate
    of Valor, Deathbringer, Kinetic Cuirass, Amanita Charm, Shogun''s Ofuda, Eye of
    Providence, Oni Hunter''s Garb, Musashi''s Dual Swords, Heartseeker, Freya''s
    Tears, Transcendence, Avenging Blade.'
  slot_scores:
    Lernaean Bow:
      total: 0.49
      efficiency: 0.5
      win: 0.53
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.5
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.38
    Riptalon:
      total: 0.54
      efficiency: 0.53
      win: 0.59
      pick: 0.26
      fit: 0.52
    Damaru:
      total: 0.5
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.44
    The Crusher:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.44
  starter: *id001
---

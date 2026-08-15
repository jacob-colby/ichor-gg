---
type: smite-build
god: Ratatoskr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Thickbark
  aspect_pick_rate: 0.36
  aspect_win_rate: 0.48
  slot_order:
  - name: Thistlethorn Acorn
    pick_rate: 0.3
    win_rate: 0.54
    alternates:
    - name: Briskberry Acorn
      pick_rate: 0.29
      win_rate: 0.43
    - name: Ashwhorl Acorn
      pick_rate: 0.25
      win_rate: 0.45
  - name: Briskberry Acorn
    pick_rate: 0.31
    win_rate: 0.52
    alternates:
    - name: Thistlethorn Acorn
      pick_rate: 0.14
      win_rate: 0.36
    - name: Ashwhorl Acorn
      pick_rate: 0.1
      win_rate: 0.5
  - name: Jotunn's Revenge
    pick_rate: 0.19
    win_rate: 0.6
    alternates:
    - name: Briskberry Acorn
      pick_rate: 0.18
      win_rate: 0.5
    - name: Thistlethorn Acorn
      pick_rate: 0.12
      win_rate: 0.11
  - name: Heartseeker
    pick_rate: 0.15
    win_rate: 0.55
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.29
    - name: Barbed Carver
      pick_rate: 0.08
      win_rate: 0.33
  - name: Breastplate of Valor
    pick_rate: 0.1
    win_rate: 0.71
    alternates:
    - name: Heartseeker
      pick_rate: 0.18
      win_rate: 0.46
    - name: Kinetic Cuirass
      pick_rate: 0.07
      win_rate: 0.6
  - name: Medal of Defense
    pick_rate: 0.09
    win_rate: 0.6
    alternates:
    - name: Heartseeker
      pick_rate: 0.16
      win_rate: 0.33
    - name: The Crusher
      pick_rate: 0.07
      win_rate: 0.75
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.28
    win_rate: 0.41
  - name: Bluestone Brooch
    pick_rate: 0.16
    win_rate: 0.54
  - name: Bumba's Hammer
    pick_rate: 0.16
    win_rate: 0.54
  source_url: https://smitebrain.com/gods/ratatoskr/
  last_verified: '2026-08-15'
  god_win_rate: 0.4625
  god_matches_won: 37
  god_matches_played: 80
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-15'
  god_matches_analyzed: 4746
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Breastplate of Valor
  - Jotunn's Revenge
  - The Crusher
  flex_slots:
  - Ashwhorl Acorn
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Hydra''s Lament, Pendulum Blade, Titan''s Bane, Tekko-Kagi,
    Runeforged Hammer, Damaru, Lernaean Bow, Avatar''s Parashu, Golden Blade, Transcendence,
    Avenging Blade, Arondight, Shield Splitter, Eye of the Storm, Tyrfing, Riptalon,
    Dominance, Silverbranch Bow, Deathbringer, Berserker''s Shield, Barbed Carver.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.62
      efficiency: 0.94
      win: 0.45
      pick: 0.25
      fit: 0.52
    Briskberry Acorn:
      total: 0.66
      efficiency: 0.93
      win: 0.52
      pick: 0.42
      fit: 0.52
    Thistlethorn Acorn:
      total: 0.67
      efficiency: 0.92
      win: 0.54
      pick: 0.3
      fit: 0.61
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.64
      win: 0.71
      pick: 0.22
      fit: 0.09
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.64
      win: 0.6
      pick: 0.3
      fit: 1.0
    The Crusher:
      total: 0.72
      efficiency: 0.64
      win: 0.75
      pick: 0.22
      fit: 1.0
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - The Crusher
  flex_slots:
  - Breastplate of Valor
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Hydra''s
    Lament, The Reaper, Runeforged Hammer, Damaru, Transcendence, Pendulum Blade,
    Lernaean Bow, Arondight, Oni Hunter''s Garb, Berserker''s Shield, Golden Blade,
    Freya''s Tears, Titan''s Bane, Tekko-Kagi, Avenging Blade, Dominance, Shield Splitter,
    Amanita Charm, Shield of the Phoenix, Eye of the Storm, Tyrfing.'
  slot_scores:
    Briskberry Acorn:
      total: 0.62
      efficiency: 0.93
      win: 0.52
      pick: 0.42
      fit: 0.29
    Thistlethorn Acorn:
      total: 0.64
      efficiency: 0.92
      win: 0.54
      pick: 0.3
      fit: 0.43
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.64
      win: 0.71
      pick: 0.22
      fit: 0.24
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.64
      win: 0.6
      pick: 0.3
      fit: 0.71
    Hydra's Lament:
      total: 0.54
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.63
    The Crusher:
      total: 0.66
      efficiency: 0.64
      win: 0.75
      pick: 0.22
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Breastplate of Valor
  - Jotunn's Revenge
  - The Crusher
  flex_slots:
  - Breastplate of Valor
  - Ashwhorl Acorn
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Hydra''s Lament, The Reaper, Pendulum Blade, Runeforged Hammer, Titan''s
    Bane, Freya''s Tears, Tekko-Kagi, Riptalon, Arondight, Damaru, Silverbranch Bow,
    Shield of the Phoenix, Berserker''s Shield, Lernaean Bow, Amanita Charm, Screeching
    Gargoyle, Golden Blade, Chandra''s Grace, Eye of Providence, Transcendence, Avenging
    Blade.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.58
      efficiency: 0.94
      win: 0.45
      pick: 0.25
      fit: 0.22
    Briskberry Acorn:
      total: 0.62
      efficiency: 0.93
      win: 0.52
      pick: 0.42
      fit: 0.22
    Thistlethorn Acorn:
      total: 0.65
      efficiency: 0.92
      win: 0.54
      pick: 0.3
      fit: 0.44
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.64
      win: 0.71
      pick: 0.22
      fit: 0.22
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.64
      win: 0.6
      pick: 0.3
      fit: 0.78
    The Crusher:
      total: 0.67
      efficiency: 0.64
      win: 0.75
      pick: 0.22
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Breastplate of Valor
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Berserker''s Shield, The Reaper,
    Runeforged Hammer, Oni Hunter''s Garb, Eye of the Storm, Chandra''s Grace, Erosion,
    Shifter''s Shield, Shield Splitter, Phoenix Feather, Freya''s Tears, Eye of Providence,
    Spectral Armor, Draconic Scale, Riptalon, Golden Blade, Hydra''s Lament, Pharaoh''s
    Curse, Avenging Blade, Leviathan''s Hide.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.61
      efficiency: 0.94
      win: 0.45
      pick: 0.25
      fit: 0.44
    Briskberry Acorn:
      total: 0.65
      efficiency: 0.93
      win: 0.52
      pick: 0.42
      fit: 0.44
    Thistlethorn Acorn:
      total: 0.65
      efficiency: 0.92
      win: 0.54
      pick: 0.3
      fit: 0.48
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.64
      win: 0.71
      pick: 0.22
      fit: 0.21
    The Crusher:
      total: 0.65
      efficiency: 0.64
      win: 0.75
      pick: 0.22
      fit: 0.5
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Breastplate of Valor
  - Jotunn's Revenge
  - The Crusher
  flex_slots:
  - Ashwhorl Acorn
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Reaper, Titan''s Bane, Tekko-Kagi, Pendulum Blade, Riptalon,
    Avenging Blade, Silverbranch Bow, Avatar''s Parashu, Hydra''s Lament, Runeforged
    Hammer, Damaru, Toxic Blade, Lernaean Bow, Screeching Gargoyle, Golden Blade,
    Transcendence, Berserker''s Shield, Shield Splitter, Eye of the Storm, Stone of
    Binding, Tyrfing, Oath-Sworn Spear.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.59
      efficiency: 0.94
      win: 0.45
      pick: 0.25
      fit: 0.33
    Briskberry Acorn:
      total: 0.63
      efficiency: 0.93
      win: 0.52
      pick: 0.42
      fit: 0.33
    Thistlethorn Acorn:
      total: 0.64
      efficiency: 0.92
      win: 0.54
      pick: 0.3
      fit: 0.38
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.64
      win: 0.71
      pick: 0.22
      fit: 0.06
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.64
      win: 0.6
      pick: 0.3
      fit: 1.0
    The Crusher:
      total: 0.72
      efficiency: 0.64
      win: 0.75
      pick: 0.22
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Riptalon
  - The Crusher
  flex_slots:
  - Riptalon
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Golden Blade, Silverbranch Bow, Tyrfing, Berserker''s Shield,
    Lernaean Bow, Toxic Blade, Tekko-Kagi, The Reaper, Hydra''s Lament, Pharaoh''s
    Curse, Dominance, Runeforged Hammer, Damaru, Shogun''s Ofuda, Amanita Charm, Qin''s
    Blade, Eye of Providence, Oni Hunter''s Garb, Eros'' Bow, Freya''s Tears.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.69
    Ashwhorl Acorn:
      total: 0.62
      efficiency: 0.94
      win: 0.45
      pick: 0.25
      fit: 0.48
    Briskberry Acorn:
      total: 0.61
      efficiency: 0.93
      win: 0.52
      pick: 0.42
      fit: 0.17
    Thistlethorn Acorn:
      total: 0.62
      efficiency: 0.92
      win: 0.54
      pick: 0.3
      fit: 0.31
    Riptalon:
      total: 0.55
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.79
    The Crusher:
      total: 0.64
      efficiency: 0.64
      win: 0.75
      pick: 0.22
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Breastplate of Valor
  - Jotunn's Revenge
  - The Crusher
  flex_slots:
  - Briskberry Acorn
  - Ashwhorl Acorn
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Freya''s Tears, Shield
    of the Phoenix, Pendulum Blade, Arondight, Screeching Gargoyle, Chandra''s Grace,
    The Reaper, Gladiator''s Shield, Runeforged Hammer, Berserker''s Shield, Prophetic
    Cloak, Damaru, Amanita Charm, Riptalon, Eye of Providence, Oni Hunter''s Garb,
    Regrowth Striders, Lernaean Bow, Silverbranch Bow, Titan''s Bane.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.57
      efficiency: 0.94
      win: 0.45
      pick: 0.25
      fit: 0.15
    Briskberry Acorn:
      total: 0.6
      efficiency: 0.93
      win: 0.52
      pick: 0.42
      fit: 0.15
    Thistlethorn Acorn:
      total: 0.68
      efficiency: 0.92
      win: 0.54
      pick: 0.3
      fit: 0.65
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.64
      win: 0.71
      pick: 0.22
      fit: 0.5
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.64
      win: 0.6
      pick: 0.3
      fit: 0.85
    The Crusher:
      total: 0.64
      efficiency: 0.64
      win: 0.75
      pick: 0.22
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - Hydra's Lament
  - The Crusher
  flex_slots:
  - Jotunn's Revenge
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Reaper, Hydra''s Lament, Pendulum Blade, Titan''s
    Bane, Tekko-Kagi, Runeforged Hammer, Damaru, Lernaean Bow, Avatar''s Parashu,
    Golden Blade, Transcendence, Avenging Blade, Arondight, Shield Splitter, Eye of
    the Storm, Tyrfing, Riptalon, Dominance, Silverbranch Bow, Deathbringer, Barbed
    Carver, Berserker''s Shield.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.62
      efficiency: 0.94
      win: 0.45
      pick: 0.25
      fit: 0.52
    Briskberry Acorn:
      total: 0.66
      efficiency: 0.93
      win: 0.52
      pick: 0.42
      fit: 0.52
    Thistlethorn Acorn:
      total: 0.67
      efficiency: 0.92
      win: 0.54
      pick: 0.3
      fit: 0.61
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.64
      win: 0.6
      pick: 0.3
      fit: 1.0
    Hydra's Lament:
      total: 0.55
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.71
    The Crusher:
      total: 0.72
      efficiency: 0.64
      win: 0.75
      pick: 0.22
      fit: 1.0
  starter: *id001
---

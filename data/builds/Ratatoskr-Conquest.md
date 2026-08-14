---
type: smite-build
god: Ratatoskr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Thickbark
  aspect_pick_rate: 0.35
  aspect_win_rate: 0.48
  slot_order:
  - name: Briskberry Acorn
    pick_rate: 0.31
    win_rate: 0.4
    alternates:
    - name: Thistlethorn Acorn
      pick_rate: 0.31
      win_rate: 0.45
    - name: Ashwhorl Acorn
      pick_rate: 0.26
      win_rate: 0.41
  - name: Jotunn's Revenge
    pick_rate: 0.12
    win_rate: 0.63
    alternates:
    - name: Briskberry Acorn
      pick_rate: 0.31
      win_rate: 0.45
    - name: Thistlethorn Acorn
      pick_rate: 0.12
      win_rate: 0.38
  - name: Thistlethorn Acorn
    pick_rate: 0.13
    win_rate: 0.13
    alternates:
    - name: Briskberry Acorn
      pick_rate: 0.17
      win_rate: 0.45
    - name: Jotunn's Revenge
      pick_rate: 0.16
      win_rate: 0.4
  - name: Heartseeker
    pick_rate: 0.17
    win_rate: 0.5
    alternates:
    - name: Shield of the Phoenix
      pick_rate: 0.08
      win_rate: 0.8
    - name: Barbed Carver
      pick_rate: 0.08
      win_rate: 0.2
  - name: Breastplate of Valor
    pick_rate: 0.07
    win_rate: 0.75
    alternates:
    - name: Heartseeker
      pick_rate: 0.14
      win_rate: 0.38
    - name: Jotunn's Revenge
      pick_rate: 0.07
      win_rate: 0.5
  - name: Medal of Defense
    pick_rate: 0.11
    win_rate: 0.6
    alternates:
    - name: Heartseeker
      pick_rate: 0.17
      win_rate: 0.25
    - name: Lucerne Hammer
      pick_rate: 0.09
      win_rate: 0.25
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.28
    win_rate: 0.44
  - name: Bluestone Brooch
    pick_rate: 0.18
    win_rate: 0.5
  - name: Bumba's Hammer
    pick_rate: 0.15
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/ratatoskr/
  last_verified: '2026-08-14'
  god_win_rate: 0.4153846153846154
  god_matches_won: 27
  god_matches_played: 65
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-14'
  god_matches_analyzed: 3454
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - The Crusher
  flex_slots:
  - The Crusher
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, The Reaper, Hydra''s Lament, Pendulum Blade, Titan''s Bane,
    Tekko-Kagi, Runeforged Hammer, Damaru, Lernaean Bow, Avatar''s Parashu, Golden
    Blade, Transcendence, Avenging Blade, Arondight, Shield Splitter, Genji''s Guard,
    Eye of the Storm, Tyrfing, Riptalon, Dominance, Silverbranch Bow, Deathbringer,
    Berserker''s Shield, Barbed Carver.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.61
      efficiency: 0.94
      win: 0.41
      pick: 0.26
      fit: 0.52
    Briskberry Acorn:
      total: 0.6
      efficiency: 0.93
      win: 0.4
      pick: 0.31
      fit: 0.52
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.64
      win: 0.75
      pick: 0.15
      fit: 0.09
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.64
      win: 0.63
      pick: 0.16
      fit: 1.0
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.57
      win: 0.8
      pick: 0.13
      fit: 0.09
    The Crusher:
      total: 0.58
      efficiency: 0.64
      win: 0.45
      pick: 0.0
      fit: 1.0
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Hydra's Lament
  flex_slots:
  - Briskberry Acorn
  - Hydra's Lament
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Shield
    of the Phoenix, The Crusher, Hydra''s Lament, Genji''s Guard, The Reaper, Runeforged
    Hammer, Damaru, Transcendence, Pendulum Blade, Lernaean Bow, Arondight, Oni Hunter''s
    Garb, Berserker''s Shield, Golden Blade, Freya''s Tears, Titan''s Bane, Tekko-Kagi,
    Avenging Blade, Dominance, Kinetic Cuirass, Shield Splitter, Amanita Charm, Eye
    of the Storm, Tyrfing.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.57
      efficiency: 0.94
      win: 0.41
      pick: 0.26
      fit: 0.29
    Briskberry Acorn:
      total: 0.57
      efficiency: 0.93
      win: 0.4
      pick: 0.31
      fit: 0.29
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.64
      win: 0.75
      pick: 0.15
      fit: 0.24
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.64
      win: 0.63
      pick: 0.16
      fit: 0.71
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.57
      win: 0.8
      pick: 0.13
      fit: 0.14
    Hydra's Lament:
      total: 0.49
      efficiency: 0.56
      win: 0.45
      pick: 0.0
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - The Crusher
  flex_slots:
  - Briskberry Acorn
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Shield of the Phoenix, The Crusher, Hydra''s Lament, Genji''s Guard, The
    Reaper, Pendulum Blade, Runeforged Hammer, Titan''s Bane, Freya''s Tears, Tekko-Kagi,
    Riptalon, Arondight, Damaru, Silverbranch Bow, Berserker''s Shield, Lernaean Bow,
    Kinetic Cuirass, Amanita Charm, Screeching Gargoyle, Golden Blade, Chandra''s
    Grace, Eye of Providence, Transcendence, Avenging Blade.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.56
      efficiency: 0.94
      win: 0.41
      pick: 0.26
      fit: 0.22
    Briskberry Acorn:
      total: 0.56
      efficiency: 0.93
      win: 0.4
      pick: 0.31
      fit: 0.22
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.64
      win: 0.75
      pick: 0.15
      fit: 0.22
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.64
      win: 0.63
      pick: 0.16
      fit: 0.78
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.57
      win: 0.8
      pick: 0.13
      fit: 0.22
    The Crusher:
      total: 0.53
      efficiency: 0.64
      win: 0.45
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Shield of the Phoenix, Amanita Charm, Kinetic Cuirass, The Crusher,
    Berserker''s Shield, The Reaper, Runeforged Hammer, Genji''s Guard, Oni Hunter''s
    Garb, Eye of the Storm, Chandra''s Grace, Erosion, Shifter''s Shield, Shield Splitter,
    Phoenix Feather, Freya''s Tears, Eye of Providence, Spectral Armor, Draconic Scale,
    Riptalon, Golden Blade, Hydra''s Lament, Pharaoh''s Curse, Avenging Blade, Leviathan''s
    Hide.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.59
      efficiency: 0.94
      win: 0.41
      pick: 0.26
      fit: 0.44
    Briskberry Acorn:
      total: 0.59
      efficiency: 0.93
      win: 0.4
      pick: 0.31
      fit: 0.44
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.64
      win: 0.75
      pick: 0.15
      fit: 0.21
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.64
      win: 0.63
      pick: 0.16
      fit: 0.44
    Shield of the Phoenix:
      total: 0.67
      efficiency: 0.57
      win: 0.8
      pick: 0.13
      fit: 0.73
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.45
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - The Crusher
  flex_slots:
  - Shield of the Phoenix
  - Briskberry Acorn
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, The Reaper, Titan''s Bane, Tekko-Kagi, Pendulum Blade,
    Riptalon, Avenging Blade, Silverbranch Bow, Avatar''s Parashu, Hydra''s Lament,
    Runeforged Hammer, Genji''s Guard, Damaru, Toxic Blade, Lernaean Bow, Screeching
    Gargoyle, Golden Blade, Transcendence, Berserker''s Shield, Shield Splitter, Eye
    of the Storm, Stone of Binding, Tyrfing, Oath-Sworn Spear.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.58
      efficiency: 0.94
      win: 0.41
      pick: 0.26
      fit: 0.33
    Briskberry Acorn:
      total: 0.57
      efficiency: 0.93
      win: 0.4
      pick: 0.31
      fit: 0.33
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.64
      win: 0.75
      pick: 0.15
      fit: 0.06
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.64
      win: 0.63
      pick: 0.16
      fit: 1.0
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.8
      pick: 0.13
      fit: 0.06
    The Crusher:
      total: 0.58
      efficiency: 0.64
      win: 0.45
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Ashwhorl Acorn
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Riptalon
  flex_slots:
  - Riptalon
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, The Crusher, Golden Blade, Silverbranch Bow, Tyrfing, Berserker''s
    Shield, Lernaean Bow, Toxic Blade, Tekko-Kagi, The Reaper, Genji''s Guard, Hydra''s
    Lament, Pharaoh''s Curse, Dominance, Runeforged Hammer, Damaru, Shogun''s Ofuda,
    Kinetic Cuirass, Amanita Charm, Qin''s Blade, Eye of Providence, Oni Hunter''s
    Garb, Eros'' Bow, Freya''s Tears.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.53
      win: 0.45
      pick: 0.0
      fit: 0.69
    Ashwhorl Acorn:
      total: 0.6
      efficiency: 0.94
      win: 0.41
      pick: 0.26
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.64
      win: 0.75
      pick: 0.15
      fit: 0.04
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.63
      pick: 0.16
      fit: 0.37
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.8
      pick: 0.13
      fit: 0.04
    Riptalon:
      total: 0.51
      efficiency: 0.53
      win: 0.45
      pick: 0.0
      fit: 0.79
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  flex_slots:
  - Briskberry Acorn
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Shield of the Phoenix, Genji''s Guard,
    Hydra''s Lament, The Crusher, Freya''s Tears, Pendulum Blade, Arondight, Screeching
    Gargoyle, Chandra''s Grace, The Reaper, Gladiator''s Shield, Runeforged Hammer,
    Berserker''s Shield, Prophetic Cloak, Kinetic Cuirass, Damaru, Amanita Charm,
    Riptalon, Eye of Providence, Oni Hunter''s Garb, Regrowth Striders, Lernaean Bow,
    Silverbranch Bow, Titan''s Bane.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.55
      efficiency: 0.94
      win: 0.41
      pick: 0.26
      fit: 0.15
    Briskberry Acorn:
      total: 0.54
      efficiency: 0.93
      win: 0.4
      pick: 0.31
      fit: 0.15
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.45
      pick: 0.0
      fit: 0.5
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.64
      win: 0.75
      pick: 0.15
      fit: 0.5
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.64
      win: 0.63
      pick: 0.16
      fit: 0.85
    Shield of the Phoenix:
      total: 0.64
      efficiency: 0.57
      win: 0.8
      pick: 0.13
      fit: 0.5
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
    Underrated for this god: The Crusher, The Reaper, Hydra''s Lament, Pendulum Blade,
    Titan''s Bane, Tekko-Kagi, Runeforged Hammer, Damaru, Lernaean Bow, Avatar''s
    Parashu, Golden Blade, Transcendence, Avenging Blade, Arondight, Shield Splitter,
    Genji''s Guard, Eye of the Storm, Tyrfing, Riptalon, Dominance, Silverbranch Bow,
    Deathbringer, Barbed Carver, Berserker''s Shield.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.61
      efficiency: 0.94
      win: 0.41
      pick: 0.26
      fit: 0.52
    Briskberry Acorn:
      total: 0.6
      efficiency: 0.93
      win: 0.4
      pick: 0.31
      fit: 0.52
    Thistlethorn Acorn:
      total: 0.48
      efficiency: 0.92
      win: 0.13
      pick: 0.2
      fit: 0.61
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.64
      win: 0.63
      pick: 0.16
      fit: 1.0
    Hydra's Lament:
      total: 0.51
      efficiency: 0.56
      win: 0.45
      pick: 0.0
      fit: 0.71
    The Crusher:
      total: 0.58
      efficiency: 0.64
      win: 0.45
      pick: 0.0
      fit: 1.0
  starter: *id001
---

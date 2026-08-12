---
type: smite-build
god: Ratatoskr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Thickbark
  aspect_pick_rate: 0.44
  aspect_win_rate: 0.57
  slot_order:
  - name: Thistlethorn Acorn
    pick_rate: 0.31
    win_rate: 0.51
    alternates:
    - name: Ashwhorl Acorn
      pick_rate: 0.27
      win_rate: 0.56
    - name: Briskberry Acorn
      pick_rate: 0.26
      win_rate: 0.54
  - name: Briskberry Acorn
    pick_rate: 0.42
    win_rate: 0.54
    alternates:
    - name: Thistlethorn Acorn
      pick_rate: 0.13
      win_rate: 0.59
    - name: Jotunn's Revenge
      pick_rate: 0.09
      win_rate: 0.45
  - name: Jotunn's Revenge
    pick_rate: 0.2
    win_rate: 0.48
    alternates:
    - name: Thistlethorn Acorn
      pick_rate: 0.15
      win_rate: 0.6
    - name: Briskberry Acorn
      pick_rate: 0.15
      win_rate: 0.47
  - name: Shifter's Shield
    pick_rate: 0.13
    win_rate: 0.48
    alternates:
    - name: Heartseeker
      pick_rate: 0.12
      win_rate: 0.44
    - name: Shield of the Phoenix
      pick_rate: 0.08
      win_rate: 0.5
  - name: Heartseeker
    pick_rate: 0.12
    win_rate: 0.66
    alternates:
    - name: Titan's Bane
      pick_rate: 0.11
      win_rate: 0.53
    - name: Shield of the Phoenix
      pick_rate: 0.08
      win_rate: 0.7
  - name: Titan's Bane
    pick_rate: 0.08
    win_rate: 0.55
    alternates:
    - name: Heartseeker
      pick_rate: 0.08
      win_rate: 0.38
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.65
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.24
    win_rate: 0.64
  - name: Bumba's Hammer
    pick_rate: 0.2
    win_rate: 0.51
  - name: Bluestone Pendant
    pick_rate: 0.17
    win_rate: 0.49
  source_url: https://smitebrain.com/gods/ratatoskr/
  last_verified: '2026-08-11'
  god_win_rate: 0.532394366197183
  god_matches_won: 189
  god_matches_played: 355
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-11'
  god_matches_analyzed: 18835
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - The Crusher
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, The Reaper, Hydra''s Lament, Pendulum Blade, Tekko-Kagi,
    Runeforged Hammer, Lernaean Bow, Damaru, Avatar''s Parashu, Golden Blade, Avenging
    Blade, Shield Splitter, Arondight, Riptalon, Dominance, Eye of the Storm, Tyrfing,
    Silverbranch Bow, Breastplate of Valor, Berserker''s Shield, Barbed Carver, Deathbringer,
    Transcendence.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.68
      efficiency: 0.96
      win: 0.56
      pick: 0.27
      fit: 0.52
    Briskberry Acorn:
      total: 0.68
      efficiency: 0.94
      win: 0.54
      pick: 0.57
      fit: 0.52
    Thistlethorn Acorn:
      total: 0.66
      efficiency: 0.92
      win: 0.51
      pick: 0.31
      fit: 0.61
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.66
      win: 0.48
      pick: 0.31
      fit: 1.0
    The Crusher:
      total: 0.62
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.62
      efficiency: 0.45
      win: 0.66
      pick: 0.26
      fit: 1.0
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Genji's Guard
  - Jotunn's Revenge
  - The Crusher
  flex_slots:
  - Jotunn's Revenge
  - The Crusher
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The Crusher, Hydra''s Lament, Breastplate of Valor, The Reaper, Pendulum
    Blade, Riptalon, Runeforged Hammer, Silverbranch Bow, Tekko-Kagi, Freya''s Tears,
    Berserker''s Shield, Lernaean Bow, Damaru, Arondight, Kinetic Cuirass, Golden
    Blade, Amanita Charm, Screeching Gargoyle, Oni Hunter''s Garb, Chandra''s Grace,
    Avatar''s Parashu, Eye of Providence.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.63
      efficiency: 0.96
      win: 0.56
      pick: 0.27
      fit: 0.22
    Briskberry Acorn:
      total: 0.63
      efficiency: 0.94
      win: 0.54
      pick: 0.57
      fit: 0.22
    Thistlethorn Acorn:
      total: 0.63
      efficiency: 0.92
      win: 0.51
      pick: 0.31
      fit: 0.44
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.65
      pick: 0.25
      fit: 0.22
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.66
      win: 0.48
      pick: 0.31
      fit: 0.78
    The Crusher:
      total: 0.57
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Berserker''s Shield, The Crusher, The
    Reaper, Oni Hunter''s Garb, Runeforged Hammer, Eye of the Storm, Riptalon, Chandra''s
    Grace, Shield Splitter, Erosion, Phoenix Feather, Freya''s Tears, Breastplate
    of Valor, Eye of Providence, Spectral Armor, Pharaoh''s Curse, Draconic Scale,
    Hydra''s Lament, Golden Blade, Leviathan''s Hide, Avenging Blade.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.67
      efficiency: 0.96
      win: 0.56
      pick: 0.27
      fit: 0.44
    Briskberry Acorn:
      total: 0.67
      efficiency: 0.94
      win: 0.54
      pick: 0.57
      fit: 0.44
    Thistlethorn Acorn:
      total: 0.64
      efficiency: 0.92
      win: 0.51
      pick: 0.31
      fit: 0.48
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.65
      pick: 0.25
      fit: 0.21
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.66
    Shield of the Phoenix:
      total: 0.63
      efficiency: 0.57
      win: 0.7
      pick: 0.17
      fit: 0.73
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Jotunn's Revenge
  - The Crusher
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, The Reaper, Tekko-Kagi, Pendulum Blade, Riptalon, Silverbranch
    Bow, Avenging Blade, Hydra''s Lament, Avatar''s Parashu, Runeforged Hammer, Lernaean
    Bow, Damaru, Screeching Gargoyle, Toxic Blade, Breastplate of Valor, Berserker''s
    Shield, Golden Blade, Shield Splitter, Stone of Binding, Dominance, Eye of the
    Storm, Oath-Sworn Spear, Tyrfing.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.65
      efficiency: 0.96
      win: 0.56
      pick: 0.27
      fit: 0.33
    Briskberry Acorn:
      total: 0.65
      efficiency: 0.94
      win: 0.54
      pick: 0.57
      fit: 0.33
    Thistlethorn Acorn:
      total: 0.62
      efficiency: 0.92
      win: 0.51
      pick: 0.31
      fit: 0.38
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.66
      win: 0.48
      pick: 0.31
      fit: 1.0
    The Crusher:
      total: 0.62
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.62
      efficiency: 0.45
      win: 0.66
      pick: 0.26
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Genji's Guard
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Genji's Guard
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Silverbranch Bow, Golden Blade, Berserker''s Shield, The Crusher,
    Tyrfing, Lernaean Bow, Tekko-Kagi, Toxic Blade, Dominance, Hydra''s Lament, Pharaoh''s
    Curse, The Reaper, Breastplate of Valor, Runeforged Hammer, Shogun''s Ofuda, Damaru,
    Eros'' Bow, Qin''s Blade, Kinetic Cuirass, Amanita Charm, Oni Hunter''s Garb,
    Eye of Providence, Freya''s Tears.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.67
      efficiency: 0.96
      win: 0.56
      pick: 0.27
      fit: 0.48
    Briskberry Acorn:
      total: 0.62
      efficiency: 0.94
      win: 0.54
      pick: 0.57
      fit: 0.17
    Thistlethorn Acorn:
      total: 0.61
      efficiency: 0.92
      win: 0.51
      pick: 0.31
      fit: 0.31
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.65
      pick: 0.25
      fit: 0.04
    Riptalon:
      total: 0.56
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.54
      win: 0.55
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Ashwhorl Acorn
  - Briskberry Acorn
  - Thistlethorn Acorn
  - Genji's Guard
  - Jotunn's Revenge
  - Hydra's Lament
  flex_slots:
  - Jotunn's Revenge
  - Hydra's Lament
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
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Breastplate of Valor,
    The Crusher, Freya''s Tears, Pendulum Blade, Arondight, Screeching Gargoyle, Chandra''s
    Grace, Berserker''s Shield, Gladiator''s Shield, The Reaper, Runeforged Hammer,
    Riptalon, Lernaean Bow, Damaru, Prophetic Cloak, Kinetic Cuirass, Amanita Charm,
    Silverbranch Bow, Oni Hunter''s Garb, Eye of Providence, Regrowth Striders, Golden
    Blade.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.62
      efficiency: 0.96
      win: 0.56
      pick: 0.27
      fit: 0.15
    Briskberry Acorn:
      total: 0.62
      efficiency: 0.94
      win: 0.54
      pick: 0.57
      fit: 0.15
    Thistlethorn Acorn:
      total: 0.66
      efficiency: 0.92
      win: 0.51
      pick: 0.31
      fit: 0.65
    Genji's Guard:
      total: 0.63
      efficiency: 0.71
      win: 0.65
      pick: 0.25
      fit: 0.5
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.66
      win: 0.48
      pick: 0.31
      fit: 0.85
    Hydra's Lament:
      total: 0.56
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.75
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
  - The Crusher
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, The Reaper, Hydra''s Lament, Pendulum Blade,
    Tekko-Kagi, Runeforged Hammer, Lernaean Bow, Damaru, Avatar''s Parashu, Golden
    Blade, Avenging Blade, Shield Splitter, Arondight, Riptalon, Dominance, Eye of
    the Storm, Tyrfing, Silverbranch Bow, Breastplate of Valor, Berserker''s Shield,
    Barbed Carver, Deathbringer, Transcendence.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.68
      efficiency: 0.96
      win: 0.56
      pick: 0.27
      fit: 0.52
    Briskberry Acorn:
      total: 0.68
      efficiency: 0.94
      win: 0.54
      pick: 0.57
      fit: 0.52
    Thistlethorn Acorn:
      total: 0.66
      efficiency: 0.92
      win: 0.51
      pick: 0.31
      fit: 0.61
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.66
      win: 0.48
      pick: 0.31
      fit: 1.0
    Hydra's Lament:
      total: 0.56
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.71
    The Crusher:
      total: 0.62
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 1.0
  starter: *id001
---

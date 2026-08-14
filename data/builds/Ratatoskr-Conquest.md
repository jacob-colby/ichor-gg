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
  - Shield of the Phoenix
  - The Crusher
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, The Reaper, Hydra''s Lament, Titan''s Bane, Pendulum Blade,
    Tekko-Kagi, Runeforged Hammer, Lernaean Bow, Damaru, Avatar''s Parashu, Golden
    Blade, Genji''s Guard, Avenging Blade, Shield Splitter, Arondight, Riptalon, Dominance,
    Eye of the Storm, Tyrfing, Silverbranch Bow, Berserker''s Shield, Deathbringer,
    Transcendence, Barbed Carver.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.61
      efficiency: 0.96
      win: 0.41
      pick: 0.26
      fit: 0.52
    Briskberry Acorn:
      total: 0.6
      efficiency: 0.94
      win: 0.4
      pick: 0.31
      fit: 0.52
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.66
      win: 0.75
      pick: 0.15
      fit: 0.09
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.66
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
      total: 0.57
      efficiency: 0.63
      win: 0.45
      pick: 0.0
      fit: 1.0
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
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
    Reaper, Pendulum Blade, Riptalon, Titan''s Bane, Runeforged Hammer, Silverbranch
    Bow, Tekko-Kagi, Freya''s Tears, Berserker''s Shield, Lernaean Bow, Damaru, Arondight,
    Kinetic Cuirass, Golden Blade, Amanita Charm, Screeching Gargoyle, Oni Hunter''s
    Garb, Chandra''s Grace, Avatar''s Parashu, Eye of Providence.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.57
      efficiency: 0.96
      win: 0.41
      pick: 0.26
      fit: 0.22
    Briskberry Acorn:
      total: 0.56
      efficiency: 0.94
      win: 0.4
      pick: 0.31
      fit: 0.22
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.66
      win: 0.75
      pick: 0.15
      fit: 0.22
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.66
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
      total: 0.52
      efficiency: 0.63
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
    this god: Shield of the Phoenix, Amanita Charm, Kinetic Cuirass, Berserker''s
    Shield, The Crusher, The Reaper, Genji''s Guard, Oni Hunter''s Garb, Runeforged
    Hammer, Eye of the Storm, Riptalon, Chandra''s Grace, Shifter''s Shield, Shield
    Splitter, Erosion, Phoenix Feather, Freya''s Tears, Eye of Providence, Spectral
    Armor, Pharaoh''s Curse, Draconic Scale, Hydra''s Lament, Golden Blade, Leviathan''s
    Hide, Avenging Blade.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.6
      efficiency: 0.96
      win: 0.41
      pick: 0.26
      fit: 0.44
    Briskberry Acorn:
      total: 0.59
      efficiency: 0.94
      win: 0.4
      pick: 0.31
      fit: 0.44
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.66
      win: 0.75
      pick: 0.15
      fit: 0.21
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.66
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
    Riptalon, Silverbranch Bow, Avenging Blade, Hydra''s Lament, Avatar''s Parashu,
    Genji''s Guard, Runeforged Hammer, Lernaean Bow, Damaru, Screeching Gargoyle,
    Toxic Blade, Berserker''s Shield, Golden Blade, Shield Splitter, Stone of Binding,
    Dominance, Eye of the Storm, Oath-Sworn Spear, Tyrfing.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.58
      efficiency: 0.96
      win: 0.41
      pick: 0.26
      fit: 0.33
    Briskberry Acorn:
      total: 0.57
      efficiency: 0.94
      win: 0.4
      pick: 0.31
      fit: 0.33
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.66
      win: 0.75
      pick: 0.15
      fit: 0.06
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.66
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
      total: 0.57
      efficiency: 0.63
      win: 0.45
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Ashwhorl Acorn
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Riptalon
  - Silverbranch Bow
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
    this god: Riptalon, Silverbranch Bow, Golden Blade, Berserker''s Shield, The Crusher,
    Tyrfing, Lernaean Bow, Genji''s Guard, Tekko-Kagi, Toxic Blade, Dominance, Hydra''s
    Lament, Pharaoh''s Curse, The Reaper, Runeforged Hammer, Shogun''s Ofuda, Damaru,
    Eros'' Bow, Qin''s Blade, Kinetic Cuirass, Amanita Charm, Oni Hunter''s Garb,
    Eye of Providence, Freya''s Tears.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.6
      efficiency: 0.96
      win: 0.41
      pick: 0.26
      fit: 0.48
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.66
      win: 0.75
      pick: 0.15
      fit: 0.04
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.66
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
      total: 0.52
      efficiency: 0.56
      win: 0.45
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.5
      efficiency: 0.54
      win: 0.45
      pick: 0.0
      fit: 0.69
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Shield of the Phoenix, Genji''s Guard,
    Hydra''s Lament, The Crusher, Freya''s Tears, Pendulum Blade, Arondight, Screeching
    Gargoyle, Chandra''s Grace, Berserker''s Shield, Gladiator''s Shield, The Reaper,
    Runeforged Hammer, Riptalon, Lernaean Bow, Damaru, Prophetic Cloak, Kinetic Cuirass,
    Amanita Charm, Silverbranch Bow, Oni Hunter''s Garb, Eye of Providence, Regrowth
    Striders, Golden Blade.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.55
      efficiency: 0.96
      win: 0.41
      pick: 0.26
      fit: 0.15
    Briskberry Acorn:
      total: 0.55
      efficiency: 0.94
      win: 0.4
      pick: 0.31
      fit: 0.15
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.45
      pick: 0.0
      fit: 0.5
    Breastplate of Valor:
      total: 0.65
      efficiency: 0.66
      win: 0.75
      pick: 0.15
      fit: 0.5
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.66
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
    Underrated for this god: The Crusher, The Reaper, Hydra''s Lament, Titan''s Bane,
    Pendulum Blade, Tekko-Kagi, Runeforged Hammer, Lernaean Bow, Damaru, Avatar''s
    Parashu, Golden Blade, Genji''s Guard, Avenging Blade, Shield Splitter, Arondight,
    Riptalon, Dominance, Eye of the Storm, Tyrfing, Silverbranch Bow, Berserker''s
    Shield, Barbed Carver, Deathbringer, Transcendence.'
  slot_scores:
    Ashwhorl Acorn:
      total: 0.61
      efficiency: 0.96
      win: 0.41
      pick: 0.26
      fit: 0.52
    Briskberry Acorn:
      total: 0.6
      efficiency: 0.94
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
      total: 0.67
      efficiency: 0.66
      win: 0.63
      pick: 0.16
      fit: 1.0
    Hydra's Lament:
      total: 0.51
      efficiency: 0.58
      win: 0.45
      pick: 0.0
      fit: 0.71
    The Crusher:
      total: 0.57
      efficiency: 0.63
      win: 0.45
      pick: 0.0
      fit: 1.0
  starter: *id001
---

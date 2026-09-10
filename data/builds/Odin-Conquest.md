---
type: smite-build
god: Odin
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.47
    win_rate: 0.73
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.5
    - name: Pendulum Blade
      pick_rate: 0.09
      win_rate: 1.0
  - name: Breastplate of Valor
    pick_rate: 0.22
    win_rate: 0.43
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.16
      win_rate: 0.8
    - name: Jotunn's Revenge
      pick_rate: 0.13
      win_rate: 0.75
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.13
      win_rate: 0.25
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 1.0
  - name: Freya's Tears
    pick_rate: 0.1
    win_rate: 0.0
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.33
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.67
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 1.0
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.5
  - name: Mana Tome
    pick_rate: 0.14
    win_rate: 1.0
    alternates:
    - name: Titan's Bane
      pick_rate: 0.14
      win_rate: 0.5
    - name: Blinking Abyss
      pick_rate: 0.07
      win_rate: 1.0
  community_starters:
  - name: Bumba's Cudgel
    pick_rate: 0.41
    win_rate: 0.77
  - name: Bumba's Hammer
    pick_rate: 0.28
    win_rate: 0.67
  - name: Bluestone Brooch
    pick_rate: 0.09
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/odin/
  last_verified: '2026-09-10'
  god_win_rate: 0.6875
  god_matches_won: 22
  god_matches_played: 32
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-10'
  god_matches_analyzed: 1308
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - Shifter's Shield
  - Pendulum Blade
  - Amanita Charm
  flex_slots:
  - Hydra's Lament
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged Hammer,
    Eye of the Storm, Berserker''s Shield, Erosion, Eye of Providence, Draconic Scale,
    Shield of the Phoenix, Stone of Binding, Heartseeker, Magi''s Cloak, Avenging
    Blade, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, The Crusher, Hide
    of the Nemean Lion, Leviathan''s Hide, Void Shield, Stampede, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.72
      win: 0.73
      pick: 0.47
      fit: 0.46
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.73
      pick: 0.0
      fit: 0.64
    Hydra's Lament:
      total: 0.62
      efficiency: 0.54
      win: 0.8
      pick: 0.22
      fit: 0.41
    Shifter's Shield:
      total: 0.73
      efficiency: 0.55
      win: 1.0
      pick: 0.2
      fit: 0.54
    Pendulum Blade:
      total: 0.67
      efficiency: 0.42
      win: 1.0
      pick: 0.09
      fit: 0.46
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.73
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Shifter's Shield
  - Pendulum Blade
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Shifter's Shield
  - Pendulum Blade
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Amanita
    Charm, Kinetic Cuirass, Shield Splitter, Runeforged Hammer, Heartseeker, Berserker''s
    Shield, Eye of the Storm, Shield of the Phoenix, Erosion, Stone of Binding, Eye
    of Providence, Avenging Blade, Draconic Scale, Screeching Gargoyle, Magi''s Cloak,
    The Crusher, Daybreak Gavel, Oni Hunter''s Garb, Transcendence, Midgardian Mail,
    Mantle Of Discord, The Reaper, Arondight.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.72
      win: 0.73
      pick: 0.47
      fit: 0.45
    Hydra's Lament:
      total: 0.63
      efficiency: 0.54
      win: 0.8
      pick: 0.22
      fit: 0.44
    Shifter's Shield:
      total: 0.71
      efficiency: 0.55
      win: 1.0
      pick: 0.2
      fit: 0.36
    Pendulum Blade:
      total: 0.66
      efficiency: 0.42
      win: 1.0
      pick: 0.09
      fit: 0.39
    Heartseeker:
      total: 0.58
      efficiency: 0.47
      win: 0.73
      pick: 0.0
      fit: 0.56
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.73
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Shifter's Shield
  - Pendulum Blade
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Hydra's Lament
  - Shifter's Shield
  - Pendulum Blade
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Runeforged Hammer,
    The Reaper, Shield Splitter, Eye of the Storm, Berserker''s Shield, Erosion, Yogi''s
    Necklace, Eye of Providence, Draconic Scale, Phoenix Feather, Avenging Blade,
    Heartseeker, Chandra''s Grace, Glorious Pridwen, Stone of Binding, Midgardian
    Mail, Daybreak Gavel, The Crusher, Hide of the Nemean Lion, Magi''s Cloak.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.72
      win: 0.73
      pick: 0.47
      fit: 0.48
    Shield of the Phoenix:
      total: 0.63
      efficiency: 0.53
      win: 0.73
      pick: 0.0
      fit: 0.77
    Hydra's Lament:
      total: 0.62
      efficiency: 0.54
      win: 0.8
      pick: 0.22
      fit: 0.42
    Shifter's Shield:
      total: 0.73
      efficiency: 0.55
      win: 1.0
      pick: 0.2
      fit: 0.52
    Pendulum Blade:
      total: 0.67
      efficiency: 0.42
      win: 1.0
      pick: 0.09
      fit: 0.48
    Amanita Charm:
      total: 0.68
      efficiency: 0.65
      win: 0.73
      pick: 0.0
      fit: 0.82
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Shifter's Shield
  - Pendulum Blade
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Jotunn's Revenge
  - Hydra's Lament
  - Shifter's Shield
  - Pendulum Blade
  - Amanita Charm
  flex_slots:
  - Hydra's Lament
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Pendulum Blade, Amanita Charm, Stone of Binding, Kinetic Cuirass,
    Avenging Blade, Screeching Gargoyle, Void Shield, Heartseeker, Shield Splitter,
    Void Stone, Runeforged Hammer, Berserker''s Shield, The Crusher, Eye of the Storm,
    The Reaper, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix,
    Magi''s Cloak, Avatar''s Parashu, Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Stone of Binding:
      total: 0.61
      efficiency: 0.51
      win: 0.73
      pick: 0.0
      fit: 0.71
    Jotunn's Revenge:
      total: 0.69
      efficiency: 0.72
      win: 0.73
      pick: 0.47
      fit: 0.56
    Hydra's Lament:
      total: 0.61
      efficiency: 0.54
      win: 0.8
      pick: 0.22
      fit: 0.35
    Shifter's Shield:
      total: 0.72
      efficiency: 0.55
      win: 1.0
      pick: 0.2
      fit: 0.44
    Pendulum Blade:
      total: 0.69
      efficiency: 0.42
      win: 1.0
      pick: 0.09
      fit: 0.56
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.73
      pick: 0.0
      fit: 0.44
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Shifter's Shield
  - Pendulum Blade
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Berserker's Shield
  - Shifter's Shield
  - Riptalon
  - Pendulum Blade
  flex_slots:
  - Golden Blade
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Golden Blade, Riptalon,
    Tyrfing, Silverbranch Bow, Shield Splitter, Runeforged Hammer, Pharaoh''s Curse,
    Lernaean Bow, Toxic Blade, Shogun''s Ofuda, Erosion, The Reaper, Stone of Binding,
    Eye of Providence, Eye of the Storm, Shield of the Phoenix, Tekko-Kagi, Draconic
    Scale, Magi''s Cloak, Heartseeker, Daybreak Gavel.'
  slot_scores:
    Golden Blade:
      total: 0.59
      efficiency: 0.52
      win: 0.73
      pick: 0.0
      fit: 0.52
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.73
      pick: 0.47
      fit: 0.27
    Berserker's Shield:
      total: 0.63
      efficiency: 0.68
      win: 0.73
      pick: 0.0
      fit: 0.42
    Shifter's Shield:
      total: 0.71
      efficiency: 0.55
      win: 1.0
      pick: 0.2
      fit: 0.35
    Riptalon:
      total: 0.58
      efficiency: 0.51
      win: 0.73
      pick: 0.0
      fit: 0.48
    Pendulum Blade:
      total: 0.64
      efficiency: 0.42
      win: 1.0
      pick: 0.09
      fit: 0.27
  community_ordered:
  - Jotunn's Revenge
  - Shifter's Shield
  - Pendulum Blade
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - Shifter's Shield
  - Pendulum Blade
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Pendulum Blade, Amanita Charm, Kinetic
    Cuirass, Shield of the Phoenix, Screeching Gargoyle, Berserker''s Shield, Shield
    Splitter, Runeforged Hammer, Prophetic Cloak, Erosion, Eye of Providence, Stone
    of Binding, Gladiator''s Shield, Draconic Scale, Eye of the Storm, Arondight,
    Magi''s Cloak, Eye of Erebus, Mantle Of Discord, Midgardian Mail, Daybreak Gavel,
    Heartseeker, Glorious Pridwen, Hide of the Nemean Lion.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.68
      efficiency: 0.72
      win: 0.73
      pick: 0.47
      fit: 0.5
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.73
      pick: 0.0
      fit: 0.51
    Hydra's Lament:
      total: 0.63
      efficiency: 0.54
      win: 0.8
      pick: 0.22
      fit: 0.48
    Shifter's Shield:
      total: 0.71
      efficiency: 0.55
      win: 1.0
      pick: 0.2
      fit: 0.41
    Pendulum Blade:
      total: 0.68
      efficiency: 0.42
      win: 1.0
      pick: 0.09
      fit: 0.5
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.73
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Shifter's Shield
  - Pendulum Blade
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Genji's Guard
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged
    Hammer, Eye of the Storm, Berserker''s Shield, Erosion, Eye of Providence, Draconic
    Scale, Shield of the Phoenix, Stone of Binding, Heartseeker, Magi''s Cloak, Avenging
    Blade, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, The Crusher, Hide
    of the Nemean Lion, Leviathan''s Hide, Void Shield, Stampede, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.72
      win: 0.73
      pick: 0.47
      fit: 0.46
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.73
      pick: 0.0
      fit: 0.64
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.2
      fit: 0.29
    Shield Splitter:
      total: 0.61
      efficiency: 0.55
      win: 0.73
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.3
      efficiency: 0.61
      win: 0.0
      pick: 0.17
      fit: 0.49
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.73
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Jotunn's Revenge
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---

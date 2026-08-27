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
    pick_rate: 0.31
    win_rate: 0.75
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.18
      win_rate: 0.67
    - name: Yogi's Necklace
      pick_rate: 0.1
      win_rate: 1.0
  - name: Breastplate of Valor
    pick_rate: 0.2
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.71
    - name: Jotunn's Revenge
      pick_rate: 0.14
      win_rate: 0.71
  - name: Genji's Guard
    pick_rate: 0.47
    win_rate: 0.67
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.14
      win_rate: 0.86
    - name: Shifter's Shield
      pick_rate: 0.04
      win_rate: 1.0
  - name: Shifter's Shield
    pick_rate: 0.26
    win_rate: 0.67
    alternates:
    - name: Freya's Tears
      pick_rate: 0.19
      win_rate: 0.67
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.75
  - name: Freya's Tears
    pick_rate: 0.24
    win_rate: 0.64
    alternates:
    - name: Draconic Scale
      pick_rate: 0.09
      win_rate: 0.5
    - name: Engraved Guard
      pick_rate: 0.07
      win_rate: 0.67
  - name: Engraved Guard
    pick_rate: 0.21
    win_rate: 1.0
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.11
      win_rate: 1.0
    - name: Medallion
      pick_rate: 0.11
      win_rate: 0.5
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.31
    win_rate: 0.75
  - name: Bumba's Cudgel
    pick_rate: 0.22
    win_rate: 0.73
  - name: Bluestone Brooch
    pick_rate: 0.16
    win_rate: 0.88
  source_url: https://smitebrain.com/gods/odin/
  last_verified: '2026-08-27'
  god_win_rate: 0.6666666666666666
  god_matches_won: 34
  god_matches_played: 51
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-27'
  god_matches_analyzed: 2301
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Yogi's Necklace
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Shell of Rebuke
  - Freya's Tears
  flex_slots:
  - Freya's Tears
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged Hammer,
    Eye of the Storm, Berserker''s Shield, Erosion, Eye of Providence, Shield of the
    Phoenix, Hydra''s Lament, Stone of Binding, Heartseeker, Magi''s Cloak, Avenging
    Blade, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Titan''s Bane,
    The Crusher, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Stampede,
    Daybreak Gavel.'
  slot_scores:
    Yogi's Necklace:
      total: 0.66
      efficiency: 0.52
      win: 1.0
      pick: 0.1
      fit: 0.15
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.67
      pick: 0.73
      fit: 0.29
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.72
      win: 0.75
      pick: 0.31
      fit: 0.46
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.21
    Shell of Rebuke:
      total: 0.62
      efficiency: 0.28
      win: 1.0
      pick: 0.34
      fit: 0.38
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.64
      pick: 0.52
      fit: 0.49
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Yogi's Necklace
  - Genji's Guard
  - Jotunn's Revenge
  - Shell of Rebuke
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Freya's Tears
  - Shifter's Shield
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Amanita
    Charm, Kinetic Cuirass, Shield Splitter, Hydra''s Lament, Runeforged Hammer, Heartseeker,
    Berserker''s Shield, Eye of the Storm, Shield of the Phoenix, Erosion, Stone of
    Binding, Eye of Providence, Avenging Blade, Screeching Gargoyle, Magi''s Cloak,
    Titan''s Bane, The Crusher, Daybreak Gavel, Oni Hunter''s Garb, Transcendence,
    Midgardian Mail, Mantle Of Discord, The Reaper, Arondight.'
  slot_scores:
    Yogi's Necklace:
      total: 0.66
      efficiency: 0.52
      win: 1.0
      pick: 0.1
      fit: 0.17
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.67
      pick: 0.73
      fit: 0.29
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.72
      win: 0.75
      pick: 0.31
      fit: 0.45
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.34
      fit: 0.26
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.64
      pick: 0.52
      fit: 0.35
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.67
      pick: 0.43
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Yogi's Necklace
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Shell of Rebuke
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Yogi''s Necklace, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass,
    Runeforged Hammer, The Reaper, Shield Splitter, Eye of the Storm, Berserker''s
    Shield, Erosion, Eye of Providence, Hydra''s Lament, Phoenix Feather, Avenging
    Blade, Heartseeker, Chandra''s Grace, Glorious Pridwen, Stone of Binding, Midgardian
    Mail, Daybreak Gavel, Titan''s Bane, The Crusher, Hide of the Nemean Lion, Magi''s
    Cloak.'
  slot_scores:
    Yogi's Necklace:
      total: 0.71
      efficiency: 0.52
      win: 1.0
      pick: 0.1
      fit: 0.5
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.67
      pick: 0.73
      fit: 0.27
    Jotunn's Revenge:
      total: 0.68
      efficiency: 0.72
      win: 0.75
      pick: 0.31
      fit: 0.48
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.21
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.34
      fit: 0.32
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.82
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Yogi's Necklace
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Shell of Rebuke
  - Freya's Tears
  flex_slots:
  - Freya's Tears
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Stone of Binding, Kinetic Cuirass, Avenging Blade,
    Screeching Gargoyle, Void Shield, Heartseeker, Shield Splitter, Void Stone, Runeforged
    Hammer, Berserker''s Shield, Titan''s Bane, The Crusher, Eye of the Storm, The
    Reaper, Erosion, Eye of Providence, Hydra''s Lament, Shield of the Phoenix, Magi''s
    Cloak, Pendulum Blade, Avatar''s Parashu, Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Yogi's Necklace:
      total: 0.65
      efficiency: 0.52
      win: 1.0
      pick: 0.1
      fit: 0.12
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.67
      pick: 0.73
      fit: 0.24
    Jotunn's Revenge:
      total: 0.69
      efficiency: 0.72
      win: 0.75
      pick: 0.31
      fit: 0.56
    Transcendence:
      total: 0.51
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.17
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.34
      fit: 0.31
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.64
      pick: 0.52
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Yogi's Necklace
  - Berserker's Shield
  - Jotunn's Revenge
  - Shell of Rebuke
  - Riptalon
  flex_slots:
  - Golden Blade
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Golden Blade, Riptalon,
    Tyrfing, Silverbranch Bow, Shield Splitter, Runeforged Hammer, Pharaoh''s Curse,
    Lernaean Bow, Toxic Blade, Shogun''s Ofuda, Erosion, The Reaper, Stone of Binding,
    Eye of Providence, Hydra''s Lament, Eye of the Storm, Shield of the Phoenix, Tekko-Kagi,
    Magi''s Cloak, Heartseeker, Daybreak Gavel.'
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.52
    Yogi's Necklace:
      total: 0.65
      efficiency: 0.52
      win: 1.0
      pick: 0.1
      fit: 0.1
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.75
      pick: 0.31
      fit: 0.27
    Shell of Rebuke:
      total: 0.6
      efficiency: 0.28
      win: 1.0
      pick: 0.34
      fit: 0.25
    Riptalon:
      total: 0.55
      efficiency: 0.51
      win: 0.67
      pick: 0.0
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Yogi's Necklace
  - Genji's Guard
  - Jotunn's Revenge
  - Shell of Rebuke
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Shell of Rebuke
  - Shifter's Shield
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Kinetic Cuirass, Shield
    of the Phoenix, Hydra''s Lament, Screeching Gargoyle, Berserker''s Shield, Shield
    Splitter, Runeforged Hammer, Prophetic Cloak, Erosion, Eye of Providence, Stone
    of Binding, Gladiator''s Shield, Eye of the Storm, Arondight, Magi''s Cloak, Eye
    of Erebus, Mantle Of Discord, Midgardian Mail, Daybreak Gavel, Heartseeker, Pendulum
    Blade, Glorious Pridwen, Hide of the Nemean Lion.'
  slot_scores:
    Yogi's Necklace:
      total: 0.65
      efficiency: 0.52
      win: 1.0
      pick: 0.1
      fit: 0.12
    Genji's Guard:
      total: 0.63
      efficiency: 0.66
      win: 0.67
      pick: 0.73
      fit: 0.44
    Jotunn's Revenge:
      total: 0.68
      efficiency: 0.72
      win: 0.75
      pick: 0.31
      fit: 0.5
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.34
      fit: 0.29
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.64
      pick: 0.52
      fit: 0.59
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.67
      pick: 0.43
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
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
    Hammer, Eye of the Storm, Berserker''s Shield, Erosion, Eye of Providence, Shield
    of the Phoenix, Hydra''s Lament, Stone of Binding, Heartseeker, Magi''s Cloak,
    Avenging Blade, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Titan''s
    Bane, The Crusher, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Stampede,
    Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.67
      pick: 0.73
      fit: 0.29
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.72
      win: 0.75
      pick: 0.31
      fit: 0.46
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.64
    Shield Splitter:
      total: 0.58
      efficiency: 0.55
      win: 0.67
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.64
      pick: 0.52
      fit: 0.49
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.54
  starter: *id001
---

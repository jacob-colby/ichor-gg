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
    pick_rate: 0.39
    win_rate: 0.6
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.57
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.58
  - name: Breastplate of Valor
    pick_rate: 0.21
    win_rate: 0.56
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.53
    - name: Hydra's Lament
      pick_rate: 0.13
      win_rate: 0.76
  - name: Genji's Guard
    pick_rate: 0.41
    win_rate: 0.55
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.69
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.43
  - name: Freya's Tears
    pick_rate: 0.21
    win_rate: 0.62
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.5
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.75
  - name: Draconic Scale
    pick_rate: 0.08
    win_rate: 0.56
    alternates:
    - name: Freya's Tears
      pick_rate: 0.18
      win_rate: 0.6
    - name: Sage's Ring
      pick_rate: 0.04
      win_rate: 0.75
  - name: Engraved Guard
    pick_rate: 0.1
    win_rate: 1.0
    alternates:
    - name: Glorious Pridwen
      pick_rate: 0.06
      win_rate: 0.5
    - name: Survivor's Sash
      pick_rate: 0.06
      win_rate: 0.5
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.3
    win_rate: 0.66
  - name: Bumba's Cudgel
    pick_rate: 0.23
    win_rate: 0.62
  - name: Bluestone Brooch
    pick_rate: 0.16
    win_rate: 0.65
  source_url: https://smitebrain.com/gods/odin/
  last_verified: '2026-08-30'
  god_win_rate: 0.59375
  god_matches_won: 76
  god_matches_played: 128
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-30'
  god_matches_analyzed: 5563
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged Hammer,
    Eye of the Storm, Berserker''s Shield, Erosion, Eye of Providence, Shield of the
    Phoenix, Stone of Binding, Heartseeker, Magi''s Cloak, Avenging Blade, Mantle
    Of Discord, Midgardian Mail, Screeching Gargoyle, Titan''s Bane, The Crusher,
    Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Stampede, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.55
      pick: 0.64
      fit: 0.29
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.6
      pick: 0.39
      fit: 0.46
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.21
    Hydra's Lament:
      total: 0.6
      efficiency: 0.54
      win: 0.76
      pick: 0.18
      fit: 0.41
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.62
      pick: 0.35
      fit: 0.49
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.54
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Freya's Tears
  flex_slots:
  - Breastplate of Valor
  - Transcendence
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
    Charm, Kinetic Cuirass, Shield Splitter, Runeforged Hammer, Heartseeker, Berserker''s
    Shield, Eye of the Storm, Shield of the Phoenix, Erosion, Stone of Binding, Eye
    of Providence, Avenging Blade, Screeching Gargoyle, Magi''s Cloak, Titan''s Bane,
    The Crusher, Daybreak Gavel, Oni Hunter''s Garb, Transcendence, Midgardian Mail,
    Mantle Of Discord, The Reaper, Arondight.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.55
      pick: 0.64
      fit: 0.29
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.56
      pick: 0.29
      fit: 0.29
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.6
      pick: 0.39
      fit: 0.45
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.25
    Hydra's Lament:
      total: 0.61
      efficiency: 0.54
      win: 0.76
      pick: 0.18
      fit: 0.44
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.62
      pick: 0.35
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Hydra's Lament
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Runeforged Hammer,
    The Reaper, Shield Splitter, Eye of the Storm, Berserker''s Shield, Erosion, Yogi''s
    Necklace, Eye of Providence, Phoenix Feather, Avenging Blade, Heartseeker, Chandra''s
    Grace, Stone of Binding, Midgardian Mail, Daybreak Gavel, Titan''s Bane, The Crusher,
    Hide of the Nemean Lion, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.55
      pick: 0.64
      fit: 0.27
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.6
      pick: 0.39
      fit: 0.48
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.77
    Hydra's Lament:
      total: 0.6
      efficiency: 0.54
      win: 0.76
      pick: 0.18
      fit: 0.42
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.62
      pick: 0.35
      fit: 0.43
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.82
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Stone of Binding, Kinetic Cuirass, Avenging Blade,
    Screeching Gargoyle, Void Shield, Heartseeker, Shield Splitter, Void Stone, Runeforged
    Hammer, Berserker''s Shield, Titan''s Bane, The Crusher, Eye of the Storm, The
    Reaper, Erosion, Eye of Providence, Shield of the Phoenix, Magi''s Cloak, Pendulum
    Blade, Avatar''s Parashu, Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.55
      pick: 0.64
      fit: 0.24
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.6
      pick: 0.39
      fit: 0.56
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.17
    Hydra's Lament:
      total: 0.59
      efficiency: 0.54
      win: 0.76
      pick: 0.18
      fit: 0.35
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.62
      pick: 0.35
      fit: 0.39
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
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
    Eye of Providence, Eye of the Storm, Shield of the Phoenix, Tekko-Kagi, Magi''s
    Cloak, Heartseeker, Daybreak Gavel.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.52
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.6
      pick: 0.39
      fit: 0.27
    Hydra's Lament:
      total: 0.58
      efficiency: 0.54
      win: 0.76
      pick: 0.18
      fit: 0.27
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.62
      pick: 0.35
      fit: 0.32
    Riptalon:
      total: 0.5
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Kinetic Cuirass, Shield
    of the Phoenix, Screeching Gargoyle, Berserker''s Shield, Shield Splitter, Runeforged
    Hammer, Prophetic Cloak, Erosion, Eye of Providence, Stone of Binding, Gladiator''s
    Shield, Eye of the Storm, Arondight, Magi''s Cloak, Eye of Erebus, Mantle Of Discord,
    Midgardian Mail, Daybreak Gavel, Heartseeker, Pendulum Blade, Hide of the Nemean
    Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.55
      pick: 0.64
      fit: 0.44
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.56
      pick: 0.29
      fit: 0.44
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.6
      pick: 0.39
      fit: 0.5
    Hydra's Lament:
      total: 0.61
      efficiency: 0.54
      win: 0.76
      pick: 0.18
      fit: 0.48
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.62
      pick: 0.35
      fit: 0.59
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.56
      pick: 0.0
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
    of the Phoenix, Stone of Binding, Heartseeker, Magi''s Cloak, Avenging Blade,
    Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Titan''s Bane, The Crusher,
    Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Stampede, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.55
      pick: 0.64
      fit: 0.29
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.6
      pick: 0.39
      fit: 0.46
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.64
    Shield Splitter:
      total: 0.53
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.62
      pick: 0.35
      fit: 0.49
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.54
  starter: *id001
---

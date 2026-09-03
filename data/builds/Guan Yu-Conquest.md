---
type: smite-build
god: Guan Yu
mode: Conquest
builds:
- source: community
  aspect: Aspect of the General
  aspect_pick_rate: 0.83
  aspect_win_rate: 0.57
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.39
    win_rate: 0.6
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.11
      win_rate: 0.63
    - name: Heartwood Charm
      pick_rate: 0.09
      win_rate: 0.59
  - name: Chronos' Pendant
    pick_rate: 0.28
    win_rate: 0.66
    alternates:
    - name: Genji's Guard
      pick_rate: 0.19
      win_rate: 0.52
    - name: Breastplate of Valor
      pick_rate: 0.16
      win_rate: 0.54
  - name: Breastplate of Valor
    pick_rate: 0.27
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.24
      win_rate: 0.62
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.58
  - name: Genji's Guard
    pick_rate: 0.22
    win_rate: 0.6
    alternates:
    - name: Freya's Tears
      pick_rate: 0.14
      win_rate: 0.51
    - name: Breastplate of Valor
      pick_rate: 0.12
      win_rate: 0.58
  - name: Freya's Tears
    pick_rate: 0.19
    win_rate: 0.67
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.69
    - name: Heartwood Charm
      pick_rate: 0.06
      win_rate: 0.6
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.8
    alternates:
    - name: Sage's Ring
      pick_rate: 0.06
      win_rate: 0.68
    - name: Adroit Ring
      pick_rate: 0.06
      win_rate: 0.67
  community_starters:
  - name: Sands Of Time
    pick_rate: 0.34
    win_rate: 0.51
  - name: Pendulum of the Ages
    pick_rate: 0.2
    win_rate: 0.67
  - name: Hunter's Cowl
    pick_rate: 0.12
    win_rate: 0.64
  source_url: https://smitebrain.com/gods/guan-yu/
  last_verified: '2026-09-03'
  god_win_rate: 0.5625823451910409
  god_matches_won: 427
  god_matches_played: 759
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-09-03'
  god_matches_analyzed: 10626
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Berserker''s Shield, Kinetic Cuirass,
    Shield Splitter, Golden Blade, Runeforged Hammer, Eye of the Storm, Hydra''s Lament,
    Shield of the Phoenix, Erosion, Eye of Providence, Draconic Scale, Tyrfing, Stone
    of Binding, Pharaoh''s Curse, Avenging Blade, Lernaean Bow, Screeching Gargoyle,
    Magi''s Cloak, Shogun''s Ofuda, Midgardian Mail, Mantle Of Discord, Heartseeker,
    Hide of the Nemean Lion, Daybreak Gavel.'
  slot_scores:
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.66
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.66
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.66
      pick: 0.0
      fit: 0.6
    Shield Splitter:
      total: 0.57
      efficiency: 0.55
      win: 0.66
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.41
      fit: 0.49
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.5
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Berserker''s Shield, Shield of the
    Phoenix, Kinetic Cuirass, Golden Blade, Runeforged Hammer, Shield Splitter, Eye
    of the Storm, Hydra''s Lament, The Reaper, Yogi''s Necklace, Erosion, Chandra''s
    Grace, Eye of Providence, Draconic Scale, Phoenix Feather, Avenging Blade, Tyrfing,
    Glorious Pridwen, Pharaoh''s Curse, Riptalon, Lernaean Bow, Shogun''s Ofuda, Stone
    of Binding, Screeching Gargoyle.'
  slot_scores:
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.66
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.66
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.66
      pick: 0.0
      fit: 0.6
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.53
      win: 0.66
      pick: 0.0
      fit: 0.79
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.67
      pick: 0.41
      fit: 0.45
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Screeching Gargoyle
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
    for this god: Jotunn''s Revenge, Berserker''s Shield, Amanita Charm, Stone of
    Binding, Screeching Gargoyle, Avenging Blade, Kinetic Cuirass, Void Shield, Heartseeker,
    Void Stone, Shield Splitter, Runeforged Hammer, Silverbranch Bow, Tekko-Kagi,
    Titan''s Bane, The Crusher, Golden Blade, Toxic Blade, Hydra''s Lament, Eye of
    the Storm, The Reaper, Shield of the Phoenix, Erosion, Eye of Providence, Draconic
    Scale, Tyrfing.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.57
      efficiency: 0.51
      win: 0.66
      pick: 0.0
      fit: 0.64
    Stone of Binding:
      total: 0.57
      efficiency: 0.51
      win: 0.66
      pick: 0.0
      fit: 0.66
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.66
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.66
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.41
      fit: 0.37
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Tyrfing
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass,
    Golden Blade, Tyrfing, Runeforged Hammer, Shield Splitter, Pharaoh''s Curse, Riptalon,
    Lernaean Bow, Silverbranch Bow, Shogun''s Ofuda, Hydra''s Lament, Shield of the
    Phoenix, Toxic Blade, Erosion, Eye of the Storm, Eye of Providence, Stone of Binding,
    Draconic Scale, Screeching Gargoyle, Daybreak Gavel, Magi''s Cloak, The Reaper,
    Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.52
      win: 0.66
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.66
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.66
      pick: 0.0
      fit: 0.24
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.66
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.41
      fit: 0.34
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Berserker''s Shield, Kinetic Cuirass, Shield of the Phoenix, Hydra''s Lament,
    Screeching Gargoyle, Shield Splitter, Runeforged Hammer, Prophetic Cloak, Erosion,
    Golden Blade, Gladiator''s Shield, Eye of Providence, Arondight, Draconic Scale,
    Stone of Binding, Eye of the Storm, Pharaoh''s Curse, Eye of Erebus, Magi''s Cloak,
    Daybreak Gavel, Midgardian Mail, Shogun''s Ofuda, Mantle Of Discord, Chandra''s
    Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.6
      pick: 0.37
      fit: 0.44
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.66
      pick: 0.0
      fit: 0.34
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.57
      pick: 0.42
      fit: 0.44
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.66
      pick: 0.0
      fit: 0.43
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.67
      pick: 0.41
      fit: 0.58
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    Underrated for this god: Jotunn''s Revenge, Amanita Charm, Berserker''s Shield,
    Kinetic Cuirass, Shield Splitter, Golden Blade, Runeforged Hammer, Eye of the
    Storm, Hydra''s Lament, Shield of the Phoenix, Erosion, Eye of Providence, Draconic
    Scale, Tyrfing, Stone of Binding, Pharaoh''s Curse, Avenging Blade, Lernaean Bow,
    Screeching Gargoyle, Magi''s Cloak, Shogun''s Ofuda, Midgardian Mail, Mantle Of
    Discord, Heartseeker, Hide of the Nemean Lion, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.6
      pick: 0.37
      fit: 0.32
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.66
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.66
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.66
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.41
      fit: 0.49
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shell of Rebuke
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Berserker''s Shield, Kinetic Cuirass, Shield Splitter, Golden Blade, Runeforged
    Hammer, Eye of the Storm, Hydra''s Lament, Shield of the Phoenix, Erosion, Eye
    of Providence, Draconic Scale, Tyrfing, Stone of Binding, Pharaoh''s Curse, Avenging
    Blade, Lernaean Bow, Screeching Gargoyle, Magi''s Cloak, Shogun''s Ofuda, Midgardian
    Mail, Mantle Of Discord, Heartseeker, Hide of the Nemean Lion, Daybreak Gavel.'
  slot_scores:
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.66
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.66
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.66
      pick: 0.0
      fit: 0.6
    Shell of Rebuke:
      total: 0.52
      efficiency: 0.28
      win: 0.8
      pick: 0.25
      fit: 0.35
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.41
      fit: 0.49
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.5
  swaps:
  - added: Shell of Rebuke
    removed: Genji's Guard
    reason: community 80% win over 61 matches (vs 56% on this god), taking the model's
      weakest slot from Genji's Guard
  starter: *id001
---

---
type: smite-build
god: Guan Yu
mode: Conquest
builds:
- source: community
  aspect: Aspect of the General
  aspect_pick_rate: 0.77
  aspect_win_rate: 0.63
  slot_order:
  - name: Chandra's Grace
    pick_rate: 0.37
    win_rate: 0.54
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.5
    - name: Prophetic Cloak
      pick_rate: 0.09
      win_rate: 0.67
  - name: Genji's Guard
    pick_rate: 0.2
    win_rate: 0.71
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.17
      win_rate: 0.83
    - name: Regrowth Striders
      pick_rate: 0.06
      win_rate: 1.0
  - name: Breastplate of Valor
    pick_rate: 0.16
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.6
    - name: Heartwood Charm
      pick_rate: 0.16
      win_rate: 0.8
  - name: Freya's Tears
    pick_rate: 0.28
    win_rate: 0.67
    alternates:
    - name: Stampede
      pick_rate: 0.06
      win_rate: 1.0
    - name: Heartwood Charm
      pick_rate: 0.06
      win_rate: 0.0
  - name: Spirit Robe
    pick_rate: 0.12
    win_rate: 0.67
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.5
    - name: Engraved Guard
      pick_rate: 0.08
      win_rate: 0.5
  - name: Olmec Blue
    pick_rate: 0.15
    win_rate: 0.5
    alternates:
    - name: Mana Tome
      pick_rate: 0.08
      win_rate: 1.0
    - name: Glorious Pridwen
      pick_rate: 0.08
      win_rate: 0.0
  community_starters:
  - name: Sands Of Time
    pick_rate: 0.43
    win_rate: 0.53
  - name: Heroism
    pick_rate: 0.09
    win_rate: 0.67
  - name: Pendulum of the Ages
    pick_rate: 0.09
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/guan-yu/
  last_verified: '2026-09-23'
  god_win_rate: 0.5714285714285714
  god_matches_won: 20
  god_matches_played: 35
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-23'
  god_matches_analyzed: 962
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Regrowth Striders
  - Freya's Tears
  - Stampede
  flex_slots:
  - Genji's Guard
  - Berserker's Shield
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Berserker''s Shield, Kinetic Cuirass,
    Shield Splitter, Shifter''s Shield, Golden Blade, Runeforged Hammer, Eye of the
    Storm, Hydra''s Lament, Shield of the Phoenix, Erosion, Eye of Providence, Draconic
    Scale, Tyrfing, Stone of Binding, Pharaoh''s Curse, Avenging Blade, Lernaean Bow,
    Screeching Gargoyle, Magi''s Cloak, Shogun''s Ofuda, Midgardian Mail, Mantle Of
    Discord, Heartseeker, Hide of the Nemean Lion, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.71
      pick: 0.27
      fit: 0.32
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.4
    Regrowth Striders:
      total: 0.62
      efficiency: 0.35
      win: 1.0
      pick: 0.08
      fit: 0.32
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.47
      fit: 0.49
    Stampede:
      total: 0.68
      efficiency: 0.51
      win: 1.0
      pick: 0.1
      fit: 0.33
  community_ordered:
  - Genji's Guard
  - Regrowth Striders
  - Freya's Tears
  - Stampede
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Regrowth Striders
  - Freya's Tears
  - Amanita Charm
  - Stampede
  flex_slots:
  - Freya's Tears
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Amanita Charm, Jotunn''s Revenge, Berserker''s Shield, Shield of the
    Phoenix, Kinetic Cuirass, Golden Blade, Runeforged Hammer, Shield Splitter, Shifter''s
    Shield, Eye of the Storm, Hydra''s Lament, The Reaper, Yogi''s Necklace, Erosion,
    Eye of Providence, Draconic Scale, Phoenix Feather, Avenging Blade, Tyrfing, Pharaoh''s
    Curse, Riptalon, Lernaean Bow, Shogun''s Ofuda, Stone of Binding, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.71
      pick: 0.27
      fit: 0.3
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.4
    Regrowth Striders:
      total: 0.67
      efficiency: 0.35
      win: 1.0
      pick: 0.08
      fit: 0.6
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.47
      fit: 0.45
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.8
    Stampede:
      total: 0.69
      efficiency: 0.51
      win: 1.0
      pick: 0.1
      fit: 0.35
  community_ordered:
  - Genji's Guard
  - Regrowth Striders
  - Freya's Tears
  - Stampede
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Regrowth Striders
  - Freya's Tears
  - Stampede
  flex_slots:
  - Freya's Tears
  - Berserker's Shield
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
    for this god: Jotunn''s Revenge, Berserker''s Shield, Amanita Charm, Stone of
    Binding, Screeching Gargoyle, Avenging Blade, Kinetic Cuirass, Void Shield, Heartseeker,
    Void Stone, Shield Splitter, Runeforged Hammer, Silverbranch Bow, Shifter''s Shield,
    Tekko-Kagi, Titan''s Bane, The Crusher, Golden Blade, Toxic Blade, Hydra''s Lament,
    Eye of the Storm, The Reaper, Shield of the Phoenix, Erosion, Eye of Providence,
    Draconic Scale, Tyrfing.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.71
      pick: 0.27
      fit: 0.24
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.55
    Regrowth Striders:
      total: 0.61
      efficiency: 0.35
      win: 1.0
      pick: 0.08
      fit: 0.24
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.47
      fit: 0.37
    Stampede:
      total: 0.67
      efficiency: 0.51
      win: 1.0
      pick: 0.1
      fit: 0.25
  community_ordered:
  - Genji's Guard
  - Regrowth Striders
  - Freya's Tears
  - Stampede
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Tyrfing
  - Regrowth Striders
  - Stampede
  flex_slots:
  - Golden Blade
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass,
    Golden Blade, Tyrfing, Shifter''s Shield, Runeforged Hammer, Shield Splitter,
    Pharaoh''s Curse, Riptalon, Lernaean Bow, Silverbranch Bow, Shogun''s Ofuda, Hydra''s
    Lament, Shield of the Phoenix, Toxic Blade, Erosion, Eye of the Storm, Eye of
    Providence, Stone of Binding, Draconic Scale, Screeching Gargoyle, Daybreak Gavel,
    Magi''s Cloak, The Reaper, Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.56
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.71
      pick: 0.27
      fit: 0.22
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.43
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.67
      pick: 0.0
      fit: 0.55
    Regrowth Striders:
      total: 0.61
      efficiency: 0.35
      win: 1.0
      pick: 0.08
      fit: 0.22
    Stampede:
      total: 0.67
      efficiency: 0.51
      win: 1.0
      pick: 0.1
      fit: 0.23
  community_ordered:
  - Genji's Guard
  - Regrowth Striders
  - Stampede
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Regrowth Striders
  - Freya's Tears
  - Stampede
  flex_slots:
  - Jotunn's Revenge
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Berserker''s Shield, Kinetic Cuirass, Shield of the Phoenix, Hydra''s Lament,
    Screeching Gargoyle, Shifter''s Shield, Shield Splitter, Prophetic Cloak, Runeforged
    Hammer, Erosion, Golden Blade, Gladiator''s Shield, Eye of Providence, Arondight,
    Draconic Scale, Stone of Binding, Eye of the Storm, Pharaoh''s Curse, Eye of Erebus,
    Magi''s Cloak, Daybreak Gavel, Midgardian Mail, Shogun''s Ofuda, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.63
      efficiency: 0.66
      win: 0.71
      pick: 0.27
      fit: 0.44
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.43
    Regrowth Striders:
      total: 0.64
      efficiency: 0.35
      win: 1.0
      pick: 0.08
      fit: 0.44
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.67
      pick: 0.47
      fit: 0.58
    Stampede:
      total: 0.67
      efficiency: 0.51
      win: 1.0
      pick: 0.1
      fit: 0.26
  community_ordered:
  - Genji's Guard
  - Regrowth Striders
  - Freya's Tears
  - Stampede
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
    Kinetic Cuirass, Shield Splitter, Shifter''s Shield, Golden Blade, Runeforged
    Hammer, Eye of the Storm, Hydra''s Lament, Shield of the Phoenix, Erosion, Eye
    of Providence, Draconic Scale, Tyrfing, Stone of Binding, Pharaoh''s Curse, Avenging
    Blade, Lernaean Bow, Screeching Gargoyle, Magi''s Cloak, Shogun''s Ofuda, Midgardian
    Mail, Mantle Of Discord, Heartseeker, Hide of the Nemean Lion, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.71
      pick: 0.27
      fit: 0.32
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.47
      fit: 0.49
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---

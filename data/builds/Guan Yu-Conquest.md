---
type: smite-build
god: Guan Yu
mode: Conquest
builds:
- source: community
  aspect: Aspect of the General
  aspect_pick_rate: 0.66
  aspect_win_rate: 0.57
  slot_order:
  - name: Chandra's Grace
    pick_rate: 0.28
    win_rate: 0.48
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.18
      win_rate: 0.7
    - name: Chronos' Pendant
      pick_rate: 0.06
      win_rate: 0.71
  - name: Breastplate of Valor
    pick_rate: 0.22
    win_rate: 0.75
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.67
    - name: Brawler’s Beat Stick
      pick_rate: 0.08
      win_rate: 0.67
  - name: Genji's Guard
    pick_rate: 0.22
    win_rate: 0.59
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.17
      win_rate: 0.65
    - name: Heartwood Charm
      pick_rate: 0.09
      win_rate: 0.67
  - name: Freya's Tears
    pick_rate: 0.16
    win_rate: 0.75
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.67
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.71
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.88
    - name: Spirit Robe
      pick_rate: 0.06
      win_rate: 0.6
  - name: Draconic Scale
    pick_rate: 0.06
    win_rate: 0.67
    alternates:
    - name: Stalwart Sigil
      pick_rate: 0.04
      win_rate: 1.0
    - name: Shield
      pick_rate: 0.04
      win_rate: 0.5
  community_starters:
  - name: Sands Of Time
    pick_rate: 0.3
    win_rate: 0.48
  - name: Pendulum of the Ages
    pick_rate: 0.12
    win_rate: 0.62
  - name: Hunter's Cowl
    pick_rate: 0.11
    win_rate: 0.75
  source_url: https://smitebrain.com/gods/guan-yu/
  last_verified: '2026-09-26'
  god_win_rate: 0.5596330275229358
  god_matches_won: 61
  god_matches_played: 109
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-26'
  god_matches_analyzed: 4198
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Shifter's Shield
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Berserker''s Shield, Kinetic Cuirass,
    Shield Splitter, Golden Blade, Runeforged Hammer, Eye of the Storm, Hydra''s Lament,
    Shield of the Phoenix, Erosion, Eye of Providence, Tyrfing, Stone of Binding,
    Pharaoh''s Curse, Avenging Blade, Lernaean Bow, Screeching Gargoyle, Magi''s Cloak,
    Shogun''s Ofuda, Midgardian Mail, Mantle Of Discord, Heartseeker, Hide of the
    Nemean Lion, Daybreak Gavel.'
  slot_scores:
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.65
      win: 0.75
      pick: 0.3
      fit: 0.32
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.4
    Freya's Tears:
      total: 0.64
      efficiency: 0.61
      win: 0.75
      pick: 0.27
      fit: 0.49
    Shifter's Shield:
      total: 0.59
      efficiency: 0.55
      win: 0.7
      pick: 0.18
      fit: 0.5
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  - Shifter's Shield
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Berserker''s Shield, Shield of the
    Phoenix, Kinetic Cuirass, Golden Blade, Runeforged Hammer, Shield Splitter, Eye
    of the Storm, Hydra''s Lament, The Reaper, Yogi''s Necklace, Erosion, Eye of Providence,
    Phoenix Feather, Avenging Blade, Tyrfing, Glorious Pridwen, Pharaoh''s Curse,
    Riptalon, Lernaean Bow, Shogun''s Ofuda, Stone of Binding, Screeching Gargoyle.'
  slot_scores:
    Berserker's Shield:
      total: 0.61
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.65
      win: 0.75
      pick: 0.3
      fit: 0.3
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.4
    Shield of the Phoenix:
      total: 0.61
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.79
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.75
      pick: 0.27
      fit: 0.45
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Berserker''s Shield, Amanita Charm, Stone of
    Binding, Screeching Gargoyle, Avenging Blade, Kinetic Cuirass, Void Shield, Heartseeker,
    Void Stone, Shield Splitter, Runeforged Hammer, Silverbranch Bow, Tekko-Kagi,
    Titan''s Bane, The Crusher, Golden Blade, Toxic Blade, Hydra''s Lament, Eye of
    the Storm, The Reaper, Shield of the Phoenix, Erosion, Eye of Providence, Tyrfing.'
  slot_scores:
    Stone of Binding:
      total: 0.58
      efficiency: 0.51
      win: 0.67
      pick: 0.0
      fit: 0.66
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.32
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.65
      win: 0.75
      pick: 0.3
      fit: 0.24
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.75
      pick: 0.27
      fit: 0.37
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Tyrfing
  - Freya's Tears
  flex_slots:
  - Golden Blade
  - Tyrfing
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass,
    Golden Blade, Tyrfing, Runeforged Hammer, Shield Splitter, Pharaoh''s Curse, Riptalon,
    Lernaean Bow, Silverbranch Bow, Shogun''s Ofuda, Hydra''s Lament, Shield of the
    Phoenix, Toxic Blade, Erosion, Eye of the Storm, Eye of Providence, Stone of Binding,
    Screeching Gargoyle, Daybreak Gavel, Magi''s Cloak, The Reaper, Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.65
      win: 0.75
      pick: 0.3
      fit: 0.22
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.24
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.67
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.75
      pick: 0.27
      fit: 0.34
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Berserker''s Shield, Kinetic Cuirass, Shield of the Phoenix, Hydra''s Lament,
    Screeching Gargoyle, Shield Splitter, Runeforged Hammer, Prophetic Cloak, Erosion,
    Golden Blade, Gladiator''s Shield, Eye of Providence, Arondight, Stone of Binding,
    Eye of the Storm, Pharaoh''s Curse, Eye of Erebus, Magi''s Cloak, Daybreak Gavel,
    Midgardian Mail, Shogun''s Ofuda, Mantle Of Discord.'
  slot_scores:
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.34
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.59
      pick: 0.34
      fit: 0.44
    Breastplate of Valor:
      total: 0.65
      efficiency: 0.65
      win: 0.75
      pick: 0.3
      fit: 0.44
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.43
    Freya's Tears:
      total: 0.65
      efficiency: 0.61
      win: 0.75
      pick: 0.27
      fit: 0.58
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Genji's Guard
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
    Storm, Hydra''s Lament, Shield of the Phoenix, Erosion, Eye of Providence, Tyrfing,
    Stone of Binding, Pharaoh''s Curse, Avenging Blade, Lernaean Bow, Screeching Gargoyle,
    Magi''s Cloak, Shogun''s Ofuda, Midgardian Mail, Mantle Of Discord, Heartseeker,
    Hide of the Nemean Lion, Daybreak Gavel.'
  slot_scores:
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.43
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.59
      pick: 0.34
      fit: 0.32
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
      total: 0.64
      efficiency: 0.61
      win: 0.75
      pick: 0.27
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

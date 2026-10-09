---
type: smite-build
god: Guan Yu
mode: Conquest
builds:
- source: community
  aspect: Aspect of the General
  aspect_pick_rate: 0.33
  aspect_win_rate: 0.54
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.3
    win_rate: 0.58
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.25
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.5
  - name: Sanguine Lash
    pick_rate: 0.2
    win_rate: 0.5
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.13
      win_rate: 1.0
    - name: Berserker's Shield
      pick_rate: 0.08
      win_rate: 0.0
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.5
    - name: Umbral Link
      pick_rate: 0.08
      win_rate: 0.67
  - name: Freya's Tears
    pick_rate: 0.18
    win_rate: 0.29
    alternates:
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.33
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.67
  - name: Shifter's Shield
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Spectral Armor
      pick_rate: 0.07
      win_rate: 0.5
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 1.0
  - name: Hussar's Wings
    pick_rate: 0.08
    win_rate: 1.0
    alternates:
    - name: Captain's Ring
      pick_rate: 0.04
      win_rate: 0.0
    - name: Mana Tome
      pick_rate: 0.04
      win_rate: 1.0
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.28
    win_rate: 0.55
  - name: Bluestone Brooch
    pick_rate: 0.13
    win_rate: 0.8
  - name: Selflessness
    pick_rate: 0.1
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/guan-yu/
  last_verified: '2026-10-09'
  god_win_rate: 0.45
  god_matches_won: 18
  god_matches_played: 40
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-09'
  god_matches_analyzed: 2961
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Hussar's Wings
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
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Shield Splitter,
    Golden Blade, Runeforged Hammer, Eye of the Storm, Hydra''s Lament, Shield of
    the Phoenix, Erosion, Eye of Providence, Draconic Scale, Tyrfing, Stone of Binding,
    Pharaoh''s Curse, Avenging Blade, Lernaean Bow, Screeching Gargoyle, Magi''s Cloak,
    Shogun''s Ofuda, Midgardian Mail, Mantle Of Discord, Heartseeker, Hide of the
    Nemean Lion, Daybreak Gavel, Berserker''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.23
      fit: 0.32
    Breastplate of Valor:
      total: 0.74
      efficiency: 0.65
      win: 1.0
      pick: 0.18
      fit: 0.32
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.4
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.21
    Hussar's Wings:
      total: 0.67
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.5
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Hussar's Wings
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix, Kinetic Cuirass,
    Golden Blade, Runeforged Hammer, Shield Splitter, Eye of the Storm, Hydra''s Lament,
    The Reaper, Yogi''s Necklace, Erosion, Chandra''s Grace, Eye of Providence, Draconic
    Scale, Phoenix Feather, Avenging Blade, Tyrfing, Glorious Pridwen, Pharaoh''s
    Curse, Riptalon, Lernaean Bow, Shogun''s Ofuda, Stone of Binding, Screeching Gargoyle,
    Berserker''s Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.73
      efficiency: 0.65
      win: 1.0
      pick: 0.18
      fit: 0.3
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.6
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.79
    Hussar's Wings:
      total: 0.67
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.5
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Breastplate of Valor
  - Hussar's Wings
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Stone of Binding, Screeching Gargoyle,
    Avenging Blade, Kinetic Cuirass, Void Shield, Heartseeker, Void Stone, Shield
    Splitter, Runeforged Hammer, Silverbranch Bow, Tekko-Kagi, Titan''s Bane, The
    Crusher, Golden Blade, Toxic Blade, Hydra''s Lament, Eye of the Storm, The Reaper,
    Shield of the Phoenix, Erosion, Eye of Providence, Draconic Scale, Tyrfing, Berserker''s
    Shield.'
  slot_scores:
    Stone of Binding:
      total: 0.5
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.66
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.23
      fit: 0.24
    Breastplate of Valor:
      total: 0.72
      efficiency: 0.65
      win: 1.0
      pick: 0.18
      fit: 0.24
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.55
    Hussar's Wings:
      total: 0.66
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.38
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Hussar's Wings
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Breastplate of Valor
  - Jotunn's Revenge
  - Tyrfing
  - Hussar's Wings
  - Pharaoh's Curse
  flex_slots:
  - Tyrfing
  - Pharaoh's Curse
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
    this god: Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Golden Blade, Tyrfing,
    Runeforged Hammer, Shield Splitter, Pharaoh''s Curse, Riptalon, Lernaean Bow,
    Silverbranch Bow, Shogun''s Ofuda, Hydra''s Lament, Shield of the Phoenix, Toxic
    Blade, Erosion, Eye of the Storm, Eye of Providence, Stone of Binding, Draconic
    Scale, Screeching Gargoyle, Daybreak Gavel, Magi''s Cloak, The Reaper, Tekko-Kagi,
    Berserker''s Shield.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.56
    Breastplate of Valor:
      total: 0.72
      efficiency: 0.65
      win: 1.0
      pick: 0.18
      fit: 0.22
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.24
    Tyrfing:
      total: 0.48
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.55
    Hussar's Wings:
      total: 0.65
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.35
    Pharaoh's Curse:
      total: 0.47
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Breastplate of Valor
  - Hussar's Wings
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Kinetic Cuirass, Shield of the Phoenix, Hydra''s Lament, Screeching Gargoyle,
    Shield Splitter, Runeforged Hammer, Prophetic Cloak, Erosion, Golden Blade, Gladiator''s
    Shield, Eye of Providence, Arondight, Draconic Scale, Stone of Binding, Eye of
    the Storm, Pharaoh''s Curse, Eye of Erebus, Magi''s Cloak, Daybreak Gavel, Midgardian
    Mail, Shogun''s Ofuda, Mantle Of Discord, Chandra''s Grace, Berserker''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.23
      fit: 0.44
    Breastplate of Valor:
      total: 0.75
      efficiency: 0.65
      win: 1.0
      pick: 0.18
      fit: 0.44
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.5
    Hussar's Wings:
      total: 0.66
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.4
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Hussar's Wings
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
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.23
      fit: 0.32
    Berserker's Shield:
      total: 0.31
      efficiency: 0.68
      win: 0.0
      pick: 0.11
      fit: 0.43
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.43
      efficiency: 0.61
      win: 0.29
      pick: 0.3
      fit: 0.49
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Freya's Tears
  starter: *id001
---

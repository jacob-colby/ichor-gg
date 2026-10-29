---
type: smite-build
god: Guan Yu
mode: Conquest
builds:
- source: community
  aspect: Aspect of the General
  aspect_pick_rate: 0.5
  aspect_win_rate: 0.52
  slot_order:
  - name: Stampede
    pick_rate: 0.14
    win_rate: 0.53
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.11
      win_rate: 0.46
    - name: Devourer's Gauntlet
      pick_rate: 0.11
      win_rate: 0.62
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.11
      win_rate: 0.54
    - name: Chandra's Grace
      pick_rate: 0.07
      win_rate: 0.78
  - name: Freya's Tears
    pick_rate: 0.2
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.33
    - name: Berserker's Shield
      pick_rate: 0.09
      win_rate: 0.73
  - name: Rod of Asclepius
    pick_rate: 0.05
    win_rate: 0.83
    alternates:
    - name: Freya's Tears
      pick_rate: 0.15
      win_rate: 0.59
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.69
  - name: Draconic Scale
    pick_rate: 0.06
    win_rate: 0.67
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 1.0
    - name: Contagion
      pick_rate: 0.05
      win_rate: 0.8
  - name: Sage's Ring
    pick_rate: 0.08
    win_rate: 0.8
    alternates:
    - name: Captain's Ring
      pick_rate: 0.05
      win_rate: 1.0
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.33
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.15
    win_rate: 0.67
  - name: Bluestone Pendant
    pick_rate: 0.15
    win_rate: 0.5
  - name: Sands Of Time
    pick_rate: 0.13
    win_rate: 0.56
  source_url: https://smitebrain.com/gods/guan-yu/
  last_verified: '2026-10-29'
  god_win_rate: 0.5537190082644629
  god_matches_won: 67
  god_matches_played: 121
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-29'
  god_matches_analyzed: 9506
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Draconic Scale, Breastplate
    of Valor, Shield Splitter, Shifter''s Shield, Golden Blade, Runeforged Hammer,
    Eye of the Storm, Hydra''s Lament, Shield of the Phoenix, Erosion, Eye of Providence,
    Tyrfing, Stone of Binding, Pharaoh''s Curse, Avenging Blade, Lernaean Bow, Screeching
    Gargoyle, Magi''s Cloak, Shogun''s Ofuda, Midgardian Mail, Mantle Of Discord,
    Heartseeker, Hide of the Nemean Lion, Daybreak Gavel.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.6
    Shield Splitter:
      total: 0.55
      efficiency: 0.55
      win: 0.62
      pick: 0.0
      fit: 0.56
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.67
      pick: 0.13
      fit: 0.5
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Draconic Scale
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Chandra's Grace
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Draconic Scale
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Chandra''s Grace, Jotunn''s Revenge, Shield of the Phoenix,
    Kinetic Cuirass, Draconic Scale, Golden Blade, Breastplate of Valor, Runeforged
    Hammer, Shield Splitter, Shifter''s Shield, Eye of the Storm, Hydra''s Lament,
    The Reaper, Yogi''s Necklace, Erosion, Eye of Providence, Phoenix Feather, Avenging
    Blade, Tyrfing, Glorious Pridwen, Pharaoh''s Curse, Riptalon, Lernaean Bow, Shogun''s
    Ofuda, Stone of Binding, Screeching Gargoyle.'
  slot_scores:
    Chandra's Grace:
      total: 0.61
      efficiency: 0.45
      win: 0.78
      pick: 0.1
      fit: 0.64
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.54
      pick: 0.15
      fit: 0.45
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.6
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.67
      pick: 0.13
      fit: 0.5
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Chandra's Grace
  - Berserker's Shield
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Avenging Blade
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Avenging Blade
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Stone of Binding, Screeching Gargoyle,
    Avenging Blade, Kinetic Cuirass, Breastplate of Valor, Void Shield, Draconic Scale,
    Heartseeker, Void Stone, Shield Splitter, Runeforged Hammer, Silverbranch Bow,
    Shifter''s Shield, Tekko-Kagi, Titan''s Bane, The Crusher, Golden Blade, Toxic
    Blade, Hydra''s Lament, Eye of the Storm, The Reaper, Shield of the Phoenix, Erosion,
    Eye of Providence, Tyrfing.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.55
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.64
    Stone of Binding:
      total: 0.56
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.66
    Avenging Blade:
      total: 0.55
      efficiency: 0.49
      win: 0.62
      pick: 0.0
      fit: 0.67
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.55
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.48
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Chandra's Grace
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Golden Blade, Breastplate
    of Valor, Draconic Scale, Tyrfing, Shifter''s Shield, Runeforged Hammer, Shield
    Splitter, Pharaoh''s Curse, Riptalon, Lernaean Bow, Silverbranch Bow, Shogun''s
    Ofuda, Hydra''s Lament, Shield of the Phoenix, Toxic Blade, Erosion, Eye of the
    Storm, Eye of Providence, Stone of Binding, Screeching Gargoyle, Daybreak Gavel,
    Magi''s Cloak, The Reaper, Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.56
    Chandra's Grace:
      total: 0.55
      efficiency: 0.45
      win: 0.78
      pick: 0.1
      fit: 0.21
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.54
      pick: 0.15
      fit: 0.43
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.24
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.62
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Chandra's Grace
  - Berserker's Shield
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chandra's Grace
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - Draconic Scale
  flex_slots:
  - Hydra's Lament
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Chandra''s Grace,
    Breastplate of Valor, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Hydra''s
    Lament, Draconic Scale, Screeching Gargoyle, Shifter''s Shield, Shield Splitter,
    Runeforged Hammer, Prophetic Cloak, Erosion, Golden Blade, Gladiator''s Shield,
    Eye of Providence, Arondight, Stone of Binding, Eye of the Storm, Pharaoh''s Curse,
    Eye of Erebus, Magi''s Cloak, Daybreak Gavel, Midgardian Mail, Shogun''s Ofuda,
    Mantle Of Discord.'
  slot_scores:
    Chandra's Grace:
      total: 0.58
      efficiency: 0.45
      win: 0.78
      pick: 0.1
      fit: 0.43
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.5
    Hydra's Lament:
      total: 0.54
      efficiency: 0.54
      win: 0.62
      pick: 0.0
      fit: 0.5
    Draconic Scale:
      total: 0.54
      efficiency: 0.5
      win: 0.67
      pick: 0.13
      fit: 0.4
  community_ordered:
  - Chandra's Grace
  - Draconic Scale
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
    Underrated for this god: Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Breastplate
    of Valor, Shield Splitter, Shifter''s Shield, Golden Blade, Runeforged Hammer,
    Eye of the Storm, Hydra''s Lament, Shield of the Phoenix, Erosion, Eye of Providence,
    Draconic Scale, Tyrfing, Stone of Binding, Pharaoh''s Curse, Avenging Blade, Lernaean
    Bow, Screeching Gargoyle, Magi''s Cloak, Shogun''s Ofuda, Midgardian Mail, Mantle
    Of Discord, Heartseeker, Hide of the Nemean Lion, Daybreak Gavel.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.54
      pick: 0.15
      fit: 0.43
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.18
      fit: 0.32
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.31
      fit: 0.49
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Berserker's Shield
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---

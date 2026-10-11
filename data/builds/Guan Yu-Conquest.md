---
type: smite-build
god: Guan Yu
mode: Conquest
builds:
- source: community
  aspect: Aspect of the General
  aspect_pick_rate: 0.32
  aspect_win_rate: 0.48
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.32
    win_rate: 0.61
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.25
    - name: Chandra's Grace
      pick_rate: 0.08
      win_rate: 0.67
  - name: Sanguine Lash
    pick_rate: 0.26
    win_rate: 0.63
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.83
    - name: Prophetic Cloak
      pick_rate: 0.07
      win_rate: 0.2
  - name: Freya's Tears
    pick_rate: 0.14
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.43
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.17
  - name: Brawler’s Beat Stick
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.2
      win_rate: 0.43
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.2
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.6
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.75
    - name: Berserker's Shield
      pick_rate: 0.07
      win_rate: 1.0
  - name: Medal of Defense
    pick_rate: 0.11
    win_rate: 0.2
    alternates:
    - name: Hussar's Wings
      pick_rate: 0.07
      win_rate: 0.67
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.5
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.26
    win_rate: 0.63
  - name: Bluestone Brooch
    pick_rate: 0.12
    win_rate: 0.56
  - name: Leather Cowl
    pick_rate: 0.1
    win_rate: 0.57
  source_url: https://smitebrain.com/gods/guan-yu/
  last_verified: '2026-10-11'
  god_win_rate: 0.4657534246575342
  god_matches_won: 34
  god_matches_played: 73
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-11'
  god_matches_analyzed: 5242
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Hussar's Wings
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Shield Splitter,
    Golden Blade, Runeforged Hammer, Eye of the Storm, Hydra''s Lament, Shield of
    the Phoenix, Erosion, Eye of Providence, Draconic Scale, Tyrfing, Stone of Binding,
    Pharaoh''s Curse, Avenging Blade, Lernaean Bow, Screeching Gargoyle, Magi''s Cloak,
    Shogun''s Ofuda, Midgardian Mail, Mantle Of Discord, Heartseeker, Hide of the
    Nemean Lion, Daybreak Gavel, Shifter''s Shield, Breastplate of Valor.'
  slot_scores:
    Berserker's Shield:
      total: 0.76
      efficiency: 0.68
      win: 1.0
      pick: 0.15
      fit: 0.43
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.6
      pick: 0.22
      fit: 0.49
    Hussar's Wings:
      total: 0.52
      efficiency: 0.39
      win: 0.67
      pick: 0.22
      fit: 0.5
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Berserker's Shield
  - Freya's Tears
  - Hussar's Wings
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
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Chandra''s Grace, Jotunn''s Revenge, Shield of the Phoenix,
    Kinetic Cuirass, Golden Blade, Runeforged Hammer, Shield Splitter, Eye of the
    Storm, Hydra''s Lament, The Reaper, Yogi''s Necklace, Erosion, Eye of Providence,
    Draconic Scale, Phoenix Feather, Avenging Blade, Tyrfing, Glorious Pridwen, Pharaoh''s
    Curse, Riptalon, Lernaean Bow, Shogun''s Ofuda, Stone of Binding, Screeching Gargoyle,
    Shifter''s Shield, Breastplate of Valor.'
  slot_scores:
    Chandra's Grace:
      total: 0.56
      efficiency: 0.45
      win: 0.67
      pick: 0.08
      fit: 0.64
    Berserker's Shield:
      total: 0.76
      efficiency: 0.68
      win: 1.0
      pick: 0.15
      fit: 0.45
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.22
      fit: 0.45
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Chandra's Grace
  - Berserker's Shield
  - Freya's Tears
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
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
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
    for this god: Jotunn''s Revenge, Amanita Charm, Stone of Binding, Screeching Gargoyle,
    Avenging Blade, Kinetic Cuirass, Void Shield, Heartseeker, Void Stone, Shield
    Splitter, Runeforged Hammer, Silverbranch Bow, Tekko-Kagi, Titan''s Bane, The
    Crusher, Golden Blade, Toxic Blade, Hydra''s Lament, Eye of the Storm, The Reaper,
    Shield of the Phoenix, Erosion, Eye of Providence, Draconic Scale, Tyrfing, Shifter''s
    Shield, Breastplate of Valor.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.52
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.64
    Stone of Binding:
      total: 0.52
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.66
    Berserker's Shield:
      total: 0.74
      efficiency: 0.68
      win: 1.0
      pick: 0.15
      fit: 0.32
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.6
      pick: 0.22
      fit: 0.37
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Berserker's Shield
  - Freya's Tears
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
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
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
    this god: Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Golden Blade, Tyrfing,
    Runeforged Hammer, Shield Splitter, Pharaoh''s Curse, Riptalon, Lernaean Bow,
    Silverbranch Bow, Shogun''s Ofuda, Hydra''s Lament, Shield of the Phoenix, Toxic
    Blade, Erosion, Eye of the Storm, Eye of Providence, Stone of Binding, Draconic
    Scale, Screeching Gargoyle, Daybreak Gavel, Magi''s Cloak, The Reaper, Tekko-Kagi,
    Shifter''s Shield, Breastplate of Valor.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.76
      efficiency: 0.68
      win: 1.0
      pick: 0.15
      fit: 0.43
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.24
    Tyrfing:
      total: 0.5
      efficiency: 0.48
      win: 0.55
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.6
      pick: 0.22
      fit: 0.34
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Berserker's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chandra's Grace
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Hydra's Lament
  flex_slots:
  - Kinetic Cuirass
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Chandra''s Grace, Kinetic Cuirass, Shield of the Phoenix, Hydra''s Lament, Screeching
    Gargoyle, Shield Splitter, Runeforged Hammer, Erosion, Golden Blade, Gladiator''s
    Shield, Eye of Providence, Arondight, Draconic Scale, Stone of Binding, Eye of
    the Storm, Pharaoh''s Curse, Eye of Erebus, Magi''s Cloak, Daybreak Gavel, Midgardian
    Mail, Shogun''s Ofuda, Mantle Of Discord, Breastplate of Valor, Shifter''s Shield,
    Prophetic Cloak.'
  slot_scores:
    Chandra's Grace:
      total: 0.53
      efficiency: 0.45
      win: 0.67
      pick: 0.08
      fit: 0.43
    Berserker's Shield:
      total: 0.75
      efficiency: 0.68
      win: 1.0
      pick: 0.15
      fit: 0.34
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.5
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.6
      pick: 0.22
      fit: 0.58
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.55
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Chandra's Grace
  - Berserker's Shield
  - Freya's Tears
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
    Underrated for this god: Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Breastplate
    of Valor, Shield Splitter, Shifter''s Shield, Golden Blade, Runeforged Hammer,
    Eye of the Storm, Hydra''s Lament, Shield of the Phoenix, Erosion, Eye of Providence,
    Draconic Scale, Tyrfing, Stone of Binding, Pharaoh''s Curse, Avenging Blade, Lernaean
    Bow, Screeching Gargoyle, Magi''s Cloak, Shogun''s Ofuda, Midgardian Mail, Mantle
    Of Discord, Heartseeker, Hide of the Nemean Lion, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.66
      win: 0.43
      pick: 0.16
      fit: 0.32
    Berserker's Shield:
      total: 0.76
      efficiency: 0.68
      win: 1.0
      pick: 0.15
      fit: 0.43
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.6
      pick: 0.22
      fit: 0.49
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Freya's Tears
  starter: *id001
---

---
type: smite-build
god: Guan Yu
mode: Conquest
builds:
- source: community
  aspect: Aspect of the General
  aspect_pick_rate: 0.51
  aspect_win_rate: 0.54
  slot_order:
  - name: Stampede
    pick_rate: 0.14
    win_rate: 0.58
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.11
      win_rate: 0.47
    - name: Devourer's Gauntlet
      pick_rate: 0.1
      win_rate: 0.64
  - name: Genji's Guard
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.11
      win_rate: 0.6
    - name: Chandra's Grace
      pick_rate: 0.07
      win_rate: 0.8
  - name: Freya's Tears
    pick_rate: 0.21
    win_rate: 0.54
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.38
    - name: Berserker's Shield
      pick_rate: 0.1
      win_rate: 0.77
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.15
      win_rate: 0.58
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.64
  - name: Draconic Scale
    pick_rate: 0.06
    win_rate: 0.57
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 1.0
    - name: Brawler’s Beat Stick
      pick_rate: 0.05
      win_rate: 0.67
  - name: Sage's Ring
    pick_rate: 0.07
    win_rate: 0.8
    alternates:
    - name: Captain's Ring
      pick_rate: 0.04
      win_rate: 1.0
    - name: Veve Charm
      pick_rate: 0.04
      win_rate: 0.33
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.15
    win_rate: 0.7
  - name: Bluestone Pendant
    pick_rate: 0.14
    win_rate: 0.53
  - name: Sands Of Time
    pick_rate: 0.12
    win_rate: 0.56
  source_url: https://smitebrain.com/gods/guan-yu/
  last_verified: '2026-10-30'
  god_win_rate: 0.5746268656716418
  god_matches_won: 77
  god_matches_played: 134
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-30'
  god_matches_analyzed: 10706
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Chandra's Grace
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Kinetic Cuirass
  flex_slots:
  - Freya's Tears
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Breastplate of Valor,
    Shield Splitter, Shifter''s Shield, Golden Blade, Runeforged Hammer, Eye of the
    Storm, Hydra''s Lament, Shield of the Phoenix, Erosion, Eye of Providence, Draconic
    Scale, Tyrfing, Stone of Binding, Pharaoh''s Curse, Avenging Blade, Lernaean Bow,
    Screeching Gargoyle, Magi''s Cloak, Shogun''s Ofuda, Midgardian Mail, Mantle Of
    Discord, Heartseeker, Hide of the Nemean Lion, Daybreak Gavel.'
  slot_scores:
    Chandra's Grace:
      total: 0.57
      efficiency: 0.45
      win: 0.8
      pick: 0.1
      fit: 0.3
    Berserker's Shield:
      total: 0.66
      efficiency: 0.68
      win: 0.77
      pick: 0.16
      fit: 0.43
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.4
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.54
      pick: 0.33
      fit: 0.49
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Chandra's Grace
  - Berserker's Shield
  - Freya's Tears
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
  - Kinetic Cuirass
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Chandra''s Grace, Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix,
    Kinetic Cuirass, Golden Blade, Breastplate of Valor, Runeforged Hammer, Shield
    Splitter, Shifter''s Shield, Eye of the Storm, Hydra''s Lament, The Reaper, Yogi''s
    Necklace, Erosion, Eye of Providence, Draconic Scale, Phoenix Feather, Avenging
    Blade, Tyrfing, Glorious Pridwen, Pharaoh''s Curse, Riptalon, Lernaean Bow, Shogun''s
    Ofuda, Stone of Binding, Screeching Gargoyle.'
  slot_scores:
    Chandra's Grace:
      total: 0.62
      efficiency: 0.45
      win: 0.8
      pick: 0.1
      fit: 0.64
    Berserker's Shield:
      total: 0.66
      efficiency: 0.68
      win: 0.77
      pick: 0.16
      fit: 0.45
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.54
      pick: 0.33
      fit: 0.45
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.58
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
  - Avenging Blade
  - Chandra's Grace
  - Berserker's Shield
  - Jotunn's Revenge
  flex_slots:
  - Screeching Gargoyle
  - Avenging Blade
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Stone of Binding, Screeching Gargoyle,
    Avenging Blade, Kinetic Cuirass, Breastplate of Valor, Void Shield, Heartseeker,
    Void Stone, Shield Splitter, Runeforged Hammer, Silverbranch Bow, Shifter''s Shield,
    Tekko-Kagi, Titan''s Bane, The Crusher, Golden Blade, Toxic Blade, Hydra''s Lament,
    Eye of the Storm, The Reaper, Shield of the Phoenix, Erosion, Eye of Providence,
    Draconic Scale, Tyrfing.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.53
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.64
    Stone of Binding:
      total: 0.54
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.66
    Avenging Blade:
      total: 0.53
      efficiency: 0.49
      win: 0.58
      pick: 0.0
      fit: 0.67
    Chandra's Grace:
      total: 0.56
      efficiency: 0.45
      win: 0.8
      pick: 0.1
      fit: 0.22
    Berserker's Shield:
      total: 0.64
      efficiency: 0.68
      win: 0.77
      pick: 0.16
      fit: 0.32
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Chandra's Grace
  - Berserker's Shield
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Golden Blade, Breastplate
    of Valor, Tyrfing, Shifter''s Shield, Runeforged Hammer, Shield Splitter, Pharaoh''s
    Curse, Riptalon, Lernaean Bow, Silverbranch Bow, Shogun''s Ofuda, Hydra''s Lament,
    Shield of the Phoenix, Toxic Blade, Erosion, Eye of the Storm, Eye of Providence,
    Draconic Scale, Stone of Binding, Screeching Gargoyle, Daybreak Gavel, Magi''s
    Cloak, The Reaper, Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.56
    Chandra's Grace:
      total: 0.55
      efficiency: 0.45
      win: 0.8
      pick: 0.1
      fit: 0.21
    Berserker's Shield:
      total: 0.66
      efficiency: 0.68
      win: 0.77
      pick: 0.16
      fit: 0.43
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.24
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.58
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.58
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
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Kinetic Cuirass
  flex_slots:
  - Breastplate of Valor
  - Kinetic Cuirass
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Chandra''s Grace, Jotunn''s Revenge,
    Breastplate of Valor, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Hydra''s
    Lament, Screeching Gargoyle, Shifter''s Shield, Shield Splitter, Runeforged Hammer,
    Prophetic Cloak, Erosion, Golden Blade, Gladiator''s Shield, Eye of Providence,
    Draconic Scale, Arondight, Stone of Binding, Eye of the Storm, Pharaoh''s Curse,
    Eye of Erebus, Magi''s Cloak, Daybreak Gavel, Midgardian Mail, Shogun''s Ofuda,
    Mantle Of Discord.'
  slot_scores:
    Chandra's Grace:
      total: 0.59
      efficiency: 0.45
      win: 0.8
      pick: 0.1
      fit: 0.43
    Berserker's Shield:
      total: 0.64
      efficiency: 0.68
      win: 0.77
      pick: 0.16
      fit: 0.34
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.43
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.54
      pick: 0.33
      fit: 0.58
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.58
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
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.16
      fit: 0.32
    Berserker's Shield:
      total: 0.66
      efficiency: 0.68
      win: 0.77
      pick: 0.16
      fit: 0.43
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.54
      pick: 0.33
      fit: 0.49
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Freya's Tears
  starter: *id001
---

---
type: smite-build
god: Guan Yu
mode: Conquest
builds:
- source: community
  aspect: Aspect of the General
  aspect_pick_rate: 0.3
  aspect_win_rate: 0.47
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.3
    win_rate: 0.53
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.29
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.6
  - name: Sanguine Lash
    pick_rate: 0.23
    win_rate: 0.54
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 1.0
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.14
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.43
    - name: Umbral Link
      pick_rate: 0.07
      win_rate: 0.5
  - name: Brawler’s Beat Stick
    pick_rate: 0.09
    win_rate: 0.4
    alternates:
    - name: Freya's Tears
      pick_rate: 0.22
      win_rate: 0.33
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.5
    - name: Contagion
      pick_rate: 0.04
      win_rate: 0.5
  - name: Hussar's Wings
    pick_rate: 0.08
    win_rate: 0.67
    alternates:
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.5
    - name: Medal of Defense
      pick_rate: 0.06
      win_rate: 0.0
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.26
    win_rate: 0.53
  - name: Bluestone Brooch
    pick_rate: 0.16
    win_rate: 0.56
  - name: Sands Of Time
    pick_rate: 0.09
    win_rate: 0.4
  source_url: https://smitebrain.com/gods/guan-yu/
  last_verified: '2026-10-10'
  god_win_rate: 0.42105263157894735
  god_matches_won: 24
  god_matches_played: 57
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-10'
  god_matches_analyzed: 4063
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
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Hussar's Wings
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Breastplate of Valor, Jotunn''s Revenge, Amanita Charm, Berserker''s
    Shield, Kinetic Cuirass, Shield Splitter, Golden Blade, Runeforged Hammer, Eye
    of the Storm, Hydra''s Lament, Shield of the Phoenix, Erosion, Eye of Providence,
    Draconic Scale, Tyrfing, Stone of Binding, Pharaoh''s Curse, Avenging Blade, Lernaean
    Bow, Screeching Gargoyle, Magi''s Cloak, Shogun''s Ofuda, Midgardian Mail, Mantle
    Of Discord, Heartseeker, Hide of the Nemean Lion, Daybreak Gavel.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.73
      efficiency: 0.65
      win: 1.0
      pick: 0.12
      fit: 0.32
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.4
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.22
      fit: 0.49
    Hussar's Wings:
      total: 0.53
      efficiency: 0.39
      win: 0.67
      pick: 0.25
      fit: 0.5
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  - Hussar's Wings
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
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Hussar's Wings
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Amanita Charm, Jotunn''s Revenge, Berserker''s
    Shield, Shield of the Phoenix, Kinetic Cuirass, Golden Blade, Runeforged Hammer,
    Shield Splitter, Eye of the Storm, Hydra''s Lament, The Reaper, Yogi''s Necklace,
    Erosion, Chandra''s Grace, Eye of Providence, Draconic Scale, Phoenix Feather,
    Avenging Blade, Tyrfing, Glorious Pridwen, Pharaoh''s Curse, Riptalon, Lernaean
    Bow, Shogun''s Ofuda, Stone of Binding, Screeching Gargoyle.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.73
      efficiency: 0.65
      win: 1.0
      pick: 0.12
      fit: 0.3
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.4
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.79
    Hussar's Wings:
      total: 0.53
      efficiency: 0.39
      win: 0.67
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
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Hussar's Wings
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Breastplate of Valor, Jotunn''s Revenge, Berserker''s Shield, Amanita
    Charm, Stone of Binding, Screeching Gargoyle, Avenging Blade, Kinetic Cuirass,
    Void Shield, Heartseeker, Void Stone, Shield Splitter, Runeforged Hammer, Silverbranch
    Bow, Tekko-Kagi, Titan''s Bane, The Crusher, Golden Blade, Toxic Blade, Hydra''s
    Lament, Eye of the Storm, The Reaper, Shield of the Phoenix, Erosion, Eye of Providence,
    Draconic Scale, Tyrfing.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.32
    Breastplate of Valor:
      total: 0.72
      efficiency: 0.65
      win: 1.0
      pick: 0.12
      fit: 0.24
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.22
      fit: 0.37
    Hussar's Wings:
      total: 0.51
      efficiency: 0.39
      win: 0.67
      pick: 0.25
      fit: 0.38
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  - Hussar's Wings
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Berserker''s Shield, Jotunn''s Revenge, Amanita
    Charm, Kinetic Cuirass, Golden Blade, Tyrfing, Runeforged Hammer, Shield Splitter,
    Pharaoh''s Curse, Riptalon, Lernaean Bow, Silverbranch Bow, Shogun''s Ofuda, Hydra''s
    Lament, Shield of the Phoenix, Toxic Blade, Erosion, Eye of the Storm, Eye of
    Providence, Stone of Binding, Draconic Scale, Screeching Gargoyle, Daybreak Gavel,
    Magi''s Cloak, The Reaper, Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.72
      efficiency: 0.65
      win: 1.0
      pick: 0.12
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
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Breastplate of Valor
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Hussar's Wings
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Jotunn''s Revenge,
    Amanita Charm, Berserker''s Shield, Kinetic Cuirass, Shield of the Phoenix, Hydra''s
    Lament, Screeching Gargoyle, Shield Splitter, Runeforged Hammer, Prophetic Cloak,
    Erosion, Golden Blade, Gladiator''s Shield, Eye of Providence, Arondight, Draconic
    Scale, Stone of Binding, Eye of the Storm, Pharaoh''s Curse, Eye of Erebus, Magi''s
    Cloak, Daybreak Gavel, Midgardian Mail, Shogun''s Ofuda, Mantle Of Discord, Chandra''s
    Grace.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.34
    Breastplate of Valor:
      total: 0.75
      efficiency: 0.65
      win: 1.0
      pick: 0.12
      fit: 0.44
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.43
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.22
      fit: 0.58
    Hussar's Wings:
      total: 0.51
      efficiency: 0.39
      win: 0.67
      pick: 0.25
      fit: 0.4
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
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
    Kinetic Cuirass, Breastplate of Valor, Shield Splitter, Golden Blade, Runeforged
    Hammer, Eye of the Storm, Hydra''s Lament, Shield of the Phoenix, Erosion, Eye
    of Providence, Draconic Scale, Tyrfing, Stone of Binding, Pharaoh''s Curse, Avenging
    Blade, Lernaean Bow, Screeching Gargoyle, Magi''s Cloak, Shogun''s Ofuda, Midgardian
    Mail, Mantle Of Discord, Heartseeker, Hide of the Nemean Lion, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.66
      win: 0.43
      pick: 0.19
      fit: 0.32
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
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
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.22
      fit: 0.49
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---

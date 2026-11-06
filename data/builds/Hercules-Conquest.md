---
type: smite-build
god: Hercules
mode: Conquest
builds:
- source: community
  aspect: Aspect of Preservation
  aspect_pick_rate: 0.04
  aspect_win_rate: 0.5
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.33
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.33
    - name: Jotunn's Revenge
      pick_rate: 0.1
      win_rate: 0.2
  - name: Breastplate of Valor
    pick_rate: 0.25
    win_rate: 0.42
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.43
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.67
  - name: Freya's Tears
    pick_rate: 0.23
    win_rate: 0.64
    alternates:
    - name: Genji's Guard
      pick_rate: 0.19
      win_rate: 0.22
    - name: Breastplate of Valor
      pick_rate: 0.13
      win_rate: 0.33
  - name: Genji's Guard
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.17
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.75
  - name: Engraved Guard
    pick_rate: 0.1
    win_rate: 0.25
    alternates:
    - name: Hussar's Wings
      pick_rate: 0.08
      win_rate: 0.33
    - name: Kinetic Cuirass
      pick_rate: 0.08
      win_rate: 0.33
  - name: Veve Charm
    pick_rate: 0.16
    win_rate: 0.25
    alternates:
    - name: Medallion
      pick_rate: 0.08
      win_rate: 0.5
    - name: Hussar's Wings
      pick_rate: 0.08
      win_rate: 1.0
  community_starters:
  - name: Bumba's Cudgel
    pick_rate: 0.42
    win_rate: 0.2
  - name: Bumba's Hammer
    pick_rate: 0.33
    win_rate: 0.5
  - name: Bluestone Brooch
    pick_rate: 0.06
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/hercules/
  last_verified: '2026-11-06'
  god_win_rate: 0.375
  god_matches_won: 18
  god_matches_played: 48
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Shield Splitter
  - Genji's Guard
  - Shell of Rebuke
  - Freya's Tears
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Genji's Guard
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield Splitter, Berserker''s Shield, Draconic Scale,
    Shield of the Phoenix, Runeforged Hammer, Erosion, Oni Hunter''s Garb, Eye of
    Providence, Hydra''s Lament, The Reaper, Midgardian Mail, Stone of Binding, Screeching
    Gargoyle, Leviathan''s Hide, Magi''s Cloak, Mantle Of Discord, Hide of the Nemean
    Lion, Wyrmskin Hide, Avenging Blade, Tyrfing, Ancile, Arondight, The Crusher,
    Jotunn''s Revenge.'
  slot_scores:
    Shield Splitter:
      total: 0.52
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.6
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.15
      fit: 0.29
    Shell of Rebuke:
      total: 0.54
      efficiency: 0.41
      win: 0.75
      pick: 0.15
      fit: 0.38
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.64
      pick: 0.36
      fit: 0.48
    Hussar's Wings:
      total: 0.68
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.54
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Genji's Guard
  - Shell of Rebuke
  - Freya's Tears
  - Hussar's Wings
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Shield of the Phoenix
  - Genji's Guard
  - Shell of Rebuke
  - Freya's Tears
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Shell of Rebuke
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, The Reaper, Berserker''s Shield,
    Shield Splitter, Phoenix Feather, Yogi''s Necklace, Runeforged Hammer, Draconic
    Scale, Chandra''s Grace, Oni Hunter''s Garb, Erosion, Hydra''s Lament, Eye of
    Providence, Bloodforge, Midgardian Mail, Regrowth Striders, Leviathan''s Hide,
    Avenging Blade, Glorious Pridwen, Wyrmskin Hide, Hide of the Nemean Lion, Screeching
    Gargoyle, Stone of Binding, Jotunn''s Revenge.'
  slot_scores:
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.76
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.15
      fit: 0.26
    Shell of Rebuke:
      total: 0.53
      efficiency: 0.41
      win: 0.75
      pick: 0.15
      fit: 0.32
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.64
      pick: 0.36
      fit: 0.42
    Hussar's Wings:
      total: 0.68
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.52
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.82
  community_ordered:
  - Genji's Guard
  - Shell of Rebuke
  - Freya's Tears
  - Hussar's Wings
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Shell of Rebuke
  - Freya's Tears
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Screeching Gargoyle, The Reaper, Stone of Binding,
    Shield Splitter, Berserker''s Shield, Avenging Blade, Void Stone, The Crusher,
    Void Shield, Heartseeker, Titan''s Bane, Shield of the Phoenix, Runeforged Hammer,
    Draconic Scale, Oni Hunter''s Garb, Hydra''s Lament, Erosion, Eye of Providence,
    Midgardian Mail, Leviathan''s Hide, Avatar''s Parashu, Magi''s Cloak, Mantle Of
    Discord, Jotunn''s Revenge.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.5
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.62
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.5
      pick: 0.15
      fit: 0.22
    Shell of Rebuke:
      total: 0.53
      efficiency: 0.41
      win: 0.75
      pick: 0.15
      fit: 0.29
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.64
      pick: 0.36
      fit: 0.36
    Hussar's Wings:
      total: 0.66
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.4
    Amanita Charm:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  - Shell of Rebuke
  - Freya's Tears
  - Hussar's Wings
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Tyrfing
  - Shell of Rebuke
  - Freya's Tears
  - Hussar's Wings
  flex_slots:
  - Tyrfing
  - Golden Blade
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Tyrfing, Golden Blade, Shield Splitter,
    Shield of the Phoenix, Oni Hunter''s Garb, Draconic Scale, Runeforged Hammer,
    Shogun''s Ofuda, Pharaoh''s Curse, Erosion, Eye of Providence, Hydra''s Lament,
    Toxic Blade, Screeching Gargoyle, Midgardian Mail, The Reaper, Stone of Binding,
    Lernaean Bow, Dominance, Leviathan''s Hide, Silverbranch Bow, Magi''s Cloak, Jotunn''s
    Revenge.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.45
    Tyrfing:
      total: 0.49
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shell of Rebuke:
      total: 0.53
      efficiency: 0.41
      win: 0.75
      pick: 0.15
      fit: 0.27
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.64
      pick: 0.36
      fit: 0.34
    Hussar's Wings:
      total: 0.66
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.38
  community_ordered:
  - Shell of Rebuke
  - Freya's Tears
  - Hussar's Wings
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Shield of the Phoenix
  - Shell of Rebuke
  - Freya's Tears
  - Hussar's Wings
  flex_slots:
  - Shield of the Phoenix
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Shield of the Phoenix,
    Berserker''s Shield, Screeching Gargoyle, Hydra''s Lament, Shield Splitter, Gladiator''s
    Shield, Draconic Scale, Oni Hunter''s Garb, Prophetic Cloak, Arondight, Erosion,
    Eye of Providence, Runeforged Hammer, Midgardian Mail, Stone of Binding, Chandra''s
    Grace, Leviathan''s Hide, Regrowth Striders, The Reaper, Magi''s Cloak, Mantle
    Of Discord, Hide of the Nemean Lion, Eye of Erebus, Jotunn''s Revenge.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.27
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.5
      pick: 0.15
      fit: 0.44
    Shield of the Phoenix:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.56
    Shell of Rebuke:
      total: 0.53
      efficiency: 0.41
      win: 0.75
      pick: 0.15
      fit: 0.3
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.64
      pick: 0.36
      fit: 0.59
    Hussar's Wings:
      total: 0.66
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.41
  community_ordered:
  - Genji's Guard
  - Shell of Rebuke
  - Freya's Tears
  - Hussar's Wings
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Shield Splitter, Jotunn''s Revenge, Berserker''s
    Shield, Draconic Scale, Shield of the Phoenix, Runeforged Hammer, Erosion, Oni
    Hunter''s Garb, Eye of Providence, Hydra''s Lament, The Reaper, Midgardian Mail,
    Stone of Binding, Screeching Gargoyle, Leviathan''s Hide, Magi''s Cloak, Mantle
    Of Discord, Hide of the Nemean Lion, Wyrmskin Hide, Avenging Blade, Tyrfing, Ancile,
    Arondight, The Crusher.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.38
      efficiency: 0.65
      win: 0.2
      pick: 0.1
      fit: 0.36
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.15
      fit: 0.29
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.61
      win: 0.33
      pick: 0.17
      fit: 0.64
    Shield Splitter:
      total: 0.52
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.64
      pick: 0.36
      fit: 0.48
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Shield of the Phoenix
  - Shell of Rebuke
  - Freya's Tears
  - Hussar's Wings
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Erosion, Shield of the Phoenix, Berserker''s Shield,
    Shield Splitter, Void Stone, The Reaper, Stampede, Void Shield, Spectral Armor,
    Doublet of Binding, Runeforged Hammer, Sanguine Lash, Draconic Scale, Phoenix
    Feather, Oni Hunter''s Garb, Umbral Link, Eye of Providence, Yogi''s Necklace,
    Shogun''s Ofuda, Mystical Mail, Hydra''s Lament, Midgardian Mail, Pharaoh''s Curse,
    Jotunn''s Revenge.'
  slot_scores:
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.69
    Shell of Rebuke:
      total: 0.54
      efficiency: 0.41
      win: 0.75
      pick: 0.15
      fit: 0.33
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.64
      pick: 0.36
      fit: 0.43
    Hussar's Wings:
      total: 0.68
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.55
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.53
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Shell of Rebuke
  - Freya's Tears
  - Hussar's Wings
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: bruiser
  slot_order:
  - Shield of the Phoenix
  - Shell of Rebuke
  - Freya's Tears
  - Hussar's Wings
  - Amanita Charm
  - Erosion
  flex_slots:
  - Shell of Rebuke
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Erosion, The Reaper, Berserker''s
    Shield, Shield Splitter, Void Stone, Phoenix Feather, Stampede, Umbral Link, Void
    Shield, Spectral Armor, Sanguine Lash, Yogi''s Necklace, Runeforged Hammer, Doublet
    of Binding, Draconic Scale, Chandra''s Grace, Oni Hunter''s Garb, Hydra''s Lament,
    Eye of Providence, Bloodforge, Shogun''s Ofuda, Mystical Mail, Jotunn''s Revenge.'
  slot_scores:
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.76
    Shell of Rebuke:
      total: 0.53
      efficiency: 0.41
      win: 0.75
      pick: 0.15
      fit: 0.32
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.64
      pick: 0.36
      fit: 0.42
    Hussar's Wings:
      total: 0.68
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.52
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.53
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.82
  community_ordered:
  - Shell of Rebuke
  - Freya's Tears
  - Hussar's Wings
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: anti-tank
  slot_order:
  - Shell of Rebuke
  - Void Shield
  - Void Stone
  - Freya's Tears
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Void Shield
  - Shell of Rebuke
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Void Stone, Void Shield, The Reaper, Erosion, Shield
    of the Phoenix, Screeching Gargoyle, Berserker''s Shield, Avenging Blade, Stone
    of Binding, Stampede, Spectral Armor, Shield Splitter, Doublet of Binding, The
    Crusher, Runeforged Hammer, Heartseeker, Sanguine Lash, Phoenix Feather, Umbral
    Link, Oni Hunter''s Garb, Yogi''s Necklace, Draconic Scale, Titan''s Bane, Shogun''s
    Ofuda, Jotunn''s Revenge.'
  slot_scores:
    Shell of Rebuke:
      total: 0.52
      efficiency: 0.41
      win: 0.75
      pick: 0.15
      fit: 0.25
    Void Shield:
      total: 0.54
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.99
    Void Stone:
      total: 0.54
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.99
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.64
      pick: 0.36
      fit: 0.32
    Hussar's Wings:
      total: 0.66
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.42
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.92
  community_ordered:
  - Shell of Rebuke
  - Freya's Tears
  - Hussar's Wings
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Freya's Tears
  - Amanita Charm
  - Hussar's Wings
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Shogun's Ofuda
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shell of Rebuke — magical protection
    swap_item: Shell of Rebuke
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Shogun''s Ofuda, Pharaoh''s Curse,
    Erosion, Shield of the Phoenix, Tyrfing, Golden Blade, Void Stone, Stampede, Void
    Shield, Spectral Armor, The Reaper, Doublet of Binding, Shield Splitter, Phoenix
    Feather, Riptalon, Umbral Link, Yogi''s Necklace, Oni Hunter''s Garb, Runeforged
    Hammer, Draconic Scale, Sanguine Lash, Toxic Blade, Mystical Mail, Jotunn''s Revenge.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.64
      pick: 0.36
      fit: 0.31
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.9
    Hussar's Wings:
      total: 0.66
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.4
    Pharaoh's Curse:
      total: 0.51
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.78
    Shogun's Ofuda:
      total: 0.51
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.78
  community_ordered:
  - Freya's Tears
  - Hussar's Wings
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: cooldown
  slot_order:
  - Shield of the Phoenix
  - Genji's Guard
  - Shell of Rebuke
  - Freya's Tears
  - Hussar's Wings
  - Erosion
  flex_slots:
  - Shell of Rebuke
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Shield of the Phoenix,
    Erosion, Berserker''s Shield, Void Stone, Chandra''s Grace, Stampede, Void Shield,
    Spectral Armor, Hydra''s Lament, Screeching Gargoyle, Doublet of Binding, The
    Reaper, Regrowth Striders, Shield Splitter, Phoenix Feather, Gladiator''s Shield,
    Umbral Link, Oni Hunter''s Garb, Yogi''s Necklace, Draconic Scale, Glorious Pridwen,
    Runeforged Hammer, Shogun''s Ofuda, Mystical Mail, Jotunn''s Revenge.'
  slot_scores:
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.79
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.15
      fit: 0.42
    Shell of Rebuke:
      total: 0.53
      efficiency: 0.41
      win: 0.75
      pick: 0.15
      fit: 0.26
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.64
      pick: 0.36
      fit: 0.55
    Hussar's Wings:
      total: 0.66
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.43
    Erosion:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.73
  community_ordered:
  - Genji's Guard
  - Shell of Rebuke
  - Freya's Tears
  - Hussar's Wings
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Amanita Charm
  - Erosion
  flex_slots:
  - Genji's Guard
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Erosion, Shield of the Phoenix, Berserker''s
    Shield, Shield Splitter, Void Stone, The Reaper, Stampede, Jotunn''s Revenge,
    Void Shield, Spectral Armor, Doublet of Binding, Runeforged Hammer, Sanguine Lash,
    Draconic Scale, Phoenix Feather, Oni Hunter''s Garb, Umbral Link, Eye of Providence,
    Yogi''s Necklace, Shogun''s Ofuda, Mystical Mail, Hydra''s Lament, Midgardian
    Mail, Pharaoh''s Curse.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.39
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.15
      fit: 0.26
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.61
      win: 0.33
      pick: 0.17
      fit: 0.65
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.69
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.53
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  starter: *id001
  aspect: Aspect of Preservation
---

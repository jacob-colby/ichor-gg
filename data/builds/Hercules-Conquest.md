---
type: smite-build
god: Hercules
mode: Conquest
builds:
- source: community
  aspect: Aspect of Preservation
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.22
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.2
    win_rate: 0.39
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.18
      win_rate: 0.44
    - name: Runeforged Hammer
      pick_rate: 0.1
      win_rate: 0.61
  - name: Breastplate of Valor
    pick_rate: 0.16
    win_rate: 0.61
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.48
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.47
  - name: Genji's Guard
    pick_rate: 0.14
    win_rate: 0.6
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.36
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.17
    win_rate: 0.44
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.54
    - name: Regrowth Striders
      pick_rate: 0.05
      win_rate: 0.6
  - name: Hide of the Nemean Lion
    pick_rate: 0.05
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.64
    - name: Brawler’s Beat Stick
      pick_rate: 0.05
      win_rate: 0.58
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.64
    alternates:
    - name: Sage's Ring
      pick_rate: 0.06
      win_rate: 0.5
    - name: Medal of Defense
      pick_rate: 0.06
      win_rate: 0.4
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.42
    win_rate: 0.61
  - name: Bumba's Cudgel
    pick_rate: 0.33
    win_rate: 0.39
  - name: War Banner
    pick_rate: 0.06
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/hercules/
  last_verified: '2026-11-04'
  god_win_rate: 0.4838709677419355
  god_matches_won: 150
  god_matches_played: 310
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-03'
  god_matches_analyzed: 14667
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield Splitter
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Shield Splitter
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Runeforged Hammer, Shield Splitter,
    Berserker''s Shield, Draconic Scale, Shield of the Phoenix, Erosion, Oni Hunter''s
    Garb, Eye of Providence, Hydra''s Lament, The Reaper, Midgardian Mail, Stone of
    Binding, Screeching Gargoyle, Leviathan''s Hide, Magi''s Cloak, Mantle Of Discord,
    Wyrmskin Hide, Avenging Blade, Tyrfing, Ancile, Arondight, The Crusher, Hide of
    the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.6
      pick: 0.22
      fit: 0.29
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.63
      win: 0.61
      pick: 0.22
      fit: 0.29
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.64
    Shield Splitter:
      total: 0.54
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.6
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.55
      win: 0.61
      pick: 0.1
      fit: 0.47
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Runeforged Hammer
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Breastplate of Valor
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
    this god: Amanita Charm, Shield of the Phoenix, Runeforged Hammer, Kinetic Cuirass,
    The Reaper, Berserker''s Shield, Shield Splitter, Regrowth Striders, Phoenix Feather,
    Yogi''s Necklace, Draconic Scale, Chandra''s Grace, Oni Hunter''s Garb, Erosion,
    Hydra''s Lament, Eye of Providence, Bloodforge, Midgardian Mail, Leviathan''s
    Hide, Avenging Blade, Glorious Pridwen, Wyrmskin Hide, Screeching Gargoyle, Stone
    of Binding, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.6
      pick: 0.22
      fit: 0.26
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.63
      win: 0.61
      pick: 0.22
      fit: 0.26
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.62
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.76
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.55
      win: 0.61
      pick: 0.1
      fit: 0.52
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.82
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Runeforged Hammer
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Kinetic Cuirass, Runeforged Hammer, Screeching Gargoyle,
    The Reaper, Stone of Binding, Shield Splitter, Berserker''s Shield, Avenging Blade,
    Void Stone, The Crusher, Void Shield, Heartseeker, Titan''s Bane, Shield of the
    Phoenix, Draconic Scale, Oni Hunter''s Garb, Hydra''s Lament, Erosion, Eye of
    Providence, Midgardian Mail, Leviathan''s Hide, Avatar''s Parashu, Magi''s Cloak,
    Mantle Of Discord.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.52
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.62
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.6
      pick: 0.22
      fit: 0.22
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.63
      win: 0.61
      pick: 0.22
      fit: 0.22
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.5
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.55
      win: 0.61
      pick: 0.1
      fit: 0.38
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Runeforged Hammer
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Tyrfing
  - Golden Blade
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
    this god: Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Runeforged Hammer,
    Tyrfing, Golden Blade, Shield Splitter, Shield of the Phoenix, Oni Hunter''s Garb,
    Draconic Scale, Shogun''s Ofuda, Pharaoh''s Curse, Erosion, Eye of Providence,
    Hydra''s Lament, Toxic Blade, Screeching Gargoyle, Midgardian Mail, The Reaper,
    Stone of Binding, Lernaean Bow, Dominance, Leviathan''s Hide, Silverbranch Bow,
    Magi''s Cloak.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.56
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.6
      pick: 0.22
      fit: 0.21
    Berserker's Shield:
      total: 0.56
      efficiency: 0.72
      win: 0.54
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.63
      win: 0.61
      pick: 0.22
      fit: 0.21
    Tyrfing:
      total: 0.51
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Runeforged Hammer
  - Freya's Tears
  flex_slots:
  - Runeforged Hammer
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    + fit + win/pick). Underrated for this god: Amanita Charm, Kinetic Cuirass, Shield
    of the Phoenix, Runeforged Hammer, Berserker''s Shield, Screeching Gargoyle, Hydra''s
    Lament, Regrowth Striders, Shield Splitter, Gladiator''s Shield, Draconic Scale,
    Oni Hunter''s Garb, Prophetic Cloak, Arondight, Erosion, Eye of Providence, Midgardian
    Mail, Stone of Binding, Chandra''s Grace, Leviathan''s Hide, The Reaper, Magi''s
    Cloak, Mantle Of Discord, Eye of Erebus, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.6
      pick: 0.22
      fit: 0.44
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.63
      win: 0.61
      pick: 0.22
      fit: 0.44
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.51
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.56
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.55
      win: 0.61
      pick: 0.1
      fit: 0.31
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.44
      pick: 0.28
      fit: 0.59
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Runeforged Hammer
  - Freya's Tears
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Shield Splitter, Berserker''s
    Shield, Draconic Scale, Shield of the Phoenix, Runeforged Hammer, Erosion, Oni
    Hunter''s Garb, Eye of Providence, Hydra''s Lament, The Reaper, Midgardian Mail,
    Stone of Binding, Screeching Gargoyle, Leviathan''s Hide, Magi''s Cloak, Mantle
    Of Discord, Hide of the Nemean Lion, Wyrmskin Hide, Avenging Blade, Tyrfing, Ancile,
    Arondight, The Crusher.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.65
      win: 0.39
      pick: 0.2
      fit: 0.36
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.6
      pick: 0.22
      fit: 0.29
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.64
    Shield Splitter:
      total: 0.54
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.44
      pick: 0.28
      fit: 0.48
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Jotunn's Revenge
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Runeforged Hammer
  - Amanita Charm
  - Erosion
  flex_slots:
  - Runeforged Hammer
  - Breastplate of Valor
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Erosion, Runeforged Hammer, Shield of
    the Phoenix, Berserker''s Shield, Shield Splitter, Void Stone, The Reaper, Stampede,
    Void Shield, Spectral Armor, Doublet of Binding, Sanguine Lash, Draconic Scale,
    Phoenix Feather, Oni Hunter''s Garb, Umbral Link, Eye of Providence, Yogi''s Necklace,
    Shogun''s Ofuda, Mystical Mail, Hydra''s Lament, Midgardian Mail, Pharaoh''s Curse.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.6
      pick: 0.22
      fit: 0.26
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.63
      win: 0.61
      pick: 0.22
      fit: 0.26
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.65
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.55
      win: 0.61
      pick: 0.1
      fit: 0.53
    Amanita Charm:
      total: 0.63
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.55
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Runeforged Hammer
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Runeforged Hammer, Kinetic Cuirass,
    Erosion, The Reaper, Berserker''s Shield, Shield Splitter, Void Stone, Phoenix
    Feather, Stampede, Umbral Link, Void Shield, Spectral Armor, Sanguine Lash, Yogi''s
    Necklace, Doublet of Binding, Draconic Scale, Chandra''s Grace, Oni Hunter''s
    Garb, Hydra''s Lament, Eye of Providence, Bloodforge, Shogun''s Ofuda, Mystical
    Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.6
      pick: 0.22
      fit: 0.26
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.63
      win: 0.61
      pick: 0.22
      fit: 0.26
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.62
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.76
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.55
      win: 0.61
      pick: 0.1
      fit: 0.52
    Amanita Charm:
      total: 0.63
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Runeforged Hammer
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Runeforged Hammer
  - Void Shield
  - Void Stone
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Void Stone, Void Shield, The Reaper, Runeforged Hammer,
    Kinetic Cuirass, Erosion, Shield of the Phoenix, Screeching Gargoyle, Berserker''s
    Shield, Avenging Blade, Stone of Binding, Stampede, Spectral Armor, Shield Splitter,
    Doublet of Binding, The Crusher, Heartseeker, Sanguine Lash, Phoenix Feather,
    Umbral Link, Oni Hunter''s Garb, Yogi''s Necklace, Draconic Scale, Titan''s Bane,
    Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.6
      pick: 0.22
      fit: 0.2
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.63
      win: 0.61
      pick: 0.22
      fit: 0.2
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.55
      win: 0.61
      pick: 0.1
      fit: 0.42
    Void Shield:
      total: 0.55
      efficiency: 0.46
      win: 0.54
      pick: 0.0
      fit: 0.99
    Void Stone:
      total: 0.56
      efficiency: 0.47
      win: 0.54
      pick: 0.0
      fit: 0.99
    Amanita Charm:
      total: 0.62
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.92
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Runeforged Hammer
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Breastplate of Valor
  - Amanita Charm
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
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Kinetic Cuirass, Shogun''s Ofuda,
    Pharaoh''s Curse, Erosion, Runeforged Hammer, Shield of the Phoenix, Tyrfing,
    Golden Blade, Void Stone, Stampede, Void Shield, Spectral Armor, The Reaper, Doublet
    of Binding, Shield Splitter, Phoenix Feather, Riptalon, Umbral Link, Yogi''s Necklace,
    Oni Hunter''s Garb, Draconic Scale, Sanguine Lash, Toxic Blade, Mystical Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.72
      win: 0.54
      pick: 0.0
      fit: 0.48
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.6
      pick: 0.22
      fit: 0.19
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.63
      win: 0.61
      pick: 0.22
      fit: 0.19
    Amanita Charm:
      total: 0.62
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.9
    Pharaoh's Curse:
      total: 0.53
      efficiency: 0.49
      win: 0.54
      pick: 0.0
      fit: 0.78
    Shogun's Ofuda:
      total: 0.53
      efficiency: 0.49
      win: 0.54
      pick: 0.0
      fit: 0.78
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Runeforged Hammer
  - Erosion
  flex_slots:
  - Erosion
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Regrowth Striders — physical protection
    swap_item: Regrowth Striders
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Shield of the Phoenix,
    Kinetic Cuirass, Erosion, Regrowth Striders, Runeforged Hammer, Berserker''s Shield,
    Void Stone, Chandra''s Grace, Stampede, Void Shield, Spectral Armor, Hydra''s
    Lament, Screeching Gargoyle, Doublet of Binding, The Reaper, Shield Splitter,
    Phoenix Feather, Gladiator''s Shield, Umbral Link, Oni Hunter''s Garb, Yogi''s
    Necklace, Draconic Scale, Glorious Pridwen, Shogun''s Ofuda, Mystical Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.6
      pick: 0.22
      fit: 0.42
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.63
      win: 0.61
      pick: 0.22
      fit: 0.42
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.53
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.79
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.55
      win: 0.61
      pick: 0.1
      fit: 0.36
    Erosion:
      total: 0.53
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.73
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Runeforged Hammer
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Erosion, Shield of the
    Phoenix, Berserker''s Shield, Shield Splitter, Void Stone, The Reaper, Stampede,
    Void Shield, Spectral Armor, Doublet of Binding, Runeforged Hammer, Sanguine Lash,
    Draconic Scale, Phoenix Feather, Oni Hunter''s Garb, Umbral Link, Eye of Providence,
    Yogi''s Necklace, Shogun''s Ofuda, Mystical Mail, Hydra''s Lament, Midgardian
    Mail, Pharaoh''s Curse.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.39
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.6
      pick: 0.22
      fit: 0.26
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.65
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.69
    Amanita Charm:
      total: 0.63
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.55
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Genji's Guard
  starter: *id001
  aspect: Aspect of Preservation
---

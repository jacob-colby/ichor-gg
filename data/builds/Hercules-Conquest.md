---
type: smite-build
god: Hercules
mode: Conquest
builds:
- source: community
  aspect: Aspect of Preservation
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.2
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.23
    win_rate: 0.44
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.43
    - name: Runeforged Hammer
      pick_rate: 0.11
      win_rate: 0.52
  - name: Breastplate of Valor
    pick_rate: 0.16
    win_rate: 0.48
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.44
    - name: Hydra's Lament
      pick_rate: 0.09
      win_rate: 0.5
  - name: Genji's Guard
    pick_rate: 0.14
    win_rate: 0.64
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.32
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.44
  - name: Freya's Tears
    pick_rate: 0.12
    win_rate: 0.35
    alternates:
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.44
    - name: Hussar's Wings
      pick_rate: 0.06
      win_rate: 0.73
  - name: Brawler’s Beat Stick
    pick_rate: 0.06
    win_rate: 0.64
    alternates:
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.62
    - name: Genji's Guard
      pick_rate: 0.05
      win_rate: 0.44
  - name: Sage's Ring
    pick_rate: 0.08
    win_rate: 0.56
    alternates:
    - name: Medal of Defense
      pick_rate: 0.06
      win_rate: 0.43
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.5
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.4
    win_rate: 0.6
  - name: Bumba's Cudgel
    pick_rate: 0.33
    win_rate: 0.42
  - name: Archmage's Gem
    pick_rate: 0.05
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/hercules/
  last_verified: '2026-10-29'
  god_win_rate: 0.475
  god_matches_won: 95
  god_matches_played: 200
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
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Shield Splitter
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Brawler’s Beat Stick — magical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged Hammer,
    Eye of the Storm, Erosion, Berserker''s Shield, Eye of Providence, Hydra''s Lament,
    Draconic Scale, Shield of the Phoenix, Shifter''s Shield, Stone of Binding, Magi''s
    Cloak, Avenging Blade, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle,
    Hide of the Nemean Lion, Heartseeker, Leviathan''s Hide, Void Shield, Stampede,
    Ancile, Prophetic Cloak, Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.44
      pick: 0.23
      fit: 0.4
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.64
      pick: 0.22
      fit: 0.33
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.7
    Shield Splitter:
      total: 0.52
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.67
    Hussar's Wings:
      total: 0.56
      efficiency: 0.39
      win: 0.73
      pick: 0.1
      fit: 0.6
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Jotunn's Revenge
  - Genji's Guard
  - Hussar's Wings
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Jotunn's Revenge
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Runeforged Hammer,
    Shield Splitter, Eye of the Storm, Berserker''s Shield, Hydra''s Lament, Erosion,
    The Reaper, Eye of Providence, Draconic Scale, Yogi''s Necklace, Avenging Blade,
    Phoenix Feather, Shifter''s Shield, Chandra''s Grace, Glorious Pridwen, Stone
    of Binding, Midgardian Mail, Hide of the Nemean Lion, Daybreak Gavel, Magi''s
    Cloak, Leviathan''s Hide, Heartseeker, Void Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.44
      pick: 0.23
      fit: 0.42
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.64
      pick: 0.22
      fit: 0.3
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.68
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.82
    Hussar's Wings:
      total: 0.56
      efficiency: 0.39
      win: 0.73
      pick: 0.1
      fit: 0.58
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Jotunn's Revenge
  - Genji's Guard
  - Hussar's Wings
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Avenging Blade
  - Genji's Guard
  - Jotunn's Revenge
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Avenging Blade
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Stone of Binding, Avenging Blade, Kinetic Cuirass,
    Screeching Gargoyle, Runeforged Hammer, Heartseeker, Void Shield, Shield Splitter,
    Void Stone, Titan''s Bane, Berserker''s Shield, The Crusher, Hydra''s Lament,
    Eye of the Storm, The Reaper, Erosion, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Shifter''s Shield, Magi''s Cloak, Pendulum Blade, Avatar''s Parashu,
    Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Stone of Binding:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.71
    Avenging Blade:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.7
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.64
      pick: 0.22
      fit: 0.24
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.44
      pick: 0.23
      fit: 0.57
    Hussar's Wings:
      total: 0.54
      efficiency: 0.39
      win: 0.73
      pick: 0.1
      fit: 0.43
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Genji's Guard
  - Jotunn's Revenge
  - Hussar's Wings
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Tyrfing
  - Hussar's Wings
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Golden Blade, Runeforged
    Hammer, Tyrfing, Shield Splitter, Pharaoh''s Curse, Riptalon, Lernaean Bow, Shogun''s
    Ofuda, Silverbranch Bow, Hydra''s Lament, Erosion, Eye of Providence, Stone of
    Binding, Toxic Blade, Eye of the Storm, Shield of the Phoenix, Draconic Scale,
    Magi''s Cloak, Shifter''s Shield, Screeching Gargoyle, Daybreak Gavel, The Reaper,
    Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.56
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.64
      pick: 0.22
      fit: 0.21
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.45
    Tyrfing:
      total: 0.48
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.55
    Hussar's Wings:
      total: 0.53
      efficiency: 0.39
      win: 0.73
      pick: 0.1
      fit: 0.38
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Genji's Guard
  - Hussar's Wings
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
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
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Kinetic Cuirass, Shield
    of the Phoenix, Hydra''s Lament, Screeching Gargoyle, Runeforged Hammer, Shield
    Splitter, Berserker''s Shield, Prophetic Cloak, Erosion, Eye of Providence, Gladiator''s
    Shield, Draconic Scale, Stone of Binding, Eye of the Storm, Arondight, Shifter''s
    Shield, Magi''s Cloak, Eye of Erebus, Mantle Of Discord, Glorious Pridwen, Midgardian
    Mail, Daybreak Gavel, Chandra''s Grace, Hide of the Nemean Lion, Leviathan''s
    Hide.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.48
      pick: 0.22
      fit: 0.48
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.64
      pick: 0.22
      fit: 0.48
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.44
      pick: 0.23
      fit: 0.46
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.55
    Hussar's Wings:
      total: 0.54
      efficiency: 0.39
      win: 0.73
      pick: 0.1
      fit: 0.45
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Jotunn's Revenge
  - Hussar's Wings
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Shifter's Shield
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Shield Splitter, Shifter''s
    Shield, Runeforged Hammer, Eye of the Storm, Erosion, Berserker''s Shield, Eye
    of Providence, Draconic Scale, Shield of the Phoenix, Hydra''s Lament, Stone of
    Binding, Magi''s Cloak, Avenging Blade, Mantle Of Discord, Midgardian Mail, Screeching
    Gargoyle, Hide of the Nemean Lion, Heartseeker, Leviathan''s Hide, Void Shield,
    Stampede, Ancile, Prophetic Cloak, Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.44
      pick: 0.23
      fit: 0.4
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.7
    Shield Splitter:
      total: 0.52
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.67
    Freya's Tears:
      total: 0.46
      efficiency: 0.61
      win: 0.35
      pick: 0.2
      fit: 0.54
    Shifter's Shield:
      total: 0.48
      efficiency: 0.55
      win: 0.43
      pick: 0.14
      fit: 0.6
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Runeforged Hammer
  - Hussar's Wings
  - Amanita Charm
  - Erosion
  flex_slots:
  - Kinetic Cuirass
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Erosion, Kinetic Cuirass, Runeforged Hammer, Shield of
    the Phoenix, Void Shield, Stampede, Void Stone, Spectral Armor, Shield Splitter,
    Eye of the Storm, Doublet of Binding, Berserker''s Shield, Eye of Providence,
    Draconic Scale, Shogun''s Ofuda, Hydra''s Lament, Pharaoh''s Curse, Shifter''s
    Shield, Avenging Blade, Mystical Mail, Midgardian Mail, Sanguine Lash, Stone of
    Binding, Yogi''s Necklace, Phoenix Feather.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.71
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.64
      pick: 0.22
      fit: 0.29
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.57
      win: 0.52
      pick: 0.11
      fit: 0.58
    Hussar's Wings:
      total: 0.56
      efficiency: 0.39
      win: 0.73
      pick: 0.1
      fit: 0.61
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.54
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Genji's Guard
  - Runeforged Hammer
  - Hussar's Wings
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Shield of the Phoenix
  - Hussar's Wings
  - Amanita Charm
  - Erosion
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Erosion, Shield of the Phoenix, Kinetic Cuirass, Runeforged
    Hammer, Void Shield, Stampede, Shield Splitter, Void Stone, Spectral Armor, Eye
    of the Storm, Doublet of Binding, Berserker''s Shield, Hydra''s Lament, The Reaper,
    Eye of Providence, Draconic Scale, Yogi''s Necklace, Avenging Blade, Shogun''s
    Ofuda, Phoenix Feather, Pharaoh''s Curse, Shifter''s Shield, Chandra''s Grace,
    Mystical Mail, Sanguine Lash.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.68
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.64
      pick: 0.22
      fit: 0.3
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.82
    Hussar's Wings:
      total: 0.56
      efficiency: 0.39
      win: 0.73
      pick: 0.1
      fit: 0.58
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.54
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Genji's Guard
  - Hussar's Wings
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Void Shield
  - Void Stone
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Hussar's Wings
  - Void Stone
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Void Shield, Void Stone, Erosion, Avenging Blade,
    Kinetic Cuirass, Runeforged Hammer, Stone of Binding, Shield of the Phoenix, The
    Reaper, Stampede, Screeching Gargoyle, Spectral Armor, Heartseeker, Doublet of
    Binding, Shield Splitter, Berserker''s Shield, Eye of the Storm, Titan''s Bane,
    The Crusher, Hydra''s Lament, Shogun''s Ofuda, Eye of Providence, Pharaoh''s Curse,
    Draconic Scale, Shifter''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.44
      pick: 0.23
      fit: 0.55
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.64
      pick: 0.22
      fit: 0.21
    Void Shield:
      total: 0.54
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 1.0
    Void Stone:
      total: 0.53
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
    Hussar's Wings:
      total: 0.54
      efficiency: 0.39
      win: 0.73
      pick: 0.1
      fit: 0.45
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.95
  community_ordered:
  - Jotunn's Revenge
  - Genji's Guard
  - Hussar's Wings
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Hussar's Wings
  - Amanita Charm
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Pharaoh's Curse
  - Shogun's Ofuda
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Pharaoh''s Curse, Shogun''s Ofuda,
    Erosion, Riptalon, Kinetic Cuirass, Golden Blade, Shield of the Phoenix, Runeforged
    Hammer, Void Shield, Stampede, Void Stone, Spectral Armor, Doublet of Binding,
    Umbral Link, The Reaper, Tyrfing, Eros'' Bow, Shield Splitter, Sanguine Lash,
    Lernaean Bow, Toxic Blade, Eye of the Storm, Silverbranch Bow, Shifter''s Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.48
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.64
      pick: 0.22
      fit: 0.19
    Hussar's Wings:
      total: 0.53
      efficiency: 0.39
      win: 0.73
      pick: 0.1
      fit: 0.4
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.9
    Pharaoh's Curse:
      total: 0.52
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.78
    Shogun's Ofuda:
      total: 0.52
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.78
  community_ordered:
  - Genji's Guard
  - Hussar's Wings
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Hussar's Wings
  - Erosion
  flex_slots:
  - Breastplate of Valor
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Shield of the Phoenix,
    Erosion, Kinetic Cuirass, Void Shield, Stampede, Hydra''s Lament, Runeforged Hammer,
    Void Stone, Spectral Armor, Chandra''s Grace, Doublet of Binding, Screeching Gargoyle,
    Berserker''s Shield, Glorious Pridwen, Gladiator''s Shield, Shield Splitter, Eye
    of Providence, Shogun''s Ofuda, Pharaoh''s Curse, Draconic Scale, Eye of the Storm,
    Mystical Mail, Prophetic Cloak, Eye of Erebus, Shifter''s Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.48
      pick: 0.22
      fit: 0.45
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.64
      pick: 0.22
      fit: 0.45
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.44
      pick: 0.23
      fit: 0.44
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.84
    Hussar's Wings:
      total: 0.54
      efficiency: 0.39
      win: 0.73
      pick: 0.1
      fit: 0.47
    Erosion:
      total: 0.52
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Jotunn's Revenge
  - Hussar's Wings
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Void Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Shield of the Phoenix
  - Void Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Erosion, Kinetic Cuirass, Shield of the
    Phoenix, Void Shield, Stampede, Shifter''s Shield, Runeforged Hammer, Void Stone,
    Spectral Armor, Shield Splitter, Eye of the Storm, Doublet of Binding, Berserker''s
    Shield, Eye of Providence, Draconic Scale, Shogun''s Ofuda, Pharaoh''s Curse,
    Avenging Blade, Mystical Mail, Hydra''s Lament, Midgardian Mail, Sanguine Lash,
    Stone of Binding, Yogi''s Necklace, Phoenix Feather.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.44
      pick: 0.23
      fit: 0.39
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.71
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.74
    Void Shield:
      total: 0.51
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.83
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.54
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
  aspect: Aspect of Preservation
---

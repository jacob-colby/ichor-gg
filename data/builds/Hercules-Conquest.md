---
type: smite-build
god: Hercules
mode: Conquest
builds:
- source: community
  aspect: Aspect of Preservation
  aspect_pick_rate: 0.02
  aspect_win_rate: 0.0
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.22
    win_rate: 0.44
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.42
    - name: Runeforged Hammer
      pick_rate: 0.12
      win_rate: 0.58
  - name: Breastplate of Valor
    pick_rate: 0.17
    win_rate: 0.46
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.41
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.54
  - name: Genji's Guard
    pick_rate: 0.14
    win_rate: 0.55
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.38
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.23
  - name: Freya's Tears
    pick_rate: 0.13
    win_rate: 0.3
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.43
    - name: Hussar's Wings
      pick_rate: 0.06
      win_rate: 0.78
  - name: Brawler’s Beat Stick
    pick_rate: 0.07
    win_rate: 0.7
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.44
    - name: Genji's Guard
      pick_rate: 0.05
      win_rate: 0.43
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.5
    alternates:
    - name: Sage's Ring
      pick_rate: 0.07
      win_rate: 0.67
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.4
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.39
    win_rate: 0.6
  - name: Bumba's Cudgel
    pick_rate: 0.32
    win_rate: 0.34
  - name: Archmage's Gem
    pick_rate: 0.06
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/hercules/
  last_verified: '2026-10-27'
  god_win_rate: 0.46496815286624205
  god_matches_won: 73
  god_matches_played: 157
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-27'
  god_matches_analyzed: 7385
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Kinetic Cuirass
  - Runeforged Hammer
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Brawler’s Beat Stick
  - Kinetic Cuirass
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Runeforged Hammer, Kinetic Cuirass, Shield Splitter,
    Eye of the Storm, Erosion, Berserker''s Shield, Eye of Providence, Draconic Scale,
    Shield of the Phoenix, Hydra''s Lament, Stone of Binding, Shifter''s Shield, Magi''s
    Cloak, Avenging Blade, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle,
    Hide of the Nemean Lion, Heartseeker, Leviathan''s Hide, Void Shield, Stampede,
    Ancile, Prophetic Cloak, Oni Hunter''s Garb.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.53
      efficiency: 0.42
      win: 0.7
      pick: 0.15
      fit: 0.43
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.55
      pick: 0.22
      fit: 0.33
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.7
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.12
      fit: 0.51
    Hussar's Wings:
      total: 0.58
      efficiency: 0.39
      win: 0.78
      pick: 0.1
      fit: 0.6
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Runeforged Hammer
  - Hussar's Wings
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Shield of the Phoenix
  - Runeforged Hammer
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Brawler’s Beat Stick — magical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Runeforged Hammer, Shield of the Phoenix, Kinetic Cuirass,
    Shield Splitter, Eye of the Storm, Berserker''s Shield, Erosion, The Reaper, Eye
    of Providence, Draconic Scale, Hydra''s Lament, Yogi''s Necklace, Avenging Blade,
    Phoenix Feather, Chandra''s Grace, Shifter''s Shield, Glorious Pridwen, Stone
    of Binding, Midgardian Mail, Hide of the Nemean Lion, Daybreak Gavel, Magi''s
    Cloak, Leviathan''s Hide, Heartseeker, Void Shield.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.68
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.55
      pick: 0.22
      fit: 0.3
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.82
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.12
      fit: 0.57
    Hussar's Wings:
      total: 0.58
      efficiency: 0.39
      win: 0.78
      pick: 0.1
      fit: 0.58
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Genji's Guard
  - Runeforged Hammer
  - Hussar's Wings
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - Genji's Guard
  - Runeforged Hammer
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Brawler’s Beat Stick
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    for this god: Runeforged Hammer, Amanita Charm, Stone of Binding, Avenging Blade,
    Kinetic Cuirass, Screeching Gargoyle, Heartseeker, Void Shield, Shield Splitter,
    Void Stone, Titan''s Bane, Berserker''s Shield, The Crusher, Eye of the Storm,
    The Reaper, Erosion, Hydra''s Lament, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Magi''s Cloak, Pendulum Blade, Avatar''s Parashu, Shifter''s Shield,
    Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.52
      efficiency: 0.42
      win: 0.7
      pick: 0.15
      fit: 0.31
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.44
      pick: 0.22
      fit: 0.57
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.55
      pick: 0.22
      fit: 0.24
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.57
      win: 0.58
      pick: 0.12
      fit: 0.4
    Hussar's Wings:
      total: 0.56
      efficiency: 0.39
      win: 0.78
      pick: 0.1
      fit: 0.43
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - Genji's Guard
  - Runeforged Hammer
  - Hussar's Wings
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Tyrfing
  - Runeforged Hammer
  - Hussar's Wings
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
    swap: Brawler’s Beat Stick — physical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Runeforged Hammer, Amanita Charm, Kinetic Cuirass,
    Golden Blade, Tyrfing, Shield Splitter, Pharaoh''s Curse, Riptalon, Lernaean Bow,
    Shogun''s Ofuda, Silverbranch Bow, Erosion, Eye of Providence, Stone of Binding,
    Toxic Blade, Eye of the Storm, Shield of the Phoenix, Hydra''s Lament, Draconic
    Scale, Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, The Reaper, Tekko-Kagi,
    Shifter''s Shield.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.56
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.55
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
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.57
      win: 0.58
      pick: 0.12
      fit: 0.32
    Hussar's Wings:
      total: 0.55
      efficiency: 0.39
      win: 0.78
      pick: 0.1
      fit: 0.38
  community_ordered:
  - Genji's Guard
  - Runeforged Hammer
  - Hussar's Wings
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Brawler’s Beat Stick
  - Breastplate of Valor
  - Genji's Guard
  - Jotunn's Revenge
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Brawler’s Beat Stick
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Runeforged Hammer,
    Kinetic Cuirass, Shield of the Phoenix, Hydra''s Lament, Screeching Gargoyle,
    Shield Splitter, Berserker''s Shield, Prophetic Cloak, Erosion, Eye of Providence,
    Gladiator''s Shield, Draconic Scale, Stone of Binding, Eye of the Storm, Arondight,
    Magi''s Cloak, Eye of Erebus, Shifter''s Shield, Mantle Of Discord, Glorious Pridwen,
    Midgardian Mail, Daybreak Gavel, Chandra''s Grace, Hide of the Nemean Lion, Leviathan''s
    Hide.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.52
      efficiency: 0.42
      win: 0.7
      pick: 0.15
      fit: 0.32
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.46
      pick: 0.23
      fit: 0.48
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.55
      pick: 0.22
      fit: 0.48
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.44
      pick: 0.22
      fit: 0.46
    Hussar's Wings:
      total: 0.56
      efficiency: 0.39
      win: 0.78
      pick: 0.1
      fit: 0.45
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Brawler’s Beat Stick
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
      pick: 0.22
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
      total: 0.44
      efficiency: 0.61
      win: 0.3
      pick: 0.22
      fit: 0.54
    Shifter's Shield:
      total: 0.48
      efficiency: 0.55
      win: 0.42
      pick: 0.15
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
  - Genji's Guard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Brawler’s Beat Stick — magical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Runeforged Hammer, Erosion, Kinetic Cuirass, Shield of
    the Phoenix, Void Shield, Stampede, Void Stone, Spectral Armor, Shield Splitter,
    Eye of the Storm, Doublet of Binding, Berserker''s Shield, Eye of Providence,
    Draconic Scale, Shogun''s Ofuda, Pharaoh''s Curse, Avenging Blade, Mystical Mail,
    Shifter''s Shield, Hydra''s Lament, Midgardian Mail, Sanguine Lash, Stone of Binding,
    Yogi''s Necklace, Phoenix Feather.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.71
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.55
      pick: 0.22
      fit: 0.29
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.12
      fit: 0.58
    Hussar's Wings:
      total: 0.58
      efficiency: 0.39
      win: 0.78
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
  - Shield of the Phoenix
  - Genji's Guard
  - Runeforged Hammer
  - Hussar's Wings
  - Amanita Charm
  - Erosion
  flex_slots:
  - Shield of the Phoenix
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Brawler’s Beat Stick — physical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Runeforged Hammer, Erosion, Shield of the Phoenix, Kinetic
    Cuirass, Void Shield, Stampede, Shield Splitter, Void Stone, Spectral Armor, Eye
    of the Storm, Doublet of Binding, Berserker''s Shield, The Reaper, Eye of Providence,
    Draconic Scale, Hydra''s Lament, Yogi''s Necklace, Avenging Blade, Shogun''s Ofuda,
    Phoenix Feather, Pharaoh''s Curse, Chandra''s Grace, Mystical Mail, Sanguine Lash,
    Shifter''s Shield.'
  slot_scores:
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.82
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.55
      pick: 0.22
      fit: 0.3
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.12
      fit: 0.57
    Hussar's Wings:
      total: 0.58
      efficiency: 0.39
      win: 0.78
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
  - Runeforged Hammer
  - Hussar's Wings
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Runeforged Hammer
  - Void Shield
  - Void Stone
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Void Stone
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Void Shield, Void Stone, Runeforged Hammer, Erosion,
    Avenging Blade, Kinetic Cuirass, Stone of Binding, Shield of the Phoenix, The
    Reaper, Stampede, Screeching Gargoyle, Spectral Armor, Heartseeker, Doublet of
    Binding, Shield Splitter, Berserker''s Shield, Eye of the Storm, Titan''s Bane,
    The Crusher, Shogun''s Ofuda, Eye of Providence, Pharaoh''s Curse, Hydra''s Lament,
    Draconic Scale, Shifter''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.44
      pick: 0.22
      fit: 0.55
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.57
      win: 0.58
      pick: 0.12
      fit: 0.45
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
      total: 0.56
      efficiency: 0.39
      win: 0.78
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
  - Runeforged Hammer
  - Hussar's Wings
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Runeforged Hammer
  - Hussar's Wings
  - Amanita Charm
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Runeforged Hammer
  - Shogun's Ofuda
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Pharaoh''s Curse, Runeforged Hammer,
    Shogun''s Ofuda, Erosion, Riptalon, Kinetic Cuirass, Golden Blade, Shield of the
    Phoenix, Void Shield, Stampede, Void Stone, Spectral Armor, Doublet of Binding,
    Umbral Link, The Reaper, Tyrfing, Eros'' Bow, Shield Splitter, Sanguine Lash,
    Lernaean Bow, Toxic Blade, Eye of the Storm, Silverbranch Bow, Shifter''s Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.48
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.57
      win: 0.58
      pick: 0.12
      fit: 0.36
    Hussar's Wings:
      total: 0.55
      efficiency: 0.39
      win: 0.78
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
  - Runeforged Hammer
  - Hussar's Wings
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Shield of the Phoenix
  - Runeforged Hammer
  - Hussar's Wings
  - Erosion
  flex_slots:
  - Runeforged Hammer
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    Runeforged Hammer, Erosion, Kinetic Cuirass, Void Shield, Stampede, Void Stone,
    Spectral Armor, Hydra''s Lament, Chandra''s Grace, Doublet of Binding, Screeching
    Gargoyle, Berserker''s Shield, Glorious Pridwen, Gladiator''s Shield, Shield Splitter,
    Eye of Providence, Shogun''s Ofuda, Pharaoh''s Curse, Draconic Scale, Eye of the
    Storm, Mystical Mail, Prophetic Cloak, Eye of Erebus, Shifter''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.44
      pick: 0.22
      fit: 0.44
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.55
      pick: 0.22
      fit: 0.45
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.84
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.57
      win: 0.58
      pick: 0.12
      fit: 0.38
    Hussar's Wings:
      total: 0.56
      efficiency: 0.39
      win: 0.78
      pick: 0.1
      fit: 0.47
    Erosion:
      total: 0.52
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Jotunn's Revenge
  - Genji's Guard
  - Runeforged Hammer
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
      pick: 0.22
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

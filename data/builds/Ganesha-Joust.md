---
type: smite-build
god: Ganesha
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Draconic Scale
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.67
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.58
    Draconic Scale:
      total: 0.58
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.63
    Shifter's Shield:
      total: 0.56
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.79
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.91
    Erosion:
      total: 0.58
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: &id001
    base: Selflessness
    upgrade: Heroism
    pick_rate: 0.59
    win_rate: 0.4863
    matches: 119
    basis: community
    borrowed_from: Conquest
  relic: &id002
    name: Phantom Shell
    pick_rate: 0.55
    win_rate: 0.47
    matches: 111
    basis: community
    borrowed_from: Conquest
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  - Erosion
  flex_slots:
  - Draconic Scale
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Glorious Pridwen — physical protection
    swap_item: Glorious Pridwen
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.66
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.71
    Shield of the Phoenix:
      total: 0.72
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.86
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.52
    Draconic Scale:
      total: 0.57
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.61
    Amanita Charm:
      total: 0.81
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.94
    Erosion:
      total: 0.58
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.64
  starter: *id001
  relic: *id002
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Kinetic Cuirass
  - Void Shield
  - Void Stone
  - Soul Gem
  flex_slots:
  - Void Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Screeching Gargoyle:
      total: 0.59
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.66
    Stone of Binding:
      total: 0.61
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.72
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.55
    Void Shield:
      total: 0.59
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.72
    Void Stone:
      total: 0.59
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.72
    Soul Gem:
      total: 0.76
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.93
  starter: *id001
  relic: *id002
- source: suggested
  archetype: attack-speed
  slot_order:
  - Kinetic Cuirass
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Eros' Bow
  - Amanita Charm
  flex_slots:
  - Eros' Bow
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: Basic-attack DPS skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.46
    Nimble Ring:
      total: 0.43
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.3
    Bragi's Harp:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.47
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.33
    Eros' Bow:
      total: 0.44
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.66
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.64
  starter: *id001
  relic: *id002
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Gladiator's Shield
  - Freya's Tears
  - Lotus Sickle
  - Soul Gem
  flex_slots:
  - Gladiator's Shield
  - Lotus Sickle
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
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.52
    Gladiator's Shield:
      total: 0.55
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.67
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.6
    Lotus Sickle:
      total: 0.54
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.52
    Soul Gem:
      total: 0.73
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.87
  starter: *id001
  relic: *id002
- source: suggested
  archetype: strength
  slot_order:
  - Toxic Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: Off-type Strength build — this kit scales on it (efficiency + fit). Joust
    — math + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.54
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.62
    Berserker's Shield:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.48
    Shield Splitter:
      total: 0.53
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.48
    Amanita Charm:
      total: 0.67
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
  relic: *id002
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Shield Splitter
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.49
    Shield Splitter:
      total: 0.51
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.49
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.39
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.3
    Soul Gem:
      total: 0.71
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.83
  starter: *id001
  relic: *id002
- source: suggested
  archetype: model
  slot_order:
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Draconic Scale
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.67
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.58
    Draconic Scale:
      total: 0.58
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.63
    Shifter's Shield:
      total: 0.56
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.79
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.91
    Erosion:
      total: 0.58
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
  relic: *id002
---

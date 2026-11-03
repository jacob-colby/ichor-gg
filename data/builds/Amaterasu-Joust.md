---
type: smite-build
god: Amaterasu
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  - Erosion
  flex_slots:
  - Freya's Tears
  - Draconic Scale
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.67
    Shield Splitter:
      total: 0.6
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.55
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.53
    Draconic Scale:
      total: 0.53
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.78
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.92
    Erosion:
      total: 0.59
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.67
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield Splitter
  - Shield of the Phoenix
  - Runeforged Hammer
  - Amanita Charm
  - Erosion
  flex_slots:
  - Shield Splitter
  - Runeforged Hammer
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.65
    Shield Splitter:
      total: 0.57
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.66
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.81
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.53
    Amanita Charm:
      total: 0.8
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.95
    Erosion:
      total: 0.58
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Avenging Blade
  - Jotunn's Revenge
  - Void Shield
  - Void Stone
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Stone of Binding:
      total: 0.6
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.7
    Avenging Blade:
      total: 0.58
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.67
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.54
    Void Shield:
      total: 0.61
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.77
    Void Stone:
      total: 0.62
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.77
    Amanita Charm:
      total: 0.71
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.77
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Berserker's Shield
  - Riptalon
  - Amanita Charm
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: Basic-attack DPS skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.53
    Toxic Blade:
      total: 0.54
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.61
    Berserker's Shield:
      total: 0.58
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.43
    Riptalon:
      total: 0.56
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.67
    Amanita Charm:
      total: 0.68
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.71
    Pharaoh's Curse:
      total: 0.52
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.53
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Soul Gem
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
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.61
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.64
    Soul Gem:
      total: 0.72
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.91
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: Off-type Intelligence build — this kit scales on it (efficiency + fit).
    Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.49
    Spear of Desolation:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.46
    Obsidian Shard:
      total: 0.52
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.35
    Soul Gem:
      total: 0.72
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.91
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  - Erosion
  - Triton's Conch
  flex_slots:
  - Erosion
  - Triton's Conch
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Sphere of Negation — magical protection
    swap_item: Sphere of Negation
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
      total: 0.54
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.51
    Shield Splitter:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.71
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.76
    Erosion:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.51
    Triton's Conch:
      total: 0.51
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  - Erosion
  flex_slots:
  - Freya's Tears
  - Draconic Scale
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.67
    Shield Splitter:
      total: 0.6
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.55
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.53
    Draconic Scale:
      total: 0.53
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.78
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.92
    Erosion:
      total: 0.59
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.67
  starter: *id001
---

---
type: smite-build
god: Artio
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Brawler’s Beat Stick
  - Kinetic Cuirass
  - Magi's Cloak
  - Shield Splitter
  - Mantle Of Discord
  - Amanita Charm
  flex_slots:
  - Mantle Of Discord
  - Brawler’s Beat Stick
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
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.52
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.56
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.6
    Magi's Cloak:
      total: 0.54
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shield Splitter:
      total: 0.57
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.55
    Mantle Of Discord:
      total: 0.54
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.7
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.75
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Magi's Cloak
  - Shield Splitter
  - Shield of the Phoenix
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Magi's Cloak
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
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.6
    Magi's Cloak:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.51
    Shield Splitter:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.51
    Shield of the Phoenix:
      total: 0.63
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.75
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.49
    Amanita Charm:
      total: 0.73
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Avenging Blade
  - Jotunn's Revenge
  - Void Stone
  - Soul Gem
  flex_slots:
  - Screeching Gargoyle
  - Void Stone
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Screeching Gargoyle:
      total: 0.56
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.61
    Stone of Binding:
      total: 0.58
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.66
    Avenging Blade:
      total: 0.58
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.67
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.51
    Void Stone:
      total: 0.55
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.64
    Soul Gem:
      total: 0.7
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.83
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Berserker's Shield
  - Tyrfing
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Tyrfing
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
  rationale: Basic-attack DPS skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.59
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.65
    Toxic Blade:
      total: 0.58
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.69
    Berserker's Shield:
      total: 0.59
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.43
    Tyrfing:
      total: 0.52
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.54
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.6
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Lotus Sickle
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
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
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.44
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.43
    Freya's Tears:
      total: 0.58
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.58
    Lotus Sickle:
      total: 0.53
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.5
    Soul Gem:
      total: 0.72
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: Off-type Strength build — this kit scales on it (efficiency + fit). Arena
    — math + mode profile (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.56
    Toxic Blade:
      total: 0.54
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.53
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.43
    Shield Splitter:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Magi's Cloak
  - Shield Splitter
  - Mantle Of Discord
  - Soul Gem
  flex_slots:
  - Magi's Cloak
  - Mantle Of Discord
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
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.47
    Magi's Cloak:
      total: 0.5
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.46
    Shield Splitter:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.43
    Mantle Of Discord:
      total: 0.49
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.46
    Soul Gem:
      total: 0.69
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.81
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Brawler’s Beat Stick
  - Kinetic Cuirass
  - Magi's Cloak
  - Shield Splitter
  - Mantle Of Discord
  - Amanita Charm
  flex_slots:
  - Mantle Of Discord
  - Brawler’s Beat Stick
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
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.52
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.56
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.6
    Magi's Cloak:
      total: 0.54
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shield Splitter:
      total: 0.57
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.55
    Mantle Of Discord:
      total: 0.54
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.7
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.75
  starter: *id001
---

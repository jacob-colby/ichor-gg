---
type: smite-build
god: Geb
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Stygian Anchor
  - Kinetic Cuirass
  - Void Shield
  - Void Stone
  - Amanita Charm
  - Erosion
  flex_slots:
  - Void Stone
  - Void Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    Stygian Anchor:
      total: 0.57
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.69
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.65
    Void Shield:
      total: 0.56
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.65
    Void Stone:
      total: 0.56
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.65
    Amanita Charm:
      total: 0.83
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.63
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.75
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Bancroft's Talon
  - Genji's Guard
  - Rod of Tahuti
  - Eros' Bow
  - Erosion
  - Triton's Conch
  flex_slots:
  - Erosion
  - Genji's Guard
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
  rationale: mana-stack (efficiency + fit). Joust — math + mode profile (no meta win/pick
    data).
  slot_scores:
    Bancroft's Talon:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.5
    Genji's Guard:
      total: 0.46
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.23
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.29
    Eros' Bow:
      total: 0.55
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.57
    Erosion:
      total: 0.5
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.49
    Triton's Conch:
      total: 0.51
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Void Shield
  - Void Stone
  - Amanita Charm
  - Erosion
  flex_slots:
  - Void Stone
  - Void Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.63
    Shield of the Phoenix:
      total: 0.64
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.77
    Void Shield:
      total: 0.56
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.67
    Void Stone:
      total: 0.56
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.67
    Amanita Charm:
      total: 0.83
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.62
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Void Shield
  - Void Stone
  - Amanita Charm
  - Erosion
  flex_slots:
  - Screeching Gargoyle
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
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
      total: 0.56
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.61
    Stone of Binding:
      total: 0.59
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.68
    Void Shield:
      total: 0.66
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.85
    Void Stone:
      total: 0.66
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.85
    Amanita Charm:
      total: 0.75
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.84
    Erosion:
      total: 0.55
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Brawler’s Beat Stick
  - Nimble Ring
  - Bragi's Harp
  - Eros' Bow
  - Amanita Charm
  - Erosion
  flex_slots:
  - Nimble Ring
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Basic-attack DPS skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.53
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.58
    Nimble Ring:
      total: 0.41
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.28
    Bragi's Harp:
      total: 0.4
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.42
    Eros' Bow:
      total: 0.48
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.52
    Amanita Charm:
      total: 0.75
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.84
    Erosion:
      total: 0.55
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Freya's Tears
  - Eros' Bow
  - Erosion
  - Soul Gem
  flex_slots:
  - Erosion
  - Brawler’s Beat Stick
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.52
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.56
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.38
    Freya's Tears:
      total: 0.55
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.51
    Eros' Bow:
      total: 0.54
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.55
    Erosion:
      total: 0.53
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.56
    Soul Gem:
      total: 0.74
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.95
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Jotunn's Revenge
  - Shield Splitter
  - Amanita Charm
  - Erosion
  flex_slots:
  - Golden Blade
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: Off-type Strength build — this kit scales on it (efficiency + fit). Joust
    — math + mode profile (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.58
    Toxic Blade:
      total: 0.64
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.8
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.43
    Shield Splitter:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.75
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.86
    Erosion:
      total: 0.56
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.61
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Toxic Blade
  - Berserker's Shield
  - Eros' Bow
  - Pharaoh's Curse
  - Shogun's Ofuda
  - Soul Gem
  flex_slots:
  - Pharaoh's Curse
  - Shogun's Ofuda
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.64
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.79
    Berserker's Shield:
      total: 0.55
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.36
    Eros' Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.59
    Pharaoh's Curse:
      total: 0.54
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.56
    Shogun's Ofuda:
      total: 0.53
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.56
    Soul Gem:
      total: 0.75
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.93
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Stygian Anchor
  - Kinetic Cuirass
  - Void Shield
  - Void Stone
  - Amanita Charm
  - Erosion
  flex_slots:
  - Void Stone
  - Void Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    Stygian Anchor:
      total: 0.57
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.69
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.65
    Void Shield:
      total: 0.56
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.65
    Void Stone:
      total: 0.56
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.65
    Amanita Charm:
      total: 0.83
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.63
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.75
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Stygian Anchor
  - Kinetic Cuirass
  - Void Stone
  - Freya's Tears
  - Amanita Charm
  - Erosion
  flex_slots:
  - Void Stone
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: The model's core, corrected where the community is clearly right (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Stygian Anchor:
      total: 0.57
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.69
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.65
    Void Stone:
      total: 0.56
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.65
    Freya's Tears:
      total: 0.53
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.49
    Amanita Charm:
      total: 0.83
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.63
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.75
  swaps:
  - added: Freya's Tears
    removed: Void Shield
    reason: Conquest community 71% win over 126 matches (vs 61% on this god), taking
      the model's weakest slot from Void Shield
  borrowed_from: Conquest
  starter: *id001
---

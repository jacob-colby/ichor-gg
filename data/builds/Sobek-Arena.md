---
type: smite-build
god: Sobek
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Void Shield
  - Void Stone
  - Amanita Charm
  - Erosion
  - Stampede
  flex_slots:
  - Void Shield
  - Void Stone
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
    Kinetic Cuirass:
      total: 0.69
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.81
    Void Shield:
      total: 0.66
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.86
    Void Stone:
      total: 0.66
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.86
    Amanita Charm:
      total: 0.83
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.76
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 1.0
    Stampede:
      total: 0.68
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.86
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Void Shield
  - Amanita Charm
  - Rod of Asclepius
  - Erosion
  - Stampede
  flex_slots:
  - Kinetic Cuirass
  - Void Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.68
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.8
    Void Shield:
      total: 0.68
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.88
    Amanita Charm:
      total: 0.83
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Rod of Asclepius:
      total: 0.77
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.96
    Erosion:
      total: 0.75
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 1.0
    Stampede:
      total: 0.7
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Void Shield
  - Void Stone
  - Amanita Charm
  - Erosion
  - Stampede
  flex_slots:
  - Stone of Binding
  - Stampede
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Stone of Binding:
      total: 0.63
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.75
    Void Shield:
      total: 0.73
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 1.0
    Void Stone:
      total: 0.73
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
    Amanita Charm:
      total: 0.83
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.65
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.79
    Stampede:
      total: 0.61
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.72
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Amanita Charm
  - Erosion
  - Stampede
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Basic-attack DPS skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Bracer of The Abyss:
      total: 0.38
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.48
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.78
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.91
    Erosion:
      total: 0.59
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.66
    Stampede:
      total: 0.57
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Void Shield
  - Freya's Tears
  - Erosion
  - Stampede
  - Soul Gem
  flex_slots:
  - Void Shield
  - Genji's Guard
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.48
    Void Shield:
      total: 0.58
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.69
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.64
    Erosion:
      total: 0.63
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.75
    Stampede:
      total: 0.6
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.69
    Soul Gem:
      total: 0.76
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Kinetic Cuirass
  - Void Shield
  - Void Stone
  - Amanita Charm
  - Erosion
  - Stampede
  flex_slots:
  - Void Shield
  - Void Stone
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
    Kinetic Cuirass:
      total: 0.69
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.81
    Void Shield:
      total: 0.66
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.86
    Void Stone:
      total: 0.66
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.86
    Amanita Charm:
      total: 0.83
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.76
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 1.0
    Stampede:
      total: 0.68
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  - Amanita Charm
  - Erosion
  - Stampede
  flex_slots:
  - Freya's Tears
  - Shell of Rebuke
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: The model's core, corrected where the community is clearly right (efficiency
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.69
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.81
    Shell of Rebuke:
      total: 0.4
      efficiency: 0.28
      win: 0.5
      pick: 0.0
      fit: 0.51
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.64
    Amanita Charm:
      total: 0.83
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.76
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 1.0
    Stampede:
      total: 0.68
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.86
  swaps:
  - added: Freya's Tears
    removed: Void Stone
    reason: Conquest community 69% win over 69 matches (vs 56% on this god), taking
      the model's weakest slot from Void Stone
  - added: Shell of Rebuke
    removed: Void Shield
    reason: Conquest community 67% win over 96 matches (vs 56% on this god), taking
      the model's weakest slot from Void Shield
  borrowed_from: Conquest
  starter: *id001
---

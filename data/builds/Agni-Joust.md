---
type: smite-build
god: Agni
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Doom Orb
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Doom Orb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Sphere of Negation — magical protection
    swap_item: Sphere of Negation
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Spear of Desolation:
      total: 0.76
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Cosmic Horror:
      total: 0.69
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.79
    Doom Orb:
      total: 0.64
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.7
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.79
    Obsidian Shard:
      total: 0.67
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.79
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Obsidian Shard
  - Triton's Conch
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Ability / burst skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Spear of Desolation:
      total: 0.65
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.78
    The Cosmic Horror:
      total: 0.57
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.56
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.56
    Soul Gem:
      total: 0.79
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.54
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Void Shield
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Soul Gem
  flex_slots:
  - Spectral Armor
  - Void Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.61
    Void Shield:
      total: 0.56
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.65
    Spectral Armor:
      total: 0.57
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.82
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.61
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.71
    Soul Gem:
      total: 0.79
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Doom Orb
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Doom Orb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Gluttonous Grimoire:
      total: 0.81
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.95
    Spear of Desolation:
      total: 0.76
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Cosmic Horror:
      total: 0.72
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.85
    Doom Orb:
      total: 0.67
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.73
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.85
    Obsidian Shard:
      total: 0.7
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Divine Ruin
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Bracer of The Abyss
  - Triton's Conch
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Basic-attack DPS skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.5
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.57
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.48
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.53
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
    Soul Gem:
      total: 0.79
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.47
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Screeching Gargoyle:
      total: 0.54
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.58
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.48
    Chronos' Pendant:
      total: 0.59
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.69
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.86
    Soul Gem:
      total: 0.79
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Bragi's Harp
  - Death Metal
  - The Crusher
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Triton's Conch
  - Death Metal
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Off-type Strength build — this kit scales on it (efficiency + fit). Joust
    — math + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.65
    Bragi's Harp:
      total: 0.61
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.77
    Death Metal:
      total: 0.56
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.63
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.63
    Soul Gem:
      total: 0.79
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.6
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.75
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Spear of Desolation
  - The Crusher
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Spear of Desolation
  - Death Metal
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.68
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.69
    Death Metal:
      total: 0.59
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.61
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.69
    The Crusher:
      total: 0.64
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.66
    Soul Gem:
      total: 0.79
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.63
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.81
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Doom Orb
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Doom Orb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Sphere of Negation — magical protection
    swap_item: Sphere of Negation
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Spear of Desolation:
      total: 0.76
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Cosmic Horror:
      total: 0.69
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.79
    Doom Orb:
      total: 0.64
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.7
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.79
    Obsidian Shard:
      total: 0.67
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.79
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Divine Ruin
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Divine Ruin
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.59
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.76
    Spear of Desolation:
      total: 0.69
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.86
    The Cosmic Horror:
      total: 0.63
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.68
    Spear of the Magus:
      total: 0.64
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.68
    Obsidian Shard:
      total: 0.61
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.68
    Soul Gem:
      total: 0.79
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: burst
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Triton's Conch
  - Obsidian Shard
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Ability / burst skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Spear of Desolation:
      total: 0.62
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.71
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.51
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.51
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.51
    Soul Gem:
      total: 0.79
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.53
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.61
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Void Shield
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Soul Gem
  flex_slots:
  - Spectral Armor
  - Void Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.57
    Void Shield:
      total: 0.54
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.63
    Spectral Armor:
      total: 0.55
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.53
    Amanita Charm:
      total: 0.8
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.97
    Erosion:
      total: 0.59
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.67
    Soul Gem:
      total: 0.79
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Doom Orb
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Doom Orb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Spear of Desolation:
      total: 0.71
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.9
    The Cosmic Horror:
      total: 0.68
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.77
    Doom Orb:
      total: 0.63
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.77
    Spear of the Magus:
      total: 0.68
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.77
    Obsidian Shard:
      total: 0.65
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.77
    Soul Gem:
      total: 0.79
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: attack-speed
  slot_order:
  - Divine Ruin
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Bracer of The Abyss
  - Triton's Conch
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Basic-attack DPS skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.5
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.57
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.48
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.53
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
    Soul Gem:
      total: 0.79
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.47
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.49
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: cooldown
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Screeching Gargoyle
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Screeching Gargoyle:
      total: 0.51
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.44
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.44
    Chronos' Pendant:
      total: 0.57
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.57
    Spear of Desolation:
      total: 0.65
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.78
    Soul Gem:
      total: 0.79
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Bragi's Harp
  - Death Metal
  - The Crusher
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Triton's Conch
  - Death Metal
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Off-type Strength build — this kit scales on it (efficiency + fit). Joust
    — math + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.65
    Bragi's Harp:
      total: 0.61
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.77
    Death Metal:
      total: 0.56
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.63
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.63
    Soul Gem:
      total: 0.79
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.6
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.75
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Bragi's Harp
  - Spear of Desolation
  - The Crusher
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Bragi's Harp
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.63
    Bragi's Harp:
      total: 0.59
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.75
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.63
    The Crusher:
      total: 0.62
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.61
    Soul Gem:
      total: 0.79
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.6
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.75
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: model
  slot_order:
  - Divine Ruin
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Divine Ruin
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.59
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.76
    Spear of Desolation:
      total: 0.69
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.86
    The Cosmic Horror:
      total: 0.63
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.68
    Spear of the Magus:
      total: 0.64
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.68
    Obsidian Shard:
      total: 0.61
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.68
    Soul Gem:
      total: 0.79
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  aspect: Aspect of Combustion
---

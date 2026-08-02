---
type: smite-build
god: Chronos
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Divine Ruin
  - Bracer of The Abyss
  - Bragi's Harp
  - Spear of Desolation
  - Spear of the Magus
  - Soul Gem
  flex_slots:
  - Bracer of The Abyss
  - Spear of Desolation
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
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.49
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.64
    Bracer of The Abyss:
      total: 0.45
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.56
    Bragi's Harp:
      total: 0.5
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.66
    Spear of Desolation:
      total: 0.44
      efficiency: 0.32
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.46
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.44
    Soul Gem:
      total: 0.68
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Divine Ruin
  - Bragi's Harp
  - Spear of Desolation
  - Spear of the Magus
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Spear of the Magus
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Ability / burst skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.45
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.56
    Bragi's Harp:
      total: 0.48
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.62
    Spear of Desolation:
      total: 0.44
      efficiency: 0.32
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.44
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.4
    Soul Gem:
      total: 0.68
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.43
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.52
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Divine Ruin
  - Kinetic Cuirass
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Divine Ruin
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.45
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.55
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.49
    Spectral Armor:
      total: 0.48
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.67
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.89
    Erosion:
      total: 0.49
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.59
    Soul Gem:
      total: 0.68
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Divine Ruin
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
  - Divine Ruin
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.47
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.49
      efficiency: 0.32
      win: 0.5
      pick: 0.0
      fit: 0.66
    The Cosmic Horror:
      total: 0.48
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.57
    Spear of the Magus:
      total: 0.52
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.57
    Obsidian Shard:
      total: 0.49
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.57
    Soul Gem:
      total: 0.68
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Tyrfing
  - Rage
  - Bragi's Harp
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Bragi's Harp
  - Rage
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: For fun — deliberately fights this god's kit (Crit / attack-speed party
    build). Scored on gold-value + flavor fit only; not meta-checked.
  slot_scores:
    Tyrfing:
      total: 0.52
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.67
    Rage:
      total: 0.5
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.66
    Bragi's Harp:
      total: 0.51
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.67
    Death Metal:
      total: 0.54
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.53
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.61
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Divine Ruin
  - Bracer of The Abyss
  - Bragi's Harp
  - Spear of Desolation
  - Spear of the Magus
  - Soul Gem
  flex_slots:
  - Bracer of The Abyss
  - Spear of Desolation
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
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.49
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.64
    Bracer of The Abyss:
      total: 0.45
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.56
    Bragi's Harp:
      total: 0.5
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.66
    Spear of Desolation:
      total: 0.44
      efficiency: 0.32
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.46
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.44
    Soul Gem:
      total: 0.68
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Divine Ruin
  - Void Stone
  - Spectral Armor
  - Erosion
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Erosion
  - Triton's Conch
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.43
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.53
    Void Stone:
      total: 0.43
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.57
    Spectral Armor:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.38
    Erosion:
      total: 0.43
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.47
    Soul Gem:
      total: 0.68
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.42
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.51
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: burst
  slot_order:
  - Divine Ruin
  - Bragi's Harp
  - Spear of the Magus
  - Spectral Armor
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Spectral Armor
  - Spear of the Magus
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Ability / burst skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.44
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.54
    Bragi's Harp:
      total: 0.45
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.41
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.35
    Spectral Armor:
      total: 0.42
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.36
    Soul Gem:
      total: 0.68
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.49
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.64
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: bruiser
  slot_order:
  - Void Shield
  - Void Stone
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Soul Gem
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Void Shield:
      total: 0.48
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.67
    Void Stone:
      total: 0.48
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.67
    Spectral Armor:
      total: 0.53
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.72
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.99
    Erosion:
      total: 0.54
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.69
    Soul Gem:
      total: 0.68
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Void Shield
  - Void Stone
  - Spear of Desolation
  - Spear of the Magus
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - Spear of Desolation
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Screeching Gargoyle:
      total: 0.47
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.6
    Void Shield:
      total: 0.53
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.77
    Void Stone:
      total: 0.56
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.83
    Spear of Desolation:
      total: 0.44
      efficiency: 0.32
      win: 0.5
      pick: 0.0
      fit: 0.57
    Spear of the Magus:
      total: 0.45
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.43
    Soul Gem:
      total: 0.68
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: model
  slot_order:
  - Divine Ruin
  - Void Stone
  - Spectral Armor
  - Erosion
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Erosion
  - Triton's Conch
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.43
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.53
    Void Stone:
      total: 0.43
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.57
    Spectral Armor:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.38
    Erosion:
      total: 0.43
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.47
    Soul Gem:
      total: 0.68
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.42
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.51
  starter: *id001
  aspect: Aspect of Relativity
---

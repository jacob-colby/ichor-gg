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
  - Spear of Desolation
  - Spear of the Magus
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
      total: 0.55
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.64
    Bracer of The Abyss:
      total: 0.59
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.56
    Bragi's Harp:
      total: 0.59
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.66
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.53
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.44
    Soul Gem:
      total: 0.81
      efficiency: 0.62
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
  - Divine Ruin
  - Spear of the Magus
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
  rationale: Ability / burst skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.51
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.56
    Bragi's Harp:
      total: 0.58
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.62
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.51
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.4
    Soul Gem:
      total: 0.81
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.54
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.52
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
  - Kinetic Cuirass
  - Void Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
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
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.49
    Void Shield:
      total: 0.53
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.57
    Spectral Armor:
      total: 0.57
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.78
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.89
    Erosion:
      total: 0.57
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.59
    Soul Gem:
      total: 0.81
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Dreamer's Idol
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
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
      total: 0.59
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.66
    The Cosmic Horror:
      total: 0.58
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.57
    Spear of the Magus:
      total: 0.59
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.57
    Obsidian Shard:
      total: 0.56
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.57
    Dreamer's Idol:
      total: 0.55
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.57
    Soul Gem:
      total: 0.81
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Tyrfing
  - Bragi's Harp
  - Death Metal
  - Riptalon
  - Damaru
  - Demon Blade
  flex_slots:
  - Riptalon
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: For fun — deliberately fights this god's kit (Crit / attack-speed party
    build). Scored on gold-value + flavor fit only; not meta-checked.
  slot_scores:
    Tyrfing:
      total: 0.59
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.67
    Bragi's Harp:
      total: 0.6
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.67
    Death Metal:
      total: 0.65
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.66
    Riptalon:
      total: 0.6
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.59
    Damaru:
      total: 0.66
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.73
      efficiency: 0.45
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
  - Spear of Desolation
  - Spear of the Magus
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
      total: 0.55
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.64
    Bracer of The Abyss:
      total: 0.59
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.56
    Bragi's Harp:
      total: 0.59
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.66
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.53
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.44
    Soul Gem:
      total: 0.81
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Void Stone
  - Spectral Armor
  - Erosion
  - Soul Gem
  - Doublet of Binding
  - Triton's Conch
  flex_slots:
  - Void Stone
  - Erosion
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Void Stone:
      total: 0.51
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.57
    Spectral Armor:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.38
    Erosion:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.47
    Soul Gem:
      total: 0.81
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 1.0
    Doublet of Binding:
      total: 0.52
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.47
    Triton's Conch:
      total: 0.53
      efficiency: 0.56
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
  - Spear of Desolation
  - Spectral Armor
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Spear of Desolation
  - Divine Ruin
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
  rationale: Ability / burst skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.5
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.54
    Bragi's Harp:
      total: 0.55
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.51
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.49
    Spectral Armor:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.36
    Soul Gem:
      total: 0.81
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.6
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.64
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: bruiser
  slot_order:
  - Void Shield
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Soul Gem
  - Doublet of Binding
  flex_slots:
  - Void Shield
  - Doublet of Binding
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Void Shield:
      total: 0.58
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.67
    Spectral Armor:
      total: 0.62
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.84
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.99
    Erosion:
      total: 0.63
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.69
    Soul Gem:
      total: 0.81
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 1.0
    Doublet of Binding:
      total: 0.57
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.57
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
  - Spear of Desolation
  - Spear of the Magus
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
      total: 0.55
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.6
    Void Shield:
      total: 0.63
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.77
    Void Stone:
      total: 0.65
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.83
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.57
    Spear of the Magus:
      total: 0.53
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.43
    Soul Gem:
      total: 0.81
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: model
  slot_order:
  - Void Stone
  - Spectral Armor
  - Erosion
  - Soul Gem
  - Doublet of Binding
  - Triton's Conch
  flex_slots:
  - Void Stone
  - Erosion
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Void Stone:
      total: 0.51
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.57
    Spectral Armor:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.38
    Erosion:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.47
    Soul Gem:
      total: 0.81
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 1.0
    Doublet of Binding:
      total: 0.52
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.47
    Triton's Conch:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.51
  starter: *id001
  aspect: Aspect of Relativity
---

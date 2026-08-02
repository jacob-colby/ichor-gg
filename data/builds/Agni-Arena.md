---
type: smite-build
god: Agni
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Dreamer's Idol
  - Rod of Asclepius
  flex_slots:
  - The Cosmic Horror
  - Dreamer's Idol
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Spear of Desolation:
      total: 0.66
      efficiency: 0.32
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Cosmic Horror:
      total: 0.6
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.63
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.79
    Obsidian Shard:
      total: 0.6
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.79
    Dreamer's Idol:
      total: 0.59
      efficiency: 0.18
      win: 0.5
      pick: 0.0
      fit: 0.99
    Rod of Asclepius:
      total: 0.72
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.97
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Divine Ruin
  - Spear of Desolation
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Divine Ruin
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Ability / burst skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.48
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.62
    Spear of Desolation:
      total: 0.55
      efficiency: 0.32
      win: 0.5
      pick: 0.0
      fit: 0.78
    Spear of the Magus:
      total: 0.52
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.56
    Obsidian Shard:
      total: 0.48
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.56
    Soul Gem:
      total: 0.68
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.54
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.74
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Mystical Mail
  - Spectral Armor
  - Amanita Charm
  - Rod of Asclepius
  - Erosion
  - Stampede
  flex_slots:
  - Stampede
  - Mystical Mail
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Mystical Mail:
      total: 0.53
      efficiency: 0.3
      win: 0.5
      pick: 0.0
      fit: 0.75
    Spectral Armor:
      total: 0.57
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.65
    Amanita Charm:
      total: 0.72
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
    Rod of Asclepius:
      total: 0.73
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.6
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.81
    Stampede:
      total: 0.54
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.75
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Dreamer's Idol
  flex_slots:
  - The Cosmic Horror
  - Dreamer's Idol
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Gluttonous Grimoire:
      total: 0.72
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.95
    Spear of Desolation:
      total: 0.66
      efficiency: 0.32
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Cosmic Horror:
      total: 0.63
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.66
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.85
    Obsidian Shard:
      total: 0.63
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.85
    Dreamer's Idol:
      total: 0.59
      efficiency: 0.18
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Tyrfing
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Golden Blade
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    Golden Blade:
      total: 0.53
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.67
    Lernaean Bow:
      total: 0.57
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.77
    Tyrfing:
      total: 0.52
      efficiency: 0.37
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
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Dreamer's Idol
  - Rod of Asclepius
  flex_slots:
  - The Cosmic Horror
  - Dreamer's Idol
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Spear of Desolation:
      total: 0.66
      efficiency: 0.32
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Cosmic Horror:
      total: 0.6
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.63
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.79
    Obsidian Shard:
      total: 0.6
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.79
    Dreamer's Idol:
      total: 0.59
      efficiency: 0.18
      win: 0.5
      pick: 0.0
      fit: 0.99
    Rod of Asclepius:
      total: 0.72
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.97
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Divine Ruin
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Asclepius
  flex_slots:
  - Obsidian Shard
  - The Cosmic Horror
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
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.55
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.76
    Spear of Desolation:
      total: 0.59
      efficiency: 0.32
      win: 0.5
      pick: 0.0
      fit: 0.86
    The Cosmic Horror:
      total: 0.54
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.68
    Spear of the Magus:
      total: 0.58
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.68
    Obsidian Shard:
      total: 0.55
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.68
    Rod of Asclepius:
      total: 0.69
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.91
  starter: *id001
  aspect: Aspect of Combustion
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
  - Bragi's Harp
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
  rationale: Ability / burst skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.47
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.6
    Bragi's Harp:
      total: 0.47
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.52
      efficiency: 0.32
      win: 0.5
      pick: 0.0
      fit: 0.71
    Spear of the Magus:
      total: 0.49
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.51
    Soul Gem:
      total: 0.68
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.52
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: bruiser
  slot_order:
  - Mystical Mail
  - Spectral Armor
  - Amanita Charm
  - Rod of Asclepius
  - Erosion
  - Stampede
  flex_slots:
  - Stampede
  - Mystical Mail
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Mystical Mail:
      total: 0.51
      efficiency: 0.3
      win: 0.5
      pick: 0.0
      fit: 0.73
    Spectral Armor:
      total: 0.56
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.72
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
    Rod of Asclepius:
      total: 0.72
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.97
    Erosion:
      total: 0.58
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.77
    Stampede:
      total: 0.53
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: *id001
  aspect: Aspect of Combustion
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
  - The Cosmic Horror
  - Dreamer's Idol
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Spear of Desolation:
      total: 0.61
      efficiency: 0.32
      win: 0.5
      pick: 0.0
      fit: 0.9
    The Cosmic Horror:
      total: 0.58
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.77
    Spear of the Magus:
      total: 0.62
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.77
    Obsidian Shard:
      total: 0.59
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.77
    Dreamer's Idol:
      total: 0.58
      efficiency: 0.18
      win: 0.5
      pick: 0.0
      fit: 0.97
    Soul Gem:
      total: 0.68
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 1.0
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
  - Rod of Asclepius
  flex_slots:
  - Obsidian Shard
  - The Cosmic Horror
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
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.55
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.76
    Spear of Desolation:
      total: 0.59
      efficiency: 0.32
      win: 0.5
      pick: 0.0
      fit: 0.86
    The Cosmic Horror:
      total: 0.54
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.68
    Spear of the Magus:
      total: 0.58
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.68
    Obsidian Shard:
      total: 0.55
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.68
    Rod of Asclepius:
      total: 0.69
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.91
  starter: *id001
  aspect: Aspect of Combustion
---

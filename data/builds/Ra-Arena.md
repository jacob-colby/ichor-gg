---
type: smite-build
god: Ra
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Divine Ruin
  - Spear of Desolation
  - The Cosmic Horror
  - Doom Orb
  - Spear of the Magus
  - Rod of Asclepius
  flex_slots:
  - Spear of the Magus
  - Doom Orb
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
      total: 0.58
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.81
    Spear of Desolation:
      total: 0.71
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Cosmic Horror:
      total: 0.59
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.72
    Doom Orb:
      total: 0.56
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.72
    Spear of the Magus:
      total: 0.57
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.72
    Rod of Asclepius:
      total: 0.71
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.96
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Divine Ruin
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Spear of the Magus
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
      total: 0.6
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.78
    The Cosmic Horror:
      total: 0.51
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.49
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.56
    Soul Gem:
      total: 0.7
      efficiency: 0.41
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
  - Divine Ruin
  - Spear of Desolation
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Soul Gem
  flex_slots:
  - Spectral Armor
  - Spear of Desolation
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.47
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.6
    Spear of Desolation:
      total: 0.46
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.5
    Spectral Armor:
      total: 0.47
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.45
    Amanita Charm:
      total: 0.68
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.91
    Erosion:
      total: 0.5
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.61
    Soul Gem:
      total: 0.7
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Doom Orb
  - Spear of the Magus
  - The World Stone
  - Soul Gem
  flex_slots:
  - Doom Orb
  - The World Stone
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
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Spear of Desolation:
      total: 0.71
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Cosmic Horror:
      total: 0.64
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.81
    Doom Orb:
      total: 0.61
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.81
    Spear of the Magus:
      total: 0.62
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.81
    The World Stone:
      total: 0.59
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.7
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Death Metal
  - Damaru
  - Demon Blade
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Damaru
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
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.77
    Death Metal:
      total: 0.55
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.51
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.6
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 1.0
    Soul Gem:
      total: 0.53
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.65
  fun: true
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Divine Ruin
  - Spear of Desolation
  - The Cosmic Horror
  - Doom Orb
  - Spear of the Magus
  - Rod of Asclepius
  flex_slots:
  - Spear of the Magus
  - Doom Orb
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
      total: 0.58
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.81
    Spear of Desolation:
      total: 0.71
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Cosmic Horror:
      total: 0.59
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.72
    Doom Orb:
      total: 0.56
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.72
    Spear of the Magus:
      total: 0.57
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.72
    Rod of Asclepius:
      total: 0.71
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Void Stone
  - Spear of Desolation
  - Spectral Armor
  - Erosion
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Spectral Armor
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
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Void Stone:
      total: 0.52
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.75
    Spear of Desolation:
      total: 0.54
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.65
    Spectral Armor:
      total: 0.49
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.49
    Erosion:
      total: 0.52
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.65
    Soul Gem:
      total: 0.7
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.48
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.62
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: burst
  slot_order:
  - Divine Ruin
  - Spear of Desolation
  - The Cosmic Horror
  - Spectral Armor
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - The Cosmic Horror
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Ability / burst skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.46
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.58
    Spear of Desolation:
      total: 0.53
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.62
    The Cosmic Horror:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.45
    Spectral Armor:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.41
    Soul Gem:
      total: 0.7
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.55
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.76
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: bruiser
  slot_order:
  - Mystical Mail
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Stampede
  - Soul Gem
  flex_slots:
  - Stampede
  - Mystical Mail
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Mystical Mail:
      total: 0.49
      efficiency: 0.3
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
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.56
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.72
    Stampede:
      total: 0.5
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.67
    Soul Gem:
      total: 0.7
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Void Shield
  - Void Stone
  - Spear of Desolation
  - The Cosmic Horror
  - Soul Gem
  flex_slots:
  - Screeching Gargoyle
  - The Cosmic Horror
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Screeching Gargoyle:
      total: 0.52
      efficiency: 0.33
      win: 0.5
      pick: 0.0
      fit: 0.7
    Void Shield:
      total: 0.56
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.84
    Void Stone:
      total: 0.62
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.96
    Spear of Desolation:
      total: 0.59
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.74
    The Cosmic Horror:
      total: 0.51
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.56
    Soul Gem:
      total: 0.7
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: model
  slot_order:
  - Void Stone
  - Spear of Desolation
  - Spectral Armor
  - Erosion
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Spectral Armor
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
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Void Stone:
      total: 0.52
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.75
    Spear of Desolation:
      total: 0.54
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.65
    Spectral Armor:
      total: 0.49
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.49
    Erosion:
      total: 0.52
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.65
    Soul Gem:
      total: 0.7
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.48
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.62
  starter: *id001
  aspect: Aspect of Thermotherapy
---

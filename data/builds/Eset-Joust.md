---
type: smite-build
god: Eset
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Divine Ruin
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.58
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.81
    Gluttonous Grimoire:
      total: 0.68
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.87
    Spear of Desolation:
      total: 0.66
      efficiency: 0.32
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Cosmic Horror:
      total: 0.59
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
  rationale: Ability / burst skew (efficiency + fit). Joust — math + mode profile
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
      total: 0.49
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Soul Gem
  flex_slots:
  - Spectral Armor
  - Eye of Providence
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
    Eye of Providence:
      total: 0.49
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.5
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.6
    Spectral Armor:
      total: 0.52
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.72
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.54
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.7
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
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Doom Orb
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - The Cosmic Horror
  - Doom Orb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Gluttonous Grimoire:
      total: 0.72
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.94
    Spear of Desolation:
      total: 0.66
      efficiency: 0.32
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Cosmic Horror:
      total: 0.62
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.84
    Doom Orb:
      total: 0.57
      efficiency: 0.31
      win: 0.5
      pick: 0.0
      fit: 0.84
    Spear of the Magus:
      total: 0.66
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.84
    Obsidian Shard:
      total: 0.62
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.84
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
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.58
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.81
    Gluttonous Grimoire:
      total: 0.68
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.87
    Spear of Desolation:
      total: 0.66
      efficiency: 0.32
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Cosmic Horror:
      total: 0.59
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
  starter: *id001
---

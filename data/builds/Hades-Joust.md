---
type: smite-build
god: Hades
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Erosion
  - Soul Gem
  flex_slots:
  - Erosion
  - Kinetic Cuirass
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
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.5
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.6
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.47
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.57
    Erosion:
      total: 0.56
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.6
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Divine Ruin
  - Bancroft's Talon
  - Death Metal
  - Doom Orb
  - Rod of Tahuti
  - Triton's Conch
  flex_slots:
  - Death Metal
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: mana-stack (efficiency + fit). Joust — math + mode profile (no meta win/pick
    data).
  slot_scores:
    Divine Ruin:
      total: 0.52
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.61
    Bancroft's Talon:
      total: 0.52
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.54
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.42
    Doom Orb:
      total: 0.48
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.42
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.42
    Triton's Conch:
      total: 0.59
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Obsidian Shard
  - Spear of the Magus
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
      total: 0.57
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.4
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.4
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.5
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.54
      efficiency: 0.44
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.61
    Void Shield:
      total: 0.56
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.65
    Spectral Armor:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.83
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.61
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.71
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Void Shield
  - Void Stone
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of Desolation
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
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Void Shield:
      total: 0.65
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.83
    Void Stone:
      total: 0.64
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.83
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.68
    Rod of Tahuti:
      total: 0.72
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.58
    Obsidian Shard:
      total: 0.61
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.68
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Divine Ruin
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
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
  rationale: Basic-attack DPS skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.48
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.53
    Bracer of The Abyss:
      total: 0.42
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.32
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.38
    Bragi's Harp:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.52
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.25
    Soul Gem:
      total: 0.75
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.93
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Gladiator's Shield
  - Freya's Tears
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Gladiator's Shield
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
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
    Gladiator's Shield:
      total: 0.52
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.65
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.51
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.61
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - The Crusher
  - Rod of Tahuti
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Triton's Conch
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Off-type Strength build — this kit scales on it (efficiency + fit). Joust
    — math + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.61
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.75
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.47
    The Crusher:
      total: 0.53
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.32
    Soul Gem:
      total: 0.76
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.96
    Triton's Conch:
      total: 0.58
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Toxic Blade
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
    Toxic Blade:
      total: 0.58
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.71
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.39
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.6
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.75
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Erosion
  - Soul Gem
  flex_slots:
  - Erosion
  - Kinetic Cuirass
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
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.5
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.6
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.47
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.57
    Erosion:
      total: 0.56
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.6
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
---

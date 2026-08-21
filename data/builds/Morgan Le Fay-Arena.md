---
type: smite-build
god: Morgan Le Fay
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Doom Orb
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
      total: 0.79
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
    Doom Orb:
      total: 0.66
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.82
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.79
    Obsidian Shard:
      total: 0.72
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.89
    Dreamer's Idol:
      total: 0.75
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.99
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
  - Bancroft's Talon
  - Death Metal
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Triton's Conch
  flex_slots:
  - Bancroft's Talon
  - Doom Orb
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
  rationale: mana-stack (efficiency + fit). Arena — math + mode profile (no meta win/pick
    data).
  slot_scores:
    Bancroft's Talon:
      total: 0.57
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.64
    Death Metal:
      total: 0.59
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.57
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.61
    Doom Orb:
      total: 0.55
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.57
    Triton's Conch:
      total: 0.66
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.87
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Obsidian Shard
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Ability / burst skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Spear of Desolation:
      total: 0.68
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.78
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.56
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.66
    Dreamer's Idol:
      total: 0.63
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.76
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.59
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.74
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spectral Armor
  - Amanita Charm
  - Rod of Asclepius
  - Erosion
  - Stampede
  flex_slots:
  - Spectral Armor
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
      total: 0.6
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.61
    Spectral Armor:
      total: 0.61
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.65
    Amanita Charm:
      total: 0.83
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Rod of Asclepius:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.66
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.81
    Stampede:
      total: 0.63
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.75
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - The Cosmic Horror
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
      total: 0.79
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Cosmic Horror:
      total: 0.69
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.73
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.85
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.85
    Obsidian Shard:
      total: 0.75
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.95
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
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Triton's Conch
  - Bracer of The Abyss
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
  rationale: Basic-attack DPS skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.57
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.54
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.32
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.52
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
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
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Chronos' Pendant:
      total: 0.59
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.71
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.86
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.37
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
  - Golden Blade
  - Toxic Blade
  - Jotunn's Revenge
  - Rod of Tahuti
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Toxic Blade
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Off-type Strength build — this kit scales on it (efficiency + fit). Arena
    — math + mode profile (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.61
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.69
    Toxic Blade:
      total: 0.62
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.79
    Jotunn's Revenge:
      total: 0.68
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.65
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.44
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.64
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Spear of Desolation
  - Rod of Tahuti
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
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.71
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.69
    Death Metal:
      total: 0.61
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.56
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.68
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.91
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Doom Orb
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
      total: 0.79
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
    Doom Orb:
      total: 0.66
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.82
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.79
    Obsidian Shard:
      total: 0.72
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.89
    Dreamer's Idol:
      total: 0.75
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.99
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Void Stone
  - Rod of Tahuti
  - Rod of Asclepius
  - Erosion
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Triton's Conch
  - Erosion
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
      total: 0.62
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.78
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.47
    Rod of Asclepius:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.99
    Erosion:
      total: 0.6
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.68
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.62
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.79
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: mana-stack
  slot_order:
  - Bancroft's Talon
  - Void Stone
  - Rod of Tahuti
  - Wish-Granting Pearl
  - Stampede
  - Triton's Conch
  flex_slots:
  - Bancroft's Talon
  - Wish-Granting Pearl
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
  rationale: mana-stack (efficiency + fit). Arena — math + mode profile (no meta win/pick
    data).
  slot_scores:
    Bancroft's Talon:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.5
    Void Stone:
      total: 0.54
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.62
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.44
    Wish-Granting Pearl:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.46
    Stampede:
      total: 0.53
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.56
    Triton's Conch:
      total: 0.67
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.9
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: burst
  slot_order:
  - Void Stone
  - Spear of Desolation
  - Rod of Tahuti
  - Stampede
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Void Stone
  - Stampede
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
  rationale: Ability / burst skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Void Stone:
      total: 0.55
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.64
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.42
    Stampede:
      total: 0.54
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.57
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.62
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.81
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Stampede
  - Soul Gem
  flex_slots:
  - Spectral Armor
  - Kinetic Cuirass
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
      total: 0.62
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.63
    Spectral Armor:
      total: 0.62
      efficiency: 0.57
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
      total: 0.67
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.83
    Stampede:
      total: 0.64
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.77
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: anti-tank
  slot_order:
  - Void Shield
  - Void Stone
  - Spear of Desolation
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Dreamer's Idol
  - Spear of Desolation
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
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Void Shield:
      total: 0.69
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.91
    Void Stone:
      total: 0.73
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
    Spear of Desolation:
      total: 0.64
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.7
    Rod of Tahuti:
      total: 0.72
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.59
    Dreamer's Idol:
      total: 0.65
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Soul Gem
  - Triton's Conch
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
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Basic-attack DPS skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Bracer of The Abyss:
      total: 0.41
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.31
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.37
    Bragi's Harp:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.23
    Soul Gem:
      total: 0.77
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.97
    Triton's Conch:
      total: 0.54
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.65
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Void Stone
  - Spear of Desolation
  - Stampede
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Stampede
  - Genji's Guard
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
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.43
    Void Stone:
      total: 0.55
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.65
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.64
    Stampede:
      total: 0.55
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.58
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.57
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.7
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: strength
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Jotunn's Revenge
  - Pharaoh's Curse
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Jotunn's Revenge
  - Pharaoh's Curse
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Off-type Strength build — this kit scales on it (efficiency + fit). Arena
    — math + mode profile (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.63
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.75
    Toxic Blade:
      total: 0.66
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.86
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.52
    Pharaoh's Curse:
      total: 0.6
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.64
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.65
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.87
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: str-int
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Jotunn's Revenge
  - Rod of Tahuti
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Jotunn's Revenge
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stampede — physical protection
    swap_item: Stampede
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.58
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.64
    Toxic Blade:
      total: 0.63
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.8
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.41
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.69
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.94
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: model
  slot_order:
  - Void Stone
  - Rod of Tahuti
  - Rod of Asclepius
  - Erosion
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Triton's Conch
  - Erosion
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
      total: 0.62
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.78
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.47
    Rod of Asclepius:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.99
    Erosion:
      total: 0.6
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.68
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.62
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.79
  starter: *id001
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: hybrid
  slot_order:
  - Void Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Rod of Asclepius
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Triton's Conch
  - Obsidian Shard
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
  rationale: The model's core, corrected where the community is clearly right (efficiency
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Void Stone:
      total: 0.62
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.78
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
    Rod of Asclepius:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.99
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.62
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.79
  swaps:
  - added: Obsidian Shard
    removed: Erosion
    reason: Conquest community 64% win over 129 matches (vs 54% on this god), taking
      the model's weakest slot from Erosion
  borrowed_from: Conquest
  starter: *id001
  aspect: Aspect of the Cursed Crown
---

---
type: smite-build
god: Chronos
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Bracer of The Abyss
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Bracer of The Abyss
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
  - vs_tag: magic_heavy
    swap: Sphere of Negation — magical protection
    swap_item: Sphere of Negation
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Bracer of The Abyss:
      total: 0.54
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.58
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.56
    Obsidian Shard:
      total: 0.54
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.54
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.44
    Dreamer's Idol:
      total: 0.59
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.64
    Soul Gem:
      total: 0.79
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: &id001
    base: Sands Of Time
    upgrade: Pendulum of the Ages
    pick_rate: 0.7
    win_rate: 0.537
    matches: 134
    basis: community
    borrowed_from: Conquest
  relic: &id002
    name: Purification Beads
    pick_rate: 0.57
    win_rate: 0.52
    matches: 109
    basis: community
    borrowed_from: Conquest
- source: suggested
  archetype: mana-stack
  slot_order:
  - Bancroft's Talon
  - Book of Thoth
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  - Dreamer's Idol
  flex_slots:
  - Spear of Desolation
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
  - vs_tag: magic_heavy
    swap: Sphere of Negation — magical protection
    swap_item: Sphere of Negation
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
      total: 0.57
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.61
    Book of Thoth:
      total: 0.38
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.28
    Bragi's Harp:
      total: 0.59
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.71
    Spear of Desolation:
      total: 0.53
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.42
    Dreamer's Idol:
      total: 0.54
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.54
  starter: *id001
  relic: *id002
- source: suggested
  archetype: burst
  slot_order:
  - Bragi's Harp
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Bragi's Harp
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Talisman of Purification — CC-immunity / cleanse
    swap_item: Talisman of Purification
  - vs_tag: magic_heavy
    swap: Sphere of Negation — magical protection
    swap_item: Sphere of Negation
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Ability / burst skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Bragi's Harp:
      total: 0.55
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.62
    Spear of Desolation:
      total: 0.58
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.56
    Obsidian Shard:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.4
    Dreamer's Idol:
      total: 0.57
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.6
    Soul Gem:
      total: 0.78
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.98
  starter: *id001
  relic: *id002
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Magi's Cloak
  - Mantle Of Discord
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Magi's Cloak
  - Mantle Of Discord
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
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
      total: 0.55
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.49
    Magi's Cloak:
      total: 0.48
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.44
    Mantle Of Discord:
      total: 0.48
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.27
    Amanita Charm:
      total: 0.68
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.69
    Soul Gem:
      total: 0.7
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.82
  starter: *id001
  relic: *id002
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Obsidian Shard
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Doom Orb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Spear of Desolation:
      total: 0.63
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.66
    Doom Orb:
      total: 0.54
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.57
    Obsidian Shard:
      total: 0.6
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.67
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.57
    Dreamer's Idol:
      total: 0.65
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.77
    Soul Gem:
      total: 0.79
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  relic: *id002
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Sphere of Negation — magical protection
    swap_item: Sphere of Negation
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Basic-attack DPS skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.41
    Nimble Ring:
      total: 0.53
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.49
    Bragi's Harp:
      total: 0.56
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.64
    Spear of Desolation:
      total: 0.49
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.38
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.3
    Soul Gem:
      total: 0.7
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.81
  starter: *id001
  relic: *id002
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Bragi's Harp
  - Heartwood Charm
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Bragi's Harp
  - Heartwood Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Chronos' Pendant:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.45
    Bragi's Harp:
      total: 0.5
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.53
    Heartwood Charm:
      total: 0.48
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.45
    Spear of Desolation:
      total: 0.6
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.24
    Soul Gem:
      total: 0.79
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  relic: *id002
- source: suggested
  archetype: strength
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Bragi's Harp
  - Soul Gem
  flex_slots:
  - Golden Blade
  - Toxic Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Off-type Strength build — this kit scales on it (efficiency + fit). Arena
    — math + mode profile (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.69
    Toxic Blade:
      total: 0.57
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.7
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.59
    Tyrfing:
      total: 0.61
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.69
    Bragi's Harp:
      total: 0.59
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.71
    Soul Gem:
      total: 0.76
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.94
  starter: *id001
  relic: *id002
- source: suggested
  archetype: str-int
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Bragi's Harp
  - Soul Gem
  flex_slots:
  - Golden Blade
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Sphere of Negation — magical protection
    swap_item: Sphere of Negation
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.7
    Toxic Blade:
      total: 0.6
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.77
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.47
    Tyrfing:
      total: 0.62
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.7
    Bragi's Harp:
      total: 0.61
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.75
    Soul Gem:
      total: 0.75
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.91
  starter: *id001
  relic: *id002
- source: suggested
  archetype: model
  slot_order:
  - Bracer of The Abyss
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Bracer of The Abyss
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
  - vs_tag: magic_heavy
    swap: Sphere of Negation — magical protection
    swap_item: Sphere of Negation
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Bracer of The Abyss:
      total: 0.54
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.58
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.56
    Obsidian Shard:
      total: 0.54
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.54
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.44
    Dreamer's Idol:
      total: 0.59
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.64
    Soul Gem:
      total: 0.79
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  relic: *id002
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Lotus Sickle
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Book of Thoth
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
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Book of Thoth:
      total: 0.3
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.12
    Spear of Desolation:
      total: 0.53
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.29
    Lotus Sickle:
      total: 0.63
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.69
    Eros' Bow:
      total: 0.64
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.78
    Soul Gem:
      total: 0.79
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  relic: *id002
  aspect: Aspect of Relativity
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Rod of Tahuti
  - Lotus Sickle
  - Eros' Bow
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Triton's Conch
  - Book of Thoth
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
    Book of Thoth:
      total: 0.37
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.25
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.37
    Lotus Sickle:
      total: 0.66
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.75
    Eros' Bow:
      total: 0.61
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.71
    Soul Gem:
      total: 0.79
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.59
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: *id001
  relic: *id002
  aspect: Aspect of Relativity
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Lotus Sickle
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Book of Thoth
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
  rationale: Ability / burst skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Book of Thoth:
      total: 0.31
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.14
    Spear of Desolation:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.35
    Lotus Sickle:
      total: 0.63
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.68
    Eros' Bow:
      total: 0.59
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.68
    Soul Gem:
      total: 0.79
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  relic: *id002
  aspect: Aspect of Relativity
- source: suggested
  archetype: bruiser
  slot_order:
  - Lotus Sickle
  - Eros' Bow
  - Amanita Charm
  - Erosion
  - Stampede
  - Soul Gem
  flex_slots:
  - Stampede
  - Lotus Sickle
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
    Lotus Sickle:
      total: 0.59
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.61
    Eros' Bow:
      total: 0.62
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.74
    Amanita Charm:
      total: 0.84
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.99
    Erosion:
      total: 0.6
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.69
    Stampede:
      total: 0.59
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.67
    Soul Gem:
      total: 0.79
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  relic: *id002
  aspect: Aspect of Relativity
- source: suggested
  archetype: anti-tank
  slot_order:
  - Void Stone
  - Spear of Desolation
  - Rod of Tahuti
  - Lotus Sickle
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Eros' Bow
  - Spear of Desolation
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
    Void Stone:
      total: 0.65
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.83
    Spear of Desolation:
      total: 0.59
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.43
    Lotus Sickle:
      total: 0.6
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.63
    Eros' Bow:
      total: 0.59
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.68
    Soul Gem:
      total: 0.79
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  relic: *id002
  aspect: Aspect of Relativity
- source: suggested
  archetype: attack-speed
  slot_order:
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Lotus Sickle
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
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
    Nimble Ring:
      total: 0.47
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.38
    Bragi's Harp:
      total: 0.5
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.53
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.21
    Lotus Sickle:
      total: 0.59
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.61
    Eros' Bow:
      total: 0.59
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.67
    Soul Gem:
      total: 0.79
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  relic: *id002
  aspect: Aspect of Relativity
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  - Lotus Sickle
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Rod of Tahuti
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
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.36
    Spear of Desolation:
      total: 0.56
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.52
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.21
    Lotus Sickle:
      total: 0.68
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.79
    Eros' Bow:
      total: 0.58
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.65
    Soul Gem:
      total: 0.79
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  relic: *id002
  aspect: Aspect of Relativity
- source: suggested
  archetype: strength
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Tyrfing
  - Lotus Sickle
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Triton's Conch
  - Tyrfing
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Off-type Strength build — this kit scales on it (efficiency + fit). Arena
    — math + mode profile (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.6
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.69
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.57
    Tyrfing:
      total: 0.58
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.62
    Lotus Sickle:
      total: 0.61
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.64
    Soul Gem:
      total: 0.79
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.59
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: *id001
  relic: *id002
  aspect: Aspect of Relativity
- source: suggested
  archetype: str-int
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Rod of Tahuti
  - Lotus Sickle
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Golden Blade
  - Rod of Tahuti
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
  rationale: Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.58
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.66
    Toxic Blade:
      total: 0.6
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.74
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.32
    Lotus Sickle:
      total: 0.63
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.69
    Eros' Bow:
      total: 0.62
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.73
    Soul Gem:
      total: 0.79
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  relic: *id002
  aspect: Aspect of Relativity
- source: suggested
  archetype: model
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Lotus Sickle
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Book of Thoth
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
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Book of Thoth:
      total: 0.3
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.12
    Spear of Desolation:
      total: 0.53
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.29
    Lotus Sickle:
      total: 0.63
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.69
    Eros' Bow:
      total: 0.64
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.78
    Soul Gem:
      total: 0.79
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  relic: *id002
  aspect: Aspect of Relativity
---

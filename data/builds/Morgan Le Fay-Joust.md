---
type: smite-build
god: Morgan Le Fay
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - Doom Orb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Sphere of Negation — magical protection
    swap_item: Sphere of Negation
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Spear of Desolation:
      total: 0.8
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 1.0
    Doom Orb:
      total: 0.65
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.67
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.79
    Obsidian Shard:
      total: 0.71
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.89
    Rod of Tahuti:
      total: 0.8
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.77
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: &id001
    base: Bluestone Pendant
    upgrade: Bluestone Brooch
    pick_rate: 0.55
    win_rate: 0.51
    matches: 158
    basis: community
    borrowed_from: Conquest
  relic: &id002
    name: Aegis of Acceleration
    pick_rate: 0.33
    win_rate: 0.52
    matches: 95
    basis: community
    borrowed_from: Conquest
- source: suggested
  archetype: mana-stack
  slot_order:
  - Bancroft's Talon
  - Book of Thoth
  - Death Metal
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Bancroft's Talon
  - Book of Thoth
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
  rationale: mana-stack (efficiency + fit). Joust — math + mode profile (no meta win/pick
    data).
  slot_scores:
    Bancroft's Talon:
      total: 0.55
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.64
    Book of Thoth:
      total: 0.43
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.57
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.57
    Bragi's Harp:
      total: 0.56
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.67
    Spear of Desolation:
      total: 0.61
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.61
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
  relic: *id002
- source: suggested
  archetype: burst
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - Doom Orb
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
  rationale: Ability / burst skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Spear of Desolation:
      total: 0.69
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.78
    Doom Orb:
      total: 0.53
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.56
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.56
    Obsidian Shard:
      total: 0.59
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.56
    Soul Gem:
      total: 0.77
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  relic: *id002
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  - Erosion
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Erosion
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
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.39
    Amanita Charm:
      total: 0.76
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.84
    Erosion:
      total: 0.52
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.54
    Soul Gem:
      total: 0.73
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.92
  starter: *id001
  relic: *id002
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - Doom Orb
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Spear of Desolation:
      total: 0.8
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 1.0
    Doom Orb:
      total: 0.68
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.71
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.85
    Obsidian Shard:
      total: 0.74
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.95
    Rod of Tahuti:
      total: 0.83
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.85
    Soul Gem:
      total: 0.77
      efficiency: 0.53
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
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Basic-attack DPS skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.52
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.55
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.4
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.32
    Soul Gem:
      total: 0.72
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.86
  starter: *id001
  relic: *id002
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Heartwood Charm
  - Spear of Desolation
  - Totem of Death
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Totem of Death
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
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Chronos' Pendant:
      total: 0.6
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.63
    Heartwood Charm:
      total: 0.57
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.73
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.86
    Totem of Death:
      total: 0.57
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.73
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.37
    Soul Gem:
      total: 0.77
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  relic: *id002
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Bragi's Harp
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Tyrfing
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
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
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.65
    Tyrfing:
      total: 0.61
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.69
    Bragi's Harp:
      total: 0.62
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.77
    Heartseeker:
      total: 0.59
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.73
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.44
    Soul Gem:
      total: 0.73
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.93
  starter: *id001
  relic: *id002
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Obsidian Shard
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Heartseeker
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Sphere of Negation — magical protection
    swap_item: Sphere of Negation
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.69
    Spear of Desolation:
      total: 0.65
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.69
    Obsidian Shard:
      total: 0.6
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.66
    Heartseeker:
      total: 0.61
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.76
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.56
    Soul Gem:
      total: 0.77
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  relic: *id002
- source: suggested
  archetype: model
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - Doom Orb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Sphere of Negation — magical protection
    swap_item: Sphere of Negation
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Spear of Desolation:
      total: 0.8
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 1.0
    Doom Orb:
      total: 0.65
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.67
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.79
    Obsidian Shard:
      total: 0.71
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.89
    Rod of Tahuti:
      total: 0.8
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.77
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  relic: *id002
- source: suggested
  archetype: core
  slot_order:
  - Gluttonous Grimoire
  - Spear of Desolation
  - Jade Scepter
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Jade Scepter
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
    Gluttonous Grimoire:
      total: 0.68
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.85
    Spear of Desolation:
      total: 0.61
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.62
    Jade Scepter:
      total: 0.51
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.49
    Obsidian Shard:
      total: 0.55
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.47
    Soul Gem:
      total: 0.74
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.95
  starter: *id001
  relic: *id002
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Chandra's Grace
  - Death Metal
  - Spear of Desolation
  - Rod of Tahuti
  - Triton's Conch
  flex_slots:
  - Death Metal
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
  rationale: mana-stack (efficiency + fit). Joust — math + mode profile (no meta win/pick
    data).
  slot_scores:
    Book of Thoth:
      total: 0.39
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.3
    Chandra's Grace:
      total: 0.52
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.55
    Death Metal:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.54
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.44
    Triton's Conch:
      total: 0.54
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: *id001
  relic: *id002
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: burst
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Triton's Conch
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
      total: 0.6
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.59
    Spear of the Magus:
      total: 0.49
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.42
    Obsidian Shard:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.52
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.42
    Soul Gem:
      total: 0.73
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.92
    Triton's Conch:
      total: 0.5
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.54
  starter: *id001
  relic: *id002
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  - Erosion
  - Soul Gem
  flex_slots:
  - Erosion
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
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
      total: 0.62
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.54
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.36
    Amanita Charm:
      total: 0.77
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.86
    Erosion:
      total: 0.54
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.56
    Soul Gem:
      total: 0.71
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.9
  starter: *id001
  relic: *id002
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: anti-tank
  slot_order:
  - Void Stone
  - Spear of Desolation
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Void Stone
  - Spear of the Magus
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Void Stone:
      total: 0.6
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.73
    Spear of Desolation:
      total: 0.65
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.7
    Spear of the Magus:
      total: 0.58
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.59
    Obsidian Shard:
      total: 0.61
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.59
    Soul Gem:
      total: 0.77
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  relic: *id002
  aspect: Aspect of the Cursed Crown
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
    Bracer of The Abyss:
      total: 0.42
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.31
    Nimble Ring:
      total: 0.47
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.37
    Bragi's Harp:
      total: 0.49
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.51
    Spear of Desolation:
      total: 0.45
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.3
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.23
    Soul Gem:
      total: 0.64
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.7
  starter: *id001
  relic: *id002
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: cooldown
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Screeching Gargoyle
  - Chronos' Pendant
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
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Screeching Gargoyle:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.53
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.43
    Chronos' Pendant:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.47
    Spear of Desolation:
      total: 0.62
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.64
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.28
    Soul Gem:
      total: 0.75
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.97
  starter: *id001
  relic: *id002
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: strength
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Runeforged Hammer
  - Soul Gem
  flex_slots:
  - Tyrfing
  - Runeforged Hammer
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Off-type Strength build — this kit scales on it (efficiency + fit). Joust
    — math + mode profile (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.58
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.65
    Toxic Blade:
      total: 0.62
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.78
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.52
    Tyrfing:
      total: 0.56
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.58
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.53
    Soul Gem:
      total: 0.63
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: *id001
  relic: *id002
  aspect: Aspect of the Cursed Crown
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
  - Triton's Conch
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
      total: 0.56
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.72
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.51
    Spear of Desolation:
      total: 0.56
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.41
    Soul Gem:
      total: 0.69
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.84
    Triton's Conch:
      total: 0.56
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.67
  starter: *id001
  relic: *id002
  aspect: Aspect of the Cursed Crown
- source: suggested
  archetype: model
  slot_order:
  - Gluttonous Grimoire
  - Spear of Desolation
  - Jade Scepter
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Jade Scepter
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
    Gluttonous Grimoire:
      total: 0.68
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.85
    Spear of Desolation:
      total: 0.61
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.62
    Jade Scepter:
      total: 0.51
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.49
    Obsidian Shard:
      total: 0.55
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.47
    Soul Gem:
      total: 0.74
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.95
  starter: *id001
  relic: *id002
  aspect: Aspect of the Cursed Crown
---

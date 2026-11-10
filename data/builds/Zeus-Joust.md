---
type: smite-build
god: Zeus
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Bracer of The Abyss
  - Spear of Desolation
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of the Magus
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
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Bracer of The Abyss:
      total: 0.52
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.51
    Spear of Desolation:
      total: 0.62
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.63
    Spear of the Magus:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.5
    Obsidian Shard:
      total: 0.57
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.6
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.5
    Soul Gem:
      total: 0.79
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
    pick_rate: 0.34
    win_rate: 0.5306
    matches: 109
    basis: community
    borrowed_from: Conquest
  relic: &id002
    name: Aegis of Acceleration
    pick_rate: 0.5
    win_rate: 0.63
    matches: 160
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
  - Death Metal
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
      total: 0.57
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.62
    Book of Thoth:
      total: 0.39
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.3
    Death Metal:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.44
    Bragi's Harp:
      total: 0.58
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.69
    Spear of Desolation:
      total: 0.54
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.44
  starter: *id001
  relic: *id002
- source: suggested
  archetype: burst
  slot_order:
  - Bragi's Harp
  - Spear of Desolation
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
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
    Bragi's Harp:
      total: 0.54
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.6
    Spear of Desolation:
      total: 0.59
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.58
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
      total: 0.79
      efficiency: 0.58
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.49
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
    Amanita Charm:
      total: 0.7
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.72
    Erosion:
      total: 0.47
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.42
    Soul Gem:
      total: 0.74
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.89
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
      total: 0.65
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.71
    Doom Orb:
      total: 0.56
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.6
    Spear of the Magus:
      total: 0.58
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.6
    Obsidian Shard:
      total: 0.62
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.7
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.6
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
  - Bragi's Harp
  - Heartwood Charm
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Heartwood Charm
  - Bragi's Harp
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
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.46
    Bragi's Harp:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.49
    Heartwood Charm:
      total: 0.48
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.46
    Spear of Desolation:
      total: 0.62
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.27
    Soul Gem:
      total: 0.79
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  relic: *id002
- source: suggested
  archetype: model
  slot_order:
  - Bracer of The Abyss
  - Spear of Desolation
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of the Magus
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
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Bracer of The Abyss:
      total: 0.52
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.51
    Spear of Desolation:
      total: 0.62
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.63
    Spear of the Magus:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.5
    Obsidian Shard:
      total: 0.57
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.6
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.5
    Soul Gem:
      total: 0.79
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  relic: *id002
---

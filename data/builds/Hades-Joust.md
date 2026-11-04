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
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
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
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.46
    Spear of Desolation:
      total: 0.56
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.53
    Spear of the Magus:
      total: 0.5
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.42
    Obsidian Shard:
      total: 0.55
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.52
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.42
    Soul Gem:
      total: 0.79
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
  - Lotus Sickle
  - Bancroft's Talon
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Triton's Conch
  flex_slots:
  - Triton's Conch
  - Lotus Sickle
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
    Lotus Sickle:
      total: 0.47
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.37
    Bancroft's Talon:
      total: 0.55
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.42
    Obsidian Shard:
      total: 0.5
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.42
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.39
    Triton's Conch:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.52
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of the Magus
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
  rationale: Ability / burst skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.35
    Spear of Desolation:
      total: 0.56
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.52
    Spear of the Magus:
      total: 0.47
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.37
    Obsidian Shard:
      total: 0.53
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.37
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.98
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Obsidian Shard
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
      total: 0.56
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.45
    Obsidian Shard:
      total: 0.52
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.35
    Amanita Charm:
      total: 0.72
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.77
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.97
  starter: *id001
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
  - Spear of the Magus
  - Void Stone
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
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Void Stone:
      total: 0.55
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.64
    Spear of Desolation:
      total: 0.61
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.62
    Spear of the Magus:
      total: 0.55
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.53
    Obsidian Shard:
      total: 0.6
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.53
    Soul Gem:
      total: 0.79
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Nimble Ring
  - Bragi's Harp
  - Obsidian Shard
  - Rod of Tahuti
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Eros' Bow
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
  rationale: Basic-attack DPS skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Nimble Ring:
      total: 0.51
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.38
    Bragi's Harp:
      total: 0.48
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.52
    Obsidian Shard:
      total: 0.47
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.35
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.25
    Eros' Bow:
      total: 0.48
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.44
    Soul Gem:
      total: 0.67
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.76
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Screeching Gargoyle
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Screeching Gargoyle:
      total: 0.5
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.49
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.39
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.39
    Freya's Tears:
      total: 0.52
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.47
    Spear of Desolation:
      total: 0.57
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.56
    Soul Gem:
      total: 0.79
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
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
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.46
    Spear of Desolation:
      total: 0.56
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.53
    Spear of the Magus:
      total: 0.5
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.42
    Obsidian Shard:
      total: 0.55
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.52
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.42
    Soul Gem:
      total: 0.79
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
---

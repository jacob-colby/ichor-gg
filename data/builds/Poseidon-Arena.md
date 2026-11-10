---
type: smite-build
god: Poseidon
mode: Arena
builds:
- source: suggested
  archetype: core
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
    swap: Talisman of Purification — CC-immunity / cleanse
    swap_item: Talisman of Purification
  - vs_tag: magic_heavy
    swap: Sphere of Negation — magical protection
    swap_item: Sphere of Negation
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
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
    Dreamer's Idol:
      total: 0.76
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.99
    Soul Gem:
      total: 0.77
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: &id001
    base: Sands Of Time
    upgrade: Pendulum of the Ages
    pick_rate: 0.44
    win_rate: 0.5216
    matches: 168
    basis: community
    borrowed_from: Conquest
  relic: &id002
    name: Purification Beads
    pick_rate: 0.58
    win_rate: 0.49
    matches: 221
    basis: community
    borrowed_from: Conquest
- source: suggested
  archetype: mana-stack
  slot_order:
  - Bancroft's Talon
  - Book of Thoth
  - Death Metal
  - Spear of Desolation
  - Rod of Tahuti
  - Dreamer's Idol
  flex_slots:
  - Bancroft's Talon
  - Book of Thoth
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
  rationale: mana-stack (efficiency + fit). Arena — math + mode profile (no meta win/pick
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
    Dreamer's Idol:
      total: 0.6
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.67
  starter: *id001
  relic: *id002
- source: suggested
  archetype: burst
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
    Dreamer's Idol:
      total: 0.65
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.76
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
  - Magi's Cloak
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Magi's Cloak
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
      total: 0.61
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.61
    Magi's Cloak:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.51
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
      total: 0.74
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.71
      efficiency: 0.53
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
  - Obsidian Shard
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Doom Orb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Talisman of Purification — CC-immunity / cleanse
    swap_item: Talisman of Purification
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
    Dreamer's Idol:
      total: 0.77
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 1.0
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
      total: 0.71
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.83
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
    + fit). Arena — math + mode profile (no meta win/pick data).
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
  - Spear of Desolation
  - Heartseeker
  - Soul Gem
  flex_slots:
  - Heartseeker
  - Spear of Desolation
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
  rationale: Off-type Strength build — this kit scales on it (efficiency + fit). Arena
    — math + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.65
    Tyrfing:
      total: 0.6
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.67
    Bragi's Harp:
      total: 0.62
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.77
    Spear of Desolation:
      total: 0.58
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.55
    Heartseeker:
      total: 0.59
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.73
    Soul Gem:
      total: 0.72
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.9
  starter: *id001
  relic: *id002
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Spear of Desolation
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Dreamer's Idol
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.69
    Death Metal:
      total: 0.59
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.65
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.56
    Dreamer's Idol:
      total: 0.65
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.76
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
  - Obsidian Shard
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Doom Orb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Talisman of Purification — CC-immunity / cleanse
    swap_item: Talisman of Purification
  - vs_tag: magic_heavy
    swap: Sphere of Negation — magical protection
    swap_item: Sphere of Negation
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
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
    Dreamer's Idol:
      total: 0.76
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.99
    Soul Gem:
      total: 0.77
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
  relic: *id002
- source: suggested
  archetype: hybrid
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Tahuti
  - Dreamer's Idol
  flex_slots:
  - Spear of the Magus
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Talisman of Purification — CC-immunity / cleanse
    swap_item: Talisman of Purification
  - vs_tag: magic_heavy
    swap: Sphere of Negation — magical protection
    swap_item: Sphere of Negation
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: The model's core, corrected where the community is clearly right (efficiency
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Nimble Ring:
      total: 0.38
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.42
    Spear of Desolation:
      total: 0.8
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 1.0
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
    Dreamer's Idol:
      total: 0.76
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.99
  swaps:
  - added: Nimble Ring
    removed: Doom Orb
    reason: Conquest community 63% win over 76 matches (vs 52% on this god), taking
      the model's weakest slot from Doom Orb
  borrowed_from: Conquest
  starter: *id001
  relic: *id002
---

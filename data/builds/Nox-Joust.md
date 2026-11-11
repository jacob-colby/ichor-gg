---
type: smite-build
god: Nox
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Erosion
  - Soul Gem
  flex_slots:
  - Freya's Tears
  - Erosion
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
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.58
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.43
    Spear of Desolation:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.34
    Erosion:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.51
    Soul Gem:
      total: 0.74
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.9
  starter: &id001
    base: Sands Of Time
    upgrade: Pendulum of the Ages
    pick_rate: 0.34
    win_rate: 0.4082
    matches: 367
    basis: community
    borrowed_from: Conquest
  relic: &id002
    name: Purification Beads
    pick_rate: 0.32
    win_rate: 0.43
    matches: 345
    basis: community
    borrowed_from: Conquest
- source: suggested
  archetype: mana-stack
  slot_order:
  - Bancroft's Talon
  - Book of Thoth
  - Genji's Guard
  - Kinetic Cuirass
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Genji's Guard
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
    Bancroft's Talon:
      total: 0.54
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.55
    Book of Thoth:
      total: 0.36
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.24
    Genji's Guard:
      total: 0.49
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.43
    Spear of Desolation:
      total: 0.49
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.38
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.35
  starter: *id001
  relic: *id002
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Freya's Tears
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: Ability / burst skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.25
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.49
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.37
    Spear of Desolation:
      total: 0.53
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.33
    Soul Gem:
      total: 0.74
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.9
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
      total: 0.59
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.58
    Spear of Desolation:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.34
    Amanita Charm:
      total: 0.74
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.81
    Erosion:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.51
    Soul Gem:
      total: 0.77
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.95
  starter: *id001
  relic: *id002
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Void Shield
  - Void Stone
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Void Shield
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Screeching Gargoyle:
      total: 0.57
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.61
    Stone of Binding:
      total: 0.58
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.67
    Void Shield:
      total: 0.57
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.69
    Void Stone:
      total: 0.58
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.46
    Soul Gem:
      total: 0.79
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.99
  starter: *id001
  relic: *id002
- source: suggested
  archetype: attack-speed
  slot_order:
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Nimble Ring
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: Basic-attack DPS skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.4
    Bracer of The Abyss:
      total: 0.41
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.29
    Nimble Ring:
      total: 0.46
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.35
    Bragi's Harp:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.21
    Soul Gem:
      total: 0.65
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: *id001
  relic: *id002
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Gladiator's Shield
  - Freya's Tears
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Gladiator's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.47
    Gladiator's Shield:
      total: 0.53
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.62
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.54
    Spear of Desolation:
      total: 0.54
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.48
    Soul Gem:
      total: 0.76
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.93
  starter: *id001
  relic: *id002
- source: suggested
  archetype: model
  slot_order:
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Erosion
  - Soul Gem
  flex_slots:
  - Freya's Tears
  - Erosion
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
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.58
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.43
    Spear of Desolation:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.34
    Erosion:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.51
    Soul Gem:
      total: 0.74
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.9
  starter: *id001
  relic: *id002
- source: suggested
  archetype: hybrid
  slot_order:
  - Chronos' Pendant
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Freya's Tears
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: The model's core, corrected where the community is clearly right (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Chronos' Pendant:
      total: 0.43
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.29
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.58
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.43
    Spear of Desolation:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.34
    Soul Gem:
      total: 0.74
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.9
  swaps:
  - added: Chronos' Pendant
    removed: Erosion
    reason: Conquest community 53% win over 119 matches (vs 43% on this god), taking
      the model's weakest slot from Erosion
  borrowed_from: Conquest
  starter: *id001
  relic: *id002
---

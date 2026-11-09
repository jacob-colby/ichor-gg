---
type: smite-build
god: Neith
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Toxic Blade
  - Death Metal
  - Bragi's Harp
  - Riptalon
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Toxic Blade
  - Bragi's Harp
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
    Toxic Blade:
      total: 0.53
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
    Death Metal:
      total: 0.56
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.49
    Bragi's Harp:
      total: 0.53
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.59
    Riptalon:
      total: 0.59
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.74
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.3
    Soul Gem:
      total: 0.71
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.84
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
    pick_rate: 0.45
    win_rate: 0.5207
    matches: 77
    basis: community
    borrowed_from: Conquest
  relic: &id002
    name: Purification Beads
    pick_rate: 0.57
    win_rate: 0.55
    matches: 98
    basis: community
    borrowed_from: Conquest
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Death Metal
  - Bragi's Harp
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Bragi's Harp
  - Transcendence
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: mana-stack (efficiency + fit). Joust — math + mode profile (no meta win/pick
    data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.37
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.24
    Death Metal:
      total: 0.57
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.51
    Bragi's Harp:
      total: 0.54
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.61
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.35
    Soul Gem:
      total: 0.7
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.82
  starter: *id001
  relic: *id002
- source: suggested
  archetype: crit
  slot_order:
  - Toxic Blade
  - Rage
  - Death Metal
  - Bragi's Harp
  - Demon Blade
  - Soul Gem
  flex_slots:
  - Demon Blade
  - Rage
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
  rationale: Crit / auto-attack skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.52
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.61
    Rage:
      total: 0.41
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.36
    Death Metal:
      total: 0.57
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.51
    Bragi's Harp:
      total: 0.52
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.56
    Demon Blade:
      total: 0.45
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.54
    Soul Gem:
      total: 0.71
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.84
  starter: *id001
  relic: *id002
- source: suggested
  archetype: burst
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Death Metal
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Ability / burst skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.53
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.46
    Death Metal:
      total: 0.53
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.43
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
      fit: 0.91
  starter: *id001
  relic: *id002
- source: suggested
  archetype: bruiser
  slot_order:
  - Toxic Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Death Metal
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Death Metal
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
    Toxic Blade:
      total: 0.54
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.62
    Berserker's Shield:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.49
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.35
    Amanita Charm:
      total: 0.65
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.62
    Soul Gem:
      total: 0.67
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.76
  starter: *id001
  relic: *id002
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Death Metal
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Death Metal
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
    Toxic Blade:
      total: 0.57
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.71
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
    Death Metal:
      total: 0.52
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.42
    Spear of Desolation:
      total: 0.54
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.4
    Soul Gem:
      total: 0.75
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.92
  starter: *id001
  relic: *id002
- source: suggested
  archetype: attack-speed
  slot_order:
  - Toxic Blade
  - Tyrfing
  - Death Metal
  - Riptalon
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Rod of Tahuti
  - Death Metal
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
    Toxic Blade:
      total: 0.56
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.67
    Tyrfing:
      total: 0.54
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.54
    Death Metal:
      total: 0.52
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.41
    Riptalon:
      total: 0.61
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.25
    Soul Gem:
      total: 0.68
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.77
  starter: *id001
  relic: *id002
- source: suggested
  archetype: cooldown
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Hydra's Lament
  - Death Metal
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Hydra's Lament
  - Death Metal
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
    Toxic Blade:
      total: 0.51
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.58
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.49
    Hydra's Lament:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.46
    Death Metal:
      total: 0.49
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.35
    Spear of Desolation:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.49
    Soul Gem:
      total: 0.76
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.94
  starter: *id001
  relic: *id002
- source: suggested
  archetype: intelligence
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Off-type Intelligence build — this kit scales on it (efficiency + fit).
    Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.36
    Death Metal:
      total: 0.56
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.5
    Bragi's Harp:
      total: 0.54
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.6
    Spear of Desolation:
      total: 0.53
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.35
    Soul Gem:
      total: 0.74
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.91
  starter: *id001
  relic: *id002
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Bragi's Harp
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Tyrfing
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.39
    Tyrfing:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.51
    Death Metal:
      total: 0.58
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.53
    Bragi's Harp:
      total: 0.55
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.31
    Soul Gem:
      total: 0.71
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.84
  starter: *id001
  relic: *id002
- source: suggested
  archetype: model
  slot_order:
  - Toxic Blade
  - Death Metal
  - Bragi's Harp
  - Riptalon
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Toxic Blade
  - Bragi's Harp
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
    Toxic Blade:
      total: 0.53
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
    Death Metal:
      total: 0.56
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.49
    Bragi's Harp:
      total: 0.53
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.59
    Riptalon:
      total: 0.59
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.74
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.3
    Soul Gem:
      total: 0.71
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.84
  starter: *id001
  relic: *id002
---

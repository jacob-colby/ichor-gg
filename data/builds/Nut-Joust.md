---
type: smite-build
god: Nut
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
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
    swap: Sphere of Negation — magical protection
    swap_item: Sphere of Negation
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.59
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.73
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.45
    Tyrfing:
      total: 0.55
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.61
    Bragi's Harp:
      total: 0.58
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.71
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.38
    Soul Gem:
      total: 0.77
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.96
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Bancroft's Talon
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Bragi's Harp
  - Rod of Tahuti
  flex_slots:
  - Tyrfing
  - Hydra's Lament
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: mana-stack (efficiency + fit). Joust — math + mode profile (no meta win/pick
    data).
  slot_scores:
    Bancroft's Talon:
      total: 0.56
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.61
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.52
    Tyrfing:
      total: 0.53
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.57
    Hydra's Lament:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.49
    Bragi's Harp:
      total: 0.58
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.71
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Bragi's Harp
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
    Toxic Blade:
      total: 0.58
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.71
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.56
    Bragi's Harp:
      total: 0.53
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.62
    Spear of Desolation:
      total: 0.57
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.4
    Soul Gem:
      total: 0.79
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Toxic Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Eros' Bow
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Eros' Bow
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.58
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.57
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.44
    Eros' Bow:
      total: 0.49
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.66
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.67
    Soul Gem:
      total: 0.7
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.82
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.63
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.81
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.55
    Spear of Desolation:
      total: 0.58
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.57
    Obsidian Shard:
      total: 0.58
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.49
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
  - Toxic Blade
  - Tyrfing
  - Bragi's Harp
  - Riptalon
  - Silverbranch Bow
  - Soul Gem
  flex_slots:
  - Bragi's Harp
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Sphere of Negation — magical protection
    swap_item: Sphere of Negation
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Basic-attack DPS skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.6
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.74
    Tyrfing:
      total: 0.56
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.63
    Bragi's Harp:
      total: 0.54
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.63
    Riptalon:
      total: 0.67
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.88
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.55
    Soul Gem:
      total: 0.71
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Toxic Blade
  - Lotus Sickle
  - Jotunn's Revenge
  - Hydra's Lament
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Hydra's Lament
  - Lotus Sickle
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
      total: 0.55
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.65
    Lotus Sickle:
      total: 0.5
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.6
    Hydra's Lament:
      total: 0.55
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.54
    Spear of Desolation:
      total: 0.59
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.6
    Soul Gem:
      total: 0.79
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Bragi's Harp
  - Titan's Bane
  - Heartseeker
  - Soul Gem
  flex_slots:
  - Heartseeker
  - Tyrfing
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Off-type Strength build — this kit scales on it (efficiency + fit). Joust
    — math + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.59
    Tyrfing:
      total: 0.55
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.6
    Bragi's Harp:
      total: 0.57
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.7
    Titan's Bane:
      total: 0.56
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.59
    Heartseeker:
      total: 0.56
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.69
    Soul Gem:
      total: 0.77
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.97
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Bragi's Harp
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Toxic Blade
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Sphere of Negation — magical protection
    swap_item: Sphere of Negation
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.57
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.68
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.48
    Tyrfing:
      total: 0.56
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.62
    Bragi's Harp:
      total: 0.6
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.75
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.38
    Soul Gem:
      total: 0.76
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.94
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
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
    swap: Sphere of Negation — magical protection
    swap_item: Sphere of Negation
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.59
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.73
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.45
    Tyrfing:
      total: 0.55
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.61
    Bragi's Harp:
      total: 0.58
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.71
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.38
    Soul Gem:
      total: 0.77
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.96
  starter: *id001
---

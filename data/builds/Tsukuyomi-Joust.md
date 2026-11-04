---
type: smite-build
god: Tsukuyomi
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Tekko-Kagi
  - Soul Gem
  flex_slots:
  - Tekko-Kagi
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
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
      total: 0.6
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.74
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.49
    Tyrfing:
      total: 0.59
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.69
    Death Metal:
      total: 0.57
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.57
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.59
    Soul Gem:
      total: 0.61
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.69
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Bragi's Harp
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Bragi's Harp
  - Heartseeker
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
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.52
    Death Metal:
      total: 0.58
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.54
    Bragi's Harp:
      total: 0.56
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.67
    Heartseeker:
      total: 0.53
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.62
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.42
    Soul Gem:
      total: 0.68
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.83
  starter: *id001
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
  - Toxic Blade
  - Death Metal
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
      total: 0.55
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.65
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.56
    Death Metal:
      total: 0.54
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.44
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
      total: 0.73
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.94
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    Golden Blade:
      total: 0.51
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.51
    Toxic Blade:
      total: 0.58
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.58
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.49
    Amanita Charm:
      total: 0.69
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.72
    Soul Gem:
      total: 0.57
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Tekko-Kagi
  - Titan's Bane
  - Heartseeker
  - Soul Gem
  flex_slots:
  - Titan's Bane
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
      total: 0.65
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.84
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.6
    Tekko-Kagi:
      total: 0.61
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.66
    Titan's Bane:
      total: 0.6
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.67
    Heartseeker:
      total: 0.6
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.77
    Soul Gem:
      total: 0.69
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Soul Gem
  flex_slots:
  - Silverbranch Bow
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Basic-attack DPS skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.56
    Toxic Blade:
      total: 0.61
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.76
    Tyrfing:
      total: 0.58
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.66
    Riptalon:
      total: 0.68
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.9
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.56
    Soul Gem:
      total: 0.63
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.68
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
  - Toxic Blade
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
      total: 0.51
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.57
    Lotus Sickle:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.59
    Hydra's Lament:
      total: 0.55
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.55
    Spear of Desolation:
      total: 0.59
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.59
    Soul Gem:
      total: 0.75
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.97
  starter: *id001
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
  - Jotunn's Revenge
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Off-type Intelligence build — this kit scales on it (efficiency + fit).
    Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.46
    Death Metal:
      total: 0.59
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.54
    Bragi's Harp:
      total: 0.56
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.67
    Spear of Desolation:
      total: 0.57
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.54
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.41
    Soul Gem:
      total: 0.72
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.92
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Death Metal
  - Bragi's Harp
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Toxic Blade
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
    Toxic Blade:
      total: 0.55
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.64
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.44
    Death Metal:
      total: 0.61
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.59
    Bragi's Harp:
      total: 0.59
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.73
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.41
    Soul Gem:
      total: 0.67
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.82
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Tekko-Kagi
  - Soul Gem
  flex_slots:
  - Tekko-Kagi
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
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
      total: 0.6
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.74
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.49
    Tyrfing:
      total: 0.59
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.69
    Death Metal:
      total: 0.57
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.57
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.59
    Soul Gem:
      total: 0.61
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Tekko-Kagi
  - Heartseeker
  - Soul Gem
  flex_slots:
  - Tekko-Kagi
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: The model's core, corrected where the community is clearly right (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.6
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.74
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.49
    Tyrfing:
      total: 0.59
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.69
    Tekko-Kagi:
      total: 0.57
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.59
    Heartseeker:
      total: 0.54
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.64
    Soul Gem:
      total: 0.61
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.69
  swaps:
  - added: Heartseeker
    removed: Death Metal
    reason: Conquest community 63% win over 133 matches (vs 55% on this god), taking
      the model's weakest slot from Death Metal
  borrowed_from: Conquest
  starter: *id001
---

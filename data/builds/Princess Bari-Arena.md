---
type: smite-build
god: Princess Bari
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Tyrfing
  - Silverbranch Bow
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Eros' Bow
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.63
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.79
    Toxic Blade:
      total: 0.72
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.99
    Tyrfing:
      total: 0.64
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.6
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.69
    Eros' Bow:
      total: 0.63
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.76
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
  - Toxic Blade
  - Bancroft's Talon
  - Jotunn's Revenge
  - Tyrfing
  - Rod of Tahuti
  - Eros' Bow
  flex_slots:
  - Eros' Bow
  - Bancroft's Talon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: mana-stack (efficiency + fit). Arena — math + mode profile (no meta win/pick
    data).
  slot_scores:
    Toxic Blade:
      total: 0.64
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.82
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
      total: 0.6
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.7
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.42
    Eros' Bow:
      total: 0.6
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.7
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Silverbranch Bow
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Tyrfing
  - Eros' Bow
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
    Toxic Blade:
      total: 0.7
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.95
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.56
    Tyrfing:
      total: 0.58
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.67
    Silverbranch Bow:
      total: 0.58
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.65
    Eros' Bow:
      total: 0.58
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.67
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
  - Golden Blade
  - Toxic Blade
  - Eros' Bow
  - Amanita Charm
  - Pharaoh's Curse
  - Soul Gem
  flex_slots:
  - Pharaoh's Curse
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.6
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.69
    Toxic Blade:
      total: 0.68
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.88
    Eros' Bow:
      total: 0.63
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.74
    Amanita Charm:
      total: 0.8
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.95
    Pharaoh's Curse:
      total: 0.61
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.71
    Soul Gem:
      total: 0.79
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Silverbranch Bow
  - Rod of Tahuti
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Eros' Bow
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
    Toxic Blade:
      total: 0.73
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.55
    Silverbranch Bow:
      total: 0.63
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.75
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.49
    Eros' Bow:
      total: 0.58
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.67
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
  - Golden Blade
  - Toxic Blade
  - Tyrfing
  - Riptalon
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Tyrfing
  - Golden Blade
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
    Golden Blade:
      total: 0.56
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.64
    Toxic Blade:
      total: 0.65
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.84
    Tyrfing:
      total: 0.57
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.64
    Riptalon:
      total: 0.66
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.87
    Eros' Bow:
      total: 0.6
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.71
    Soul Gem:
      total: 0.79
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Spear of Desolation
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Tyrfing
  - Eros' Bow
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
    Toxic Blade:
      total: 0.67
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.89
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.59
    Tyrfing:
      total: 0.57
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.65
    Spear of Desolation:
      total: 0.59
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.59
    Eros' Bow:
      total: 0.56
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.63
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
  - Golden Blade
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Golden Blade
  - Triton's Conch
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Off-type Strength build — this kit scales on it (efficiency + fit). Arena
    — math + mode profile (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.62
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.76
    Toxic Blade:
      total: 0.66
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.87
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.59
    Tyrfing:
      total: 0.63
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.76
    Soul Gem:
      total: 0.79
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.58
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.79
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Tyrfing
  - Bragi's Harp
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Eros' Bow
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.62
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.76
    Toxic Blade:
      total: 0.69
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.93
    Tyrfing:
      total: 0.63
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.76
    Bragi's Harp:
      total: 0.6
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.75
    Eros' Bow:
      total: 0.61
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.74
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
  - Golden Blade
  - Toxic Blade
  - Tyrfing
  - Silverbranch Bow
  - Eros' Bow
  - Soul Gem
  flex_slots:
  - Eros' Bow
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.63
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.79
    Toxic Blade:
      total: 0.72
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.99
    Tyrfing:
      total: 0.64
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.6
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.69
    Eros' Bow:
      total: 0.63
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.76
    Soul Gem:
      total: 0.79
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
---

---
type: smite-build
god: Aladdin
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  - Soul Gem
  flex_slots:
  - Heartseeker
  - Hydra's Lament
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.77
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.9
    Hydra's Lament:
      total: 0.62
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.68
    Pendulum Blade:
      total: 0.65
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.9
    The Crusher:
      total: 0.71
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.79
    Heartseeker:
      total: 0.65
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.89
    Soul Gem:
      total: 0.78
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
  - Jotunn's Revenge
  - Hydra's Lament
  - The Crusher
  - Rod of Tahuti
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Triton's Conch
  - Hydra's Lament
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
    Jotunn's Revenge:
      total: 0.68
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.71
    Hydra's Lament:
      total: 0.59
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.63
    The Crusher:
      total: 0.6
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.77
      win: 0.5
      pick: 0.0
      fit: 0.57
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.6
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.77
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Pendulum Blade
  - The Crusher
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - The Crusher
  - Pendulum Blade
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
  rationale: Ability / burst skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.71
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.78
    Spear of Desolation:
      total: 0.65
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.78
    Pendulum Blade:
      total: 0.59
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.78
    The Crusher:
      total: 0.65
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.77
      win: 0.5
      pick: 0.0
      fit: 0.56
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Void Shield
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Soul Gem
  flex_slots:
  - Spectral Armor
  - Void Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.6
    Void Shield:
      total: 0.55
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.65
    Spectral Armor:
      total: 0.56
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.81
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.61
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.7
    Soul Gem:
      total: 0.74
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.91
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  - Titan's Bane
  - Soul Gem
  flex_slots:
  - Pendulum Blade
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.78
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.93
    Pendulum Blade:
      total: 0.67
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.93
    The Crusher:
      total: 0.76
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.89
    Heartseeker:
      total: 0.7
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.99
    Titan's Bane:
      total: 0.67
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.89
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Soul Gem
  flex_slots:
  - Silverbranch Bow
  - Jotunn's Revenge
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Basic-attack DPS skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.67
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.91
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.39
    Tyrfing:
      total: 0.58
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.71
    Riptalon:
      total: 0.74
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.95
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.61
    Soul Gem:
      total: 0.75
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.94
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Spear of Desolation
  - Pendulum Blade
  - Totem of Death
  - Soul Gem
  flex_slots:
  - Pendulum Blade
  - Totem of Death
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
    Jotunn's Revenge:
      total: 0.74
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.85
    Hydra's Lament:
      total: 0.65
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.75
    Spear of Desolation:
      total: 0.69
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.85
    Pendulum Blade:
      total: 0.63
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.85
    Totem of Death:
      total: 0.61
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.75
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  - Soul Gem
  flex_slots:
  - Heartseeker
  - Hydra's Lament
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.77
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.9
    Hydra's Lament:
      total: 0.62
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.68
    Pendulum Blade:
      total: 0.65
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.9
    The Crusher:
      total: 0.71
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.79
    Heartseeker:
      total: 0.65
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.89
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
---

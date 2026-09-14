---
type: smite-build
god: Nemesis
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Golden Blade
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
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.6
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.73
    Lernaean Bow:
      total: 0.61
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.69
    Toxic Blade:
      total: 0.66
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.88
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.49
    Tyrfing:
      total: 0.61
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.73
    Soul Gem:
      total: 0.74
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.96
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Bragi's Harp
  - Death Metal
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
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: mana-stack (efficiency + fit). Arena — math + mode profile (no meta win/pick
    data).
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.52
    Bragi's Harp:
      total: 0.56
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.67
    Death Metal:
      total: 0.57
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.54
    Heartseeker:
      total: 0.54
      efficiency: 0.47
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
      total: 0.76
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Toxic Blade
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  - Shogun's Ofuda
  - Soul Gem
  flex_slots:
  - Shogun's Ofuda
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.63
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.8
    Amanita Charm:
      total: 0.82
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.99
    Erosion:
      total: 0.6
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.69
    Pharaoh's Curse:
      total: 0.62
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.72
    Shogun's Ofuda:
      total: 0.61
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.72
    Soul Gem:
      total: 0.7
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.89
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Silverbranch Bow
  - Tekko-Kagi
  - Heartseeker
  - Soul Gem
  flex_slots:
  - Silverbranch Bow
  - Tekko-Kagi
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.71
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.98
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.61
    Silverbranch Bow:
      total: 0.6
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.68
    Tekko-Kagi:
      total: 0.58
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.66
    Heartseeker:
      total: 0.62
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.77
    Soul Gem:
      total: 0.76
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Toxic Blade
  - Tyrfing
  - Riptalon
  - Soul Gem
  flex_slots:
  - Golden Blade
  - Lernaean Bow
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
  rationale: Basic-attack DPS skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.67
    Lernaean Bow:
      total: 0.56
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.59
    Toxic Blade:
      total: 0.65
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.87
    Tyrfing:
      total: 0.57
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.67
    Riptalon:
      total: 0.71
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.9
    Soul Gem:
      total: 0.76
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.95
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Toxic Blade
  - Chronos' Pendant
  - Jotunn's Revenge
  - Hydra's Lament
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Hydra's Lament
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.57
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.7
    Chronos' Pendant:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.59
    Hydra's Lament:
      total: 0.55
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.55
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.59
    Soul Gem:
      total: 0.76
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Golden Blade
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
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.6
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.73
    Lernaean Bow:
      total: 0.61
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.69
    Toxic Blade:
      total: 0.66
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.88
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.49
    Tyrfing:
      total: 0.61
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.73
    Soul Gem:
      total: 0.74
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.96
  starter: *id001
---

---
type: smite-build
god: Kali
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Toxic Blade
  - Jotunn's Revenge
  - The Crusher
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
      total: 0.56
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.59
    Lernaean Bow:
      total: 0.6
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.69
    Toxic Blade:
      total: 0.59
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.75
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.49
    The Crusher:
      total: 0.59
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.55
    Soul Gem:
      total: 0.76
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.96
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Bancroft's Talon
  - Jotunn's Revenge
  - Bragi's Harp
  - Death Metal
  - Rod of Tahuti
  - Triton's Conch
  flex_slots:
  - Bragi's Harp
  - Bancroft's Talon
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
    Bancroft's Talon:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.53
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.52
    Bragi's Harp:
      total: 0.54
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.67
    Death Metal:
      total: 0.55
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.54
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.5
      pick: 0.0
      fit: 0.42
    Triton's Conch:
      total: 0.58
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.72
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  - Shogun's Ofuda
  - Soul Gem
  flex_slots:
  - Erosion
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Spectral Armor:
      total: 0.58
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.81
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.99
    Erosion:
      total: 0.61
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.69
    Pharaoh's Curse:
      total: 0.64
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.72
    Shogun's Ofuda:
      total: 0.61
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.72
    Soul Gem:
      total: 0.73
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.89
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Void Shield
  - The Crusher
  - Heartseeker
  - Soul Gem
  flex_slots:
  - Heartseeker
  - Void Shield
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
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.65
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.87
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.61
    Void Shield:
      total: 0.58
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.7
    The Crusher:
      total: 0.66
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.67
    Heartseeker:
      total: 0.59
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.77
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
  - Golden Blade
  - Toxic Blade
  - Tyrfing
  - Riptalon
  - Pharaoh's Curse
  - Soul Gem
  flex_slots:
  - Tyrfing
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
      total: 0.6
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.67
    Toxic Blade:
      total: 0.65
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.87
    Tyrfing:
      total: 0.56
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.67
    Riptalon:
      total: 0.72
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.9
    Pharaoh's Curse:
      total: 0.55
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.56
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
  - Genji's Guard
  - Jotunn's Revenge
  - Hydra's Lament
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Toxic Blade
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
      total: 0.52
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.61
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.64
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
      total: 0.55
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.59
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
  - Golden Blade
  - Lernaean Bow
  - Toxic Blade
  - Jotunn's Revenge
  - The Crusher
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
      total: 0.56
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.59
    Lernaean Bow:
      total: 0.6
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.69
    Toxic Blade:
      total: 0.59
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.75
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.49
    The Crusher:
      total: 0.59
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.55
    Soul Gem:
      total: 0.76
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.96
  starter: *id001
---

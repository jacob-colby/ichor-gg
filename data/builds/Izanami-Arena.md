---
type: smite-build
god: Izanami
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Toxic Blade
  - Jotunn's Revenge
  - Riptalon
  - Pharaoh's Curse
  - Soul Gem
  flex_slots:
  - Lernaean Bow
  - Pharaoh's Curse
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
    Lernaean Bow:
      total: 0.55
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.59
    Toxic Blade:
      total: 0.6
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.74
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.39
    Riptalon:
      total: 0.65
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.78
    Pharaoh's Curse:
      total: 0.54
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.54
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Toxic Blade
  - Bancroft's Talon
  - Jotunn's Revenge
  - Death Metal
  - Rod of Tahuti
  - Triton's Conch
  flex_slots:
  - Toxic Blade
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: mana-stack (efficiency + fit). Arena — math + mode profile (no meta win/pick
    data).
  slot_scores:
    Toxic Blade:
      total: 0.54
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.62
    Bancroft's Talon:
      total: 0.53
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.55
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.44
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.35
    Triton's Conch:
      total: 0.55
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Death Metal
  - Demon Blade
  - Deathbringer
  - Soul Gem
  flex_slots:
  - Demon Blade
  - Deathbringer
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
  rationale: Crit / auto-attack skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.59
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.72
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.38
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.46
    Demon Blade:
      total: 0.5
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.63
    Deathbringer:
      total: 0.46
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.41
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Death Metal
  - Rod of Tahuti
  - Pharaoh's Curse
  - Soul Gem
  flex_slots:
  - Death Metal
  - Pharaoh's Curse
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
      total: 0.59
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.71
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.46
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.43
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.33
    Pharaoh's Curse:
      total: 0.51
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.47
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
  - Toxic Blade
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  - Shogun's Ofuda
  - Soul Gem
  flex_slots:
  - Toxic Blade
  - Erosion
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.59
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.72
    Amanita Charm:
      total: 0.79
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.92
    Erosion:
      total: 0.57
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.62
    Pharaoh's Curse:
      total: 0.62
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.68
    Shogun's Ofuda:
      total: 0.61
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.68
    Soul Gem:
      total: 0.76
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Void Shield
  - Void Stone
  - The Crusher
  - Soul Gem
  flex_slots:
  - Void Stone
  - The Crusher
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
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.84
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.5
    Void Shield:
      total: 0.58
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.7
    Void Stone:
      total: 0.58
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.7
    The Crusher:
      total: 0.55
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.52
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
      total: 0.56
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.59
    Toxic Blade:
      total: 0.63
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.79
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.59
    Riptalon:
      total: 0.66
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.82
    Pharaoh's Curse:
      total: 0.54
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.52
    Soul Gem:
      total: 0.76
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Spear of Desolation
  - Pharaoh's Curse
  - Shogun's Ofuda
  - Soul Gem
  flex_slots:
  - Pharaoh's Curse
  - Shogun's Ofuda
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
      total: 0.55
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.64
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.48
    Pharaoh's Curse:
      total: 0.52
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.48
    Shogun's Ofuda:
      total: 0.51
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.48
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
  - Lernaean Bow
  - Toxic Blade
  - Jotunn's Revenge
  - Riptalon
  - Pharaoh's Curse
  - Soul Gem
  flex_slots:
  - Lernaean Bow
  - Pharaoh's Curse
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
    Lernaean Bow:
      total: 0.55
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.59
    Toxic Blade:
      total: 0.6
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.74
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.39
    Riptalon:
      total: 0.65
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.78
    Pharaoh's Curse:
      total: 0.54
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.54
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
---

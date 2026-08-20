---
type: smite-build
god: Hou Yi
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Toxic Blade
  - Bragi's Harp
  - Death Metal
  - Riptalon
  - Demon Blade
  - Soul Gem
  flex_slots:
  - Toxic Blade
  - Bragi's Harp
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
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.53
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.63
    Bragi's Harp:
      total: 0.52
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.62
    Death Metal:
      total: 0.54
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.52
    Riptalon:
      total: 0.61
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.69
    Demon Blade:
      total: 0.55
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.75
    Soul Gem:
      total: 0.69
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.8
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Bancroft's Talon
  - Jotunn's Revenge
  - Bragi's Harp
  - Death Metal
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Bragi's Harp
  - The Crusher
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
  rationale: mana-stack (efficiency + fit). Joust — math + mode profile (no meta win/pick
    data).
  slot_scores:
    Bancroft's Talon:
      total: 0.54
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.55
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.44
    Bragi's Harp:
      total: 0.51
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.61
    Death Metal:
      total: 0.54
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.51
    The Crusher:
      total: 0.51
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.39
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.77
      win: 0.5
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Toxic Blade
  - Death Metal
  - Damaru
  - Demon Blade
  - Pharaoh's Curse
  - Soul Gem
  flex_slots:
  - Toxic Blade
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
  rationale: Crit / auto-attack skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.52
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.61
    Death Metal:
      total: 0.55
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.55
    Damaru:
      total: 0.53
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.49
    Demon Blade:
      total: 0.55
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.75
    Pharaoh's Curse:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.46
    Soul Gem:
      total: 0.68
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  - Shogun's Ofuda
  - Soul Gem
  flex_slots:
  - Berserker's Shield
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.43
    Amanita Charm:
      total: 0.74
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.86
    Erosion:
      total: 0.54
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.56
    Pharaoh's Curse:
      total: 0.59
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.63
    Shogun's Ofuda:
      total: 0.57
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.63
    Soul Gem:
      total: 0.67
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.76
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
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.62
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.82
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.47
    Void Shield:
      total: 0.53
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.6
    The Crusher:
      total: 0.59
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.55
    Heartseeker:
      total: 0.53
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.65
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
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Pharaoh's Curse
  - Soul Gem
  flex_slots:
  - Pharaoh's Curse
  - Silverbranch Bow
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
  rationale: Basic-attack DPS skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.6
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.77
    Tyrfing:
      total: 0.57
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.67
    Riptalon:
      total: 0.67
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.81
    Silverbranch Bow:
      total: 0.5
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.47
    Pharaoh's Curse:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.46
    Soul Gem:
      total: 0.66
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.75
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Toxic Blade
  - Genji's Guard
  - Jotunn's Revenge
  - Hydra's Lament
  - Totem of Death
  - Soul Gem
  flex_slots:
  - Totem of Death
  - Toxic Blade
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
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.48
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.5
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.43
    Hydra's Lament:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.5
    Totem of Death:
      total: 0.49
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.5
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Divine Ruin
  - Toxic Blade
  - Bragi's Harp
  - Death Metal
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Bragi's Harp
  - Divine Ruin
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Off-type Intelligence build — this kit scales on it (efficiency + fit).
    Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.5
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.61
    Toxic Blade:
      total: 0.52
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.62
    Bragi's Harp:
      total: 0.51
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.6
    Death Metal:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.77
      win: 0.5
      pick: 0.0
      fit: 0.35
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Toxic Blade
  - Bragi's Harp
  - Death Metal
  - The Crusher
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Bragi's Harp
  - The Crusher
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
  rationale: Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.54
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.64
    Bragi's Harp:
      total: 0.54
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.65
    Death Metal:
      total: 0.56
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.53
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.43
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.77
      win: 0.5
      pick: 0.0
      fit: 0.33
    Soul Gem:
      total: 0.77
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.98
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Toxic Blade
  - Bragi's Harp
  - Death Metal
  - Riptalon
  - Demon Blade
  - Soul Gem
  flex_slots:
  - Toxic Blade
  - Bragi's Harp
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
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.53
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.63
    Bragi's Harp:
      total: 0.52
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.62
    Death Metal:
      total: 0.54
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.52
    Riptalon:
      total: 0.61
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.69
    Demon Blade:
      total: 0.55
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.75
    Soul Gem:
      total: 0.69
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.8
  starter: *id001
---

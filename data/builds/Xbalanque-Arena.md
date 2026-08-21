---
type: smite-build
god: Xbalanque
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Toxic Blade
  - Tyrfing
  - Riptalon
  - Demon Blade
  flex_slots:
  - Lernaean Bow
  - Demon Blade
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.67
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.83
    Lernaean Bow:
      total: 0.63
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.74
    Toxic Blade:
      total: 0.64
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.82
    Tyrfing:
      total: 0.66
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.83
    Riptalon:
      total: 0.71
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.9
    Demon Blade:
      total: 0.63
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.87
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Jotunn's Revenge
  - Hydra's Lament
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Heartseeker
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: mana-stack (efficiency + fit). Arena — math + mode profile (no meta win/pick
    data).
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.53
    Toxic Blade:
      total: 0.56
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.67
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.44
    Hydra's Lament:
      total: 0.48
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.42
    Heartseeker:
      total: 0.51
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Golden Blade
  - Tyrfing
  - Riptalon
  - Damaru
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Deathbringer
  - Damaru
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Crit / auto-attack skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.65
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.79
    Tyrfing:
      total: 0.63
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.79
    Riptalon:
      total: 0.68
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.86
    Damaru:
      total: 0.54
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.57
    Demon Blade:
      total: 0.63
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.88
    Deathbringer:
      total: 0.54
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Amanita Charm
  - Erosion
  - Pharaoh's Curse
  - Shogun's Ofuda
  - Umbral Link
  flex_slots:
  - Erosion
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.61
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.69
    Amanita Charm:
      total: 0.83
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.61
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.7
    Pharaoh's Curse:
      total: 0.66
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.78
    Shogun's Ofuda:
      total: 0.65
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.78
    Umbral Link:
      total: 0.61
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Void Shield
  - Void Stone
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Void Shield
  - Void Stone
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.72
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.99
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.47
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
    Riptalon:
      total: 0.75
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 1.0
    Silverbranch Bow:
      total: 0.61
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Toxic Blade
  - Tyrfing
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Lernaean Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Basic-attack DPS skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.63
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.75
    Lernaean Bow:
      total: 0.58
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.65
    Toxic Blade:
      total: 0.63
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.79
    Tyrfing:
      total: 0.62
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.75
    Riptalon:
      total: 0.67
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.84
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Hydra's Lament
  - Pharaoh's Curse
  flex_slots:
  - Hydra's Lament
  - Golden Blade
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.52
    Toxic Blade:
      total: 0.54
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.62
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.41
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.57
    Hydra's Lament:
      total: 0.53
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.51
    Pharaoh's Curse:
      total: 0.53
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.51
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Divine Ruin
  - Toxic Blade
  - Jotunn's Revenge
  - Death Metal
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Triton's Conch
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
    Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.52
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.61
    Toxic Blade:
      total: 0.59
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.72
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.36
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.5
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.53
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Bragi's Harp
  - Death Metal
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Golden Blade
  - Bragi's Harp
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
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.6
    Toxic Blade:
      total: 0.61
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.77
    Bragi's Harp:
      total: 0.56
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.67
    Death Metal:
      total: 0.59
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.34
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
  - Tyrfing
  - Riptalon
  - Demon Blade
  flex_slots:
  - Lernaean Bow
  - Demon Blade
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.67
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.83
    Lernaean Bow:
      total: 0.63
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.74
    Toxic Blade:
      total: 0.64
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.82
    Tyrfing:
      total: 0.66
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.83
    Riptalon:
      total: 0.71
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.9
    Demon Blade:
      total: 0.63
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.87
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Toxic Blade
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Lernaean Bow
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: The model's core, corrected where the community is clearly right (efficiency
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.67
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.83
    Lernaean Bow:
      total: 0.63
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.74
    Toxic Blade:
      total: 0.64
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.82
    Tyrfing:
      total: 0.66
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.83
    Riptalon:
      total: 0.71
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.9
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.52
  swaps:
  - added: Silverbranch Bow
    removed: Demon Blade
    reason: Conquest community 68% win over 149 matches (vs 57% on this god), taking
      the model's weakest slot from Demon Blade
  borrowed_from: Conquest
  starter: *id001
---

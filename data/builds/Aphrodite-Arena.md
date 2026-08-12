---
type: smite-build
god: Aphrodite
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Void Shield
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Stampede
  flex_slots:
  - Kinetic Cuirass
  - Void Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.6
    Void Shield:
      total: 0.59
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.73
    Spectral Armor:
      total: 0.6
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.82
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.66
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.8
    Stampede:
      total: 0.61
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Void Shield
  - Spectral Armor
  - Erosion
  - Stampede
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Spectral Armor
  - Void Shield
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Ability / burst skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Void Shield:
      total: 0.55
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.64
    Spectral Armor:
      total: 0.56
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.54
    Erosion:
      total: 0.59
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.67
    Stampede:
      total: 0.56
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.64
    Soul Gem:
      total: 0.79
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.57
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Stampede
  - Soul Gem
  flex_slots:
  - Spectral Armor
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.6
    Spectral Armor:
      total: 0.61
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.65
    Amanita Charm:
      total: 0.82
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.66
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.8
    Stampede:
      total: 0.61
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.75
    Soul Gem:
      total: 0.79
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Void Shield
  - Void Stone
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Stampede
  flex_slots:
  - Stampede
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Void Shield:
      total: 0.71
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.97
    Void Stone:
      total: 0.7
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.97
    Spectral Armor:
      total: 0.57
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.79
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.96
    Erosion:
      total: 0.61
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.71
    Stampede:
      total: 0.57
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.67
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Spectral Armor
  - Erosion
  - Soul Gem
  flex_slots:
  - Bracer of The Abyss
  - Nimble Ring
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
    Bracer of The Abyss:
      total: 0.42
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.41
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.34
    Bragi's Harp:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.47
    Spectral Armor:
      total: 0.53
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.49
    Erosion:
      total: 0.55
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.59
    Soul Gem:
      total: 0.79
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.99
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Freya's Tears
  - Spectral Armor
  - Erosion
  - Stampede
  - Soul Gem
  flex_slots:
  - Stampede
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.58
    Spectral Armor:
      total: 0.57
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.56
    Erosion:
      total: 0.61
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.69
    Stampede:
      total: 0.57
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.66
    Soul Gem:
      total: 0.79
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Spectral Armor
  - Erosion
  - Pharaoh's Curse
  - Shogun's Ofuda
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Shogun's Ofuda
  - Spectral Armor
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Off-type Strength build — this kit scales on it (efficiency + fit). Arena
    — math + mode profile (no meta win/pick data).
  slot_scores:
    Spectral Armor:
      total: 0.55
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.53
    Erosion:
      total: 0.58
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.65
    Pharaoh's Curse:
      total: 0.59
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.61
    Shogun's Ofuda:
      total: 0.57
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.61
    Soul Gem:
      total: 0.79
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.6
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.75
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Spectral Armor
  - Erosion
  - Stampede
  - Pharaoh's Curse
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Spectral Armor
  - Pharaoh's Curse
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
  rationale: Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Spectral Armor:
      total: 0.57
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.55
    Erosion:
      total: 0.6
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.69
    Stampede:
      total: 0.57
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.65
    Pharaoh's Curse:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.55
    Soul Gem:
      total: 0.79
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.61
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.77
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Kinetic Cuirass
  - Void Shield
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Stampede
  flex_slots:
  - Kinetic Cuirass
  - Void Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.6
    Void Shield:
      total: 0.59
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.73
    Spectral Armor:
      total: 0.6
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.82
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.66
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.8
    Stampede:
      total: 0.61
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: *id001
---

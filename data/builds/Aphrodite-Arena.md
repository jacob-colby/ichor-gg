---
type: smite-build
god: Aphrodite
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Mystical Mail
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Stampede
  flex_slots:
  - Kinetic Cuirass
  - Mystical Mail
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Doublet of Binding — magical protection
    swap_item: Doublet of Binding
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.6
    Mystical Mail:
      total: 0.61
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.73
    Spectral Armor:
      total: 0.65
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.84
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.68
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.8
    Stampede:
      total: 0.63
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Mystical Mail
  - Spectral Armor
  - Erosion
  - Stampede
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Stampede
  - Mystical Mail
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Ability / burst skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Mystical Mail:
      total: 0.57
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.64
    Spectral Armor:
      total: 0.6
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.54
    Erosion:
      total: 0.61
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.67
    Stampede:
      total: 0.59
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.64
    Soul Gem:
      total: 0.81
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.62
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Spectral Armor
  - Amanita Charm
  - Rod of Asclepius
  - Erosion
  - Stampede
  - Triton's Conch
  flex_slots:
  - Stampede
  - Triton's Conch
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Spectral Armor:
      total: 0.66
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.65
    Amanita Charm:
      total: 0.84
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 1.0
    Rod of Asclepius:
      total: 0.81
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.68
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.8
    Stampede:
      total: 0.64
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.75
    Triton's Conch:
      total: 0.63
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.7
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Void Shield
  - Void Stone
  - Dreamer's Idol
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Spectral Armor
  - Dreamer's Idol
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Void Shield:
      total: 0.73
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.97
    Void Stone:
      total: 0.71
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.97
    Dreamer's Idol:
      total: 0.6
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.68
    Spectral Armor:
      total: 0.62
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.82
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.96
    Erosion:
      total: 0.63
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Death Metal
  - Damaru
  - Demon Blade
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: For fun — deliberately fights this god's kit (Crit / attack-speed party
    build). Scored on gold-value + flavor fit only; not meta-checked.
  slot_scores:
    Golden Blade:
      total: 0.65
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.67
    Lernaean Bow:
      total: 0.71
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.77
    Death Metal:
      total: 0.65
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.66
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.73
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
    Pharaoh's Curse:
      total: 0.64
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.64
  fun: true
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Kinetic Cuirass
  - Mystical Mail
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Stampede
  flex_slots:
  - Kinetic Cuirass
  - Mystical Mail
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Doublet of Binding — magical protection
    swap_item: Doublet of Binding
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.6
    Mystical Mail:
      total: 0.61
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.73
    Spectral Armor:
      total: 0.65
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.84
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.68
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.8
    Stampede:
      total: 0.63
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: *id001
---

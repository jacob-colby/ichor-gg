---
type: smite-build
god: Sol
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Divine Ruin
  - Bragi's Harp
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
  - Spear of the Magus
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
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.49
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.64
    Bragi's Harp:
      total: 0.49
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.64
    Spear of Desolation:
      total: 0.5
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.58
    The Cosmic Horror:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.46
    Spear of the Magus:
      total: 0.44
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.46
    Soul Gem:
      total: 0.7
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Divine Ruin
  - Bragi's Harp
  - Spear of Desolation
  - The Cosmic Horror
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Divine Ruin
  - The Cosmic Horror
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
  rationale: Ability / burst skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.45
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.56
    Bragi's Harp:
      total: 0.48
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.62
    Spear of Desolation:
      total: 0.49
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.56
    The Cosmic Horror:
      total: 0.43
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.4
    Soul Gem:
      total: 0.7
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.48
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Divine Ruin
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Stampede
  - Soul Gem
  flex_slots:
  - Divine Ruin
  - Stampede
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.44
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.55
    Spectral Armor:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.42
    Amanita Charm:
      total: 0.64
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.83
    Erosion:
      total: 0.46
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.53
    Stampede:
      total: 0.43
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.52
    Soul Gem:
      total: 0.7
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Void Shield
  - Void Stone
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - Void Shield
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
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Void Shield:
      total: 0.49
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.7
    Void Stone:
      total: 0.5
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.7
    Spear of Desolation:
      total: 0.54
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.66
    The Cosmic Horror:
      total: 0.52
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.5
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.56
    Soul Gem:
      total: 0.7
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Death Metal
  - Damaru
  - Demon Blade
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Damaru
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: For fun — deliberately fights this god's kit (Crit / attack-speed party
    build). Scored on gold-value + flavor fit only; not meta-checked.
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.67
    Lernaean Bow:
      total: 0.57
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.77
    Death Metal:
      total: 0.55
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.51
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.6
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 1.0
    Soul Gem:
      total: 0.53
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.65
  fun: true
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Divine Ruin
  - Bragi's Harp
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
  - Spear of the Magus
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
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.49
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.64
    Bragi's Harp:
      total: 0.49
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.64
    Spear of Desolation:
      total: 0.5
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.58
    The Cosmic Horror:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.46
    Spear of the Magus:
      total: 0.44
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.46
    Soul Gem:
      total: 0.7
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
---

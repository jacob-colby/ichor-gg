---
type: smite-build
god: Ah Puch
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Doom Orb
  - Spear of the Magus
  - The World Stone
  - Soul Gem
  flex_slots:
  - Doom Orb
  - The World Stone
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
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Spear of Desolation:
      total: 0.71
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Cosmic Horror:
      total: 0.63
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.79
    Doom Orb:
      total: 0.6
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.61
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.79
    The World Stone:
      total: 0.58
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.79
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
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Spear of the Magus
  - Divine Ruin
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Ability / burst skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.48
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.62
    Spear of Desolation:
      total: 0.6
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.78
    The Cosmic Horror:
      total: 0.51
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.49
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
    Triton's Conch:
      total: 0.49
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Divine Ruin
  - Stygian Anchor
  - Spear of Desolation
  - Amanita Charm
  - Erosion
  - Soul Gem
  flex_slots:
  - Erosion
  - Stygian Anchor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.47
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.61
    Stygian Anchor:
      total: 0.43
      efficiency: 0.25
      win: 0.5
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.46
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.49
    Amanita Charm:
      total: 0.63
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.81
    Erosion:
      total: 0.45
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.51
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
  - Spear of Desolation
  - The Cosmic Horror
  - Doom Orb
  - Spear of the Magus
  - The World Stone
  - Soul Gem
  flex_slots:
  - Doom Orb
  - The World Stone
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
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Spear of Desolation:
      total: 0.71
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Cosmic Horror:
      total: 0.66
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.85
    Doom Orb:
      total: 0.63
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.64
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.85
    The World Stone:
      total: 0.61
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.85
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
  - Tyrfing
  - Rage
  - Bragi's Harp
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Bragi's Harp
  - Rage
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
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
    Tyrfing:
      total: 0.52
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.67
    Rage:
      total: 0.5
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.66
    Bragi's Harp:
      total: 0.5
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.67
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
  fun: true
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Doom Orb
  - Spear of the Magus
  - The World Stone
  - Soul Gem
  flex_slots:
  - Doom Orb
  - The World Stone
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
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Spear of Desolation:
      total: 0.71
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Cosmic Horror:
      total: 0.63
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.79
    Doom Orb:
      total: 0.6
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.61
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.79
    The World Stone:
      total: 0.58
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.7
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
---

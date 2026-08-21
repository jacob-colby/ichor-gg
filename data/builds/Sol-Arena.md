---
type: smite-build
god: Sol
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Bragi's Harp
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
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Bragi's Harp:
      total: 0.54
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.64
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.58
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.46
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.56
    Dreamer's Idol:
      total: 0.58
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.66
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
  - Divine Ruin
  - Bancroft's Talon
  - Bragi's Harp
  - Doom Orb
  - Rod of Tahuti
  - Triton's Conch
  flex_slots:
  - Divine Ruin
  - Doom Orb
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
  rationale: mana-stack (efficiency + fit). Arena — math + mode profile (no meta win/pick
    data).
  slot_scores:
    Divine Ruin:
      total: 0.52
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.61
    Bancroft's Talon:
      total: 0.56
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.61
    Bragi's Harp:
      total: 0.58
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.71
    Doom Orb:
      total: 0.47
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.42
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
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
  archetype: burst
  slot_order:
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Bragi's Harp
  - Triton's Conch
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
  rationale: Ability / burst skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Bragi's Harp:
      total: 0.53
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.62
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.4
    Dreamer's Idol:
      total: 0.55
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.6
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
  archetype: bruiser
  slot_order:
  - Void Shield
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Stampede
  - Soul Gem
  flex_slots:
  - Spectral Armor
  - Void Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    Void Shield:
      total: 0.57
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.66
    Spectral Armor:
      total: 0.57
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.56
    Amanita Charm:
      total: 0.82
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.98
    Erosion:
      total: 0.6
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.68
    Stampede:
      total: 0.59
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.66
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Void Shield
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Void Shield
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
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Void Shield:
      total: 0.58
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.7
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.56
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.66
    Dreamer's Idol:
      total: 0.63
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.76
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
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Triton's Conch
  - Bracer of The Abyss
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
  rationale: Basic-attack DPS skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.54
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.31
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.51
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
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
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.34
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.34
    Chronos' Pendant:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.6
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.26
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Soul Gem
  - Triton's Conch
  flex_slots:
  - Triton's Conch
  - Tyrfing
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
  rationale: Off-type Strength build — this kit scales on it (efficiency + fit). Arena
    — math + mode profile (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.62
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.71
    Toxic Blade:
      total: 0.64
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.81
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.59
    Tyrfing:
      total: 0.6
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.71
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.61
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.79
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Bragi's Harp
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
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
      total: 0.62
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.72
    Toxic Blade:
      total: 0.67
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.88
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.48
    Tyrfing:
      total: 0.6
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.72
    Bragi's Harp:
      total: 0.6
      efficiency: 0.44
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
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Bragi's Harp
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
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Bragi's Harp:
      total: 0.54
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.64
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.58
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.46
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.56
    Dreamer's Idol:
      total: 0.58
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.66
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
---

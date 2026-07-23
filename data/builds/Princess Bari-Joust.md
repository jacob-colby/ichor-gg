---
type: smite-build
god: Princess Bari
mode: Joust
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.57
    win_rate: 0.47
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.1
      win_rate: 0.42
    - name: Book of Thoth
      pick_rate: 0.1
      win_rate: 0.61
  - name: Soul Gem
    pick_rate: 0.19
    win_rate: 0.44
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.18
      win_rate: 0.61
    - name: The World Stone
      pick_rate: 0.14
      win_rate: 0.44
  - name: Rod of Tahuti
    pick_rate: 0.15
    win_rate: 0.59
    alternates:
    - name: Soul Gem
      pick_rate: 0.19
      win_rate: 0.59
    - name: The World Stone
      pick_rate: 0.13
      win_rate: 0.42
  - name: Obsidian Shard
    pick_rate: 0.2
    win_rate: 0.47
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.28
      win_rate: 0.48
    - name: Soul Gem
      pick_rate: 0.05
      win_rate: 0.63
  - name: Blinking Abyss
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.2
      win_rate: 0.69
    - name: Rod of Tahuti
      pick_rate: 0.16
      win_rate: 0.58
  - name: Evil Eye
    pick_rate: 0.1
    win_rate: 0.82
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.09
      win_rate: 0.7
    - name: Void Shard
      pick_rate: 0.08
      win_rate: 0.44
  source_url: https://smitebrain.com/gods/princess-bari/
  last_verified: '2026-07-23'
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
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.51
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.66
    Bragi's Harp:
      total: 0.49
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.62
    Spear of Desolation:
      total: 0.51
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.61
    The Cosmic Horror:
      total: 0.47
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.47
    Spear of the Magus:
      total: 0.45
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.47
    Soul Gem:
      total: 0.71
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
  - Triton's Conch
  - The Cosmic Horror
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
      total: 0.46
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.57
    Bragi's Harp:
      total: 0.48
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.6
    Spear of Desolation:
      total: 0.5
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.58
    The Cosmic Horror:
      total: 0.44
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.42
    Soul Gem:
      total: 0.71
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 1.0
    Triton's Conch:
      total: 0.44
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.53
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Divine Ruin
  - Stygian Anchor
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Soul Gem
  flex_slots:
  - Spectral Armor
  - Stygian Anchor
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Divine Ruin:
      total: 0.46
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.55
    Stygian Anchor:
      total: 0.41
      efficiency: 0.26
      win: 0.5
      pick: 0.0
      fit: 0.55
    Spectral Armor:
      total: 0.41
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.32
    Amanita Charm:
      total: 0.6
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.75
    Erosion:
      total: 0.42
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.45
    Soul Gem:
      total: 0.71
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
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Spear of Desolation:
      total: 0.56
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.7
    The Cosmic Horror:
      total: 0.53
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.6
    Doom Orb:
      total: 0.5
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.6
    Spear of the Magus:
      total: 0.51
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.6
    The World Stone:
      total: 0.48
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.6
    Soul Gem:
      total: 0.71
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
      total: 0.53
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.67
    Rage:
      total: 0.51
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.66
    Bragi's Harp:
      total: 0.51
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.67
    Death Metal:
      total: 0.55
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.52
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.61
      efficiency: 0.22
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
---

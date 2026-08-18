---
type: smite-build
god: Vulcan
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fortification
  aspect_pick_rate: 0.13
  aspect_win_rate: 0.59
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.35
    win_rate: 0.55
    alternates:
    - name: Book of Thoth
      pick_rate: 0.34
      win_rate: 0.55
    - name: Chronos' Pendant
      pick_rate: 0.06
      win_rate: 0.63
  - name: The World Stone
    pick_rate: 0.14
    win_rate: 0.53
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.27
      win_rate: 0.51
    - name: Book of Thoth
      pick_rate: 0.13
      win_rate: 0.55
  - name: Rod of Tahuti
    pick_rate: 0.19
    win_rate: 0.59
    alternates:
    - name: Soul Gem
      pick_rate: 0.14
      win_rate: 0.61
    - name: The World Stone
      pick_rate: 0.13
      win_rate: 0.54
  - name: Obsidian Shard
    pick_rate: 0.31
    win_rate: 0.59
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.23
      win_rate: 0.63
    - name: Soul Reaver
      pick_rate: 0.06
      win_rate: 0.32
  - name: Evil Eye
    pick_rate: 0.09
    win_rate: 0.38
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.16
      win_rate: 0.58
    - name: Obsidian Shard
      pick_rate: 0.16
      win_rate: 0.66
  - name: Shrapnel Mod
    pick_rate: 0.12
    win_rate: 0.38
    alternates:
    - name: Thermal Mod
      pick_rate: 0.11
      win_rate: 0.41
    - name: Surplus Mod
      pick_rate: 0.09
      win_rate: 0.56
  - name: Surplus Mod
    pick_rate: 0.24
    win_rate: 0.38
    alternates:
    - name: Shrapnel Mod
      pick_rate: 0.34
      win_rate: 0.55
    - name: Thermal Mod
      pick_rate: 0.21
      win_rate: 0.7
  - name: Thermal Mod
    pick_rate: 0.14
    win_rate: 0.7
    alternates:
    - name: Surplus Mod
      pick_rate: 0.69
      win_rate: 0.6
    - name: Seismic Mod
      pick_rate: 0.12
      win_rate: 0.65
  - name: Seismic Mod
    pick_rate: 0.64
    win_rate: 0.64
    alternates:
    - name: Surplus Mod
      pick_rate: 0.36
      win_rate: 0.63
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.32
    win_rate: 0.6
  - name: Sands Of Time
    pick_rate: 0.25
    win_rate: 0.45
  - name: Archmage's Gem
    pick_rate: 0.22
    win_rate: 0.71
  source_url: https://smitebrain.com/gods/vulcan/
  last_verified: '2026-08-18'
  god_win_rate: 0.5467289719626168
  god_matches_won: 234
  god_matches_played: 428
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-18'
  god_matches_analyzed: 8839
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - The Cosmic Horror
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Chronos' Pendant
  - The Cosmic Horror
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Nimble Ring, Chronos'' Pendant, The Cosmic Horror,
    Spear of the Magus, Genji''s Guard, Doom Orb, Bracer of The Abyss, Dreamer''s
    Idol, Gem of Focus, Breastplate of Valor, Death Metal, Helm of Radiance, Totem
    of Death, Blood-Bound Book, Rod of Asclepius, Bragi''s Harp, Bancroft''s Talon,
    Jade Scepter, Freya''s Tears, Ethereal Staff, Alchemist Coat.'
  slot_scores:
    Chronos' Pendant:
      total: 0.56
      efficiency: 0.55
      win: 0.63
      pick: 0.06
      fit: 0.52
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.55
      pick: 0.35
      fit: 0.83
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.77
      win: 0.59
      pick: 0.3
      fit: 0.66
    Obsidian Shard:
      total: 0.57
      efficiency: 0.52
      win: 0.59
      pick: 0.52
      fit: 0.66
    Soul Gem:
      total: 0.62
      efficiency: 0.57
      win: 0.61
      pick: 0.22
      fit: 0.93
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Gluttonous
    Grimoire, Nimble Ring, Chronos'' Pendant, Genji''s Guard, Death Metal, The Cosmic
    Horror, Spear of the Magus, Breastplate of Valor, Bragi''s Harp, Doom Orb, Bancroft''s
    Talon, Helm of Radiance, Bracer of The Abyss, Blood-Bound Book, Rod of Asclepius,
    Triton''s Conch, Gem of Focus, Oni Hunter''s Garb, Freya''s Tears, Totem of Death,
    Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.55
      pick: 0.0
      fit: 0.22
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.64
      win: 0.55
      pick: 0.0
      fit: 0.22
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.55
      win: 0.63
      pick: 0.06
      fit: 0.39
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.59
      pick: 0.3
      fit: 0.52
    Obsidian Shard:
      total: 0.54
      efficiency: 0.52
      win: 0.59
      pick: 0.52
      fit: 0.43
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.61
      pick: 0.22
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - The Cosmic Horror
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Chronos' Pendant
  - The Cosmic Horror
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Chronos'' Pendant, Nimble Ring, The Cosmic Horror, Spear
    of the Magus, Genji''s Guard, Death Metal, Breastplate of Valor, Doom Orb, Bragi''s
    Harp, Freya''s Tears, Gem of Focus, Dreamer''s Idol, Shield of the Phoenix, Totem
    of Death, Helm of Radiance, Bracer of The Abyss, Kinetic Cuirass, Blood-Bound
    Book, Rod of Asclepius, Amanita Charm, Screeching Gargoyle.'
  slot_scores:
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.55
      win: 0.63
      pick: 0.06
      fit: 0.4
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.55
      pick: 0.35
      fit: 0.7
    The Cosmic Horror:
      total: 0.53
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.77
      win: 0.59
      pick: 0.3
      fit: 0.5
    Obsidian Shard:
      total: 0.55
      efficiency: 0.52
      win: 0.59
      pick: 0.52
      fit: 0.5
    Soul Gem:
      total: 0.6
      efficiency: 0.57
      win: 0.61
      pick: 0.22
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Shield of the Phoenix, Kinetic Cuirass,
    Rod of Asclepius, Nimble Ring, Genji''s Guard, Chandra''s Grace, Blood-Bound Book,
    Oni Hunter''s Garb, Freya''s Tears, Bancroft''s Talon, Lifebinder, Breastplate
    of Valor, The Cosmic Horror, Phoenix Feather, Spear of the Magus, Erosion, Spectral
    Armor, Shifter''s Shield, Eye of Providence, Helm of Radiance, Draconic Scale,
    Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.55
      pick: 0.0
      fit: 0.24
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.77
      win: 0.59
      pick: 0.3
      fit: 0.36
    Obsidian Shard:
      total: 0.53
      efficiency: 0.52
      win: 0.59
      pick: 0.52
      fit: 0.36
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.76
    Soul Gem:
      total: 0.61
      efficiency: 0.57
      win: 0.61
      pick: 0.22
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus, Nimble
    Ring, Chronos'' Pendant, Doom Orb, Dreamer''s Idol, Genji''s Guard, Screeching
    Gargoyle, Breastplate of Valor, Bracer of The Abyss, Death Metal, Helm of Radiance,
    Blood-Bound Book, Rod of Asclepius, Gem of Focus, Stone of Binding, Bancroft''s
    Talon, Freya''s Tears, Totem of Death, Jade Scepter, Kinetic Cuirass.'
  slot_scores:
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.55
      pick: 0.35
      fit: 0.88
    The Cosmic Horror:
      total: 0.56
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.75
    Spear of the Magus:
      total: 0.56
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.75
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.77
      win: 0.59
      pick: 0.3
      fit: 0.75
    Obsidian Shard:
      total: 0.59
      efficiency: 0.52
      win: 0.59
      pick: 0.52
      fit: 0.75
    Soul Gem:
      total: 0.63
      efficiency: 0.57
      win: 0.61
      pick: 0.22
      fit: 0.98
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Gluttonous Grimoire, Chronos'' Pendant, Genji''s Guard,
    The Cosmic Horror, Spear of the Magus, Bragi''s Harp, Death Metal, Bracer of The
    Abyss, Breastplate of Valor, Blood-Bound Book, Bancroft''s Talon, Kinetic Cuirass,
    Amanita Charm, Helm of Radiance, Freya''s Tears, Rod of Asclepius, Eye of Providence,
    Oni Hunter''s Garb, Shield of the Phoenix, Jade Scepter, Doom Orb, Gem of Focus.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.56
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.49
      efficiency: 0.42
      win: 0.55
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.77
      win: 0.59
      pick: 0.3
      fit: 0.32
    Obsidian Shard:
      total: 0.52
      efficiency: 0.52
      win: 0.59
      pick: 0.52
      fit: 0.32
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.61
      pick: 0.22
      fit: 0.58
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
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Chronos'' Pendant, Genji''s Guard,
    Breastplate of Valor, Gluttonous Grimoire, Nimble Ring, Freya''s Tears, Shield
    of the Phoenix, Gem of Focus, The Cosmic Horror, Screeching Gargoyle, Totem of
    Death, Chandra''s Grace, Spear of the Magus, Death Metal, Gladiator''s Shield,
    Kinetic Cuirass, Amanita Charm, Bragi''s Harp, Eye of Providence, Oni Hunter''s
    Garb, Bracer of The Abyss, Prophetic Cloak, Helm of Radiance.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.55
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.64
      win: 0.55
      pick: 0.0
      fit: 0.43
    Chronos' Pendant:
      total: 0.56
      efficiency: 0.55
      win: 0.63
      pick: 0.06
      fit: 0.56
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.55
      pick: 0.35
      fit: 0.76
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.77
      win: 0.59
      pick: 0.3
      fit: 0.33
    Soul Gem:
      total: 0.61
      efficiency: 0.57
      win: 0.61
      pick: 0.22
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Nimble Ring, The Cosmic Horror,
    Spear of the Magus, Chronos'' Pendant, Genji''s Guard, Doom Orb, Bracer of The
    Abyss, Dreamer''s Idol, Gem of Focus, Breastplate of Valor, Death Metal, Helm
    of Radiance, Totem of Death, Blood-Bound Book, Rod of Asclepius, Bragi''s Harp,
    Bancroft''s Talon, Jade Scepter, Freya''s Tears, Ethereal Staff, Alchemist Coat.'
  slot_scores:
    Nimble Ring:
      total: 0.56
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.51
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.55
      pick: 0.35
      fit: 0.83
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.66
    Spear of the Magus:
      total: 0.55
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.77
      win: 0.59
      pick: 0.3
      fit: 0.66
    Obsidian Shard:
      total: 0.57
      efficiency: 0.52
      win: 0.59
      pick: 0.52
      fit: 0.66
  starter: *id001
---

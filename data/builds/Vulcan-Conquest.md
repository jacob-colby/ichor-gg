---
type: smite-build
god: Vulcan
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fortification
  aspect_pick_rate: 0.11
  aspect_win_rate: 0.65
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.41
    win_rate: 0.53
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.3
      win_rate: 0.52
    - name: Chronos' Pendant
      pick_rate: 0.06
      win_rate: 0.7
  - name: Spear of Desolation
    pick_rate: 0.34
    win_rate: 0.49
    alternates:
    - name: Book of Thoth
      pick_rate: 0.15
      win_rate: 0.58
    - name: The World Stone
      pick_rate: 0.11
      win_rate: 0.47
  - name: Rod of Tahuti
    pick_rate: 0.21
    win_rate: 0.66
    alternates:
    - name: Soul Gem
      pick_rate: 0.18
      win_rate: 0.48
    - name: The World Stone
      pick_rate: 0.09
      win_rate: 0.67
  - name: Obsidian Shard
    pick_rate: 0.36
    win_rate: 0.62
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.21
      win_rate: 0.54
    - name: Soul Reaver
      pick_rate: 0.05
      win_rate: 0.38
  - name: Evil Eye
    pick_rate: 0.1
    win_rate: 0.33
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.16
      win_rate: 0.63
    - name: Obsidian Shard
      pick_rate: 0.14
      win_rate: 0.71
  - name: Oracle Staff
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Evil Eye
      pick_rate: 0.08
      win_rate: 0.44
    - name: Shrapnel Mod
      pick_rate: 0.08
      win_rate: 0.33
  - name: Shrapnel Mod
    pick_rate: 0.44
    win_rate: 0.5
    alternates:
    - name: Surplus Mod
      pick_rate: 0.31
      win_rate: 0.18
    - name: Thermal Mod
      pick_rate: 0.11
      win_rate: 1.0
  - name: Surplus Mod
    pick_rate: 0.8
    win_rate: 0.56
    alternates:
    - name: Masterwork Mod
      pick_rate: 0.15
      win_rate: 0.67
    - name: Thermal Mod
      pick_rate: 0.05
      win_rate: 1.0
  - name: Seismic Mod
    pick_rate: 1.0
    win_rate: 1.0
  community_starters:
  - name: Pendulum of The Ages
    pick_rate: 0.3
    win_rate: 0.63
  - name: Sands of Time
    pick_rate: 0.25
    win_rate: 0.42
  - name: Archmage's Gem
    pick_rate: 0.23
    win_rate: 0.75
  source_url: https://smitebrain.com/gods/vulcan/
  last_verified: '2026-08-14'
  god_win_rate: 0.5428571428571428
  god_matches_won: 95
  god_matches_played: 175
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-14'
  god_matches_analyzed: 3454
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Chronos' Pendant
  - Gluttonous Grimoire
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of Desolation
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Chronos'' Pendant, Gluttonous Grimoire, Spear of the Magus, The Cosmic
    Horror, Genji''s Guard, Bracer of The Abyss, Doom Orb, Dreamer''s Idol, Breastplate
    of Valor, Blood-Bound Book, Gem of Focus, Bancroft''s Talon, Helm of Radiance,
    Death Metal, Rod of Asclepius, Nimble Ring, Jade Scepter, Bragi''s Harp, Ancient
    Signet, Polynomicon, Ethereal Staff, Wish-Granting Pearl.'
  slot_scores:
    Chronos' Pendant:
      total: 0.59
      efficiency: 0.56
      win: 0.7
      pick: 0.06
      fit: 0.52
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.76
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.49
      pick: 0.46
      fit: 0.83
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.44
      win: 0.66
      pick: 0.33
      fit: 0.66
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.62
      pick: 0.6
      fit: 0.66
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Chronos' Pendant
  - Gluttonous Grimoire
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of Desolation
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Chronos'' Pendant, Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror,
    Genji''s Guard, Death Metal, Breastplate of Valor, Doom Orb, Dreamer''s Idol,
    Bragi''s Harp, Bracer of The Abyss, Gem of Focus, Freya''s Tears, Blood-Bound
    Book, Bancroft''s Talon, Helm of Radiance, Shield of the Phoenix, Rod of Asclepius,
    Jade Scepter, Kinetic Cuirass, Amanita Charm, Oni Hunter''s Garb.'
  slot_scores:
    Chronos' Pendant:
      total: 0.57
      efficiency: 0.56
      win: 0.7
      pick: 0.06
      fit: 0.4
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.6
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.49
      pick: 0.46
      fit: 0.7
    Spear of the Magus:
      total: 0.52
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.44
      win: 0.66
      pick: 0.33
      fit: 0.5
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.62
      pick: 0.6
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Chronos' Pendant
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Shield of the Phoenix, Rod of Asclepius,
    Kinetic Cuirass, Genji''s Guard, Blood-Bound Book, Bancroft''s Talon, Chandra''s
    Grace, Oni Hunter''s Garb, Breastplate of Valor, Spear of the Magus, Lifebinder,
    Freya''s Tears, The Cosmic Horror, Phoenix Feather, Helm of Radiance, Shifter''s
    Shield, Spectral Armor, Erosion, Jade Scepter, Eye of Providence, Draconic Scale,
    Sphere of Negation.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.53
      pick: 0.0
      fit: 0.24
    Chronos' Pendant:
      total: 0.56
      efficiency: 0.56
      win: 0.7
      pick: 0.06
      fit: 0.28
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.56
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.63
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.62
      pick: 0.6
      fit: 0.36
    Amanita Charm:
      total: 0.57
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.76
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Chronos' Pendant
  - Gluttonous Grimoire
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
  - Spear of Desolation
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
    for this god: Gluttonous Grimoire, Chronos'' Pendant, Spear of the Magus, The
    Cosmic Horror, Doom Orb, Dreamer''s Idol, Genji''s Guard, Bracer of The Abyss,
    Screeching Gargoyle, Breastplate of Valor, Blood-Bound Book, Bancroft''s Talon,
    Helm of Radiance, Death Metal, Rod of Asclepius, Gem of Focus, Jade Scepter, Stone
    of Binding, Ancient Signet, Nimble Ring, Bragi''s Harp, Freya''s Tears.'
  slot_scores:
    Chronos' Pendant:
      total: 0.57
      efficiency: 0.56
      win: 0.7
      pick: 0.06
      fit: 0.39
    Gluttonous Grimoire:
      total: 0.6
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.85
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.49
      pick: 0.46
      fit: 0.88
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.75
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.44
      win: 0.66
      pick: 0.33
      fit: 0.75
    Obsidian Shard:
      total: 0.61
      efficiency: 0.54
      win: 0.62
      pick: 0.6
      fit: 0.75
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Chronos' Pendant
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  - Obsidian Shard
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
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
    this god: Chronos'' Pendant, Gluttonous Grimoire, Genji''s Guard, Spear of the
    Magus, Bracer of The Abyss, The Cosmic Horror, Bragi''s Harp, Death Metal, Breastplate
    of Valor, Nimble Ring, Blood-Bound Book, Bancroft''s Talon, Helm of Radiance,
    Rod of Asclepius, Kinetic Cuirass, Amanita Charm, Jade Scepter, Oni Hunter''s
    Garb, Doom Orb, Freya''s Tears, Dreamer''s Idol, Eye of Providence, Gem of Focus.'
  slot_scores:
    Chronos' Pendant:
      total: 0.55
      efficiency: 0.56
      win: 0.7
      pick: 0.06
      fit: 0.25
    Bracer of The Abyss:
      total: 0.5
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.48
      efficiency: 0.49
      win: 0.53
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.49
      efficiency: 0.44
      win: 0.53
      pick: 0.0
      fit: 0.63
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.49
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.62
      pick: 0.6
      fit: 0.32
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Spear of Desolation
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of Desolation
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
    Gluttonous Grimoire, Breastplate of Valor, Freya''s Tears, Shield of the Phoenix,
    Gem of Focus, Spear of the Magus, The Cosmic Horror, Screeching Gargoyle, Chandra''s
    Grace, Death Metal, Bracer of The Abyss, Gladiator''s Shield, Blood-Bound Book,
    Bragi''s Harp, Kinetic Cuirass, Bancroft''s Talon, Helm of Radiance, Amanita Charm,
    Doom Orb, Oni Hunter''s Garb, Dreamer''s Idol.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.53
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.43
    Chronos' Pendant:
      total: 0.6
      efficiency: 0.56
      win: 0.7
      pick: 0.06
      fit: 0.56
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.49
      pick: 0.46
      fit: 0.76
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.62
      pick: 0.6
      fit: 0.33
    Soul Gem:
      total: 0.57
      efficiency: 0.59
      win: 0.48
      pick: 0.28
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror,
    Genji''s Guard, Bracer of The Abyss, Chronos'' Pendant, Doom Orb, Dreamer''s Idol,
    Breastplate of Valor, Blood-Bound Book, Gem of Focus, Bancroft''s Talon, Helm
    of Radiance, Death Metal, Rod of Asclepius, Nimble Ring, Jade Scepter, Bragi''s
    Harp, Ancient Signet, Polynomicon, Ethereal Staff, Wish-Granting Pearl.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.53
      pick: 0.0
      fit: 0.17
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.49
      pick: 0.46
      fit: 0.83
    The Cosmic Horror:
      total: 0.54
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.66
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.66
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.62
      pick: 0.6
      fit: 0.66
    Soul Gem:
      total: 0.58
      efficiency: 0.59
      win: 0.48
      pick: 0.28
      fit: 0.93
  starter: *id001
---

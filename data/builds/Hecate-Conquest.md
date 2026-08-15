---
type: smite-build
god: Hecate
mode: Conquest
builds:
- source: community
  aspect: Aspect of Ruin
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.63
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.52
    win_rate: 0.45
    alternates:
    - name: Book of Thoth
      pick_rate: 0.16
      win_rate: 0.65
    - name: Chronos' Pendant
      pick_rate: 0.13
      win_rate: 0.71
  - name: Book of Thoth
    pick_rate: 0.22
    win_rate: 0.39
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.18
      win_rate: 0.68
    - name: The World Stone
      pick_rate: 0.12
      win_rate: 0.38
  - name: The World Stone
    pick_rate: 0.2
    win_rate: 0.55
    alternates:
    - name: Soul Gem
      pick_rate: 0.16
      win_rate: 0.44
    - name: Gem of Focus
      pick_rate: 0.07
      win_rate: 0.29
  - name: Rod of Tahuti
    pick_rate: 0.3
    win_rate: 0.59
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.19
      win_rate: 0.44
    - name: Void Shard
      pick_rate: 0.05
      win_rate: 0.4
  - name: Obsidian Shard
    pick_rate: 0.21
    win_rate: 0.44
    alternates:
    - name: Evil Eye
      pick_rate: 0.17
      win_rate: 0.62
    - name: Rod of Tahuti
      pick_rate: 0.16
      win_rate: 0.58
  - name: Blinking Abyss
    pick_rate: 0.13
    win_rate: 0.6
    alternates:
    - name: Evil Eye
      pick_rate: 0.1
      win_rate: 0.25
    - name: Void Shard
      pick_rate: 0.08
      win_rate: 0.33
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.24
    win_rate: 0.6
  - name: Conduit Gem
    pick_rate: 0.21
    win_rate: 0.68
  - name: Pendulum of the Ages
    pick_rate: 0.15
    win_rate: 0.31
  source_url: https://smitebrain.com/gods/hecate/
  last_verified: '2026-08-14'
  god_win_rate: 0.5523809523809524
  god_matches_won: 58
  god_matches_played: 105
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
  - Nimble Ring
  - Spear of Desolation
  - The Cosmic Horror
  - The World Stone
  - Rod of Tahuti
  flex_slots:
  - The Cosmic Horror
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Chronos'' Pendant, Gluttonous Grimoire, The Cosmic Horror, Spear of
    the Magus, Nimble Ring, Doom Orb, Genji''s Guard, Dreamer''s Idol, Totem of Death,
    Death Metal, Breastplate of Valor, Helm of Radiance, Blood-Bound Book, Rod of
    Asclepius, Bancroft''s Talon, Jade Scepter, Freya''s Tears, Bracer of The Abyss,
    Ethereal Staff, Alchemist Coat, Gem of Focus.'
  slot_scores:
    Chronos' Pendant:
      total: 0.61
      efficiency: 0.55
      win: 0.71
      pick: 0.13
      fit: 0.64
    Nimble Ring:
      total: 0.5
      efficiency: 0.68
      win: 0.45
      pick: 0.0
      fit: 0.41
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.45
      pick: 0.52
      fit: 1.0
    The Cosmic Horror:
      total: 0.52
      efficiency: 0.58
      win: 0.45
      pick: 0.0
      fit: 0.77
    The World Stone:
      total: 0.54
      efficiency: 0.46
      win: 0.55
      pick: 0.31
      fit: 0.77
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.77
      win: 0.59
      pick: 0.5
      fit: 0.77
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Chronos' Pendant
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Chronos''
    Pendant, Gluttonous Grimoire, Nimble Ring, Death Metal, Genji''s Guard, The Cosmic
    Horror, Spear of the Magus, Breastplate of Valor, Doom Orb, Bragi''s Harp, Bancroft''s
    Talon, Triton''s Conch, Helm of Radiance, Blood-Bound Book, Rod of Asclepius,
    Totem of Death, Oni Hunter''s Garb, Polynomicon, Jade Scepter, Freya''s Tears,
    Gem of Focus.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.69
      win: 0.45
      pick: 0.0
      fit: 0.24
    Chronos' Pendant:
      total: 0.58
      efficiency: 0.55
      win: 0.71
      pick: 0.13
      fit: 0.43
    Spear of Desolation:
      total: 0.5
      efficiency: 0.52
      win: 0.45
      pick: 0.52
      fit: 0.61
    The World Stone:
      total: 0.51
      efficiency: 0.46
      win: 0.55
      pick: 0.31
      fit: 0.57
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.59
      pick: 0.5
      fit: 0.57
    Soul Gem:
      total: 0.52
      efficiency: 0.57
      win: 0.44
      pick: 0.25
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - The Cosmic Horror
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - The World Stone
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
    god: Chronos'' Pendant, Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus,
    Genji''s Guard, Nimble Ring, Death Metal, Breastplate of Valor, Doom Orb, Freya''s
    Tears, Dreamer''s Idol, Totem of Death, Shield of the Phoenix, Bragi''s Harp,
    Helm of Radiance, Blood-Bound Book, Rod of Asclepius, Kinetic Cuirass, Amanita
    Charm, Screeching Gargoyle, Triton''s Conch, Gem of Focus.'
  slot_scores:
    Chronos' Pendant:
      total: 0.58
      efficiency: 0.55
      win: 0.71
      pick: 0.13
      fit: 0.44
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.45
      pick: 0.52
      fit: 0.78
    The Cosmic Horror:
      total: 0.49
      efficiency: 0.58
      win: 0.45
      pick: 0.0
      fit: 0.56
    The World Stone:
      total: 0.51
      efficiency: 0.46
      win: 0.55
      pick: 0.31
      fit: 0.56
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.59
      pick: 0.5
      fit: 0.56
    Soul Gem:
      total: 0.54
      efficiency: 0.57
      win: 0.44
      pick: 0.25
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Chronos' Pendant
  - Kinetic Cuirass
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Shield of the Phoenix, Kinetic Cuirass,
    Rod of Asclepius, Genji''s Guard, Chandra''s Grace, Nimble Ring, Freya''s Tears,
    Blood-Bound Book, Oni Hunter''s Garb, Lifebinder, Breastplate of Valor, Bancroft''s
    Talon, The Cosmic Horror, Spear of the Magus, Phoenix Feather, Erosion, Shifter''s
    Shield, Spectral Armor, Eye of Providence, Draconic Scale, Helm of Radiance, Jade
    Scepter.'
  slot_scores:
    Chronos' Pendant:
      total: 0.57
      efficiency: 0.55
      win: 0.71
      pick: 0.13
      fit: 0.32
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.59
      win: 0.45
      pick: 0.0
      fit: 0.6
    Spear of Desolation:
      total: 0.49
      efficiency: 0.52
      win: 0.45
      pick: 0.52
      fit: 0.5
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.77
      win: 0.59
      pick: 0.5
      fit: 0.38
    Amanita Charm:
      total: 0.54
      efficiency: 0.63
      win: 0.45
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.54
      efficiency: 0.57
      win: 0.44
      pick: 0.25
      fit: 0.9
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Chronos' Pendant
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - The World Stone
  - Rod of Tahuti
  flex_slots:
  - The World Stone
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Chronos'' Pendant, Gluttonous Grimoire, The Cosmic Horror, Spear
    of the Magus, Doom Orb, Nimble Ring, Dreamer''s Idol, Genji''s Guard, Screeching
    Gargoyle, Breastplate of Valor, Death Metal, Helm of Radiance, Blood-Bound Book,
    Rod of Asclepius, Totem of Death, Freya''s Tears, Bancroft''s Talon, Jade Scepter,
    Stone of Binding, Shield of the Phoenix, Kinetic Cuirass, Gem of Focus.'
  slot_scores:
    Chronos' Pendant:
      total: 0.59
      efficiency: 0.55
      win: 0.71
      pick: 0.13
      fit: 0.45
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.63
      win: 0.45
      pick: 0.0
      fit: 0.94
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.45
      pick: 0.52
      fit: 1.0
    The Cosmic Horror:
      total: 0.53
      efficiency: 0.58
      win: 0.45
      pick: 0.0
      fit: 0.84
    The World Stone:
      total: 0.55
      efficiency: 0.46
      win: 0.55
      pick: 0.31
      fit: 0.84
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.77
      win: 0.59
      pick: 0.5
      fit: 0.84
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Chronos' Pendant
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
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
    this god: Chronos'' Pendant, Nimble Ring, Gluttonous Grimoire, Genji''s Guard,
    The Cosmic Horror, Spear of the Magus, Death Metal, Bragi''s Harp, Bracer of The
    Abyss, Breastplate of Valor, Blood-Bound Book, Bancroft''s Talon, Kinetic Cuirass,
    Amanita Charm, Freya''s Tears, Helm of Radiance, Rod of Asclepius, Eye of Providence,
    Oni Hunter''s Garb, Shield of the Phoenix, Jade Scepter, Doom Orb, Gem of Focus.'
  slot_scores:
    Chronos' Pendant:
      total: 0.56
      efficiency: 0.55
      win: 0.71
      pick: 0.13
      fit: 0.26
    Bracer of The Abyss:
      total: 0.44
      efficiency: 0.51
      win: 0.45
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.51
      efficiency: 0.68
      win: 0.45
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.44
      efficiency: 0.42
      win: 0.45
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.59
      pick: 0.5
      fit: 0.31
    Soul Gem:
      total: 0.5
      efficiency: 0.57
      win: 0.44
      pick: 0.25
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
    Breastplate of Valor, Gluttonous Grimoire, Freya''s Tears, Shield of the Phoenix,
    Nimble Ring, Totem of Death, The Cosmic Horror, Screeching Gargoyle, Chandra''s
    Grace, Spear of the Magus, Death Metal, Gladiator''s Shield, Kinetic Cuirass,
    Prophetic Cloak, Amanita Charm, Doom Orb, Helm of Radiance, Eye of Providence,
    Oni Hunter''s Garb, Gem of Focus.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.45
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.64
      win: 0.45
      pick: 0.0
      fit: 0.48
    Chronos' Pendant:
      total: 0.61
      efficiency: 0.55
      win: 0.71
      pick: 0.13
      fit: 0.63
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.45
      pick: 0.52
      fit: 0.86
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.59
      pick: 0.5
      fit: 0.37
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.44
      pick: 0.25
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Gluttonous Grimoire
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
    Underrated for this god: Gluttonous Grimoire, The Cosmic Horror, Spear of the
    Magus, Nimble Ring, Chronos'' Pendant, Doom Orb, Genji''s Guard, Dreamer''s Idol,
    Gem of Focus, Totem of Death, Death Metal, Breastplate of Valor, Helm of Radiance,
    Blood-Bound Book, Rod of Asclepius, Bancroft''s Talon, Jade Scepter, Freya''s
    Tears, Bracer of The Abyss, Ethereal Staff, Alchemist Coat.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.63
      win: 0.45
      pick: 0.0
      fit: 0.87
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.45
      pick: 0.52
      fit: 1.0
    The Cosmic Horror:
      total: 0.52
      efficiency: 0.58
      win: 0.45
      pick: 0.0
      fit: 0.77
    Spear of the Magus:
      total: 0.52
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.77
      win: 0.59
      pick: 0.5
      fit: 0.77
    Obsidian Shard:
      total: 0.52
      efficiency: 0.52
      win: 0.44
      pick: 0.45
      fit: 0.77
  starter: *id001
---

---
type: smite-build
god: Hecate
mode: Conquest
builds:
- source: community
  aspect: Aspect of Ruin
  aspect_pick_rate: 0.13
  aspect_win_rate: 0.65
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.56
    win_rate: 0.54
    alternates:
    - name: Book of Thoth
      pick_rate: 0.2
      win_rate: 0.59
    - name: Chronos' Pendant
      pick_rate: 0.09
      win_rate: 0.71
  - name: Book of Thoth
    pick_rate: 0.23
    win_rate: 0.43
    alternates:
    - name: The World Stone
      pick_rate: 0.17
      win_rate: 0.59
    - name: Spear of Desolation
      pick_rate: 0.17
      win_rate: 0.59
  - name: Soul Gem
    pick_rate: 0.24
    win_rate: 0.51
    alternates:
    - name: The World Stone
      pick_rate: 0.14
      win_rate: 0.54
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.47
  - name: Rod of Tahuti
    pick_rate: 0.33
    win_rate: 0.63
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.2
      win_rate: 0.46
    - name: The World Stone
      pick_rate: 0.06
      win_rate: 0.55
  - name: Obsidian Shard
    pick_rate: 0.18
    win_rate: 0.56
    alternates:
    - name: Evil Eye
      pick_rate: 0.13
      win_rate: 0.5
    - name: Rod of Tahuti
      pick_rate: 0.13
      win_rate: 0.47
  - name: Evil Eye
    pick_rate: 0.1
    win_rate: 0.56
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.09
      win_rate: 0.75
    - name: Void Shard
      pick_rate: 0.09
      win_rate: 0.25
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.25
    win_rate: 0.62
  - name: Conduit Gem
    pick_rate: 0.2
    win_rate: 0.68
  - name: Pendulum of the Ages
    pick_rate: 0.19
    win_rate: 0.54
  source_url: https://smitebrain.com/gods/hecate/
  last_verified: '2026-08-17'
  god_win_rate: 0.57
  god_matches_won: 114
  god_matches_played: 200
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-17'
  god_matches_analyzed: 7467
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
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
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
    the Magus, Nimble Ring, Doom Orb, Genji''s Guard, Dreamer''s Idol, Gem of Focus,
    Totem of Death, Death Metal, Breastplate of Valor, Helm of Radiance, Blood-Bound
    Book, Rod of Asclepius, Bancroft''s Talon, Jade Scepter, Freya''s Tears, Bracer
    of The Abyss, Ethereal Staff, Alchemist Coat.'
  slot_scores:
    Chronos' Pendant:
      total: 0.61
      efficiency: 0.55
      win: 0.71
      pick: 0.09
      fit: 0.64
    Nimble Ring:
      total: 0.55
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.41
    Spear of Desolation:
      total: 0.6
      efficiency: 0.52
      win: 0.54
      pick: 0.56
      fit: 1.0
    The Cosmic Horror:
      total: 0.57
      efficiency: 0.58
      win: 0.56
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.77
      win: 0.63
      pick: 0.55
      fit: 0.77
    Obsidian Shard:
      total: 0.57
      efficiency: 0.52
      win: 0.56
      pick: 0.39
      fit: 0.77
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Chronos' Pendant
  - Gluttonous Grimoire
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  flex_slots:
  - Genji's Guard
  - The World Stone
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
    Talon, Triton''s Conch, Helm of Radiance, Gem of Focus, Blood-Bound Book, Rod
    of Asclepius, Totem of Death, Oni Hunter''s Garb, Polynomicon, Jade Scepter, Freya''s
    Tears.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.56
      pick: 0.0
      fit: 0.24
    Chronos' Pendant:
      total: 0.58
      efficiency: 0.55
      win: 0.71
      pick: 0.09
      fit: 0.43
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.57
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.54
      pick: 0.56
      fit: 0.61
    The World Stone:
      total: 0.52
      efficiency: 0.46
      win: 0.59
      pick: 0.23
      fit: 0.57
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.77
      win: 0.63
      pick: 0.55
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Chronos' Pendant
  - Nimble Ring
  - Spear of Desolation
  - The Cosmic Horror
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Chronos'' Pendant, Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus,
    Genji''s Guard, Nimble Ring, Death Metal, Breastplate of Valor, Doom Orb, Freya''s
    Tears, Gem of Focus, Dreamer''s Idol, Totem of Death, Shield of the Phoenix, Bragi''s
    Harp, Helm of Radiance, Blood-Bound Book, Rod of Asclepius, Kinetic Cuirass, Amanita
    Charm, Screeching Gargoyle, Triton''s Conch.'
  slot_scores:
    Chronos' Pendant:
      total: 0.58
      efficiency: 0.55
      win: 0.71
      pick: 0.09
      fit: 0.44
    Nimble Ring:
      total: 0.52
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.22
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.54
      pick: 0.56
      fit: 0.78
    The Cosmic Horror:
      total: 0.54
      efficiency: 0.58
      win: 0.56
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.77
      win: 0.63
      pick: 0.55
      fit: 0.56
    Obsidian Shard:
      total: 0.54
      efficiency: 0.52
      win: 0.56
      pick: 0.39
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Chronos' Pendant
  - Kinetic Cuirass
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
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
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.56
      pick: 0.0
      fit: 0.27
    Chronos' Pendant:
      total: 0.56
      efficiency: 0.55
      win: 0.71
      pick: 0.09
      fit: 0.32
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.6
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.63
      pick: 0.55
      fit: 0.38
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.51
      pick: 0.37
      fit: 0.9
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Chronos' Pendant
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - The Cosmic Horror
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Chronos'' Pendant, The Cosmic Horror, Spear
    of the Magus, Doom Orb, Nimble Ring, Dreamer''s Idol, Genji''s Guard, Screeching
    Gargoyle, Breastplate of Valor, Death Metal, Gem of Focus, Helm of Radiance, Blood-Bound
    Book, Rod of Asclepius, Totem of Death, Freya''s Tears, Bancroft''s Talon, Jade
    Scepter, Stone of Binding, Shield of the Phoenix, Kinetic Cuirass.'
  slot_scores:
    Chronos' Pendant:
      total: 0.58
      efficiency: 0.55
      win: 0.71
      pick: 0.09
      fit: 0.45
    Gluttonous Grimoire:
      total: 0.61
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.94
    Spear of Desolation:
      total: 0.6
      efficiency: 0.52
      win: 0.54
      pick: 0.56
      fit: 1.0
    The Cosmic Horror:
      total: 0.58
      efficiency: 0.58
      win: 0.56
      pick: 0.0
      fit: 0.84
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.77
      win: 0.63
      pick: 0.55
      fit: 0.84
    Obsidian Shard:
      total: 0.58
      efficiency: 0.52
      win: 0.56
      pick: 0.39
      fit: 0.84
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Chronos' Pendant
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  - Rod of Tahuti
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
    this god: Nimble Ring, Chronos'' Pendant, Gluttonous Grimoire, Genji''s Guard,
    The Cosmic Horror, Spear of the Magus, Death Metal, Bragi''s Harp, Bracer of The
    Abyss, Breastplate of Valor, Blood-Bound Book, Bancroft''s Talon, Kinetic Cuirass,
    Amanita Charm, Freya''s Tears, Helm of Radiance, Rod of Asclepius, Eye of Providence,
    Oni Hunter''s Garb, Shield of the Phoenix, Gem of Focus, Jade Scepter, Doom Orb.'
  slot_scores:
    Chronos' Pendant:
      total: 0.55
      efficiency: 0.55
      win: 0.71
      pick: 0.09
      fit: 0.26
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.56
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.49
      efficiency: 0.42
      win: 0.56
      pick: 0.0
      fit: 0.62
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.63
      pick: 0.55
      fit: 0.31
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
    Gem of Focus, Nimble Ring, Totem of Death, The Cosmic Horror, Screeching Gargoyle,
    Chandra''s Grace, Spear of the Magus, Death Metal, Gladiator''s Shield, Kinetic
    Cuirass, Prophetic Cloak, Amanita Charm, Doom Orb, Helm of Radiance, Eye of Providence,
    Oni Hunter''s Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.56
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.64
      win: 0.56
      pick: 0.0
      fit: 0.48
    Chronos' Pendant:
      total: 0.61
      efficiency: 0.55
      win: 0.71
      pick: 0.09
      fit: 0.63
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.54
      pick: 0.56
      fit: 0.86
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.63
      pick: 0.55
      fit: 0.37
    Soul Gem:
      total: 0.59
      efficiency: 0.57
      win: 0.51
      pick: 0.37
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
      total: 0.6
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.87
    Spear of Desolation:
      total: 0.6
      efficiency: 0.52
      win: 0.54
      pick: 0.56
      fit: 1.0
    The Cosmic Horror:
      total: 0.57
      efficiency: 0.58
      win: 0.56
      pick: 0.0
      fit: 0.77
    Spear of the Magus:
      total: 0.57
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.77
      win: 0.63
      pick: 0.55
      fit: 0.77
    Obsidian Shard:
      total: 0.57
      efficiency: 0.52
      win: 0.56
      pick: 0.39
      fit: 0.77
  starter: *id001
---

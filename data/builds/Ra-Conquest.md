---
type: smite-build
god: Ra
mode: Conquest
builds:
- source: community
  aspect: Aspect of Thermotherapy
  aspect_pick_rate: 0.06
  aspect_win_rate: 1.0
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.52
    win_rate: 0.54
    alternates:
    - name: Book of Thoth
      pick_rate: 0.27
      win_rate: 0.43
    - name: Divine Ruin
      pick_rate: 0.04
      win_rate: 0.86
  - name: The World Stone
    pick_rate: 0.34
    win_rate: 0.53
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.25
      win_rate: 0.49
    - name: Book of Thoth
      pick_rate: 0.12
      win_rate: 0.68
  - name: Rod of Tahuti
    pick_rate: 0.35
    win_rate: 0.58
    alternates:
    - name: The World Stone
      pick_rate: 0.17
      win_rate: 0.46
    - name: Soul Gem
      pick_rate: 0.07
      win_rate: 0.36
  - name: Nimble Ring
    pick_rate: 0.25
    win_rate: 0.62
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.27
      win_rate: 0.45
    - name: Obsidian Shard
      pick_rate: 0.17
      win_rate: 0.44
  - name: Obsidian Shard
    pick_rate: 0.21
    win_rate: 0.61
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.64
    - name: Evil Eye
      pick_rate: 0.1
      win_rate: 0.38
  - name: Blinking Abyss
    pick_rate: 0.15
    win_rate: 0.45
    alternates:
    - name: Evil Eye
      pick_rate: 0.11
      win_rate: 0.5
    - name: Obsidian Shard
      pick_rate: 0.11
      win_rate: 0.63
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.4
    win_rate: 0.45
  - name: Pendulum of the Ages
    pick_rate: 0.29
    win_rate: 0.67
  - name: Conduit Gem
    pick_rate: 0.18
    win_rate: 0.47
  source_url: https://smitebrain.com/gods/ra/
  last_verified: '2026-10-22'
  god_win_rate: 0.5214723926380368
  god_matches_won: 85
  god_matches_played: 163
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-22'
  god_matches_analyzed: 1760
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Divine Ruin
  - Spear of Desolation
  - Nimble Ring
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Divine Ruin, Spear of the Magus, Gluttonous Grimoire, Chronos'' Pendant,
    Doom Orb, Dreamer''s Idol, Gem of Focus, The Cosmic Horror, Ancient Signet, Totem
    of Death, Soul Gem, Rod of Asclepius, Polynomicon, Blood-Bound Book, Soul Reaver,
    Jade Scepter, Bancroft''s Talon, Staff of Myrddin, Helm of Radiance, Ethereal
    Staff, Wish-Granting Pearl, Typhon’s Heart, Breastplate of Valor, Bracer of The
    Abyss.'
  slot_scores:
    Divine Ruin:
      total: 0.62
      efficiency: 0.43
      win: 0.86
      pick: 0.04
      fit: 0.51
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.54
      pick: 0.52
      fit: 1.0
    Nimble Ring:
      total: 0.5
      efficiency: 0.39
      win: 0.62
      pick: 0.42
      fit: 0.41
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.58
      pick: 0.55
      fit: 0.72
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.72
    Obsidian Shard:
      total: 0.61
      efficiency: 0.54
      win: 0.61
      pick: 0.45
      fit: 0.82
  community_ordered:
  - Divine Ruin
  - Spear of Desolation
  - Nimble Ring
  - Rod of Tahuti
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Divine Ruin
  - Spear of Desolation
  - The World Stone
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - The World Stone
  - Doom Orb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Divine
    Ruin, Spear of the Magus, Doom Orb, Death Metal, Gluttonous Grimoire, Ancient
    Signet, Chronos'' Pendant, Dreamer''s Idol, Bragi''s Harp, Gem of Focus, Polynomicon,
    Soul Reaver, The Cosmic Horror, Rod of Asclepius, Bancroft''s Talon, Totem of
    Death, Triton''s Conch, Soul Gem, Blood-Bound Book, Jade Scepter, Wish-Granting
    Pearl, Helm of Radiance, Breastplate of Valor, Ethereal Staff.'
  slot_scores:
    Divine Ruin:
      total: 0.6
      efficiency: 0.43
      win: 0.86
      pick: 0.04
      fit: 0.39
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.54
      pick: 0.52
      fit: 0.61
    The World Stone:
      total: 0.53
      efficiency: 0.52
      win: 0.53
      pick: 0.46
      fit: 0.57
    Doom Orb:
      total: 0.51
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.58
      pick: 0.55
      fit: 0.57
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.61
      pick: 0.45
      fit: 0.57
  community_ordered:
  - Divine Ruin
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Divine Ruin
  - Spear of Desolation
  - Nimble Ring
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Divine Ruin, Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s
    Idol, Chronos'' Pendant, Death Metal, Gem of Focus, The Cosmic Horror, Soul Gem,
    Ancient Signet, Bragi''s Harp, Totem of Death, Rod of Asclepius, Polynomicon,
    Blood-Bound Book, Soul Reaver, Jade Scepter, Triton''s Conch, Breastplate of Valor,
    Bancroft''s Talon, Genji''s Guard, Helm of Radiance, Ethereal Staff.'
  slot_scores:
    Divine Ruin:
      total: 0.59
      efficiency: 0.43
      win: 0.86
      pick: 0.04
      fit: 0.32
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.54
      pick: 0.52
      fit: 0.78
    Nimble Ring:
      total: 0.47
      efficiency: 0.39
      win: 0.62
      pick: 0.42
      fit: 0.22
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.58
      pick: 0.55
      fit: 0.56
    Spear of the Magus:
      total: 0.54
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.56
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.61
      pick: 0.45
      fit: 0.66
  community_ordered:
  - Divine Ruin
  - Spear of Desolation
  - Nimble Ring
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Divine Ruin
  - Spear of Desolation
  - Nimble Ring
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Asclepius, Gluttonous Grimoire,
    Kinetic Cuirass, Freya''s Tears, Ethereal Staff, Genji''s Guard, Breastplate of
    Valor, Shifter''s Shield, Lifebinder, Spear of the Magus, Helm of Radiance, Sphere
    of Negation, Yogi''s Necklace, Erosion, Chandra''s Grace, Eye of Providence, Phoenix
    Feather, Draconic Scale, Jade Scepter, Wish-Granting Pearl, Glorious Pridwen,
    Blood-Bound Book, Chronos'' Pendant, Soul Gem.'
  slot_scores:
    Divine Ruin:
      total: 0.59
      efficiency: 0.43
      win: 0.86
      pick: 0.04
      fit: 0.3
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.54
      pick: 0.52
      fit: 0.5
    Nimble Ring:
      total: 0.47
      efficiency: 0.39
      win: 0.62
      pick: 0.42
      fit: 0.2
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.58
      pick: 0.55
      fit: 0.36
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.61
      pick: 0.45
      fit: 0.46
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Divine Ruin
  - Spear of Desolation
  - Nimble Ring
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Divine Ruin
  - Spear of Desolation
  - Nimble Ring
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Divine Ruin, Spear of the Magus, Gluttonous Grimoire, Doom Orb,
    Dreamer''s Idol, The Cosmic Horror, Chronos'' Pendant, Soul Gem, Gem of Focus,
    Ancient Signet, Totem of Death, Rod of Asclepius, Polynomicon, Blood-Bound Book,
    Soul Reaver, Jade Scepter, Screeching Gargoyle, Bancroft''s Talon, Helm of Radiance,
    Ethereal Staff, Breastplate of Valor, Wish-Granting Pearl, Staff of Myrddin, Genji''s
    Guard.'
  slot_scores:
    Divine Ruin:
      total: 0.6
      efficiency: 0.43
      win: 0.86
      pick: 0.04
      fit: 0.38
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.54
      pick: 0.52
      fit: 1.0
    Nimble Ring:
      total: 0.48
      efficiency: 0.39
      win: 0.62
      pick: 0.42
      fit: 0.28
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.86
      win: 0.58
      pick: 0.55
      fit: 0.81
    Spear of the Magus:
      total: 0.57
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.81
    Obsidian Shard:
      total: 0.62
      efficiency: 0.54
      win: 0.61
      pick: 0.45
      fit: 0.91
  community_ordered:
  - Divine Ruin
  - Spear of Desolation
  - Nimble Ring
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Divine Ruin
  - Bracer of The Abyss
  - Nimble Ring
  - Rod of Tahuti
  - Bragi's Harp
  - Obsidian Shard
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Divine Ruin, Gluttonous Grimoire, Spear of the Magus, Bragi''s Harp,
    Bracer of The Abyss, Chronos'' Pendant, Doom Orb, Ancient Signet, Blood-Bound
    Book, Death Metal, Dreamer''s Idol, Gem of Focus, Bancroft''s Talon, Soul Gem,
    Rod of Asclepius, Polynomicon, Typhon’s Heart, The Cosmic Horror, Totem of Death,
    Soul Reaver, Jade Scepter, Helm of Radiance, Breastplate of Valor.'
  slot_scores:
    Divine Ruin:
      total: 0.58
      efficiency: 0.43
      win: 0.86
      pick: 0.04
      fit: 0.27
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.6
      efficiency: 0.65
      win: 0.62
      pick: 0.42
      fit: 0.48
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.58
      pick: 0.55
      fit: 0.29
    Bragi's Harp:
      total: 0.49
      efficiency: 0.44
      win: 0.54
      pick: 0.0
      fit: 0.62
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.61
      pick: 0.45
      fit: 0.39
  community_ordered:
  - Divine Ruin
  - Nimble Ring
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Divine Ruin
  - Spear of Desolation
  - Chronos' Pendant
  - Gem of Focus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Chronos' Pendant
  - Gem of Focus
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Chronos'' Pendant, Gem of Focus, Spear
    of the Magus, Totem of Death, Soul Gem, Gluttonous Grimoire, Breastplate of Valor,
    Doom Orb, Genji''s Guard, Dreamer''s Idol, Death Metal, Ancient Signet, Staff
    of Myrddin, The Cosmic Horror, Eye of Erebus, Screeching Gargoyle, Chandra''s
    Grace, Bragi''s Harp, Freya''s Tears, Rod of Asclepius, Polynomicon, Blood-Bound
    Book, Soul Reaver, Shield of the Phoenix.'
  slot_scores:
    Divine Ruin:
      total: 0.58
      efficiency: 0.43
      win: 0.86
      pick: 0.04
      fit: 0.25
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.54
      pick: 0.52
      fit: 0.85
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.55
      win: 0.54
      pick: 0.0
      fit: 0.65
    Gem of Focus:
      total: 0.51
      efficiency: 0.5
      win: 0.54
      pick: 0.0
      fit: 0.65
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.58
      pick: 0.55
      fit: 0.35
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.61
      pick: 0.45
      fit: 0.45
  community_ordered:
  - Divine Ruin
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Chronos' Pendant
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Chronos''
    Pendant, Doom Orb, Dreamer''s Idol, Gem of Focus, The Cosmic Horror, Ancient Signet,
    Totem of Death, Rod of Asclepius, Polynomicon, Blood-Bound Book, Soul Reaver,
    Jade Scepter, Divine Ruin, Bancroft''s Talon, Staff of Myrddin, Helm of Radiance,
    Ethereal Staff, Wish-Granting Pearl, Typhon’s Heart, Breastplate of Valor, Bracer
    of The Abyss.'
  slot_scores:
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.55
      win: 0.54
      pick: 0.0
      fit: 0.69
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.54
      pick: 0.52
      fit: 1.0
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.72
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.58
      pick: 0.55
      fit: 0.72
    Obsidian Shard:
      total: 0.61
      efficiency: 0.54
      win: 0.61
      pick: 0.45
      fit: 0.82
    Soul Gem:
      total: 0.5
      efficiency: 0.52
      win: 0.36
      pick: 0.11
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Divine Ruin
  - Spear of Desolation
  - Genji's Guard
  - Rod of Tahuti
  - Obsidian Shard
  - Rod of Asclepius
  flex_slots:
  - Obsidian Shard
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Asclepius, Amanita Charm, Gluttonous Grimoire, Genji''s Guard,
    Lifebinder, Void Stone, Spear of the Magus, Doublet of Binding, Soul Gem, Chandra''s
    Grace, Screeching Gargoyle, Ethereal Staff, Chronos'' Pendant, Doom Orb, Yogi''s
    Necklace, Jade Scepter, Phoenix Feather, Wish-Granting Pearl, Dreamer''s Idol,
    Erosion, Freya''s Tears, Gem of Focus, Shield of the Phoenix, Sphere of Negation,
    Ancile.'
  slot_scores:
    Divine Ruin:
      total: 0.57
      efficiency: 0.43
      win: 0.86
      pick: 0.04
      fit: 0.23
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.54
      pick: 0.52
      fit: 0.65
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.42
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.58
      pick: 0.55
      fit: 0.39
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.61
      pick: 0.45
      fit: 0.49
    Rod of Asclepius:
      total: 0.56
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.82
  community_ordered:
  - Divine Ruin
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: mana-stack
  slot_order:
  - Divine Ruin
  - Genji's Guard
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Rod of Asclepius
  flex_slots:
  - Genji's Guard
  - The World Stone
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Asclepius, Amanita Charm, Lifebinder, Triton''s Conch, Gluttonous Grimoire,
    Genji''s Guard, Spear of the Magus, Soul Gem, Ethereal Staff, Doom Orb, Wish-Granting
    Pearl, Death Metal, Ancient Signet, Void Stone, Chronos'' Pendant, Doublet of
    Binding, Jade Scepter, Yogi''s Necklace, Bancroft''s Talon, Sphere of Negation,
    Dreamer''s Idol, Blood-Bound Book, Gem of Focus, Bragi''s Harp.'
  slot_scores:
    Divine Ruin:
      total: 0.59
      efficiency: 0.43
      win: 0.86
      pick: 0.04
      fit: 0.33
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.28
    The World Stone:
      total: 0.51
      efficiency: 0.52
      win: 0.53
      pick: 0.46
      fit: 0.47
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.58
      pick: 0.55
      fit: 0.47
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.61
      pick: 0.45
      fit: 0.48
    Rod of Asclepius:
      total: 0.56
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.83
  community_ordered:
  - Divine Ruin
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: burst
  slot_order:
  - Divine Ruin
  - Spear of Desolation
  - Nimble Ring
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Asclepius, Amanita Charm, Gluttonous Grimoire, Lifebinder, Spear of
    the Magus, Genji''s Guard, Triton''s Conch, Soul Gem, Doom Orb, Ethereal Staff,
    Void Stone, Chronos'' Pendant, Dreamer''s Idol, Doublet of Binding, Screeching
    Gargoyle, Death Metal, Jade Scepter, Chandra''s Grace, Wish-Granting Pearl, Gem
    of Focus, Sphere of Negation, Ancient Signet, Yogi''s Necklace, Blood-Bound Book,
    Daybreak Gavel.'
  slot_scores:
    Divine Ruin:
      total: 0.58
      efficiency: 0.43
      win: 0.86
      pick: 0.04
      fit: 0.28
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.54
      pick: 0.52
      fit: 0.62
    Nimble Ring:
      total: 0.46
      efficiency: 0.39
      win: 0.62
      pick: 0.42
      fit: 0.18
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.58
      pick: 0.55
      fit: 0.45
    Spear of the Magus:
      total: 0.52
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.45
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.61
      pick: 0.45
      fit: 0.55
  community_ordered:
  - Divine Ruin
  - Spear of Desolation
  - Nimble Ring
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: bruiser
  slot_order:
  - Divine Ruin
  - Rod of Tahuti
  - Amanita Charm
  - Rod of Asclepius
  - Obsidian Shard
  - Erosion
  flex_slots:
  - Erosion
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Asclepius, Shield of the Phoenix, Erosion, Kinetic
    Cuirass, Lifebinder, Freya''s Tears, Void Shield, Stampede, Genji''s Guard, Breastplate
    of Valor, Gluttonous Grimoire, Void Stone, Shifter''s Shield, Spectral Armor,
    Doublet of Binding, Ethereal Staff, Chandra''s Grace, Eye of Providence, Draconic
    Scale, Yogi''s Necklace, Soul Gem, Phoenix Feather, Glorious Pridwen, Mystical
    Mail, Spear of the Magus, Helm of Radiance.'
  slot_scores:
    Divine Ruin:
      total: 0.57
      efficiency: 0.43
      win: 0.86
      pick: 0.04
      fit: 0.19
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.58
      pick: 0.55
      fit: 0.26
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 1.0
    Rod of Asclepius:
      total: 0.58
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.9
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.61
      pick: 0.45
      fit: 0.36
    Erosion:
      total: 0.55
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.87
  community_ordered:
  - Divine Ruin
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: anti-tank
  slot_order:
  - Divine Ruin
  - Spear of Desolation
  - Void Stone
  - Gluttonous Grimoire
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Gluttonous Grimoire
  - Void Stone
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Rod of Asclepius, Amanita Charm, Void Stone,
    Spear of the Magus, Screeching Gargoyle, Genji''s Guard, Lifebinder, Doom Orb,
    Dreamer''s Idol, Soul Gem, Doublet of Binding, Ethereal Staff, The Cosmic Horror,
    Chandra''s Grace, Chronos'' Pendant, Yogi''s Necklace, Jade Scepter, Wish-Granting
    Pearl, Phoenix Feather, Sphere of Negation, Erosion, Gem of Focus, Ancile, Freya''s
    Tears.'
  slot_scores:
    Divine Ruin:
      total: 0.57
      efficiency: 0.43
      win: 0.86
      pick: 0.04
      fit: 0.19
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.54
      pick: 0.52
      fit: 0.74
    Void Stone:
      total: 0.54
      efficiency: 0.45
      win: 0.54
      pick: 0.0
      fit: 0.96
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.55
      win: 0.54
      pick: 0.0
      fit: 0.8
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.58
      pick: 0.55
      fit: 0.56
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.61
      pick: 0.45
      fit: 0.66
  community_ordered:
  - Divine Ruin
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: attack-speed
  slot_order:
  - Divine Ruin
  - Bracer of The Abyss
  - Nimble Ring
  - Rod of Tahuti
  - Bragi's Harp
  - Rod of Asclepius
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Asclepius, Amanita Charm, Gluttonous Grimoire, Soul Gem, Genji''s
    Guard, Lifebinder, Void Stone, Triton''s Conch, Doublet of Binding, Spear of the
    Magus, Blood-Bound Book, Bragi''s Harp, Bancroft''s Talon, Ethereal Staff, Yogi''s
    Necklace, Bracer of The Abyss, Screeching Gargoyle, Daybreak Gavel, Chandra''s
    Grace, Chronos'' Pendant, Doom Orb, Jade Scepter, Ancient Signet, Wish-Granting
    Pearl, Sphere of Negation.'
  slot_scores:
    Divine Ruin:
      total: 0.56
      efficiency: 0.43
      win: 0.86
      pick: 0.04
      fit: 0.16
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.58
      efficiency: 0.65
      win: 0.62
      pick: 0.42
      fit: 0.35
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.58
      pick: 0.55
      fit: 0.17
    Bragi's Harp:
      total: 0.47
      efficiency: 0.44
      win: 0.54
      pick: 0.0
      fit: 0.49
    Rod of Asclepius:
      total: 0.54
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Divine Ruin
  - Nimble Ring
  - Rod of Tahuti
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: cooldown
  slot_order:
  - Divine Ruin
  - Spear of Desolation
  - Genji's Guard
  - Chronos' Pendant
  - Rod of Tahuti
  - Rod of Asclepius
  flex_slots:
  - Genji's Guard
  - Chronos' Pendant
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Asclepius, Genji''s Guard,
    Amanita Charm, Lifebinder, Chronos'' Pendant, Screeching Gargoyle, Gluttonous
    Grimoire, Chandra''s Grace, Soul Gem, Spear of the Magus, Triton''s Conch, Gem
    of Focus, Void Stone, Doublet of Binding, Freya''s Tears, Ethereal Staff, Shield
    of the Phoenix, Eye of Erebus, Totem of Death, Yogi''s Necklace, Doom Orb, Daybreak
    Gavel, Jade Scepter, Wish-Granting Pearl, Breastplate of Valor.'
  slot_scores:
    Divine Ruin:
      total: 0.57
      efficiency: 0.43
      win: 0.86
      pick: 0.04
      fit: 0.22
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.54
      pick: 0.52
      fit: 0.67
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.49
    Chronos' Pendant:
      total: 0.51
      efficiency: 0.55
      win: 0.54
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.58
      pick: 0.55
      fit: 0.27
    Rod of Asclepius:
      total: 0.55
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.74
  community_ordered:
  - Divine Ruin
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Void Stone
  - Rod of Tahuti
  - Spear of the Magus
  - Soul Gem
  flex_slots:
  - Void Stone
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Soul Gem, Rod of Asclepius, Amanita Charm, Gluttonous
    Grimoire, Genji''s Guard, Lifebinder, Void Stone, Spear of the Magus, Doublet
    of Binding, Chandra''s Grace, Screeching Gargoyle, Ethereal Staff, Chronos'' Pendant,
    Doom Orb, Yogi''s Necklace, Jade Scepter, Phoenix Feather, Wish-Granting Pearl,
    Dreamer''s Idol, Erosion, Freya''s Tears, Gem of Focus, Shield of the Phoenix,
    Sphere of Negation, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.42
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.54
      pick: 0.52
      fit: 0.65
    Void Stone:
      total: 0.51
      efficiency: 0.45
      win: 0.54
      pick: 0.0
      fit: 0.75
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.58
      pick: 0.55
      fit: 0.39
    Spear of the Magus:
      total: 0.51
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.39
    Soul Gem:
      total: 0.5
      efficiency: 0.52
      win: 0.36
      pick: 0.11
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
  aspect: Aspect of Thermotherapy
---

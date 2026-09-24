---
type: smite-build
god: Ra
mode: Conquest
builds:
- source: community
  aspect: Aspect of Thermotherapy
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.5
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.44
    win_rate: 0.53
    alternates:
    - name: Book of Thoth
      pick_rate: 0.28
      win_rate: 0.54
    - name: Chandra's Grace
      pick_rate: 0.07
      win_rate: 0.62
  - name: The World Stone
    pick_rate: 0.38
    win_rate: 0.55
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.16
      win_rate: 0.52
    - name: Chronos' Pendant
      pick_rate: 0.14
      win_rate: 0.5
  - name: Rod of Tahuti
    pick_rate: 0.27
    win_rate: 0.53
    alternates:
    - name: Soul Gem
      pick_rate: 0.13
      win_rate: 0.76
    - name: The World Stone
      pick_rate: 0.1
      win_rate: 0.5
  - name: Nimble Ring
    pick_rate: 0.18
    win_rate: 0.64
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.26
      win_rate: 0.62
    - name: Obsidian Shard
      pick_rate: 0.12
      win_rate: 0.42
  - name: Obsidian Shard
    pick_rate: 0.3
    win_rate: 0.5
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.13
      win_rate: 0.56
    - name: Nimble Ring
      pick_rate: 0.09
      win_rate: 0.83
  - name: Evil Eye
    pick_rate: 0.11
    win_rate: 0.4
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.14
      win_rate: 0.83
    - name: Blinking Abyss
      pick_rate: 0.1
      win_rate: 0.67
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.34
    win_rate: 0.66
  - name: Pendulum of the Ages
    pick_rate: 0.31
    win_rate: 0.56
  - name: Conduit Gem
    pick_rate: 0.19
    win_rate: 0.38
  source_url: https://smitebrain.com/gods/ra/
  last_verified: '2026-09-24'
  god_win_rate: 0.5454545454545454
  god_matches_won: 96
  god_matches_played: 176
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-24'
  god_matches_analyzed: 1954
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The World Stone
  - Book of Thoth
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s Idol,
    Gem of Focus, The Cosmic Horror, Ancient Signet, Totem of Death, Rod of Asclepius,
    Polynomicon, Blood-Bound Book, Soul Reaver, Jade Scepter, Divine Ruin, Bancroft''s
    Talon, Staff of Myrddin, Helm of Radiance, Ethereal Staff, Wish-Granting Pearl,
    Typhon’s Heart, Breastplate of Valor, Bracer of The Abyss.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.54
      pick: 0.28
      fit: 0.41
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.53
      pick: 0.44
      fit: 1.0
    The World Stone:
      total: 0.56
      efficiency: 0.52
      win: 0.55
      pick: 0.52
      fit: 0.72
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.53
      pick: 0.42
      fit: 0.72
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.5
      pick: 0.65
      fit: 0.82
    Soul Gem:
      total: 0.68
      efficiency: 0.52
      win: 0.76
      pick: 0.2
      fit: 1.0
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Doom Orb
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Doom Orb
  - Book of Thoth
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Spear
    of the Magus, Doom Orb, Death Metal, Gluttonous Grimoire, Ancient Signet, Dreamer''s
    Idol, Bragi''s Harp, Gem of Focus, Polynomicon, Soul Reaver, The Cosmic Horror,
    Rod of Asclepius, Bancroft''s Talon, Totem of Death, Triton''s Conch, Blood-Bound
    Book, Jade Scepter, Divine Ruin, Wish-Granting Pearl, Helm of Radiance, Breastplate
    of Valor, Ethereal Staff.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.51
      win: 0.54
      pick: 0.28
      fit: 0.39
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.53
      pick: 0.44
      fit: 0.61
    The World Stone:
      total: 0.54
      efficiency: 0.52
      win: 0.55
      pick: 0.52
      fit: 0.57
    Doom Orb:
      total: 0.51
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.53
      pick: 0.42
      fit: 0.57
    Soul Gem:
      total: 0.64
      efficiency: 0.52
      win: 0.76
      pick: 0.2
      fit: 0.71
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The World Stone
  - Book of Thoth
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
    god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s Idol, Death
    Metal, Gem of Focus, The Cosmic Horror, Ancient Signet, Bragi''s Harp, Totem of
    Death, Rod of Asclepius, Polynomicon, Blood-Bound Book, Soul Reaver, Jade Scepter,
    Divine Ruin, Triton''s Conch, Breastplate of Valor, Bancroft''s Talon, Genji''s
    Guard, Helm of Radiance, Ethereal Staff.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.54
      pick: 0.28
      fit: 0.22
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.53
      pick: 0.44
      fit: 0.78
    The World Stone:
      total: 0.54
      efficiency: 0.52
      win: 0.55
      pick: 0.52
      fit: 0.56
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.53
      pick: 0.42
      fit: 0.56
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.5
      pick: 0.65
      fit: 0.66
    Soul Gem:
      total: 0.66
      efficiency: 0.52
      win: 0.76
      pick: 0.2
      fit: 0.88
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Amanita Charm, Shield of the Phoenix, Rod of Asclepius, Chandra''s Grace,
    Gluttonous Grimoire, Kinetic Cuirass, Freya''s Tears, Ethereal Staff, Genji''s
    Guard, Breastplate of Valor, Shifter''s Shield, Lifebinder, Spear of the Magus,
    Helm of Radiance, Sphere of Negation, Yogi''s Necklace, Erosion, Eye of Providence,
    Phoenix Feather, Draconic Scale, Jade Scepter, Wish-Granting Pearl, Glorious Pridwen,
    Blood-Bound Book.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.6
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.53
      pick: 0.44
      fit: 0.5
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.53
      pick: 0.42
      fit: 0.36
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.67
      efficiency: 0.52
      win: 0.76
      pick: 0.2
      fit: 0.9
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The World Stone
  - Spear of the Magus
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s Idol,
    The Cosmic Horror, Gem of Focus, Ancient Signet, Totem of Death, Rod of Asclepius,
    Polynomicon, Blood-Bound Book, Soul Reaver, Jade Scepter, Divine Ruin, Screeching
    Gargoyle, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Breastplate of
    Valor, Wish-Granting Pearl, Staff of Myrddin, Genji''s Guard.'
  slot_scores:
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.53
      pick: 0.44
      fit: 1.0
    Spear of the Magus:
      total: 0.57
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.81
    The World Stone:
      total: 0.58
      efficiency: 0.52
      win: 0.55
      pick: 0.52
      fit: 0.81
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.53
      pick: 0.42
      fit: 0.81
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.5
      pick: 0.65
      fit: 0.91
    Soul Gem:
      total: 0.68
      efficiency: 0.52
      win: 0.76
      pick: 0.2
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Spear of Desolation
  - Bragi's Harp
  - Nimble Ring
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Spear of the Magus, Bragi''s Harp, Bracer of The
    Abyss, Doom Orb, Ancient Signet, Blood-Bound Book, Death Metal, Dreamer''s Idol,
    Gem of Focus, Bancroft''s Talon, Rod of Asclepius, Polynomicon, Typhon’s Heart,
    The Cosmic Horror, Totem of Death, Soul Reaver, Jade Scepter, Divine Ruin, Helm
    of Radiance, Breastplate of Valor.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.4
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.53
      pick: 0.44
      fit: 0.41
    Bragi's Harp:
      total: 0.49
      efficiency: 0.44
      win: 0.54
      pick: 0.0
      fit: 0.62
    Nimble Ring:
      total: 0.6
      efficiency: 0.65
      win: 0.64
      pick: 0.3
      fit: 0.48
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.53
      pick: 0.42
      fit: 0.29
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.76
      pick: 0.2
      fit: 0.58
  community_ordered:
  - Spear of Desolation
  - Nimble Ring
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Gem of Focus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Gem of Focus
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Gem of Focus, Spear of the Magus,
    Totem of Death, Gluttonous Grimoire, Chandra''s Grace, Breastplate of Valor, Doom
    Orb, Genji''s Guard, Dreamer''s Idol, Death Metal, Ancient Signet, Staff of Myrddin,
    The Cosmic Horror, Eye of Erebus, Screeching Gargoyle, Bragi''s Harp, Freya''s
    Tears, Rod of Asclepius, Polynomicon, Blood-Bound Book, Soul Reaver, Shield of
    the Phoenix.'
  slot_scores:
    Chronos' Pendant:
      total: 0.52
      efficiency: 0.55
      win: 0.5
      pick: 0.19
      fit: 0.65
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.53
      pick: 0.44
      fit: 0.85
    Gem of Focus:
      total: 0.52
      efficiency: 0.5
      win: 0.54
      pick: 0.0
      fit: 0.65
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.53
      pick: 0.42
      fit: 0.35
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.5
      pick: 0.65
      fit: 0.45
    Soul Gem:
      total: 0.68
      efficiency: 0.52
      win: 0.76
      pick: 0.2
      fit: 0.95
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
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
    Underrated for this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s
    Idol, Gem of Focus, The Cosmic Horror, Ancient Signet, Totem of Death, Rod of
    Asclepius, Polynomicon, Blood-Bound Book, Soul Reaver, Jade Scepter, Divine Ruin,
    Bancroft''s Talon, Staff of Myrddin, Helm of Radiance, Ethereal Staff, Wish-Granting
    Pearl, Typhon’s Heart, Breastplate of Valor, Bracer of The Abyss.'
  slot_scores:
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.55
      win: 0.5
      pick: 0.19
      fit: 0.69
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.53
      pick: 0.44
      fit: 1.0
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.72
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.53
      pick: 0.42
      fit: 0.72
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.5
      pick: 0.65
      fit: 0.82
    Soul Gem:
      total: 0.68
      efficiency: 0.52
      win: 0.76
      pick: 0.2
      fit: 1.0
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Genji's Guard
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Book of Thoth
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Asclepius, Amanita Charm, Chandra''s Grace, Gluttonous Grimoire,
    Genji''s Guard, Lifebinder, Void Stone, Spear of the Magus, Doublet of Binding,
    Screeching Gargoyle, Ethereal Staff, Doom Orb, Yogi''s Necklace, Jade Scepter,
    Phoenix Feather, Wish-Granting Pearl, Dreamer''s Idol, Erosion, Freya''s Tears,
    Gem of Focus, Shield of the Phoenix, Sphere of Negation, Ancile.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.51
      win: 0.54
      pick: 0.28
      fit: 0.13
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.53
      pick: 0.44
      fit: 0.65
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.42
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.53
      pick: 0.42
      fit: 0.39
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.5
      pick: 0.65
      fit: 0.49
    Soul Gem:
      total: 0.68
      efficiency: 0.52
      win: 0.76
      pick: 0.2
      fit: 1.0
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Genji's Guard
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Book of Thoth
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Asclepius, Amanita Charm, Lifebinder, Triton''s Conch, Gluttonous Grimoire,
    Genji''s Guard, Spear of the Magus, Ethereal Staff, Doom Orb, Wish-Granting Pearl,
    Death Metal, Ancient Signet, Void Stone, Doublet of Binding, Jade Scepter, Yogi''s
    Necklace, Bancroft''s Talon, Sphere of Negation, Dreamer''s Idol, Blood-Bound
    Book, Gem of Focus, Bragi''s Harp.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.54
      pick: 0.28
      fit: 0.32
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.53
      pick: 0.44
      fit: 0.5
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.28
    The World Stone:
      total: 0.52
      efficiency: 0.52
      win: 0.55
      pick: 0.52
      fit: 0.47
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.53
      pick: 0.42
      fit: 0.47
    Soul Gem:
      total: 0.68
      efficiency: 0.52
      win: 0.76
      pick: 0.2
      fit: 1.0
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The World Stone
  - Book of Thoth
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Asclepius, Amanita Charm, Gluttonous Grimoire, Lifebinder, Spear of
    the Magus, Chandra''s Grace, Genji''s Guard, Triton''s Conch, Doom Orb, Ethereal
    Staff, Void Stone, Dreamer''s Idol, Doublet of Binding, Screeching Gargoyle, Death
    Metal, Jade Scepter, Wish-Granting Pearl, Gem of Focus, Sphere of Negation, Ancient
    Signet, Yogi''s Necklace, Blood-Bound Book, Daybreak Gavel.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.51
      win: 0.54
      pick: 0.28
      fit: 0.18
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.53
      pick: 0.44
      fit: 0.62
    The World Stone:
      total: 0.52
      efficiency: 0.52
      win: 0.55
      pick: 0.52
      fit: 0.45
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.53
      pick: 0.42
      fit: 0.45
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.5
      pick: 0.65
      fit: 0.55
    Soul Gem:
      total: 0.68
      efficiency: 0.52
      win: 0.76
      pick: 0.2
      fit: 1.0
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  - Erosion
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Amanita Charm, Rod of Asclepius, Shield of the Phoenix, Erosion, Chandra''s
    Grace, Kinetic Cuirass, Lifebinder, Freya''s Tears, Void Shield, Stampede, Genji''s
    Guard, Breastplate of Valor, Gluttonous Grimoire, Void Stone, Shifter''s Shield,
    Spectral Armor, Doublet of Binding, Ethereal Staff, Eye of Providence, Draconic
    Scale, Yogi''s Necklace, Phoenix Feather, Glorious Pridwen, Mystical Mail, Spear
    of the Magus, Helm of Radiance.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.67
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.52
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.53
      pick: 0.42
      fit: 0.26
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.55
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.87
    Soul Gem:
      total: 0.68
      efficiency: 0.52
      win: 0.76
      pick: 0.2
      fit: 1.0
  community_ordered:
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: anti-tank
  slot_order:
  - Void Stone
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Void Stone
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Rod of Asclepius, Amanita Charm, Void Stone,
    Spear of the Magus, Screeching Gargoyle, Chandra''s Grace, Genji''s Guard, Lifebinder,
    Doom Orb, Dreamer''s Idol, Doublet of Binding, Ethereal Staff, The Cosmic Horror,
    Yogi''s Necklace, Jade Scepter, Wish-Granting Pearl, Phoenix Feather, Sphere of
    Negation, Erosion, Gem of Focus, Ancile, Freya''s Tears.'
  slot_scores:
    Void Stone:
      total: 0.55
      efficiency: 0.45
      win: 0.54
      pick: 0.0
      fit: 0.96
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.53
      pick: 0.44
      fit: 0.74
    The World Stone:
      total: 0.54
      efficiency: 0.52
      win: 0.55
      pick: 0.52
      fit: 0.56
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.53
      pick: 0.42
      fit: 0.56
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.5
      pick: 0.65
      fit: 0.66
    Soul Gem:
      total: 0.68
      efficiency: 0.52
      win: 0.76
      pick: 0.2
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Spear of Desolation
  - Bragi's Harp
  - Nimble Ring
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
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Asclepius, Amanita Charm, Gluttonous Grimoire, Chandra''s Grace,
    Genji''s Guard, Lifebinder, Void Stone, Triton''s Conch, Doublet of Binding, Spear
    of the Magus, Blood-Bound Book, Bragi''s Harp, Bancroft''s Talon, Ethereal Staff,
    Yogi''s Necklace, Bracer of The Abyss, Screeching Gargoyle, Daybreak Gavel, Doom
    Orb, Jade Scepter, Ancient Signet, Wish-Granting Pearl, Sphere of Negation.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.28
    Spear of Desolation:
      total: 0.5
      efficiency: 0.57
      win: 0.53
      pick: 0.44
      fit: 0.29
    Bragi's Harp:
      total: 0.47
      efficiency: 0.44
      win: 0.54
      pick: 0.0
      fit: 0.49
    Nimble Ring:
      total: 0.58
      efficiency: 0.65
      win: 0.64
      pick: 0.3
      fit: 0.35
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.53
      pick: 0.42
      fit: 0.17
    Soul Gem:
      total: 0.7
      efficiency: 0.57
      win: 0.76
      pick: 0.2
      fit: 0.96
  community_ordered:
  - Spear of Desolation
  - Nimble Ring
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: cooldown
  slot_order:
  - Screeching Gargoyle
  - Spear of Desolation
  - Genji's Guard
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Screeching Gargoyle
  - Obsidian Shard
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Asclepius, Chandra''s Grace,
    Genji''s Guard, Amanita Charm, Lifebinder, Screeching Gargoyle, Gluttonous Grimoire,
    Spear of the Magus, Triton''s Conch, Gem of Focus, Void Stone, Doublet of Binding,
    Freya''s Tears, Ethereal Staff, Shield of the Phoenix, Eye of Erebus, Totem of
    Death, Yogi''s Necklace, Doom Orb, Daybreak Gavel, Jade Scepter, Wish-Granting
    Pearl, Breastplate of Valor.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.51
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.53
      pick: 0.44
      fit: 0.67
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.53
      pick: 0.42
      fit: 0.27
    Obsidian Shard:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.65
      fit: 0.37
    Soul Gem:
      total: 0.68
      efficiency: 0.52
      win: 0.76
      pick: 0.2
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
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
    Underrated for this god: Rod of Asclepius, Amanita Charm, Gluttonous Grimoire,
    Genji''s Guard, Lifebinder, Void Stone, Spear of the Magus, Doublet of Binding,
    Chandra''s Grace, Screeching Gargoyle, Ethereal Staff, Doom Orb, Yogi''s Necklace,
    Jade Scepter, Phoenix Feather, Wish-Granting Pearl, Dreamer''s Idol, Erosion,
    Freya''s Tears, Gem of Focus, Shield of the Phoenix, Sphere of Negation, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.42
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.53
      pick: 0.44
      fit: 0.65
    Void Stone:
      total: 0.52
      efficiency: 0.45
      win: 0.54
      pick: 0.0
      fit: 0.75
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.53
      pick: 0.42
      fit: 0.39
    Spear of the Magus:
      total: 0.51
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.39
    Soul Gem:
      total: 0.68
      efficiency: 0.52
      win: 0.76
      pick: 0.2
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
  aspect: Aspect of Thermotherapy
---

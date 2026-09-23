---
type: smite-build
god: Merlin
mode: Conquest
builds:
- source: community
  aspect: Aspect of Pandemonium
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.25
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.37
    win_rate: 0.57
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.26
      win_rate: 0.65
    - name: The Cosmic Horror
      pick_rate: 0.11
      win_rate: 0.5
  - name: The World Stone
    pick_rate: 0.26
    win_rate: 0.6
    alternates:
    - name: Soul Reaver
      pick_rate: 0.13
      win_rate: 0.5
    - name: Soul Gem
      pick_rate: 0.12
      win_rate: 0.33
  - name: Soul Gem
    pick_rate: 0.24
    win_rate: 0.71
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.16
      win_rate: 0.36
    - name: The World Stone
      pick_rate: 0.11
      win_rate: 0.5
  - name: Rod of Tahuti
    pick_rate: 0.38
    win_rate: 0.52
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.2
      win_rate: 0.54
    - name: Soul Gem
      pick_rate: 0.08
      win_rate: 0.8
  - name: Obsidian Shard
    pick_rate: 0.29
    win_rate: 0.56
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.14
      win_rate: 0.75
    - name: Evil Eye
      pick_rate: 0.11
      win_rate: 0.33
  - name: Soul Reaver
    pick_rate: 0.13
    win_rate: 0.75
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.19
      win_rate: 0.67
    - name: Evil Eye
      pick_rate: 0.13
      win_rate: 1.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.3
    win_rate: 0.61
  - name: Pendulum of the Ages
    pick_rate: 0.28
    win_rate: 0.52
  - name: Bluestone Pendant
    pick_rate: 0.17
    win_rate: 0.46
  source_url: https://smitebrain.com/gods/merlin/
  last_verified: '2026-09-23'
  god_win_rate: 0.5131578947368421
  god_matches_won: 39
  god_matches_played: 76
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-23'
  god_matches_analyzed: 962
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Spear of the Magus
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s Idol,
    Gem of Focus, Ancient Signet, Totem of Death, Rod of Asclepius, Book of Thoth,
    Polynomicon, The Cosmic Horror, Blood-Bound Book, Jade Scepter, Divine Ruin, Bancroft''s
    Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin, Wish-Granting Pearl,
    Typhon’s Heart, Bracer of The Abyss, Nimble Ring.'
  slot_scores:
    Chronos' Pendant:
      total: 0.59
      efficiency: 0.55
      win: 0.65
      pick: 0.26
      fit: 0.63
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.57
      pick: 0.37
      fit: 1.0
    Spear of the Magus:
      total: 0.6
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.67
      efficiency: 0.52
      win: 0.71
      pick: 0.37
      fit: 1.0
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.52
      pick: 0.63
      fit: 0.79
    Obsidian Shard:
      total: 0.61
      efficiency: 0.54
      win: 0.56
      pick: 0.63
      fit: 0.89
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - The World Stone
  - Soul Gem
  - Rod of Tahuti
  - Soul Reaver
  flex_slots:
  - Chronos' Pendant
  - The World Stone
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
    Idol, Bragi''s Harp, Gem of Focus, Book of Thoth, Polynomicon, Rod of Asclepius,
    Bancroft''s Talon, Totem of Death, Triton''s Conch, Blood-Bound Book, Jade Scepter,
    Divine Ruin, Wish-Granting Pearl, Helm of Radiance, Breastplate of Valor, Ethereal
    Staff, The Cosmic Horror.'
  slot_scores:
    Chronos' Pendant:
      total: 0.56
      efficiency: 0.55
      win: 0.65
      pick: 0.26
      fit: 0.43
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.57
      pick: 0.37
      fit: 0.61
    The World Stone:
      total: 0.55
      efficiency: 0.52
      win: 0.6
      pick: 0.35
      fit: 0.57
    Soul Gem:
      total: 0.63
      efficiency: 0.52
      win: 0.71
      pick: 0.37
      fit: 0.71
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.52
      pick: 0.63
      fit: 0.57
    Soul Reaver:
      total: 0.58
      efficiency: 0.4
      win: 0.75
      pick: 0.4
      fit: 0.59
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - The World Stone
  - Soul Gem
  - Rod of Tahuti
  - Soul Reaver
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Spear of the Magus
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
  - Chronos' Pendant
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
    Metal, Gem of Focus, Ancient Signet, Bragi''s Harp, Totem of Death, Rod of Asclepius,
    Book of Thoth, Polynomicon, Blood-Bound Book, Jade Scepter, The Cosmic Horror,
    Divine Ruin, Triton''s Conch, Breastplate of Valor, Bancroft''s Talon, Genji''s
    Guard, Helm of Radiance, Ethereal Staff.'
  slot_scores:
    Chronos' Pendant:
      total: 0.56
      efficiency: 0.55
      win: 0.65
      pick: 0.26
      fit: 0.44
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.57
      pick: 0.37
      fit: 0.78
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.56
    Soul Gem:
      total: 0.65
      efficiency: 0.52
      win: 0.71
      pick: 0.37
      fit: 0.88
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.52
      pick: 0.63
      fit: 0.56
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.56
      pick: 0.63
      fit: 0.66
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Kinetic Cuirass
  - Soul Gem
  - Soul Reaver
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Soul Reaver
  - Book of Thoth
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Asclepius, Shield of the Phoenix, Gluttonous Grimoire,
    Kinetic Cuirass, Ethereal Staff, Freya''s Tears, Spear of the Magus, Shifter''s
    Shield, Genji''s Guard, Breastplate of Valor, Lifebinder, Helm of Radiance, Sphere
    of Negation, Erosion, Yogi''s Necklace, Eye of Providence, Draconic Scale, Phoenix
    Feather, Jade Scepter, Chandra''s Grace, Wish-Granting Pearl, Blood-Bound Book,
    Doom Orb, Glorious Pridwen.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.21
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.61
    Soul Gem:
      total: 0.65
      efficiency: 0.52
      win: 0.71
      pick: 0.37
      fit: 0.89
    Soul Reaver:
      total: 0.56
      efficiency: 0.4
      win: 0.75
      pick: 0.4
      fit: 0.41
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.52
      pick: 0.63
      fit: 0.39
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.81
  community_ordered:
  - Soul Gem
  - Soul Reaver
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
  - The World Stone
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
    Ancient Signet, The Cosmic Horror, Gem of Focus, Rod of Asclepius, Book of Thoth,
    Totem of Death, Polynomicon, Blood-Bound Book, Jade Scepter, Divine Ruin, Bancroft''s
    Talon, Helm of Radiance, Ethereal Staff, Screeching Gargoyle, Wish-Granting Pearl,
    Typhon’s Heart, Breastplate of Valor, Bracer of The Abyss.'
  slot_scores:
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.57
      pick: 0.37
      fit: 1.0
    Spear of the Magus:
      total: 0.61
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.85
    The World Stone:
      total: 0.6
      efficiency: 0.52
      win: 0.6
      pick: 0.35
      fit: 0.85
    Soul Gem:
      total: 0.67
      efficiency: 0.52
      win: 0.71
      pick: 0.37
      fit: 1.0
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.52
      pick: 0.63
      fit: 0.85
    Obsidian Shard:
      total: 0.62
      efficiency: 0.54
      win: 0.56
      pick: 0.63
      fit: 0.95
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Soul Gem
  - Rod of Tahuti
  - Soul Reaver
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
    this god: Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Bragi''s Harp,
    Bracer of The Abyss, Doom Orb, Ancient Signet, Blood-Bound Book, Dreamer''s Idol,
    Death Metal, Bancroft''s Talon, Gem of Focus, Rod of Asclepius, Book of Thoth,
    Typhon’s Heart, Polynomicon, Totem of Death, Jade Scepter, Divine Ruin, Helm of
    Radiance, Daybreak Gavel, The Cosmic Horror.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.51
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.52
      efficiency: 0.44
      win: 0.6
      pick: 0.0
      fit: 0.63
    Soul Gem:
      total: 0.62
      efficiency: 0.57
      win: 0.71
      pick: 0.37
      fit: 0.58
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.52
      pick: 0.63
      fit: 0.32
    Soul Reaver:
      total: 0.55
      efficiency: 0.4
      win: 0.75
      pick: 0.4
      fit: 0.37
  community_ordered:
  - Soul Gem
  - Rod of Tahuti
  - Soul Reaver
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Chronos' Pendant
  - Spear of Desolation
  - Soul Gem
  - Rod of Tahuti
  - Soul Reaver
  flex_slots:
  - Soul Reaver
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Gem of Focus, Spear of the Magus,
    Gluttonous Grimoire, Totem of Death, Doom Orb, Breastplate of Valor, Dreamer''s
    Idol, Genji''s Guard, Ancient Signet, Death Metal, Staff of Myrddin, Eye of Erebus,
    Screeching Gargoyle, Bragi''s Harp, Rod of Asclepius, Book of Thoth, Chandra''s
    Grace, Freya''s Tears, Polynomicon, Blood-Bound Book, Jade Scepter, The Cosmic
    Horror.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.14
    Chronos' Pendant:
      total: 0.59
      efficiency: 0.55
      win: 0.65
      pick: 0.26
      fit: 0.63
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.57
      pick: 0.37
      fit: 0.86
    Soul Gem:
      total: 0.66
      efficiency: 0.52
      win: 0.71
      pick: 0.37
      fit: 0.96
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.52
      pick: 0.63
      fit: 0.37
    Soul Reaver:
      total: 0.55
      efficiency: 0.4
      win: 0.75
      pick: 0.4
      fit: 0.34
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Soul Gem
  - Rod of Tahuti
  - Soul Reaver
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s
    Idol, The Cosmic Horror, Gem of Focus, Ancient Signet, Totem of Death, Rod of
    Asclepius, Book of Thoth, Polynomicon, Blood-Bound Book, Jade Scepter, Divine
    Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin, Wish-Granting
    Pearl, Typhon’s Heart, Bracer of The Abyss, Nimble Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.57
      pick: 0.37
      fit: 1.0
    Doom Orb:
      total: 0.57
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.6
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.67
      efficiency: 0.52
      win: 0.71
      pick: 0.37
      fit: 1.0
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.52
      pick: 0.63
      fit: 0.79
    Obsidian Shard:
      total: 0.61
      efficiency: 0.54
      win: 0.56
      pick: 0.63
      fit: 0.89
  community_ordered:
  - Spear of Desolation
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
---

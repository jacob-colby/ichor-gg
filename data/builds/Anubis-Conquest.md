---
type: smite-build
god: Anubis
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Bancroft's Talon
    pick_rate: 0.62
    win_rate: 0.42
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.13
      win_rate: 0.0
    - name: Blood-Bound Book
      pick_rate: 0.1
      win_rate: 0.5
  - name: Blood-Bound Book
    pick_rate: 0.26
    win_rate: 0.5
    alternates:
    - name: Typhon’s Heart
      pick_rate: 0.23
      win_rate: 0.33
    - name: The Cosmic Horror
      pick_rate: 0.15
      win_rate: 0.67
  - name: Rod of Tahuti
    pick_rate: 0.23
    win_rate: 0.56
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.18
      win_rate: 0.29
    - name: Totem of Death
      pick_rate: 0.1
      win_rate: 0.75
  - name: Soul Gem
    pick_rate: 0.22
    win_rate: 0.5
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.27
      win_rate: 0.2
    - name: Blinking Abyss
      pick_rate: 0.11
      win_rate: 0.5
  - name: Doom Orb
    pick_rate: 0.31
    win_rate: 0.5
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.13
      win_rate: 0.5
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.33
  - name: Killing Stone
    pick_rate: 0.26
    win_rate: 0.4
    alternates:
    - name: Dreamer's Idol
      pick_rate: 0.26
      win_rate: 0.6
    - name: Divine Ruin
      pick_rate: 0.11
      win_rate: 0.5
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.31
    win_rate: 0.42
  - name: Conduit Gem
    pick_rate: 0.23
    win_rate: 0.33
  - name: Blood-soaked Shroud
    pick_rate: 0.15
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/anubis/
  last_verified: '2026-09-10'
  god_win_rate: 0.4358974358974359
  god_matches_won: 17
  god_matches_played: 39
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-10'
  god_matches_analyzed: 1308
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - The Cosmic Horror
  - Totem of Death
  - Rod of Tahuti
  - Doom Orb
  - Soul Gem
  - Dreamer's Idol
  flex_slots:
  - Soul Gem
  - Doom Orb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Spear of the Magus, Obsidian Shard, Gluttonous Grimoire, The World Stone,
    Chronos'' Pendant, Gem of Focus, Ancient Signet, Rod of Asclepius, Book of Thoth,
    Polynomicon, Soul Reaver, Jade Scepter, Helm of Radiance, Ethereal Staff, Staff
    of Myrddin, Wish-Granting Pearl, Bracer of The Abyss, Nimble Ring.'
  slot_scores:
    The Cosmic Horror:
      total: 0.59
      efficiency: 0.45
      win: 0.67
      pick: 0.2
      fit: 0.79
    Totem of Death:
      total: 0.59
      efficiency: 0.4
      win: 0.75
      pick: 0.16
      fit: 0.73
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.56
      pick: 0.36
      fit: 0.79
    Doom Orb:
      total: 0.56
      efficiency: 0.53
      win: 0.5
      pick: 0.67
      fit: 0.79
    Soul Gem:
      total: 0.57
      efficiency: 0.52
      win: 0.5
      pick: 0.37
      fit: 1.0
    Dreamer's Idol:
      total: 0.61
      efficiency: 0.51
      win: 0.6
      pick: 0.8
      fit: 0.79
  community_ordered:
  - The Cosmic Horror
  - Totem of Death
  - Rod of Tahuti
  - Doom Orb
  - Soul Gem
  - Dreamer's Idol
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - The Cosmic Horror
  - The World Stone
  - Rod of Tahuti
  - Totem of Death
  - Doom Orb
  - Dreamer's Idol
  flex_slots:
  - Doom Orb
  - The World Stone
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    of the Magus, Obsidian Shard, The World Stone, Death Metal, Gluttonous Grimoire,
    Ancient Signet, Chronos'' Pendant, Bragi''s Harp, Gem of Focus, Book of Thoth,
    Polynomicon, Soul Reaver, Rod of Asclepius, Triton''s Conch, Jade Scepter, Wish-Granting
    Pearl, Helm of Radiance, Breastplate of Valor, Ethereal Staff.'
  slot_scores:
    The Cosmic Horror:
      total: 0.54
      efficiency: 0.45
      win: 0.67
      pick: 0.2
      fit: 0.47
    The World Stone:
      total: 0.49
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.56
      pick: 0.36
      fit: 0.57
    Totem of Death:
      total: 0.56
      efficiency: 0.4
      win: 0.75
      pick: 0.16
      fit: 0.53
    Doom Orb:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.67
      fit: 0.57
    Dreamer's Idol:
      total: 0.56
      efficiency: 0.51
      win: 0.6
      pick: 0.8
      fit: 0.47
  community_ordered:
  - The Cosmic Horror
  - Rod of Tahuti
  - Totem of Death
  - Doom Orb
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - The Cosmic Horror
  - Totem of Death
  - Rod of Tahuti
  - Doom Orb
  - Soul Gem
  - Dreamer's Idol
  flex_slots:
  - The Cosmic Horror
  - Doom Orb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    god: Spear of the Magus, Obsidian Shard, Gluttonous Grimoire, The World Stone,
    Chronos'' Pendant, Death Metal, Gem of Focus, Ancient Signet, Bragi''s Harp, Rod
    of Asclepius, Book of Thoth, Polynomicon, Soul Reaver, Jade Scepter, Triton''s
    Conch, Breastplate of Valor, Genji''s Guard, Helm of Radiance, Ethereal Staff.'
  slot_scores:
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.45
      win: 0.67
      pick: 0.2
      fit: 0.56
    Totem of Death:
      total: 0.57
      efficiency: 0.4
      win: 0.75
      pick: 0.16
      fit: 0.54
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.56
      pick: 0.36
      fit: 0.56
    Doom Orb:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.67
      fit: 0.56
    Soul Gem:
      total: 0.56
      efficiency: 0.52
      win: 0.5
      pick: 0.37
      fit: 0.88
    Dreamer's Idol:
      total: 0.57
      efficiency: 0.51
      win: 0.6
      pick: 0.8
      fit: 0.56
  community_ordered:
  - The Cosmic Horror
  - Totem of Death
  - Rod of Tahuti
  - Doom Orb
  - Soul Gem
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - The Cosmic Horror
  - Totem of Death
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  - Dreamer's Idol
  flex_slots:
  - Dreamer's Idol
  - The Cosmic Horror
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Asclepius, Shield of the Phoenix, Gluttonous Grimoire,
    Kinetic Cuirass, Ethereal Staff, Freya''s Tears, Spear of the Magus, Shifter''s
    Shield, Genji''s Guard, Breastplate of Valor, Lifebinder, Obsidian Shard, Helm
    of Radiance, Sphere of Negation, Erosion, Yogi''s Necklace, Eye of Providence,
    Draconic Scale, Phoenix Feather, Jade Scepter, Chandra''s Grace, Wish-Granting
    Pearl, Glorious Pridwen.'
  slot_scores:
    The Cosmic Horror:
      total: 0.53
      efficiency: 0.45
      win: 0.67
      pick: 0.2
      fit: 0.39
    Totem of Death:
      total: 0.55
      efficiency: 0.4
      win: 0.75
      pick: 0.16
      fit: 0.41
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.56
      pick: 0.36
      fit: 0.39
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.56
      efficiency: 0.52
      win: 0.5
      pick: 0.37
      fit: 0.89
    Dreamer's Idol:
      total: 0.55
      efficiency: 0.51
      win: 0.6
      pick: 0.8
      fit: 0.39
  community_ordered:
  - The Cosmic Horror
  - Totem of Death
  - Rod of Tahuti
  - Soul Gem
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - The Cosmic Horror
  - Totem of Death
  - Rod of Tahuti
  - Doom Orb
  - Soul Gem
  - Dreamer's Idol
  flex_slots:
  - Doom Orb
  - Totem of Death
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    for this god: Spear of the Magus, Obsidian Shard, Gluttonous Grimoire, The World
    Stone, Chronos'' Pendant, Ancient Signet, Gem of Focus, Rod of Asclepius, Book
    of Thoth, Polynomicon, Soul Reaver, Jade Scepter, Helm of Radiance, Ethereal Staff,
    Screeching Gargoyle, Wish-Granting Pearl, Breastplate of Valor, Bracer of The
    Abyss.'
  slot_scores:
    The Cosmic Horror:
      total: 0.6
      efficiency: 0.45
      win: 0.67
      pick: 0.2
      fit: 0.85
    Totem of Death:
      total: 0.57
      efficiency: 0.4
      win: 0.75
      pick: 0.16
      fit: 0.54
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.56
      pick: 0.36
      fit: 0.85
    Doom Orb:
      total: 0.57
      efficiency: 0.53
      win: 0.5
      pick: 0.67
      fit: 0.85
    Soul Gem:
      total: 0.57
      efficiency: 0.52
      win: 0.5
      pick: 0.37
      fit: 1.0
    Dreamer's Idol:
      total: 0.61
      efficiency: 0.51
      win: 0.6
      pick: 0.8
      fit: 0.85
  community_ordered:
  - The Cosmic Horror
  - Totem of Death
  - Rod of Tahuti
  - Doom Orb
  - Soul Gem
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Totem of Death
  - Dreamer's Idol
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Obsidian Shard,
    Bragi''s Harp, Bracer of The Abyss, Chronos'' Pendant, The World Stone, Ancient
    Signet, Death Metal, Gem of Focus, Rod of Asclepius, Book of Thoth, Polynomicon,
    Soul Reaver, Jade Scepter, Helm of Radiance, Daybreak Gavel.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.56
      pick: 0.36
      fit: 0.32
    Totem of Death:
      total: 0.54
      efficiency: 0.4
      win: 0.75
      pick: 0.16
      fit: 0.35
    Dreamer's Idol:
      total: 0.53
      efficiency: 0.51
      win: 0.6
      pick: 0.8
      fit: 0.32
  community_ordered:
  - Rod of Tahuti
  - Totem of Death
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - The Cosmic Horror
  - Totem of Death
  - Rod of Tahuti
  - Soul Gem
  - Dreamer's Idol
  flex_slots:
  - The Cosmic Horror
  - Chronos' Pendant
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Talisman of Purification — CC-immunity / cleanse
    swap_item: Talisman of Purification
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
    + fit + win/pick). Underrated for this god: Chronos'' Pendant, Gem of Focus, Spear
    of the Magus, Obsidian Shard, Gluttonous Grimoire, The World Stone, Breastplate
    of Valor, Genji''s Guard, Ancient Signet, Death Metal, Staff of Myrddin, Eye of
    Erebus, Screeching Gargoyle, Bragi''s Harp, Rod of Asclepius, Book of Thoth, Chandra''s
    Grace, Freya''s Tears, Polynomicon, Soul Reaver, Jade Scepter.'
  slot_scores:
    Chronos' Pendant:
      total: 0.51
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.63
    The Cosmic Horror:
      total: 0.52
      efficiency: 0.45
      win: 0.67
      pick: 0.2
      fit: 0.37
    Totem of Death:
      total: 0.59
      efficiency: 0.4
      win: 0.75
      pick: 0.16
      fit: 0.73
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.56
      pick: 0.36
      fit: 0.37
    Soul Gem:
      total: 0.57
      efficiency: 0.52
      win: 0.5
      pick: 0.37
      fit: 0.96
    Dreamer's Idol:
      total: 0.54
      efficiency: 0.51
      win: 0.6
      pick: 0.8
      fit: 0.37
  community_ordered:
  - The Cosmic Horror
  - Totem of Death
  - Rod of Tahuti
  - Soul Gem
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Doom Orb
  - Obsidian Shard
  - Soul Gem
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
    Underrated for this god: Spear of the Magus, Obsidian Shard, Gluttonous Grimoire,
    The World Stone, Chronos'' Pendant, Gem of Focus, Ancient Signet, Rod of Asclepius,
    Book of Thoth, Polynomicon, Soul Reaver, Jade Scepter, Helm of Radiance, Ethereal
    Staff, Staff of Myrddin, Wish-Granting Pearl, Bracer of The Abyss, Nimble Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.5
      efficiency: 0.57
      win: 0.29
      pick: 0.28
      fit: 1.0
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.56
      pick: 0.36
      fit: 0.79
    Doom Orb:
      total: 0.56
      efficiency: 0.53
      win: 0.5
      pick: 0.67
      fit: 0.79
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.89
    Soul Gem:
      total: 0.57
      efficiency: 0.52
      win: 0.5
      pick: 0.37
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Doom Orb
  - Soul Gem
  starter: *id001
---

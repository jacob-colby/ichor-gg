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
    pick_rate: 0.55
    win_rate: 0.42
    alternates:
    - name: Doom Orb
      pick_rate: 0.09
      win_rate: 0.5
    - name: The Cosmic Horror
      pick_rate: 0.09
      win_rate: 0.5
  - name: Spear of Desolation
    pick_rate: 0.23
    win_rate: 0.2
    alternates:
    - name: The Cosmic Horror
      pick_rate: 0.14
      win_rate: 0.67
    - name: Blood-Bound Book
      pick_rate: 0.14
      win_rate: 0.0
  - name: Rod of Tahuti
    pick_rate: 0.24
    win_rate: 0.2
    alternates:
    - name: Spear of the Magus
      pick_rate: 0.14
      win_rate: 0.33
    - name: The Cosmic Horror
      pick_rate: 0.1
      win_rate: 0.5
  - name: The Cosmic Horror
    pick_rate: 0.1
    win_rate: 1.0
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.25
      win_rate: 0.2
    - name: Totem of Death
      pick_rate: 0.1
      win_rate: 0.0
  - name: Soul Reaver
    pick_rate: 0.16
    win_rate: 0.67
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.26
      win_rate: 0.8
    - name: Obsidian Shard
      pick_rate: 0.16
      win_rate: 0.33
  - name: Blinking Abyss
    pick_rate: 0.17
    win_rate: 0.5
    alternates:
    - name: Killing Stone
      pick_rate: 0.17
      win_rate: 1.0
    - name: Obsidian Shard
      pick_rate: 0.17
      win_rate: 0.5
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.36
    win_rate: 0.75
  - name: Conduit Gem
    pick_rate: 0.23
    win_rate: 0.2
  - name: Pendulum of the Ages
    pick_rate: 0.18
    win_rate: 0.25
  source_url: https://smitebrain.com/gods/anubis/
  last_verified: '2026-08-26'
  god_win_rate: 0.4090909090909091
  god_matches_won: 9
  god_matches_played: 22
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-26'
  god_matches_analyzed: 888
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - The Cosmic Horror
  - Soul Reaver
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Rod of Tahuti
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
    this god: Soul Gem, Doom Orb, Gluttonous Grimoire, The World Stone, Dreamer''s
    Idol, Chronos'' Pendant, Gem of Focus, Ancient Signet, Rod of Asclepius, Book
    of Thoth, Polynomicon, Jade Scepter, Divine Ruin, Helm of Radiance, Ethereal Staff,
    Staff of Myrddin, Wish-Granting Pearl, Typhon’s Heart, Bracer of The Abyss, Nimble
    Ring.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.51
      win: 0.46
      pick: 0.0
      fit: 0.42
    The Cosmic Horror:
      total: 0.73
      efficiency: 0.45
      win: 1.0
      pick: 0.17
      fit: 0.79
    Soul Reaver:
      total: 0.55
      efficiency: 0.4
      win: 0.67
      pick: 0.35
      fit: 0.62
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.86
      win: 0.2
      pick: 0.37
      fit: 0.79
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.5
      pick: 0.52
      fit: 0.89
    Soul Gem:
      total: 0.54
      efficiency: 0.52
      win: 0.46
      pick: 0.0
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - The Cosmic Horror
  - Doom Orb
  - Soul Reaver
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Rod of Tahuti
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Doom
    Orb, Soul Gem, The World Stone, Death Metal, Gluttonous Grimoire, Ancient Signet,
    Chronos'' Pendant, Dreamer''s Idol, Bragi''s Harp, Gem of Focus, Book of Thoth,
    Polynomicon, Rod of Asclepius, Triton''s Conch, Jade Scepter, Divine Ruin, Wish-Granting
    Pearl, Helm of Radiance, Breastplate of Valor, Ethereal Staff.'
  slot_scores:
    The Cosmic Horror:
      total: 0.68
      efficiency: 0.45
      win: 1.0
      pick: 0.17
      fit: 0.47
    Doom Orb:
      total: 0.5
      efficiency: 0.53
      win: 0.5
      pick: 0.09
      fit: 0.57
    Soul Reaver:
      total: 0.55
      efficiency: 0.4
      win: 0.67
      pick: 0.35
      fit: 0.59
    Rod of Tahuti:
      total: 0.49
      efficiency: 0.86
      win: 0.2
      pick: 0.37
      fit: 0.57
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.5
      pick: 0.52
      fit: 0.57
    Soul Gem:
      total: 0.49
      efficiency: 0.52
      win: 0.46
      pick: 0.0
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - The Cosmic Horror
  - Soul Reaver
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Rod of Tahuti
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
    god: Soul Gem, Doom Orb, Gluttonous Grimoire, The World Stone, Dreamer''s Idol,
    Chronos'' Pendant, Death Metal, Gem of Focus, Ancient Signet, Bragi''s Harp, Rod
    of Asclepius, Book of Thoth, Polynomicon, Jade Scepter, Divine Ruin, Triton''s
    Conch, Breastplate of Valor, Genji''s Guard, Helm of Radiance, Ethereal Staff.'
  slot_scores:
    Book of Thoth:
      total: 0.42
      efficiency: 0.51
      win: 0.46
      pick: 0.0
      fit: 0.22
    The Cosmic Horror:
      total: 0.7
      efficiency: 0.45
      win: 1.0
      pick: 0.17
      fit: 0.56
    Soul Reaver:
      total: 0.52
      efficiency: 0.4
      win: 0.67
      pick: 0.35
      fit: 0.42
    Rod of Tahuti:
      total: 0.49
      efficiency: 0.86
      win: 0.2
      pick: 0.37
      fit: 0.56
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.5
      pick: 0.52
      fit: 0.66
    Soul Gem:
      total: 0.52
      efficiency: 0.52
      win: 0.46
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - The Cosmic Horror
  - Soul Reaver
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Rod of Tahuti
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    this god: Amanita Charm, Soul Gem, Rod of Asclepius, Shield of the Phoenix, Gluttonous
    Grimoire, Kinetic Cuirass, Ethereal Staff, Freya''s Tears, Shifter''s Shield,
    Genji''s Guard, Breastplate of Valor, Doom Orb, Lifebinder, Helm of Radiance,
    Sphere of Negation, Erosion, Yogi''s Necklace, Eye of Providence, Draconic Scale,
    Phoenix Feather, Jade Scepter, Chandra''s Grace, Wish-Granting Pearl, Glorious
    Pridwen.'
  slot_scores:
    The Cosmic Horror:
      total: 0.67
      efficiency: 0.45
      win: 1.0
      pick: 0.17
      fit: 0.39
    Soul Reaver:
      total: 0.52
      efficiency: 0.4
      win: 0.67
      pick: 0.35
      fit: 0.41
    Rod of Tahuti:
      total: 0.47
      efficiency: 0.86
      win: 0.2
      pick: 0.37
      fit: 0.39
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.5
      pick: 0.52
      fit: 0.49
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.52
      efficiency: 0.52
      win: 0.46
      pick: 0.0
      fit: 0.89
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - The Cosmic Horror
  - Doom Orb
  - Soul Reaver
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Rod of Tahuti
  - Soul Reaver
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
    for this god: Doom Orb, Soul Gem, Gluttonous Grimoire, The World Stone, Dreamer''s
    Idol, Chronos'' Pendant, Ancient Signet, Gem of Focus, Rod of Asclepius, Book
    of Thoth, Polynomicon, Jade Scepter, Divine Ruin, Helm of Radiance, Ethereal Staff,
    Screeching Gargoyle, Wish-Granting Pearl, Typhon’s Heart, Breastplate of Valor,
    Bracer of The Abyss.'
  slot_scores:
    The Cosmic Horror:
      total: 0.74
      efficiency: 0.45
      win: 1.0
      pick: 0.17
      fit: 0.85
    Doom Orb:
      total: 0.54
      efficiency: 0.53
      win: 0.5
      pick: 0.09
      fit: 0.85
    Soul Reaver:
      total: 0.53
      efficiency: 0.4
      win: 0.67
      pick: 0.35
      fit: 0.5
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.86
      win: 0.2
      pick: 0.37
      fit: 0.85
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.5
      pick: 0.52
      fit: 0.95
    Soul Gem:
      total: 0.54
      efficiency: 0.52
      win: 0.46
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - The Cosmic Horror
  - Soul Reaver
  - Rod of Tahuti
  flex_slots:
  - Rod of Tahuti
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
    this god: Nimble Ring, Soul Gem, Gluttonous Grimoire, Doom Orb, Bragi''s Harp,
    Bracer of The Abyss, Chronos'' Pendant, The World Stone, Ancient Signet, Dreamer''s
    Idol, Death Metal, Gem of Focus, Rod of Asclepius, Book of Thoth, Typhon’s Heart,
    Polynomicon, Jade Scepter, Divine Ruin, Helm of Radiance, Daybreak Gavel.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.45
      efficiency: 0.52
      win: 0.46
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.46
      efficiency: 0.44
      win: 0.46
      pick: 0.0
      fit: 0.63
    The Cosmic Horror:
      total: 0.66
      efficiency: 0.45
      win: 1.0
      pick: 0.17
      fit: 0.32
    Soul Reaver:
      total: 0.51
      efficiency: 0.4
      win: 0.67
      pick: 0.35
      fit: 0.37
    Rod of Tahuti:
      total: 0.46
      efficiency: 0.86
      win: 0.2
      pick: 0.37
      fit: 0.32
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Gem of Focus
  - The Cosmic Horror
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Gem of Focus
  - Rod of Tahuti
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
    + fit + win/pick). Underrated for this god: Soul Gem, Chronos'' Pendant, Gem of
    Focus, Doom Orb, Gluttonous Grimoire, The World Stone, Breastplate of Valor, Dreamer''s
    Idol, Genji''s Guard, Ancient Signet, Death Metal, Staff of Myrddin, Eye of Erebus,
    Screeching Gargoyle, Bragi''s Harp, Rod of Asclepius, Book of Thoth, Chandra''s
    Grace, Freya''s Tears, Polynomicon, Jade Scepter.'
  slot_scores:
    Chronos' Pendant:
      total: 0.49
      efficiency: 0.55
      win: 0.46
      pick: 0.0
      fit: 0.63
    Gem of Focus:
      total: 0.48
      efficiency: 0.5
      win: 0.46
      pick: 0.0
      fit: 0.63
    The Cosmic Horror:
      total: 0.67
      efficiency: 0.45
      win: 1.0
      pick: 0.17
      fit: 0.37
    Rod of Tahuti:
      total: 0.46
      efficiency: 0.86
      win: 0.2
      pick: 0.37
      fit: 0.37
    Obsidian Shard:
      total: 0.51
      efficiency: 0.54
      win: 0.5
      pick: 0.52
      fit: 0.47
    Soul Gem:
      total: 0.53
      efficiency: 0.52
      win: 0.46
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
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
    Underrated for this god: Soul Gem, Gluttonous Grimoire, Doom Orb, The World Stone,
    Dreamer''s Idol, Chronos'' Pendant, Gem of Focus, Ancient Signet, Rod of Asclepius,
    Book of Thoth, Polynomicon, Jade Scepter, Divine Ruin, Helm of Radiance, Ethereal
    Staff, Staff of Myrddin, Wish-Granting Pearl, Typhon’s Heart, Bracer of The Abyss,
    Nimble Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.46
      efficiency: 0.57
      win: 0.2
      pick: 0.31
      fit: 1.0
    Doom Orb:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.09
      fit: 0.79
    Spear of the Magus:
      total: 0.49
      efficiency: 0.6
      win: 0.33
      pick: 0.22
      fit: 0.79
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.86
      win: 0.2
      pick: 0.37
      fit: 0.79
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.5
      pick: 0.52
      fit: 0.89
    Soul Gem:
      total: 0.54
      efficiency: 0.52
      win: 0.46
      pick: 0.0
      fit: 1.0
  starter: *id001
---

---
type: smite-build
god: Kukulkan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Squall
  aspect_pick_rate: 0.18
  aspect_win_rate: 0.57
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.9
    win_rate: 0.51
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.05
      win_rate: 0.0
    - name: Mana Tome
      pick_rate: 0.03
      win_rate: 0.0
  - name: Spear of Desolation
    pick_rate: 0.28
    win_rate: 0.82
    alternates:
    - name: Gem of Focus
      pick_rate: 0.13
      win_rate: 0.4
    - name: Chronos' Pendant
      pick_rate: 0.1
      win_rate: 0.25
  - name: Soul Reaver
    pick_rate: 0.16
    win_rate: 0.67
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.75
    - name: Breastplate of Valor
      pick_rate: 0.11
      win_rate: 0.25
  - name: Rod of Tahuti
    pick_rate: 0.23
    win_rate: 0.5
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.14
      win_rate: 0.6
    - name: Polynomicon
      pick_rate: 0.11
      win_rate: 0.5
  - name: Obsidian Shard
    pick_rate: 0.18
    win_rate: 0.5
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.21
      win_rate: 0.43
    - name: Void Shard
      pick_rate: 0.09
      win_rate: 0.0
  - name: Mote of Chaos
    pick_rate: 0.17
    win_rate: 0.67
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.17
      win_rate: 0.33
    - name: Soul Reaver
      pick_rate: 0.11
      win_rate: 0.5
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.36
    win_rate: 0.36
  - name: Pendulum of the Ages
    pick_rate: 0.21
    win_rate: 0.63
  - name: Conduit Gem
    pick_rate: 0.13
    win_rate: 0.8
  source_url: https://smitebrain.com/gods/kukulkan/
  last_verified: '2026-08-26'
  god_win_rate: 0.48717948717948717
  god_matches_won: 19
  god_matches_played: 39
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
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of the Magus
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
    this god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom Orb, The World
    Stone, Dreamer''s Idol, The Cosmic Horror, Ancient Signet, Totem of Death, Rod
    of Asclepius, Blood-Bound Book, Jade Scepter, Divine Ruin, Bancroft''s Talon,
    Helm of Radiance, Ethereal Staff, Staff of Myrddin, Wish-Granting Pearl, Typhon’s
    Heart, Bracer of The Abyss, Nimble Ring, Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.51
      win: 0.51
      pick: 0.9
      fit: 0.42
    Spear of Desolation:
      total: 0.74
      efficiency: 0.57
      win: 0.82
      pick: 0.38
      fit: 1.0
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.5
      pick: 0.38
      fit: 0.79
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.5
      pick: 0.39
      fit: 0.89
    Soul Gem:
      total: 0.56
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Spear of Desolation
  - Soul Reaver
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Book of Thoth
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Spear of the Magus, Doom Orb, The World Stone, Death Metal, Gluttonous Grimoire,
    Ancient Signet, Dreamer''s Idol, Bragi''s Harp, The Cosmic Horror, Rod of Asclepius,
    Bancroft''s Talon, Totem of Death, Triton''s Conch, Blood-Bound Book, Jade Scepter,
    Divine Ruin, Wish-Granting Pearl, Helm of Radiance, Ethereal Staff, Chronos''
    Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.51
      win: 0.51
      pick: 0.9
      fit: 0.39
    Genji's Guard:
      total: 0.54
      efficiency: 0.45
      win: 0.75
      pick: 0.17
      fit: 0.24
    Spear of Desolation:
      total: 0.68
      efficiency: 0.57
      win: 0.82
      pick: 0.38
      fit: 0.61
    Soul Reaver:
      total: 0.54
      efficiency: 0.4
      win: 0.67
      pick: 0.25
      fit: 0.59
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.5
      pick: 0.38
      fit: 0.57
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.5
      pick: 0.39
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Spear of Desolation
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
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom Orb, The World Stone,
    Dreamer''s Idol, Death Metal, The Cosmic Horror, Ancient Signet, Bragi''s Harp,
    Totem of Death, Rod of Asclepius, Blood-Bound Book, Jade Scepter, Divine Ruin,
    Triton''s Conch, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Chronos''
    Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.51
      win: 0.51
      pick: 0.9
      fit: 0.22
    Genji's Guard:
      total: 0.54
      efficiency: 0.45
      win: 0.75
      pick: 0.17
      fit: 0.22
    Spear of Desolation:
      total: 0.71
      efficiency: 0.57
      win: 0.82
      pick: 0.38
      fit: 0.78
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.5
      pick: 0.38
      fit: 0.56
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.5
      pick: 0.39
      fit: 0.66
    Soul Gem:
      total: 0.54
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Book of Thoth
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
    Grimoire, Kinetic Cuirass, Ethereal Staff, Freya''s Tears, Spear of the Magus,
    Shifter''s Shield, Lifebinder, Helm of Radiance, Sphere of Negation, Erosion,
    Yogi''s Necklace, Eye of Providence, Draconic Scale, Phoenix Feather, Jade Scepter,
    Chandra''s Grace, Wish-Granting Pearl, Blood-Bound Book, Doom Orb, Glorious Pridwen.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.51
      pick: 0.9
      fit: 0.21
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.75
      pick: 0.17
      fit: 0.26
    Spear of Desolation:
      total: 0.66
      efficiency: 0.57
      win: 0.82
      pick: 0.38
      fit: 0.49
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.5
      pick: 0.38
      fit: 0.39
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.54
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.89
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Soul Gem
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Spear of the Magus, Soul Gem, Gluttonous Grimoire, Doom Orb, The
    World Stone, Dreamer''s Idol, The Cosmic Horror, Ancient Signet, Rod of Asclepius,
    Totem of Death, Blood-Bound Book, Jade Scepter, Divine Ruin, Bancroft''s Talon,
    Helm of Radiance, Ethereal Staff, Screeching Gargoyle, Wish-Granting Pearl, Typhon’s
    Heart, Bracer of The Abyss, Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.51
      pick: 0.9
      fit: 0.3
    Spear of Desolation:
      total: 0.74
      efficiency: 0.57
      win: 0.82
      pick: 0.38
      fit: 1.0
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.5
      pick: 0.38
      fit: 0.85
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.5
      pick: 0.39
      fit: 0.95
    Soul Gem:
      total: 0.56
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Book of Thoth
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Spear of Desolation
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear of the Magus, Bragi''s
    Harp, Bracer of The Abyss, Doom Orb, The World Stone, Ancient Signet, Blood-Bound
    Book, Dreamer''s Idol, Death Metal, Bancroft''s Talon, Rod of Asclepius, The Cosmic
    Horror, Typhon’s Heart, Totem of Death, Jade Scepter, Divine Ruin, Helm of Radiance,
    Daybreak Gavel, Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.51
      pick: 0.9
      fit: 0.17
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
    Spear of Desolation:
      total: 0.65
      efficiency: 0.57
      win: 0.82
      pick: 0.38
      fit: 0.4
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.5
      pick: 0.38
      fit: 0.32
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Spear of Desolation
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
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Spear of the Magus, Gluttonous
    Grimoire, Totem of Death, Doom Orb, The World Stone, Dreamer''s Idol, Ancient
    Signet, Death Metal, Staff of Myrddin, The Cosmic Horror, Eye of Erebus, Screeching
    Gargoyle, Bragi''s Harp, Rod of Asclepius, Chandra''s Grace, Freya''s Tears, Blood-Bound
    Book, Jade Scepter, Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.51
      pick: 0.9
      fit: 0.14
    Genji's Guard:
      total: 0.58
      efficiency: 0.45
      win: 0.75
      pick: 0.17
      fit: 0.48
    Spear of Desolation:
      total: 0.72
      efficiency: 0.57
      win: 0.82
      pick: 0.38
      fit: 0.86
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.5
      pick: 0.38
      fit: 0.37
    Obsidian Shard:
      total: 0.51
      efficiency: 0.54
      win: 0.5
      pick: 0.39
      fit: 0.47
    Soul Gem:
      total: 0.55
      efficiency: 0.52
      win: 0.5
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
    Underrated for this god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom
    Orb, The World Stone, Dreamer''s Idol, Chronos'' Pendant, The Cosmic Horror, Ancient
    Signet, Totem of Death, Rod of Asclepius, Blood-Bound Book, Jade Scepter, Divine
    Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin, Wish-Granting
    Pearl, Typhon’s Heart, Bracer of The Abyss, Nimble Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.74
      efficiency: 0.57
      win: 0.82
      pick: 0.38
      fit: 1.0
    Doom Orb:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.5
      pick: 0.38
      fit: 0.79
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.5
      pick: 0.39
      fit: 0.89
    Soul Gem:
      total: 0.56
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
---

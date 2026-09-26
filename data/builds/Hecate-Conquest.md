---
type: smite-build
god: Hecate
mode: Conquest
builds:
- source: community
  aspect: Aspect of Ruin
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.42
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.46
    win_rate: 0.57
    alternates:
    - name: Book of Thoth
      pick_rate: 0.17
      win_rate: 0.58
    - name: Chronos' Pendant
      pick_rate: 0.16
      win_rate: 0.52
  - name: The World Stone
    pick_rate: 0.35
    win_rate: 0.46
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.14
      win_rate: 0.63
    - name: Book of Thoth
      pick_rate: 0.11
      win_rate: 0.73
  - name: Soul Gem
    pick_rate: 0.25
    win_rate: 0.57
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.22
      win_rate: 0.57
    - name: Gem of Focus
      pick_rate: 0.06
      win_rate: 0.33
  - name: Rod of Tahuti
    pick_rate: 0.36
    win_rate: 0.55
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.27
      win_rate: 0.57
    - name: Soul Reaver
      pick_rate: 0.05
      win_rate: 0.56
  - name: Obsidian Shard
    pick_rate: 0.31
    win_rate: 0.59
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.14
      win_rate: 0.6
    - name: Evil Eye
      pick_rate: 0.11
      win_rate: 0.5
  - name: Evil Eye
    pick_rate: 0.18
    win_rate: 0.43
    alternates:
    - name: Dreamer's Idol
      pick_rate: 0.09
      win_rate: 0.71
    - name: Killing Stone
      pick_rate: 0.08
      win_rate: 0.33
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.28
    win_rate: 0.48
  - name: Conduit Gem
    pick_rate: 0.25
    win_rate: 0.62
  - name: Pendulum of the Ages
    pick_rate: 0.18
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/hecate/
  last_verified: '2026-09-26'
  god_win_rate: 0.5555555555555556
  god_matches_won: 110
  god_matches_played: 198
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-26'
  god_matches_analyzed: 4198
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  - Dreamer's Idol
  flex_slots:
  - Soul Gem
  - Book of Thoth
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
    this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, The Cosmic Horror,
    Ancient Signet, Totem of Death, Rod of Asclepius, Polynomicon, Soul Reaver, Blood-Bound
    Book, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal
    Staff, Staff of Myrddin, Wish-Granting Pearl, Typhon’s Heart, Bracer of The Abyss,
    Nimble Ring, Gem of Focus.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.51
      win: 0.58
      pick: 0.17
      fit: 0.41
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.57
      pick: 0.46
      fit: 1.0
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.55
      pick: 0.6
      fit: 0.77
    Obsidian Shard:
      total: 0.62
      efficiency: 0.54
      win: 0.59
      pick: 0.67
      fit: 0.87
    Soul Gem:
      total: 0.61
      efficiency: 0.52
      win: 0.57
      pick: 0.39
      fit: 1.0
    Dreamer's Idol:
      total: 0.63
      efficiency: 0.51
      win: 0.71
      pick: 0.28
      fit: 0.77
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  - Dreamer's Idol
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Ancient Signet
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  flex_slots:
  - Doom Orb
  - Ancient Signet
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
    of the Magus, Doom Orb, Death Metal, Gluttonous Grimoire, Ancient Signet, Bragi''s
    Harp, Polynomicon, Soul Reaver, The Cosmic Horror, Rod of Asclepius, Bancroft''s
    Talon, Totem of Death, Triton''s Conch, Blood-Bound Book, Jade Scepter, Divine
    Ruin, Wish-Granting Pearl, Helm of Radiance, Breastplate of Valor, Ethereal Staff,
    Gem of Focus.'
  slot_scores:
    Ancient Signet:
      total: 0.51
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.49
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.57
      pick: 0.46
      fit: 0.61
    Doom Orb:
      total: 0.52
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.55
      pick: 0.6
      fit: 0.57
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.59
      pick: 0.67
      fit: 0.57
    Dreamer's Idol:
      total: 0.58
      efficiency: 0.51
      win: 0.71
      pick: 0.28
      fit: 0.47
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  - Dreamer's Idol
  flex_slots:
  - Obsidian Shard
  - Book of Thoth
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
    god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Death Metal, The Cosmic
    Horror, Ancient Signet, Bragi''s Harp, Totem of Death, Rod of Asclepius, Polynomicon,
    Soul Reaver, Blood-Bound Book, Jade Scepter, Divine Ruin, Triton''s Conch, Breastplate
    of Valor, Bancroft''s Talon, Genji''s Guard, Helm of Radiance, Ethereal Staff,
    Gem of Focus.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.58
      pick: 0.17
      fit: 0.22
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.57
      pick: 0.46
      fit: 0.78
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.55
      pick: 0.6
      fit: 0.56
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.59
      pick: 0.67
      fit: 0.66
    Soul Gem:
      total: 0.59
      efficiency: 0.52
      win: 0.57
      pick: 0.39
      fit: 0.88
    Dreamer's Idol:
      total: 0.59
      efficiency: 0.51
      win: 0.71
      pick: 0.28
      fit: 0.56
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Spear of Desolation
  - Rod of Tahuti
  - Dreamer's Idol
  - Obsidian Shard
  - Soul Gem
  - Amanita Charm
  flex_slots:
  - Obsidian Shard
  - Spear of Desolation
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
    this god: Amanita Charm, Rod of Asclepius, Shield of the Phoenix, Gluttonous Grimoire,
    Kinetic Cuirass, Ethereal Staff, Freya''s Tears, Genji''s Guard, Spear of the
    Magus, Breastplate of Valor, Shifter''s Shield, Lifebinder, Helm of Radiance,
    Sphere of Negation, Yogi''s Necklace, Erosion, Eye of Providence, Phoenix Feather,
    Draconic Scale, Chandra''s Grace, Jade Scepter, Wish-Granting Pearl, Blood-Bound
    Book, Doom Orb, Glorious Pridwen.'
  slot_scores:
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.57
      pick: 0.46
      fit: 0.5
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.55
      pick: 0.6
      fit: 0.38
    Dreamer's Idol:
      total: 0.57
      efficiency: 0.51
      win: 0.71
      pick: 0.28
      fit: 0.38
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.59
      pick: 0.67
      fit: 0.48
    Soul Gem:
      total: 0.59
      efficiency: 0.52
      win: 0.57
      pick: 0.39
      fit: 0.9
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Dreamer's Idol
  - Obsidian Shard
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
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
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, The Cosmic Horror,
    Ancient Signet, Totem of Death, Rod of Asclepius, Polynomicon, Soul Reaver, Blood-Bound
    Book, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance, Screeching
    Gargoyle, Ethereal Staff, Wish-Granting Pearl, Typhon’s Heart, Breastplate of
    Valor, Staff of Myrddin, Gem of Focus.'
  slot_scores:
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.57
      pick: 0.46
      fit: 1.0
    Doom Orb:
      total: 0.56
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.84
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.55
      pick: 0.6
      fit: 0.84
    Obsidian Shard:
      total: 0.63
      efficiency: 0.54
      win: 0.59
      pick: 0.67
      fit: 0.94
    Soul Gem:
      total: 0.61
      efficiency: 0.52
      win: 0.57
      pick: 0.39
      fit: 1.0
    Dreamer's Idol:
      total: 0.64
      efficiency: 0.51
      win: 0.71
      pick: 0.28
      fit: 0.84
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
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
  - Soul Gem
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
    this god: Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Bragi''s Harp,
    Bracer of The Abyss, Doom Orb, Ancient Signet, Blood-Bound Book, Death Metal,
    Bancroft''s Talon, Rod of Asclepius, The Cosmic Horror, Polynomicon, Typhon’s
    Heart, Soul Reaver, Totem of Death, Jade Scepter, Divine Ruin, Helm of Radiance,
    Daybreak Gavel, Gem of Focus.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.5
      efficiency: 0.44
      win: 0.56
      pick: 0.0
      fit: 0.62
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.55
      pick: 0.6
      fit: 0.31
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.57
      pick: 0.39
      fit: 0.58
    Dreamer's Idol:
      total: 0.56
      efficiency: 0.51
      win: 0.71
      pick: 0.28
      fit: 0.31
  community_ordered:
  - Rod of Tahuti
  - Soul Gem
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  - Dreamer's Idol
  flex_slots:
  - Obsidian Shard
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
    + fit + win/pick). Underrated for this god: Spear of the Magus, Gluttonous Grimoire,
    Totem of Death, Doom Orb, Breastplate of Valor, Genji''s Guard, Ancient Signet,
    Death Metal, Staff of Myrddin, The Cosmic Horror, Eye of Erebus, Screeching Gargoyle,
    Bragi''s Harp, Rod of Asclepius, Chandra''s Grace, Freya''s Tears, Polynomicon,
    Soul Reaver, Blood-Bound Book, Jade Scepter, Gem of Focus.'
  slot_scores:
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.55
      win: 0.52
      pick: 0.16
      fit: 0.63
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.57
      pick: 0.46
      fit: 0.86
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.55
      pick: 0.6
      fit: 0.37
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.59
      pick: 0.67
      fit: 0.47
    Soul Gem:
      total: 0.6
      efficiency: 0.52
      win: 0.57
      pick: 0.39
      fit: 0.96
    Dreamer's Idol:
      total: 0.57
      efficiency: 0.51
      win: 0.71
      pick: 0.28
      fit: 0.37
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  - Dreamer's Idol
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
    Underrated for this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, The
    Cosmic Horror, Gem of Focus, Ancient Signet, Totem of Death, Rod of Asclepius,
    Polynomicon, Blood-Bound Book, Soul Reaver, Jade Scepter, Divine Ruin, Bancroft''s
    Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin, Wish-Granting Pearl,
    Typhon’s Heart, Bracer of The Abyss, Nimble Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.57
      pick: 0.46
      fit: 1.0
    Doom Orb:
      total: 0.55
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.77
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.55
      pick: 0.6
      fit: 0.77
    Obsidian Shard:
      total: 0.62
      efficiency: 0.54
      win: 0.59
      pick: 0.67
      fit: 0.87
    Soul Gem:
      total: 0.61
      efficiency: 0.52
      win: 0.57
      pick: 0.39
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
---

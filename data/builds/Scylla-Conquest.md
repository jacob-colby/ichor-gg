---
type: smite-build
god: Scylla
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Devourer
  aspect_pick_rate: 0.32
  aspect_win_rate: 0.56
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.36
    win_rate: 0.5
    alternates:
    - name: Yogi's Necklace
      pick_rate: 0.2
      win_rate: 0.64
    - name: Book of Thoth
      pick_rate: 0.16
      win_rate: 0.78
  - name: The World Stone
    pick_rate: 0.2
    win_rate: 0.55
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.25
      win_rate: 0.71
    - name: Breastplate of Valor
      pick_rate: 0.13
      win_rate: 0.86
  - name: Rod of Tahuti
    pick_rate: 0.25
    win_rate: 0.71
    alternates:
    - name: Soul Gem
      pick_rate: 0.16
      win_rate: 0.67
    - name: Polynomicon
      pick_rate: 0.14
      win_rate: 0.38
  - name: Obsidian Shard
    pick_rate: 0.27
    win_rate: 0.53
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.33
      win_rate: 0.56
    - name: Polynomicon
      pick_rate: 0.05
      win_rate: 1.0
  - name: Polynomicon
    pick_rate: 0.11
    win_rate: 0.4
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.19
      win_rate: 0.67
    - name: Dreamer's Idol
      pick_rate: 0.06
      win_rate: 0.67
  - name: Void Shard
    pick_rate: 0.09
    win_rate: 0.33
    alternates:
    - name: Killing Stone
      pick_rate: 0.09
      win_rate: 0.33
    - name: Ring of Dispel
      pick_rate: 0.06
      win_rate: 0.0
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.57
    win_rate: 0.59
  - name: Conduit Gem
    pick_rate: 0.3
    win_rate: 0.71
  - name: Pendulum of the Ages
    pick_rate: 0.05
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/scylla/
  last_verified: '2026-09-23'
  god_win_rate: 0.6071428571428571
  god_matches_won: 34
  god_matches_played: 56
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
  - Book of Thoth
  - Spear of Desolation
  - Breastplate of Valor
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Breastplate of Valor
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
    this god: Dreamer''s Idol, Spear of the Magus, Gluttonous Grimoire, Doom Orb,
    Chronos'' Pendant, The Cosmic Horror, Gem of Focus, Ancient Signet, Totem of Death,
    Rod of Asclepius, Blood-Bound Book, Soul Reaver, Jade Scepter, Divine Ruin, Bancroft''s
    Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin, Wish-Granting Pearl,
    Typhon’s Heart, Bracer of The Abyss, Nimble Ring.'
  slot_scores:
    Book of Thoth:
      total: 0.6
      efficiency: 0.51
      win: 0.78
      pick: 0.16
      fit: 0.42
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.5
      pick: 0.36
      fit: 1.0
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.47
      win: 0.86
      pick: 0.18
      fit: 0.21
    Rod of Tahuti:
      total: 0.76
      efficiency: 0.86
      win: 0.71
      pick: 0.39
      fit: 0.79
    Dreamer's Idol:
      total: 0.6
      efficiency: 0.51
      win: 0.67
      pick: 0.13
      fit: 0.79
    Soul Gem:
      total: 0.64
      efficiency: 0.52
      win: 0.67
      pick: 0.25
      fit: 1.0
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Breastplate of Valor
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Breastplate of Valor
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Dreamer's Idol
  - Obsidian Shard
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Dreamer''s
    Idol, Spear of the Magus, Doom Orb, Death Metal, Gluttonous Grimoire, Ancient
    Signet, Chronos'' Pendant, Bragi''s Harp, Gem of Focus, Soul Reaver, The Cosmic
    Horror, Rod of Asclepius, Bancroft''s Talon, Totem of Death, Triton''s Conch,
    Blood-Bound Book, Jade Scepter, Divine Ruin, Wish-Granting Pearl, Helm of Radiance,
    Ethereal Staff.'
  slot_scores:
    Book of Thoth:
      total: 0.6
      efficiency: 0.51
      win: 0.78
      pick: 0.16
      fit: 0.39
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.47
      win: 0.86
      pick: 0.18
      fit: 0.24
    Rod of Tahuti:
      total: 0.72
      efficiency: 0.86
      win: 0.71
      pick: 0.39
      fit: 0.57
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.53
      pick: 0.45
      fit: 0.57
    Dreamer's Idol:
      total: 0.56
      efficiency: 0.51
      win: 0.67
      pick: 0.13
      fit: 0.47
    Soul Gem:
      total: 0.6
      efficiency: 0.52
      win: 0.67
      pick: 0.25
      fit: 0.71
  community_ordered:
  - Book of Thoth
  - Breastplate of Valor
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Breastplate of Valor
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Dreamer's Idol
  - Spear of Desolation
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Dreamer''s Idol, Spear of the Magus, Gluttonous Grimoire, Doom Orb, Chronos''
    Pendant, Death Metal, Gem of Focus, The Cosmic Horror, Ancient Signet, Bragi''s
    Harp, Totem of Death, Rod of Asclepius, Blood-Bound Book, Soul Reaver, Jade Scepter,
    Divine Ruin, Triton''s Conch, Bancroft''s Talon, Genji''s Guard, Helm of Radiance,
    Ethereal Staff.'
  slot_scores:
    Book of Thoth:
      total: 0.57
      efficiency: 0.51
      win: 0.78
      pick: 0.16
      fit: 0.22
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.36
      fit: 0.78
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.47
      win: 0.86
      pick: 0.18
      fit: 0.22
    Rod of Tahuti:
      total: 0.72
      efficiency: 0.86
      win: 0.71
      pick: 0.39
      fit: 0.56
    Dreamer's Idol:
      total: 0.57
      efficiency: 0.51
      win: 0.67
      pick: 0.13
      fit: 0.56
    Soul Gem:
      total: 0.63
      efficiency: 0.52
      win: 0.67
      pick: 0.25
      fit: 0.88
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Breastplate of Valor
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Breastplate of Valor
  - Rod of Tahuti
  - Dreamer's Idol
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Book of Thoth
  - Dreamer's Idol
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
    Kinetic Cuirass, Ethereal Staff, Freya''s Tears, Spear of the Magus, Shifter''s
    Shield, Genji''s Guard, Lifebinder, Helm of Radiance, Sphere of Negation, Erosion,
    Eye of Providence, Draconic Scale, Phoenix Feather, Jade Scepter, Chandra''s Grace,
    Wish-Granting Pearl, Blood-Bound Book, Doom Orb, Glorious Pridwen.'
  slot_scores:
    Book of Thoth:
      total: 0.57
      efficiency: 0.51
      win: 0.78
      pick: 0.16
      fit: 0.21
    Breastplate of Valor:
      total: 0.66
      efficiency: 0.65
      win: 0.86
      pick: 0.18
      fit: 0.26
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.71
      pick: 0.39
      fit: 0.39
    Dreamer's Idol:
      total: 0.54
      efficiency: 0.51
      win: 0.67
      pick: 0.13
      fit: 0.39
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.63
      efficiency: 0.52
      win: 0.67
      pick: 0.25
      fit: 0.89
  community_ordered:
  - Book of Thoth
  - Breastplate of Valor
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Dreamer''s Idol, Spear of the Magus, Gluttonous Grimoire, Doom Orb,
    The Cosmic Horror, Chronos'' Pendant, Ancient Signet, Gem of Focus, Rod of Asclepius,
    Totem of Death, Blood-Bound Book, Soul Reaver, Jade Scepter, Divine Ruin, Bancroft''s
    Talon, Helm of Radiance, Ethereal Staff, Screeching Gargoyle, Wish-Granting Pearl,
    Typhon’s Heart, Bracer of The Abyss.'
  slot_scores:
    Book of Thoth:
      total: 0.58
      efficiency: 0.51
      win: 0.78
      pick: 0.16
      fit: 0.3
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.5
      pick: 0.36
      fit: 1.0
    Rod of Tahuti:
      total: 0.77
      efficiency: 0.86
      win: 0.71
      pick: 0.39
      fit: 0.85
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.53
      pick: 0.45
      fit: 0.95
    Dreamer's Idol:
      total: 0.61
      efficiency: 0.51
      win: 0.67
      pick: 0.13
      fit: 0.85
    Soul Gem:
      total: 0.64
      efficiency: 0.52
      win: 0.67
      pick: 0.25
      fit: 1.0
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Book of Thoth
  - Bracer of The Abyss
  - Nimble Ring
  - Rod of Tahuti
  - Bragi's Harp
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
    this god: Nimble Ring, Dreamer''s Idol, Gluttonous Grimoire, Spear of the Magus,
    Bragi''s Harp, Bracer of The Abyss, Doom Orb, Chronos'' Pendant, Ancient Signet,
    Blood-Bound Book, Death Metal, Bancroft''s Talon, Gem of Focus, Rod of Asclepius,
    The Cosmic Horror, Typhon’s Heart, Soul Reaver, Totem of Death, Jade Scepter,
    Divine Ruin, Helm of Radiance, Daybreak Gavel.'
  slot_scores:
    Book of Thoth:
      total: 0.56
      efficiency: 0.51
      win: 0.78
      pick: 0.16
      fit: 0.17
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.71
      pick: 0.39
      fit: 0.32
    Bragi's Harp:
      total: 0.5
      efficiency: 0.44
      win: 0.55
      pick: 0.0
      fit: 0.63
    Soul Gem:
      total: 0.6
      efficiency: 0.57
      win: 0.67
      pick: 0.25
      fit: 0.58
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Breastplate of Valor
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Book of Thoth
  - Dreamer's Idol
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Talisman of Purification — CC-immunity / cleanse
    swap_item: Talisman of Purification
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Dreamer''s Idol, Chronos'' Pendant,
    Gem of Focus, Spear of the Magus, Gluttonous Grimoire, Totem of Death, Doom Orb,
    Genji''s Guard, Ancient Signet, Death Metal, Staff of Myrddin, The Cosmic Horror,
    Eye of Erebus, Screeching Gargoyle, Bragi''s Harp, Rod of Asclepius, Chandra''s
    Grace, Freya''s Tears, Blood-Bound Book, Soul Reaver, Jade Scepter.'
  slot_scores:
    Book of Thoth:
      total: 0.56
      efficiency: 0.51
      win: 0.78
      pick: 0.16
      fit: 0.14
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.5
      pick: 0.36
      fit: 0.86
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.47
      win: 0.86
      pick: 0.18
      fit: 0.48
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.71
      pick: 0.39
      fit: 0.37
    Dreamer's Idol:
      total: 0.54
      efficiency: 0.51
      win: 0.67
      pick: 0.13
      fit: 0.37
    Soul Gem:
      total: 0.64
      efficiency: 0.52
      win: 0.67
      pick: 0.25
      fit: 0.96
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Breastplate of Valor
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
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
    Underrated for this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s
    Idol, Chronos'' Pendant, The Cosmic Horror, Gem of Focus, Ancient Signet, Totem
    of Death, Rod of Asclepius, Blood-Bound Book, Soul Reaver, Jade Scepter, Divine
    Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin, Wish-Granting
    Pearl, Typhon’s Heart, Bracer of The Abyss, Nimble Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.5
      pick: 0.36
      fit: 1.0
    Doom Orb:
      total: 0.55
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.76
      efficiency: 0.86
      win: 0.71
      pick: 0.39
      fit: 0.79
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.53
      pick: 0.45
      fit: 0.89
    Soul Gem:
      total: 0.64
      efficiency: 0.52
      win: 0.67
      pick: 0.25
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
---

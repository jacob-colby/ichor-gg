---
type: smite-build
god: Kukulkan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Squall
  aspect_pick_rate: 0.28
  aspect_win_rate: 0.47
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.87
    win_rate: 0.53
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.03
      win_rate: 0.5
    - name: Jade Scepter
      pick_rate: 0.03
      win_rate: 1.0
  - name: Chronos' Pendant
    pick_rate: 0.27
    win_rate: 0.5
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.12
      win_rate: 0.38
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.29
  - name: Rod of Tahuti
    pick_rate: 0.24
    win_rate: 0.67
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.14
      win_rate: 0.67
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.29
  - name: Obsidian Shard
    pick_rate: 0.24
    win_rate: 0.47
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.15
      win_rate: 0.78
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.25
  - name: Dreamer's Idol
    pick_rate: 0.08
    win_rate: 0.8
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.27
      win_rate: 0.5
    - name: Obsidian Shard
      pick_rate: 0.17
      win_rate: 0.6
  - name: Time-lock Aegis
    pick_rate: 0.12
    win_rate: 0.25
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.09
      win_rate: 0.33
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.67
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.54
    win_rate: 0.53
  - name: Conduit Gem
    pick_rate: 0.27
    win_rate: 0.44
  - name: Pendulum of the Ages
    pick_rate: 0.09
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/kukulkan/
  last_verified: '2026-09-23'
  god_win_rate: 0.5522388059701493
  god_matches_won: 37
  god_matches_played: 67
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
  - Nimble Ring
  - Spear of Desolation
  - Jade Scepter
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  flex_slots:
  - Obsidian Shard
  - Nimble Ring
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jade Scepter, Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom
    Orb, The World Stone, The Cosmic Horror, Gem of Focus, Ancient Signet, Totem of
    Death, Rod of Asclepius, Polynomicon, Blood-Bound Book, Soul Reaver, Divine Ruin,
    Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin, Wish-Granting
    Pearl, Typhon’s Heart, Bracer of The Abyss, Nimble Ring.'
  slot_scores:
    Nimble Ring:
      total: 0.42
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.42
    Spear of Desolation:
      total: 0.66
      efficiency: 0.57
      win: 0.67
      pick: 0.22
      fit: 1.0
    Jade Scepter:
      total: 0.68
      efficiency: 0.48
      win: 1.0
      pick: 0.03
      fit: 0.42
    Rod of Tahuti:
      total: 0.74
      efficiency: 0.86
      win: 0.67
      pick: 0.37
      fit: 0.79
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.47
      pick: 0.4
      fit: 0.89
    Dreamer's Idol:
      total: 0.66
      efficiency: 0.51
      win: 0.8
      pick: 0.17
      fit: 0.79
  community_ordered:
  - Spear of Desolation
  - Jade Scepter
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Doom Orb
  - Jade Scepter
  - Rod of Tahuti
  - Dreamer's Idol
  flex_slots:
  - Book of Thoth
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jade
    Scepter, Soul Gem, Spear of the Magus, Doom Orb, The World Stone, Death Metal,
    Gluttonous Grimoire, Ancient Signet, Bragi''s Harp, Gem of Focus, Polynomicon,
    Soul Reaver, The Cosmic Horror, Rod of Asclepius, Bancroft''s Talon, Totem of
    Death, Triton''s Conch, Blood-Bound Book, Divine Ruin, Wish-Granting Pearl, Helm
    of Radiance, Ethereal Staff, Breastplate of Valor.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.51
      win: 0.53
      pick: 0.87
      fit: 0.39
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.67
      pick: 0.22
      fit: 0.61
    Doom Orb:
      total: 0.5
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.57
    Jade Scepter:
      total: 0.66
      efficiency: 0.48
      win: 1.0
      pick: 0.03
      fit: 0.29
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.86
      win: 0.67
      pick: 0.37
      fit: 0.57
    Dreamer's Idol:
      total: 0.62
      efficiency: 0.51
      win: 0.8
      pick: 0.17
      fit: 0.47
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Jade Scepter
  - Rod of Tahuti
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Nimble Ring
  - Spear of Desolation
  - Jade Scepter
  - Rod of Tahuti
  - Dreamer's Idol
  flex_slots:
  - Book of Thoth
  - Nimble Ring
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jade Scepter, Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom Orb,
    The World Stone, Death Metal, Gem of Focus, The Cosmic Horror, Ancient Signet,
    Bragi''s Harp, Totem of Death, Rod of Asclepius, Polynomicon, Blood-Bound Book,
    Soul Reaver, Divine Ruin, Triton''s Conch, Bancroft''s Talon, Helm of Radiance,
    Ethereal Staff, Breastplate of Valor.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.51
      win: 0.53
      pick: 0.87
      fit: 0.22
    Nimble Ring:
      total: 0.39
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.22
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.67
      pick: 0.22
      fit: 0.78
    Jade Scepter:
      total: 0.65
      efficiency: 0.48
      win: 1.0
      pick: 0.03
      fit: 0.22
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.67
      pick: 0.37
      fit: 0.56
    Dreamer's Idol:
      total: 0.63
      efficiency: 0.51
      win: 0.8
      pick: 0.17
      fit: 0.56
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Jade Scepter
  - Rod of Tahuti
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Spear of Desolation
  - Jade Scepter
  - Dreamer's Idol
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Amanita Charm
  - Soul Gem
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
    this god: Jade Scepter, Amanita Charm, Soul Gem, Rod of Asclepius, Shield of the
    Phoenix, Gluttonous Grimoire, Kinetic Cuirass, Ethereal Staff, Freya''s Tears,
    Spear of the Magus, Shifter''s Shield, Lifebinder, Helm of Radiance, Sphere of
    Negation, Erosion, Yogi''s Necklace, Eye of Providence, Draconic Scale, Phoenix
    Feather, Chandra''s Grace, Wish-Granting Pearl, Blood-Bound Book, Doom Orb, Glorious
    Pridwen, Breastplate of Valor.'
  slot_scores:
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.67
      pick: 0.22
      fit: 0.49
    Jade Scepter:
      total: 0.7
      efficiency: 0.54
      win: 1.0
      pick: 0.03
      fit: 0.4
    Dreamer's Idol:
      total: 0.6
      efficiency: 0.51
      win: 0.8
      pick: 0.17
      fit: 0.39
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.67
      pick: 0.37
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
  community_ordered:
  - Spear of Desolation
  - Jade Scepter
  - Dreamer's Idol
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Jade Scepter
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  flex_slots:
  - Obsidian Shard
  - Nimble Ring
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
    for this god: Jade Scepter, Spear of the Magus, Soul Gem, Gluttonous Grimoire,
    Doom Orb, The World Stone, The Cosmic Horror, Ancient Signet, Gem of Focus, Rod
    of Asclepius, Totem of Death, Polynomicon, Blood-Bound Book, Soul Reaver, Divine
    Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Screeching Gargoyle,
    Wish-Granting Pearl, Typhon’s Heart, Bracer of The Abyss, Breastplate of Valor.'
  slot_scores:
    Nimble Ring:
      total: 0.41
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.3
    Spear of Desolation:
      total: 0.66
      efficiency: 0.57
      win: 0.67
      pick: 0.22
      fit: 1.0
    Jade Scepter:
      total: 0.66
      efficiency: 0.48
      win: 1.0
      pick: 0.03
      fit: 0.3
    Rod of Tahuti:
      total: 0.75
      efficiency: 0.86
      win: 0.67
      pick: 0.37
      fit: 0.85
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.47
      pick: 0.4
      fit: 0.95
    Dreamer's Idol:
      total: 0.67
      efficiency: 0.51
      win: 0.8
      pick: 0.17
      fit: 0.85
  community_ordered:
  - Spear of Desolation
  - Jade Scepter
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Jade Scepter
  - Rod of Tahuti
  - Dreamer's Idol
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jade Scepter, Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear of the
    Magus, Bragi''s Harp, Bracer of The Abyss, Doom Orb, The World Stone, Ancient
    Signet, Blood-Bound Book, Death Metal, Bancroft''s Talon, Gem of Focus, Rod of
    Asclepius, The Cosmic Horror, Typhon’s Heart, Polynomicon, Soul Reaver, Totem
    of Death, Divine Ruin, Helm of Radiance, Daybreak Gavel.'
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
    Jade Scepter:
      total: 0.64
      efficiency: 0.48
      win: 1.0
      pick: 0.03
      fit: 0.17
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.67
      pick: 0.37
      fit: 0.32
    Dreamer's Idol:
      total: 0.59
      efficiency: 0.51
      win: 0.8
      pick: 0.17
      fit: 0.32
  community_ordered:
  - Jade Scepter
  - Rod of Tahuti
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Jade Scepter
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Chronos' Pendant
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Talisman of Purification — CC-immunity / cleanse
    swap_item: Talisman of Purification
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
    + fit + win/pick). Underrated for this god: Jade Scepter, Soul Gem, Gem of Focus,
    Spear of the Magus, Gluttonous Grimoire, Totem of Death, Doom Orb, The World Stone,
    Ancient Signet, Death Metal, Staff of Myrddin, The Cosmic Horror, Eye of Erebus,
    Screeching Gargoyle, Bragi''s Harp, Rod of Asclepius, Chandra''s Grace, Freya''s
    Tears, Polynomicon, Blood-Bound Book, Soul Reaver, Breastplate of Valor.'
  slot_scores:
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.55
      win: 0.5
      pick: 0.37
      fit: 0.63
    Spear of Desolation:
      total: 0.64
      efficiency: 0.57
      win: 0.67
      pick: 0.22
      fit: 0.86
    Jade Scepter:
      total: 0.64
      efficiency: 0.48
      win: 1.0
      pick: 0.03
      fit: 0.14
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.67
      pick: 0.37
      fit: 0.37
    Dreamer's Idol:
      total: 0.6
      efficiency: 0.51
      win: 0.8
      pick: 0.17
      fit: 0.37
    Soul Gem:
      total: 0.55
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Jade Scepter
  - Rod of Tahuti
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
    Underrated for this god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom
    Orb, The World Stone, The Cosmic Horror, Gem of Focus, Ancient Signet, Totem of
    Death, Rod of Asclepius, Polynomicon, Blood-Bound Book, Soul Reaver, Jade Scepter,
    Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin,
    Wish-Granting Pearl, Typhon’s Heart, Bracer of The Abyss, Nimble Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.66
      efficiency: 0.57
      win: 0.67
      pick: 0.22
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
      total: 0.74
      efficiency: 0.86
      win: 0.67
      pick: 0.37
      fit: 0.79
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.47
      pick: 0.4
      fit: 0.89
    Soul Gem:
      total: 0.56
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
---

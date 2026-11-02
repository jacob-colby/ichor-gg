---
type: smite-build
god: Vulcan
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fortification
  aspect_pick_rate: 0.09
  aspect_win_rate: 0.49
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.51
    win_rate: 0.57
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.29
      win_rate: 0.55
    - name: Chronos' Pendant
      pick_rate: 0.06
      win_rate: 0.6
  - name: Spear of Desolation
    pick_rate: 0.27
    win_rate: 0.63
    alternates:
    - name: Book of Thoth
      pick_rate: 0.16
      win_rate: 0.56
    - name: The World Stone
      pick_rate: 0.12
      win_rate: 0.59
  - name: Rod of Tahuti
    pick_rate: 0.23
    win_rate: 0.57
    alternates:
    - name: The World Stone
      pick_rate: 0.17
      win_rate: 0.53
    - name: Spear of Desolation
      pick_rate: 0.12
      win_rate: 0.57
  - name: Obsidian Shard
    pick_rate: 0.17
    win_rate: 0.51
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.34
      win_rate: 0.62
    - name: The World Stone
      pick_rate: 0.07
      win_rate: 0.64
  - name: Evil Eye
    pick_rate: 0.08
    win_rate: 0.53
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.23
      win_rate: 0.59
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.55
  - name: Shrapnel Mod
    pick_rate: 0.18
    win_rate: 0.55
    alternates:
    - name: Thermal Mod
      pick_rate: 0.11
      win_rate: 0.59
    - name: Surplus Mod
      pick_rate: 0.1
      win_rate: 0.47
  - name: Surplus Mod
    pick_rate: 0.25
    win_rate: 0.57
    alternates:
    - name: Shrapnel Mod
      pick_rate: 0.37
      win_rate: 0.61
    - name: Thermal Mod
      pick_rate: 0.2
      win_rate: 0.55
  - name: Thermal Mod
    pick_rate: 0.11
    win_rate: 0.57
    alternates:
    - name: Surplus Mod
      pick_rate: 0.7
      win_rate: 0.6
    - name: Seismic Mod
      pick_rate: 0.1
      win_rate: 0.53
  - name: Seismic Mod
    pick_rate: 0.3
    win_rate: 0.5
    alternates:
    - name: Surplus Mod
      pick_rate: 0.7
      win_rate: 0.62
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.32
    win_rate: 0.61
  - name: Pendulum of the Ages
    pick_rate: 0.29
    win_rate: 0.59
  - name: Conduit Gem
    pick_rate: 0.19
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/vulcan/
  last_verified: '2026-11-02'
  god_win_rate: 0.5645677694770544
  god_matches_won: 529
  god_matches_played: 937
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14397
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Nimble Ring
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Nimble Ring
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
    this god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom Orb, Chronos''
    Pendant, Nimble Ring, Dreamer''s Idol, The Cosmic Horror, Bracer of The Abyss,
    Heartwood Charm, Gem of Focus, Eros'' Bow, Ancient Signet, Polynomicon, Blood-Bound
    Book, Totem of Death, Soul Reaver, Divine Ruin, Jade Scepter, Bancroft''s Talon,
    Helm of Radiance, Ethereal Staff, Staff of Myrddin, Typhon’s Heart, Bragi''s Harp.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.48
      win: 0.57
      pick: 0.51
      fit: 0.35
    Nimble Ring:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.51
    Spear of Desolation:
      total: 0.62
      efficiency: 0.56
      win: 0.63
      pick: 0.37
      fit: 0.83
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.81
      win: 0.57
      pick: 0.36
      fit: 0.66
    Spear of the Magus:
      total: 0.54
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.66
    Obsidian Shard:
      total: 0.55
      efficiency: 0.55
      win: 0.51
      pick: 0.28
      fit: 0.76
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Nimble Ring
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Doom Orb
  flex_slots:
  - Nimble Ring
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Sundering Echo, Chronos'' Pendant, Doom Orb, Death Metal, Spear of the Magus,
    Bragi''s Harp, Nimble Ring, Gluttonous Grimoire, Heartwood Charm, Ancient Signet,
    Polynomicon, Dreamer''s Idol, Gem of Focus, Bracer of The Abyss, Soul Reaver,
    The Cosmic Horror, Blood-Bound Book, Eros'' Bow, Bancroft''s Talon, Totem of Death,
    Triton''s Conch, Divine Ruin, Genji''s Guard, Jade Scepter.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.48
      win: 0.57
      pick: 0.51
      fit: 0.35
    Nimble Ring:
      total: 0.5
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.35
    Spear of Desolation:
      total: 0.58
      efficiency: 0.56
      win: 0.63
      pick: 0.37
      fit: 0.56
    The World Stone:
      total: 0.51
      efficiency: 0.5
      win: 0.53
      pick: 0.26
      fit: 0.52
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.81
      win: 0.57
      pick: 0.36
      fit: 0.52
    Doom Orb:
      total: 0.51
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.52
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Chronos' Pendant
  - Nimble Ring
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Chronos' Pendant
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
    god: Soul Gem, Spear of the Magus, Chronos'' Pendant, Gluttonous Grimoire, Sundering
    Echo, Doom Orb, Nimble Ring, Dreamer''s Idol, Death Metal, Bragi''s Harp, The
    Cosmic Horror, Heartwood Charm, Gem of Focus, Bracer of The Abyss, Ancient Signet,
    Polynomicon, Blood-Bound Book, Totem of Death, Eros'' Bow, Soul Reaver, Genji''s
    Guard, Damaru, Divine Ruin, Jade Scepter, Bancroft''s Talon.'
  slot_scores:
    Chronos' Pendant:
      total: 0.51
      efficiency: 0.52
      win: 0.6
      pick: 0.06
      fit: 0.4
    Nimble Ring:
      total: 0.5
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.3
    Spear of Desolation:
      total: 0.6
      efficiency: 0.56
      win: 0.63
      pick: 0.37
      fit: 0.7
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.81
      win: 0.57
      pick: 0.36
      fit: 0.5
    Spear of the Magus:
      total: 0.52
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.5
    Obsidian Shard:
      total: 0.53
      efficiency: 0.55
      win: 0.51
      pick: 0.28
      fit: 0.6
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Kinetic Cuirass
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Book of Thoth
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
    this god: Amanita Charm, Soul Gem, Shield of the Phoenix, Gluttonous Grimoire,
    Kinetic Cuirass, Ethereal Staff, Genji''s Guard, Yogi''s Necklace, Phoenix Feather,
    Blood-Bound Book, Freya''s Tears, Breastplate of Valor, Rod of Asclepius, Sphere
    of Negation, Chandra''s Grace, Helm of Radiance, Spear of the Magus, Eros'' Bow,
    Helm of Darkness, Erosion, Nimble Ring, Oni Hunter''s Garb, Eye of Providence,
    Draconic Scale, Doom Orb, Jade Scepter, Midgardian Mail.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.48
      win: 0.57
      pick: 0.51
      fit: 0.19
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.56
      efficiency: 0.56
      win: 0.63
      pick: 0.37
      fit: 0.45
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.81
      win: 0.57
      pick: 0.36
      fit: 0.36
    Amanita Charm:
      total: 0.59
      efficiency: 0.62
      win: 0.57
      pick: 0.0
      fit: 0.76
    Soul Gem:
      total: 0.56
      efficiency: 0.5
      win: 0.57
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Doom Orb
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s
    Idol, The Cosmic Horror, Chronos'' Pendant, Nimble Ring, Bracer of The Abyss,
    Heartwood Charm, Gem of Focus, Ancient Signet, Eros'' Bow, Polynomicon, Blood-Bound
    Book, Totem of Death, Soul Reaver, Divine Ruin, Jade Scepter, Bancroft''s Talon,
    Screeching Gargoyle, Helm of Radiance, Ethereal Staff, Genji''s Guard, Typhon’s
    Heart.'
  slot_scores:
    Nimble Ring:
      total: 0.51
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.38
    Spear of Desolation:
      total: 0.63
      efficiency: 0.56
      win: 0.63
      pick: 0.37
      fit: 0.88
    Doom Orb:
      total: 0.55
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.75
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.81
      win: 0.57
      pick: 0.36
      fit: 0.75
    Spear of the Magus:
      total: 0.56
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.75
    Obsidian Shard:
      total: 0.56
      efficiency: 0.55
      win: 0.51
      pick: 0.28
      fit: 0.85
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Spear of Desolation
  - Bragi's Harp
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
    this god: Nimble Ring, Soul Gem, Gluttonous Grimoire, Sundering Echo, Bragi''s
    Harp, Spear of the Magus, Chronos'' Pendant, Blood-Bound Book, Bracer of The Abyss,
    Doom Orb, Eros'' Bow, Death Metal, Dreamer''s Idol, Bancroft''s Talon, Ancient
    Signet, Heartwood Charm, Polynomicon, Gem of Focus, The Cosmic Horror, Typhon’s
    Heart, Soul Reaver, Totem of Death, Divine Ruin, Jade Scepter, Genji''s Guard.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.49
      win: 0.57
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.54
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.56
      efficiency: 0.56
      win: 0.63
      pick: 0.37
      fit: 0.4
    Bragi's Harp:
      total: 0.49
      efficiency: 0.41
      win: 0.57
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.81
      win: 0.57
      pick: 0.36
      fit: 0.32
    Soul Gem:
      total: 0.54
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.58
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Chronos' Pendant
  - Spear of Desolation
  - Heartwood Charm
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Heartwood Charm
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
    + fit + win/pick). Underrated for this god: Soul Gem, Chronos'' Pendant, Heartwood
    Charm, Gem of Focus, Spear of the Magus, Sundering Echo, Gluttonous Grimoire,
    Nimble Ring, Totem of Death, Doom Orb, Genji''s Guard, Damaru, Breastplate of
    Valor, Death Metal, Dreamer''s Idol, Bragi''s Harp, Chandra''s Grace, Bracer of
    The Abyss, The Cosmic Horror, Ancient Signet, Polynomicon, Blood-Bound Book, Eros''
    Bow, Staff of Myrddin, Screeching Gargoyle.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.48
      win: 0.57
      pick: 0.51
      fit: 0.13
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.52
      win: 0.6
      pick: 0.06
      fit: 0.56
    Spear of Desolation:
      total: 0.61
      efficiency: 0.56
      win: 0.63
      pick: 0.37
      fit: 0.76
    Heartwood Charm:
      total: 0.51
      efficiency: 0.47
      win: 0.57
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.81
      win: 0.57
      pick: 0.36
      fit: 0.33
    Soul Gem:
      total: 0.56
      efficiency: 0.5
      win: 0.57
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Book of Thoth
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
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
  - Spear of the Magus
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
    Orb, Nimble Ring, Dreamer''s Idol, Chronos'' Pendant, The Cosmic Horror, Bracer
    of The Abyss, Heartwood Charm, Gem of Focus, Eros'' Bow, Ancient Signet, Polynomicon,
    Blood-Bound Book, Totem of Death, Soul Reaver, Divine Ruin, Jade Scepter, Bancroft''s
    Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin, Typhon’s Heart, Bragi''s
    Harp.'
  slot_scores:
    Spear of Desolation:
      total: 0.62
      efficiency: 0.56
      win: 0.63
      pick: 0.37
      fit: 0.83
    Doom Orb:
      total: 0.53
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.66
    Spear of the Magus:
      total: 0.54
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.81
      win: 0.57
      pick: 0.36
      fit: 0.66
    Obsidian Shard:
      total: 0.55
      efficiency: 0.55
      win: 0.51
      pick: 0.28
      fit: 0.76
    Soul Gem:
      total: 0.57
      efficiency: 0.5
      win: 0.57
      pick: 0.0
      fit: 0.93
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
---

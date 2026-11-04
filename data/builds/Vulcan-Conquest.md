---
type: smite-build
god: Vulcan
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fortification
  aspect_pick_rate: 0.33
  aspect_win_rate: 0.0
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.67
    win_rate: 0.0
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.33
      win_rate: 1.0
  - name: The World Stone
    pick_rate: 0.33
    win_rate: 1.0
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.33
      win_rate: 0.0
    - name: Spear of Desolation
      pick_rate: 0.33
      win_rate: 0.0
  - name: Rod of Tahuti
    pick_rate: 0.33
    win_rate: 1.0
    alternates:
    - name: Yogi's Necklace
      pick_rate: 0.33
      win_rate: 0.0
    - name: Soul Gem
      pick_rate: 0.33
      win_rate: 0.0
  - name: Talisman of Purification
    pick_rate: 0.33
    win_rate: 1.0
    alternates:
    - name: Genji's Guard
      pick_rate: 0.33
      win_rate: 0.0
    - name: Rod of Tahuti
      pick_rate: 0.33
      win_rate: 0.0
  - name: Obsidian Shard
    pick_rate: 0.67
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.33
      win_rate: 0.0
  - name: Circe's Hexstone
    pick_rate: 0.33
    win_rate: 1.0
    alternates:
    - name: Shrapnel Mod
      pick_rate: 0.33
      win_rate: 0.0
    - name: Breastplate of Valor
      pick_rate: 0.33
      win_rate: 0.0
  - name: Efficiency Mod
    pick_rate: 0.33
    win_rate: 1.0
    alternates:
    - name: Surplus Mod
      pick_rate: 0.33
      win_rate: 0.0
    - name: Shrapnel Mod
      pick_rate: 0.33
      win_rate: 0.0
  - name: Thermal Mod
    pick_rate: 0.5
    win_rate: 1.0
    alternates:
    - name: Surplus Mod
      pick_rate: 0.5
      win_rate: 0.0
  - name: Surplus Mod
    pick_rate: 1.0
    win_rate: 1.0
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.67
    win_rate: 0.5
  - name: Sands Of Time
    pick_rate: 0.33
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/vulcan/
  last_verified: '2026-11-04'
  god_win_rate: 0.3333333333333333
  god_matches_won: 1
  god_matches_played: 3
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-04'
  god_matches_analyzed: 149
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Nimble Ring
  - The World Stone
  - Talisman of Purification
  - Rod of Tahuti
  - Obsidian Shard
  - Circe's Hexstone
  flex_slots:
  - Talisman of Purification
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Helm of Darkness — magical protection
    swap_item: Helm of Darkness
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Nimble Ring, Dreamer''s
    Idol, Chronos'' Pendant, Ancient Signet, The Cosmic Horror, Bracer of The Abyss,
    Gem of Focus, Heartwood Charm, Blood-Bound Book, Polynomicon, Totem of Death,
    Soul Reaver, Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm of Radiance, Ethereal
    Staff, Typhon’s Heart, Staff of Myrddin, Bragi''s Harp.'
  slot_scores:
    Nimble Ring:
      total: 0.39
      efficiency: 0.58
      win: 0.25
      pick: 0.0
      fit: 0.51
    The World Stone:
      total: 0.76
      efficiency: 0.52
      win: 1.0
      pick: 0.45
      fit: 0.66
    Talisman of Purification:
      total: 0.57
      efficiency: 0.18
      win: 1.0
      pick: 0.55
      fit: 0.17
    Rod of Tahuti:
      total: 0.88
      efficiency: 0.86
      win: 1.0
      pick: 0.51
      fit: 0.66
    Obsidian Shard:
      total: 0.59
      efficiency: 0.58
      win: 0.5
      pick: 1.0
      fit: 0.76
    Circe's Hexstone:
      total: 0.58
      efficiency: 0.16
      win: 1.0
      pick: 1.0
      fit: 0.17
  community_ordered:
  - The World Stone
  - Talisman of Purification
  - Rod of Tahuti
  - Obsidian Shard
  - Circe's Hexstone
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - The World Stone
  - Talisman of Purification
  - Rod of Tahuti
  - Obsidian Shard
  - Circe's Hexstone
  flex_slots:
  - Obsidian Shard
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Helm of Darkness — magical protection
    swap_item: Helm of Darkness
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Death
    Metal, Spear of the Magus, Ancient Signet, Doom Orb, Bragi''s Harp, Nimble Ring,
    Gluttonous Grimoire, Chronos'' Pendant, Heartwood Charm, Polynomicon, Dreamer''s
    Idol, Gem of Focus, Bracer of The Abyss, Blood-Bound Book, Soul Reaver, The Cosmic
    Horror, Bancroft''s Talon, Totem of Death, Triton''s Conch, Divine Ruin, Jade
    Scepter, Helm of Radiance.'
  slot_scores:
    Book of Thoth:
      total: 0.26
      efficiency: 0.49
      win: 0.0
      pick: 0.67
      fit: 0.35
    The World Stone:
      total: 0.73
      efficiency: 0.52
      win: 1.0
      pick: 0.45
      fit: 0.52
    Talisman of Purification:
      total: 0.56
      efficiency: 0.18
      win: 1.0
      pick: 0.55
      fit: 0.13
    Rod of Tahuti:
      total: 0.86
      efficiency: 0.86
      win: 1.0
      pick: 0.51
      fit: 0.52
    Obsidian Shard:
      total: 0.56
      efficiency: 0.58
      win: 0.5
      pick: 1.0
      fit: 0.53
    Circe's Hexstone:
      total: 0.58
      efficiency: 0.16
      win: 1.0
      pick: 1.0
      fit: 0.13
  community_ordered:
  - Book of Thoth
  - The World Stone
  - Talisman of Purification
  - Rod of Tahuti
  - Obsidian Shard
  - Circe's Hexstone
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Nimble Ring
  - The World Stone
  - Talisman of Purification
  - Rod of Tahuti
  - Obsidian Shard
  - Circe's Hexstone
  flex_slots:
  - Obsidian Shard
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Chronos'' Pendant, Dreamer''s
    Idol, Death Metal, Nimble Ring, Bragi''s Harp, Ancient Signet, Gem of Focus, The
    Cosmic Horror, Heartwood Charm, Bracer of The Abyss, Blood-Bound Book, Polynomicon,
    Totem of Death, Soul Reaver, Damaru, Divine Ruin, Jade Scepter, Triton''s Conch,
    Bancroft''s Talon.'
  slot_scores:
    Nimble Ring:
      total: 0.36
      efficiency: 0.58
      win: 0.25
      pick: 0.0
      fit: 0.3
    The World Stone:
      total: 0.73
      efficiency: 0.52
      win: 1.0
      pick: 0.45
      fit: 0.5
    Talisman of Purification:
      total: 0.57
      efficiency: 0.18
      win: 1.0
      pick: 0.55
      fit: 0.2
    Rod of Tahuti:
      total: 0.85
      efficiency: 0.86
      win: 1.0
      pick: 0.51
      fit: 0.5
    Obsidian Shard:
      total: 0.57
      efficiency: 0.58
      win: 0.5
      pick: 1.0
      fit: 0.6
    Circe's Hexstone:
      total: 0.59
      efficiency: 0.16
      win: 1.0
      pick: 1.0
      fit: 0.2
  community_ordered:
  - The World Stone
  - Talisman of Purification
  - Rod of Tahuti
  - Obsidian Shard
  - Circe's Hexstone
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - The World Stone
  - Talisman of Purification
  - Rod of Tahuti
  - Obsidian Shard
  - Circe's Hexstone
  - Amanita Charm
  flex_slots:
  - Obsidian Shard
  - Amanita Charm
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
    this god: Amanita Charm, Shield of the Phoenix, Gluttonous Grimoire, Kinetic Cuirass,
    Ethereal Staff, Blood-Bound Book, Phoenix Feather, Helm of Radiance, Sphere of
    Negation, Spear of the Magus, Helm of Darkness, Oni Hunter''s Garb, Chandra''s
    Grace, Erosion, Eye of Providence, Jade Scepter, Nimble Ring, Draconic Scale,
    Midgardian Mail, Ancient Signet, Doom Orb.'
  slot_scores:
    The World Stone:
      total: 0.71
      efficiency: 0.52
      win: 1.0
      pick: 0.45
      fit: 0.36
    Talisman of Purification:
      total: 0.56
      efficiency: 0.18
      win: 1.0
      pick: 0.55
      fit: 0.09
    Rod of Tahuti:
      total: 0.83
      efficiency: 0.86
      win: 1.0
      pick: 0.51
      fit: 0.36
    Obsidian Shard:
      total: 0.55
      efficiency: 0.58
      win: 0.5
      pick: 1.0
      fit: 0.46
    Circe's Hexstone:
      total: 0.62
      efficiency: 0.23
      win: 1.0
      pick: 1.0
      fit: 0.27
    Amanita Charm:
      total: 0.46
      efficiency: 0.65
      win: 0.25
      pick: 0.0
      fit: 0.76
  community_ordered:
  - The World Stone
  - Talisman of Purification
  - Rod of Tahuti
  - Obsidian Shard
  - Circe's Hexstone
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of the Magus
  - Talisman of Purification
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Circe's Hexstone
  flex_slots:
  - Talisman of Purification
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
    The Cosmic Horror, Nimble Ring, Ancient Signet, Chronos'' Pendant, Bracer of The
    Abyss, Gem of Focus, Heartwood Charm, Blood-Bound Book, Polynomicon, Soul Reaver,
    Totem of Death, Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm of Radiance,
    Ethereal Staff, Screeching Gargoyle, Typhon’s Heart.'
  slot_scores:
    Spear of the Magus:
      total: 0.43
      efficiency: 0.58
      win: 0.25
      pick: 0.0
      fit: 0.75
    Talisman of Purification:
      total: 0.56
      efficiency: 0.18
      win: 1.0
      pick: 0.55
      fit: 0.13
    The World Stone:
      total: 0.77
      efficiency: 0.52
      win: 1.0
      pick: 0.45
      fit: 0.75
    Rod of Tahuti:
      total: 0.89
      efficiency: 0.86
      win: 1.0
      pick: 0.51
      fit: 0.75
    Obsidian Shard:
      total: 0.61
      efficiency: 0.58
      win: 0.5
      pick: 1.0
      fit: 0.85
    Circe's Hexstone:
      total: 0.58
      efficiency: 0.16
      win: 1.0
      pick: 1.0
      fit: 0.13
  community_ordered:
  - Talisman of Purification
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Circe's Hexstone
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - The World Stone
  - Circe's Hexstone
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Talisman of Purification — CC-immunity / cleanse
    swap_item: Talisman of Purification
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
    this god: Nimble Ring, Gluttonous Grimoire, Bragi''s Harp, Spear of the Magus,
    Blood-Bound Book, Bracer of The Abyss, Ancient Signet, Death Metal, Doom Orb,
    Chronos'' Pendant, Dreamer''s Idol, Bancroft''s Talon, Polynomicon, Gem of Focus,
    Heartwood Charm, The Cosmic Horror, Typhon’s Heart, Soul Reaver, Divine Ruin,
    Jade Scepter, Totem of Death, Damaru, Helm of Radiance.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.35
      efficiency: 0.52
      win: 0.25
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.41
      efficiency: 0.63
      win: 0.25
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.36
      efficiency: 0.45
      win: 0.25
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.83
      efficiency: 0.86
      win: 1.0
      pick: 0.51
      fit: 0.32
    The World Stone:
      total: 0.7
      efficiency: 0.52
      win: 1.0
      pick: 0.45
      fit: 0.32
    Circe's Hexstone:
      total: 0.57
      efficiency: 0.16
      win: 1.0
      pick: 1.0
      fit: 0.08
  community_ordered:
  - Rod of Tahuti
  - The World Stone
  - Circe's Hexstone
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - The World Stone
  - Talisman of Purification
  - Rod of Tahuti
  - Obsidian Shard
  - Circe's Hexstone
  flex_slots:
  - Obsidian Shard
  - Chronos' Pendant
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Chronos'' Pendant, Gem of Focus, Heartwood
    Charm, Spear of the Magus, Gluttonous Grimoire, Nimble Ring, Totem of Death, Damaru,
    Doom Orb, Ancient Signet, Death Metal, Dreamer''s Idol, Bragi''s Harp, Bracer
    of The Abyss, Chandra''s Grace, The Cosmic Horror, Blood-Bound Book, Polynomicon,
    Staff of Myrddin, Eye of Erebus, Soul Reaver, Screeching Gargoyle.'
  slot_scores:
    Chronos' Pendant:
      total: 0.39
      efficiency: 0.55
      win: 0.25
      pick: 0.0
      fit: 0.56
    The World Stone:
      total: 0.71
      efficiency: 0.52
      win: 1.0
      pick: 0.45
      fit: 0.33
    Talisman of Purification:
      total: 0.61
      efficiency: 0.18
      win: 1.0
      pick: 0.55
      fit: 0.43
    Rod of Tahuti:
      total: 0.83
      efficiency: 0.86
      win: 1.0
      pick: 0.51
      fit: 0.33
    Obsidian Shard:
      total: 0.54
      efficiency: 0.58
      win: 0.5
      pick: 1.0
      fit: 0.43
    Circe's Hexstone:
      total: 0.62
      efficiency: 0.16
      win: 1.0
      pick: 1.0
      fit: 0.43
  community_ordered:
  - The World Stone
  - Talisman of Purification
  - Rod of Tahuti
  - Obsidian Shard
  - Circe's Hexstone
  starter: *id001
- source: suggested
  archetype: model
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Nimble
    Ring, Dreamer''s Idol, Chronos'' Pendant, Ancient Signet, The Cosmic Horror, Bracer
    of The Abyss, Gem of Focus, Heartwood Charm, Blood-Bound Book, Polynomicon, Totem
    of Death, Soul Reaver, Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm of Radiance,
    Ethereal Staff, Typhon’s Heart, Staff of Myrddin, Bragi''s Harp.'
  slot_scores:
    Nimble Ring:
      total: 0.39
      efficiency: 0.58
      win: 0.25
      pick: 0.0
      fit: 0.51
    Spear of Desolation:
      total: 0.36
      efficiency: 0.59
      win: 0.0
      pick: 0.45
      fit: 0.83
    Doom Orb:
      total: 0.4
      efficiency: 0.53
      win: 0.25
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.88
      efficiency: 0.86
      win: 1.0
      pick: 0.51
      fit: 0.66
    Spear of the Magus:
      total: 0.41
      efficiency: 0.58
      win: 0.25
      pick: 0.0
      fit: 0.66
    Obsidian Shard:
      total: 0.59
      efficiency: 0.58
      win: 0.5
      pick: 1.0
      fit: 0.76
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
---

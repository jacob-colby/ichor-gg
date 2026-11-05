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
    - name: Gem of Focus
      pick_rate: 0.12
      win_rate: 0.54
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
    win_rate: 0.5
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.33
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
      win_rate: 0.6
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
      win_rate: 0.48
  - name: Surplus Mod
    pick_rate: 0.25
    win_rate: 0.57
    alternates:
    - name: Shrapnel Mod
      pick_rate: 0.37
      win_rate: 0.61
    - name: Thermal Mod
      pick_rate: 0.21
      win_rate: 0.55
  - name: Thermal Mod
    pick_rate: 0.11
    win_rate: 0.57
    alternates:
    - name: Surplus Mod
      pick_rate: 0.7
      win_rate: 0.6
    - name: Seismic Mod
      pick_rate: 0.09
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
    win_rate: 0.52
  source_url: https://smitebrain.com/gods/vulcan/
  last_verified: '2026-11-04'
  god_win_rate: 0.5650793650793651
  god_matches_won: 534
  god_matches_played: 945
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-03'
  god_matches_analyzed: 14667
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - Obsidian Shard
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
    this god: Soul Gem, Chronos'' Pendant, Spear of the Magus, Dreamer''s Idol, Gluttonous
    Grimoire, Doom Orb, Ancient Signet, Polynomicon, Bracer of The Abyss, The Cosmic
    Horror, Nimble Ring, Heartwood Charm, Blood-Bound Book, Soul Reaver, Totem of
    Death, Bancroft''s Talon, Jade Scepter, Divine Ruin, Bragi''s Harp, Ethereal Staff,
    Helm of Radiance, Genji''s Guard, Death Metal.'
  slot_scores:
    Chronos' Pendant:
      total: 0.55
      efficiency: 0.56
      win: 0.6
      pick: 0.06
      fit: 0.52
    Spear of Desolation:
      total: 0.64
      efficiency: 0.6
      win: 0.63
      pick: 0.37
      fit: 0.83
    Spear of the Magus:
      total: 0.55
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.82
      win: 0.57
      pick: 0.36
      fit: 0.66
    Obsidian Shard:
      total: 0.54
      efficiency: 0.53
      win: 0.5
      pick: 0.28
      fit: 0.76
    Soul Gem:
      total: 0.58
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.93
  community_ordered:
  - Chronos' Pendant
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
  - Chronos' Pendant
  - Spear of Desolation
  - Ancient Signet
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Ancient Signet
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
    Gem, Chronos'' Pendant, Death Metal, Bragi''s Harp, Ancient Signet, Polynomicon,
    Spear of the Magus, Doom Orb, Dreamer''s Idol, Heartwood Charm, Gluttonous Grimoire,
    Soul Reaver, Bracer of The Abyss, Blood-Bound Book, Nimble Ring, The Cosmic Horror,
    Bancroft''s Talon, Totem of Death, Triton''s Conch, Genji''s Guard, Jade Scepter,
    Divine Ruin, Damaru.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.48
      win: 0.57
      pick: 0.51
      fit: 0.35
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.56
      win: 0.6
      pick: 0.06
      fit: 0.39
    Spear of Desolation:
      total: 0.6
      efficiency: 0.6
      win: 0.63
      pick: 0.37
      fit: 0.56
    Ancient Signet:
      total: 0.52
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.57
      pick: 0.36
      fit: 0.52
    Soul Gem:
      total: 0.54
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.66
  community_ordered:
  - Book of Thoth
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of the Magus
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Chronos'' Pendant, Spear of the Magus, Dreamer''s Idol, Gluttonous
    Grimoire, Death Metal, Bragi''s Harp, Doom Orb, Ancient Signet, Polynomicon, Heartwood
    Charm, The Cosmic Horror, Bracer of The Abyss, Blood-Bound Book, Nimble Ring,
    Soul Reaver, Totem of Death, Damaru, Genji''s Guard, Triton''s Conch, Bancroft''s
    Talon, Jade Scepter, Divine Ruin.'
  slot_scores:
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.56
      win: 0.6
      pick: 0.06
      fit: 0.4
    Spear of Desolation:
      total: 0.62
      efficiency: 0.6
      win: 0.63
      pick: 0.37
      fit: 0.7
    Spear of the Magus:
      total: 0.52
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.57
      pick: 0.36
      fit: 0.5
    Obsidian Shard:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.28
      fit: 0.6
    Soul Gem:
      total: 0.56
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Shield of the Phoenix, Kinetic Cuirass, Genji''s
    Guard, Ethereal Staff, Gluttonous Grimoire, Phoenix Feather, Freya''s Tears, Blood-Bound
    Book, Yogi''s Necklace, Breastplate of Valor, Chandra''s Grace, Draconic Scale,
    Oni Hunter''s Garb, Helm of Radiance, Sphere of Negation, Erosion, Spear of the
    Magus, Helm of Darkness, Eye of Providence, Shifter''s Shield, Ancient Signet,
    Regrowth Striders, Jade Scepter, Lifebinder.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.56
      pick: 0.0
      fit: 0.24
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.58
      efficiency: 0.6
      win: 0.63
      pick: 0.37
      fit: 0.45
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.57
      pick: 0.36
      fit: 0.36
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.76
    Soul Gem:
      total: 0.57
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
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
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Spear of the Magus, Dreamer''s Idol, Gluttonous Grimoire,
    Doom Orb, Chronos'' Pendant, The Cosmic Horror, Ancient Signet, Polynomicon, Bracer
    of The Abyss, Nimble Ring, Heartwood Charm, Blood-Bound Book, Soul Reaver, Totem
    of Death, Bancroft''s Talon, Jade Scepter, Divine Ruin, Screeching Gargoyle, Genji''s
    Guard, Ethereal Staff, Helm of Radiance, Bragi''s Harp.'
  slot_scores:
    Spear of Desolation:
      total: 0.65
      efficiency: 0.6
      win: 0.63
      pick: 0.37
      fit: 0.88
    Doom Orb:
      total: 0.54
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.75
    Spear of the Magus:
      total: 0.56
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.75
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.82
      win: 0.57
      pick: 0.36
      fit: 0.75
    Obsidian Shard:
      total: 0.55
      efficiency: 0.53
      win: 0.5
      pick: 0.28
      fit: 0.85
    Soul Gem:
      total: 0.58
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.98
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
    this god: Soul Gem, Nimble Ring, Gluttonous Grimoire, Bragi''s Harp, Chronos''
    Pendant, Blood-Bound Book, Bracer of The Abyss, Spear of the Magus, Death Metal,
    Ancient Signet, Dreamer''s Idol, Polynomicon, Doom Orb, Bancroft''s Talon, Soul
    Reaver, Heartwood Charm, The Cosmic Horror, Typhon’s Heart, Totem of Death, Damaru,
    Genji''s Guard, Jade Scepter, Divine Ruin.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.5
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.52
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.57
      efficiency: 0.6
      win: 0.63
      pick: 0.37
      fit: 0.4
    Bragi's Harp:
      total: 0.51
      efficiency: 0.47
      win: 0.56
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.57
      pick: 0.36
      fit: 0.32
    Soul Gem:
      total: 0.54
      efficiency: 0.58
      win: 0.56
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
    Charm, Spear of the Magus, Damaru, Genji''s Guard, Totem of Death, Dreamer''s
    Idol, Death Metal, Bragi''s Harp, Ancient Signet, Gluttonous Grimoire, Polynomicon,
    Doom Orb, Breastplate of Valor, Chandra''s Grace, Bracer of The Abyss, Nimble
    Ring, Blood-Bound Book, Soul Reaver, The Cosmic Horror, Staff of Myrddin, Screeching
    Gargoyle, Freya''s Tears.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.48
      win: 0.57
      pick: 0.51
      fit: 0.13
    Chronos' Pendant:
      total: 0.55
      efficiency: 0.56
      win: 0.6
      pick: 0.06
      fit: 0.56
    Spear of Desolation:
      total: 0.63
      efficiency: 0.6
      win: 0.63
      pick: 0.37
      fit: 0.76
    Heartwood Charm:
      total: 0.51
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.57
      pick: 0.36
      fit: 0.33
    Soul Gem:
      total: 0.57
      efficiency: 0.53
      win: 0.56
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
    Underrated for this god: Soul Gem, Spear of the Magus, Dreamer''s Idol, Gluttonous
    Grimoire, Doom Orb, Chronos'' Pendant, Ancient Signet, Polynomicon, Bracer of
    The Abyss, The Cosmic Horror, Nimble Ring, Heartwood Charm, Blood-Bound Book,
    Soul Reaver, Totem of Death, Bancroft''s Talon, Jade Scepter, Divine Ruin, Bragi''s
    Harp, Ethereal Staff, Helm of Radiance, Genji''s Guard, Death Metal.'
  slot_scores:
    Spear of Desolation:
      total: 0.64
      efficiency: 0.6
      win: 0.63
      pick: 0.37
      fit: 0.83
    Doom Orb:
      total: 0.53
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.66
    Spear of the Magus:
      total: 0.55
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.82
      win: 0.57
      pick: 0.36
      fit: 0.66
    Obsidian Shard:
      total: 0.54
      efficiency: 0.53
      win: 0.5
      pick: 0.28
      fit: 0.76
    Soul Gem:
      total: 0.58
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.93
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
---

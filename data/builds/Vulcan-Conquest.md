---
type: smite-build
god: Vulcan
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fortification
  aspect_pick_rate: 0.09
  aspect_win_rate: 0.53
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.43
    win_rate: 0.47
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.3
      win_rate: 0.44
    - name: Chronos' Pendant
      pick_rate: 0.07
      win_rate: 0.67
  - name: Spear of Desolation
    pick_rate: 0.18
    win_rate: 0.69
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.15
      win_rate: 0.37
    - name: The World Stone
      pick_rate: 0.15
      win_rate: 0.59
  - name: Rod of Tahuti
    pick_rate: 0.24
    win_rate: 0.57
    alternates:
    - name: Soul Gem
      pick_rate: 0.1
      win_rate: 0.61
    - name: The World Stone
      pick_rate: 0.09
      win_rate: 0.47
  - name: Obsidian Shard
    pick_rate: 0.18
    win_rate: 0.43
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.32
      win_rate: 0.62
    - name: Soul Gem
      pick_rate: 0.1
      win_rate: 0.71
  - name: Shrapnel Mod
    pick_rate: 0.09
    win_rate: 0.43
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.24
      win_rate: 0.63
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.4
  - name: Thermal Mod
    pick_rate: 0.12
    win_rate: 0.47
    alternates:
    - name: Shrapnel Mod
      pick_rate: 0.14
      win_rate: 0.59
    - name: Surplus Mod
      pick_rate: 0.08
      win_rate: 0.38
  - name: Surplus Mod
    pick_rate: 0.23
    win_rate: 0.59
    alternates:
    - name: Shrapnel Mod
      pick_rate: 0.38
      win_rate: 0.52
    - name: Thermal Mod
      pick_rate: 0.23
      win_rate: 0.64
  - name: Seismic Mod
    pick_rate: 0.07
    win_rate: 0.57
    alternates:
    - name: Surplus Mod
      pick_rate: 0.78
      win_rate: 0.55
    - name: Thermal Mod
      pick_rate: 0.11
      win_rate: 0.36
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.34
    win_rate: 0.5
  - name: Archmage's Gem
    pick_rate: 0.23
    win_rate: 0.62
  - name: Sands Of Time
    pick_rate: 0.22
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/vulcan/
  last_verified: '2026-11-06'
  god_win_rate: 0.5222222222222223
  god_matches_won: 94
  god_matches_played: 180
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - The World Stone
  - Dreamer's Idol
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
    this god: Spear of the Magus, Dreamer''s Idol, Gluttonous Grimoire, Doom Orb,
    Ancient Signet, Polynomicon, Bracer of The Abyss, The Cosmic Horror, Nimble Ring,
    Gem of Focus, Heartwood Charm, Blood-Bound Book, Soul Reaver, Totem of Death,
    Bancroft''s Talon, Jade Scepter, Divine Ruin, Bragi''s Harp, Ethereal Staff, Helm
    of Radiance, Genji''s Guard, Death Metal.'
  slot_scores:
    Spear of Desolation:
      total: 0.66
      efficiency: 0.6
      win: 0.69
      pick: 0.25
      fit: 0.83
    Spear of the Magus:
      total: 0.55
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.66
    The World Stone:
      total: 0.55
      efficiency: 0.49
      win: 0.59
      pick: 0.2
      fit: 0.66
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.82
      win: 0.57
      pick: 0.37
      fit: 0.66
    Dreamer's Idol:
      total: 0.54
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.66
    Soul Gem:
      total: 0.65
      efficiency: 0.53
      win: 0.71
      pick: 0.17
      fit: 0.93
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Death Metal
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - The World Stone
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Death
    Metal, Bragi''s Harp, Ancient Signet, Polynomicon, Spear of the Magus, Doom Orb,
    Dreamer''s Idol, Heartwood Charm, Gluttonous Grimoire, Soul Reaver, Bracer of
    The Abyss, Gem of Focus, Blood-Bound Book, Nimble Ring, The Cosmic Horror, Bancroft''s
    Talon, Totem of Death, Triton''s Conch, Genji''s Guard, Jade Scepter, Divine Ruin,
    Damaru.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.48
      win: 0.47
      pick: 0.43
      fit: 0.35
    Death Metal:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.52
    Spear of Desolation:
      total: 0.62
      efficiency: 0.6
      win: 0.69
      pick: 0.25
      fit: 0.56
    The World Stone:
      total: 0.53
      efficiency: 0.49
      win: 0.59
      pick: 0.2
      fit: 0.52
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.57
      pick: 0.37
      fit: 0.52
    Soul Gem:
      total: 0.61
      efficiency: 0.53
      win: 0.71
      pick: 0.17
      fit: 0.66
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - The World Stone
  - Dreamer's Idol
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
    god: Spear of the Magus, Dreamer''s Idol, Gluttonous Grimoire, Death Metal, Bragi''s
    Harp, Doom Orb, Ancient Signet, Polynomicon, Gem of Focus, Heartwood Charm, The
    Cosmic Horror, Bracer of The Abyss, Blood-Bound Book, Nimble Ring, Soul Reaver,
    Totem of Death, Damaru, Genji''s Guard, Triton''s Conch, Bancroft''s Talon, Jade
    Scepter, Divine Ruin.'
  slot_scores:
    Spear of Desolation:
      total: 0.64
      efficiency: 0.6
      win: 0.69
      pick: 0.25
      fit: 0.7
    Spear of the Magus:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.5
    The World Stone:
      total: 0.52
      efficiency: 0.49
      win: 0.59
      pick: 0.2
      fit: 0.5
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.57
      pick: 0.37
      fit: 0.5
    Dreamer's Idol:
      total: 0.52
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.5
    Soul Gem:
      total: 0.63
      efficiency: 0.53
      win: 0.71
      pick: 0.17
      fit: 0.8
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
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
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Genji''s Guard,
    Ethereal Staff, Gluttonous Grimoire, Phoenix Feather, Freya''s Tears, Blood-Bound
    Book, Yogi''s Necklace, Breastplate of Valor, Chandra''s Grace, Draconic Scale,
    Oni Hunter''s Garb, Helm of Radiance, Sphere of Negation, Erosion, Spear of the
    Magus, Helm of Darkness, Eye of Providence, Shifter''s Shield, Ancient Signet,
    Regrowth Striders, Jade Scepter, Lifebinder.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.24
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.6
      efficiency: 0.6
      win: 0.69
      pick: 0.25
      fit: 0.45
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.57
      pick: 0.37
      fit: 0.36
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.76
    Soul Gem:
      total: 0.64
      efficiency: 0.53
      win: 0.71
      pick: 0.17
      fit: 0.85
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - The World Stone
  - Dreamer's Idol
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
    for this god: Spear of the Magus, Dreamer''s Idol, Gluttonous Grimoire, Doom Orb,
    The Cosmic Horror, Ancient Signet, Polynomicon, Bracer of The Abyss, Nimble Ring,
    Gem of Focus, Heartwood Charm, Blood-Bound Book, Soul Reaver, Totem of Death,
    Bancroft''s Talon, Jade Scepter, Divine Ruin, Screeching Gargoyle, Genji''s Guard,
    Ethereal Staff, Helm of Radiance, Bragi''s Harp.'
  slot_scores:
    Spear of Desolation:
      total: 0.67
      efficiency: 0.6
      win: 0.69
      pick: 0.25
      fit: 0.88
    Spear of the Magus:
      total: 0.56
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.75
    The World Stone:
      total: 0.56
      efficiency: 0.49
      win: 0.59
      pick: 0.2
      fit: 0.75
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.82
      win: 0.57
      pick: 0.37
      fit: 0.75
    Dreamer's Idol:
      total: 0.56
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.75
    Soul Gem:
      total: 0.66
      efficiency: 0.53
      win: 0.71
      pick: 0.17
      fit: 0.98
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
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
    this god: Nimble Ring, Gluttonous Grimoire, Bragi''s Harp, Blood-Bound Book, Bracer
    of The Abyss, Spear of the Magus, Death Metal, Ancient Signet, Dreamer''s Idol,
    Polynomicon, Doom Orb, Bancroft''s Talon, Soul Reaver, Gem of Focus, Heartwood
    Charm, The Cosmic Horror, Typhon’s Heart, Totem of Death, Damaru, Genji''s Guard,
    Jade Scepter, Divine Ruin.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.5
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.53
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.59
      efficiency: 0.6
      win: 0.69
      pick: 0.25
      fit: 0.4
    Bragi's Harp:
      total: 0.52
      efficiency: 0.47
      win: 0.57
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.57
      pick: 0.37
      fit: 0.32
    Soul Gem:
      total: 0.62
      efficiency: 0.58
      win: 0.71
      pick: 0.17
      fit: 0.58
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Gem of Focus
  - Heartwood Charm
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Soul Gem
  flex_slots:
  - Heartwood Charm
  - Spear of the Magus
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
    + fit + win/pick). Underrated for this god: Gem of Focus, Heartwood Charm, Spear
    of the Magus, Damaru, Genji''s Guard, Totem of Death, Dreamer''s Idol, Death Metal,
    Bragi''s Harp, Ancient Signet, Gluttonous Grimoire, Polynomicon, Doom Orb, Breastplate
    of Valor, Chandra''s Grace, Bracer of The Abyss, Nimble Ring, Blood-Bound Book,
    Soul Reaver, The Cosmic Horror, Staff of Myrddin, Screeching Gargoyle, Freya''s
    Tears.'
  slot_scores:
    Gem of Focus:
      total: 0.52
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.56
    Heartwood Charm:
      total: 0.52
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.65
      efficiency: 0.6
      win: 0.69
      pick: 0.25
      fit: 0.76
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.57
      pick: 0.37
      fit: 0.33
    Spear of the Magus:
      total: 0.5
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.33
    Soul Gem:
      total: 0.64
      efficiency: 0.53
      win: 0.71
      pick: 0.17
      fit: 0.86
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
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
    Underrated for this god: Spear of the Magus, Dreamer''s Idol, Gluttonous Grimoire,
    Doom Orb, Ancient Signet, Polynomicon, Bracer of The Abyss, The Cosmic Horror,
    Nimble Ring, Gem of Focus, Heartwood Charm, Blood-Bound Book, Soul Reaver, Totem
    of Death, Bancroft''s Talon, Jade Scepter, Divine Ruin, Bragi''s Harp, Ethereal
    Staff, Helm of Radiance, Genji''s Guard, Death Metal.'
  slot_scores:
    Spear of Desolation:
      total: 0.66
      efficiency: 0.6
      win: 0.69
      pick: 0.25
      fit: 0.83
    Doom Orb:
      total: 0.53
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.66
    Spear of the Magus:
      total: 0.55
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.82
      win: 0.57
      pick: 0.37
      fit: 0.66
    Obsidian Shard:
      total: 0.51
      efficiency: 0.53
      win: 0.43
      pick: 0.3
      fit: 0.76
    Soul Gem:
      total: 0.65
      efficiency: 0.53
      win: 0.71
      pick: 0.17
      fit: 0.93
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
---

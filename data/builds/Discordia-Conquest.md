---
type: smite-build
god: Discordia
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Gilded Victor
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.55
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.4
    win_rate: 0.64
    alternates:
    - name: Book of Thoth
      pick_rate: 0.22
      win_rate: 0.57
    - name: Chronos' Pendant
      pick_rate: 0.17
      win_rate: 0.5
  - name: Chronos' Pendant
    pick_rate: 0.15
    win_rate: 0.38
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.21
      win_rate: 0.55
    - name: Book of Thoth
      pick_rate: 0.12
      win_rate: 0.69
  - name: Rod of Tahuti
    pick_rate: 0.29
    win_rate: 0.5
    alternates:
    - name: Soul Gem
      pick_rate: 0.17
      win_rate: 0.72
    - name: Spear of Desolation
      pick_rate: 0.09
      win_rate: 0.67
  - name: Obsidian Shard
    pick_rate: 0.15
    win_rate: 0.47
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.35
      win_rate: 0.57
    - name: Spear of the Magus
      pick_rate: 0.11
      win_rate: 0.55
  - name: Evil Eye
    pick_rate: 0.11
    win_rate: 0.67
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.19
      win_rate: 0.67
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.38
  - name: Killing Stone
    pick_rate: 0.11
    win_rate: 0.6
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.17
      win_rate: 0.75
    - name: Evil Eye
      pick_rate: 0.13
      win_rate: 0.83
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.28
    win_rate: 0.62
  - name: Archmage's Gem
    pick_rate: 0.21
    win_rate: 0.59
  - name: Conduit Gem
    pick_rate: 0.12
    win_rate: 0.38
  source_url: https://smitebrain.com/gods/discordia/
  last_verified: '2026-11-06'
  god_win_rate: 0.5523809523809524
  god_matches_won: 58
  god_matches_played: 105
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
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Dreamer's Idol
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
    this god: Dreamer''s Idol, Gluttonous Grimoire, Doom Orb, The World Stone, Ancient
    Signet, The Cosmic Horror, Polynomicon, Gem of Focus, Heartwood Charm, Blood-Bound
    Book, Soul Reaver, Totem of Death, Bancroft''s Talon, Jade Scepter, Divine Ruin,
    Ethereal Staff, Helm of Radiance, Bracer of The Abyss, Death Metal, Staff of Myrddin,
    Genji''s Guard, Alchemist Coat.'
  slot_scores:
    Spear of Desolation:
      total: 0.67
      efficiency: 0.6
      win: 0.64
      pick: 0.4
      fit: 1.0
    Doom Orb:
      total: 0.55
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.57
      efficiency: 0.56
      win: 0.55
      pick: 0.18
      fit: 0.79
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.82
      win: 0.5
      pick: 0.45
      fit: 0.79
    Dreamer's Idol:
      total: 0.56
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.67
      efficiency: 0.53
      win: 0.72
      pick: 0.26
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Spear of the Magus
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Death
    Metal, Ancient Signet, Polynomicon, Doom Orb, Dreamer''s Idol, The World Stone,
    Heartwood Charm, Bragi''s Harp, Gluttonous Grimoire, Soul Reaver, Gem of Focus,
    Blood-Bound Book, The Cosmic Horror, Bancroft''s Talon, Totem of Death, Triton''s
    Conch, Genji''s Guard, Jade Scepter, Divine Ruin, Ethereal Staff, Damaru, Helm
    of Radiance.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.48
      win: 0.57
      pick: 0.22
      fit: 0.39
    Death Metal:
      total: 0.54
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.57
    Spear of Desolation:
      total: 0.61
      efficiency: 0.6
      win: 0.64
      pick: 0.4
      fit: 0.61
    Ancient Signet:
      total: 0.53
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.5
      pick: 0.45
      fit: 0.57
    Soul Gem:
      total: 0.63
      efficiency: 0.53
      win: 0.72
      pick: 0.26
      fit: 0.71
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Death Metal
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Dreamer's Idol
  - Death Metal
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
    god: Dreamer''s Idol, Gluttonous Grimoire, Death Metal, Doom Orb, The World Stone,
    Ancient Signet, Gem of Focus, Heartwood Charm, Polynomicon, The Cosmic Horror,
    Bragi''s Harp, Blood-Bound Book, Totem of Death, Soul Reaver, Damaru, Genji''s
    Guard, Triton''s Conch, Bancroft''s Talon, Jade Scepter, Divine Ruin, Breastplate
    of Valor, Ethereal Staff.'
  slot_scores:
    Death Metal:
      total: 0.52
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.64
      efficiency: 0.6
      win: 0.64
      pick: 0.4
      fit: 0.78
    Spear of the Magus:
      total: 0.54
      efficiency: 0.56
      win: 0.55
      pick: 0.18
      fit: 0.56
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.5
      pick: 0.45
      fit: 0.56
    Dreamer's Idol:
      total: 0.53
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.56
    Soul Gem:
      total: 0.65
      efficiency: 0.53
      win: 0.72
      pick: 0.26
      fit: 0.88
  community_ordered:
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Kinetic Cuirass
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
    Book, Yogi''s Necklace, Draconic Scale, Breastplate of Valor, Chandra''s Grace,
    Oni Hunter''s Garb, Helm of Radiance, Sphere of Negation, Erosion, Helm of Darkness,
    Eye of Providence, Shifter''s Shield, Jade Scepter, Lifebinder, Dreamer''s Idol,
    Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.26
    Spear of Desolation:
      total: 0.59
      efficiency: 0.6
      win: 0.64
      pick: 0.4
      fit: 0.49
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.61
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.82
      win: 0.5
      pick: 0.45
      fit: 0.39
    Amanita Charm:
      total: 0.62
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.66
      efficiency: 0.53
      win: 0.72
      pick: 0.26
      fit: 0.89
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Dreamer's Idol
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
    for this god: Dreamer''s Idol, Gluttonous Grimoire, Doom Orb, The World Stone,
    The Cosmic Horror, Ancient Signet, Polynomicon, Gem of Focus, Heartwood Charm,
    Blood-Bound Book, Soul Reaver, Totem of Death, Bancroft''s Talon, Jade Scepter,
    Divine Ruin, Screeching Gargoyle, Ethereal Staff, Genji''s Guard, Helm of Radiance,
    Bracer of The Abyss, Death Metal, Alchemist Coat.'
  slot_scores:
    Spear of Desolation:
      total: 0.67
      efficiency: 0.6
      win: 0.64
      pick: 0.4
      fit: 1.0
    Doom Orb:
      total: 0.56
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.58
      efficiency: 0.56
      win: 0.55
      pick: 0.18
      fit: 0.85
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.82
      win: 0.5
      pick: 0.45
      fit: 0.85
    Dreamer's Idol:
      total: 0.57
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.85
    Soul Gem:
      total: 0.67
      efficiency: 0.53
      win: 0.72
      pick: 0.26
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Spear of the Magus
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
    of The Abyss, Death Metal, Ancient Signet, Dreamer''s Idol, Polynomicon, Doom
    Orb, The World Stone, Bancroft''s Talon, Soul Reaver, Gem of Focus, Heartwood
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
      total: 0.58
      efficiency: 0.6
      win: 0.64
      pick: 0.4
      fit: 0.4
    Bragi's Harp:
      total: 0.52
      efficiency: 0.47
      win: 0.57
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.82
      win: 0.5
      pick: 0.45
      fit: 0.32
    Soul Gem:
      total: 0.63
      efficiency: 0.58
      win: 0.72
      pick: 0.26
      fit: 0.58
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Gem of Focus
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
    + fit + win/pick). Underrated for this god: Gem of Focus, Heartwood Charm, Totem
    of Death, Damaru, Genji''s Guard, Dreamer''s Idol, Death Metal, Gluttonous Grimoire,
    Ancient Signet, Doom Orb, Polynomicon, Breastplate of Valor, The World Stone,
    Chandra''s Grace, Blood-Bound Book, The Cosmic Horror, Bragi''s Harp, Soul Reaver,
    Staff of Myrddin, Screeching Gargoyle, Freya''s Tears, Eye of Erebus, Shield of
    the Phoenix.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.48
      win: 0.57
      pick: 0.22
      fit: 0.14
    Gem of Focus:
      total: 0.53
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.65
      efficiency: 0.6
      win: 0.64
      pick: 0.4
      fit: 0.86
    Heartwood Charm:
      total: 0.53
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.82
      win: 0.5
      pick: 0.45
      fit: 0.37
    Soul Gem:
      total: 0.67
      efficiency: 0.53
      win: 0.72
      pick: 0.26
      fit: 0.96
  community_ordered:
  - Book of Thoth
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
  - Soul Gem
  - Obsidian Shard
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
    Underrated for this god: Dreamer''s Idol, Gluttonous Grimoire, Doom Orb, The World
    Stone, Ancient Signet, The Cosmic Horror, Polynomicon, Gem of Focus, Heartwood
    Charm, Blood-Bound Book, Soul Reaver, Totem of Death, Bancroft''s Talon, Jade
    Scepter, Divine Ruin, Ethereal Staff, Helm of Radiance, Bracer of The Abyss, Death
    Metal, Staff of Myrddin, Genji''s Guard, Alchemist Coat.'
  slot_scores:
    Spear of Desolation:
      total: 0.67
      efficiency: 0.6
      win: 0.64
      pick: 0.4
      fit: 1.0
    Doom Orb:
      total: 0.55
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.57
      efficiency: 0.56
      win: 0.55
      pick: 0.18
      fit: 0.79
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.82
      win: 0.5
      pick: 0.45
      fit: 0.79
    Soul Gem:
      total: 0.67
      efficiency: 0.53
      win: 0.72
      pick: 0.26
      fit: 1.0
    Obsidian Shard:
      total: 0.54
      efficiency: 0.53
      win: 0.47
      pick: 0.25
      fit: 0.89
  community_ordered:
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Soul Gem
  - Obsidian Shard
  starter: *id001
---

---
type: smite-build
god: Merlin
mode: Conquest
builds:
- source: community
  aspect: Aspect of Pandemonium
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.56
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.41
    win_rate: 0.49
    alternates:
    - name: The World Stone
      pick_rate: 0.13
      win_rate: 0.46
    - name: Book of Thoth
      pick_rate: 0.11
      win_rate: 0.43
  - name: Soul Gem
    pick_rate: 0.19
    win_rate: 0.46
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.2
      win_rate: 0.55
    - name: Book of Thoth
      pick_rate: 0.12
      win_rate: 0.64
  - name: Rod of Tahuti
    pick_rate: 0.24
    win_rate: 0.4
    alternates:
    - name: Soul Gem
      pick_rate: 0.23
      win_rate: 0.54
    - name: The World Stone
      pick_rate: 0.09
      win_rate: 0.59
  - name: Obsidian Shard
    pick_rate: 0.18
    win_rate: 0.56
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.3
      win_rate: 0.62
    - name: Spear of the Magus
      pick_rate: 0.15
      win_rate: 0.54
  - name: Evil Eye
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.19
      win_rate: 0.69
    - name: Obsidian Shard
      pick_rate: 0.14
      win_rate: 0.68
  - name: Oracle Staff
    pick_rate: 0.11
    win_rate: 0.91
    alternates:
    - name: Evil Eye
      pick_rate: 0.11
      win_rate: 0.64
    - name: Void Shard
      pick_rate: 0.1
      win_rate: 0.5
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.39
    win_rate: 0.6
  - name: Bluestone Brooch
    pick_rate: 0.18
    win_rate: 0.52
  - name: Archmage's Gem
    pick_rate: 0.15
    win_rate: 0.61
  source_url: https://smitebrain.com/gods/merlin/
  last_verified: '2026-11-06'
  god_win_rate: 0.5376344086021505
  god_matches_won: 100
  god_matches_played: 186
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
  - Book of Thoth
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The World Stone, Dreamer''s Idol, Gluttonous Grimoire, Doom Orb, Chronos''
    Pendant, Ancient Signet, The Cosmic Horror, Polynomicon, Gem of Focus, Heartwood
    Charm, Blood-Bound Book, Soul Reaver, Totem of Death, Bancroft''s Talon, Jade
    Scepter, Divine Ruin, Ethereal Staff, Helm of Radiance, Bracer of The Abyss, Death
    Metal, Staff of Myrddin, Genji''s Guard, Alchemist Coat.'
  slot_scores:
    Book of Thoth:
      total: 0.53
      efficiency: 0.48
      win: 0.64
      pick: 0.16
      fit: 0.42
    Spear of Desolation:
      total: 0.6
      efficiency: 0.6
      win: 0.49
      pick: 0.41
      fit: 1.0
    Spear of the Magus:
      total: 0.57
      efficiency: 0.56
      win: 0.54
      pick: 0.25
      fit: 0.79
    The World Stone:
      total: 0.56
      efficiency: 0.49
      win: 0.59
      pick: 0.14
      fit: 0.79
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.4
      pick: 0.37
      fit: 0.79
    Obsidian Shard:
      total: 0.59
      efficiency: 0.53
      win: 0.56
      pick: 0.3
      fit: 0.89
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Book of Thoth
  - Spear of the Magus
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: The
    World Stone, Death Metal, Ancient Signet, Polynomicon, Doom Orb, Chronos'' Pendant,
    Dreamer''s Idol, Heartwood Charm, Bragi''s Harp, Gluttonous Grimoire, Soul Reaver,
    Gem of Focus, Blood-Bound Book, The Cosmic Horror, Bancroft''s Talon, Totem of
    Death, Triton''s Conch, Genji''s Guard, Jade Scepter, Divine Ruin, Ethereal Staff,
    Damaru, Helm of Radiance.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.48
      win: 0.64
      pick: 0.16
      fit: 0.39
    Spear of Desolation:
      total: 0.54
      efficiency: 0.6
      win: 0.49
      pick: 0.41
      fit: 0.61
    Spear of the Magus:
      total: 0.52
      efficiency: 0.56
      win: 0.54
      pick: 0.25
      fit: 0.47
    The World Stone:
      total: 0.53
      efficiency: 0.49
      win: 0.59
      pick: 0.14
      fit: 0.57
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.82
      win: 0.4
      pick: 0.37
      fit: 0.57
    Obsidian Shard:
      total: 0.54
      efficiency: 0.53
      win: 0.56
      pick: 0.3
      fit: 0.57
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Spear of the Magus
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The World Stone, Dreamer''s Idol, Gluttonous Grimoire, Death Metal, Chronos''
    Pendant, Doom Orb, Ancient Signet, Gem of Focus, Heartwood Charm, Polynomicon,
    The Cosmic Horror, Bragi''s Harp, Blood-Bound Book, Totem of Death, Soul Reaver,
    Damaru, Genji''s Guard, Triton''s Conch, Bancroft''s Talon, Jade Scepter, Divine
    Ruin, Breastplate of Valor, Ethereal Staff.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.48
      win: 0.64
      pick: 0.16
      fit: 0.22
    Spear of Desolation:
      total: 0.57
      efficiency: 0.6
      win: 0.49
      pick: 0.41
      fit: 0.78
    Spear of the Magus:
      total: 0.53
      efficiency: 0.56
      win: 0.54
      pick: 0.25
      fit: 0.56
    Soul Gem:
      total: 0.54
      efficiency: 0.53
      win: 0.46
      pick: 0.26
      fit: 0.88
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.82
      win: 0.4
      pick: 0.37
      fit: 0.56
    Obsidian Shard:
      total: 0.55
      efficiency: 0.53
      win: 0.56
      pick: 0.3
      fit: 0.66
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Spear of the Magus
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Shield of the Phoenix
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Obsidian Shard
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
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
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.61
      win: 0.52
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.53
      efficiency: 0.6
      win: 0.49
      pick: 0.41
      fit: 0.49
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.75
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.82
      win: 0.4
      pick: 0.37
      fit: 0.39
    Obsidian Shard:
      total: 0.53
      efficiency: 0.53
      win: 0.56
      pick: 0.3
      fit: 0.49
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.81
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - The World Stone
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The World Stone, Dreamer''s Idol, Gluttonous Grimoire, Doom Orb,
    The Cosmic Horror, Chronos'' Pendant, Ancient Signet, Polynomicon, Gem of Focus,
    Heartwood Charm, Blood-Bound Book, Soul Reaver, Totem of Death, Bancroft''s Talon,
    Jade Scepter, Divine Ruin, Screeching Gargoyle, Ethereal Staff, Genji''s Guard,
    Helm of Radiance, Bracer of The Abyss, Death Metal, Alchemist Coat.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.48
      win: 0.64
      pick: 0.16
      fit: 0.3
    Spear of Desolation:
      total: 0.6
      efficiency: 0.6
      win: 0.49
      pick: 0.41
      fit: 1.0
    Spear of the Magus:
      total: 0.58
      efficiency: 0.56
      win: 0.54
      pick: 0.25
      fit: 0.85
    The World Stone:
      total: 0.57
      efficiency: 0.49
      win: 0.59
      pick: 0.14
      fit: 0.85
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.4
      pick: 0.37
      fit: 0.85
    Obsidian Shard:
      total: 0.6
      efficiency: 0.53
      win: 0.56
      pick: 0.3
      fit: 0.95
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Book of Thoth
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Book of Thoth
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
    this god: Nimble Ring, Gluttonous Grimoire, Bragi''s Harp, The World Stone, Blood-Bound
    Book, Bracer of The Abyss, Death Metal, Ancient Signet, Dreamer''s Idol, Polynomicon,
    Chronos'' Pendant, Doom Orb, Bancroft''s Talon, Soul Reaver, Gem of Focus, Heartwood
    Charm, The Cosmic Horror, Typhon’s Heart, Totem of Death, Damaru, Genji''s Guard,
    Jade Scepter, Divine Ruin.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.48
      win: 0.64
      pick: 0.16
      fit: 0.17
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.5
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.49
      efficiency: 0.47
      win: 0.52
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.82
      win: 0.4
      pick: 0.37
      fit: 0.32
    Obsidian Shard:
      total: 0.52
      efficiency: 0.53
      win: 0.56
      pick: 0.3
      fit: 0.42
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Chronos' Pendant
  - Soul Gem
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Chronos'' Pendant, Gem of Focus, Heartwood
    Charm, The World Stone, Totem of Death, Damaru, Genji''s Guard, Dreamer''s Idol,
    Death Metal, Gluttonous Grimoire, Ancient Signet, Doom Orb, Polynomicon, Breastplate
    of Valor, Chandra''s Grace, Blood-Bound Book, The Cosmic Horror, Bragi''s Harp,
    Soul Reaver, Staff of Myrddin, Screeching Gargoyle, Freya''s Tears, Eye of Erebus,
    Shield of the Phoenix.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.48
      win: 0.64
      pick: 0.16
      fit: 0.14
    Spear of Desolation:
      total: 0.58
      efficiency: 0.6
      win: 0.49
      pick: 0.41
      fit: 0.86
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.63
    Soul Gem:
      total: 0.55
      efficiency: 0.53
      win: 0.46
      pick: 0.26
      fit: 0.96
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.82
      win: 0.4
      pick: 0.37
      fit: 0.37
    Obsidian Shard:
      total: 0.52
      efficiency: 0.53
      win: 0.56
      pick: 0.3
      fit: 0.47
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Soul Gem
  - Rod of Tahuti
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
    Stone, Chronos'' Pendant, Ancient Signet, The Cosmic Horror, Polynomicon, Gem
    of Focus, Heartwood Charm, Blood-Bound Book, Soul Reaver, Totem of Death, Bancroft''s
    Talon, Jade Scepter, Divine Ruin, Ethereal Staff, Helm of Radiance, Bracer of
    The Abyss, Death Metal, Staff of Myrddin, Genji''s Guard, Alchemist Coat.'
  slot_scores:
    Spear of Desolation:
      total: 0.6
      efficiency: 0.6
      win: 0.49
      pick: 0.41
      fit: 1.0
    Doom Orb:
      total: 0.53
      efficiency: 0.51
      win: 0.52
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.57
      efficiency: 0.56
      win: 0.54
      pick: 0.25
      fit: 0.79
    Soul Gem:
      total: 0.56
      efficiency: 0.53
      win: 0.46
      pick: 0.26
      fit: 1.0
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.4
      pick: 0.37
      fit: 0.79
    Obsidian Shard:
      total: 0.59
      efficiency: 0.53
      win: 0.56
      pick: 0.3
      fit: 0.89
  community_ordered:
  - Spear of Desolation
  - Spear of the Magus
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
---

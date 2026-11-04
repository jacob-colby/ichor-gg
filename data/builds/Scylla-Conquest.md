---
type: smite-build
god: Scylla
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.67
    win_rate: 1.0
    alternates:
    - name: Ancient Signet
      pick_rate: 0.33
      win_rate: 1.0
  - name: Killing Stone
    pick_rate: 0.33
    win_rate: 1.0
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.33
      win_rate: 1.0
    - name: Necronomicon
      pick_rate: 0.33
      win_rate: 1.0
  - name: Rod of Tahuti
    pick_rate: 0.67
    win_rate: 1.0
    alternates:
    - name: Gem
      pick_rate: 0.33
      win_rate: 1.0
  - name: Spear of the Magus
    pick_rate: 0.67
    win_rate: 1.0
    alternates:
    - name: Circlet
      pick_rate: 0.33
      win_rate: 1.0
  - name: Polynomicon
    pick_rate: 0.5
    win_rate: 1.0
    alternates:
    - name: Talisman of Purification
      pick_rate: 0.5
      win_rate: 1.0
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.67
    win_rate: 1.0
  - name: Conduit Gem
    pick_rate: 0.33
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/scylla/
  last_verified: '2026-11-04'
  god_win_rate: 1
  god_matches_won: 3
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
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Soul Gem
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Obsidian Shard, Soul Gem, Gluttonous Grimoire, Doom Orb, The World Stone,
    Dreamer''s Idol, Chronos'' Pendant, The Cosmic Horror, Gem of Focus, Heartwood
    Charm, Blood-Bound Book, Totem of Death, Soul Reaver, Book of Thoth, Divine Ruin,
    Jade Scepter, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin,
    Typhon’s Heart, Alchemist Coat, Bracer of The Abyss, Death Metal.'
  slot_scores:
    Spear of Desolation:
      total: 0.84
      efficiency: 0.59
      win: 1.0
      pick: 0.67
      fit: 1.0
    Doom Orb:
      total: 0.76
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.92
      efficiency: 0.86
      win: 1.0
      pick: 1.0
      fit: 0.79
    Spear of the Magus:
      total: 0.82
      efficiency: 0.58
      win: 1.0
      pick: 1.0
      fit: 0.79
    Obsidian Shard:
      total: 0.79
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.89
    Soul Gem:
      total: 0.78
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Polynomicon
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Obsidian Shard, Death Metal, Doom Orb, The World Stone, Gluttonous Grimoire,
    Chronos'' Pendant, Heartwood Charm, Dreamer''s Idol, Bragi''s Harp, Gem of Focus,
    Soul Reaver, Blood-Bound Book, The Cosmic Horror, Book of Thoth, Bancroft''s Talon,
    Triton''s Conch, Totem of Death, Divine Ruin, Jade Scepter, Genji''s Guard, Helm
    of Radiance, Ethereal Staff, Wish-Granting Pearl.'
  slot_scores:
    Book of Thoth:
      total: 0.68
      efficiency: 0.49
      win: 1.0
      pick: 0.0
      fit: 0.39
    Spear of Desolation:
      total: 0.78
      efficiency: 0.59
      win: 1.0
      pick: 0.67
      fit: 0.61
    Rod of Tahuti:
      total: 0.89
      efficiency: 0.86
      win: 1.0
      pick: 1.0
      fit: 0.57
    Spear of the Magus:
      total: 0.77
      efficiency: 0.58
      win: 1.0
      pick: 1.0
      fit: 0.47
    Polynomicon:
      total: 0.75
      efficiency: 0.5
      win: 1.0
      pick: 1.0
      fit: 0.49
    Soul Gem:
      total: 0.74
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Polynomicon
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  - Polynomicon
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Polynomicon
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Obsidian Shard, Gluttonous Grimoire, Doom Orb, The World Stone,
    Dreamer''s Idol, Chronos'' Pendant, Death Metal, The Cosmic Horror, Gem of Focus,
    Heartwood Charm, Bragi''s Harp, Blood-Bound Book, Totem of Death, Soul Reaver,
    Book of Thoth, Damaru, Divine Ruin, Jade Scepter, Genji''s Guard, Triton''s Conch,
    Bancroft''s Talon, Helm of Radiance, Ethereal Staff.'
  slot_scores:
    Spear of Desolation:
      total: 0.81
      efficiency: 0.59
      win: 1.0
      pick: 0.67
      fit: 0.78
    Rod of Tahuti:
      total: 0.89
      efficiency: 0.86
      win: 1.0
      pick: 1.0
      fit: 0.56
    Spear of the Magus:
      total: 0.78
      efficiency: 0.58
      win: 1.0
      pick: 1.0
      fit: 0.56
    Obsidian Shard:
      total: 0.75
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.66
    Polynomicon:
      total: 0.72
      efficiency: 0.5
      win: 1.0
      pick: 1.0
      fit: 0.32
    Soul Gem:
      total: 0.77
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Polynomicon
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    Kinetic Cuirass, Ethereal Staff, Genji''s Guard, Obsidian Shard, Phoenix Feather,
    Blood-Bound Book, Freya''s Tears, Yogi''s Necklace, Helm of Radiance, Sphere of
    Negation, Helm of Darkness, Breastplate of Valor, Erosion, Oni Hunter''s Garb,
    Eye of Providence, Chandra''s Grace, Jade Scepter, Draconic Scale, Midgardian
    Mail, Doom Orb, Regrowth Striders.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.74
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.76
      efficiency: 0.59
      win: 1.0
      pick: 0.67
      fit: 0.49
    Rod of Tahuti:
      total: 0.86
      efficiency: 0.86
      win: 1.0
      pick: 1.0
      fit: 0.39
    Spear of the Magus:
      total: 0.76
      efficiency: 0.58
      win: 1.0
      pick: 1.0
      fit: 0.39
    Amanita Charm:
      total: 0.8
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.77
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.89
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Soul Gem
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
    for this god: Obsidian Shard, Soul Gem, Gluttonous Grimoire, Doom Orb, The World
    Stone, Dreamer''s Idol, The Cosmic Horror, Chronos'' Pendant, Gem of Focus, Heartwood
    Charm, Blood-Bound Book, Totem of Death, Soul Reaver, Book of Thoth, Divine Ruin,
    Jade Scepter, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Screeching
    Gargoyle, Typhon’s Heart, Genji''s Guard, Alchemist Coat, Staff of Myrddin.'
  slot_scores:
    Spear of Desolation:
      total: 0.84
      efficiency: 0.59
      win: 1.0
      pick: 0.67
      fit: 1.0
    Doom Orb:
      total: 0.76
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.93
      efficiency: 0.86
      win: 1.0
      pick: 1.0
      fit: 0.85
    Spear of the Magus:
      total: 0.83
      efficiency: 0.58
      win: 1.0
      pick: 1.0
      fit: 0.85
    Obsidian Shard:
      total: 0.8
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.95
    Soul Gem:
      total: 0.78
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Spear of Desolation
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Spear of the Magus
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
    this god: Nimble Ring, Soul Gem, Gluttonous Grimoire, Obsidian Shard, Bragi''s
    Harp, Blood-Bound Book, Bracer of The Abyss, Death Metal, Doom Orb, The World
    Stone, Chronos'' Pendant, Dreamer''s Idol, Bancroft''s Talon, Gem of Focus, Heartwood
    Charm, The Cosmic Horror, Typhon’s Heart, Soul Reaver, Book of Thoth, Divine Ruin,
    Jade Scepter, Totem of Death, Damaru, Helm of Radiance.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.69
      efficiency: 0.52
      win: 1.0
      pick: 0.0
      fit: 0.4
    Spear of Desolation:
      total: 0.75
      efficiency: 0.59
      win: 1.0
      pick: 0.67
      fit: 0.4
    Nimble Ring:
      total: 0.74
      efficiency: 0.63
      win: 1.0
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.7
      efficiency: 0.45
      win: 1.0
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.85
      efficiency: 0.86
      win: 1.0
      pick: 1.0
      fit: 0.32
    Spear of the Magus:
      total: 0.75
      efficiency: 0.58
      win: 1.0
      pick: 1.0
      fit: 0.32
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Chronos' Pendant
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Chronos'' Pendant, Obsidian
    Shard, Gem of Focus, Heartwood Charm, Totem of Death, Gluttonous Grimoire, Damaru,
    Doom Orb, Genji''s Guard, The World Stone, Death Metal, Dreamer''s Idol, Breastplate
    of Valor, Chandra''s Grace, The Cosmic Horror, Staff of Myrddin, Blood-Bound Book,
    Eye of Erebus, Screeching Gargoyle, Bragi''s Harp, Soul Reaver, Book of Thoth,
    Freya''s Tears.'
  slot_scores:
    Chronos' Pendant:
      total: 0.74
      efficiency: 0.55
      win: 1.0
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.82
      efficiency: 0.59
      win: 1.0
      pick: 0.67
      fit: 0.86
    Rod of Tahuti:
      total: 0.86
      efficiency: 0.86
      win: 1.0
      pick: 1.0
      fit: 0.37
    Spear of the Magus:
      total: 0.76
      efficiency: 0.58
      win: 1.0
      pick: 1.0
      fit: 0.37
    Obsidian Shard:
      total: 0.72
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.47
    Soul Gem:
      total: 0.78
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Spear of the Magus
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
    Underrated for this god: Obsidian Shard, Soul Gem, Gluttonous Grimoire, Doom Orb,
    The World Stone, Dreamer''s Idol, Chronos'' Pendant, The Cosmic Horror, Gem of
    Focus, Heartwood Charm, Blood-Bound Book, Totem of Death, Soul Reaver, Book of
    Thoth, Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm of Radiance, Ethereal
    Staff, Staff of Myrddin, Typhon’s Heart, Alchemist Coat, Bracer of The Abyss,
    Death Metal.'
  slot_scores:
    Spear of Desolation:
      total: 0.84
      efficiency: 0.59
      win: 1.0
      pick: 0.67
      fit: 1.0
    Doom Orb:
      total: 0.76
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.92
      efficiency: 0.86
      win: 1.0
      pick: 1.0
      fit: 0.79
    Spear of the Magus:
      total: 0.82
      efficiency: 0.58
      win: 1.0
      pick: 1.0
      fit: 0.79
    Obsidian Shard:
      total: 0.79
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.89
    Soul Gem:
      total: 0.78
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  starter: *id001
---

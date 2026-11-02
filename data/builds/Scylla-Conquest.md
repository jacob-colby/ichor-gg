---
type: smite-build
god: Scylla
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Devourer
  aspect_pick_rate: 0.14
  aspect_win_rate: 0.6
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.42
    win_rate: 0.53
    alternates:
    - name: Book of Thoth
      pick_rate: 0.23
      win_rate: 0.6
    - name: Yogi's Necklace
      pick_rate: 0.09
      win_rate: 0.59
  - name: Book of Thoth
    pick_rate: 0.21
    win_rate: 0.53
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.26
      win_rate: 0.6
    - name: Polynomicon
      pick_rate: 0.12
      win_rate: 0.52
  - name: Rod of Tahuti
    pick_rate: 0.31
    win_rate: 0.55
    alternates:
    - name: Polynomicon
      pick_rate: 0.27
      win_rate: 0.58
    - name: Spear of Desolation
      pick_rate: 0.06
      win_rate: 0.51
  - name: Obsidian Shard
    pick_rate: 0.23
    win_rate: 0.52
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.32
      win_rate: 0.61
    - name: Polynomicon
      pick_rate: 0.09
      win_rate: 0.58
  - name: Polynomicon
    pick_rate: 0.07
    win_rate: 0.59
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.3
      win_rate: 0.61
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.55
  - name: Blinking Abyss
    pick_rate: 0.12
    win_rate: 0.6
    alternates:
    - name: Evil Eye
      pick_rate: 0.08
      win_rate: 0.61
    - name: Obsidian Shard
      pick_rate: 0.06
      win_rate: 0.74
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.6
    win_rate: 0.6
  - name: Conduit Gem
    pick_rate: 0.3
    win_rate: 0.48
  - name: Bluestone Pendant
    pick_rate: 0.05
    win_rate: 0.75
  source_url: https://smitebrain.com/gods/scylla/
  last_verified: '2026-10-30'
  god_win_rate: 0.5562347188264058
  god_matches_won: 455
  god_matches_played: 818
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-30'
  god_matches_analyzed: 10706
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Spear of the Magus, Soul Gem, Gluttonous Grimoire, Doom Orb, The World
    Stone, Dreamer''s Idol, Lotus Sickle, Chronos'' Pendant, The Cosmic Horror, Gem
    of Focus, Ancient Signet, Totem of Death, Rod of Asclepius, Soul Reaver, Blood-Bound
    Book, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal
    Staff, Staff of Myrddin, Wish-Granting Pearl, Typhon’s Heart, Bracer of The Abyss.'
  slot_scores:
    Spear of Desolation:
      total: 0.61
      efficiency: 0.58
      win: 0.53
      pick: 0.42
      fit: 1.0
    Doom Orb:
      total: 0.56
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.59
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.85
      win: 0.55
      pick: 0.48
      fit: 0.79
    Obsidian Shard:
      total: 0.58
      efficiency: 0.55
      win: 0.52
      pick: 0.38
      fit: 0.89
    Soul Gem:
      total: 0.59
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Lotus Sickle
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Spear of the Magus
  - Soul Gem
  flex_slots:
  - Lotus Sickle
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Spear of the Magus, Lotus Sickle, Doom Orb, The World Stone, Death Metal,
    Gluttonous Grimoire, Chronos'' Pendant, Ancient Signet, Dreamer''s Idol, Bragi''s
    Harp, Gem of Focus, Soul Reaver, The Cosmic Horror, Rod of Asclepius, Bancroft''s
    Talon, Totem of Death, Triton''s Conch, Blood-Bound Book, Jade Scepter, Divine
    Ruin, Wish-Granting Pearl, Helm of Radiance, Genji''s Guard.'
  slot_scores:
    Lotus Sickle:
      total: 0.54
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.53
    Spear of Desolation:
      total: 0.55
      efficiency: 0.58
      win: 0.53
      pick: 0.42
      fit: 0.61
    Doom Orb:
      total: 0.53
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.85
      win: 0.55
      pick: 0.48
      fit: 0.57
    Spear of the Magus:
      total: 0.54
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.47
    Soul Gem:
      total: 0.54
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom Orb, Lotus Sickle,
    The World Stone, Dreamer''s Idol, Chronos'' Pendant, Death Metal, Gem of Focus,
    The Cosmic Horror, Ancient Signet, Bragi''s Harp, Totem of Death, Rod of Asclepius,
    Soul Reaver, Blood-Bound Book, Jade Scepter, Divine Ruin, Triton''s Conch, Bancroft''s
    Talon, Genji''s Guard, Breastplate of Valor, Helm of Radiance.'
  slot_scores:
    Spear of Desolation:
      total: 0.58
      efficiency: 0.58
      win: 0.53
      pick: 0.42
      fit: 0.78
    Doom Orb:
      total: 0.52
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.55
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.85
      win: 0.55
      pick: 0.48
      fit: 0.56
    Obsidian Shard:
      total: 0.54
      efficiency: 0.55
      win: 0.52
      pick: 0.38
      fit: 0.66
    Soul Gem:
      total: 0.57
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Freya's Tears
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
    this god: Amanita Charm, Soul Gem, Rod of Asclepius, Shield of the Phoenix, Gluttonous
    Grimoire, Kinetic Cuirass, Ethereal Staff, Freya''s Tears, Spear of the Magus,
    Yogi''s Necklace, Genji''s Guard, Shifter''s Shield, Lifebinder, Breastplate of
    Valor, Helm of Radiance, Sphere of Negation, Erosion, Eye of Providence, Jade
    Scepter, Draconic Scale, Phoenix Feather, Chandra''s Grace, Lotus Sickle, Wish-Granting
    Pearl, Blood-Bound Book, Doom Orb.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.54
      efficiency: 0.58
      win: 0.53
      pick: 0.42
      fit: 0.49
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.42
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.85
      win: 0.55
      pick: 0.48
      fit: 0.39
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.57
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.89
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
    for this god: Spear of the Magus, Soul Gem, Gluttonous Grimoire, Doom Orb, The
    World Stone, Dreamer''s Idol, The Cosmic Horror, Lotus Sickle, Chronos'' Pendant,
    Gem of Focus, Ancient Signet, Rod of Asclepius, Totem of Death, Soul Reaver, Blood-Bound
    Book, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal
    Staff, Screeching Gargoyle, Wish-Granting Pearl, Typhon’s Heart, Bracer of The
    Abyss.'
  slot_scores:
    Spear of Desolation:
      total: 0.61
      efficiency: 0.58
      win: 0.53
      pick: 0.42
      fit: 1.0
    Doom Orb:
      total: 0.57
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.6
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.85
      win: 0.55
      pick: 0.48
      fit: 0.85
    Obsidian Shard:
      total: 0.59
      efficiency: 0.55
      win: 0.52
      pick: 0.38
      fit: 0.95
    Soul Gem:
      total: 0.59
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Spear of Desolation
  - Nimble Ring
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
    this god: Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear of the Magus, Bragi''s
    Harp, Bracer of The Abyss, Lotus Sickle, Doom Orb, Chronos'' Pendant, The World
    Stone, Dreamer''s Idol, Blood-Bound Book, Death Metal, Ancient Signet, Bancroft''s
    Talon, Gem of Focus, The Cosmic Horror, Rod of Asclepius, Typhon’s Heart, Soul
    Reaver, Jade Scepter, Divine Ruin, Totem of Death, Helm of Radiance.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.5
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.4
    Spear of Desolation:
      total: 0.52
      efficiency: 0.58
      win: 0.53
      pick: 0.42
      fit: 0.4
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.51
      efficiency: 0.44
      win: 0.57
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.85
      win: 0.55
      pick: 0.48
      fit: 0.32
    Soul Gem:
      total: 0.54
      efficiency: 0.57
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
  - Lotus Sickle
  - Spear of Desolation
  - Chronos' Pendant
  - Gem of Focus
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Chronos' Pendant
  - Gem of Focus
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
    + fit + win/pick). Underrated for this god: Soul Gem, Lotus Sickle, Chronos''
    Pendant, Gem of Focus, Spear of the Magus, Gluttonous Grimoire, Totem of Death,
    Doom Orb, The World Stone, Dreamer''s Idol, Genji''s Guard, Breastplate of Valor,
    Death Metal, Ancient Signet, The Cosmic Horror, Staff of Myrddin, Eye of Erebus,
    Screeching Gargoyle, Bragi''s Harp, Rod of Asclepius, Chandra''s Grace, Freya''s
    Tears, Soul Reaver, Blood-Bound Book.'
  slot_scores:
    Lotus Sickle:
      total: 0.55
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.59
      efficiency: 0.58
      win: 0.53
      pick: 0.42
      fit: 0.86
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.63
    Gem of Focus:
      total: 0.53
      efficiency: 0.5
      win: 0.57
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.85
      win: 0.55
      pick: 0.48
      fit: 0.37
    Soul Gem:
      total: 0.58
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.96
  community_ordered:
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
    Underrated for this god: Spear of the Magus, Soul Gem, Gluttonous Grimoire, Doom
    Orb, The World Stone, Dreamer''s Idol, Lotus Sickle, Chronos'' Pendant, The Cosmic
    Horror, Gem of Focus, Ancient Signet, Totem of Death, Rod of Asclepius, Soul Reaver,
    Blood-Bound Book, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance,
    Ethereal Staff, Staff of Myrddin, Wish-Granting Pearl, Typhon’s Heart, Bracer
    of The Abyss.'
  slot_scores:
    Spear of Desolation:
      total: 0.61
      efficiency: 0.58
      win: 0.53
      pick: 0.42
      fit: 1.0
    Doom Orb:
      total: 0.56
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.59
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.85
      win: 0.55
      pick: 0.48
      fit: 0.79
    Obsidian Shard:
      total: 0.58
      efficiency: 0.55
      win: 0.52
      pick: 0.38
      fit: 0.89
    Soul Gem:
      total: 0.59
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
---

---
type: smite-build
god: Ra
mode: Conquest
builds:
- source: community
  aspect: Aspect of Thermotherapy
  aspect_pick_rate: 0.04
  aspect_win_rate: 0.59
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.55
    win_rate: 0.54
    alternates:
    - name: Book of Thoth
      pick_rate: 0.26
      win_rate: 0.51
    - name: The World Stone
      pick_rate: 0.05
      win_rate: 0.41
  - name: The World Stone
    pick_rate: 0.39
    win_rate: 0.54
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.21
      win_rate: 0.53
    - name: Book of Thoth
      pick_rate: 0.1
      win_rate: 0.57
  - name: Rod of Tahuti
    pick_rate: 0.35
    win_rate: 0.55
    alternates:
    - name: The World Stone
      pick_rate: 0.13
      win_rate: 0.52
    - name: Nimble Ring
      pick_rate: 0.11
      win_rate: 0.53
  - name: Nimble Ring
    pick_rate: 0.23
    win_rate: 0.57
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.32
      win_rate: 0.55
    - name: Obsidian Shard
      pick_rate: 0.13
      win_rate: 0.47
  - name: Obsidian Shard
    pick_rate: 0.22
    win_rate: 0.6
    alternates:
    - name: Nimble Ring
      pick_rate: 0.13
      win_rate: 0.57
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.57
  - name: Blinking Abyss
    pick_rate: 0.12
    win_rate: 0.59
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.1
      win_rate: 0.53
    - name: Evil Eye
      pick_rate: 0.08
      win_rate: 0.52
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.33
    win_rate: 0.6
  - name: Archmage's Gem
    pick_rate: 0.31
    win_rate: 0.54
  - name: Conduit Gem
    pick_rate: 0.17
    win_rate: 0.49
  source_url: https://smitebrain.com/gods/ra/
  last_verified: '2026-11-02'
  god_win_rate: 0.5287713841368584
  god_matches_won: 680
  god_matches_played: 1286
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14484
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Chronos'' Pendant,
    Doom Orb, Dreamer''s Idol, Gem of Focus, Heartwood Charm, The Cosmic Horror, Totem
    of Death, Ancient Signet, Blood-Bound Book, Polynomicon, Soul Reaver, Divine Ruin,
    Jade Scepter, Staff of Myrddin, Bancroft''s Talon, Helm of Radiance, Ethereal
    Staff, Genji''s Guard, Typhon’s Heart, Rod of Asclepius, Bracer of The Abyss.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.5
      win: 0.51
      pick: 0.26
      fit: 0.41
    Spear of Desolation:
      total: 0.63
      efficiency: 0.59
      win: 0.54
      pick: 0.55
      fit: 1.0
    The World Stone:
      total: 0.56
      efficiency: 0.53
      win: 0.54
      pick: 0.53
      fit: 0.72
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.87
      win: 0.55
      pick: 0.55
      fit: 0.72
    Obsidian Shard:
      total: 0.62
      efficiency: 0.58
      win: 0.6
      pick: 0.48
      fit: 0.82
    Soul Gem:
      total: 0.58
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - The World Stone
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Death Metal, Doom Orb, Spear of the Magus, Gluttonous Grimoire, Chronos''
    Pendant, Heartwood Charm, Ancient Signet, Polynomicon, Dreamer''s Idol, Bragi''s
    Harp, Gem of Focus, Soul Reaver, Blood-Bound Book, The Cosmic Horror, Bancroft''s
    Talon, Totem of Death, Triton''s Conch, Divine Ruin, Jade Scepter, Genji''s Guard,
    Helm of Radiance, Ethereal Staff, Wish-Granting Pearl.'
  slot_scores:
    Spear of Desolation:
      total: 0.57
      efficiency: 0.59
      win: 0.54
      pick: 0.55
      fit: 0.61
    Doom Orb:
      total: 0.52
      efficiency: 0.54
      win: 0.55
      pick: 0.0
      fit: 0.57
    The World Stone:
      total: 0.54
      efficiency: 0.53
      win: 0.54
      pick: 0.53
      fit: 0.57
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.87
      win: 0.55
      pick: 0.55
      fit: 0.57
    Obsidian Shard:
      total: 0.58
      efficiency: 0.58
      win: 0.6
      pick: 0.48
      fit: 0.57
    Soul Gem:
      total: 0.54
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The World Stone
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s Idol,
    Chronos'' Pendant, Death Metal, Gem of Focus, The Cosmic Horror, Heartwood Charm,
    Ancient Signet, Bragi''s Harp, Blood-Bound Book, Polynomicon, Totem of Death,
    Soul Reaver, Divine Ruin, Jade Scepter, Damaru, Genji''s Guard, Triton''s Conch,
    Bancroft''s Talon, Helm of Radiance, Breastplate of Valor.'
  slot_scores:
    Spear of Desolation:
      total: 0.59
      efficiency: 0.59
      win: 0.54
      pick: 0.55
      fit: 0.78
    Spear of the Magus:
      total: 0.53
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.56
    The World Stone:
      total: 0.54
      efficiency: 0.53
      win: 0.54
      pick: 0.53
      fit: 0.56
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.87
      win: 0.55
      pick: 0.55
      fit: 0.56
    Obsidian Shard:
      total: 0.6
      efficiency: 0.58
      win: 0.6
      pick: 0.48
      fit: 0.66
    Soul Gem:
      total: 0.56
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Kinetic Cuirass
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
    this god: Amanita Charm, Soul Gem, Shield of the Phoenix, Kinetic Cuirass, Gluttonous
    Grimoire, Genji''s Guard, Ethereal Staff, Freya''s Tears, Breastplate of Valor,
    Phoenix Feather, Blood-Bound Book, Helm of Radiance, Yogi''s Necklace, Rod of
    Asclepius, Sphere of Negation, Helm of Darkness, Chandra''s Grace, Spear of the
    Magus, Erosion, Eye of Providence, Jade Scepter, Oni Hunter''s Garb, Draconic
    Scale, Glorious Pridwen, Chronos'' Pendant, Regrowth Striders.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.6
    Spear of Desolation:
      total: 0.55
      efficiency: 0.59
      win: 0.54
      pick: 0.55
      fit: 0.5
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.87
      win: 0.55
      pick: 0.55
      fit: 0.36
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.8
    Obsidian Shard:
      total: 0.57
      efficiency: 0.58
      win: 0.6
      pick: 0.48
      fit: 0.46
    Soul Gem:
      total: 0.56
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.9
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The World Stone
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
    for this god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s
    Idol, The Cosmic Horror, Chronos'' Pendant, Gem of Focus, Heartwood Charm, Ancient
    Signet, Blood-Bound Book, Polynomicon, Totem of Death, Soul Reaver, Divine Ruin,
    Jade Scepter, Screeching Gargoyle, Bancroft''s Talon, Helm of Radiance, Ethereal
    Staff, Genji''s Guard, Staff of Myrddin, Typhon’s Heart, Breastplate of Valor.'
  slot_scores:
    Spear of Desolation:
      total: 0.63
      efficiency: 0.59
      win: 0.54
      pick: 0.55
      fit: 1.0
    Spear of the Magus:
      total: 0.57
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.81
    The World Stone:
      total: 0.58
      efficiency: 0.53
      win: 0.54
      pick: 0.53
      fit: 0.81
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.87
      win: 0.55
      pick: 0.55
      fit: 0.81
    Obsidian Shard:
      total: 0.63
      efficiency: 0.58
      win: 0.6
      pick: 0.48
      fit: 0.91
    Soul Gem:
      total: 0.58
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Spear of Desolation
  - Bragi's Harp
  - Rod of Tahuti
  - Nimble Ring
  - Obsidian Shard
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
    this god: Soul Gem, Gluttonous Grimoire, Bragi''s Harp, Spear of the Magus, Blood-Bound
    Book, Bracer of The Abyss, Chronos'' Pendant, Death Metal, Doom Orb, Eros'' Bow,
    Dreamer''s Idol, Gem of Focus, Ancient Signet, Heartwood Charm, Bancroft''s Talon,
    Polynomicon, The Cosmic Horror, Typhon’s Heart, Soul Reaver, Totem of Death, Divine
    Ruin, Jade Scepter, Damaru.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.4
    Spear of Desolation:
      total: 0.54
      efficiency: 0.59
      win: 0.54
      pick: 0.55
      fit: 0.41
    Bragi's Harp:
      total: 0.5
      efficiency: 0.45
      win: 0.55
      pick: 0.0
      fit: 0.62
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.87
      win: 0.55
      pick: 0.55
      fit: 0.29
    Nimble Ring:
      total: 0.57
      efficiency: 0.64
      win: 0.57
      pick: 0.38
      fit: 0.48
    Obsidian Shard:
      total: 0.56
      efficiency: 0.58
      win: 0.6
      pick: 0.48
      fit: 0.39
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Nimble Ring
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Gem of Focus
  - Rod of Tahuti
  - Obsidian Shard
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
    + fit + win/pick). Underrated for this god: Soul Gem, Chronos'' Pendant, Gem of
    Focus, Heartwood Charm, Spear of the Magus, Totem of Death, Damaru, Gluttonous
    Grimoire, Genji''s Guard, Doom Orb, Death Metal, Breastplate of Valor, Dreamer''s
    Idol, Chandra''s Grace, Staff of Myrddin, Ancient Signet, The Cosmic Horror, Blood-Bound
    Book, Polynomicon, Eye of Erebus, Screeching Gargoyle, Bragi''s Harp, Soul Reaver,
    Freya''s Tears.'
  slot_scores:
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.55
      win: 0.55
      pick: 0.0
      fit: 0.65
    Spear of Desolation:
      total: 0.6
      efficiency: 0.59
      win: 0.54
      pick: 0.55
      fit: 0.85
    Gem of Focus:
      total: 0.52
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.65
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.87
      win: 0.55
      pick: 0.55
      fit: 0.35
    Obsidian Shard:
      total: 0.56
      efficiency: 0.58
      win: 0.6
      pick: 0.48
      fit: 0.45
    Soul Gem:
      total: 0.57
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.95
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - Chronos' Pendant
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
    Underrated for this god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Chronos''
    Pendant, Doom Orb, Dreamer''s Idol, Gem of Focus, Heartwood Charm, The Cosmic
    Horror, Totem of Death, Ancient Signet, Blood-Bound Book, Polynomicon, Soul Reaver,
    Divine Ruin, Jade Scepter, Staff of Myrddin, Bancroft''s Talon, Helm of Radiance,
    Ethereal Staff, Genji''s Guard, Typhon’s Heart, Rod of Asclepius, Bracer of The
    Abyss.'
  slot_scores:
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.55
      win: 0.55
      pick: 0.0
      fit: 0.69
    Spear of Desolation:
      total: 0.63
      efficiency: 0.59
      win: 0.54
      pick: 0.55
      fit: 1.0
    Spear of the Magus:
      total: 0.55
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.72
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.87
      win: 0.55
      pick: 0.55
      fit: 0.72
    Obsidian Shard:
      total: 0.62
      efficiency: 0.58
      win: 0.6
      pick: 0.48
      fit: 0.82
    Soul Gem:
      total: 0.58
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Void Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Void Stone
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Amanita Charm, Genji''s Guard, Gluttonous Grimoire, Rod of
    Asclepius, Void Stone, Doublet of Binding, Chandra''s Grace, Spear of the Magus,
    Screeching Gargoyle, Ethereal Staff, Lifebinder, Phoenix Feather, Chronos'' Pendant,
    Oni Hunter''s Garb, Yogi''s Necklace, Doom Orb, Eros'' Bow, Blood-Bound Book,
    Jade Scepter, Sphere of Negation, Gem of Focus, Dreamer''s Idol, Erosion, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.55
      pick: 0.0
      fit: 0.42
    Spear of Desolation:
      total: 0.57
      efficiency: 0.59
      win: 0.54
      pick: 0.55
      fit: 0.65
    Void Stone:
      total: 0.52
      efficiency: 0.46
      win: 0.55
      pick: 0.0
      fit: 0.75
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.87
      win: 0.55
      pick: 0.55
      fit: 0.39
    Obsidian Shard:
      total: 0.57
      efficiency: 0.58
      win: 0.6
      pick: 0.48
      fit: 0.49
    Soul Gem:
      total: 0.58
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - The World Stone
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Amanita Charm, Triton''s Conch, Genji''s Guard, Rod of Asclepius, Gluttonous
    Grimoire, Death Metal, Spear of the Magus, Ethereal Staff, Doom Orb, Lifebinder,
    Blood-Bound Book, Void Stone, Yogi''s Necklace, Chronos'' Pendant, Eros'' Bow,
    Sphere of Negation, Jade Scepter, Wish-Granting Pearl, Ancient Signet, Bancroft''s
    Talon, Heartwood Charm, Chandra''s Grace, Doublet of Binding, Polynomicon.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.55
      pick: 0.0
      fit: 0.28
    Spear of Desolation:
      total: 0.55
      efficiency: 0.59
      win: 0.54
      pick: 0.55
      fit: 0.5
    The World Stone:
      total: 0.52
      efficiency: 0.53
      win: 0.54
      pick: 0.53
      fit: 0.47
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.87
      win: 0.55
      pick: 0.55
      fit: 0.47
    Obsidian Shard:
      total: 0.57
      efficiency: 0.58
      win: 0.6
      pick: 0.48
      fit: 0.48
    Soul Gem:
      total: 0.58
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Genji's Guard
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Amanita Charm, Gluttonous Grimoire, Genji''s Guard, Rod of Asclepius,
    Triton''s Conch, Spear of the Magus, Doom Orb, Void Stone, Ethereal Staff, Lifebinder,
    Chronos'' Pendant, Blood-Bound Book, Death Metal, Dreamer''s Idol, Doublet of
    Binding, Screeching Gargoyle, Chandra''s Grace, Eros'' Bow, Yogi''s Necklace,
    Jade Scepter, Sphere of Negation, Gem of Focus, Phoenix Feather, Heartwood Charm.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.5
      win: 0.51
      pick: 0.26
      fit: 0.18
    Spear of Desolation:
      total: 0.57
      efficiency: 0.59
      win: 0.54
      pick: 0.55
      fit: 0.62
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.55
      pick: 0.0
      fit: 0.27
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.87
      win: 0.55
      pick: 0.55
      fit: 0.45
    Obsidian Shard:
      total: 0.58
      efficiency: 0.58
      win: 0.6
      pick: 0.48
      fit: 0.55
    Soul Gem:
      total: 0.58
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: bruiser
  slot_order:
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  - Erosion
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Amanita Charm, Soul Gem, Shield of the Phoenix, Erosion, Kinetic Cuirass,
    Rod of Asclepius, Genji''s Guard, Freya''s Tears, Stampede, Void Stone, Void Shield,
    Breastplate of Valor, Gluttonous Grimoire, Spectral Armor, Phoenix Feather, Doublet
    of Binding, Ethereal Staff, Lifebinder, Chandra''s Grace, Yogi''s Necklace, Eye
    of Providence, Draconic Scale, Glorious Pridwen, Oni Hunter''s Garb, Regrowth
    Striders, Midgardian Mail.'
  slot_scores:
    Spear of Desolation:
      total: 0.54
      efficiency: 0.59
      win: 0.54
      pick: 0.55
      fit: 0.43
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.87
      win: 0.55
      pick: 0.55
      fit: 0.26
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.55
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.87
    Obsidian Shard:
      total: 0.55
      efficiency: 0.58
      win: 0.6
      pick: 0.48
      fit: 0.36
    Soul Gem:
      total: 0.58
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: anti-tank
  slot_order:
  - Void Stone
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Void Stone
  - The World Stone
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Gluttonous Grimoire, Amanita Charm, Void Stone, Screeching
    Gargoyle, Genji''s Guard, Spear of the Magus, Doom Orb, Rod of Asclepius, Dreamer''s
    Idol, Doublet of Binding, The Cosmic Horror, Ethereal Staff, Chandra''s Grace,
    Lifebinder, Yogi''s Necklace, Phoenix Feather, Chronos'' Pendant, Oni Hunter''s
    Garb, Blood-Bound Book, Eros'' Bow, Jade Scepter, Sphere of Negation, Gem of Focus,
    Erosion.'
  slot_scores:
    Void Stone:
      total: 0.55
      efficiency: 0.46
      win: 0.55
      pick: 0.0
      fit: 0.96
    Spear of Desolation:
      total: 0.59
      efficiency: 0.59
      win: 0.54
      pick: 0.55
      fit: 0.74
    The World Stone:
      total: 0.54
      efficiency: 0.53
      win: 0.54
      pick: 0.53
      fit: 0.56
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.87
      win: 0.55
      pick: 0.55
      fit: 0.56
    Obsidian Shard:
      total: 0.6
      efficiency: 0.58
      win: 0.6
      pick: 0.48
      fit: 0.66
    Soul Gem:
      total: 0.58
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bragi's Harp
  - Nimble Ring
  - Rod of Tahuti
  - Eros' Bow
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Eros' Bow
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Amanita Charm, Eros'' Bow, Gluttonous Grimoire, Genji''s Guard,
    Blood-Bound Book, Rod of Asclepius, Void Stone, Triton''s Conch, Doublet of Binding,
    Yogi''s Necklace, Bragi''s Harp, Ethereal Staff, Bancroft''s Talon, Lifebinder,
    Spear of the Magus, Screeching Gargoyle, Chandra''s Grace, Bracer of The Abyss,
    Phoenix Feather, Oni Hunter''s Garb, Chronos'' Pendant, Death Metal, Doom Orb,
    Sphere of Negation.'
  slot_scores:
    Bragi's Harp:
      total: 0.48
      efficiency: 0.45
      win: 0.55
      pick: 0.0
      fit: 0.49
    Nimble Ring:
      total: 0.55
      efficiency: 0.64
      win: 0.57
      pick: 0.38
      fit: 0.35
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.87
      win: 0.55
      pick: 0.55
      fit: 0.17
    Eros' Bow:
      total: 0.53
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.66
    Obsidian Shard:
      total: 0.54
      efficiency: 0.58
      win: 0.6
      pick: 0.48
      fit: 0.27
    Soul Gem:
      total: 0.59
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Nimble Ring
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: cooldown
  slot_order:
  - Screeching Gargoyle
  - Spear of Desolation
  - Genji's Guard
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Genji''s Guard, Amanita
    Charm, Chandra''s Grace, Screeching Gargoyle, Chronos'' Pendant, Rod of Asclepius,
    Gluttonous Grimoire, Void Stone, Gem of Focus, Triton''s Conch, Heartwood Charm,
    Doublet of Binding, Ethereal Staff, Spear of the Magus, Lifebinder, Eye of Erebus,
    Shield of the Phoenix, Blood-Bound Book, Yogi''s Necklace, Freya''s Tears, Phoenix
    Feather, Totem of Death, Doom Orb, Oni Hunter''s Garb, Eros'' Bow.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.52
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.58
      efficiency: 0.59
      win: 0.54
      pick: 0.55
      fit: 0.67
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.55
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.87
      win: 0.55
      pick: 0.55
      fit: 0.27
    Obsidian Shard:
      total: 0.55
      efficiency: 0.58
      win: 0.6
      pick: 0.48
      fit: 0.37
    Soul Gem:
      total: 0.58
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Thermotherapy
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Void Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Void Stone
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Soul Gem, Amanita Charm, Genji''s Guard, Gluttonous Grimoire,
    Rod of Asclepius, Void Stone, Doublet of Binding, Chandra''s Grace, Spear of the
    Magus, Screeching Gargoyle, Ethereal Staff, Lifebinder, Phoenix Feather, Chronos''
    Pendant, Oni Hunter''s Garb, Yogi''s Necklace, Doom Orb, Eros'' Bow, Blood-Bound
    Book, Jade Scepter, Sphere of Negation, Gem of Focus, Dreamer''s Idol, Erosion,
    Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.55
      pick: 0.0
      fit: 0.42
    Spear of Desolation:
      total: 0.57
      efficiency: 0.59
      win: 0.54
      pick: 0.55
      fit: 0.65
    Void Stone:
      total: 0.52
      efficiency: 0.46
      win: 0.55
      pick: 0.0
      fit: 0.75
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.87
      win: 0.55
      pick: 0.55
      fit: 0.39
    Obsidian Shard:
      total: 0.57
      efficiency: 0.58
      win: 0.6
      pick: 0.48
      fit: 0.49
    Soul Gem:
      total: 0.58
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Thermotherapy
---

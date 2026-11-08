---
type: smite-build
god: Hecate
mode: Conquest
builds:
- source: community
  aspect: Aspect of Ruin
  aspect_pick_rate: 0.12
  aspect_win_rate: 0.57
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.5
    win_rate: 0.44
    alternates:
    - name: Book of Thoth
      pick_rate: 0.2
      win_rate: 0.42
    - name: Chronos' Pendant
      pick_rate: 0.11
      win_rate: 0.46
  - name: The World Stone
    pick_rate: 0.26
    win_rate: 0.39
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.16
      win_rate: 0.53
    - name: Book of Thoth
      pick_rate: 0.11
      win_rate: 0.54
  - name: Rod of Tahuti
    pick_rate: 0.2
    win_rate: 0.48
    alternates:
    - name: Soul Gem
      pick_rate: 0.14
      win_rate: 0.63
    - name: Spear of Desolation
      pick_rate: 0.13
      win_rate: 0.4
  - name: Obsidian Shard
    pick_rate: 0.13
    win_rate: 0.43
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.39
      win_rate: 0.42
    - name: Chronos' Pendant
      pick_rate: 0.08
      win_rate: 0.67
  - name: Void Shard
    pick_rate: 0.11
    win_rate: 0.2
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.25
      win_rate: 0.52
    - name: Rod of Tahuti
      pick_rate: 0.12
      win_rate: 0.64
  - name: Evil Eye
    pick_rate: 0.1
    win_rate: 0.2
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.75
    - name: Killing Stone
      pick_rate: 0.08
      win_rate: 0.5
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.39
    win_rate: 0.43
  - name: Conduit Gem
    pick_rate: 0.32
    win_rate: 0.47
  - name: Bluestone Brooch
    pick_rate: 0.11
    win_rate: 0.77
  source_url: https://smitebrain.com/gods/hecate/
  last_verified: '2026-11-08'
  god_win_rate: 0.4789915966386555
  god_matches_won: 57
  god_matches_played: 119
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-08'
  god_matches_analyzed: 5119
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
  - Obsidian Shard
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Chronos'' Pendant, Spear of the Magus, Lotus Sickle, Dreamer''s Idol,
    Gluttonous Grimoire, Doom Orb, Ancient Signet, Gem of Focus, Heartwood Charm,
    The Cosmic Horror, Polynomicon, Blood-Bound Book, Totem of Death, Soul Reaver,
    Bancroft''s Talon, Jade Scepter, Divine Ruin, Ethereal Staff, Helm of Radiance,
    Staff of Myrddin, Genji''s Guard, Bracer of The Abyss, Death Metal, Rod of Asclepius.'
  slot_scores:
    Chronos' Pendant:
      total: 0.6
      efficiency: 0.56
      win: 0.67
      pick: 0.13
      fit: 0.64
    Spear of Desolation:
      total: 0.58
      efficiency: 0.6
      win: 0.44
      pick: 0.5
      fit: 1.0
    Spear of the Magus:
      total: 0.51
      efficiency: 0.56
      win: 0.43
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.48
      pick: 0.31
      fit: 0.77
    Obsidian Shard:
      total: 0.52
      efficiency: 0.53
      win: 0.43
      pick: 0.22
      fit: 0.87
    Soul Gem:
      total: 0.63
      efficiency: 0.53
      win: 0.63
      pick: 0.22
      fit: 1.0
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Chronos' Pendant
  - Rod of Tahuti
  - Lotus Sickle
  - Soul Gem
  flex_slots:
  - Lotus Sickle
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Chronos''
    Pendant, Lotus Sickle, Death Metal, Ancient Signet, Polynomicon, Spear of the
    Magus, Doom Orb, Dreamer''s Idol, Heartwood Charm, Bragi''s Harp, Gluttonous Grimoire,
    Soul Reaver, Gem of Focus, Blood-Bound Book, The Cosmic Horror, Bancroft''s Talon,
    Totem of Death, Triton''s Conch, Genji''s Guard, Jade Scepter, Divine Ruin, Ethereal
    Staff, Damaru, Helm of Radiance.'
  slot_scores:
    Book of Thoth:
      total: 0.42
      efficiency: 0.48
      win: 0.42
      pick: 0.2
      fit: 0.39
    Spear of Desolation:
      total: 0.53
      efficiency: 0.6
      win: 0.44
      pick: 0.5
      fit: 0.61
    Chronos' Pendant:
      total: 0.57
      efficiency: 0.56
      win: 0.67
      pick: 0.13
      fit: 0.43
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.48
      pick: 0.31
      fit: 0.57
    Lotus Sickle:
      total: 0.49
      efficiency: 0.57
      win: 0.43
      pick: 0.0
      fit: 0.63
    Soul Gem:
      total: 0.59
      efficiency: 0.53
      win: 0.63
      pick: 0.22
      fit: 0.71
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Chronos' Pendant
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Lotus Sickle
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Lotus Sickle
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
    god: Chronos'' Pendant, Lotus Sickle, Spear of the Magus, Dreamer''s Idol, Gluttonous
    Grimoire, Death Metal, Doom Orb, Ancient Signet, Gem of Focus, Heartwood Charm,
    Polynomicon, The Cosmic Horror, Bragi''s Harp, Blood-Bound Book, Totem of Death,
    Soul Reaver, Damaru, Genji''s Guard, Triton''s Conch, Bancroft''s Talon, Jade
    Scepter, Divine Ruin, Breastplate of Valor, Ethereal Staff.'
  slot_scores:
    Chronos' Pendant:
      total: 0.57
      efficiency: 0.56
      win: 0.67
      pick: 0.13
      fit: 0.44
    Spear of Desolation:
      total: 0.55
      efficiency: 0.6
      win: 0.44
      pick: 0.5
      fit: 0.78
    Obsidian Shard:
      total: 0.49
      efficiency: 0.53
      win: 0.43
      pick: 0.22
      fit: 0.66
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.48
      pick: 0.31
      fit: 0.56
    Lotus Sickle:
      total: 0.48
      efficiency: 0.57
      win: 0.43
      pick: 0.0
      fit: 0.54
    Soul Gem:
      total: 0.61
      efficiency: 0.53
      win: 0.63
      pick: 0.22
      fit: 0.88
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Kinetic Cuirass
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Spear of Desolation
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
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Genji''s Guard,
    Ethereal Staff, Gluttonous Grimoire, Freya''s Tears, Phoenix Feather, Blood-Bound
    Book, Yogi''s Necklace, Rod of Asclepius, Soul Locket, Breastplate of Valor, Lotus
    Sickle, Chandra''s Grace, Draconic Scale, Oni Hunter''s Garb, Helm of Radiance,
    Sphere of Negation, Erosion, Helm of Darkness, Spear of the Magus, Eye of Providence,
    Shifter''s Shield, Regrowth Striders, Jade Scepter.'
  slot_scores:
    Chronos' Pendant:
      total: 0.55
      efficiency: 0.56
      win: 0.67
      pick: 0.13
      fit: 0.32
    Spear of Desolation:
      total: 0.51
      efficiency: 0.6
      win: 0.44
      pick: 0.5
      fit: 0.5
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.61
      win: 0.43
      pick: 0.0
      fit: 0.6
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.82
      win: 0.48
      pick: 0.31
      fit: 0.38
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
      win: 0.43
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.62
      efficiency: 0.53
      win: 0.63
      pick: 0.22
      fit: 0.9
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
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
    for this god: Chronos'' Pendant, Spear of the Magus, Dreamer''s Idol, Gluttonous
    Grimoire, Doom Orb, The Cosmic Horror, Lotus Sickle, Ancient Signet, Polynomicon,
    Gem of Focus, Heartwood Charm, Blood-Bound Book, Soul Reaver, Totem of Death,
    Bancroft''s Talon, Jade Scepter, Divine Ruin, Screeching Gargoyle, Genji''s Guard,
    Ethereal Staff, Helm of Radiance, Bracer of The Abyss, Death Metal, Rod of Asclepius.'
  slot_scores:
    Chronos' Pendant:
      total: 0.57
      efficiency: 0.56
      win: 0.67
      pick: 0.13
      fit: 0.45
    Spear of Desolation:
      total: 0.58
      efficiency: 0.6
      win: 0.44
      pick: 0.5
      fit: 1.0
    Spear of the Magus:
      total: 0.52
      efficiency: 0.56
      win: 0.43
      pick: 0.0
      fit: 0.84
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.48
      pick: 0.31
      fit: 0.84
    Obsidian Shard:
      total: 0.53
      efficiency: 0.53
      win: 0.43
      pick: 0.22
      fit: 0.94
    Soul Gem:
      total: 0.63
      efficiency: 0.53
      win: 0.63
      pick: 0.22
      fit: 1.0
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Chronos' Pendant
  - Bracer of The Abyss
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
    this god: Chronos'' Pendant, Nimble Ring, Gluttonous Grimoire, Bragi''s Harp,
    Lotus Sickle, Blood-Bound Book, Bracer of The Abyss, Spear of the Magus, Death
    Metal, Ancient Signet, Dreamer''s Idol, Polynomicon, Doom Orb, Eros'' Bow, Bancroft''s
    Talon, Gem of Focus, Heartwood Charm, Soul Reaver, The Cosmic Horror, Typhon’s
    Heart, Totem of Death, Damaru, Genji''s Guard, Jade Scepter.'
  slot_scores:
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.56
      win: 0.67
      pick: 0.13
      fit: 0.26
    Bracer of The Abyss:
      total: 0.44
      efficiency: 0.52
      win: 0.43
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.47
      efficiency: 0.57
      win: 0.43
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.45
      efficiency: 0.47
      win: 0.43
      pick: 0.0
      fit: 0.62
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.82
      win: 0.48
      pick: 0.31
      fit: 0.31
    Soul Gem:
      total: 0.59
      efficiency: 0.58
      win: 0.63
      pick: 0.22
      fit: 0.58
  community_ordered:
  - Chronos' Pendant
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Gem of Focus
  - Rod of Tahuti
  - Lotus Sickle
  - Soul Gem
  flex_slots:
  - Lotus Sickle
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
    + fit + win/pick). Underrated for this god: Chronos'' Pendant, Lotus Sickle, Gem
    of Focus, Heartwood Charm, Totem of Death, Spear of the Magus, Damaru, Genji''s
    Guard, Dreamer''s Idol, Death Metal, Gluttonous Grimoire, Ancient Signet, Doom
    Orb, Polynomicon, Breastplate of Valor, Chandra''s Grace, Blood-Bound Book, The
    Cosmic Horror, Bragi''s Harp, Soul Reaver, Staff of Myrddin, Screeching Gargoyle,
    Freya''s Tears, Eye of Erebus, Shield of the Phoenix.'
  slot_scores:
    Chronos' Pendant:
      total: 0.6
      efficiency: 0.56
      win: 0.67
      pick: 0.13
      fit: 0.63
    Spear of Desolation:
      total: 0.56
      efficiency: 0.6
      win: 0.44
      pick: 0.5
      fit: 0.86
    Gem of Focus:
      total: 0.47
      efficiency: 0.51
      win: 0.43
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.82
      win: 0.48
      pick: 0.31
      fit: 0.37
    Lotus Sickle:
      total: 0.5
      efficiency: 0.57
      win: 0.43
      pick: 0.0
      fit: 0.73
    Soul Gem:
      total: 0.62
      efficiency: 0.53
      win: 0.63
      pick: 0.22
      fit: 0.96
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Tahuti
  - Lotus Sickle
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - Lotus Sickle
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
    Underrated for this god: Spear of the Magus, Lotus Sickle, Dreamer''s Idol, Gluttonous
    Grimoire, Doom Orb, Chronos'' Pendant, Ancient Signet, Gem of Focus, Heartwood
    Charm, The Cosmic Horror, Polynomicon, Blood-Bound Book, Totem of Death, Soul
    Reaver, Bancroft''s Talon, Jade Scepter, Divine Ruin, Ethereal Staff, Helm of
    Radiance, Staff of Myrddin, Genji''s Guard, Bracer of The Abyss, Death Metal,
    Rod of Asclepius.'
  slot_scores:
    Spear of Desolation:
      total: 0.58
      efficiency: 0.6
      win: 0.44
      pick: 0.5
      fit: 1.0
    Spear of the Magus:
      total: 0.51
      efficiency: 0.56
      win: 0.43
      pick: 0.0
      fit: 0.77
    Obsidian Shard:
      total: 0.52
      efficiency: 0.53
      win: 0.43
      pick: 0.22
      fit: 0.87
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.48
      pick: 0.31
      fit: 0.77
    Lotus Sickle:
      total: 0.51
      efficiency: 0.57
      win: 0.43
      pick: 0.0
      fit: 0.74
    Soul Gem:
      total: 0.63
      efficiency: 0.53
      win: 0.63
      pick: 0.22
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
community_aspects:
  source: SmiteBrain per-match feed, obsidian+ (data/Analysis/aspect_matches)
  complete_from: '2026-09-24'
  partial_windows:
    ob44: '2026-09-24'
  minimum_matches: 30
  window_rule: the newest patch window, or the last closed one when the newest holds
    fewer than minimum_matches of the aspect's matches
  aspects:
  - aspect: Aspect of Ruin
    status: shown
    window: ob46
    window_rule: last closed
    window_start: '2026-10-20'
    window_end: '2026-11-03'
    matches: 39
    wins: 18
    win_share: 0.46
    aggregate:
      aspect_matches: 48
      aspect_win_rate: 0.479
      no_aspect_matches: 372
      no_aspect_win_rate: 0.589
    roles:
    - role: Mid
      matches: 32
      share: 0.82
    - role: Support
      matches: 6
      share: 0.15
    - role: Solo
      matches: 1
      share: 0.03
    base_role: Mid
    base_role_share: 0.82
    role_shift: null
    items:
    - name: Chronos' Pendant
      share: 0.49
    - name: Soul Reaver
      share: 0.41
    - name: Spear of Desolation
      share: 0.41
    - name: Divine Ruin
      share: 0.36
    - name: Gem of Focus
      share: 0.36
    - name: Soul Gem
      share: 0.31
    - name: The World Stone
      share: 0.31
    - name: Rod of Tahuti
      share: 0.23
    starters:
    - name: Bluestone Brooch
      share: 0.51
    - name: Bluestone Pendant
      share: 0.38
    - name: Archmage's Gem
      share: 0.05
    relics:
    - name: aegis-of-acceleration
      share: 0.49
    - name: purification-beads
      share: 0.41
    - name: phantom-shell
      share: 0.08
    matches_by_window:
      ob47: 14
      ob46: 39
      ob45: 33
      ob44: 35
    unmapped_slugs:
    - aegis-of-acceleration
    - brawlers-ruin
    - phantom-shell
    - purification-beads
    - sundering-arc
---

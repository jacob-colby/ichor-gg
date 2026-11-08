---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.73
  aspect_win_rate: 0.53
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.16
    win_rate: 0.37
    alternates:
    - name: Alchemist Coat
      pick_rate: 0.15
      win_rate: 0.46
    - name: Chronos' Pendant
      pick_rate: 0.11
      win_rate: 0.57
  - name: Breastplate of Valor
    pick_rate: 0.11
    win_rate: 0.62
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.53
    - name: Spear of Desolation
      pick_rate: 0.1
      win_rate: 0.79
  - name: Freya's Tears
    pick_rate: 0.16
    win_rate: 0.67
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.09
      win_rate: 0.38
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.5
  - name: Rod of Tahuti
    pick_rate: 0.13
    win_rate: 0.7
    alternates:
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.61
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.67
  - name: Obsidian Shard
    pick_rate: 0.08
    win_rate: 0.92
    alternates:
    - name: Doublet of Binding
      pick_rate: 0.07
      win_rate: 0.36
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.36
  - name: Evil Eye
    pick_rate: 0.06
    win_rate: 0.33
    alternates:
    - name: Xibalban Effigy
      pick_rate: 0.05
      win_rate: 0.4
    - name: Veve Charm
      pick_rate: 0.04
      win_rate: 0.75
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.18
    win_rate: 0.52
  - name: Conduit Gem
    pick_rate: 0.14
    win_rate: 0.44
  - name: Archmage's Gem
    pick_rate: 0.13
    win_rate: 0.79
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-11-08'
  god_win_rate: 0.5401069518716578
  god_matches_won: 101
  god_matches_played: 187
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
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Obsidian Shard
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Breastplate of Valor
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Gluttonous Grimoire, Kinetic Cuirass, Genji''s
    Guard, Shield of the Phoenix, Lotus Sickle, Helm of Radiance, Blood-Bound Book,
    Draconic Scale, Helm of Darkness, Oni Hunter''s Garb, Chronos'' Pendant, Spear
    of the Magus, Erosion, Eye of Providence, Ancient Signet, Screeching Gargoyle,
    Shifter''s Shield, Dreamer''s Idol, Midgardian Mail, Polynomicon, Jade Scepter,
    Stone of Binding, Leviathan''s Hide.'
  slot_scores:
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.63
      win: 0.62
      pick: 0.15
      fit: 0.28
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.25
      fit: 0.44
    Obsidian Shard:
      total: 0.68
      efficiency: 0.53
      win: 0.92
      pick: 0.17
      fit: 0.44
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.82
      win: 0.7
      pick: 0.22
      fit: 0.34
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  - Obsidian Shard
  - Rod of Tahuti
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Obsidian Shard
  - Rod of Tahuti
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
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Genji''s
    Guard, Amanita Charm, Soul Gem, Gluttonous Grimoire, Kinetic Cuirass, Lotus Sickle,
    Ancient Signet, Death Metal, Blood-Bound Book, Oni Hunter''s Garb, Helm of Radiance,
    Polynomicon, Shield of the Phoenix, Chronos'' Pendant, Spear of the Magus, Helm
    of Darkness, Draconic Scale, Dreamer''s Idol, Doom Orb, Screeching Gargoyle, Jade
    Scepter, Erosion, Bancroft''s Talon, Eye of Providence, Triton''s Conch.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.48
      win: 0.57
      pick: 0.0
      fit: 0.24
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.26
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.63
      win: 0.62
      pick: 0.15
      fit: 0.26
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.25
      fit: 0.31
    Obsidian Shard:
      total: 0.67
      efficiency: 0.53
      win: 0.92
      pick: 0.17
      fit: 0.39
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.82
      win: 0.7
      pick: 0.22
      fit: 0.35
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  - Obsidian Shard
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Gluttonous Grimoire, Amanita Charm, Genji''s Guard, Kinetic Cuirass,
    Lotus Sickle, Shield of the Phoenix, Spear of the Magus, Blood-Bound Book, Chronos''
    Pendant, Helm of Radiance, Oni Hunter''s Garb, Dreamer''s Idol, Draconic Scale,
    Screeching Gargoyle, Death Metal, Ancient Signet, Helm of Darkness, Erosion, Polynomicon,
    Eye of Providence, Doom Orb, Midgardian Mail, Shifter''s Shield, Leviathan''s
    Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.25
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.63
      win: 0.62
      pick: 0.15
      fit: 0.25
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.25
      fit: 0.37
    Obsidian Shard:
      total: 0.67
      efficiency: 0.53
      win: 0.92
      pick: 0.17
      fit: 0.43
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.82
      win: 0.7
      pick: 0.22
      fit: 0.33
    Soul Gem:
      total: 0.55
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.62
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  - Obsidian Shard
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Freya's Tears
  - Obsidian Shard
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Freya's Tears
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
    Blood-Bound Book, Kinetic Cuirass, Genji''s Guard, Ethereal Staff, Phoenix Feather,
    Bancroft''s Talon, Yogi''s Necklace, Lotus Sickle, Chandra''s Grace, Rod of Asclepius,
    Soul Locket, Oni Hunter''s Garb, Draconic Scale, Helm of Radiance, Sphere of Negation,
    Chronos'' Pendant, Regrowth Striders, Spear of the Magus, Erosion, Helm of Darkness,
    Eye of Providence.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.25
      fit: 0.4
    Obsidian Shard:
      total: 0.68
      efficiency: 0.53
      win: 0.92
      pick: 0.17
      fit: 0.44
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.82
      win: 0.7
      pick: 0.22
      fit: 0.34
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.75
    Soul Gem:
      total: 0.6
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.95
  community_ordered:
  - Freya's Tears
  - Obsidian Shard
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Gluttonous Grimoire, Amanita Charm, Genji''s Guard, Kinetic
    Cuirass, Screeching Gargoyle, Stone of Binding, Spear of the Magus, Void Stone,
    Void Shield, Dreamer''s Idol, Lotus Sickle, Shield of the Phoenix, Blood-Bound
    Book, Helm of Radiance, Doom Orb, Oni Hunter''s Garb, Draconic Scale, Chronos''
    Pendant, The World Stone, Helm of Darkness, Ancient Signet, Erosion, Eye of Providence,
    Polynomicon.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.24
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.63
      win: 0.62
      pick: 0.15
      fit: 0.24
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.25
      fit: 0.37
    Obsidian Shard:
      total: 0.69
      efficiency: 0.53
      win: 0.92
      pick: 0.17
      fit: 0.55
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.82
      win: 0.7
      pick: 0.22
      fit: 0.45
    Soul Gem:
      total: 0.57
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.72
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  - Obsidian Shard
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Obsidian Shard
  - Rod of Tahuti
  - Eros' Bow
  flex_slots:
  - Bragi's Harp
  - Eros' Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Soul Gem, Kinetic Cuirass, Gluttonous
    Grimoire, Nimble Ring, Lotus Sickle, Shield of the Phoenix, Blood-Bound Book,
    Bragi''s Harp, Helm of Radiance, Oni Hunter''s Garb, Ancient Signet, Chronos''
    Pendant, Eros'' Bow, Draconic Scale, Spear of the Magus, Death Metal, Polynomicon,
    Screeching Gargoyle, Bracer of The Abyss, Helm of Darkness, Erosion, Midgardian
    Mail, Dreamer''s Idol.'
  slot_scores:
    Nimble Ring:
      total: 0.5
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.33
    Bragi's Harp:
      total: 0.49
      efficiency: 0.47
      win: 0.57
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.25
      fit: 0.28
    Obsidian Shard:
      total: 0.66
      efficiency: 0.53
      win: 0.92
      pick: 0.17
      fit: 0.32
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.7
      pick: 0.22
      fit: 0.22
    Eros' Bow:
      total: 0.49
      efficiency: 0.5
      win: 0.57
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Freya's Tears
  - Obsidian Shard
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Soul Gem
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Soul Gem, Amanita
    Charm, Kinetic Cuirass, Shield of the Phoenix, Gluttonous Grimoire, Lotus Sickle,
    Screeching Gargoyle, Chronos'' Pendant, Oni Hunter''s Garb, Gladiator''s Shield,
    Draconic Scale, Blood-Bound Book, Helm of Radiance, Erosion, Eye of Providence,
    Gem of Focus, Heartwood Charm, Midgardian Mail, Shifter''s Shield, Chandra''s
    Grace, Ancient Signet, Spear of the Magus, Helm of Darkness, Prophetic Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.4
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.63
      win: 0.62
      pick: 0.15
      fit: 0.4
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.25
      fit: 0.53
    Obsidian Shard:
      total: 0.66
      efficiency: 0.53
      win: 0.92
      pick: 0.17
      fit: 0.31
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.7
      pick: 0.22
      fit: 0.21
    Soul Gem:
      total: 0.56
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.66
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  - Obsidian Shard
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Soul Gem, Gluttonous Grimoire, Kinetic
    Cuirass, Genji''s Guard, Shield of the Phoenix, Lotus Sickle, Helm of Radiance,
    Blood-Bound Book, Draconic Scale, Helm of Darkness, Oni Hunter''s Garb, Spear
    of the Magus, Erosion, Eye of Providence, Chronos'' Pendant, Ancient Signet, Screeching
    Gargoyle, Shifter''s Shield, Dreamer''s Idol, Midgardian Mail, Polynomicon, Jade
    Scepter, Stone of Binding, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.28
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.55
    Spear of Desolation:
      total: 0.46
      efficiency: 0.6
      win: 0.37
      pick: 0.16
      fit: 0.47
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.25
      fit: 0.44
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.82
      win: 0.7
      pick: 0.22
      fit: 0.34
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
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
  - aspect: Aspect of Hysteria
    status: shown
    window: ob47
    window_rule: newest
    window_start: '2026-11-03'
    window_end: '2026-11-08'
    matches: 124
    wins: 68
    win_share: 0.55
    aggregate:
      aspect_matches: 143
      aspect_win_rate: 0.524
      no_aspect_matches: 50
      no_aspect_win_rate: 0.58
    roles:
    - role: Mid
      matches: 49
      share: 0.4
    - role: Solo
      matches: 44
      share: 0.35
    - role: Support
      matches: 30
      share: 0.24
    - role: Jungle
      matches: 1
      share: 0.01
    base_role: Mid Support
    base_role_share: 0.64
    role_shift: null
    items:
    - name: Freya's Tears
      share: 0.44
    - name: Rod of Tahuti
      share: 0.36
    - name: Spear of Desolation
      share: 0.35
    - name: Breastplate of Valor
      share: 0.3
    - name: Chronos' Pendant
      share: 0.26
    - name: Alchemist Coat
      share: 0.24
    - name: Genji's Guard
      share: 0.19
    - name: Prophetic Cloak
      share: 0.16
    starters:
    - name: Bluestone Pendant
      share: 0.22
    - name: Archmage's Gem
      share: 0.19
    - name: Bluestone Brooch
      share: 0.17
    relics:
    - name: purification-beads
      share: 0.37
    - name: aegis-of-acceleration
      share: 0.33
    - name: phantom-shell
      share: 0.23
    matches_by_window:
      ob47: 124
      ob46: 240
      ob45: 244
      ob44: 234
    unmapped_slugs:
    - aegis-of-acceleration
    - agility-relic
    - brawlers-ruin
    - phantom-shell
    - purification-beads
    - sundering-arc
---

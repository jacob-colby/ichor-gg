---
type: smite-build
god: Nox
mode: Conquest
builds:
- source: community
  aspect: Aspect of Silent Night
  aspect_pick_rate: 0.2
  aspect_win_rate: 0.41
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.22
    win_rate: 0.41
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.17
      win_rate: 0.42
    - name: Chronos' Pendant
      pick_rate: 0.13
      win_rate: 0.41
  - name: Chronos' Pendant
    pick_rate: 0.11
    win_rate: 0.52
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.12
      win_rate: 0.29
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.38
  - name: Rod of Tahuti
    pick_rate: 0.13
    win_rate: 0.4
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.43
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.08
    win_rate: 0.49
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.21
      win_rate: 0.39
    - name: Obsidian Shard
      pick_rate: 0.08
      win_rate: 0.5
  - name: Obsidian Shard
    pick_rate: 0.11
    win_rate: 0.39
    alternates:
    - name: Evil Eye
      pick_rate: 0.06
      win_rate: 0.22
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 0.72
  - name: Evil Eye
    pick_rate: 0.07
    win_rate: 0.24
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.06
      win_rate: 0.55
    - name: Oracle Staff
      pick_rate: 0.04
      win_rate: 0.5
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.18
    win_rate: 0.58
  - name: Archmage's Gem
    pick_rate: 0.17
    win_rate: 0.49
  - name: Sands Of Time
    pick_rate: 0.16
    win_rate: 0.18
  source_url: https://smitebrain.com/gods/nox/
  last_verified: '2026-11-08'
  god_win_rate: 0.43291839557399725
  god_matches_won: 313
  god_matches_played: 723
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
  - Kinetic Cuirass
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Chronos' Pendant
  - Spear of Desolation
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass,
    Soul Gem, Genji''s Guard, Breastplate of Valor, Shield of the Phoenix, Draconic
    Scale, Helm of Radiance, Blood-Bound Book, Helm of Darkness, Oni Hunter''s Garb,
    Erosion, Eye of Providence, Spear of the Magus, Shifter''s Shield, Ancient Signet,
    Midgardian Mail, Dreamer''s Idol, Polynomicon, Jade Scepter, Screeching Gargoyle,
    Stone of Binding, Leviathan''s Hide.'
  slot_scores:
    Chronos' Pendant:
      total: 0.48
      efficiency: 0.56
      win: 0.52
      pick: 0.15
      fit: 0.29
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.61
      win: 0.41
      pick: 0.0
      fit: 0.58
    Spear of Desolation:
      total: 0.47
      efficiency: 0.6
      win: 0.41
      pick: 0.22
      fit: 0.44
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.49
      pick: 0.13
      fit: 0.43
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.82
      win: 0.4
      pick: 0.2
      fit: 0.34
    Amanita Charm:
      total: 0.49
      efficiency: 0.68
      win: 0.41
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Chronos' Pendant
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Freya''s
    Tears, Amanita Charm, Soul Gem, Gluttonous Grimoire, Genji''s Guard, Kinetic Cuirass,
    Breastplate of Valor, Ancient Signet, Death Metal, Blood-Bound Book, Oni Hunter''s
    Garb, Helm of Radiance, Polynomicon, Shield of the Phoenix, Spear of the Magus,
    Helm of Darkness, Draconic Scale, Dreamer''s Idol, Doom Orb, Screeching Gargoyle,
    Jade Scepter, Erosion, Bancroft''s Talon, Eye of Providence, Triton''s Conch.'
  slot_scores:
    Book of Thoth:
      total: 0.39
      efficiency: 0.48
      win: 0.41
      pick: 0.0
      fit: 0.24
    Genji's Guard:
      total: 0.47
      efficiency: 0.71
      win: 0.38
      pick: 0.12
      fit: 0.26
    Chronos' Pendant:
      total: 0.48
      efficiency: 0.56
      win: 0.52
      pick: 0.15
      fit: 0.26
    Freya's Tears:
      total: 0.49
      efficiency: 0.61
      win: 0.49
      pick: 0.13
      fit: 0.31
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.82
      win: 0.4
      pick: 0.2
      fit: 0.35
    Amanita Charm:
      total: 0.47
      efficiency: 0.68
      win: 0.41
      pick: 0.0
      fit: 0.33
  community_ordered:
  - Genji's Guard
  - Chronos' Pendant
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Chronos' Pendant
  - Kinetic Cuirass
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Kinetic Cuirass
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Freya''s Tears, Soul Gem, Gluttonous Grimoire, Amanita Charm, Kinetic Cuirass,
    Genji''s Guard, Breastplate of Valor, Shield of the Phoenix, Spear of the Magus,
    Blood-Bound Book, Helm of Radiance, Oni Hunter''s Garb, Dreamer''s Idol, Draconic
    Scale, Screeching Gargoyle, Death Metal, Ancient Signet, Helm of Darkness, Erosion,
    Polynomicon, Eye of Providence, Doom Orb, Midgardian Mail, Shifter''s Shield,
    Leviathan''s Hide.'
  slot_scores:
    Chronos' Pendant:
      total: 0.48
      efficiency: 0.56
      win: 0.52
      pick: 0.15
      fit: 0.26
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.61
      win: 0.41
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.48
      efficiency: 0.6
      win: 0.41
      pick: 0.22
      fit: 0.46
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.49
      pick: 0.13
      fit: 0.37
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.82
      win: 0.4
      pick: 0.2
      fit: 0.33
    Soul Gem:
      total: 0.48
      efficiency: 0.58
      win: 0.41
      pick: 0.0
      fit: 0.62
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Chronos' Pendant
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Chronos' Pendant
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
    this god: Amanita Charm, Soul Gem, Freya''s Tears, Shield of the Phoenix, Gluttonous
    Grimoire, Blood-Bound Book, Kinetic Cuirass, Ethereal Staff, Genji''s Guard, Phoenix
    Feather, Bancroft''s Talon, Yogi''s Necklace, Breastplate of Valor, Draconic Scale,
    Chandra''s Grace, Oni Hunter''s Garb, Helm of Radiance, Sphere of Negation, Erosion,
    Helm of Darkness, Eye of Providence, Spear of the Magus, Shifter''s Shield, Ancient
    Signet, Jade Scepter, Regrowth Striders.'
  slot_scores:
    Chronos' Pendant:
      total: 0.48
      efficiency: 0.56
      win: 0.52
      pick: 0.15
      fit: 0.29
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.61
      win: 0.41
      pick: 0.0
      fit: 0.58
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.49
      pick: 0.13
      fit: 0.39
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.82
      win: 0.4
      pick: 0.2
      fit: 0.34
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.41
      pick: 0.0
      fit: 0.78
    Soul Gem:
      total: 0.53
      efficiency: 0.58
      win: 0.41
      pick: 0.0
      fit: 0.92
  community_ordered:
  - Chronos' Pendant
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Chronos' Pendant
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Chronos' Pendant
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Soul Gem, Freya''s Tears, Amanita Charm, Kinetic
    Cuirass, Screeching Gargoyle, Genji''s Guard, Stone of Binding, Spear of the Magus,
    Void Stone, Void Shield, Dreamer''s Idol, Breastplate of Valor, Shield of the
    Phoenix, Blood-Bound Book, Doom Orb, Helm of Radiance, Oni Hunter''s Garb, Draconic
    Scale, The World Stone, Helm of Darkness, Ancient Signet, Erosion, Eye of Providence,
    Polynomicon, Shifter''s Shield.'
  slot_scores:
    Chronos' Pendant:
      total: 0.47
      efficiency: 0.56
      win: 0.52
      pick: 0.15
      fit: 0.24
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.61
      win: 0.41
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.49
      efficiency: 0.61
      win: 0.49
      pick: 0.13
      fit: 0.35
    Spear of Desolation:
      total: 0.49
      efficiency: 0.6
      win: 0.41
      pick: 0.22
      fit: 0.54
    Gluttonous Grimoire:
      total: 0.5
      efficiency: 0.58
      win: 0.41
      pick: 0.0
      fit: 0.75
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.82
      win: 0.4
      pick: 0.2
      fit: 0.46
  community_ordered:
  - Chronos' Pendant
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire,
    Soul Gem, Genji''s Guard, Nimble Ring, Breastplate of Valor, Blood-Bound Book,
    Bragi''s Harp, Shield of the Phoenix, Helm of Radiance, Oni Hunter''s Garb, Ancient
    Signet, Draconic Scale, Death Metal, Polynomicon, Bracer of The Abyss, Spear of
    the Magus, Helm of Darkness, Screeching Gargoyle, Erosion, Midgardian Mail, Eye
    of Providence, Dreamer''s Idol.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.41
      efficiency: 0.52
      win: 0.41
      pick: 0.0
      fit: 0.29
    Nimble Ring:
      total: 0.43
      efficiency: 0.57
      win: 0.41
      pick: 0.0
      fit: 0.35
    Bragi's Harp:
      total: 0.42
      efficiency: 0.47
      win: 0.41
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.48
      efficiency: 0.61
      win: 0.49
      pick: 0.13
      fit: 0.27
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.82
      win: 0.4
      pick: 0.2
      fit: 0.21
    Amanita Charm:
      total: 0.47
      efficiency: 0.68
      win: 0.41
      pick: 0.0
      fit: 0.3
  community_ordered:
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Chronos' Pendant
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Genji''s Guard, Soul
    Gem, Amanita Charm, Breastplate of Valor, Kinetic Cuirass, Shield of the Phoenix,
    Gluttonous Grimoire, Screeching Gargoyle, Gladiator''s Shield, Oni Hunter''s Garb,
    Draconic Scale, Prophetic Cloak, Blood-Bound Book, Helm of Radiance, Erosion,
    Eye of Providence, Gem of Focus, Heartwood Charm, Midgardian Mail, Shifter''s
    Shield, Chandra''s Grace, Ancient Signet, Helm of Darkness, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.71
      win: 0.38
      pick: 0.12
      fit: 0.41
    Chronos' Pendant:
      total: 0.49
      efficiency: 0.56
      win: 0.52
      pick: 0.15
      fit: 0.37
    Spear of Desolation:
      total: 0.48
      efficiency: 0.6
      win: 0.41
      pick: 0.22
      fit: 0.48
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.49
      pick: 0.13
      fit: 0.54
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.82
      win: 0.4
      pick: 0.2
      fit: 0.2
    Soul Gem:
      total: 0.49
      efficiency: 0.58
      win: 0.41
      pick: 0.0
      fit: 0.65
  community_ordered:
  - Genji's Guard
  - Chronos' Pendant
  - Spear of Desolation
  - Freya's Tears
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
    Underrated for this god: Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass,
    Soul Gem, Genji''s Guard, Freya''s Tears, Breastplate of Valor, Shield of the
    Phoenix, Draconic Scale, Helm of Radiance, Blood-Bound Book, Helm of Darkness,
    Oni Hunter''s Garb, Erosion, Eye of Providence, Spear of the Magus, Shifter''s
    Shield, Ancient Signet, Midgardian Mail, Dreamer''s Idol, Polynomicon, Jade Scepter,
    Screeching Gargoyle, Stone of Binding, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.47
      efficiency: 0.71
      win: 0.38
      pick: 0.12
      fit: 0.26
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.61
      win: 0.41
      pick: 0.0
      fit: 0.58
    Spear of Desolation:
      total: 0.47
      efficiency: 0.6
      win: 0.41
      pick: 0.22
      fit: 0.44
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.49
      pick: 0.13
      fit: 0.43
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.82
      win: 0.4
      pick: 0.2
      fit: 0.34
    Amanita Charm:
      total: 0.49
      efficiency: 0.68
      win: 0.41
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Genji's Guard
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
community_aspects:
  source: SmiteBrain per-match feed, obsidian+ (data/Analysis/aspect_matches)
  complete_from: '2026-10-20'
  minimum_matches: 30
  window_rule: the newest patch window, or the last closed one when the newest holds
    fewer than minimum_matches of the aspect's matches
  aspects:
  - aspect: Aspect of Silent Night
    status: shown
    window: ob47
    window_rule: newest
    window_start: '2026-11-03'
    window_end: '2026-11-08'
    matches: 126
    wins: 55
    win_share: 0.44
    aggregate:
      aspect_matches: 167
      aspect_win_rate: 0.419
      no_aspect_matches: 595
      no_aspect_win_rate: 0.434
    roles:
    - role: Support
      matches: 123
      share: 0.98
    - role: Carry
      matches: 2
      share: 0.02
    - role: Solo
      matches: 1
      share: 0.01
    base_role: Mid Support
    base_role_share: 0.98
    role_shift: null
    items:
    - name: Freya's Tears
      share: 0.63
    - name: Genji's Guard
      share: 0.55
    - name: Gauntlet of Thebes
      share: 0.44
    - name: Shell of Rebuke
      share: 0.44
    - name: Breastplate of Valor
      share: 0.37
    - name: Stampede
      share: 0.37
    - name: Chandra's Grace
      share: 0.21
    - name: Stone of Binding
      share: 0.2
    starters:
    - name: Heroism
      share: 0.25
    - name: Selflessness
      share: 0.19
    - name: War Flag
      share: 0.19
    relics:
    - name: phantom-shell
      share: 0.53
    - name: purification-beads
      share: 0.16
    - name: aegis-of-acceleration
      share: 0.14
    matches_by_window:
      ob47: 126
    unmapped_slugs:
    - aegis-of-acceleration
    - brawlers-ruin
    - phantom-shell
    - purification-beads
    - sundering-arc
---

---
type: smite-build
god: Hades
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.29
    win_rate: 0.46
    alternates:
    - name: The World Stone
      pick_rate: 0.13
      win_rate: 0.57
    - name: Book of Thoth
      pick_rate: 0.12
      win_rate: 0.68
  - name: The World Stone
    pick_rate: 0.29
    win_rate: 0.52
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.16
      win_rate: 0.59
    - name: Chronos' Pendant
      pick_rate: 0.07
      win_rate: 0.38
  - name: Rod of Tahuti
    pick_rate: 0.21
    win_rate: 0.58
    alternates:
    - name: The World Stone
      pick_rate: 0.12
      win_rate: 0.41
    - name: Spear of Desolation
      pick_rate: 0.09
      win_rate: 0.61
  - name: Blinking Abyss
    pick_rate: 0.08
    win_rate: 0.45
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.29
      win_rate: 0.51
    - name: The World Stone
      pick_rate: 0.07
      win_rate: 0.63
  - name: Obsidian Shard
    pick_rate: 0.09
    win_rate: 0.59
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.12
      win_rate: 0.48
    - name: Blinking Abyss
      pick_rate: 0.08
      win_rate: 0.52
  - name: Killing Stone
    pick_rate: 0.12
    win_rate: 0.76
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.57
    - name: Obsidian Shard
      pick_rate: 0.08
      win_rate: 0.46
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.43
    win_rate: 0.6
  - name: Conduit Gem
    pick_rate: 0.28
    win_rate: 0.5
  - name: Pendulum of the Ages
    pick_rate: 0.07
    win_rate: 0.65
  source_url: https://smitebrain.com/gods/hades/
  last_verified: '2026-11-04'
  god_win_rate: 0.5801282051282052
  god_matches_won: 181
  god_matches_played: 312
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
  - Book of Thoth
  - Genji's Guard
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Rod of Tahuti
  - Obsidian Shard
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Soul Gem, Amanita Charm, Kinetic Cuirass, Genji''s
    Guard, Lotus Sickle, Blood-Bound Book, Freya''s Tears, Spear of the Magus, Breastplate
    of Valor, Shield of the Phoenix, Helm of Radiance, Dreamer''s Idol, Ancient Signet,
    Oni Hunter''s Garb, Jade Scepter, Polynomicon, Helm of Darkness, Doom Orb, Draconic
    Scale, Ethereal Staff, Erosion, Bancroft''s Talon, Screeching Gargoyle, Midgardian
    Mail, Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.48
      win: 0.68
      pick: 0.12
      fit: 0.22
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.55
      pick: 0.0
      fit: 0.22
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.55
      pick: 0.0
      fit: 0.46
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.78
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.58
      pick: 0.33
      fit: 0.42
    Obsidian Shard:
      total: 0.54
      efficiency: 0.53
      win: 0.59
      pick: 0.19
      fit: 0.52
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Obsidian Shard
  - Rod of Tahuti
  - Lotus Sickle
  - Soul Gem
  flex_slots:
  - Book of Thoth
  - Lotus Sickle
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Gluttonous Grimoire, Genji''s Guard, Amanita Charm, Lotus Sickle, Kinetic
    Cuirass, Breastplate of Valor, Death Metal, Ancient Signet, Blood-Bound Book,
    Polynomicon, Freya''s Tears, Spear of the Magus, Helm of Radiance, Oni Hunter''s
    Garb, Shield of the Phoenix, Doom Orb, Dreamer''s Idol, Bancroft''s Talon, Triton''s
    Conch, Jade Scepter, Heartwood Charm, Soul Reaver, Bragi''s Harp, Helm of Darkness,
    Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.48
      win: 0.68
      pick: 0.12
      fit: 0.27
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.55
      pick: 0.0
      fit: 0.24
    Obsidian Shard:
      total: 0.53
      efficiency: 0.53
      win: 0.59
      pick: 0.19
      fit: 0.42
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.58
      pick: 0.33
      fit: 0.39
    Lotus Sickle:
      total: 0.52
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.47
    Soul Gem:
      total: 0.54
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.59
  community_ordered:
  - Book of Thoth
  - Obsidian Shard
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Kinetic Cuirass
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Gluttonous Grimoire, Genji''s Guard, Amanita Charm, Kinetic Cuirass,
    Lotus Sickle, Freya''s Tears, Breastplate of Valor, Spear of the Magus, Shield
    of the Phoenix, Blood-Bound Book, Dreamer''s Idol, Death Metal, Ancient Signet,
    Helm of Radiance, Doom Orb, Oni Hunter''s Garb, Screeching Gargoyle, Polynomicon,
    Jade Scepter, Draconic Scale, Gem of Focus, Heartwood Charm, Helm of Darkness,
    Midgardian Mail, Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.48
      win: 0.68
      pick: 0.12
      fit: 0.15
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.55
      pick: 0.0
      fit: 0.22
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.61
      win: 0.55
      pick: 0.0
      fit: 0.35
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.58
      pick: 0.33
      fit: 0.37
    Obsidian Shard:
      total: 0.53
      efficiency: 0.53
      win: 0.59
      pick: 0.19
      fit: 0.47
    Soul Gem:
      total: 0.56
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Kinetic Cuirass
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Book of Thoth
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
    this god: Amanita Charm, Soul Gem, Gluttonous Grimoire, Shield of the Phoenix,
    Blood-Bound Book, Kinetic Cuirass, Genji''s Guard, Ethereal Staff, Phoenix Feather,
    Bancroft''s Talon, Freya''s Tears, Yogi''s Necklace, Rod of Asclepius, Soul Locket,
    Breastplate of Valor, Lotus Sickle, Chandra''s Grace, Draconic Scale, Oni Hunter''s
    Garb, Helm of Radiance, Sphere of Negation, Erosion, Spear of the Magus, Helm
    of Darkness, Eye of Providence, Shifter''s Shield, Ancient Signet.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.48
      win: 0.68
      pick: 0.12
      fit: 0.19
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.55
      pick: 0.0
      fit: 0.24
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.61
      win: 0.55
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.58
      pick: 0.33
      fit: 0.35
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.76
    Soul Gem:
      total: 0.59
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.94
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Spear of Desolation
  - Gluttonous Grimoire
  - Rod of Tahuti
  - Obsidian Shard
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Soul Gem, Amanita Charm, Genji''s Guard, Spear
    of the Magus, Kinetic Cuirass, Screeching Gargoyle, Dreamer''s Idol, Stone of
    Binding, Doom Orb, Lotus Sickle, Void Stone, Blood-Bound Book, Void Shield, Freya''s
    Tears, Breastplate of Valor, Shield of the Phoenix, Helm of Radiance, Ancient
    Signet, Oni Hunter''s Garb, Polynomicon, The Cosmic Horror, Jade Scepter, Helm
    of Darkness, Draconic Scale, Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.48
      win: 0.68
      pick: 0.12
      fit: 0.18
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.55
      pick: 0.0
      fit: 0.18
    Spear of Desolation:
      total: 0.53
      efficiency: 0.6
      win: 0.46
      pick: 0.29
      fit: 0.62
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.84
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.58
      pick: 0.33
      fit: 0.53
    Obsidian Shard:
      total: 0.56
      efficiency: 0.53
      win: 0.59
      pick: 0.19
      fit: 0.63
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Book of Thoth
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
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
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Soul Gem, Amanita Charm, Genji''s Guard, Kinetic
    Cuirass, Nimble Ring, Lotus Sickle, Bragi''s Harp, Blood-Bound Book, Breastplate
    of Valor, Freya''s Tears, Eros'' Bow, Ancient Signet, Spear of the Magus, Helm
    of Radiance, Death Metal, Shield of the Phoenix, Bracer of The Abyss, Polynomicon,
    Oni Hunter''s Garb, Dreamer''s Idol, Jade Scepter, Screeching Gargoyle, Draconic
    Scale, Midgardian Mail, Doom Orb, Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.48
      win: 0.68
      pick: 0.12
      fit: 0.13
    Nimble Ring:
      total: 0.5
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.38
    Bragi's Harp:
      total: 0.49
      efficiency: 0.47
      win: 0.55
      pick: 0.0
      fit: 0.52
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.58
      pick: 0.33
      fit: 0.25
    Eros' Bow:
      total: 0.49
      efficiency: 0.5
      win: 0.55
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Book of Thoth
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Genji''s Guard, Freya''s
    Tears, Gluttonous Grimoire, Breastplate of Valor, Amanita Charm, Lotus Sickle,
    Shield of the Phoenix, Kinetic Cuirass, Screeching Gargoyle, Gladiator''s Shield,
    Blood-Bound Book, Gem of Focus, Heartwood Charm, Oni Hunter''s Garb, Chandra''s
    Grace, Spear of the Magus, Ancient Signet, Helm of Radiance, Prophetic Cloak,
    Eye of Erebus, Draconic Scale, Death Metal, Damaru, Dreamer''s Idol, Polynomicon,
    Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.48
      win: 0.68
      pick: 0.12
      fit: 0.09
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.55
      pick: 0.0
      fit: 0.39
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.39
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.55
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.58
      pick: 0.33
      fit: 0.24
    Soul Gem:
      total: 0.56
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.74
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Spear of Desolation
  - Kinetic Cuirass
  - Gluttonous Grimoire
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Soul Gem, Amanita Charm, Kinetic
    Cuirass, Genji''s Guard, Lotus Sickle, Blood-Bound Book, Freya''s Tears, Spear
    of the Magus, Breastplate of Valor, Shield of the Phoenix, Helm of Radiance, Dreamer''s
    Idol, Ancient Signet, Chronos'' Pendant, Oni Hunter''s Garb, Jade Scepter, Polynomicon,
    Helm of Darkness, Doom Orb, Draconic Scale, Ethereal Staff, Erosion, Bancroft''s
    Talon, Screeching Gargoyle, Midgardian Mail.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.48
      win: 0.68
      pick: 0.12
      fit: 0.22
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.55
      pick: 0.0
      fit: 0.22
    Spear of Desolation:
      total: 0.51
      efficiency: 0.6
      win: 0.46
      pick: 0.29
      fit: 0.53
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.55
      pick: 0.0
      fit: 0.46
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.78
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.58
      pick: 0.33
      fit: 0.42
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
---

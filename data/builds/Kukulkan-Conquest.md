---
type: smite-build
god: Kukulkan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Squall
  aspect_pick_rate: 0.16
  aspect_win_rate: 0.68
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.88
    win_rate: 0.59
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.04
      win_rate: 0.78
    - name: Jade Scepter
      pick_rate: 0.02
      win_rate: 0.5
  - name: Spear of Desolation
    pick_rate: 0.31
    win_rate: 0.62
    alternates:
    - name: Polynomicon
      pick_rate: 0.07
      win_rate: 0.6
    - name: Soul Gem
      pick_rate: 0.07
      win_rate: 0.67
  - name: Rod of Tahuti
    pick_rate: 0.16
    win_rate: 0.53
    alternates:
    - name: Polynomicon
      pick_rate: 0.13
      win_rate: 0.67
    - name: Spear of Desolation
      pick_rate: 0.08
      win_rate: 0.63
  - name: Obsidian Shard
    pick_rate: 0.12
    win_rate: 0.56
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.32
      win_rate: 0.59
    - name: Polynomicon
      pick_rate: 0.05
      win_rate: 0.73
  - name: Soul Reaver
    pick_rate: 0.06
    win_rate: 0.55
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.19
      win_rate: 0.66
    - name: Rod of Tahuti
      pick_rate: 0.13
      win_rate: 0.56
  - name: Evil Eye
    pick_rate: 0.08
    win_rate: 0.55
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.57
    - name: Oracle Staff
      pick_rate: 0.07
      win_rate: 0.44
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.41
    win_rate: 0.56
  - name: Conduit Gem
    pick_rate: 0.28
    win_rate: 0.56
  - name: Pendulum of the Ages
    pick_rate: 0.15
    win_rate: 0.58
  source_url: https://smitebrain.com/gods/kukulkan/
  last_verified: '2026-09-12'
  god_win_rate: 0.5876777251184834
  god_matches_won: 124
  god_matches_played: 211
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-12'
  god_matches_analyzed: 4284
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom Orb, The World
    Stone, Dreamer''s Idol, Chronos'' Pendant, The Cosmic Horror, Gem of Focus, Ancient
    Signet, Totem of Death, Rod of Asclepius, Soul Reaver, Blood-Bound Book, Divine
    Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin, Wish-Granting
    Pearl, Typhon’s Heart, Jade Scepter, Bracer of The Abyss, Nimble Ring.'
  slot_scores:
    Book of Thoth:
      total: 0.55
      efficiency: 0.51
      win: 0.59
      pick: 0.88
      fit: 0.42
    Spear of Desolation:
      total: 0.65
      efficiency: 0.57
      win: 0.62
      pick: 0.42
      fit: 1.0
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.53
      pick: 0.25
      fit: 0.79
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.56
      pick: 0.2
      fit: 0.89
    Soul Gem:
      total: 0.64
      efficiency: 0.52
      win: 0.67
      pick: 0.1
      fit: 1.0
  community_ordered:
  - Book of Thoth
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
  - Polynomicon
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Polynomicon
  - Obsidian Shard
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
    Gem, Spear of the Magus, Doom Orb, The World Stone, Death Metal, Gluttonous Grimoire,
    Ancient Signet, Chronos'' Pendant, Dreamer''s Idol, Bragi''s Harp, Gem of Focus,
    Soul Reaver, The Cosmic Horror, Rod of Asclepius, Bancroft''s Talon, Totem of
    Death, Triton''s Conch, Blood-Bound Book, Divine Ruin, Wish-Granting Pearl, Helm
    of Radiance, Breastplate of Valor, Ethereal Staff, Jade Scepter.'
  slot_scores:
    Book of Thoth:
      total: 0.55
      efficiency: 0.51
      win: 0.59
      pick: 0.88
      fit: 0.39
    Polynomicon:
      total: 0.54
      efficiency: 0.46
      win: 0.67
      pick: 0.2
      fit: 0.49
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.62
      pick: 0.42
      fit: 0.61
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.53
      pick: 0.25
      fit: 0.57
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.56
      pick: 0.2
      fit: 0.57
    Soul Gem:
      total: 0.59
      efficiency: 0.52
      win: 0.67
      pick: 0.1
      fit: 0.71
  community_ordered:
  - Book of Thoth
  - Polynomicon
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
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
    god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom Orb, The World Stone,
    Dreamer''s Idol, Chronos'' Pendant, Death Metal, Gem of Focus, The Cosmic Horror,
    Ancient Signet, Bragi''s Harp, Totem of Death, Rod of Asclepius, Soul Reaver,
    Blood-Bound Book, Divine Ruin, Triton''s Conch, Breastplate of Valor, Bancroft''s
    Talon, Genji''s Guard, Helm of Radiance, Ethereal Staff, Jade Scepter.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.51
      win: 0.59
      pick: 0.88
      fit: 0.22
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.62
      pick: 0.42
      fit: 0.78
    Spear of the Magus:
      total: 0.54
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.53
      pick: 0.25
      fit: 0.56
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.56
      pick: 0.2
      fit: 0.66
    Soul Gem:
      total: 0.62
      efficiency: 0.52
      win: 0.67
      pick: 0.1
      fit: 0.88
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Kinetic Cuirass
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Amanita Charm, Rod of Asclepius, Shield of the Phoenix, Gluttonous
    Grimoire, Kinetic Cuirass, Ethereal Staff, Freya''s Tears, Spear of the Magus,
    Shifter''s Shield, Genji''s Guard, Breastplate of Valor, Lifebinder, Helm of Radiance,
    Sphere of Negation, Erosion, Yogi''s Necklace, Eye of Providence, Draconic Scale,
    Phoenix Feather, Chandra''s Grace, Wish-Granting Pearl, Blood-Bound Book, Doom
    Orb, Glorious Pridwen, Jade Scepter.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.51
      win: 0.59
      pick: 0.88
      fit: 0.21
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.62
      pick: 0.42
      fit: 0.49
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.53
      pick: 0.25
      fit: 0.39
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.62
      efficiency: 0.52
      win: 0.67
      pick: 0.1
      fit: 0.89
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of the Magus
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
    for this god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom Orb, The
    World Stone, Dreamer''s Idol, The Cosmic Horror, Chronos'' Pendant, Ancient Signet,
    Gem of Focus, Rod of Asclepius, Totem of Death, Soul Reaver, Blood-Bound Book,
    Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Screeching Gargoyle,
    Wish-Granting Pearl, Typhon’s Heart, Jade Scepter, Breastplate of Valor, Bracer
    of The Abyss.'
  slot_scores:
    Book of Thoth:
      total: 0.53
      efficiency: 0.51
      win: 0.59
      pick: 0.88
      fit: 0.3
    Spear of Desolation:
      total: 0.65
      efficiency: 0.57
      win: 0.62
      pick: 0.42
      fit: 1.0
    Spear of the Magus:
      total: 0.59
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.53
      pick: 0.25
      fit: 0.85
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.56
      pick: 0.2
      fit: 0.95
    Soul Gem:
      total: 0.64
      efficiency: 0.52
      win: 0.67
      pick: 0.1
      fit: 1.0
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
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
    this god: Soul Gem, Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Bragi''s
    Harp, Bracer of The Abyss, Doom Orb, Chronos'' Pendant, The World Stone, Ancient
    Signet, Blood-Bound Book, Dreamer''s Idol, Death Metal, Bancroft''s Talon, Gem
    of Focus, Rod of Asclepius, The Cosmic Horror, Typhon’s Heart, Soul Reaver, Totem
    of Death, Divine Ruin, Helm of Radiance, Daybreak Gavel, Jade Scepter.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.62
      pick: 0.42
      fit: 0.4
    Bragi's Harp:
      total: 0.5
      efficiency: 0.44
      win: 0.56
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.53
      pick: 0.25
      fit: 0.32
    Soul Gem:
      total: 0.59
      efficiency: 0.57
      win: 0.67
      pick: 0.1
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
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
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
    + fit + win/pick). Underrated for this god: Soul Gem, Chronos'' Pendant, Gem of
    Focus, Spear of the Magus, Gluttonous Grimoire, Totem of Death, Doom Orb, The
    World Stone, Breastplate of Valor, Dreamer''s Idol, Genji''s Guard, Ancient Signet,
    Death Metal, Staff of Myrddin, The Cosmic Horror, Eye of Erebus, Screeching Gargoyle,
    Bragi''s Harp, Rod of Asclepius, Chandra''s Grace, Freya''s Tears, Soul Reaver,
    Blood-Bound Book, Jade Scepter.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.51
      win: 0.59
      pick: 0.88
      fit: 0.14
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.62
      pick: 0.42
      fit: 0.86
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.53
      pick: 0.25
      fit: 0.37
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.56
      pick: 0.2
      fit: 0.47
    Soul Gem:
      total: 0.63
      efficiency: 0.52
      win: 0.67
      pick: 0.1
      fit: 0.96
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
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
    Underrated for this god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom
    Orb, The World Stone, Dreamer''s Idol, Chronos'' Pendant, The Cosmic Horror, Gem
    of Focus, Ancient Signet, Totem of Death, Rod of Asclepius, Blood-Bound Book,
    Soul Reaver, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal
    Staff, Staff of Myrddin, Wish-Granting Pearl, Typhon’s Heart, Bracer of The Abyss,
    Nimble Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.65
      efficiency: 0.57
      win: 0.62
      pick: 0.42
      fit: 1.0
    Doom Orb:
      total: 0.55
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.53
      pick: 0.25
      fit: 0.79
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.56
      pick: 0.2
      fit: 0.89
    Soul Gem:
      total: 0.64
      efficiency: 0.52
      win: 0.67
      pick: 0.1
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
---

---
type: smite-build
god: Kukulkan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Squall
  aspect_pick_rate: 0.23
  aspect_win_rate: 0.55
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.84
    win_rate: 0.57
    alternates:
    - name: Yogi's Necklace
      pick_rate: 0.05
      win_rate: 0.55
    - name: Jade Scepter
      pick_rate: 0.04
      win_rate: 0.88
  - name: Chronos' Pendant
    pick_rate: 0.29
    win_rate: 0.56
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.18
      win_rate: 0.54
    - name: Book of Thoth
      pick_rate: 0.08
      win_rate: 0.5
  - name: Rod of Tahuti
    pick_rate: 0.17
    win_rate: 0.67
    alternates:
    - name: Soul Gem
      pick_rate: 0.12
      win_rate: 0.46
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.5
  - name: Obsidian Shard
    pick_rate: 0.16
    win_rate: 0.42
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.29
      win_rate: 0.59
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.45
  - name: Spear of the Magus
    pick_rate: 0.04
    win_rate: 1.0
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.24
      win_rate: 0.56
    - name: Obsidian Shard
      pick_rate: 0.2
      win_rate: 0.58
  - name: Evil Eye
    pick_rate: 0.09
    win_rate: 0.4
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.12
      win_rate: 0.57
    - name: Blinking Abyss
      pick_rate: 0.07
      win_rate: 0.75
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.52
    win_rate: 0.56
  - name: Conduit Gem
    pick_rate: 0.2
    win_rate: 0.48
  - name: Pendulum of the Ages
    pick_rate: 0.13
    win_rate: 0.74
  source_url: https://smitebrain.com/gods/kukulkan/
  last_verified: '2026-09-25'
  god_win_rate: 0.5728155339805825
  god_matches_won: 118
  god_matches_played: 206
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-25'
  god_matches_analyzed: 2996
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Nimble Ring
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Jade Scepter
  flex_slots:
  - Book of Thoth
  - Nimble Ring
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Spear of the Magus, Jade Scepter, Gluttonous Grimoire, Doom Orb, The
    World Stone, Dreamer''s Idol, The Cosmic Horror, Gem of Focus, Ancient Signet,
    Totem of Death, Rod of Asclepius, Polynomicon, Blood-Bound Book, Soul Reaver,
    Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin,
    Wish-Granting Pearl, Typhon’s Heart, Bracer of The Abyss, Nimble Ring.'
  slot_scores:
    Book of Thoth:
      total: 0.54
      efficiency: 0.51
      win: 0.57
      pick: 0.84
      fit: 0.42
    Nimble Ring:
      total: 0.45
      efficiency: 0.39
      win: 0.55
      pick: 0.0
      fit: 0.42
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.54
      pick: 0.25
      fit: 1.0
    Spear of the Magus:
      total: 0.78
      efficiency: 0.6
      win: 1.0
      pick: 0.09
      fit: 0.79
    Rod of Tahuti:
      total: 0.73
      efficiency: 0.86
      win: 0.67
      pick: 0.26
      fit: 0.79
    Jade Scepter:
      total: 0.63
      efficiency: 0.48
      win: 0.88
      pick: 0.04
      fit: 0.42
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Jade Scepter
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
  - Jade Scepter
  flex_slots:
  - Book of Thoth
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Spear
    of the Magus, Jade Scepter, Doom Orb, The World Stone, Death Metal, Gluttonous
    Grimoire, Ancient Signet, Dreamer''s Idol, Bragi''s Harp, Gem of Focus, Polynomicon,
    Soul Reaver, The Cosmic Horror, Rod of Asclepius, Bancroft''s Talon, Totem of
    Death, Triton''s Conch, Blood-Bound Book, Divine Ruin, Wish-Granting Pearl, Helm
    of Radiance, Ethereal Staff, Breastplate of Valor.'
  slot_scores:
    Book of Thoth:
      total: 0.53
      efficiency: 0.51
      win: 0.57
      pick: 0.84
      fit: 0.39
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.54
      pick: 0.25
      fit: 0.61
    Doom Orb:
      total: 0.52
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.57
    Spear of the Magus:
      total: 0.74
      efficiency: 0.6
      win: 1.0
      pick: 0.09
      fit: 0.47
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.67
      pick: 0.26
      fit: 0.57
    Jade Scepter:
      total: 0.61
      efficiency: 0.48
      win: 0.88
      pick: 0.04
      fit: 0.29
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Jade Scepter
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Nimble Ring
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Jade Scepter
  flex_slots:
  - Book of Thoth
  - Nimble Ring
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Spear of the Magus, Jade Scepter, Gluttonous Grimoire, Doom Orb, The World
    Stone, Dreamer''s Idol, Death Metal, Gem of Focus, The Cosmic Horror, Ancient
    Signet, Bragi''s Harp, Totem of Death, Rod of Asclepius, Polynomicon, Blood-Bound
    Book, Soul Reaver, Divine Ruin, Triton''s Conch, Bancroft''s Talon, Helm of Radiance,
    Ethereal Staff, Breastplate of Valor, Genji''s Guard.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.51
      win: 0.57
      pick: 0.84
      fit: 0.22
    Nimble Ring:
      total: 0.42
      efficiency: 0.39
      win: 0.55
      pick: 0.0
      fit: 0.22
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.54
      pick: 0.25
      fit: 0.78
    Spear of the Magus:
      total: 0.75
      efficiency: 0.6
      win: 1.0
      pick: 0.09
      fit: 0.56
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.67
      pick: 0.26
      fit: 0.56
    Jade Scepter:
      total: 0.6
      efficiency: 0.48
      win: 0.88
      pick: 0.04
      fit: 0.22
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Jade Scepter
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Spear of the Magus
  - Jade Scepter
  - Rod of Tahuti
  - Amanita Charm
  - Rod of Asclepius
  flex_slots:
  - Rod of Asclepius
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    this god: Spear of the Magus, Jade Scepter, Amanita Charm, Rod of Asclepius, Shield
    of the Phoenix, Gluttonous Grimoire, Kinetic Cuirass, Ethereal Staff, Freya''s
    Tears, Shifter''s Shield, Lifebinder, Helm of Radiance, Yogi''s Necklace, Sphere
    of Negation, Erosion, Eye of Providence, Breastplate of Valor, Draconic Scale,
    Phoenix Feather, Chandra''s Grace, Wish-Granting Pearl, Blood-Bound Book, Doom
    Orb, Glorious Pridwen, Genji''s Guard.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.51
      win: 0.57
      pick: 0.84
      fit: 0.21
    Spear of the Magus:
      total: 0.72
      efficiency: 0.6
      win: 1.0
      pick: 0.09
      fit: 0.39
    Jade Scepter:
      total: 0.65
      efficiency: 0.54
      win: 0.88
      pick: 0.04
      fit: 0.4
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.67
      pick: 0.26
      fit: 0.39
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.81
    Rod of Asclepius:
      total: 0.55
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Book of Thoth
  - Spear of the Magus
  - Jade Scepter
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Gluttonous Grimoire
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
  - Jade Scepter
  flex_slots:
  - Gluttonous Grimoire
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
    for this god: Spear of the Magus, Jade Scepter, Gluttonous Grimoire, Doom Orb,
    The World Stone, Dreamer''s Idol, The Cosmic Horror, Ancient Signet, Gem of Focus,
    Rod of Asclepius, Totem of Death, Polynomicon, Blood-Bound Book, Soul Reaver,
    Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Screeching Gargoyle,
    Wish-Granting Pearl, Typhon’s Heart, Bracer of The Abyss, Breastplate of Valor.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.95
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.54
      pick: 0.25
      fit: 1.0
    Doom Orb:
      total: 0.56
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.79
      efficiency: 0.6
      win: 1.0
      pick: 0.09
      fit: 0.85
    Rod of Tahuti:
      total: 0.74
      efficiency: 0.86
      win: 0.67
      pick: 0.26
      fit: 0.85
    Jade Scepter:
      total: 0.61
      efficiency: 0.48
      win: 0.88
      pick: 0.04
      fit: 0.3
  community_ordered:
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Jade Scepter
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Spear of the Magus
  - Rod of Tahuti
  - Jade Scepter
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Spear of the Magus, Jade Scepter, Nimble Ring, Gluttonous Grimoire,
    Bragi''s Harp, Bracer of The Abyss, Doom Orb, The World Stone, Ancient Signet,
    Blood-Bound Book, Dreamer''s Idol, Death Metal, Bancroft''s Talon, Gem of Focus,
    Rod of Asclepius, The Cosmic Horror, Typhon’s Heart, Polynomicon, Soul Reaver,
    Totem of Death, Divine Ruin, Helm of Radiance, Daybreak Gavel.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.5
      efficiency: 0.44
      win: 0.55
      pick: 0.0
      fit: 0.63
    Spear of the Magus:
      total: 0.71
      efficiency: 0.6
      win: 1.0
      pick: 0.09
      fit: 0.32
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.67
      pick: 0.26
      fit: 0.32
    Jade Scepter:
      total: 0.59
      efficiency: 0.48
      win: 0.88
      pick: 0.04
      fit: 0.17
  community_ordered:
  - Spear of the Magus
  - Rod of Tahuti
  - Jade Scepter
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Spear of the Magus
  - Jade Scepter
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Chronos' Pendant
  - Soul Gem
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Spear of the Magus, Jade Scepter,
    Gem of Focus, Gluttonous Grimoire, Totem of Death, Doom Orb, The World Stone,
    Dreamer''s Idol, Ancient Signet, Death Metal, Breastplate of Valor, Staff of Myrddin,
    The Cosmic Horror, Eye of Erebus, Screeching Gargoyle, Bragi''s Harp, Rod of Asclepius,
    Chandra''s Grace, Freya''s Tears, Polynomicon, Genji''s Guard, Blood-Bound Book,
    Soul Reaver.'
  slot_scores:
    Chronos' Pendant:
      total: 0.56
      efficiency: 0.55
      win: 0.56
      pick: 0.4
      fit: 0.63
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.54
      pick: 0.25
      fit: 0.86
    Spear of the Magus:
      total: 0.72
      efficiency: 0.6
      win: 1.0
      pick: 0.09
      fit: 0.37
    Jade Scepter:
      total: 0.59
      efficiency: 0.48
      win: 0.88
      pick: 0.04
      fit: 0.14
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.67
      pick: 0.26
      fit: 0.37
    Soul Gem:
      total: 0.54
      efficiency: 0.52
      win: 0.46
      pick: 0.19
      fit: 0.96
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Spear of the Magus
  - Jade Scepter
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
    Underrated for this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, The
    World Stone, Dreamer''s Idol, The Cosmic Horror, Gem of Focus, Ancient Signet,
    Totem of Death, Rod of Asclepius, Polynomicon, Blood-Bound Book, Soul Reaver,
    Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff,
    Staff of Myrddin, Wish-Granting Pearl, Typhon’s Heart, Bracer of The Abyss, Nimble
    Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.54
      pick: 0.25
      fit: 1.0
    Doom Orb:
      total: 0.55
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.78
      efficiency: 0.6
      win: 1.0
      pick: 0.09
      fit: 0.79
    Rod of Tahuti:
      total: 0.73
      efficiency: 0.86
      win: 0.67
      pick: 0.26
      fit: 0.79
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.42
      pick: 0.27
      fit: 0.89
    Soul Gem:
      total: 0.55
      efficiency: 0.52
      win: 0.46
      pick: 0.19
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
---

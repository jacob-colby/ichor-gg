---
type: smite-build
god: Scylla
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Devourer
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.6
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.45
    win_rate: 0.45
    alternates:
    - name: Book of Thoth
      pick_rate: 0.24
      win_rate: 0.67
    - name: Doom Orb
      pick_rate: 0.1
      win_rate: 0.6
  - name: Book of Thoth
    pick_rate: 0.22
    win_rate: 0.55
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.24
      win_rate: 0.67
    - name: Soul Gem
      pick_rate: 0.1
      win_rate: 0.2
  - name: Polynomicon
    pick_rate: 0.3
    win_rate: 0.64
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.21
      win_rate: 0.4
    - name: Chronos' Pendant
      pick_rate: 0.06
      win_rate: 0.67
  - name: Rod of Tahuti
    pick_rate: 0.33
    win_rate: 0.47
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.26
      win_rate: 0.42
    - name: Polynomicon
      pick_rate: 0.09
      win_rate: 0.75
  - name: Obsidian Shard
    pick_rate: 0.16
    win_rate: 0.5
    alternates:
    - name: Evil Eye
      pick_rate: 0.13
      win_rate: 0.8
    - name: Rod of Tahuti
      pick_rate: 0.13
      win_rate: 0.6
  - name: Void Shard
    pick_rate: 0.11
    win_rate: 0.33
    alternates:
    - name: Killing Stone
      pick_rate: 0.07
      win_rate: 0.0
    - name: Obsidian Shard
      pick_rate: 0.07
      win_rate: 1.0
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.49
    win_rate: 0.5
  - name: Conduit Gem
    pick_rate: 0.33
    win_rate: 0.56
  - name: Pendulum of the Ages
    pick_rate: 0.06
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/scylla/
  last_verified: '2026-09-09'
  god_win_rate: 0.5510204081632653
  god_matches_won: 27
  god_matches_played: 49
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-09'
  god_matches_analyzed: 921
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Chronos' Pendant
  - Doom Orb
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Chronos'' Pendant, Doom Orb, Spear of the Magus, Gluttonous Grimoire,
    The World Stone, Dreamer''s Idol, The Cosmic Horror, Gem of Focus, Ancient Signet,
    Totem of Death, Rod of Asclepius, Blood-Bound Book, Soul Reaver, Jade Scepter,
    Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin,
    Wish-Granting Pearl, Typhon’s Heart, Bracer of The Abyss, Soul Gem, Nimble Ring.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.55
      pick: 0.3
      fit: 0.42
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.45
      pick: 0.45
      fit: 1.0
    Chronos' Pendant:
      total: 0.59
      efficiency: 0.55
      win: 0.67
      pick: 0.09
      fit: 0.63
    Doom Orb:
      total: 0.58
      efficiency: 0.53
      win: 0.6
      pick: 0.1
      fit: 0.79
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.47
      pick: 0.55
      fit: 0.79
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.5
      pick: 0.35
      fit: 0.89
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Chronos' Pendant
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Chronos' Pendant
  - Polynomicon
  - Doom Orb
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Chronos''
    Pendant, Doom Orb, Spear of the Magus, The World Stone, Death Metal, Gluttonous
    Grimoire, Ancient Signet, Dreamer''s Idol, Bragi''s Harp, Gem of Focus, Soul Reaver,
    The Cosmic Horror, Rod of Asclepius, Bancroft''s Talon, Totem of Death, Triton''s
    Conch, Blood-Bound Book, Jade Scepter, Divine Ruin, Wish-Granting Pearl, Helm
    of Radiance, Breastplate of Valor, Ethereal Staff, Soul Gem.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.55
      pick: 0.3
      fit: 0.39
    Chronos' Pendant:
      total: 0.56
      efficiency: 0.55
      win: 0.67
      pick: 0.09
      fit: 0.43
    Polynomicon:
      total: 0.54
      efficiency: 0.46
      win: 0.64
      pick: 0.47
      fit: 0.49
    Doom Orb:
      total: 0.55
      efficiency: 0.53
      win: 0.6
      pick: 0.1
      fit: 0.57
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.47
      pick: 0.55
      fit: 0.57
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.5
      pick: 0.35
      fit: 0.57
  community_ordered:
  - Book of Thoth
  - Chronos' Pendant
  - Polynomicon
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Chronos' Pendant
  - Doom Orb
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Chronos'' Pendant, Doom Orb, Spear of the Magus, Gluttonous Grimoire, The
    World Stone, Dreamer''s Idol, Death Metal, Gem of Focus, The Cosmic Horror, Ancient
    Signet, Bragi''s Harp, Totem of Death, Rod of Asclepius, Blood-Bound Book, Soul
    Reaver, Jade Scepter, Divine Ruin, Triton''s Conch, Breastplate of Valor, Bancroft''s
    Talon, Genji''s Guard, Helm of Radiance, Ethereal Staff, Soul Gem.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.55
      pick: 0.3
      fit: 0.22
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.45
      pick: 0.45
      fit: 0.78
    Chronos' Pendant:
      total: 0.56
      efficiency: 0.55
      win: 0.67
      pick: 0.09
      fit: 0.44
    Doom Orb:
      total: 0.54
      efficiency: 0.53
      win: 0.6
      pick: 0.1
      fit: 0.56
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.47
      pick: 0.55
      fit: 0.56
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.5
      pick: 0.35
      fit: 0.66
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Chronos' Pendant
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Chronos' Pendant
  - Doom Orb
  - Rod of Tahuti
  - Amanita Charm
  - Rod of Asclepius
  flex_slots:
  - Doom Orb
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
    this god: Amanita Charm, Rod of Asclepius, Shield of the Phoenix, Gluttonous Grimoire,
    Doom Orb, Kinetic Cuirass, Ethereal Staff, Freya''s Tears, Spear of the Magus,
    Shifter''s Shield, Genji''s Guard, Breastplate of Valor, Lifebinder, Helm of Radiance,
    Sphere of Negation, Erosion, Yogi''s Necklace, Eye of Providence, Draconic Scale,
    Phoenix Feather, Jade Scepter, Chandra''s Grace, Wish-Granting Pearl, Blood-Bound
    Book, Glorious Pridwen, Soul Gem.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.55
      pick: 0.3
      fit: 0.21
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.55
      win: 0.67
      pick: 0.09
      fit: 0.31
    Doom Orb:
      total: 0.52
      efficiency: 0.53
      win: 0.6
      pick: 0.1
      fit: 0.39
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.47
      pick: 0.55
      fit: 0.39
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.81
    Rod of Asclepius:
      total: 0.53
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Book of Thoth
  - Chronos' Pendant
  - Doom Orb
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Chronos' Pendant
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
    for this god: Doom Orb, Chronos'' Pendant, Spear of the Magus, Gluttonous Grimoire,
    The World Stone, Dreamer''s Idol, The Cosmic Horror, Ancient Signet, Gem of Focus,
    Rod of Asclepius, Totem of Death, Blood-Bound Book, Soul Reaver, Jade Scepter,
    Divine Ruin, Bancroft''s Talon, Soul Gem, Helm of Radiance, Ethereal Staff, Screeching
    Gargoyle, Wish-Granting Pearl, Typhon’s Heart, Breastplate of Valor, Bracer of
    The Abyss.'
  slot_scores:
    Chronos' Pendant:
      total: 0.56
      efficiency: 0.55
      win: 0.67
      pick: 0.09
      fit: 0.44
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.45
      pick: 0.45
      fit: 1.0
    Doom Orb:
      total: 0.59
      efficiency: 0.53
      win: 0.6
      pick: 0.1
      fit: 0.85
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.47
      pick: 0.55
      fit: 0.85
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.85
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.5
      pick: 0.35
      fit: 0.95
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Book of Thoth
  - Chronos' Pendant
  - Bracer of The Abyss
  - Rod of Tahuti
  - Nimble Ring
  - Bragi's Harp
  flex_slots:
  - Bracer of The Abyss
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Chronos'' Pendant, Nimble Ring, Doom Orb, Gluttonous Grimoire, Spear
    of the Magus, Bragi''s Harp, Bracer of The Abyss, The World Stone, Ancient Signet,
    Blood-Bound Book, Dreamer''s Idol, Death Metal, Bancroft''s Talon, Gem of Focus,
    Rod of Asclepius, The Cosmic Horror, Typhon’s Heart, Soul Reaver, Totem of Death,
    Jade Scepter, Divine Ruin, Helm of Radiance, Daybreak Gavel, Soul Gem.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.55
      pick: 0.3
      fit: 0.17
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.55
      win: 0.67
      pick: 0.09
      fit: 0.25
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.4
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.47
      pick: 0.55
      fit: 0.32
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Book of Thoth
  - Chronos' Pendant
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Chronos' Pendant
  - Gem of Focus
  - Rod of Tahuti
  - Doom Orb
  flex_slots:
  - Gem of Focus
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
    + fit + win/pick). Underrated for this god: Chronos'' Pendant, Doom Orb, Gem of
    Focus, Spear of the Magus, Gluttonous Grimoire, Totem of Death, The World Stone,
    Breastplate of Valor, Dreamer''s Idol, Genji''s Guard, Ancient Signet, Death Metal,
    Staff of Myrddin, The Cosmic Horror, Eye of Erebus, Screeching Gargoyle, Bragi''s
    Harp, Rod of Asclepius, Chandra''s Grace, Freya''s Tears, Soul Gem, Blood-Bound
    Book, Soul Reaver, Jade Scepter.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.51
      win: 0.55
      pick: 0.3
      fit: 0.14
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.45
      pick: 0.45
      fit: 0.86
    Chronos' Pendant:
      total: 0.59
      efficiency: 0.55
      win: 0.67
      pick: 0.09
      fit: 0.63
    Gem of Focus:
      total: 0.49
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.47
      pick: 0.55
      fit: 0.37
    Doom Orb:
      total: 0.52
      efficiency: 0.53
      win: 0.6
      pick: 0.1
      fit: 0.37
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Chronos' Pendant
  - Rod of Tahuti
  - Doom Orb
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
      total: 0.58
      efficiency: 0.57
      win: 0.45
      pick: 0.45
      fit: 1.0
    Doom Orb:
      total: 0.58
      efficiency: 0.53
      win: 0.6
      pick: 0.1
      fit: 0.79
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.47
      pick: 0.55
      fit: 0.79
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.5
      pick: 0.35
      fit: 0.89
    Soul Gem:
      total: 0.43
      efficiency: 0.52
      win: 0.2
      pick: 0.14
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
---

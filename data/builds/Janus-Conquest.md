---
type: smite-build
god: Janus
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.35
    win_rate: 0.53
    alternates:
    - name: Book of Thoth
      pick_rate: 0.3
      win_rate: 0.36
    - name: Chronos' Pendant
      pick_rate: 0.18
      win_rate: 0.35
  - name: Book of Thoth
    pick_rate: 0.34
    win_rate: 0.48
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.27
      win_rate: 0.44
    - name: Doom Orb
      pick_rate: 0.09
      win_rate: 0.25
  - name: Soul Gem
    pick_rate: 0.36
    win_rate: 0.53
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.16
      win_rate: 0.43
    - name: Rod of Tahuti
      pick_rate: 0.13
      win_rate: 0.25
  - name: Rod of Tahuti
    pick_rate: 0.4
    win_rate: 0.56
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.18
      win_rate: 0.5
    - name: Soul Gem
      pick_rate: 0.1
      win_rate: 0.33
  - name: Obsidian Shard
    pick_rate: 0.32
    win_rate: 0.6
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.25
      win_rate: 0.45
    - name: Evil Eye
      pick_rate: 0.1
      win_rate: 0.25
  - name: Killing Stone
    pick_rate: 0.18
    win_rate: 0.67
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.18
      win_rate: 0.44
    - name: Dreamer's Idol
      pick_rate: 0.1
      win_rate: 0.6
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.49
    win_rate: 0.49
  - name: Conduit Gem
    pick_rate: 0.36
    win_rate: 0.27
  - name: Pendulum of the Ages
    pick_rate: 0.11
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/janus/
  last_verified: '2026-09-10'
  god_win_rate: 0.43478260869565216
  god_matches_won: 40
  god_matches_played: 92
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-10'
  god_matches_analyzed: 1308
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  flex_slots:
  - Dreamer's Idol
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Spear of the Magus, Gluttonous Grimoire, The World Stone, Gem of Focus,
    The Cosmic Horror, Ancient Signet, Totem of Death, Rod of Asclepius, Polynomicon,
    Blood-Bound Book, Soul Reaver, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm
    of Radiance, Ethereal Staff, Staff of Myrddin, Wish-Granting Pearl, Typhon’s Heart,
    Bracer of The Abyss, Nimble Ring, Doom Orb.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.48
      pick: 0.46
      fit: 0.44
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.53
      pick: 0.35
      fit: 1.0
    Soul Gem:
      total: 0.6
      efficiency: 0.52
      win: 0.53
      pick: 0.56
      fit: 1.0
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.56
      pick: 0.67
      fit: 0.78
    Obsidian Shard:
      total: 0.63
      efficiency: 0.54
      win: 0.6
      pick: 0.69
      fit: 0.88
    Dreamer's Idol:
      total: 0.58
      efficiency: 0.51
      win: 0.6
      pick: 0.31
      fit: 0.78
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Ancient Signet
  - Spear of Desolation
  - The World Stone
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - The World Stone
  - Ancient Signet
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
    of the Magus, The World Stone, Death Metal, Gluttonous Grimoire, Ancient Signet,
    Bragi''s Harp, Gem of Focus, Polynomicon, Soul Reaver, The Cosmic Horror, Rod
    of Asclepius, Bancroft''s Talon, Totem of Death, Triton''s Conch, Blood-Bound
    Book, Jade Scepter, Divine Ruin, Wish-Granting Pearl, Helm of Radiance, Breastplate
    of Valor, Ethereal Staff, Doom Orb.'
  slot_scores:
    Ancient Signet:
      total: 0.5
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.49
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.53
      pick: 0.35
      fit: 0.61
    The World Stone:
      total: 0.51
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.57
    Soul Gem:
      total: 0.55
      efficiency: 0.52
      win: 0.53
      pick: 0.56
      fit: 0.71
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.56
      pick: 0.67
      fit: 0.57
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.6
      pick: 0.69
      fit: 0.57
  community_ordered:
  - Spear of Desolation
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  flex_slots:
  - Dreamer's Idol
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    god: Spear of the Magus, Gluttonous Grimoire, The World Stone, Death Metal, Gem
    of Focus, The Cosmic Horror, Ancient Signet, Bragi''s Harp, Totem of Death, Rod
    of Asclepius, Polynomicon, Blood-Bound Book, Soul Reaver, Jade Scepter, Divine
    Ruin, Triton''s Conch, Breastplate of Valor, Bancroft''s Talon, Genji''s Guard,
    Helm of Radiance, Ethereal Staff, Doom Orb.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.51
      win: 0.48
      pick: 0.46
      fit: 0.22
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.53
      pick: 0.35
      fit: 0.78
    Soul Gem:
      total: 0.58
      efficiency: 0.52
      win: 0.53
      pick: 0.56
      fit: 0.88
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.56
      pick: 0.67
      fit: 0.56
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.6
      pick: 0.69
      fit: 0.66
    Dreamer's Idol:
      total: 0.55
      efficiency: 0.51
      win: 0.6
      pick: 0.31
      fit: 0.56
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Soul Gem
  - Rod of Tahuti
  - Amanita Charm
  - Obsidian Shard
  flex_slots:
  - Kinetic Cuirass
  - Spear of Desolation
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
    this god: Amanita Charm, Rod of Asclepius, Shield of the Phoenix, Gluttonous Grimoire,
    Kinetic Cuirass, Ethereal Staff, Freya''s Tears, Shifter''s Shield, Genji''s Guard,
    Breastplate of Valor, Lifebinder, Spear of the Magus, Helm of Radiance, Sphere
    of Negation, Erosion, Yogi''s Necklace, Eye of Providence, Draconic Scale, Phoenix
    Feather, Jade Scepter, Chandra''s Grace, Wish-Granting Pearl, Blood-Bound Book,
    Glorious Pridwen, Stone of Binding.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.62
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.53
      pick: 0.35
      fit: 0.48
    Soul Gem:
      total: 0.58
      efficiency: 0.52
      win: 0.53
      pick: 0.56
      fit: 0.88
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.56
      pick: 0.67
      fit: 0.37
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.82
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.6
      pick: 0.69
      fit: 0.47
  community_ordered:
  - Spear of Desolation
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - The World Stone
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  flex_slots:
  - Dreamer's Idol
  - The World Stone
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    for this god: Spear of the Magus, Gluttonous Grimoire, The World Stone, The Cosmic
    Horror, Ancient Signet, Gem of Focus, Rod of Asclepius, Totem of Death, Polynomicon,
    Blood-Bound Book, Soul Reaver, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm
    of Radiance, Ethereal Staff, Screeching Gargoyle, Wish-Granting Pearl, Doom Orb,
    Typhon’s Heart, Breastplate of Valor, Bracer of The Abyss.'
  slot_scores:
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.53
      pick: 0.35
      fit: 1.0
    The World Stone:
      total: 0.55
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.85
    Soul Gem:
      total: 0.6
      efficiency: 0.52
      win: 0.53
      pick: 0.56
      fit: 1.0
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.86
      win: 0.56
      pick: 0.67
      fit: 0.85
    Obsidian Shard:
      total: 0.64
      efficiency: 0.54
      win: 0.6
      pick: 0.69
      fit: 0.95
    Dreamer's Idol:
      total: 0.59
      efficiency: 0.51
      win: 0.6
      pick: 0.31
      fit: 0.85
  community_ordered:
  - Spear of Desolation
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Soul Gem
  - Rod of Tahuti
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
    this god: Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Bragi''s Harp,
    Bracer of The Abyss, Ancient Signet, The World Stone, Blood-Bound Book, Death
    Metal, Bancroft''s Talon, Gem of Focus, Rod of Asclepius, Typhon’s Heart, The
    Cosmic Horror, Polynomicon, Soul Reaver, Totem of Death, Jade Scepter, Divine
    Ruin, Helm of Radiance, Daybreak Gavel, Doom Orb.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.41
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.49
    Bragi's Harp:
      total: 0.49
      efficiency: 0.44
      win: 0.53
      pick: 0.0
      fit: 0.64
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.53
      pick: 0.56
      fit: 0.57
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.56
      pick: 0.67
      fit: 0.3
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.6
      pick: 0.69
      fit: 0.4
  community_ordered:
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Gem of Focus
  - Spear of Desolation
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  flex_slots:
  - Dreamer's Idol
  - Gem of Focus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Talisman of Purification — CC-immunity / cleanse
    swap_item: Talisman of Purification
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
    + fit + win/pick). Underrated for this god: Gem of Focus, Spear of the Magus,
    Totem of Death, Gluttonous Grimoire, Breastplate of Valor, Genji''s Guard, The
    World Stone, Death Metal, Ancient Signet, Staff of Myrddin, The Cosmic Horror,
    Eye of Erebus, Screeching Gargoyle, Chandra''s Grace, Bragi''s Harp, Freya''s
    Tears, Rod of Asclepius, Polynomicon, Blood-Bound Book, Soul Reaver, Shield of
    the Phoenix, Doom Orb.'
  slot_scores:
    Gem of Focus:
      total: 0.51
      efficiency: 0.5
      win: 0.53
      pick: 0.0
      fit: 0.65
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.53
      pick: 0.35
      fit: 0.85
    Soul Gem:
      total: 0.59
      efficiency: 0.52
      win: 0.53
      pick: 0.56
      fit: 0.95
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.56
      pick: 0.67
      fit: 0.35
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.6
      pick: 0.69
      fit: 0.45
    Dreamer's Idol:
      total: 0.51
      efficiency: 0.51
      win: 0.6
      pick: 0.31
      fit: 0.35
  community_ordered:
  - Spear of Desolation
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
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
    World Stone, Gem of Focus, The Cosmic Horror, Ancient Signet, Totem of Death,
    Rod of Asclepius, Polynomicon, Blood-Bound Book, Soul Reaver, Jade Scepter, Divine
    Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin, Wish-Granting
    Pearl, Typhon’s Heart, Bracer of The Abyss, Nimble Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.53
      pick: 0.35
      fit: 1.0
    Doom Orb:
      total: 0.42
      efficiency: 0.53
      win: 0.25
      pick: 0.12
      fit: 0.78
    Spear of the Magus:
      total: 0.57
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.78
    Soul Gem:
      total: 0.6
      efficiency: 0.52
      win: 0.53
      pick: 0.56
      fit: 1.0
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.56
      pick: 0.67
      fit: 0.78
    Obsidian Shard:
      total: 0.63
      efficiency: 0.54
      win: 0.6
      pick: 0.69
      fit: 0.88
  community_ordered:
  - Spear of Desolation
  - Doom Orb
  - Soul Gem
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
---

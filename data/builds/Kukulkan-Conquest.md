---
type: smite-build
god: Kukulkan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Squall
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.57
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.9
    win_rate: 0.54
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.03
      win_rate: 0.58
    - name: Spear of Desolation
      pick_rate: 0.03
      win_rate: 0.54
  - name: Spear of Desolation
    pick_rate: 0.27
    win_rate: 0.56
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.21
      win_rate: 0.54
    - name: Polynomicon
      pick_rate: 0.09
      win_rate: 0.54
  - name: Rod of Tahuti
    pick_rate: 0.27
    win_rate: 0.59
    alternates:
    - name: Polynomicon
      pick_rate: 0.16
      win_rate: 0.54
    - name: Spear of Desolation
      pick_rate: 0.08
      win_rate: 0.4
  - name: Obsidian Shard
    pick_rate: 0.17
    win_rate: 0.5
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.31
      win_rate: 0.54
    - name: Polynomicon
      pick_rate: 0.06
      win_rate: 0.58
  - name: Evil Eye
    pick_rate: 0.07
    win_rate: 0.57
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.19
      win_rate: 0.57
    - name: Rod of Tahuti
      pick_rate: 0.19
      win_rate: 0.52
  - name: Blinking Abyss
    pick_rate: 0.11
    win_rate: 0.63
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.1
      win_rate: 0.61
    - name: Soul Reaver
      pick_rate: 0.08
      win_rate: 0.5
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.5
    win_rate: 0.59
  - name: Conduit Gem
    pick_rate: 0.21
    win_rate: 0.45
  - name: Pendulum of the Ages
    pick_rate: 0.19
    win_rate: 0.59
  source_url: https://smitebrain.com/gods/kukulkan/
  last_verified: '2026-11-02'
  god_win_rate: 0.5398428731762065
  god_matches_won: 481
  god_matches_played: 891
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14397
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
    Stone, Dreamer''s Idol, The Cosmic Horror, Heartwood Charm, Gem of Focus, Ancient
    Signet, Totem of Death, Blood-Bound Book, Divine Ruin, Jade Scepter, Bancroft''s
    Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin, Typhon’s Heart, Rod
    of Asclepius, Bracer of The Abyss, Alchemist Coat, Genji''s Guard.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.48
      win: 0.54
      pick: 0.9
      fit: 0.42
    Spear of Desolation:
      total: 0.62
      efficiency: 0.56
      win: 0.56
      pick: 0.37
      fit: 1.0
    Spear of the Magus:
      total: 0.55
      efficiency: 0.54
      win: 0.54
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.81
      win: 0.59
      pick: 0.42
      fit: 0.79
    Obsidian Shard:
      total: 0.57
      efficiency: 0.55
      win: 0.5
      pick: 0.28
      fit: 0.89
    Soul Gem:
      total: 0.57
      efficiency: 0.5
      win: 0.54
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Sundering Echo
  - Spear of Desolation
  - Rod of Tahuti
  - Doom Orb
  - Soul Gem
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Sundering Echo, Doom Orb, The World Stone, Death Metal, Spear of the Magus,
    Gluttonous Grimoire, Heartwood Charm, Ancient Signet, Dreamer''s Idol, Bragi''s
    Harp, Gem of Focus, The Cosmic Horror, Blood-Bound Book, Bancroft''s Talon, Totem
    of Death, Triton''s Conch, Divine Ruin, Jade Scepter, Genji''s Guard, Helm of
    Radiance, Ethereal Staff, Breastplate of Valor.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.48
      win: 0.54
      pick: 0.9
      fit: 0.39
    Sundering Echo:
      total: 0.52
      efficiency: 0.55
      win: 0.54
      pick: 0.0
      fit: 0.57
    Spear of Desolation:
      total: 0.56
      efficiency: 0.56
      win: 0.56
      pick: 0.37
      fit: 0.61
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.81
      win: 0.59
      pick: 0.42
      fit: 0.57
    Doom Orb:
      total: 0.51
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.57
    Soul Gem:
      total: 0.52
      efficiency: 0.5
      win: 0.54
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
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
    god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom Orb, Sundering Echo,
    The World Stone, Dreamer''s Idol, Death Metal, The Cosmic Horror, Heartwood Charm,
    Gem of Focus, Totem of Death, Ancient Signet, Bragi''s Harp, Blood-Bound Book,
    Genji''s Guard, Damaru, Divine Ruin, Jade Scepter, Triton''s Conch, Bancroft''s
    Talon, Breastplate of Valor, Chandra''s Grace.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.48
      win: 0.54
      pick: 0.9
      fit: 0.22
    Spear of Desolation:
      total: 0.58
      efficiency: 0.56
      win: 0.56
      pick: 0.37
      fit: 0.78
    Spear of the Magus:
      total: 0.51
      efficiency: 0.54
      win: 0.54
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.81
      win: 0.59
      pick: 0.42
      fit: 0.56
    Obsidian Shard:
      total: 0.53
      efficiency: 0.55
      win: 0.5
      pick: 0.28
      fit: 0.66
    Soul Gem:
      total: 0.55
      efficiency: 0.5
      win: 0.54
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
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
    this god: Amanita Charm, Soul Gem, Shield of the Phoenix, Gluttonous Grimoire,
    Kinetic Cuirass, Ethereal Staff, Genji''s Guard, Phoenix Feather, Yogi''s Necklace,
    Freya''s Tears, Rod of Asclepius, Blood-Bound Book, Breastplate of Valor, Sphere
    of Negation, Chandra''s Grace, Helm of Radiance, Helm of Darkness, Spear of the
    Magus, Erosion, Oni Hunter''s Garb, Eye of Providence, Draconic Scale, Doom Orb,
    Jade Scepter, Midgardian Mail, The World Stone, Glorious Pridwen.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.48
      win: 0.54
      pick: 0.9
      fit: 0.21
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.54
      efficiency: 0.56
      win: 0.56
      pick: 0.37
      fit: 0.49
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.81
      win: 0.59
      pick: 0.42
      fit: 0.39
    Amanita Charm:
      total: 0.58
      efficiency: 0.62
      win: 0.54
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.55
      efficiency: 0.5
      win: 0.54
      pick: 0.0
      fit: 0.89
  community_ordered:
  - Book of Thoth
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
  - Spear of the Magus
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
    for this god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom Orb, The
    World Stone, Dreamer''s Idol, The Cosmic Horror, Heartwood Charm, Gem of Focus,
    Ancient Signet, Blood-Bound Book, Totem of Death, Divine Ruin, Jade Scepter, Bancroft''s
    Talon, Screeching Gargoyle, Helm of Radiance, Ethereal Staff, Genji''s Guard,
    Typhon’s Heart, Rod of Asclepius, Staff of Myrddin, Bracer of The Abyss.'
  slot_scores:
    Spear of Desolation:
      total: 0.62
      efficiency: 0.56
      win: 0.56
      pick: 0.37
      fit: 1.0
    Doom Orb:
      total: 0.55
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.56
      efficiency: 0.54
      win: 0.54
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.81
      win: 0.59
      pick: 0.42
      fit: 0.85
    Obsidian Shard:
      total: 0.58
      efficiency: 0.55
      win: 0.5
      pick: 0.28
      fit: 0.95
    Soul Gem:
      total: 0.57
      efficiency: 0.5
      win: 0.54
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
  - Nimble Ring
  - Bragi's Harp
  - Spear of Desolation
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
    this god: Nimble Ring, Soul Gem, Gluttonous Grimoire, Sundering Echo, Bragi''s
    Harp, Spear of the Magus, Blood-Bound Book, Bracer of The Abyss, Doom Orb, The
    World Stone, Eros'' Bow, Death Metal, Dreamer''s Idol, Bancroft''s Talon, Ancient
    Signet, Heartwood Charm, Gem of Focus, The Cosmic Horror, Typhon’s Heart, Totem
    of Death, Divine Ruin, Jade Scepter, Genji''s Guard.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.49
      win: 0.54
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.48
      efficiency: 0.41
      win: 0.54
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.37
      fit: 0.4
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.81
      win: 0.59
      pick: 0.42
      fit: 0.32
    Soul Gem:
      total: 0.52
      efficiency: 0.55
      win: 0.54
      pick: 0.0
      fit: 0.58
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
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
    + fit + win/pick). Underrated for this god: Soul Gem, Heartwood Charm, Gem of
    Focus, Spear of the Magus, Totem of Death, Gluttonous Grimoire, Sundering Echo,
    Doom Orb, Genji''s Guard, The World Stone, Damaru, Breastplate of Valor, Chandra''s
    Grace, Dreamer''s Idol, Death Metal, The Cosmic Horror, Staff of Myrddin, Ancient
    Signet, Blood-Bound Book, Screeching Gargoyle, Eye of Erebus, Bragi''s Harp, Freya''s
    Tears.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.48
      win: 0.54
      pick: 0.9
      fit: 0.14
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.52
      win: 0.54
      pick: 0.29
      fit: 0.63
    Spear of Desolation:
      total: 0.59
      efficiency: 0.56
      win: 0.56
      pick: 0.37
      fit: 0.86
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.81
      win: 0.59
      pick: 0.42
      fit: 0.37
    Obsidian Shard:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.28
      fit: 0.47
    Soul Gem:
      total: 0.56
      efficiency: 0.5
      win: 0.54
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Book of Thoth
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
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
  - Spear of the Magus
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
    Orb, The World Stone, Dreamer''s Idol, The Cosmic Horror, Heartwood Charm, Gem
    of Focus, Ancient Signet, Totem of Death, Blood-Bound Book, Divine Ruin, Jade
    Scepter, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin,
    Typhon’s Heart, Rod of Asclepius, Bracer of The Abyss, Alchemist Coat, Genji''s
    Guard.'
  slot_scores:
    Spear of Desolation:
      total: 0.62
      efficiency: 0.56
      win: 0.56
      pick: 0.37
      fit: 1.0
    Doom Orb:
      total: 0.54
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.55
      efficiency: 0.54
      win: 0.54
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.81
      win: 0.59
      pick: 0.42
      fit: 0.79
    Obsidian Shard:
      total: 0.57
      efficiency: 0.55
      win: 0.5
      pick: 0.28
      fit: 0.89
    Soul Gem:
      total: 0.57
      efficiency: 0.5
      win: 0.54
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
---

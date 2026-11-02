---
type: smite-build
god: Scylla
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Devourer
  aspect_pick_rate: 0.13
  aspect_win_rate: 0.57
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.41
    win_rate: 0.54
    alternates:
    - name: Book of Thoth
      pick_rate: 0.24
      win_rate: 0.58
    - name: Doom Orb
      pick_rate: 0.09
      win_rate: 0.56
  - name: Book of Thoth
    pick_rate: 0.21
    win_rate: 0.51
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.27
      win_rate: 0.58
    - name: Polynomicon
      pick_rate: 0.14
      win_rate: 0.54
  - name: Rod of Tahuti
    pick_rate: 0.3
    win_rate: 0.54
    alternates:
    - name: Polynomicon
      pick_rate: 0.28
      win_rate: 0.57
    - name: Spear of Desolation
      pick_rate: 0.07
      win_rate: 0.51
  - name: Obsidian Shard
    pick_rate: 0.23
    win_rate: 0.52
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.34
      win_rate: 0.62
    - name: Polynomicon
      pick_rate: 0.09
      win_rate: 0.54
  - name: Void Shard
    pick_rate: 0.07
    win_rate: 0.49
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.29
      win_rate: 0.63
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.54
  - name: Blinking Abyss
    pick_rate: 0.12
    win_rate: 0.66
    alternates:
    - name: Evil Eye
      pick_rate: 0.09
      win_rate: 0.56
    - name: Obsidian Shard
      pick_rate: 0.06
      win_rate: 0.68
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.59
    win_rate: 0.6
  - name: Conduit Gem
    pick_rate: 0.31
    win_rate: 0.46
  - name: Sundering Axe
    pick_rate: 0.09
    win_rate: 0.7
  source_url: https://smitebrain.com/gods/scylla/
  last_verified: '2026-11-02'
  god_win_rate: 0.5484162895927602
  god_matches_won: 606
  god_matches_played: 1105
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
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Doom Orb
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
    this god: Soul Gem, Doom Orb, Spear of the Magus, Gluttonous Grimoire, The World
    Stone, Dreamer''s Idol, Chronos'' Pendant, The Cosmic Horror, Heartwood Charm,
    Gem of Focus, Ancient Signet, Totem of Death, Blood-Bound Book, Soul Reaver, Divine
    Ruin, Jade Scepter, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Staff
    of Myrddin, Typhon’s Heart, Rod of Asclepius, Bracer of The Abyss, Alchemist Coat,
    Genji''s Guard.'
  slot_scores:
    Spear of Desolation:
      total: 0.61
      efficiency: 0.56
      win: 0.54
      pick: 0.41
      fit: 1.0
    Doom Orb:
      total: 0.55
      efficiency: 0.51
      win: 0.56
      pick: 0.09
      fit: 0.79
    Spear of the Magus:
      total: 0.55
      efficiency: 0.54
      win: 0.54
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.81
      win: 0.54
      pick: 0.47
      fit: 0.79
    Obsidian Shard:
      total: 0.58
      efficiency: 0.55
      win: 0.52
      pick: 0.38
      fit: 0.89
    Soul Gem:
      total: 0.57
      efficiency: 0.5
      win: 0.54
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Spear of Desolation
  - Polynomicon
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Doom Orb
  - Polynomicon
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
    Gluttonous Grimoire, Chronos'' Pendant, Heartwood Charm, Ancient Signet, Dreamer''s
    Idol, Bragi''s Harp, Gem of Focus, Soul Reaver, The Cosmic Horror, Blood-Bound
    Book, Bancroft''s Talon, Totem of Death, Triton''s Conch, Divine Ruin, Jade Scepter,
    Genji''s Guard, Helm of Radiance, Ethereal Staff, Breastplate of Valor.'
  slot_scores:
    Spear of Desolation:
      total: 0.55
      efficiency: 0.56
      win: 0.54
      pick: 0.41
      fit: 0.61
    Polynomicon:
      total: 0.51
      efficiency: 0.47
      win: 0.57
      pick: 0.44
      fit: 0.49
    Doom Orb:
      total: 0.52
      efficiency: 0.51
      win: 0.56
      pick: 0.09
      fit: 0.57
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.81
      win: 0.54
      pick: 0.47
      fit: 0.57
    Obsidian Shard:
      total: 0.53
      efficiency: 0.55
      win: 0.52
      pick: 0.38
      fit: 0.57
    Soul Gem:
      total: 0.52
      efficiency: 0.5
      win: 0.54
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Spear of Desolation
  - Polynomicon
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Doom Orb
  - Spear of the Magus
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
    god: Soul Gem, Doom Orb, Spear of the Magus, Gluttonous Grimoire, Sundering Echo,
    The World Stone, Chronos'' Pendant, Dreamer''s Idol, Death Metal, The Cosmic Horror,
    Heartwood Charm, Gem of Focus, Totem of Death, Ancient Signet, Bragi''s Harp,
    Blood-Bound Book, Soul Reaver, Genji''s Guard, Damaru, Divine Ruin, Jade Scepter,
    Triton''s Conch, Bancroft''s Talon, Breastplate of Valor, Chandra''s Grace.'
  slot_scores:
    Spear of Desolation:
      total: 0.58
      efficiency: 0.56
      win: 0.54
      pick: 0.41
      fit: 0.78
    Doom Orb:
      total: 0.52
      efficiency: 0.51
      win: 0.56
      pick: 0.09
      fit: 0.56
    Spear of the Magus:
      total: 0.51
      efficiency: 0.54
      win: 0.54
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.81
      win: 0.54
      pick: 0.47
      fit: 0.56
    Obsidian Shard:
      total: 0.55
      efficiency: 0.55
      win: 0.52
      pick: 0.38
      fit: 0.66
    Soul Gem:
      total: 0.55
      efficiency: 0.5
      win: 0.54
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Obsidian Shard
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
    this god: Amanita Charm, Soul Gem, Shield of the Phoenix, Gluttonous Grimoire,
    Kinetic Cuirass, Ethereal Staff, Genji''s Guard, Phoenix Feather, Yogi''s Necklace,
    Freya''s Tears, Rod of Asclepius, Blood-Bound Book, Breastplate of Valor, Sphere
    of Negation, Doom Orb, Chandra''s Grace, Helm of Radiance, Helm of Darkness, Spear
    of the Magus, Erosion, Oni Hunter''s Garb, Eye of Providence, Draconic Scale,
    Jade Scepter, Midgardian Mail, The World Stone, Glorious Pridwen.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.53
      efficiency: 0.56
      win: 0.54
      pick: 0.41
      fit: 0.49
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.81
      win: 0.54
      pick: 0.47
      fit: 0.39
    Obsidian Shard:
      total: 0.52
      efficiency: 0.55
      win: 0.52
      pick: 0.38
      fit: 0.49
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
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
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
  - Doom Orb
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
    for this god: Soul Gem, Doom Orb, Spear of the Magus, Gluttonous Grimoire, The
    World Stone, Dreamer''s Idol, The Cosmic Horror, Chronos'' Pendant, Heartwood
    Charm, Gem of Focus, Ancient Signet, Blood-Bound Book, Totem of Death, Soul Reaver,
    Divine Ruin, Jade Scepter, Bancroft''s Talon, Screeching Gargoyle, Helm of Radiance,
    Ethereal Staff, Genji''s Guard, Typhon’s Heart, Rod of Asclepius, Staff of Myrddin,
    Bracer of The Abyss.'
  slot_scores:
    Spear of Desolation:
      total: 0.61
      efficiency: 0.56
      win: 0.54
      pick: 0.41
      fit: 1.0
    Doom Orb:
      total: 0.56
      efficiency: 0.51
      win: 0.56
      pick: 0.09
      fit: 0.85
    Spear of the Magus:
      total: 0.56
      efficiency: 0.54
      win: 0.54
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.81
      win: 0.54
      pick: 0.47
      fit: 0.85
    Obsidian Shard:
      total: 0.59
      efficiency: 0.55
      win: 0.52
      pick: 0.38
      fit: 0.95
    Soul Gem:
      total: 0.57
      efficiency: 0.5
      win: 0.54
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Spear of Desolation
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
    this god: Nimble Ring, Soul Gem, Gluttonous Grimoire, Doom Orb, Sundering Echo,
    Bragi''s Harp, Spear of the Magus, Blood-Bound Book, Bracer of The Abyss, The
    World Stone, Eros'' Bow, Chronos'' Pendant, Death Metal, Dreamer''s Idol, Bancroft''s
    Talon, Ancient Signet, Heartwood Charm, Gem of Focus, The Cosmic Horror, Typhon’s
    Heart, Soul Reaver, Totem of Death, Divine Ruin, Jade Scepter, Genji''s Guard.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.49
      win: 0.54
      pick: 0.0
      fit: 0.4
    Spear of Desolation:
      total: 0.52
      efficiency: 0.56
      win: 0.54
      pick: 0.41
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
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.81
      win: 0.54
      pick: 0.47
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
  - Chronos' Pendant
  - Spear of Desolation
  - Heartwood Charm
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Heartwood Charm
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
    + fit + win/pick). Underrated for this god: Soul Gem, Chronos'' Pendant, Heartwood
    Charm, Gem of Focus, Doom Orb, Spear of the Magus, Totem of Death, Gluttonous
    Grimoire, Sundering Echo, Genji''s Guard, The World Stone, Damaru, Breastplate
    of Valor, Chandra''s Grace, Dreamer''s Idol, Death Metal, The Cosmic Horror, Staff
    of Myrddin, Ancient Signet, Blood-Bound Book, Screeching Gargoyle, Eye of Erebus,
    Bragi''s Harp, Freya''s Tears, Soul Reaver.'
  slot_scores:
    Chronos' Pendant:
      total: 0.52
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.59
      efficiency: 0.56
      win: 0.54
      pick: 0.41
      fit: 0.86
    Heartwood Charm:
      total: 0.5
      efficiency: 0.47
      win: 0.54
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.81
      win: 0.54
      pick: 0.47
      fit: 0.37
    Obsidian Shard:
      total: 0.52
      efficiency: 0.55
      win: 0.52
      pick: 0.38
      fit: 0.47
    Soul Gem:
      total: 0.56
      efficiency: 0.5
      win: 0.54
      pick: 0.0
      fit: 0.96
  community_ordered:
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
    Orb, The World Stone, Dreamer''s Idol, Chronos'' Pendant, The Cosmic Horror, Heartwood
    Charm, Gem of Focus, Ancient Signet, Totem of Death, Blood-Bound Book, Soul Reaver,
    Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm of Radiance, Ethereal Staff,
    Staff of Myrddin, Typhon’s Heart, Rod of Asclepius, Bracer of The Abyss, Alchemist
    Coat, Genji''s Guard.'
  slot_scores:
    Spear of Desolation:
      total: 0.61
      efficiency: 0.56
      win: 0.54
      pick: 0.41
      fit: 1.0
    Doom Orb:
      total: 0.55
      efficiency: 0.51
      win: 0.56
      pick: 0.09
      fit: 0.79
    Spear of the Magus:
      total: 0.55
      efficiency: 0.54
      win: 0.54
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.81
      win: 0.54
      pick: 0.47
      fit: 0.79
    Obsidian Shard:
      total: 0.58
      efficiency: 0.55
      win: 0.52
      pick: 0.38
      fit: 0.89
    Soul Gem:
      total: 0.57
      efficiency: 0.5
      win: 0.54
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Spear of Desolation
  - Blinking Abyss
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - Blinking Abyss
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
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Spear of the Magus, Gluttonous
    Grimoire, Doom Orb, The World Stone, Dreamer''s Idol, Chronos'' Pendant, The Cosmic
    Horror, Heartwood Charm, Gem of Focus, Ancient Signet, Totem of Death, Blood-Bound
    Book, Soul Reaver, Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm of Radiance,
    Ethereal Staff, Staff of Myrddin, Typhon’s Heart, Rod of Asclepius, Bracer of
    The Abyss, Alchemist Coat, Genji''s Guard.'
  slot_scores:
    Spear of Desolation:
      total: 0.61
      efficiency: 0.56
      win: 0.54
      pick: 0.41
      fit: 1.0
    Blinking Abyss:
      total: 0.45
      efficiency: 0.19
      win: 0.66
      pick: 0.37
      fit: 0.42
    Spear of the Magus:
      total: 0.55
      efficiency: 0.54
      win: 0.54
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.81
      win: 0.54
      pick: 0.47
      fit: 0.79
    Obsidian Shard:
      total: 0.58
      efficiency: 0.55
      win: 0.52
      pick: 0.38
      fit: 0.89
    Soul Gem:
      total: 0.57
      efficiency: 0.5
      win: 0.54
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Blinking Abyss
  - Rod of Tahuti
  - Obsidian Shard
  swaps:
  - added: Blinking Abyss
    removed: Doom Orb
    reason: community 66% win over 133 matches (vs 55% on this god), taking the model's
      weakest slot from Doom Orb
  starter: *id001
---

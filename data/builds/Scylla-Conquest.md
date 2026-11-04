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
      win_rate: 0.57
  - name: Book of Thoth
    pick_rate: 0.21
    win_rate: 0.52
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.27
      win_rate: 0.59
    - name: Polynomicon
      pick_rate: 0.14
      win_rate: 0.54
  - name: Rod of Tahuti
    pick_rate: 0.3
    win_rate: 0.53
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
    win_rate: 0.48
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
  last_verified: '2026-11-04'
  god_win_rate: 0.5493716337522442
  god_matches_won: 612
  god_matches_played: 1114
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
    Stone, Dreamer''s Idol, Chronos'' Pendant, The Cosmic Horror, Ancient Signet,
    Gem of Focus, Heartwood Charm, Blood-Bound Book, Totem of Death, Soul Reaver,
    Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm of Radiance, Ethereal Staff,
    Staff of Myrddin, Typhon’s Heart, Alchemist Coat, Bracer of The Abyss, Death Metal.'
  slot_scores:
    Spear of Desolation:
      total: 0.62
      efficiency: 0.59
      win: 0.54
      pick: 0.41
      fit: 1.0
    Doom Orb:
      total: 0.57
      efficiency: 0.53
      win: 0.57
      pick: 0.09
      fit: 0.79
    Spear of the Magus:
      total: 0.56
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.53
      pick: 0.47
      fit: 0.79
    Obsidian Shard:
      total: 0.59
      efficiency: 0.58
      win: 0.52
      pick: 0.38
      fit: 0.89
    Soul Gem:
      total: 0.58
      efficiency: 0.53
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
  - Book of Thoth
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Doom Orb
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Doom Orb, Death Metal, Spear of the Magus, Ancient Signet, The World Stone,
    Gluttonous Grimoire, Chronos'' Pendant, Heartwood Charm, Dreamer''s Idol, Bragi''s
    Harp, Gem of Focus, Soul Reaver, Blood-Bound Book, The Cosmic Horror, Bancroft''s
    Talon, Triton''s Conch, Totem of Death, Divine Ruin, Jade Scepter, Genji''s Guard,
    Helm of Radiance, Ethereal Staff, Wish-Granting Pearl.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.49
      win: 0.52
      pick: 0.29
      fit: 0.39
    Spear of Desolation:
      total: 0.56
      efficiency: 0.59
      win: 0.54
      pick: 0.41
      fit: 0.61
    Doom Orb:
      total: 0.53
      efficiency: 0.53
      win: 0.57
      pick: 0.09
      fit: 0.57
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.53
      pick: 0.47
      fit: 0.57
    Obsidian Shard:
      total: 0.54
      efficiency: 0.58
      win: 0.52
      pick: 0.38
      fit: 0.57
    Soul Gem:
      total: 0.53
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Doom Orb, Spear of the Magus, Gluttonous Grimoire, The World Stone,
    Dreamer''s Idol, Chronos'' Pendant, Death Metal, Ancient Signet, The Cosmic Horror,
    Gem of Focus, Heartwood Charm, Bragi''s Harp, Blood-Bound Book, Totem of Death,
    Soul Reaver, Damaru, Divine Ruin, Jade Scepter, Genji''s Guard, Triton''s Conch,
    Bancroft''s Talon, Helm of Radiance, Ethereal Staff.'
  slot_scores:
    Spear of Desolation:
      total: 0.59
      efficiency: 0.59
      win: 0.54
      pick: 0.41
      fit: 0.78
    Doom Orb:
      total: 0.53
      efficiency: 0.53
      win: 0.57
      pick: 0.09
      fit: 0.56
    Spear of the Magus:
      total: 0.53
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.53
      pick: 0.47
      fit: 0.56
    Obsidian Shard:
      total: 0.56
      efficiency: 0.58
      win: 0.52
      pick: 0.38
      fit: 0.66
    Soul Gem:
      total: 0.56
      efficiency: 0.53
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
    Kinetic Cuirass, Ethereal Staff, Genji''s Guard, Phoenix Feather, Blood-Bound
    Book, Freya''s Tears, Yogi''s Necklace, Helm of Radiance, Doom Orb, Sphere of
    Negation, Helm of Darkness, Spear of the Magus, Breastplate of Valor, Erosion,
    Oni Hunter''s Garb, Eye of Providence, Chandra''s Grace, Jade Scepter, Draconic
    Scale, Midgardian Mail, Ancient Signet, Regrowth Striders.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.54
      efficiency: 0.59
      win: 0.54
      pick: 0.41
      fit: 0.49
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.53
      pick: 0.47
      fit: 0.39
    Obsidian Shard:
      total: 0.53
      efficiency: 0.58
      win: 0.52
      pick: 0.38
      fit: 0.49
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.56
      efficiency: 0.53
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
    World Stone, Dreamer''s Idol, The Cosmic Horror, Chronos'' Pendant, Ancient Signet,
    Gem of Focus, Heartwood Charm, Blood-Bound Book, Totem of Death, Soul Reaver,
    Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm of Radiance, Ethereal Staff,
    Screeching Gargoyle, Typhon’s Heart, Genji''s Guard, Alchemist Coat, Staff of
    Myrddin.'
  slot_scores:
    Spear of Desolation:
      total: 0.62
      efficiency: 0.59
      win: 0.54
      pick: 0.41
      fit: 1.0
    Doom Orb:
      total: 0.58
      efficiency: 0.53
      win: 0.57
      pick: 0.09
      fit: 0.85
    Spear of the Magus:
      total: 0.57
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.53
      pick: 0.47
      fit: 0.85
    Obsidian Shard:
      total: 0.6
      efficiency: 0.58
      win: 0.52
      pick: 0.38
      fit: 0.95
    Soul Gem:
      total: 0.58
      efficiency: 0.53
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
    this god: Nimble Ring, Soul Gem, Gluttonous Grimoire, Doom Orb, Bragi''s Harp,
    Spear of the Magus, Blood-Bound Book, Bracer of The Abyss, Ancient Signet, Death
    Metal, The World Stone, Chronos'' Pendant, Dreamer''s Idol, Bancroft''s Talon,
    Gem of Focus, Heartwood Charm, The Cosmic Horror, Typhon’s Heart, Soul Reaver,
    Divine Ruin, Jade Scepter, Totem of Death, Damaru, Helm of Radiance.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.4
    Spear of Desolation:
      total: 0.53
      efficiency: 0.59
      win: 0.54
      pick: 0.41
      fit: 0.4
    Nimble Ring:
      total: 0.54
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.49
      efficiency: 0.45
      win: 0.54
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.53
      pick: 0.47
      fit: 0.32
    Soul Gem:
      total: 0.53
      efficiency: 0.57
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
  - Gem of Focus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
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
    + fit + win/pick). Underrated for this god: Soul Gem, Chronos'' Pendant, Gem of
    Focus, Heartwood Charm, Doom Orb, Spear of the Magus, Totem of Death, Gluttonous
    Grimoire, Damaru, Genji''s Guard, The World Stone, Death Metal, Ancient Signet,
    Dreamer''s Idol, Breastplate of Valor, Chandra''s Grace, The Cosmic Horror, Staff
    of Myrddin, Blood-Bound Book, Eye of Erebus, Screeching Gargoyle, Bragi''s Harp,
    Soul Reaver, Freya''s Tears.'
  slot_scores:
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.55
      win: 0.54
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.6
      efficiency: 0.59
      win: 0.54
      pick: 0.41
      fit: 0.86
    Gem of Focus:
      total: 0.51
      efficiency: 0.5
      win: 0.54
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.53
      pick: 0.47
      fit: 0.37
    Obsidian Shard:
      total: 0.53
      efficiency: 0.58
      win: 0.52
      pick: 0.38
      fit: 0.47
    Soul Gem:
      total: 0.57
      efficiency: 0.53
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
    Orb, The World Stone, Dreamer''s Idol, Chronos'' Pendant, The Cosmic Horror, Ancient
    Signet, Gem of Focus, Heartwood Charm, Blood-Bound Book, Totem of Death, Soul
    Reaver, Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm of Radiance, Ethereal
    Staff, Staff of Myrddin, Typhon’s Heart, Alchemist Coat, Bracer of The Abyss,
    Death Metal.'
  slot_scores:
    Spear of Desolation:
      total: 0.62
      efficiency: 0.59
      win: 0.54
      pick: 0.41
      fit: 1.0
    Doom Orb:
      total: 0.57
      efficiency: 0.53
      win: 0.57
      pick: 0.09
      fit: 0.79
    Spear of the Magus:
      total: 0.56
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.53
      pick: 0.47
      fit: 0.79
    Obsidian Shard:
      total: 0.59
      efficiency: 0.58
      win: 0.52
      pick: 0.38
      fit: 0.89
    Soul Gem:
      total: 0.58
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
---

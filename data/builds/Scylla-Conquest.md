---
type: smite-build
god: Scylla
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Devourer
  aspect_pick_rate: 0.12
  aspect_win_rate: 0.63
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.49
    win_rate: 0.52
    alternates:
    - name: Book of Thoth
      pick_rate: 0.19
      win_rate: 0.69
    - name: Doom Orb
      pick_rate: 0.1
      win_rate: 0.57
  - name: Book of Thoth
    pick_rate: 0.22
    win_rate: 0.47
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.22
      win_rate: 0.67
    - name: Soul Gem
      pick_rate: 0.09
      win_rate: 0.33
  - name: Polynomicon
    pick_rate: 0.31
    win_rate: 0.6
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.19
      win_rate: 0.42
    - name: Chronos' Pendant
      pick_rate: 0.06
      win_rate: 0.75
  - name: Obsidian Shard
    pick_rate: 0.32
    win_rate: 0.45
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.27
      win_rate: 0.53
    - name: Polynomicon
      pick_rate: 0.1
      win_rate: 0.67
  - name: Evil Eye
    pick_rate: 0.13
    win_rate: 0.71
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.13
      win_rate: 0.57
    - name: Rod of Tahuti
      pick_rate: 0.12
      win_rate: 0.67
  - name: Void Shard
    pick_rate: 0.09
    win_rate: 0.33
    alternates:
    - name: Soul Gem
      pick_rate: 0.09
      win_rate: 0.67
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 1.0
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.55
    win_rate: 0.54
  - name: Conduit Gem
    pick_rate: 0.31
    win_rate: 0.57
  - name: Pendulum of the Ages
    pick_rate: 0.04
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/scylla/
  last_verified: '2026-09-10'
  god_win_rate: 0.5671641791044776
  god_matches_won: 38
  god_matches_played: 67
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
  - Chronos' Pendant
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Chronos'' Pendant, Spear of the Magus, Doom Orb, Gluttonous Grimoire,
    The World Stone, Dreamer''s Idol, The Cosmic Horror, Gem of Focus, Ancient Signet,
    Totem of Death, Rod of Asclepius, Blood-Bound Book, Soul Reaver, Jade Scepter,
    Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin,
    Wish-Granting Pearl, Typhon’s Heart, Bracer of The Abyss, Nimble Ring.'
  slot_scores:
    Chronos' Pendant:
      total: 0.63
      efficiency: 0.55
      win: 0.75
      pick: 0.09
      fit: 0.63
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.52
      pick: 0.49
      fit: 1.0
    Doom Orb:
      total: 0.56
      efficiency: 0.53
      win: 0.57
      pick: 0.1
      fit: 0.79
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.53
      pick: 0.45
      fit: 0.79
    Soul Gem:
      total: 0.65
      efficiency: 0.52
      win: 0.67
      pick: 0.28
      fit: 1.0
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Soul Gem
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Polynomicon
  - Doom Orb
  - Rod of Tahuti
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Chronos''
    Pendant, Doom Orb, Spear of the Magus, The World Stone, Death Metal, Gluttonous
    Grimoire, Ancient Signet, Dreamer''s Idol, Bragi''s Harp, Gem of Focus, Soul Reaver,
    The Cosmic Horror, Rod of Asclepius, Bancroft''s Talon, Totem of Death, Triton''s
    Conch, Blood-Bound Book, Jade Scepter, Divine Ruin, Wish-Granting Pearl, Helm
    of Radiance, Breastplate of Valor, Ethereal Staff.'
  slot_scores:
    Chronos' Pendant:
      total: 0.6
      efficiency: 0.55
      win: 0.75
      pick: 0.09
      fit: 0.43
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.52
      pick: 0.49
      fit: 0.61
    Polynomicon:
      total: 0.53
      efficiency: 0.46
      win: 0.6
      pick: 0.48
      fit: 0.49
    Doom Orb:
      total: 0.53
      efficiency: 0.53
      win: 0.57
      pick: 0.1
      fit: 0.57
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.53
      pick: 0.45
      fit: 0.57
    Soul Gem:
      total: 0.6
      efficiency: 0.52
      win: 0.67
      pick: 0.28
      fit: 0.71
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Polynomicon
  - Doom Orb
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Chronos'' Pendant, Spear of the Magus, Doom Orb, Gluttonous Grimoire, The
    World Stone, Dreamer''s Idol, Death Metal, Gem of Focus, The Cosmic Horror, Ancient
    Signet, Bragi''s Harp, Totem of Death, Rod of Asclepius, Blood-Bound Book, Soul
    Reaver, Jade Scepter, Divine Ruin, Triton''s Conch, Breastplate of Valor, Bancroft''s
    Talon, Genji''s Guard, Helm of Radiance, Ethereal Staff.'
  slot_scores:
    Chronos' Pendant:
      total: 0.6
      efficiency: 0.55
      win: 0.75
      pick: 0.09
      fit: 0.44
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.52
      pick: 0.49
      fit: 0.78
    Doom Orb:
      total: 0.53
      efficiency: 0.53
      win: 0.57
      pick: 0.1
      fit: 0.56
    Spear of the Magus:
      total: 0.54
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.53
      pick: 0.45
      fit: 0.56
    Soul Gem:
      total: 0.63
      efficiency: 0.52
      win: 0.67
      pick: 0.28
      fit: 0.88
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Kinetic Cuirass
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
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
    Kinetic Cuirass, Ethereal Staff, Freya''s Tears, Spear of the Magus, Shifter''s
    Shield, Genji''s Guard, Breastplate of Valor, Lifebinder, Helm of Radiance, Sphere
    of Negation, Doom Orb, Erosion, Yogi''s Necklace, Eye of Providence, Draconic
    Scale, Phoenix Feather, Jade Scepter, Chandra''s Grace, Wish-Granting Pearl, Blood-Bound
    Book, Glorious Pridwen.'
  slot_scores:
    Chronos' Pendant:
      total: 0.58
      efficiency: 0.55
      win: 0.75
      pick: 0.09
      fit: 0.31
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.52
      pick: 0.49
      fit: 0.49
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.61
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.53
      pick: 0.45
      fit: 0.39
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.63
      efficiency: 0.52
      win: 0.67
      pick: 0.28
      fit: 0.89
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
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
    for this god: Chronos'' Pendant, Spear of the Magus, Doom Orb, Gluttonous Grimoire,
    The World Stone, Dreamer''s Idol, The Cosmic Horror, Ancient Signet, Gem of Focus,
    Rod of Asclepius, Totem of Death, Blood-Bound Book, Soul Reaver, Jade Scepter,
    Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Screeching Gargoyle,
    Wish-Granting Pearl, Typhon’s Heart, Breastplate of Valor, Bracer of The Abyss.'
  slot_scores:
    Chronos' Pendant:
      total: 0.6
      efficiency: 0.55
      win: 0.75
      pick: 0.09
      fit: 0.44
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.52
      pick: 0.49
      fit: 1.0
    Doom Orb:
      total: 0.57
      efficiency: 0.53
      win: 0.57
      pick: 0.1
      fit: 0.85
    Spear of the Magus:
      total: 0.59
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.53
      pick: 0.45
      fit: 0.85
    Soul Gem:
      total: 0.65
      efficiency: 0.52
      win: 0.67
      pick: 0.28
      fit: 1.0
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Chronos' Pendant
  - Bracer of The Abyss
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
    this god: Chronos'' Pendant, Nimble Ring, Gluttonous Grimoire, Spear of the Magus,
    Bragi''s Harp, Doom Orb, Bracer of The Abyss, The World Stone, Ancient Signet,
    Blood-Bound Book, Dreamer''s Idol, Death Metal, Bancroft''s Talon, Gem of Focus,
    Rod of Asclepius, The Cosmic Horror, Typhon’s Heart, Soul Reaver, Totem of Death,
    Jade Scepter, Divine Ruin, Helm of Radiance, Daybreak Gavel.'
  slot_scores:
    Chronos' Pendant:
      total: 0.57
      efficiency: 0.55
      win: 0.75
      pick: 0.09
      fit: 0.25
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
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.53
      pick: 0.45
      fit: 0.32
    Soul Gem:
      total: 0.6
      efficiency: 0.57
      win: 0.67
      pick: 0.28
      fit: 0.58
  community_ordered:
  - Chronos' Pendant
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Gem of Focus
  - Spear of the Magus
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Gem of Focus
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Chronos'' Pendant, Gem of Focus, Spear
    of the Magus, Doom Orb, Gluttonous Grimoire, Totem of Death, The World Stone,
    Breastplate of Valor, Dreamer''s Idol, Genji''s Guard, Ancient Signet, Death Metal,
    Staff of Myrddin, The Cosmic Horror, Eye of Erebus, Screeching Gargoyle, Bragi''s
    Harp, Rod of Asclepius, Chandra''s Grace, Freya''s Tears, Blood-Bound Book, Soul
    Reaver, Jade Scepter.'
  slot_scores:
    Chronos' Pendant:
      total: 0.63
      efficiency: 0.55
      win: 0.75
      pick: 0.09
      fit: 0.63
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.52
      pick: 0.49
      fit: 0.86
    Gem of Focus:
      total: 0.52
      efficiency: 0.5
      win: 0.55
      pick: 0.0
      fit: 0.63
    Spear of the Magus:
      total: 0.51
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.37
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.53
      pick: 0.45
      fit: 0.37
    Soul Gem:
      total: 0.64
      efficiency: 0.52
      win: 0.67
      pick: 0.28
      fit: 0.96
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
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
    World Stone, Dreamer''s Idol, Chronos'' Pendant, The Cosmic Horror, Gem of Focus,
    Ancient Signet, Totem of Death, Rod of Asclepius, Blood-Bound Book, Soul Reaver,
    Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff,
    Staff of Myrddin, Wish-Granting Pearl, Typhon’s Heart, Bracer of The Abyss, Nimble
    Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.52
      pick: 0.49
      fit: 1.0
    Doom Orb:
      total: 0.56
      efficiency: 0.53
      win: 0.57
      pick: 0.1
      fit: 0.79
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.53
      pick: 0.45
      fit: 0.79
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.45
      pick: 0.53
      fit: 0.89
    Soul Gem:
      total: 0.65
      efficiency: 0.52
      win: 0.67
      pick: 0.28
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
---

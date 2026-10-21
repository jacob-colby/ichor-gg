---
type: smite-build
god: Vulcan
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fortification
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.4
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.52
    win_rate: 0.59
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.15
      win_rate: 0.5
    - name: Chronos' Pendant
      pick_rate: 0.12
      win_rate: 1.0
  - name: Spear of Desolation
    pick_rate: 0.29
    win_rate: 0.73
    alternates:
    - name: Gem of Focus
      pick_rate: 0.17
      win_rate: 0.56
    - name: Chronos' Pendant
      pick_rate: 0.1
      win_rate: 0.4
  - name: Rod of Tahuti
    pick_rate: 0.22
    win_rate: 0.64
    alternates:
    - name: The World Stone
      pick_rate: 0.18
      win_rate: 0.78
    - name: Spear of Desolation
      pick_rate: 0.1
      win_rate: 0.6
  - name: Obsidian Shard
    pick_rate: 0.16
    win_rate: 0.38
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.33
      win_rate: 0.71
    - name: Shrapnel Mod
      pick_rate: 0.06
      win_rate: 0.67
  - name: Shrapnel Mod
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.21
      win_rate: 0.7
    - name: Rod of Tahuti
      pick_rate: 0.13
      win_rate: 0.5
  - name: Surplus Mod
    pick_rate: 0.15
    win_rate: 0.57
    alternates:
    - name: Shrapnel Mod
      pick_rate: 0.28
      win_rate: 0.69
    - name: Thermal Mod
      pick_rate: 0.13
      win_rate: 0.83
  - name: Efficiency Mod
    pick_rate: 0.15
    win_rate: 0.5
    alternates:
    - name: Surplus Mod
      pick_rate: 0.38
      win_rate: 0.67
    - name: Shrapnel Mod
      pick_rate: 0.3
      win_rate: 0.5
  - name: Thermal Mod
    pick_rate: 0.19
    win_rate: 0.5
    alternates:
    - name: Surplus Mod
      pick_rate: 0.52
      win_rate: 0.45
    - name: Masterwork Mod
      pick_rate: 0.1
      win_rate: 0.5
  - name: Seismic Mod
    pick_rate: 0.33
    win_rate: 0.5
    alternates:
    - name: Surplus Mod
      pick_rate: 0.67
      win_rate: 0.5
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.33
    win_rate: 0.76
  - name: Pendulum of the Ages
    pick_rate: 0.21
    win_rate: 0.36
  - name: Sands Of Time
    pick_rate: 0.21
    win_rate: 0.55
  source_url: https://smitebrain.com/gods/vulcan/
  last_verified: '2026-10-21'
  god_win_rate: 0.6153846153846154
  god_matches_won: 32
  god_matches_played: 52
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-21'
  god_matches_analyzed: 814
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Nimble Ring
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - The World Stone
  flex_slots:
  - Book of Thoth
  - Nimble Ring
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
    this god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Nimble Ring, Doom
    Orb, Dreamer''s Idol, Bracer of The Abyss, The Cosmic Horror, Ancient Signet,
    Totem of Death, Chronos'' Pendant, Rod of Asclepius, Polynomicon, Blood-Bound
    Book, Soul Reaver, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance,
    Ethereal Staff, Wish-Granting Pearl, Typhon’s Heart, Bragi''s Harp.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.51
      win: 0.59
      pick: 0.52
      fit: 0.35
    Nimble Ring:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.51
    Spear of Desolation:
      total: 0.67
      efficiency: 0.57
      win: 0.73
      pick: 0.4
      fit: 0.83
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.64
      pick: 0.34
      fit: 0.66
    Spear of the Magus:
      total: 0.54
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.66
    The World Stone:
      total: 0.65
      efficiency: 0.52
      win: 0.78
      pick: 0.28
      fit: 0.66
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - The World Stone
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Nimble Ring
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - The World Stone
  flex_slots:
  - Spear of the Magus
  - Nimble Ring
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Spear of the Magus, Doom Orb, Bragi''s Harp, Nimble Ring, Death Metal, Gluttonous
    Grimoire, Ancient Signet, Dreamer''s Idol, Bracer of The Abyss, Polynomicon, Soul
    Reaver, The Cosmic Horror, Rod of Asclepius, Bancroft''s Talon, Totem of Death,
    Chronos'' Pendant, Triton''s Conch, Blood-Bound Book, Jade Scepter, Divine Ruin,
    Wish-Granting Pearl, Breastplate of Valor.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.51
      win: 0.59
      pick: 0.52
      fit: 0.35
    Nimble Ring:
      total: 0.49
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.35
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.73
      pick: 0.4
      fit: 0.56
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.64
      pick: 0.34
      fit: 0.52
    Spear of the Magus:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.43
    The World Stone:
      total: 0.62
      efficiency: 0.52
      win: 0.78
      pick: 0.28
      fit: 0.52
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - The World Stone
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Nimble Ring
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - The World Stone
  flex_slots:
  - Book of Thoth
  - Nimble Ring
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
    god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom Orb, Nimble Ring,
    Dreamer''s Idol, Bragi''s Harp, Death Metal, Ancient Signet, The Cosmic Horror,
    Bracer of The Abyss, Totem of Death, Chronos'' Pendant, Rod of Asclepius, Polynomicon,
    Blood-Bound Book, Soul Reaver, Jade Scepter, Divine Ruin, Breastplate of Valor,
    Triton''s Conch, Bancroft''s Talon, Genji''s Guard.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.59
      pick: 0.52
      fit: 0.2
    Nimble Ring:
      total: 0.48
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.3
    Spear of Desolation:
      total: 0.65
      efficiency: 0.57
      win: 0.73
      pick: 0.4
      fit: 0.7
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.64
      pick: 0.34
      fit: 0.5
    Spear of the Magus:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.5
    The World Stone:
      total: 0.62
      efficiency: 0.52
      win: 0.78
      pick: 0.28
      fit: 0.5
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - The World Stone
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Nimble Ring
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Book of Thoth
  - Nimble Ring
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
    this god: Amanita Charm, Soul Gem, Rod of Asclepius, Shield of the Phoenix, Gluttonous
    Grimoire, Kinetic Cuirass, Ethereal Staff, Freya''s Tears, Genji''s Guard, Spear
    of the Magus, Breastplate of Valor, Shifter''s Shield, Lifebinder, Helm of Radiance,
    Yogi''s Necklace, Sphere of Negation, Nimble Ring, Erosion, Eye of Providence,
    Phoenix Feather, Chandra''s Grace, Draconic Scale, Jade Scepter, Blood-Bound Book,
    Wish-Granting Pearl, Doom Orb.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.59
      pick: 0.52
      fit: 0.19
    Nimble Ring:
      total: 0.48
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.28
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.73
      pick: 0.4
      fit: 0.45
    The World Stone:
      total: 0.6
      efficiency: 0.52
      win: 0.78
      pick: 0.28
      fit: 0.36
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.64
      pick: 0.34
      fit: 0.36
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.76
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Nimble Ring
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - The World Stone
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s
    Idol, The Cosmic Horror, Nimble Ring, Ancient Signet, Bracer of The Abyss, Rod
    of Asclepius, Polynomicon, Totem of Death, Chronos'' Pendant, Blood-Bound Book,
    Soul Reaver, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance, Screeching
    Gargoyle, Ethereal Staff, Wish-Granting Pearl, Typhon’s Heart.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.51
      win: 0.59
      pick: 0.52
      fit: 0.26
    Nimble Ring:
      total: 0.49
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.38
    Spear of Desolation:
      total: 0.68
      efficiency: 0.57
      win: 0.73
      pick: 0.4
      fit: 0.88
    Rod of Tahuti:
      total: 0.72
      efficiency: 0.86
      win: 0.64
      pick: 0.34
      fit: 0.75
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.75
    The World Stone:
      total: 0.66
      efficiency: 0.52
      win: 0.78
      pick: 0.28
      fit: 0.75
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - The World Stone
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Spear of Desolation
  - Bragi's Harp
  - Rod of Tahuti
  - The World Stone
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
    this god: Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear of the Magus, Bragi''s
    Harp, Bracer of The Abyss, Doom Orb, Ancient Signet, Blood-Bound Book, Dreamer''s
    Idol, Death Metal, Bancroft''s Talon, Rod of Asclepius, The Cosmic Horror, Typhon’s
    Heart, Polynomicon, Soul Reaver, Totem of Death, Jade Scepter, Chronos'' Pendant,
    Divine Ruin, Helm of Radiance, Daybreak Gavel.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.73
      pick: 0.4
      fit: 0.4
    Bragi's Harp:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.64
      pick: 0.34
      fit: 0.32
    The World Stone:
      total: 0.59
      efficiency: 0.52
      win: 0.78
      pick: 0.28
      fit: 0.32
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - The World Stone
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Gem of Focus
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
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
    + fit + win/pick). Underrated for this god: Soul Gem, Spear of the Magus, Nimble
    Ring, Gluttonous Grimoire, Totem of Death, Chronos'' Pendant, Doom Orb, Breastplate
    of Valor, Dreamer''s Idol, Bragi''s Harp, Genji''s Guard, Ancient Signet, Death
    Metal, Bracer of The Abyss, The Cosmic Horror, Staff of Myrddin, Rod of Asclepius,
    Eye of Erebus, Polynomicon, Screeching Gargoyle, Chandra''s Grace, Freya''s Tears,
    Blood-Bound Book.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.51
      win: 0.59
      pick: 0.52
      fit: 0.13
    Gem of Focus:
      total: 0.52
      efficiency: 0.5
      win: 0.56
      pick: 0.23
      fit: 0.56
    Spear of Desolation:
      total: 0.66
      efficiency: 0.57
      win: 0.73
      pick: 0.4
      fit: 0.76
    The World Stone:
      total: 0.6
      efficiency: 0.52
      win: 0.78
      pick: 0.28
      fit: 0.33
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.64
      pick: 0.34
      fit: 0.33
    Soul Gem:
      total: 0.54
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Book of Thoth
  - Gem of Focus
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Nimble Ring
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
    Underrated for this god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Nimble
    Ring, Doom Orb, Dreamer''s Idol, Chronos'' Pendant, Bracer of The Abyss, The Cosmic
    Horror, Ancient Signet, Totem of Death, Rod of Asclepius, Polynomicon, Blood-Bound
    Book, Soul Reaver, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance,
    Ethereal Staff, Wish-Granting Pearl, Typhon’s Heart, Bragi''s Harp.'
  slot_scores:
    Nimble Ring:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.51
    Spear of Desolation:
      total: 0.67
      efficiency: 0.57
      win: 0.73
      pick: 0.4
      fit: 0.83
    Doom Orb:
      total: 0.51
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.64
      pick: 0.34
      fit: 0.66
    Spear of the Magus:
      total: 0.54
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.66
    Obsidian Shard:
      total: 0.49
      efficiency: 0.54
      win: 0.38
      pick: 0.27
      fit: 0.76
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
---

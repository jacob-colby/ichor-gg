---
type: smite-build
god: Vulcan
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fortification
  aspect_pick_rate: 0.09
  aspect_win_rate: 0.6
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.38
    win_rate: 0.52
    alternates:
    - name: Book of Thoth
      pick_rate: 0.24
      win_rate: 0.54
    - name: Gem of Focus
      pick_rate: 0.13
      win_rate: 0.29
  - name: The World Stone
    pick_rate: 0.22
    win_rate: 0.58
    alternates:
    - name: Book of Thoth
      pick_rate: 0.22
      win_rate: 0.33
    - name: Spear of Desolation
      pick_rate: 0.2
      win_rate: 0.64
  - name: Rod of Tahuti
    pick_rate: 0.2
    win_rate: 0.55
    alternates:
    - name: Soul Gem
      pick_rate: 0.2
      win_rate: 0.36
    - name: Chronos' Pendant
      pick_rate: 0.09
      win_rate: 0.6
  - name: Obsidian Shard
    pick_rate: 0.26
    win_rate: 0.43
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.32
      win_rate: 0.53
    - name: Soul Reaver
      pick_rate: 0.09
      win_rate: 0.6
  - name: Soul Reaver
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: Shrapnel Mod
      pick_rate: 0.12
      win_rate: 0.83
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.6
  - name: Shrapnel Mod
    pick_rate: 0.21
    win_rate: 0.4
    alternates:
    - name: Evil Eye
      pick_rate: 0.19
      win_rate: 0.22
    - name: Surplus Mod
      pick_rate: 0.15
      win_rate: 0.71
  - name: Surplus Mod
    pick_rate: 0.29
    win_rate: 0.42
    alternates:
    - name: Shrapnel Mod
      pick_rate: 0.37
      win_rate: 0.47
    - name: Thermal Mod
      pick_rate: 0.15
      win_rate: 0.83
  - name: Thermal Mod
    pick_rate: 0.15
    win_rate: 0.25
    alternates:
    - name: Surplus Mod
      pick_rate: 0.74
      win_rate: 0.6
    - name: Masterwork Mod
      pick_rate: 0.07
      win_rate: 0.5
  - name: Seismic Mod
    pick_rate: 0.5
    win_rate: 0.0
    alternates:
    - name: Surplus Mod
      pick_rate: 0.5
      win_rate: 0.5
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.29
    win_rate: 0.56
  - name: Sands Of Time
    pick_rate: 0.27
    win_rate: 0.6
  - name: Archmage's Gem
    pick_rate: 0.22
    win_rate: 0.42
  source_url: https://smitebrain.com/gods/vulcan/
  last_verified: '2026-08-26'
  god_win_rate: 0.5272727272727272
  god_matches_won: 29
  god_matches_played: 55
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-26'
  god_matches_analyzed: 888
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Chronos' Pendant
  - Nimble Ring
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
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
    this god: Chronos'' Pendant, Spear of the Magus, Gluttonous Grimoire, Nimble Ring,
    Doom Orb, Dreamer''s Idol, Bracer of The Abyss, The Cosmic Horror, Ancient Signet,
    Totem of Death, Rod of Asclepius, Polynomicon, Blood-Bound Book, Jade Scepter,
    Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Gem of Focus,
    Wish-Granting Pearl, Typhon’s Heart, Bragi''s Harp.'
  slot_scores:
    Chronos' Pendant:
      total: 0.55
      efficiency: 0.55
      win: 0.6
      pick: 0.14
      fit: 0.52
    Nimble Ring:
      total: 0.48
      efficiency: 0.6
      win: 0.42
      pick: 0.0
      fit: 0.51
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.52
      pick: 0.38
      fit: 0.83
    The World Stone:
      total: 0.56
      efficiency: 0.52
      win: 0.58
      pick: 0.3
      fit: 0.66
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.55
      pick: 0.31
      fit: 0.66
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.43
      pick: 0.43
      fit: 0.76
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Chronos' Pendant
  - Nimble Ring
  - Spear of Desolation
  - The World Stone
  - Soul Reaver
  - Rod of Tahuti
  flex_slots:
  - Soul Reaver
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Chronos''
    Pendant, Spear of the Magus, Doom Orb, Bragi''s Harp, Nimble Ring, Death Metal,
    Gluttonous Grimoire, Ancient Signet, Dreamer''s Idol, Bracer of The Abyss, Polynomicon,
    The Cosmic Horror, Rod of Asclepius, Bancroft''s Talon, Totem of Death, Triton''s
    Conch, Blood-Bound Book, Jade Scepter, Divine Ruin, Wish-Granting Pearl, Breastplate
    of Valor, Gem of Focus.'
  slot_scores:
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.55
      win: 0.6
      pick: 0.14
      fit: 0.39
    Nimble Ring:
      total: 0.45
      efficiency: 0.6
      win: 0.42
      pick: 0.0
      fit: 0.35
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.52
      pick: 0.38
      fit: 0.56
    The World Stone:
      total: 0.53
      efficiency: 0.52
      win: 0.58
      pick: 0.3
      fit: 0.52
    Soul Reaver:
      total: 0.46
      efficiency: 0.4
      win: 0.5
      pick: 0.26
      fit: 0.55
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.55
      pick: 0.31
      fit: 0.52
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Chronos' Pendant
  - Nimble Ring
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
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
    god: Chronos'' Pendant, Spear of the Magus, Gluttonous Grimoire, Doom Orb, Nimble
    Ring, Dreamer''s Idol, Bragi''s Harp, Death Metal, Ancient Signet, The Cosmic
    Horror, Bracer of The Abyss, Totem of Death, Rod of Asclepius, Polynomicon, Blood-Bound
    Book, Jade Scepter, Divine Ruin, Breastplate of Valor, Triton''s Conch, Bancroft''s
    Talon, Genji''s Guard, Gem of Focus.'
  slot_scores:
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.55
      win: 0.6
      pick: 0.14
      fit: 0.4
    Nimble Ring:
      total: 0.44
      efficiency: 0.6
      win: 0.42
      pick: 0.0
      fit: 0.3
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.52
      pick: 0.38
      fit: 0.7
    The World Stone:
      total: 0.53
      efficiency: 0.52
      win: 0.58
      pick: 0.3
      fit: 0.5
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.55
      pick: 0.31
      fit: 0.5
    Obsidian Shard:
      total: 0.5
      efficiency: 0.54
      win: 0.43
      pick: 0.43
      fit: 0.6
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Chronos' Pendant
  - Nimble Ring
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - The World Stone
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
    this god: Amanita Charm, Rod of Asclepius, Shield of the Phoenix, Gluttonous Grimoire,
    Kinetic Cuirass, Ethereal Staff, Freya''s Tears, Genji''s Guard, Spear of the
    Magus, Breastplate of Valor, Shifter''s Shield, Lifebinder, Helm of Radiance,
    Yogi''s Necklace, Sphere of Negation, Nimble Ring, Erosion, Eye of Providence,
    Phoenix Feather, Chandra''s Grace, Draconic Scale, Jade Scepter, Blood-Bound Book,
    Wish-Granting Pearl, Doom Orb.'
  slot_scores:
    Chronos' Pendant:
      total: 0.51
      efficiency: 0.55
      win: 0.6
      pick: 0.14
      fit: 0.28
    Nimble Ring:
      total: 0.44
      efficiency: 0.6
      win: 0.42
      pick: 0.0
      fit: 0.28
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.52
      pick: 0.38
      fit: 0.45
    The World Stone:
      total: 0.51
      efficiency: 0.52
      win: 0.58
      pick: 0.3
      fit: 0.36
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.55
      pick: 0.31
      fit: 0.36
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.76
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Chronos' Pendant
  - Nimble Ring
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Chronos' Pendant
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
    for this god: Chronos'' Pendant, Spear of the Magus, Gluttonous Grimoire, Doom
    Orb, Dreamer''s Idol, The Cosmic Horror, Nimble Ring, Ancient Signet, Bracer of
    The Abyss, Rod of Asclepius, Polynomicon, Totem of Death, Blood-Bound Book, Jade
    Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance, Screeching Gargoyle,
    Ethereal Staff, Wish-Granting Pearl, Typhon’s Heart, Gem of Focus.'
  slot_scores:
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.55
      win: 0.6
      pick: 0.14
      fit: 0.39
    Nimble Ring:
      total: 0.46
      efficiency: 0.6
      win: 0.42
      pick: 0.0
      fit: 0.38
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.52
      pick: 0.38
      fit: 0.88
    The World Stone:
      total: 0.57
      efficiency: 0.52
      win: 0.58
      pick: 0.3
      fit: 0.75
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.55
      pick: 0.31
      fit: 0.75
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.43
      pick: 0.43
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Chronos' Pendant
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
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
    Bragi''s Harp, Bracer of The Abyss, Doom Orb, Ancient Signet, Blood-Bound Book,
    Dreamer''s Idol, Death Metal, Bancroft''s Talon, Rod of Asclepius, The Cosmic
    Horror, Typhon’s Heart, Polynomicon, Totem of Death, Jade Scepter, Divine Ruin,
    Helm of Radiance, Daybreak Gavel, Gem of Focus.'
  slot_scores:
    Chronos' Pendant:
      total: 0.51
      efficiency: 0.55
      win: 0.6
      pick: 0.14
      fit: 0.25
    Bracer of The Abyss:
      total: 0.43
      efficiency: 0.52
      win: 0.42
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.49
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.44
      efficiency: 0.44
      win: 0.42
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.52
      pick: 0.38
      fit: 0.4
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.55
      pick: 0.31
      fit: 0.32
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Obsidian Shard
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
    + fit + win/pick). Underrated for this god: Chronos'' Pendant, Spear of the Magus,
    Nimble Ring, Gluttonous Grimoire, Totem of Death, Doom Orb, Breastplate of Valor,
    Dreamer''s Idol, Bragi''s Harp, Genji''s Guard, Ancient Signet, Death Metal, Bracer
    of The Abyss, Gem of Focus, The Cosmic Horror, Staff of Myrddin, Rod of Asclepius,
    Eye of Erebus, Polynomicon, Screeching Gargoyle, Chandra''s Grace, Freya''s Tears,
    Blood-Bound Book.'
  slot_scores:
    Chronos' Pendant:
      total: 0.55
      efficiency: 0.55
      win: 0.6
      pick: 0.14
      fit: 0.56
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.52
      pick: 0.38
      fit: 0.76
    The World Stone:
      total: 0.51
      efficiency: 0.52
      win: 0.58
      pick: 0.3
      fit: 0.33
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.55
      pick: 0.31
      fit: 0.33
    Obsidian Shard:
      total: 0.47
      efficiency: 0.54
      win: 0.43
      pick: 0.43
      fit: 0.43
    Soul Gem:
      total: 0.49
      efficiency: 0.52
      win: 0.36
      pick: 0.31
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
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
    Underrated for this god: Spear of the Magus, Gluttonous Grimoire, Nimble Ring,
    Doom Orb, Dreamer''s Idol, Chronos'' Pendant, Bracer of The Abyss, The Cosmic
    Horror, Gem of Focus, Ancient Signet, Totem of Death, Rod of Asclepius, Polynomicon,
    Blood-Bound Book, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance,
    Ethereal Staff, Wish-Granting Pearl, Typhon’s Heart, Bragi''s Harp.'
  slot_scores:
    Nimble Ring:
      total: 0.48
      efficiency: 0.6
      win: 0.42
      pick: 0.0
      fit: 0.51
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.52
      pick: 0.38
      fit: 0.83
    Doom Orb:
      total: 0.47
      efficiency: 0.53
      win: 0.42
      pick: 0.0
      fit: 0.66
    Spear of the Magus:
      total: 0.5
      efficiency: 0.6
      win: 0.42
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.55
      pick: 0.31
      fit: 0.66
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.43
      pick: 0.43
      fit: 0.76
  starter: *id001
---

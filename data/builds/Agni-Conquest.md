---
type: smite-build
god: Agni
mode: Conquest
builds:
- source: community
  aspect: Aspect of Combustion
  aspect_pick_rate: 0.09
  aspect_win_rate: 0.54
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.51
    win_rate: 0.51
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.15
      win_rate: 0.64
    - name: Book of Thoth
      pick_rate: 0.11
      win_rate: 0.24
  - name: The World Stone
    pick_rate: 0.23
    win_rate: 0.31
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.13
      win_rate: 0.42
    - name: Soul Gem
      pick_rate: 0.11
      win_rate: 0.69
  - name: Soul Gem
    pick_rate: 0.21
    win_rate: 0.33
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.2
      win_rate: 0.46
    - name: The World Stone
      pick_rate: 0.1
      win_rate: 0.67
  - name: Rod of Tahuti
    pick_rate: 0.4
    win_rate: 0.53
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.09
      win_rate: 0.69
    - name: Spear of the Magus
      pick_rate: 0.07
      win_rate: 0.4
  - name: Obsidian Shard
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.15
      win_rate: 0.58
    - name: Evil Eye
      pick_rate: 0.07
      win_rate: 0.56
  - name: Killing Stone
    pick_rate: 0.09
    win_rate: 0.29
    alternates:
    - name: Void Shard
      pick_rate: 0.08
      win_rate: 0.5
    - name: Spear of the Magus
      pick_rate: 0.08
      win_rate: 0.83
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.28
    win_rate: 0.57
  - name: Bluestone Brooch
    pick_rate: 0.23
    win_rate: 0.62
  - name: Conduit Gem
    pick_rate: 0.18
    win_rate: 0.44
  source_url: https://smitebrain.com/gods/agni/
  last_verified: '2026-11-06'
  god_win_rate: 0.5066666666666667
  god_matches_won: 76
  god_matches_played: 150
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Spear of the Magus
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Chronos'' Pendant, Dreamer''s Idol, Gluttonous Grimoire, Doom Orb, Ancient
    Signet, The Cosmic Horror, Polynomicon, Gem of Focus, Heartwood Charm, Blood-Bound
    Book, Soul Reaver, Totem of Death, Bancroft''s Talon, Jade Scepter, Divine Ruin,
    Ethereal Staff, Helm of Radiance, Bracer of The Abyss, Death Metal, Staff of Myrddin,
    Genji''s Guard, Alchemist Coat, Book of Thoth.'
  slot_scores:
    Chronos' Pendant:
      total: 0.59
      efficiency: 0.56
      win: 0.64
      pick: 0.15
      fit: 0.63
    Spear of Desolation:
      total: 0.62
      efficiency: 0.6
      win: 0.51
      pick: 0.51
      fit: 1.0
    Doom Orb:
      total: 0.52
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.82
      win: 0.53
      pick: 0.67
      fit: 0.79
    Spear of the Magus:
      total: 0.7
      efficiency: 0.56
      win: 0.83
      pick: 0.25
      fit: 0.79
    Obsidian Shard:
      total: 0.56
      efficiency: 0.53
      win: 0.5
      pick: 0.28
      fit: 0.89
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Chronos' Pendant
  - Spear of Desolation
  - Ancient Signet
  - Rod of Tahuti
  - Spear of the Magus
  flex_slots:
  - Ancient Signet
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
    Pendant, Death Metal, Ancient Signet, Polynomicon, Doom Orb, Dreamer''s Idol,
    Heartwood Charm, Bragi''s Harp, Gluttonous Grimoire, Soul Reaver, Gem of Focus,
    Blood-Bound Book, The Cosmic Horror, Bancroft''s Talon, Totem of Death, Triton''s
    Conch, Genji''s Guard, Jade Scepter, Divine Ruin, Ethereal Staff, Damaru, Helm
    of Radiance, Book of Thoth.'
  slot_scores:
    Book of Thoth:
      total: 0.34
      efficiency: 0.48
      win: 0.24
      pick: 0.11
      fit: 0.39
    Chronos' Pendant:
      total: 0.56
      efficiency: 0.56
      win: 0.64
      pick: 0.15
      fit: 0.43
    Spear of Desolation:
      total: 0.56
      efficiency: 0.6
      win: 0.51
      pick: 0.51
      fit: 0.61
    Ancient Signet:
      total: 0.5
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.53
      pick: 0.67
      fit: 0.57
    Spear of the Magus:
      total: 0.65
      efficiency: 0.56
      win: 0.83
      pick: 0.25
      fit: 0.47
  community_ordered:
  - Book of Thoth
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Death Metal
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Death Metal
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
    god: Chronos'' Pendant, Dreamer''s Idol, Gluttonous Grimoire, Death Metal, Doom
    Orb, Ancient Signet, Gem of Focus, Heartwood Charm, Polynomicon, The Cosmic Horror,
    Bragi''s Harp, Blood-Bound Book, Totem of Death, Soul Reaver, Damaru, Genji''s
    Guard, Triton''s Conch, Bancroft''s Talon, Jade Scepter, Divine Ruin, Breastplate
    of Valor, Ethereal Staff, Book of Thoth.'
  slot_scores:
    Chronos' Pendant:
      total: 0.56
      efficiency: 0.56
      win: 0.64
      pick: 0.15
      fit: 0.44
    Spear of Desolation:
      total: 0.58
      efficiency: 0.6
      win: 0.51
      pick: 0.51
      fit: 0.78
    Death Metal:
      total: 0.49
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.53
      pick: 0.67
      fit: 0.56
    Spear of the Magus:
      total: 0.66
      efficiency: 0.56
      win: 0.83
      pick: 0.25
      fit: 0.56
    Obsidian Shard:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.28
      fit: 0.66
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Shield of the Phoenix
  - Rod of Tahuti
  - Spear of the Magus
  - Amanita Charm
  flex_slots:
  - Chronos' Pendant
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Genji''s Guard,
    Ethereal Staff, Gluttonous Grimoire, Phoenix Feather, Freya''s Tears, Blood-Bound
    Book, Yogi''s Necklace, Draconic Scale, Breastplate of Valor, Chandra''s Grace,
    Oni Hunter''s Garb, Helm of Radiance, Sphere of Negation, Erosion, Helm of Darkness,
    Eye of Providence, Shifter''s Shield, Jade Scepter, Lifebinder, Dreamer''s Idol,
    Midgardian Mail.'
  slot_scores:
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.56
      win: 0.64
      pick: 0.15
      fit: 0.31
    Spear of Desolation:
      total: 0.54
      efficiency: 0.6
      win: 0.51
      pick: 0.51
      fit: 0.49
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.75
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.53
      pick: 0.67
      fit: 0.39
    Spear of the Magus:
      total: 0.64
      efficiency: 0.56
      win: 0.83
      pick: 0.25
      fit: 0.39
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.81
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
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
    for this god: Chronos'' Pendant, Dreamer''s Idol, Gluttonous Grimoire, Doom Orb,
    The Cosmic Horror, Ancient Signet, Polynomicon, Gem of Focus, Heartwood Charm,
    Blood-Bound Book, Soul Reaver, Totem of Death, Bancroft''s Talon, Jade Scepter,
    Divine Ruin, Screeching Gargoyle, Ethereal Staff, Genji''s Guard, Helm of Radiance,
    Bracer of The Abyss, Death Metal, Alchemist Coat, Book of Thoth.'
  slot_scores:
    Chronos' Pendant:
      total: 0.56
      efficiency: 0.56
      win: 0.64
      pick: 0.15
      fit: 0.44
    Spear of Desolation:
      total: 0.62
      efficiency: 0.6
      win: 0.51
      pick: 0.51
      fit: 1.0
    Doom Orb:
      total: 0.53
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.82
      win: 0.53
      pick: 0.67
      fit: 0.85
    Spear of the Magus:
      total: 0.71
      efficiency: 0.56
      win: 0.83
      pick: 0.25
      fit: 0.85
    Obsidian Shard:
      total: 0.57
      efficiency: 0.53
      win: 0.5
      pick: 0.28
      fit: 0.95
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Chronos' Pendant
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Spear of the Magus
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
    this god: Chronos'' Pendant, Nimble Ring, Gluttonous Grimoire, Bragi''s Harp,
    Blood-Bound Book, Bracer of The Abyss, Death Metal, Ancient Signet, Dreamer''s
    Idol, Polynomicon, Doom Orb, Bancroft''s Talon, Soul Reaver, Gem of Focus, Heartwood
    Charm, The Cosmic Horror, Typhon’s Heart, Totem of Death, Damaru, Genji''s Guard,
    Jade Scepter, Divine Ruin, Book of Thoth.'
  slot_scores:
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.56
      win: 0.64
      pick: 0.15
      fit: 0.25
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.5
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.49
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.53
      pick: 0.67
      fit: 0.32
    Spear of the Magus:
      total: 0.63
      efficiency: 0.56
      win: 0.83
      pick: 0.25
      fit: 0.32
  community_ordered:
  - Chronos' Pendant
  - Rod of Tahuti
  - Spear of the Magus
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Gem of Focus
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
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
    + fit + win/pick). Underrated for this god: Chronos'' Pendant, Gem of Focus, Heartwood
    Charm, Totem of Death, Damaru, Genji''s Guard, Dreamer''s Idol, Death Metal, Gluttonous
    Grimoire, Ancient Signet, Doom Orb, Polynomicon, Breastplate of Valor, Chandra''s
    Grace, Blood-Bound Book, The Cosmic Horror, Bragi''s Harp, Soul Reaver, Staff
    of Myrddin, Screeching Gargoyle, Freya''s Tears, Eye of Erebus, Shield of the
    Phoenix.'
  slot_scores:
    Chronos' Pendant:
      total: 0.59
      efficiency: 0.56
      win: 0.64
      pick: 0.15
      fit: 0.63
    Spear of Desolation:
      total: 0.59
      efficiency: 0.6
      win: 0.51
      pick: 0.51
      fit: 0.86
    Gem of Focus:
      total: 0.5
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.53
      pick: 0.67
      fit: 0.37
    Spear of the Magus:
      total: 0.64
      efficiency: 0.56
      win: 0.83
      pick: 0.25
      fit: 0.37
    Obsidian Shard:
      total: 0.5
      efficiency: 0.53
      win: 0.5
      pick: 0.28
      fit: 0.47
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Chronos' Pendant
  - Jotunn's Revenge
  - Spear of Desolation
  - Nimble Ring
  - Rod of Tahuti
  - Spear of the Magus
  flex_slots:
  - Chronos' Pendant
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Chronos'' Pendant, Tyrfing,
    Bragi''s Harp, Death Metal, The Crusher, Hydra''s Lament, Tekko-Kagi, Heartseeker,
    Titan''s Bane, The Reaper, Dreamer''s Idol, Gluttonous Grimoire, Arondight, Ancient
    Signet, Lernaean Bow, Dominance, Golden Blade, Doom Orb, Polynomicon, Silverbranch
    Bow, Avatar''s Parashu, Bracer of The Abyss, Pendulum Blade, Nimble Ring, Blood-Bound
    Book, Gem of Focus, Heartwood Charm, Toxic Blade, Soul Reaver, The Cosmic Horror,
    Transcendence, Runeforged Hammer, Triton''s Conch, Riptalon.'
  slot_scores:
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.56
      win: 0.64
      pick: 0.15
      fit: 0.34
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.65
    Spear of Desolation:
      total: 0.55
      efficiency: 0.6
      win: 0.51
      pick: 0.51
      fit: 0.55
    Nimble Ring:
      total: 0.46
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.35
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.53
      pick: 0.67
      fit: 0.44
    Spear of the Magus:
      total: 0.65
      efficiency: 0.56
      win: 0.83
      pick: 0.25
      fit: 0.44
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Jotunn's Revenge
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Jotunn's Revenge
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Chronos'' Pendant, Jotunn''s Revenge,
    Death Metal, The Crusher, Hydra''s Lament, Heartseeker, Dreamer''s Idol, Gluttonous
    Grimoire, Titan''s Bane, The Reaper, Tyrfing, Doom Orb, Ancient Signet, Bragi''s
    Harp, Polynomicon, Arondight, Avatar''s Parashu, Gem of Focus, Heartwood Charm,
    Pendulum Blade, The Cosmic Horror, Blood-Bound Book, Soul Reaver, Tekko-Kagi,
    Triton''s Conch, Totem of Death, Transcendence, Runeforged Hammer, Dominance,
    Bancroft''s Talon, Jade Scepter, Divine Ruin, Golden Blade, Shield Splitter, Book
    of Thoth.'
  slot_scores:
    Chronos' Pendant:
      total: 0.56
      efficiency: 0.56
      win: 0.64
      pick: 0.15
      fit: 0.44
    Spear of Desolation:
      total: 0.57
      efficiency: 0.6
      win: 0.51
      pick: 0.51
      fit: 0.69
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.53
      pick: 0.67
      fit: 0.56
    Spear of the Magus:
      total: 0.67
      efficiency: 0.56
      win: 0.83
      pick: 0.25
      fit: 0.56
    Obsidian Shard:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.28
      fit: 0.66
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
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
    Underrated for this god: Dreamer''s Idol, Gluttonous Grimoire, Doom Orb, Chronos''
    Pendant, Ancient Signet, The Cosmic Horror, Polynomicon, Gem of Focus, Heartwood
    Charm, Blood-Bound Book, Soul Reaver, Totem of Death, Book of Thoth, Bancroft''s
    Talon, Jade Scepter, Divine Ruin, Ethereal Staff, Helm of Radiance, Bracer of
    The Abyss, Death Metal, Staff of Myrddin, Genji''s Guard, Alchemist Coat.'
  slot_scores:
    Spear of Desolation:
      total: 0.62
      efficiency: 0.6
      win: 0.51
      pick: 0.51
      fit: 1.0
    Doom Orb:
      total: 0.52
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.7
      efficiency: 0.56
      win: 0.83
      pick: 0.25
      fit: 0.79
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.82
      win: 0.53
      pick: 0.67
      fit: 0.79
    Obsidian Shard:
      total: 0.56
      efficiency: 0.53
      win: 0.5
      pick: 0.28
      fit: 0.89
    Soul Gem:
      total: 0.5
      efficiency: 0.53
      win: 0.33
      pick: 0.33
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Nimble Ring
  - Rod of Tahuti
  - Spear of the Magus
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
    this god: Chronos'' Pendant, Dreamer''s Idol, Gluttonous Grimoire, Doom Orb, Ancient
    Signet, Polynomicon, The Cosmic Horror, Gem of Focus, Heartwood Charm, Bracer
    of The Abyss, Nimble Ring, Blood-Bound Book, Soul Reaver, Totem of Death, Bancroft''s
    Talon, Jade Scepter, Divine Ruin, Ethereal Staff, Bragi''s Harp, Helm of Radiance,
    Genji''s Guard, Death Metal, Book of Thoth.'
  slot_scores:
    Chronos' Pendant:
      total: 0.57
      efficiency: 0.56
      win: 0.64
      pick: 0.15
      fit: 0.54
    Spear of Desolation:
      total: 0.6
      efficiency: 0.6
      win: 0.51
      pick: 0.51
      fit: 0.86
    Nimble Ring:
      total: 0.48
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.82
      win: 0.53
      pick: 0.67
      fit: 0.68
    Spear of the Magus:
      total: 0.68
      efficiency: 0.56
      win: 0.83
      pick: 0.25
      fit: 0.68
    Obsidian Shard:
      total: 0.54
      efficiency: 0.53
      win: 0.5
      pick: 0.28
      fit: 0.78
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Chronos' Pendant
  - Spear of Desolation
  - Ancient Signet
  - Rod of Tahuti
  - Spear of the Magus
  flex_slots:
  - Ancient Signet
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
    Pendant, Death Metal, Bragi''s Harp, Ancient Signet, Polynomicon, Doom Orb, Dreamer''s
    Idol, Heartwood Charm, Gluttonous Grimoire, Soul Reaver, Gem of Focus, Blood-Bound
    Book, Bracer of The Abyss, Nimble Ring, The Cosmic Horror, Bancroft''s Talon,
    Totem of Death, Triton''s Conch, Genji''s Guard, Jade Scepter, Divine Ruin, Damaru,
    Book of Thoth.'
  slot_scores:
    Book of Thoth:
      total: 0.33
      efficiency: 0.48
      win: 0.24
      pick: 0.11
      fit: 0.36
    Chronos' Pendant:
      total: 0.55
      efficiency: 0.56
      win: 0.64
      pick: 0.15
      fit: 0.4
    Spear of Desolation:
      total: 0.55
      efficiency: 0.6
      win: 0.51
      pick: 0.51
      fit: 0.57
    Ancient Signet:
      total: 0.49
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.53
      pick: 0.67
      fit: 0.53
    Spear of the Magus:
      total: 0.65
      efficiency: 0.56
      win: 0.83
      pick: 0.25
      fit: 0.43
  community_ordered:
  - Book of Thoth
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: burst
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Nimble Ring
  - Rod of Tahuti
  - Spear of the Magus
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
    god: Chronos'' Pendant, Dreamer''s Idol, Gluttonous Grimoire, Death Metal, Doom
    Orb, Bragi''s Harp, Ancient Signet, Polynomicon, Gem of Focus, Heartwood Charm,
    The Cosmic Horror, Bracer of The Abyss, Blood-Bound Book, Nimble Ring, Soul Reaver,
    Totem of Death, Damaru, Genji''s Guard, Triton''s Conch, Bancroft''s Talon, Jade
    Scepter, Divine Ruin, Book of Thoth.'
  slot_scores:
    Chronos' Pendant:
      total: 0.55
      efficiency: 0.56
      win: 0.64
      pick: 0.15
      fit: 0.41
    Spear of Desolation:
      total: 0.57
      efficiency: 0.6
      win: 0.51
      pick: 0.51
      fit: 0.71
    Nimble Ring:
      total: 0.45
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.29
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.53
      pick: 0.67
      fit: 0.51
    Spear of the Magus:
      total: 0.66
      efficiency: 0.56
      win: 0.83
      pick: 0.25
      fit: 0.51
    Obsidian Shard:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.28
      fit: 0.61
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: bruiser
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Shield of the Phoenix
  - Rod of Tahuti
  - Spear of the Magus
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Genji''s Guard,
    Ethereal Staff, Gluttonous Grimoire, Phoenix Feather, Freya''s Tears, Blood-Bound
    Book, Yogi''s Necklace, Breastplate of Valor, Chandra''s Grace, Draconic Scale,
    Oni Hunter''s Garb, Helm of Radiance, Sphere of Negation, Erosion, Helm of Darkness,
    Eye of Providence, Shifter''s Shield, Ancient Signet, Regrowth Striders, Jade
    Scepter, Lifebinder.'
  slot_scores:
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.56
      win: 0.64
      pick: 0.15
      fit: 0.29
    Spear of Desolation:
      total: 0.54
      efficiency: 0.6
      win: 0.51
      pick: 0.51
      fit: 0.46
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.72
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.53
      pick: 0.67
      fit: 0.36
    Spear of the Magus:
      total: 0.64
      efficiency: 0.56
      win: 0.83
      pick: 0.25
      fit: 0.36
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: anti-tank
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Nimble Ring
  - Rod of Tahuti
  - Spear of the Magus
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
    for this god: Chronos'' Pendant, Dreamer''s Idol, Gluttonous Grimoire, Doom Orb,
    The Cosmic Horror, Ancient Signet, Polynomicon, Bracer of The Abyss, Gem of Focus,
    Heartwood Charm, Blood-Bound Book, Nimble Ring, Soul Reaver, Totem of Death, Bancroft''s
    Talon, Jade Scepter, Divine Ruin, Screeching Gargoyle, Genji''s Guard, Ethereal
    Staff, Helm of Radiance, Death Metal, Book of Thoth.'
  slot_scores:
    Chronos' Pendant:
      total: 0.55
      efficiency: 0.56
      win: 0.64
      pick: 0.15
      fit: 0.4
    Spear of Desolation:
      total: 0.6
      efficiency: 0.6
      win: 0.51
      pick: 0.51
      fit: 0.9
    Nimble Ring:
      total: 0.46
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.37
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.82
      win: 0.53
      pick: 0.67
      fit: 0.77
    Spear of the Magus:
      total: 0.7
      efficiency: 0.56
      win: 0.83
      pick: 0.25
      fit: 0.77
    Obsidian Shard:
      total: 0.56
      efficiency: 0.53
      win: 0.5
      pick: 0.28
      fit: 0.87
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: attack-speed
  slot_order:
  - Chronos' Pendant
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Rod of Tahuti
  - Spear of the Magus
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
    this god: Chronos'' Pendant, Nimble Ring, Gluttonous Grimoire, Bragi''s Harp,
    Blood-Bound Book, Bracer of The Abyss, Death Metal, Ancient Signet, Dreamer''s
    Idol, Polynomicon, Doom Orb, Bancroft''s Talon, Soul Reaver, Gem of Focus, Heartwood
    Charm, The Cosmic Horror, Typhon’s Heart, Totem of Death, Damaru, Genji''s Guard,
    Jade Scepter, Divine Ruin, Book of Thoth.'
  slot_scores:
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.56
      win: 0.64
      pick: 0.15
      fit: 0.25
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.5
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.49
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.53
      pick: 0.67
      fit: 0.32
    Spear of the Magus:
      total: 0.63
      efficiency: 0.56
      win: 0.83
      pick: 0.25
      fit: 0.32
  community_ordered:
  - Chronos' Pendant
  - Rod of Tahuti
  - Spear of the Magus
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Nimble Ring
  - Spear of Desolation
  - Gem of Focus
  - Rod of Tahuti
  - Spear of the Magus
  flex_slots:
  - Gem of Focus
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Chronos'' Pendant, Gem of Focus, Heartwood
    Charm, Damaru, Genji''s Guard, Totem of Death, Dreamer''s Idol, Death Metal, Ancient
    Signet, Gluttonous Grimoire, Bragi''s Harp, Polynomicon, Doom Orb, Breastplate
    of Valor, Chandra''s Grace, Bracer of The Abyss, Blood-Bound Book, Nimble Ring,
    Soul Reaver, The Cosmic Horror, Staff of Myrddin, Screeching Gargoyle, Freya''s
    Tears.'
  slot_scores:
    Chronos' Pendant:
      total: 0.58
      efficiency: 0.56
      win: 0.64
      pick: 0.15
      fit: 0.57
    Nimble Ring:
      total: 0.44
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.22
    Spear of Desolation:
      total: 0.58
      efficiency: 0.6
      win: 0.51
      pick: 0.51
      fit: 0.78
    Gem of Focus:
      total: 0.49
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.53
      pick: 0.67
      fit: 0.34
    Spear of the Magus:
      total: 0.63
      efficiency: 0.56
      win: 0.83
      pick: 0.25
      fit: 0.34
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: strength
  slot_order:
  - Chronos' Pendant
  - Jotunn's Revenge
  - Spear of Desolation
  - Nimble Ring
  - Rod of Tahuti
  - Spear of the Magus
  flex_slots:
  - Chronos' Pendant
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Chronos'' Pendant, Tyrfing,
    Bragi''s Harp, Death Metal, The Crusher, Hydra''s Lament, Tekko-Kagi, Heartseeker,
    Titan''s Bane, The Reaper, Dreamer''s Idol, Gluttonous Grimoire, Arondight, Ancient
    Signet, Lernaean Bow, Dominance, Golden Blade, Doom Orb, Polynomicon, Silverbranch
    Bow, Avatar''s Parashu, Bracer of The Abyss, Pendulum Blade, Nimble Ring, Blood-Bound
    Book, Gem of Focus, Heartwood Charm, Toxic Blade, Soul Reaver, The Cosmic Horror,
    Transcendence, Runeforged Hammer, Triton''s Conch, Riptalon.'
  slot_scores:
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.56
      win: 0.64
      pick: 0.15
      fit: 0.34
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.65
    Spear of Desolation:
      total: 0.55
      efficiency: 0.6
      win: 0.51
      pick: 0.51
      fit: 0.55
    Nimble Ring:
      total: 0.46
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.35
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.53
      pick: 0.67
      fit: 0.44
    Spear of the Magus:
      total: 0.65
      efficiency: 0.56
      win: 0.83
      pick: 0.25
      fit: 0.44
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: str-int
  slot_order:
  - Chronos' Pendant
  - Jotunn's Revenge
  - Spear of Desolation
  - Nimble Ring
  - Rod of Tahuti
  - Spear of the Magus
  flex_slots:
  - Jotunn's Revenge
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Chronos'' Pendant, Jotunn''s Revenge,
    Tyrfing, Death Metal, Bragi''s Harp, The Crusher, Hydra''s Lament, Heartseeker,
    Dreamer''s Idol, Tekko-Kagi, Gluttonous Grimoire, Titan''s Bane, Ancient Signet,
    The Reaper, Doom Orb, Polynomicon, Arondight, Silverbranch Bow, Bracer of The
    Abyss, Gem of Focus, Heartwood Charm, Blood-Bound Book, Avatar''s Parashu, Golden
    Blade, Lernaean Bow, Dominance, Nimble Ring, The Cosmic Horror, Pendulum Blade,
    Soul Reaver, Toxic Blade, Triton''s Conch, Totem of Death, Transcendence, Runeforged
    Hammer.'
  slot_scores:
    Chronos' Pendant:
      total: 0.55
      efficiency: 0.56
      win: 0.64
      pick: 0.15
      fit: 0.4
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.56
      efficiency: 0.6
      win: 0.51
      pick: 0.51
      fit: 0.63
    Nimble Ring:
      total: 0.46
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.37
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.53
      pick: 0.67
      fit: 0.51
    Spear of the Magus:
      total: 0.66
      efficiency: 0.56
      win: 0.83
      pick: 0.25
      fit: 0.51
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Spear of the Magus
  starter: *id001
  aspect: Aspect of Combustion
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
    Underrated for this god: Dreamer''s Idol, Gluttonous Grimoire, Doom Orb, Chronos''
    Pendant, Ancient Signet, Polynomicon, The Cosmic Horror, Gem of Focus, Heartwood
    Charm, Bracer of The Abyss, Nimble Ring, Blood-Bound Book, Soul Reaver, Totem
    of Death, Book of Thoth, Bancroft''s Talon, Jade Scepter, Divine Ruin, Ethereal
    Staff, Bragi''s Harp, Helm of Radiance, Genji''s Guard, Death Metal.'
  slot_scores:
    Spear of Desolation:
      total: 0.6
      efficiency: 0.6
      win: 0.51
      pick: 0.51
      fit: 0.86
    Doom Orb:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.68
    Spear of the Magus:
      total: 0.68
      efficiency: 0.56
      win: 0.83
      pick: 0.25
      fit: 0.68
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.82
      win: 0.53
      pick: 0.67
      fit: 0.68
    Obsidian Shard:
      total: 0.54
      efficiency: 0.53
      win: 0.5
      pick: 0.28
      fit: 0.78
    Soul Gem:
      total: 0.5
      efficiency: 0.53
      win: 0.33
      pick: 0.33
      fit: 0.96
  community_ordered:
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
  aspect: Aspect of Combustion
---

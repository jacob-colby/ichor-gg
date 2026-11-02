---
type: smite-build
god: Agni
mode: Conquest
builds:
- source: community
  aspect: Aspect of Combustion
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.33
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.44
    win_rate: 0.51
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.24
      win_rate: 0.55
    - name: Book of Thoth
      pick_rate: 0.16
      win_rate: 0.53
  - name: The World Stone
    pick_rate: 0.32
    win_rate: 0.55
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.17
      win_rate: 0.51
    - name: Chronos' Pendant
      pick_rate: 0.11
      win_rate: 0.53
  - name: Rod of Tahuti
    pick_rate: 0.19
    win_rate: 0.61
    alternates:
    - name: Soul Gem
      pick_rate: 0.16
      win_rate: 0.44
    - name: The World Stone
      pick_rate: 0.14
      win_rate: 0.45
  - name: Obsidian Shard
    pick_rate: 0.18
    win_rate: 0.5
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.35
      win_rate: 0.52
    - name: Soul Reaver
      pick_rate: 0.06
      win_rate: 0.56
  - name: Evil Eye
    pick_rate: 0.1
    win_rate: 0.37
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.17
      win_rate: 0.57
    - name: Rod of Tahuti
      pick_rate: 0.16
      win_rate: 0.56
  - name: Soul Reaver
    pick_rate: 0.07
    win_rate: 0.56
    alternates:
    - name: Evil Eye
      pick_rate: 0.12
      win_rate: 0.45
    - name: Obsidian Shard
      pick_rate: 0.08
      win_rate: 0.75
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.26
    win_rate: 0.59
  - name: Archmage's Gem
    pick_rate: 0.21
    win_rate: 0.55
  - name: Conduit Gem
    pick_rate: 0.2
    win_rate: 0.44
  source_url: https://smitebrain.com/gods/agni/
  last_verified: '2026-10-30'
  god_win_rate: 0.5093399750933998
  god_matches_won: 409
  god_matches_played: 803
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-30'
  god_matches_analyzed: 10706
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - The World Stone
  - Spear of the Magus
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
    this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s Idol,
    Lotus Sickle, The Cosmic Horror, Gem of Focus, Ancient Signet, Totem of Death,
    Rod of Asclepius, Polynomicon, Blood-Bound Book, Jade Scepter, Divine Ruin, Bancroft''s
    Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin, Wish-Granting Pearl,
    Typhon’s Heart, Bracer of The Abyss.'
  slot_scores:
    Nimble Ring:
      total: 0.44
      efficiency: 0.39
      win: 0.53
      pick: 0.0
      fit: 0.42
    Spear of Desolation:
      total: 0.6
      efficiency: 0.58
      win: 0.51
      pick: 0.44
      fit: 1.0
    The World Stone:
      total: 0.57
      efficiency: 0.52
      win: 0.55
      pick: 0.44
      fit: 0.79
    Spear of the Magus:
      total: 0.57
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.85
      win: 0.61
      pick: 0.3
      fit: 0.79
    Obsidian Shard:
      total: 0.57
      efficiency: 0.55
      win: 0.5
      pick: 0.3
      fit: 0.89
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Lotus Sickle
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Spear of the Magus
  - Rod of Tahuti
  flex_slots:
  - Lotus Sickle
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Spear
    of the Magus, Lotus Sickle, Doom Orb, Death Metal, Gluttonous Grimoire, Ancient
    Signet, Dreamer''s Idol, Bragi''s Harp, Gem of Focus, Polynomicon, The Cosmic
    Horror, Rod of Asclepius, Bancroft''s Talon, Totem of Death, Triton''s Conch,
    Blood-Bound Book, Jade Scepter, Divine Ruin, Wish-Granting Pearl, Helm of Radiance,
    Genji''s Guard.'
  slot_scores:
    Lotus Sickle:
      total: 0.52
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.53
    Book of Thoth:
      total: 0.48
      efficiency: 0.5
      win: 0.53
      pick: 0.16
      fit: 0.39
    Spear of Desolation:
      total: 0.55
      efficiency: 0.58
      win: 0.51
      pick: 0.44
      fit: 0.61
    The World Stone:
      total: 0.54
      efficiency: 0.52
      win: 0.55
      pick: 0.44
      fit: 0.57
    Spear of the Magus:
      total: 0.52
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.85
      win: 0.61
      pick: 0.3
      fit: 0.57
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Soul Gem
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
    god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Lotus Sickle, Dreamer''s
    Idol, Death Metal, Gem of Focus, The Cosmic Horror, Ancient Signet, Bragi''s Harp,
    Totem of Death, Rod of Asclepius, Polynomicon, Blood-Bound Book, Jade Scepter,
    Divine Ruin, Triton''s Conch, Bancroft''s Talon, Genji''s Guard, Breastplate of
    Valor, Helm of Radiance.'
  slot_scores:
    Spear of Desolation:
      total: 0.57
      efficiency: 0.58
      win: 0.51
      pick: 0.44
      fit: 0.78
    Spear of the Magus:
      total: 0.53
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.56
    The World Stone:
      total: 0.53
      efficiency: 0.52
      win: 0.55
      pick: 0.44
      fit: 0.56
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.85
      win: 0.61
      pick: 0.3
      fit: 0.56
    Obsidian Shard:
      total: 0.53
      efficiency: 0.55
      win: 0.5
      pick: 0.3
      fit: 0.66
    Soul Gem:
      total: 0.52
      efficiency: 0.52
      win: 0.44
      pick: 0.25
      fit: 0.88
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  - Rod of Asclepius
  flex_slots:
  - Spear of Desolation
  - Freya's Tears
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
    this god: Amanita Charm, Rod of Asclepius, Shield of the Phoenix, Gluttonous Grimoire,
    Kinetic Cuirass, Ethereal Staff, Freya''s Tears, Spear of the Magus, Genji''s
    Guard, Shifter''s Shield, Lifebinder, Breastplate of Valor, Helm of Radiance,
    Yogi''s Necklace, Sphere of Negation, Erosion, Eye of Providence, Jade Scepter,
    Draconic Scale, Phoenix Feather, Chandra''s Grace, Lotus Sickle, Wish-Granting
    Pearl, Blood-Bound Book, Doom Orb.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.53
      efficiency: 0.58
      win: 0.51
      pick: 0.44
      fit: 0.49
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.42
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.85
      win: 0.61
      pick: 0.3
      fit: 0.39
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.81
    Rod of Asclepius:
      total: 0.54
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Spear of the Magus
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
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s Idol,
    The Cosmic Horror, Lotus Sickle, Gem of Focus, Ancient Signet, Rod of Asclepius,
    Polynomicon, Totem of Death, Blood-Bound Book, Jade Scepter, Divine Ruin, Bancroft''s
    Talon, Helm of Radiance, Ethereal Staff, Screeching Gargoyle, Wish-Granting Pearl,
    Typhon’s Heart, Bracer of The Abyss.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.5
      win: 0.53
      pick: 0.16
      fit: 0.3
    Spear of Desolation:
      total: 0.6
      efficiency: 0.58
      win: 0.51
      pick: 0.44
      fit: 1.0
    The World Stone:
      total: 0.58
      efficiency: 0.52
      win: 0.55
      pick: 0.44
      fit: 0.85
    Spear of the Magus:
      total: 0.58
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.72
      efficiency: 0.85
      win: 0.61
      pick: 0.3
      fit: 0.85
    Obsidian Shard:
      total: 0.57
      efficiency: 0.55
      win: 0.5
      pick: 0.3
      fit: 0.95
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Spear of Desolation
  - Bragi's Harp
  - Gluttonous Grimoire
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
    this god: Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Bragi''s Harp,
    Bracer of The Abyss, Lotus Sickle, Doom Orb, Dreamer''s Idol, Blood-Bound Book,
    Death Metal, Ancient Signet, Bancroft''s Talon, Gem of Focus, The Cosmic Horror,
    Rod of Asclepius, Polynomicon, Typhon’s Heart, Jade Scepter, Divine Ruin, Totem
    of Death, Helm of Radiance.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.51
      efficiency: 0.58
      win: 0.51
      pick: 0.44
      fit: 0.4
    Bragi's Harp:
      total: 0.49
      efficiency: 0.44
      win: 0.53
      pick: 0.0
      fit: 0.63
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.85
      win: 0.61
      pick: 0.3
      fit: 0.32
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Lotus Sickle
  - Book of Thoth
  - Spear of Desolation
  - Chronos' Pendant
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Lotus Sickle
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
    + fit + win/pick). Underrated for this god: Lotus Sickle, Gem of Focus, Spear
    of the Magus, Gluttonous Grimoire, Totem of Death, Doom Orb, Dreamer''s Idol,
    Genji''s Guard, Breastplate of Valor, Death Metal, Ancient Signet, The Cosmic
    Horror, Staff of Myrddin, Eye of Erebus, Screeching Gargoyle, Bragi''s Harp, Rod
    of Asclepius, Chandra''s Grace, Polynomicon, Freya''s Tears, Blood-Bound Book.'
  slot_scores:
    Lotus Sickle:
      total: 0.53
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.63
    Book of Thoth:
      total: 0.44
      efficiency: 0.5
      win: 0.53
      pick: 0.16
      fit: 0.14
    Spear of Desolation:
      total: 0.58
      efficiency: 0.58
      win: 0.51
      pick: 0.44
      fit: 0.86
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.55
      win: 0.55
      pick: 0.24
      fit: 0.63
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.85
      win: 0.61
      pick: 0.3
      fit: 0.37
    Soul Gem:
      total: 0.53
      efficiency: 0.52
      win: 0.44
      pick: 0.25
      fit: 0.96
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Chronos' Pendant
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Spear of Desolation
  - Transcendence
  - Nimble Ring
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
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
    win/pick). Underrated for this god: Jotunn''s Revenge, Spear of the Magus, Tyrfing,
    Bragi''s Harp, Hydra''s Lament, Heartseeker, Tekko-Kagi, Lernaean Bow, Nimble
    Ring, Death Metal, Gluttonous Grimoire, Titan''s Bane, The Crusher, Silverbranch
    Bow, The Reaper, Golden Blade, Lotus Sickle, Doom Orb, Dreamer''s Idol, Pendulum
    Blade, Dominance, Arondight, Avatar''s Parashu, Bracer of The Abyss, Riptalon,
    Transcendence, Ancient Signet, Runeforged Hammer, Gem of Focus, Toxic Blade, The
    Cosmic Horror, Avenging Blade, Triton''s Conch, Rod of Asclepius, Polynomicon.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.5
      win: 0.53
      pick: 0.16
      fit: 0.23
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.69
      win: 0.53
      pick: 0.0
      fit: 0.65
    Spear of Desolation:
      total: 0.54
      efficiency: 0.58
      win: 0.51
      pick: 0.44
      fit: 0.55
    Transcendence:
      total: 0.47
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.32
    Nimble Ring:
      total: 0.5
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.35
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.85
      win: 0.61
      pick: 0.3
      fit: 0.44
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Spear of Desolation
  - Transcendence
  - Rod of Tahuti
  - Spear of the Magus
  flex_slots:
  - Book of Thoth
  - Transcendence
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Spear of the Magus,
    Gluttonous Grimoire, Heartseeker, Hydra''s Lament, Death Metal, Doom Orb, Lotus
    Sickle, Titan''s Bane, The Crusher, Dreamer''s Idol, The Reaper, Pendulum Blade,
    Bragi''s Harp, Ancient Signet, Tyrfing, Gem of Focus, The Cosmic Horror, Avatar''s
    Parashu, Arondight, Transcendence, Tekko-Kagi, Runeforged Hammer, Rod of Asclepius,
    Triton''s Conch, Polynomicon, Totem of Death, Blood-Bound Book, Avenging Blade,
    Jade Scepter, Divine Ruin, Golden Blade, Bancroft''s Talon, Silverbranch Bow.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.5
      win: 0.53
      pick: 0.16
      fit: 0.31
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.69
      win: 0.53
      pick: 0.0
      fit: 0.69
    Spear of Desolation:
      total: 0.56
      efficiency: 0.58
      win: 0.51
      pick: 0.44
      fit: 0.69
    Transcendence:
      total: 0.47
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.31
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.85
      win: 0.61
      pick: 0.3
      fit: 0.56
    Spear of the Magus:
      total: 0.53
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
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
    Underrated for this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s
    Idol, Lotus Sickle, The Cosmic Horror, Gem of Focus, Ancient Signet, Totem of
    Death, Rod of Asclepius, Polynomicon, Blood-Bound Book, Jade Scepter, Divine Ruin,
    Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin, Wish-Granting
    Pearl, Typhon’s Heart, Bracer of The Abyss.'
  slot_scores:
    Spear of Desolation:
      total: 0.6
      efficiency: 0.58
      win: 0.51
      pick: 0.44
      fit: 1.0
    Doom Orb:
      total: 0.54
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.57
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.85
      win: 0.61
      pick: 0.3
      fit: 0.79
    Obsidian Shard:
      total: 0.57
      efficiency: 0.55
      win: 0.5
      pick: 0.3
      fit: 0.89
    Soul Gem:
      total: 0.54
      efficiency: 0.52
      win: 0.44
      pick: 0.25
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Nimble Ring
  - The World Stone
  - Spear of the Magus
  - Rod of Tahuti
  flex_slots:
  - Nimble Ring
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
    this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Nimble Ring, Lotus
    Sickle, Dreamer''s Idol, The Cosmic Horror, Bracer of The Abyss, Gem of Focus,
    Ancient Signet, Totem of Death, Rod of Asclepius, Polynomicon, Blood-Bound Book,
    Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff,
    Wish-Granting Pearl, Typhon’s Heart.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.5
      win: 0.53
      pick: 0.16
      fit: 0.36
    Spear of Desolation:
      total: 0.58
      efficiency: 0.58
      win: 0.51
      pick: 0.44
      fit: 0.86
    Nimble Ring:
      total: 0.52
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.5
    The World Stone:
      total: 0.55
      efficiency: 0.52
      win: 0.55
      pick: 0.44
      fit: 0.68
    Spear of the Magus:
      total: 0.55
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.68
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.85
      win: 0.61
      pick: 0.3
      fit: 0.68
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: mana-stack
  slot_order:
  - Lotus Sickle
  - Book of Thoth
  - Spear of Desolation
  - Nimble Ring
  - The World Stone
  - Rod of Tahuti
  flex_slots:
  - Nimble Ring
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Spear
    of the Magus, Lotus Sickle, Doom Orb, Bragi''s Harp, Nimble Ring, Gluttonous Grimoire,
    Death Metal, Ancient Signet, Dreamer''s Idol, Gem of Focus, Bracer of The Abyss,
    Polynomicon, The Cosmic Horror, Rod of Asclepius, Bancroft''s Talon, Totem of
    Death, Triton''s Conch, Blood-Bound Book, Jade Scepter, Divine Ruin, Wish-Granting
    Pearl.'
  slot_scores:
    Lotus Sickle:
      total: 0.51
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.49
    Book of Thoth:
      total: 0.48
      efficiency: 0.5
      win: 0.53
      pick: 0.16
      fit: 0.36
    Spear of Desolation:
      total: 0.54
      efficiency: 0.58
      win: 0.51
      pick: 0.44
      fit: 0.57
    Nimble Ring:
      total: 0.5
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.34
    The World Stone:
      total: 0.53
      efficiency: 0.52
      win: 0.55
      pick: 0.44
      fit: 0.53
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.85
      win: 0.61
      pick: 0.3
      fit: 0.53
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Nimble Ring
  - The World Stone
  - Spear of the Magus
  - Rod of Tahuti
  flex_slots:
  - Nimble Ring
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
    god: Spear of the Magus, Gluttonous Grimoire, Lotus Sickle, Doom Orb, Dreamer''s
    Idol, Nimble Ring, Bragi''s Harp, Death Metal, Gem of Focus, The Cosmic Horror,
    Ancient Signet, Bracer of The Abyss, Totem of Death, Rod of Asclepius, Polynomicon,
    Blood-Bound Book, Jade Scepter, Divine Ruin, Triton''s Conch, Bancroft''s Talon,
    Genji''s Guard.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.5
      win: 0.53
      pick: 0.16
      fit: 0.2
    Spear of Desolation:
      total: 0.56
      efficiency: 0.58
      win: 0.51
      pick: 0.44
      fit: 0.71
    Nimble Ring:
      total: 0.49
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.29
    The World Stone:
      total: 0.53
      efficiency: 0.52
      win: 0.55
      pick: 0.44
      fit: 0.51
    Spear of the Magus:
      total: 0.53
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.85
      win: 0.61
      pick: 0.3
      fit: 0.51
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  - Rod of Asclepius
  flex_slots:
  - Spear of Desolation
  - Freya's Tears
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
    this god: Amanita Charm, Rod of Asclepius, Shield of the Phoenix, Gluttonous Grimoire,
    Kinetic Cuirass, Ethereal Staff, Freya''s Tears, Genji''s Guard, Spear of the
    Magus, Shifter''s Shield, Lifebinder, Breastplate of Valor, Helm of Radiance,
    Yogi''s Necklace, Sphere of Negation, Erosion, Nimble Ring, Eye of Providence,
    Jade Scepter, Phoenix Feather, Draconic Scale, Chandra''s Grace, Lotus Sickle,
    Blood-Bound Book, Wish-Granting Pearl.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.57
    Spear of Desolation:
      total: 0.52
      efficiency: 0.58
      win: 0.51
      pick: 0.44
      fit: 0.46
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.39
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.85
      win: 0.61
      pick: 0.3
      fit: 0.36
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.77
    Rod of Asclepius:
      total: 0.54
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: anti-tank
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - The World Stone
  - Spear of the Magus
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
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s Idol,
    The Cosmic Horror, Nimble Ring, Lotus Sickle, Bracer of The Abyss, Ancient Signet,
    Gem of Focus, Rod of Asclepius, Polynomicon, Totem of Death, Blood-Bound Book,
    Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff,
    Screeching Gargoyle, Wish-Granting Pearl.'
  slot_scores:
    Nimble Ring:
      total: 0.5
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.37
    Spear of Desolation:
      total: 0.59
      efficiency: 0.58
      win: 0.51
      pick: 0.44
      fit: 0.9
    The World Stone:
      total: 0.57
      efficiency: 0.52
      win: 0.55
      pick: 0.44
      fit: 0.77
    Spear of the Magus:
      total: 0.57
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.85
      win: 0.61
      pick: 0.3
      fit: 0.77
    Obsidian Shard:
      total: 0.56
      efficiency: 0.55
      win: 0.5
      pick: 0.3
      fit: 0.87
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Spear of Desolation
  - Bragi's Harp
  - Gluttonous Grimoire
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
    this god: Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Bragi''s Harp,
    Bracer of The Abyss, Lotus Sickle, Doom Orb, Dreamer''s Idol, Blood-Bound Book,
    Death Metal, Ancient Signet, Bancroft''s Talon, Gem of Focus, The Cosmic Horror,
    Rod of Asclepius, Polynomicon, Typhon’s Heart, Jade Scepter, Divine Ruin, Totem
    of Death, Helm of Radiance.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.51
      efficiency: 0.58
      win: 0.51
      pick: 0.44
      fit: 0.4
    Bragi's Harp:
      total: 0.49
      efficiency: 0.44
      win: 0.53
      pick: 0.0
      fit: 0.63
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.85
      win: 0.61
      pick: 0.3
      fit: 0.32
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: cooldown
  slot_order:
  - Lotus Sickle
  - Chronos' Pendant
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
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
    + fit + win/pick). Underrated for this god: Lotus Sickle, Spear of the Magus,
    Gem of Focus, Gluttonous Grimoire, Nimble Ring, Totem of Death, Doom Orb, Dreamer''s
    Idol, Genji''s Guard, Breastplate of Valor, Bragi''s Harp, Death Metal, Ancient
    Signet, Bracer of The Abyss, The Cosmic Horror, Staff of Myrddin, Eye of Erebus,
    Rod of Asclepius, Polynomicon, Screeching Gargoyle, Chandra''s Grace.'
  slot_scores:
    Lotus Sickle:
      total: 0.53
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.57
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.55
      win: 0.55
      pick: 0.24
      fit: 0.57
    Spear of Desolation:
      total: 0.57
      efficiency: 0.58
      win: 0.51
      pick: 0.44
      fit: 0.78
    Spear of the Magus:
      total: 0.5
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.34
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.85
      win: 0.61
      pick: 0.3
      fit: 0.34
    Soul Gem:
      total: 0.52
      efficiency: 0.52
      win: 0.44
      pick: 0.25
      fit: 0.88
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: strength
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Spear of Desolation
  - Transcendence
  - Nimble Ring
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
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
    win/pick). Underrated for this god: Jotunn''s Revenge, Spear of the Magus, Tyrfing,
    Bragi''s Harp, Hydra''s Lament, Heartseeker, Tekko-Kagi, Lernaean Bow, Nimble
    Ring, Death Metal, Gluttonous Grimoire, Titan''s Bane, The Crusher, Silverbranch
    Bow, The Reaper, Golden Blade, Lotus Sickle, Doom Orb, Dreamer''s Idol, Pendulum
    Blade, Dominance, Arondight, Avatar''s Parashu, Bracer of The Abyss, Riptalon,
    Transcendence, Ancient Signet, Runeforged Hammer, Gem of Focus, Toxic Blade, The
    Cosmic Horror, Avenging Blade, Triton''s Conch, Rod of Asclepius, Polynomicon.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.5
      win: 0.53
      pick: 0.16
      fit: 0.23
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.69
      win: 0.53
      pick: 0.0
      fit: 0.65
    Spear of Desolation:
      total: 0.54
      efficiency: 0.58
      win: 0.51
      pick: 0.44
      fit: 0.55
    Transcendence:
      total: 0.47
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.32
    Nimble Ring:
      total: 0.5
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.35
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.85
      win: 0.61
      pick: 0.3
      fit: 0.44
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Spear of Desolation
  - Transcendence
  - Nimble Ring
  - Rod of Tahuti
  flex_slots:
  - Book of Thoth
  - Transcendence
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Spear of the Magus,
    Gluttonous Grimoire, Bragi''s Harp, Heartseeker, Hydra''s Lament, Nimble Ring,
    Death Metal, Tyrfing, Lotus Sickle, Doom Orb, Tekko-Kagi, Titan''s Bane, Silverbranch
    Bow, The Crusher, Dreamer''s Idol, Lernaean Bow, The Reaper, Golden Blade, Pendulum
    Blade, Bracer of The Abyss, Ancient Signet, Gem of Focus, Arondight, The Cosmic
    Horror, Avatar''s Parashu, Riptalon, Dominance, Transcendence, Toxic Blade, Runeforged
    Hammer, Rod of Asclepius, Polynomicon, Triton''s Conch, Totem of Death.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.5
      win: 0.53
      pick: 0.16
      fit: 0.28
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.69
      win: 0.53
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.55
      efficiency: 0.58
      win: 0.51
      pick: 0.44
      fit: 0.63
    Transcendence:
      total: 0.46
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.5
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.37
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.85
      win: 0.61
      pick: 0.3
      fit: 0.51
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
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
    Underrated for this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Nimble
    Ring, Lotus Sickle, Dreamer''s Idol, The Cosmic Horror, Bracer of The Abyss, Gem
    of Focus, Ancient Signet, Totem of Death, Rod of Asclepius, Polynomicon, Blood-Bound
    Book, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal
    Staff, Wish-Granting Pearl, Typhon’s Heart.'
  slot_scores:
    Spear of Desolation:
      total: 0.58
      efficiency: 0.58
      win: 0.51
      pick: 0.44
      fit: 0.86
    Doom Orb:
      total: 0.53
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.68
    Spear of the Magus:
      total: 0.55
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.68
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.85
      win: 0.61
      pick: 0.3
      fit: 0.68
    Obsidian Shard:
      total: 0.55
      efficiency: 0.55
      win: 0.5
      pick: 0.3
      fit: 0.78
    Soul Gem:
      total: 0.54
      efficiency: 0.52
      win: 0.44
      pick: 0.25
      fit: 0.96
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
  aspect: Aspect of Combustion
---

---
type: smite-build
god: Nu Wa
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shining Mist
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.67
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.28
    win_rate: 0.81
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.23
      win_rate: 0.52
    - name: Chronos' Pendant
      pick_rate: 0.16
      win_rate: 0.73
  - name: Chronos' Pendant
    pick_rate: 0.23
    win_rate: 0.81
    alternates:
    - name: The World Stone
      pick_rate: 0.16
      win_rate: 0.6
    - name: Spear of Desolation
      pick_rate: 0.13
      win_rate: 0.67
  - name: Soul Gem
    pick_rate: 0.25
    win_rate: 0.64
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.13
      win_rate: 0.75
    - name: The World Stone
      pick_rate: 0.12
      win_rate: 0.91
  - name: Rod of Tahuti
    pick_rate: 0.19
    win_rate: 0.81
    alternates:
    - name: Soul Gem
      pick_rate: 0.14
      win_rate: 0.67
    - name: Soul Reaver
      pick_rate: 0.12
      win_rate: 0.7
  - name: Obsidian Shard
    pick_rate: 0.22
    win_rate: 0.63
    alternates:
    - name: Evil Eye
      pick_rate: 0.16
      win_rate: 0.67
    - name: Rod of Tahuti
      pick_rate: 0.14
      win_rate: 0.6
  - name: Evil Eye
    pick_rate: 0.24
    win_rate: 0.55
    alternates:
    - name: Oracle Staff
      pick_rate: 0.11
      win_rate: 1.0
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.75
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.27
    win_rate: 0.68
  - name: Conduit Gem
    pick_rate: 0.22
    win_rate: 0.65
  - name: Archmage's Gem
    pick_rate: 0.17
    win_rate: 0.81
  source_url: https://smitebrain.com/gods/nu-wa/
  last_verified: '2026-08-27'
  god_win_rate: 0.6881720430107527
  god_matches_won: 64
  god_matches_played: 93
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-27'
  god_matches_analyzed: 2301
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Chronos' Pendant
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
    this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s Idol,
    The Cosmic Horror, Gem of Focus, Ancient Signet, Totem of Death, Rod of Asclepius,
    Polynomicon, Blood-Bound Book, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm
    of Radiance, Ethereal Staff, Staff of Myrddin, Wish-Granting Pearl, Typhon’s Heart,
    Bracer of The Abyss, Nimble Ring.'
  slot_scores:
    Book of Thoth:
      total: 0.62
      efficiency: 0.51
      win: 0.81
      pick: 0.28
      fit: 0.42
    Chronos' Pendant:
      total: 0.67
      efficiency: 0.55
      win: 0.81
      pick: 0.31
      fit: 0.63
    Spear of the Magus:
      total: 0.63
      efficiency: 0.6
      win: 0.67
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.8
      efficiency: 0.86
      win: 0.81
      pick: 0.32
      fit: 0.79
    Obsidian Shard:
      total: 0.63
      efficiency: 0.54
      win: 0.63
      pick: 0.48
      fit: 0.89
    Soul Gem:
      total: 0.64
      efficiency: 0.52
      win: 0.64
      pick: 0.39
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Chronos' Pendant
  - Doom Orb
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Spear
    of the Magus, Doom Orb, Death Metal, Gluttonous Grimoire, Ancient Signet, Dreamer''s
    Idol, Bragi''s Harp, Gem of Focus, Polynomicon, The Cosmic Horror, Rod of Asclepius,
    Bancroft''s Talon, Totem of Death, Triton''s Conch, Blood-Bound Book, Jade Scepter,
    Divine Ruin, Wish-Granting Pearl, Helm of Radiance, Breastplate of Valor, Ethereal
    Staff.'
  slot_scores:
    Book of Thoth:
      total: 0.61
      efficiency: 0.51
      win: 0.81
      pick: 0.28
      fit: 0.39
    Chronos' Pendant:
      total: 0.64
      efficiency: 0.55
      win: 0.81
      pick: 0.31
      fit: 0.43
    Doom Orb:
      total: 0.57
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.77
      efficiency: 0.86
      win: 0.81
      pick: 0.32
      fit: 0.57
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.63
      pick: 0.48
      fit: 0.57
    Soul Gem:
      total: 0.6
      efficiency: 0.52
      win: 0.64
      pick: 0.39
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Chronos' Pendant
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
    god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s Idol, Death
    Metal, Gem of Focus, The Cosmic Horror, Ancient Signet, Bragi''s Harp, Totem of
    Death, Rod of Asclepius, Polynomicon, Blood-Bound Book, Jade Scepter, Divine Ruin,
    Triton''s Conch, Breastplate of Valor, Bancroft''s Talon, Genji''s Guard, Helm
    of Radiance, Ethereal Staff.'
  slot_scores:
    Book of Thoth:
      total: 0.59
      efficiency: 0.51
      win: 0.81
      pick: 0.28
      fit: 0.22
    Chronos' Pendant:
      total: 0.64
      efficiency: 0.55
      win: 0.81
      pick: 0.31
      fit: 0.44
    Spear of the Magus:
      total: 0.6
      efficiency: 0.6
      win: 0.67
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.76
      efficiency: 0.86
      win: 0.81
      pick: 0.32
      fit: 0.56
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.63
      pick: 0.48
      fit: 0.66
    Soul Gem:
      total: 0.62
      efficiency: 0.52
      win: 0.64
      pick: 0.39
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Chronos' Pendant
  - Kinetic Cuirass
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Book of Thoth
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
    of Negation, Erosion, Yogi''s Necklace, Eye of Providence, Draconic Scale, Phoenix
    Feather, Jade Scepter, Chandra''s Grace, Wish-Granting Pearl, Blood-Bound Book,
    Doom Orb, Glorious Pridwen.'
  slot_scores:
    Book of Thoth:
      total: 0.59
      efficiency: 0.51
      win: 0.81
      pick: 0.28
      fit: 0.21
    Chronos' Pendant:
      total: 0.62
      efficiency: 0.55
      win: 0.81
      pick: 0.31
      fit: 0.31
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.61
    Rod of Tahuti:
      total: 0.74
      efficiency: 0.86
      win: 0.81
      pick: 0.32
      fit: 0.39
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.62
      efficiency: 0.52
      win: 0.64
      pick: 0.39
      fit: 0.89
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Chronos' Pendant
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Soul Gem
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
    The Cosmic Horror, Ancient Signet, Gem of Focus, Rod of Asclepius, Totem of Death,
    Polynomicon, Blood-Bound Book, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm
    of Radiance, Ethereal Staff, Screeching Gargoyle, Wish-Granting Pearl, Typhon’s
    Heart, Breastplate of Valor, Bracer of The Abyss.'
  slot_scores:
    Book of Thoth:
      total: 0.6
      efficiency: 0.51
      win: 0.81
      pick: 0.28
      fit: 0.3
    Chronos' Pendant:
      total: 0.64
      efficiency: 0.55
      win: 0.81
      pick: 0.31
      fit: 0.44
    Spear of the Magus:
      total: 0.64
      efficiency: 0.6
      win: 0.67
      pick: 0.0
      fit: 0.85
    Rod of Tahuti:
      total: 0.81
      efficiency: 0.86
      win: 0.81
      pick: 0.32
      fit: 0.85
    Obsidian Shard:
      total: 0.64
      efficiency: 0.54
      win: 0.63
      pick: 0.48
      fit: 0.95
    Soul Gem:
      total: 0.64
      efficiency: 0.52
      win: 0.64
      pick: 0.39
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Book of Thoth
  - Chronos' Pendant
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
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
    Bracer of The Abyss, Doom Orb, Ancient Signet, Blood-Bound Book, Dreamer''s Idol,
    Death Metal, Bancroft''s Talon, Gem of Focus, Rod of Asclepius, The Cosmic Horror,
    Typhon’s Heart, Polynomicon, Totem of Death, Jade Scepter, Divine Ruin, Helm of
    Radiance, Daybreak Gavel.'
  slot_scores:
    Book of Thoth:
      total: 0.58
      efficiency: 0.51
      win: 0.81
      pick: 0.28
      fit: 0.17
    Chronos' Pendant:
      total: 0.61
      efficiency: 0.55
      win: 0.81
      pick: 0.31
      fit: 0.25
    Bracer of The Abyss:
      total: 0.54
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.6
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.55
      efficiency: 0.44
      win: 0.67
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.73
      efficiency: 0.86
      win: 0.81
      pick: 0.32
      fit: 0.32
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Chronos' Pendant
  - Gem of Focus
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
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
    + fit + win/pick). Underrated for this god: Gem of Focus, Spear of the Magus,
    Gluttonous Grimoire, Totem of Death, Doom Orb, Breastplate of Valor, Dreamer''s
    Idol, Genji''s Guard, Ancient Signet, Death Metal, Staff of Myrddin, The Cosmic
    Horror, Eye of Erebus, Screeching Gargoyle, Bragi''s Harp, Rod of Asclepius, Chandra''s
    Grace, Freya''s Tears, Polynomicon, Blood-Bound Book, Jade Scepter.'
  slot_scores:
    Book of Thoth:
      total: 0.58
      efficiency: 0.51
      win: 0.81
      pick: 0.28
      fit: 0.14
    Chronos' Pendant:
      total: 0.67
      efficiency: 0.55
      win: 0.81
      pick: 0.31
      fit: 0.63
    Gem of Focus:
      total: 0.57
      efficiency: 0.5
      win: 0.67
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.52
      pick: 0.23
      fit: 0.86
    Rod of Tahuti:
      total: 0.74
      efficiency: 0.86
      win: 0.81
      pick: 0.32
      fit: 0.37
    Soul Gem:
      total: 0.63
      efficiency: 0.52
      win: 0.64
      pick: 0.39
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Book of Thoth
  - Chronos' Pendant
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
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
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Spear of the Magus, Heartseeker,
    Bragi''s Harp, Tyrfing, Hydra''s Lament, Tekko-Kagi, Lernaean Bow, Nimble Ring,
    Death Metal, Titan''s Bane, The Crusher, Gluttonous Grimoire, Silverbranch Bow,
    The Reaper, Doom Orb, Golden Blade, Pendulum Blade, Dreamer''s Idol, Arondight,
    Dominance, Avatar''s Parashu, Bracer of The Abyss, Ancient Signet, Transcendence,
    Riptalon, Runeforged Hammer, Gem of Focus, Toxic Blade, The Cosmic Horror, Avenging
    Blade, Triton''s Conch, Rod of Asclepius, Polynomicon, Totem of Death.'
  slot_scores:
    Book of Thoth:
      total: 0.59
      efficiency: 0.51
      win: 0.81
      pick: 0.28
      fit: 0.23
    Chronos' Pendant:
      total: 0.62
      efficiency: 0.55
      win: 0.81
      pick: 0.31
      fit: 0.34
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.65
    Transcendence:
      total: 0.53
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.32
    Rod of Tahuti:
      total: 0.75
      efficiency: 0.86
      win: 0.81
      pick: 0.32
      fit: 0.44
    Soul Gem:
      total: 0.59
      efficiency: 0.52
      win: 0.64
      pick: 0.39
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Chronos' Pendant
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Soul Gem
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
    Heartseeker, Gluttonous Grimoire, Hydra''s Lament, Death Metal, Doom Orb, Titan''s
    Bane, The Crusher, Dreamer''s Idol, The Reaper, Pendulum Blade, Bragi''s Harp,
    Ancient Signet, Avatar''s Parashu, Arondight, Gem of Focus, The Cosmic Horror,
    Tyrfing, Transcendence, Tekko-Kagi, Runeforged Hammer, Rod of Asclepius, Triton''s
    Conch, Polynomicon, Totem of Death, Avenging Blade, Blood-Bound Book, Jade Scepter,
    Divine Ruin, Bancroft''s Talon, Golden Blade, Silverbranch Bow, Helm of Radiance.'
  slot_scores:
    Book of Thoth:
      total: 0.6
      efficiency: 0.51
      win: 0.81
      pick: 0.28
      fit: 0.31
    Chronos' Pendant:
      total: 0.64
      efficiency: 0.55
      win: 0.81
      pick: 0.31
      fit: 0.44
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.69
    Transcendence:
      total: 0.53
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.31
    Rod of Tahuti:
      total: 0.76
      efficiency: 0.86
      win: 0.81
      pick: 0.32
      fit: 0.56
    Soul Gem:
      total: 0.61
      efficiency: 0.52
      win: 0.64
      pick: 0.39
      fit: 0.79
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
    Idol, The Cosmic Horror, Gem of Focus, Ancient Signet, Totem of Death, Rod of
    Asclepius, Polynomicon, Blood-Bound Book, Jade Scepter, Divine Ruin, Bancroft''s
    Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin, Wish-Granting Pearl,
    Typhon’s Heart, Bracer of The Abyss, Nimble Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.52
      pick: 0.23
      fit: 1.0
    Doom Orb:
      total: 0.6
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.63
      efficiency: 0.6
      win: 0.67
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.8
      efficiency: 0.86
      win: 0.81
      pick: 0.32
      fit: 0.79
    Obsidian Shard:
      total: 0.63
      efficiency: 0.54
      win: 0.63
      pick: 0.48
      fit: 0.89
    Soul Gem:
      total: 0.64
      efficiency: 0.52
      win: 0.64
      pick: 0.39
      fit: 1.0
  starter: *id001
---

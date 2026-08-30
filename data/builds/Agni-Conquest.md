---
type: smite-build
god: Agni
mode: Conquest
builds:
- source: community
  aspect: Aspect of Combustion
  aspect_pick_rate: 0.02
  aspect_win_rate: 0.64
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.35
    win_rate: 0.62
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.33
      win_rate: 0.48
    - name: Book of Thoth
      pick_rate: 0.11
      win_rate: 0.51
  - name: The World Stone
    pick_rate: 0.24
    win_rate: 0.58
    alternates:
    - name: Soul Reaver
      pick_rate: 0.21
      win_rate: 0.52
    - name: Spear of Desolation
      pick_rate: 0.15
      win_rate: 0.59
  - name: Soul Reaver
    pick_rate: 0.15
    win_rate: 0.51
    alternates:
    - name: The World Stone
      pick_rate: 0.14
      win_rate: 0.6
    - name: Soul Gem
      pick_rate: 0.14
      win_rate: 0.55
  - name: Rod of Tahuti
    pick_rate: 0.26
    win_rate: 0.59
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.21
      win_rate: 0.62
    - name: Soul Reaver
      pick_rate: 0.08
      win_rate: 0.67
  - name: Obsidian Shard
    pick_rate: 0.23
    win_rate: 0.53
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.13
      win_rate: 0.69
    - name: Evil Eye
      pick_rate: 0.13
      win_rate: 0.47
  - name: Evil Eye
    pick_rate: 0.15
    win_rate: 0.53
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.55
    - name: Obsidian Shard
      pick_rate: 0.08
      win_rate: 0.81
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.43
    win_rate: 0.63
  - name: Bluestone Pendant
    pick_rate: 0.25
    win_rate: 0.44
  - name: Archmage's Gem
    pick_rate: 0.11
    win_rate: 0.62
  source_url: https://smitebrain.com/gods/agni/
  last_verified: '2026-08-30'
  god_win_rate: 0.5654362416107382
  god_matches_won: 337
  god_matches_played: 596
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-30'
  god_matches_analyzed: 5563
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The World Stone
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
    this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s Idol,
    The Cosmic Horror, Gem of Focus, Ancient Signet, Totem of Death, Rod of Asclepius,
    Polynomicon, Book of Thoth, Blood-Bound Book, Jade Scepter, Divine Ruin, Bancroft''s
    Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin, Wish-Granting Pearl,
    Typhon’s Heart, Bracer of The Abyss, Nimble Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.65
      efficiency: 0.57
      win: 0.62
      pick: 0.35
      fit: 1.0
    Spear of the Magus:
      total: 0.57
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.79
    The World Stone:
      total: 0.58
      efficiency: 0.52
      win: 0.58
      pick: 0.33
      fit: 0.79
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.79
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.53
      pick: 0.5
      fit: 0.89
    Soul Gem:
      total: 0.59
      efficiency: 0.52
      win: 0.55
      pick: 0.22
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - The World Stone
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
    Idol, Bragi''s Harp, Gem of Focus, Polynomicon, Book of Thoth, The Cosmic Horror,
    Rod of Asclepius, Bancroft''s Talon, Totem of Death, Triton''s Conch, Blood-Bound
    Book, Jade Scepter, Divine Ruin, Wish-Granting Pearl, Helm of Radiance, Breastplate
    of Valor, Ethereal Staff.'
  slot_scores:
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.62
      pick: 0.35
      fit: 0.61
    Doom Orb:
      total: 0.51
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.57
    The World Stone:
      total: 0.54
      efficiency: 0.52
      win: 0.58
      pick: 0.33
      fit: 0.57
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.57
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.53
      pick: 0.5
      fit: 0.57
    Soul Gem:
      total: 0.55
      efficiency: 0.52
      win: 0.55
      pick: 0.22
      fit: 0.71
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
  - The World Stone
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
    god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s Idol, Death
    Metal, Gem of Focus, The Cosmic Horror, Ancient Signet, Bragi''s Harp, Totem of
    Death, Rod of Asclepius, Polynomicon, Book of Thoth, Blood-Bound Book, Jade Scepter,
    Divine Ruin, Triton''s Conch, Breastplate of Valor, Bancroft''s Talon, Genji''s
    Guard, Helm of Radiance, Ethereal Staff.'
  slot_scores:
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.62
      pick: 0.35
      fit: 0.78
    Spear of the Magus:
      total: 0.53
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.56
    The World Stone:
      total: 0.54
      efficiency: 0.52
      win: 0.58
      pick: 0.33
      fit: 0.56
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.56
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.53
      pick: 0.5
      fit: 0.66
    Soul Gem:
      total: 0.57
      efficiency: 0.52
      win: 0.55
      pick: 0.22
      fit: 0.88
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
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.62
      pick: 0.35
      fit: 0.49
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.39
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.53
      pick: 0.5
      fit: 0.49
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.57
      efficiency: 0.52
      win: 0.55
      pick: 0.22
      fit: 0.89
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The World Stone
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
    for this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s Idol,
    The Cosmic Horror, Ancient Signet, Gem of Focus, Rod of Asclepius, Totem of Death,
    Polynomicon, Book of Thoth, Blood-Bound Book, Jade Scepter, Divine Ruin, Bancroft''s
    Talon, Helm of Radiance, Ethereal Staff, Screeching Gargoyle, Wish-Granting Pearl,
    Typhon’s Heart, Breastplate of Valor, Bracer of The Abyss.'
  slot_scores:
    Spear of Desolation:
      total: 0.65
      efficiency: 0.57
      win: 0.62
      pick: 0.35
      fit: 1.0
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.85
    The World Stone:
      total: 0.59
      efficiency: 0.52
      win: 0.58
      pick: 0.33
      fit: 0.85
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.85
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.53
      pick: 0.5
      fit: 0.95
    Soul Gem:
      total: 0.59
      efficiency: 0.52
      win: 0.55
      pick: 0.22
      fit: 1.0
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
    this god: Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Bragi''s Harp,
    Bracer of The Abyss, Doom Orb, Ancient Signet, Blood-Bound Book, Dreamer''s Idol,
    Death Metal, Bancroft''s Talon, Gem of Focus, Rod of Asclepius, The Cosmic Horror,
    Typhon’s Heart, Polynomicon, Book of Thoth, Totem of Death, Jade Scepter, Divine
    Ruin, Helm of Radiance, Daybreak Gavel.'
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
    Bragi's Harp:
      total: 0.49
      efficiency: 0.44
      win: 0.53
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.62
      pick: 0.35
      fit: 0.4
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.32
    Soul Gem:
      total: 0.54
      efficiency: 0.57
      win: 0.55
      pick: 0.22
      fit: 0.58
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
  - Chronos' Pendant
  - The World Stone
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
    Grace, Freya''s Tears, Polynomicon, Book of Thoth, Blood-Bound Book, Jade Scepter.'
  slot_scores:
    Chronos' Pendant:
      total: 0.52
      efficiency: 0.55
      win: 0.48
      pick: 0.33
      fit: 0.63
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.62
      pick: 0.35
      fit: 0.86
    The World Stone:
      total: 0.51
      efficiency: 0.52
      win: 0.58
      pick: 0.33
      fit: 0.37
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.37
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.53
      pick: 0.5
      fit: 0.47
    Soul Gem:
      total: 0.58
      efficiency: 0.52
      win: 0.55
      pick: 0.22
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - The World Stone
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
    Tyrfing, Bragi''s Harp, Hydra''s Lament, Tekko-Kagi, Lernaean Bow, Nimble Ring,
    Death Metal, Titan''s Bane, The Crusher, Gluttonous Grimoire, Silverbranch Bow,
    The Reaper, Golden Blade, Doom Orb, Pendulum Blade, Dreamer''s Idol, Arondight,
    Dominance, Avatar''s Parashu, Bracer of The Abyss, Ancient Signet, Riptalon, Transcendence,
    Runeforged Hammer, Gem of Focus, Toxic Blade, The Cosmic Horror, Avenging Blade,
    Triton''s Conch, Rod of Asclepius, Polynomicon, Book of Thoth, Totem of Death.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.65
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.62
      pick: 0.35
      fit: 0.55
    The World Stone:
      total: 0.52
      efficiency: 0.52
      win: 0.58
      pick: 0.33
      fit: 0.44
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.44
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.53
      pick: 0.5
      fit: 0.54
    Soul Gem:
      total: 0.54
      efficiency: 0.52
      win: 0.55
      pick: 0.22
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Spear of the Magus,
    Heartseeker, Gluttonous Grimoire, Hydra''s Lament, Death Metal, Doom Orb, Titan''s
    Bane, The Crusher, Dreamer''s Idol, The Reaper, Pendulum Blade, Bragi''s Harp,
    Ancient Signet, Avatar''s Parashu, Tyrfing, Arondight, Gem of Focus, The Cosmic
    Horror, Transcendence, Tekko-Kagi, Runeforged Hammer, Rod of Asclepius, Triton''s
    Conch, Polynomicon, Book of Thoth, Totem of Death, Avenging Blade, Blood-Bound
    Book, Jade Scepter, Divine Ruin, Golden Blade, Bancroft''s Talon, Silverbranch
    Bow, Helm of Radiance.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.51
      win: 0.51
      pick: 0.11
      fit: 0.31
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.69
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.31
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.62
      pick: 0.35
      fit: 0.69
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.56
    Soul Gem:
      total: 0.56
      efficiency: 0.52
      win: 0.55
      pick: 0.22
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
    Asclepius, Book of Thoth, Polynomicon, Blood-Bound Book, Jade Scepter, Divine
    Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin, Wish-Granting
    Pearl, Typhon’s Heart, Bracer of The Abyss, Nimble Ring.'
  slot_scores:
    Spear of Desolation:
      total: 0.65
      efficiency: 0.57
      win: 0.62
      pick: 0.35
      fit: 1.0
    Doom Orb:
      total: 0.54
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.57
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.79
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.53
      pick: 0.5
      fit: 0.89
    Soul Gem:
      total: 0.59
      efficiency: 0.52
      win: 0.55
      pick: 0.22
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Nimble Ring, Dreamer''s
    Idol, The Cosmic Horror, Bracer of The Abyss, Gem of Focus, Ancient Signet, Totem
    of Death, Rod of Asclepius, Polynomicon, Book of Thoth, Blood-Bound Book, Jade
    Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Wish-Granting
    Pearl, Staff of Myrddin, Typhon’s Heart.'
  slot_scores:
    Nimble Ring:
      total: 0.52
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.5
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.62
      pick: 0.35
      fit: 0.86
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.68
    The World Stone:
      total: 0.56
      efficiency: 0.52
      win: 0.58
      pick: 0.33
      fit: 0.68
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.68
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.53
      pick: 0.5
      fit: 0.78
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: mana-stack
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Doom Orb
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Doom Orb
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Spear
    of the Magus, Doom Orb, Bragi''s Harp, Nimble Ring, Death Metal, Gluttonous Grimoire,
    Ancient Signet, Dreamer''s Idol, Gem of Focus, Bracer of The Abyss, Polynomicon,
    Book of Thoth, The Cosmic Horror, Rod of Asclepius, Bancroft''s Talon, Totem of
    Death, Triton''s Conch, Blood-Bound Book, Jade Scepter, Divine Ruin, Wish-Granting
    Pearl, Helm of Radiance.'
  slot_scores:
    Nimble Ring:
      total: 0.5
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.34
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.62
      pick: 0.35
      fit: 0.57
    Doom Orb:
      total: 0.5
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.53
    The World Stone:
      total: 0.54
      efficiency: 0.52
      win: 0.58
      pick: 0.33
      fit: 0.53
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.53
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.53
      pick: 0.5
      fit: 0.53
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: burst
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s Idol, Nimble
    Ring, Bragi''s Harp, Death Metal, Gem of Focus, The Cosmic Horror, Ancient Signet,
    Bracer of The Abyss, Totem of Death, Rod of Asclepius, Polynomicon, Book of Thoth,
    Blood-Bound Book, Jade Scepter, Divine Ruin, Breastplate of Valor, Triton''s Conch,
    Bancroft''s Talon, Genji''s Guard.'
  slot_scores:
    Nimble Ring:
      total: 0.49
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.29
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.62
      pick: 0.35
      fit: 0.71
    Spear of the Magus:
      total: 0.53
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.51
    The World Stone:
      total: 0.54
      efficiency: 0.52
      win: 0.58
      pick: 0.33
      fit: 0.51
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.51
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.53
      pick: 0.5
      fit: 0.61
  starter: *id001
  aspect: Aspect of Combustion
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
    Kinetic Cuirass, Ethereal Staff, Freya''s Tears, Genji''s Guard, Spear of the
    Magus, Breastplate of Valor, Shifter''s Shield, Lifebinder, Helm of Radiance,
    Sphere of Negation, Yogi''s Necklace, Erosion, Nimble Ring, Eye of Providence,
    Phoenix Feather, Draconic Scale, Chandra''s Grace, Jade Scepter, Wish-Granting
    Pearl, Blood-Bound Book, Doom Orb.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.57
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.62
      pick: 0.35
      fit: 0.46
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.36
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.53
      pick: 0.5
      fit: 0.46
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.77
    Soul Gem:
      total: 0.57
      efficiency: 0.52
      win: 0.55
      pick: 0.22
      fit: 0.86
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The World Stone
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
    for this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s Idol,
    The Cosmic Horror, Nimble Ring, Ancient Signet, Bracer of The Abyss, Gem of Focus,
    Rod of Asclepius, Polynomicon, Book of Thoth, Totem of Death, Blood-Bound Book,
    Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance, Screeching Gargoyle,
    Ethereal Staff, Wish-Granting Pearl, Typhon’s Heart.'
  slot_scores:
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.62
      pick: 0.35
      fit: 0.9
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.77
    The World Stone:
      total: 0.57
      efficiency: 0.52
      win: 0.58
      pick: 0.33
      fit: 0.77
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.77
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.53
      pick: 0.5
      fit: 0.87
    Soul Gem:
      total: 0.59
      efficiency: 0.52
      win: 0.55
      pick: 0.22
      fit: 1.0
  starter: *id001
  aspect: Aspect of Combustion
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
    this god: Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Bragi''s Harp,
    Bracer of The Abyss, Doom Orb, Ancient Signet, Blood-Bound Book, Dreamer''s Idol,
    Death Metal, Bancroft''s Talon, Gem of Focus, Rod of Asclepius, The Cosmic Horror,
    Typhon’s Heart, Polynomicon, Book of Thoth, Totem of Death, Jade Scepter, Divine
    Ruin, Helm of Radiance, Daybreak Gavel.'
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
    Bragi's Harp:
      total: 0.49
      efficiency: 0.44
      win: 0.53
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.62
      pick: 0.35
      fit: 0.4
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.32
    Soul Gem:
      total: 0.54
      efficiency: 0.57
      win: 0.55
      pick: 0.22
      fit: 0.58
  starter: *id001
  aspect: Aspect of Combustion
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
  - Chronos' Pendant
  - The World Stone
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
    + fit + win/pick). Underrated for this god: Spear of the Magus, Gem of Focus,
    Gluttonous Grimoire, Nimble Ring, Totem of Death, Doom Orb, Breastplate of Valor,
    Dreamer''s Idol, Genji''s Guard, Bragi''s Harp, Ancient Signet, Death Metal, Bracer
    of The Abyss, The Cosmic Horror, Staff of Myrddin, Eye of Erebus, Rod of Asclepius,
    Screeching Gargoyle, Polynomicon, Book of Thoth, Chandra''s Grace, Freya''s Tears,
    Blood-Bound Book.'
  slot_scores:
    Chronos' Pendant:
      total: 0.51
      efficiency: 0.55
      win: 0.48
      pick: 0.33
      fit: 0.57
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.62
      pick: 0.35
      fit: 0.78
    The World Stone:
      total: 0.51
      efficiency: 0.52
      win: 0.58
      pick: 0.33
      fit: 0.34
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.34
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.53
      pick: 0.5
      fit: 0.44
    Soul Gem:
      total: 0.57
      efficiency: 0.52
      win: 0.55
      pick: 0.22
      fit: 0.88
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - The World Stone
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
    Tyrfing, Bragi''s Harp, Hydra''s Lament, Tekko-Kagi, Lernaean Bow, Nimble Ring,
    Death Metal, Titan''s Bane, The Crusher, Gluttonous Grimoire, Silverbranch Bow,
    The Reaper, Golden Blade, Doom Orb, Pendulum Blade, Dreamer''s Idol, Arondight,
    Dominance, Avatar''s Parashu, Bracer of The Abyss, Ancient Signet, Riptalon, Transcendence,
    Runeforged Hammer, Gem of Focus, Toxic Blade, The Cosmic Horror, Avenging Blade,
    Triton''s Conch, Rod of Asclepius, Polynomicon, Book of Thoth, Totem of Death.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.65
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.62
      pick: 0.35
      fit: 0.55
    The World Stone:
      total: 0.52
      efficiency: 0.52
      win: 0.58
      pick: 0.33
      fit: 0.44
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.44
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.53
      pick: 0.5
      fit: 0.54
    Soul Gem:
      total: 0.54
      efficiency: 0.52
      win: 0.55
      pick: 0.22
      fit: 0.65
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - The World Stone
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
    Heartseeker, Gluttonous Grimoire, Bragi''s Harp, Hydra''s Lament, Nimble Ring,
    Tyrfing, Death Metal, Doom Orb, Tekko-Kagi, Titan''s Bane, Silverbranch Bow, The
    Crusher, Dreamer''s Idol, Lernaean Bow, The Reaper, Ancient Signet, Golden Blade,
    Pendulum Blade, Bracer of The Abyss, Arondight, Gem of Focus, Avatar''s Parashu,
    Riptalon, The Cosmic Horror, Dominance, Transcendence, Toxic Blade, Runeforged
    Hammer, Rod of Asclepius, Polynomicon, Book of Thoth, Triton''s Conch, Totem of
    Death, Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.62
      pick: 0.35
      fit: 0.63
    The World Stone:
      total: 0.53
      efficiency: 0.52
      win: 0.58
      pick: 0.33
      fit: 0.51
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.51
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.53
      pick: 0.5
      fit: 0.61
    Soul Gem:
      total: 0.55
      efficiency: 0.52
      win: 0.55
      pick: 0.22
      fit: 0.73
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
    Ring, Dreamer''s Idol, The Cosmic Horror, Bracer of The Abyss, Gem of Focus, Ancient
    Signet, Totem of Death, Rod of Asclepius, Book of Thoth, Polynomicon, Blood-Bound
    Book, Jade Scepter, Divine Ruin, Bancroft''s Talon, Helm of Radiance, Ethereal
    Staff, Wish-Granting Pearl, Staff of Myrddin, Typhon’s Heart.'
  slot_scores:
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.62
      pick: 0.35
      fit: 0.86
    Doom Orb:
      total: 0.53
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.68
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.68
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.59
      pick: 0.43
      fit: 0.68
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.53
      pick: 0.5
      fit: 0.78
    Soul Gem:
      total: 0.58
      efficiency: 0.52
      win: 0.55
      pick: 0.22
      fit: 0.96
  starter: *id001
  aspect: Aspect of Combustion
---

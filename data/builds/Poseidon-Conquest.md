---
type: smite-build
god: Poseidon
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Trident
  aspect_pick_rate: 0.5
  aspect_win_rate: 0.0
  slot_order:
  - name: Gem of Focus
    pick_rate: 0.5
    win_rate: 1.0
    alternates:
    - name: Tyrfing
      pick_rate: 0.5
      win_rate: 0.0
  - name: The World Stone
    pick_rate: 0.5
    win_rate: 1.0
    alternates:
    - name: Bragi's Harp
      pick_rate: 0.5
      win_rate: 0.0
  - name: Rod of Tahuti
    pick_rate: 0.5
    win_rate: 1.0
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.5
      win_rate: 0.0
  - name: Obsidian Shard
    pick_rate: 0.5
    win_rate: 1.0
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.5
      win_rate: 0.0
  - name: Nimble Ring
    pick_rate: 0.5
    win_rate: 1.0
    alternates:
    - name: The Executioner
      pick_rate: 0.5
      win_rate: 0.0
  - name: Mote of Chaos
    pick_rate: 0.5
    win_rate: 1.0
    alternates:
    - name: Hussar's Wings
      pick_rate: 0.5
      win_rate: 0.0
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.5
    win_rate: 1.0
  - name: Hunter's Cowl
    pick_rate: 0.5
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/poseidon/
  last_verified: '2026-11-04'
  god_win_rate: 0.5
  god_matches_won: 1
  god_matches_played: 2
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-04'
  god_matches_analyzed: 149
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Gem of Focus
  - The World Stone
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Nimble Ring
  flex_slots:
  - Nimble Ring
  - Spear of Desolation
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
    this god: Spear of Desolation, Soul Gem, Spear of the Magus, Gluttonous Grimoire,
    Doom Orb, Dreamer''s Idol, Chronos'' Pendant, The Cosmic Horror, Ancient Signet,
    Heartwood Charm, Blood-Bound Book, Polynomicon, Totem of Death, Soul Reaver, Book
    of Thoth, Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm of Radiance, Ethereal
    Staff, Staff of Myrddin, Typhon’s Heart, Alchemist Coat, Bracer of The Abyss,
    Death Metal.'
  slot_scores:
    Gem of Focus:
      total: 0.75
      efficiency: 0.5
      win: 1.0
      pick: 0.5
      fit: 0.63
    The World Stone:
      total: 0.79
      efficiency: 0.52
      win: 1.0
      pick: 0.68
      fit: 0.79
    Spear of Desolation:
      total: 0.58
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
    Rod of Tahuti:
      total: 0.91
      efficiency: 0.86
      win: 1.0
      pick: 0.78
      fit: 0.79
    Obsidian Shard:
      total: 0.83
      efficiency: 0.58
      win: 1.0
      pick: 0.83
      fit: 0.89
    Nimble Ring:
      total: 0.7
      efficiency: 0.38
      win: 1.0
      pick: 1.0
      fit: 0.42
  community_ordered:
  - Gem of Focus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Nimble Ring
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Gem of Focus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Nimble Ring
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
    of Desolation, Soul Gem, Death Metal, Doom Orb, Spear of the Magus, Ancient Signet,
    Gluttonous Grimoire, Chronos'' Pendant, Heartwood Charm, Dreamer''s Idol, Polynomicon,
    Soul Reaver, Blood-Bound Book, The Cosmic Horror, Book of Thoth, Bancroft''s Talon,
    Triton''s Conch, Totem of Death, Divine Ruin, Jade Scepter, Genji''s Guard, Helm
    of Radiance, Ethereal Staff, Wish-Granting Pearl.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.39
    Gem of Focus:
      total: 0.72
      efficiency: 0.5
      win: 1.0
      pick: 0.5
      fit: 0.43
    The World Stone:
      total: 0.75
      efficiency: 0.52
      win: 1.0
      pick: 0.68
      fit: 0.57
    Rod of Tahuti:
      total: 0.88
      efficiency: 0.86
      win: 1.0
      pick: 0.78
      fit: 0.57
    Obsidian Shard:
      total: 0.78
      efficiency: 0.58
      win: 1.0
      pick: 0.83
      fit: 0.57
    Nimble Ring:
      total: 0.68
      efficiency: 0.38
      win: 1.0
      pick: 1.0
      fit: 0.29
  community_ordered:
  - Gem of Focus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Nimble Ring
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Gem of Focus
  - The World Stone
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Nimble Ring
  flex_slots:
  - Nimble Ring
  - Spear of Desolation
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
    god: Spear of Desolation, Soul Gem, Spear of the Magus, Gluttonous Grimoire, Doom
    Orb, Dreamer''s Idol, Chronos'' Pendant, Death Metal, Ancient Signet, The Cosmic
    Horror, Heartwood Charm, Blood-Bound Book, Polynomicon, Totem of Death, Soul Reaver,
    Book of Thoth, Damaru, Divine Ruin, Jade Scepter, Genji''s Guard, Triton''s Conch,
    Bancroft''s Talon, Helm of Radiance, Ethereal Staff.'
  slot_scores:
    Gem of Focus:
      total: 0.72
      efficiency: 0.5
      win: 1.0
      pick: 0.5
      fit: 0.44
    The World Stone:
      total: 0.75
      efficiency: 0.52
      win: 1.0
      pick: 0.68
      fit: 0.56
    Spear of Desolation:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.78
    Rod of Tahuti:
      total: 0.87
      efficiency: 0.86
      win: 1.0
      pick: 0.78
      fit: 0.56
    Obsidian Shard:
      total: 0.79
      efficiency: 0.58
      win: 1.0
      pick: 0.83
      fit: 0.66
    Nimble Ring:
      total: 0.67
      efficiency: 0.38
      win: 1.0
      pick: 1.0
      fit: 0.22
  community_ordered:
  - Gem of Focus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Nimble Ring
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Gem of Focus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Nimble Ring
  - Amanita Charm
  flex_slots:
  - Nimble Ring
  - Amanita Charm
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
    this god: Amanita Charm, Soul Gem, Shield of the Phoenix, Gluttonous Grimoire,
    Kinetic Cuirass, Ethereal Staff, Spear of Desolation, Genji''s Guard, Phoenix
    Feather, Blood-Bound Book, Freya''s Tears, Yogi''s Necklace, Helm of Radiance,
    Sphere of Negation, Helm of Darkness, Spear of the Magus, Breastplate of Valor,
    Erosion, Oni Hunter''s Garb, Eye of Providence, Chandra''s Grace, Jade Scepter,
    Draconic Scale, Midgardian Mail, Doom Orb, Ancient Signet, Regrowth Striders.'
  slot_scores:
    Gem of Focus:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.5
      fit: 0.31
    The World Stone:
      total: 0.73
      efficiency: 0.52
      win: 1.0
      pick: 0.68
      fit: 0.39
    Rod of Tahuti:
      total: 0.85
      efficiency: 0.86
      win: 1.0
      pick: 0.78
      fit: 0.39
    Obsidian Shard:
      total: 0.77
      efficiency: 0.58
      win: 1.0
      pick: 0.83
      fit: 0.49
    Nimble Ring:
      total: 0.67
      efficiency: 0.38
      win: 1.0
      pick: 1.0
      fit: 0.21
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.81
  community_ordered:
  - Gem of Focus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Nimble Ring
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Gem of Focus
  - The World Stone
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Nimble Ring
  flex_slots:
  - Nimble Ring
  - Spear of Desolation
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
    for this god: Spear of Desolation, Soul Gem, Spear of the Magus, Gluttonous Grimoire,
    Doom Orb, Dreamer''s Idol, The Cosmic Horror, Chronos'' Pendant, Ancient Signet,
    Heartwood Charm, Blood-Bound Book, Polynomicon, Totem of Death, Soul Reaver, Book
    of Thoth, Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm of Radiance, Ethereal
    Staff, Screeching Gargoyle, Typhon’s Heart, Genji''s Guard, Alchemist Coat, Staff
    of Myrddin.'
  slot_scores:
    Gem of Focus:
      total: 0.72
      efficiency: 0.5
      win: 1.0
      pick: 0.5
      fit: 0.44
    The World Stone:
      total: 0.8
      efficiency: 0.52
      win: 1.0
      pick: 0.68
      fit: 0.85
    Spear of Desolation:
      total: 0.58
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
    Rod of Tahuti:
      total: 0.92
      efficiency: 0.86
      win: 1.0
      pick: 0.78
      fit: 0.85
    Obsidian Shard:
      total: 0.84
      efficiency: 0.58
      win: 1.0
      pick: 0.83
      fit: 0.95
    Nimble Ring:
      total: 0.68
      efficiency: 0.38
      win: 1.0
      pick: 1.0
      fit: 0.3
  community_ordered:
  - Gem of Focus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Nimble Ring
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Bragi's Harp
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Nimble Ring
  flex_slots:
  - Bracer of The Abyss
  - Bragi's Harp
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
    this god: Soul Gem, Spear of Desolation, Gluttonous Grimoire, Spear of the Magus,
    Blood-Bound Book, Bracer of The Abyss, Ancient Signet, Death Metal, Doom Orb,
    Chronos'' Pendant, Dreamer''s Idol, Bancroft''s Talon, Polynomicon, Heartwood
    Charm, The Cosmic Horror, Typhon’s Heart, Soul Reaver, Book of Thoth, Divine Ruin,
    Jade Scepter, Totem of Death, Damaru, Helm of Radiance.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.4
    Bragi's Harp:
      total: 0.28
      efficiency: 0.45
      win: 0.0
      pick: 0.68
      fit: 0.63
    The World Stone:
      total: 0.72
      efficiency: 0.52
      win: 1.0
      pick: 0.68
      fit: 0.32
    Rod of Tahuti:
      total: 0.84
      efficiency: 0.86
      win: 1.0
      pick: 0.78
      fit: 0.32
    Obsidian Shard:
      total: 0.76
      efficiency: 0.58
      win: 1.0
      pick: 0.83
      fit: 0.42
    Nimble Ring:
      total: 0.79
      efficiency: 0.63
      win: 1.0
      pick: 1.0
      fit: 0.48
  community_ordered:
  - Bragi's Harp
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Nimble Ring
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Gem of Focus
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of Desolation
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Spear of Desolation, Soul Gem, Chronos''
    Pendant, Heartwood Charm, Spear of the Magus, Totem of Death, Gluttonous Grimoire,
    Damaru, Doom Orb, Genji''s Guard, Death Metal, Ancient Signet, Dreamer''s Idol,
    Breastplate of Valor, Chandra''s Grace, The Cosmic Horror, Staff of Myrddin, Blood-Bound
    Book, Polynomicon, Eye of Erebus, Screeching Gargoyle, Soul Reaver, Book of Thoth,
    Freya''s Tears.'
  slot_scores:
    Gem of Focus:
      total: 0.75
      efficiency: 0.5
      win: 1.0
      pick: 0.5
      fit: 0.63
    Spear of Desolation:
      total: 0.56
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.86
    The World Stone:
      total: 0.72
      efficiency: 0.52
      win: 1.0
      pick: 0.68
      fit: 0.37
    Rod of Tahuti:
      total: 0.85
      efficiency: 0.86
      win: 1.0
      pick: 0.78
      fit: 0.37
    Obsidian Shard:
      total: 0.77
      efficiency: 0.58
      win: 1.0
      pick: 0.83
      fit: 0.47
    Soul Gem:
      total: 0.55
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Gem of Focus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Gem of Focus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Nimble Ring
  flex_slots:
  - Gem of Focus
  - Jotunn's Revenge
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
    win/pick). Underrated for this god: Jotunn''s Revenge, Tekko-Kagi, Spear of Desolation,
    Titan''s Bane, Soul Gem, Hydra''s Lament, Death Metal, The Crusher, Spear of the
    Magus, Heartseeker, Lernaean Bow, The Reaper, Gluttonous Grimoire, Arondight,
    Doom Orb, Silverbranch Bow, Golden Blade, Ancient Signet, Dominance, Chronos''
    Pendant, Dreamer''s Idol, Pendulum Blade, Avatar''s Parashu, Bracer of The Abyss,
    Transcendence, Runeforged Hammer, Toxic Blade, The Cosmic Horror, Heartwood Charm,
    Blood-Bound Book, Polynomicon, Avenging Blade, Triton''s Conch, Shield Splitter.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.65
    Gem of Focus:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.5
      fit: 0.34
    The World Stone:
      total: 0.73
      efficiency: 0.52
      win: 1.0
      pick: 0.68
      fit: 0.44
    Rod of Tahuti:
      total: 0.86
      efficiency: 0.86
      win: 1.0
      pick: 0.78
      fit: 0.44
    Obsidian Shard:
      total: 0.78
      efficiency: 0.58
      win: 1.0
      pick: 0.83
      fit: 0.54
    Nimble Ring:
      total: 0.76
      efficiency: 0.58
      win: 1.0
      pick: 1.0
      fit: 0.35
  community_ordered:
  - Gem of Focus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Nimble Ring
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Gem of Focus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Nimble Ring
  flex_slots:
  - Nimble Ring
  - Jotunn's Revenge
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Spear of Desolation,
    Soul Gem, Titan''s Bane, Spear of the Magus, Death Metal, Hydra''s Lament, Gluttonous
    Grimoire, The Crusher, Doom Orb, Heartseeker, The Reaper, Dreamer''s Idol, Chronos''
    Pendant, Ancient Signet, Arondight, Tekko-Kagi, Pendulum Blade, The Cosmic Horror,
    Heartwood Charm, Avatar''s Parashu, Blood-Bound Book, Polynomicon, Transcendence,
    Runeforged Hammer, Triton''s Conch, Soul Reaver, Totem of Death, Book of Thoth,
    Avenging Blade, Divine Ruin, Jade Scepter, Shield Splitter, Eye of the Storm,
    Bancroft''s Talon.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.69
    Gem of Focus:
      total: 0.72
      efficiency: 0.5
      win: 1.0
      pick: 0.5
      fit: 0.44
    The World Stone:
      total: 0.75
      efficiency: 0.52
      win: 1.0
      pick: 0.68
      fit: 0.56
    Rod of Tahuti:
      total: 0.88
      efficiency: 0.86
      win: 1.0
      pick: 0.78
      fit: 0.56
    Obsidian Shard:
      total: 0.79
      efficiency: 0.58
      win: 1.0
      pick: 0.83
      fit: 0.66
    Nimble Ring:
      total: 0.68
      efficiency: 0.38
      win: 1.0
      pick: 1.0
      fit: 0.31
  community_ordered:
  - Gem of Focus
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Nimble Ring
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
    Underrated for this god: Spear of Desolation, Soul Gem, Spear of the Magus, Gluttonous
    Grimoire, Doom Orb, Dreamer''s Idol, Chronos'' Pendant, The Cosmic Horror, Ancient
    Signet, Heartwood Charm, Blood-Bound Book, Polynomicon, Totem of Death, Soul Reaver,
    Book of Thoth, Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm of Radiance,
    Ethereal Staff, Staff of Myrddin, Typhon’s Heart, Alchemist Coat, Bracer of The
    Abyss, Death Metal.'
  slot_scores:
    Spear of Desolation:
      total: 0.58
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 1.0
    Doom Orb:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.55
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.91
      efficiency: 0.86
      win: 1.0
      pick: 0.78
      fit: 0.79
    Obsidian Shard:
      total: 0.83
      efficiency: 0.58
      win: 1.0
      pick: 0.83
      fit: 0.89
    Soul Gem:
      total: 0.56
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
---

---
type: smite-build
god: The Morrigan
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.5
    win_rate: 1.0
    alternates:
    - name: Hussar's Wings
      pick_rate: 0.5
      win_rate: 1.0
  - name: The World Stone
    pick_rate: 0.5
    win_rate: 1.0
    alternates:
    - name: Gem
      pick_rate: 0.5
      win_rate: 1.0
  - name: Gem of Focus
    pick_rate: 1.0
    win_rate: 1.0
  - name: Polynomicon
    pick_rate: 1.0
    win_rate: 1.0
  - name: Evil Eye
    pick_rate: 1.0
    win_rate: 1.0
  community_starters:
  - name: Conduit Gem
    pick_rate: 0.5
    win_rate: 1.0
  - name: Pendulum of the Ages
    pick_rate: 0.5
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/the-morrigan/
  last_verified: '2026-11-04'
  god_win_rate: 1
  god_matches_won: 2
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
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Obsidian Shard
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Obsidian Shard, Soul Gem, Spear of the Magus, Gluttonous
    Grimoire, Doom Orb, Dreamer''s Idol, Chronos'' Pendant, The Cosmic Horror, Ancient
    Signet, Heartwood Charm, Blood-Bound Book, Totem of Death, Soul Reaver, Book of
    Thoth, Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm of Radiance, Ethereal
    Staff, Staff of Myrddin, Typhon’s Heart, Alchemist Coat, Bracer of The Abyss,
    Death Metal.'
  slot_scores:
    Spear of Desolation:
      total: 0.83
      efficiency: 0.59
      win: 1.0
      pick: 0.5
      fit: 1.0
    Spear of the Magus:
      total: 0.77
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.8
    The World Stone:
      total: 0.79
      efficiency: 0.52
      win: 1.0
      pick: 0.68
      fit: 0.8
    Obsidian Shard:
      total: 0.79
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.9
    Rod of Tahuti:
      total: 0.87
      efficiency: 0.86
      win: 1.0
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.78
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - The World Stone
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Polynomicon
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Soul Gem, Obsidian Shard, Death Metal, Doom Orb, Spear of the Magus,
    Ancient Signet, Gluttonous Grimoire, Chronos'' Pendant, Heartwood Charm, Dreamer''s
    Idol, Bragi''s Harp, Soul Reaver, Blood-Bound Book, The Cosmic Horror, Book of
    Thoth, Bancroft''s Talon, Triton''s Conch, Totem of Death, Divine Ruin, Jade Scepter,
    Genji''s Guard, Helm of Radiance, Ethereal Staff, Wish-Granting Pearl.'
  slot_scores:
    Book of Thoth:
      total: 0.68
      efficiency: 0.49
      win: 1.0
      pick: 0.0
      fit: 0.39
    Spear of Desolation:
      total: 0.77
      efficiency: 0.59
      win: 1.0
      pick: 0.5
      fit: 0.61
    The World Stone:
      total: 0.75
      efficiency: 0.52
      win: 1.0
      pick: 0.68
      fit: 0.57
    Polynomicon:
      total: 0.75
      efficiency: 0.5
      win: 1.0
      pick: 1.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.84
      efficiency: 0.86
      win: 1.0
      pick: 0.0
      fit: 0.57
    Soul Gem:
      total: 0.74
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Polynomicon
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Spear of Desolation
  - The World Stone
  - Gem of Focus
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - The World Stone
  - Gem of Focus
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
    god: Rod of Tahuti, Soul Gem, Obsidian Shard, Spear of the Magus, Gluttonous Grimoire,
    Doom Orb, Dreamer''s Idol, Chronos'' Pendant, Death Metal, Ancient Signet, The
    Cosmic Horror, Heartwood Charm, Bragi''s Harp, Blood-Bound Book, Totem of Death,
    Soul Reaver, Book of Thoth, Damaru, Divine Ruin, Jade Scepter, Genji''s Guard,
    Triton''s Conch, Bancroft''s Talon, Helm of Radiance, Ethereal Staff.'
  slot_scores:
    Spear of Desolation:
      total: 0.8
      efficiency: 0.59
      win: 1.0
      pick: 0.5
      fit: 0.78
    The World Stone:
      total: 0.75
      efficiency: 0.52
      win: 1.0
      pick: 0.68
      fit: 0.56
    Gem of Focus:
      total: 0.74
      efficiency: 0.5
      win: 1.0
      pick: 1.0
      fit: 0.44
    Obsidian Shard:
      total: 0.75
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.84
      efficiency: 0.86
      win: 1.0
      pick: 0.0
      fit: 0.56
    Soul Gem:
      total: 0.77
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Gem of Focus
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Soul Gem, Shield of the Phoenix, Gluttonous
    Grimoire, Kinetic Cuirass, Ethereal Staff, Genji''s Guard, Obsidian Shard, Phoenix
    Feather, Freya''s Tears, Blood-Bound Book, Yogi''s Necklace, Helm of Radiance,
    Spear of the Magus, Sphere of Negation, Helm of Darkness, Breastplate of Valor,
    Erosion, Oni Hunter''s Garb, Eye of Providence, Chandra''s Grace, Draconic Scale,
    Jade Scepter, Midgardian Mail, Doom Orb, Regrowth Striders.'
  slot_scores:
    Genji's Guard:
      total: 0.73
      efficiency: 0.69
      win: 1.0
      pick: 0.0
      fit: 0.25
    Kinetic Cuirass:
      total: 0.74
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.76
      efficiency: 0.59
      win: 1.0
      pick: 0.5
      fit: 0.49
    Rod of Tahuti:
      total: 0.81
      efficiency: 0.86
      win: 1.0
      pick: 0.0
      fit: 0.39
    Amanita Charm:
      total: 0.8
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.77
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.89
  community_ordered:
  - Spear of Desolation
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Obsidian Shard
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
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Obsidian Shard, Soul Gem, Spear of the Magus, Gluttonous
    Grimoire, Doom Orb, Dreamer''s Idol, The Cosmic Horror, Chronos'' Pendant, Ancient
    Signet, Heartwood Charm, Blood-Bound Book, Soul Reaver, Totem of Death, Book of
    Thoth, Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm of Radiance, Ethereal
    Staff, Screeching Gargoyle, Typhon’s Heart, Genji''s Guard, Alchemist Coat, Bracer
    of The Abyss.'
  slot_scores:
    Spear of Desolation:
      total: 0.83
      efficiency: 0.59
      win: 1.0
      pick: 0.5
      fit: 1.0
    Spear of the Magus:
      total: 0.78
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.86
    The World Stone:
      total: 0.8
      efficiency: 0.52
      win: 1.0
      pick: 0.68
      fit: 0.86
    Obsidian Shard:
      total: 0.8
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.96
    Rod of Tahuti:
      total: 0.88
      efficiency: 0.86
      win: 1.0
      pick: 0.0
      fit: 0.86
    Soul Gem:
      total: 0.78
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
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
    this god: Rod of Tahuti, Nimble Ring, Soul Gem, Gluttonous Grimoire, Obsidian
    Shard, Bragi''s Harp, Spear of the Magus, Blood-Bound Book, Bracer of The Abyss,
    Ancient Signet, Doom Orb, Death Metal, Chronos'' Pendant, Dreamer''s Idol, Bancroft''s
    Talon, Heartwood Charm, The Cosmic Horror, Typhon’s Heart, Soul Reaver, Book of
    Thoth, Divine Ruin, Jade Scepter, Totem of Death, Damaru, Helm of Radiance.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.69
      efficiency: 0.52
      win: 1.0
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.74
      efficiency: 0.63
      win: 1.0
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.74
      efficiency: 0.59
      win: 1.0
      pick: 0.5
      fit: 0.4
    Bragi's Harp:
      total: 0.7
      efficiency: 0.45
      win: 1.0
      pick: 0.0
      fit: 0.62
    Rod of Tahuti:
      total: 0.8
      efficiency: 0.86
      win: 1.0
      pick: 0.0
      fit: 0.32
    Soul Gem:
      total: 0.74
      efficiency: 0.57
      win: 1.0
      pick: 0.0
      fit: 0.58
  community_ordered:
  - Spear of Desolation
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Gem of Focus
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Chronos' Pendant
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Soul Gem, Chronos''
    Pendant, Obsidian Shard, Heartwood Charm, Spear of the Magus, Gluttonous Grimoire,
    Totem of Death, Damaru, Doom Orb, Genji''s Guard, Dreamer''s Idol, Ancient Signet,
    Death Metal, Breastplate of Valor, Chandra''s Grace, The Cosmic Horror, Staff
    of Myrddin, Blood-Bound Book, Eye of Erebus, Screeching Gargoyle, Bragi''s Harp,
    Soul Reaver, Book of Thoth, Freya''s Tears.'
  slot_scores:
    Chronos' Pendant:
      total: 0.74
      efficiency: 0.55
      win: 1.0
      pick: 0.0
      fit: 0.62
    Spear of Desolation:
      total: 0.81
      efficiency: 0.59
      win: 1.0
      pick: 0.5
      fit: 0.86
    Gem of Focus:
      total: 0.77
      efficiency: 0.5
      win: 1.0
      pick: 1.0
      fit: 0.62
    Obsidian Shard:
      total: 0.73
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.81
      efficiency: 0.86
      win: 1.0
      pick: 0.0
      fit: 0.38
    Soul Gem:
      total: 0.78
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Spear of Desolation
  - Gem of Focus
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Spear of Desolation
  - Transcendence
  - Tekko-Kagi
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
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Tekko-Kagi,
    Titan''s Bane, Obsidian Shard, Soul Gem, Tyrfing, Hydra''s Lament, Bragi''s Harp,
    Death Metal, The Crusher, Spear of the Magus, Heartseeker, Lernaean Bow, The Reaper,
    Nimble Ring, Gluttonous Grimoire, Arondight, Silverbranch Bow, Golden Blade, Doom
    Orb, Dominance, Ancient Signet, Dreamer''s Idol, Pendulum Blade, Chronos'' Pendant,
    Avatar''s Parashu, Transcendence, Bracer of The Abyss, Toxic Blade, Runeforged
    Hammer, The Cosmic Horror, Heartwood Charm, Blood-Bound Book, Avenging Blade,
    Riptalon, Shield Splitter.'
  slot_scores:
    Book of Thoth:
      total: 0.66
      efficiency: 0.49
      win: 1.0
      pick: 0.0
      fit: 0.22
    Jotunn's Revenge:
      total: 0.78
      efficiency: 0.67
      win: 1.0
      pick: 0.0
      fit: 0.65
    Spear of Desolation:
      total: 0.76
      efficiency: 0.59
      win: 1.0
      pick: 0.5
      fit: 0.54
    Transcendence:
      total: 0.68
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.33
    Tekko-Kagi:
      total: 0.74
      efficiency: 0.55
      win: 1.0
      pick: 0.0
      fit: 0.67
    Rod of Tahuti:
      total: 0.82
      efficiency: 0.86
      win: 1.0
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Spear of Desolation
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Spear of Desolation
  - Transcendence
  - Obsidian Shard
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Obsidian Shard, Soul Gem, Titan''s Bane, Spear of the Magus, Death Metal, Hydra''s
    Lament, Gluttonous Grimoire, The Crusher, Doom Orb, Heartseeker, The Reaper, Dreamer''s
    Idol, Ancient Signet, Chronos'' Pendant, Arondight, Tekko-Kagi, Bragi''s Harp,
    Pendulum Blade, The Cosmic Horror, Tyrfing, Avatar''s Parashu, Heartwood Charm,
    Blood-Bound Book, Transcendence, Runeforged Hammer, Triton''s Conch, Soul Reaver,
    Book of Thoth, Totem of Death, Avenging Blade, Divine Ruin, Jade Scepter, Shield
    Splitter, Eye of the Storm, Golden Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.67
      efficiency: 0.49
      win: 1.0
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.79
      efficiency: 0.67
      win: 1.0
      pick: 0.0
      fit: 0.69
    Spear of Desolation:
      total: 0.79
      efficiency: 0.59
      win: 1.0
      pick: 0.5
      fit: 0.69
    Transcendence:
      total: 0.68
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.31
    Obsidian Shard:
      total: 0.75
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.84
      efficiency: 0.86
      win: 1.0
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Spear of Desolation
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Obsidian Shard
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Obsidian Shard, Soul Gem, Spear of the
    Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s Idol, Chronos'' Pendant, The
    Cosmic Horror, Ancient Signet, Heartwood Charm, Blood-Bound Book, Totem of Death,
    Soul Reaver, Book of Thoth, Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm
    of Radiance, Ethereal Staff, Staff of Myrddin, Typhon’s Heart, Alchemist Coat,
    Bracer of The Abyss, Death Metal.'
  slot_scores:
    Spear of Desolation:
      total: 0.83
      efficiency: 0.59
      win: 1.0
      pick: 0.5
      fit: 1.0
    Doom Orb:
      total: 0.76
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.8
    Spear of the Magus:
      total: 0.77
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.8
    Obsidian Shard:
      total: 0.79
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.9
    Rod of Tahuti:
      total: 0.87
      efficiency: 0.86
      win: 1.0
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.78
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  starter: *id001
---

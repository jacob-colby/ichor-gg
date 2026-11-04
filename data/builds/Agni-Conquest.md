---
type: smite-build
god: Agni
mode: Conquest
builds:
- source: community
  aspect: Aspect of Combustion
  aspect_pick_rate: 1.0
  aspect_win_rate: 1.0
  slot_order:
  - name: Tyrfing
    pick_rate: 1.0
    win_rate: 1.0
  - name: Bragi's Harp
    pick_rate: 1.0
    win_rate: 1.0
  - name: The Executioner
    pick_rate: 1.0
    win_rate: 1.0
  - name: Odysseus' Bow
    pick_rate: 1.0
    win_rate: 1.0
  - name: Riptalon
    pick_rate: 1.0
    win_rate: 1.0
  - name: Silverbranch Bow
    pick_rate: 1.0
    win_rate: 1.0
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 1.0
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/agni/
  last_verified: '2026-11-04'
  god_win_rate: 1
  god_matches_won: 1
  god_matches_played: 1
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Spear of Desolation, Obsidian Shard, Soul Gem, Spear
    of the Magus, Gluttonous Grimoire, Doom Orb, The World Stone, Dreamer''s Idol,
    Chronos'' Pendant, The Cosmic Horror, Ancient Signet, Gem of Focus, Heartwood
    Charm, Blood-Bound Book, Polynomicon, Totem of Death, Soul Reaver, Book of Thoth,
    Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm of Radiance, Ethereal Staff,
    Staff of Myrddin, Typhon’s Heart, Alchemist Coat, Bracer of The Abyss, Death Metal.'
  slot_scores:
    Spear of Desolation:
      total: 0.81
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 1.0
    Doom Orb:
      total: 0.76
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.77
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.79
    Obsidian Shard:
      total: 0.79
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.89
    Rod of Tahuti:
      total: 0.87
      efficiency: 0.86
      win: 1.0
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.78
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Bragi's Harp
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Spear of Desolation, Soul Gem, Obsidian Shard, Death Metal, Doom Orb,
    Spear of the Magus, Ancient Signet, The World Stone, Gluttonous Grimoire, Chronos''
    Pendant, Heartwood Charm, Dreamer''s Idol, Polynomicon, Gem of Focus, Soul Reaver,
    Blood-Bound Book, The Cosmic Horror, Book of Thoth, Bancroft''s Talon, Triton''s
    Conch, Totem of Death, Divine Ruin, Jade Scepter, Genji''s Guard, Helm of Radiance,
    Ethereal Staff, Wish-Granting Pearl.'
  slot_scores:
    Book of Thoth:
      total: 0.68
      efficiency: 0.49
      win: 1.0
      pick: 0.0
      fit: 0.39
    Bragi's Harp:
      total: 0.74
      efficiency: 0.41
      win: 1.0
      pick: 1.0
      fit: 0.67
    Spear of Desolation:
      total: 0.75
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.61
    Doom Orb:
      total: 0.72
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.57
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
  - Bragi's Harp
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Bragi's Harp
  - Spear of Desolation
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of the Magus
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Spear of Desolation, Soul Gem, Obsidian Shard, Spear of the
    Magus, Gluttonous Grimoire, Doom Orb, The World Stone, Dreamer''s Idol, Chronos''
    Pendant, Death Metal, Ancient Signet, The Cosmic Horror, Gem of Focus, Heartwood
    Charm, Blood-Bound Book, Polynomicon, Totem of Death, Soul Reaver, Book of Thoth,
    Damaru, Divine Ruin, Jade Scepter, Genji''s Guard, Triton''s Conch, Bancroft''s
    Talon, Helm of Radiance, Ethereal Staff.'
  slot_scores:
    Bragi's Harp:
      total: 0.72
      efficiency: 0.41
      win: 1.0
      pick: 1.0
      fit: 0.54
    Spear of Desolation:
      total: 0.77
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.78
    Spear of the Magus:
      total: 0.73
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.56
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
  - Bragi's Harp
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
  - Spear of Desolation
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
    Grimoire, Kinetic Cuirass, Ethereal Staff, Spear of Desolation, Genji''s Guard,
    Obsidian Shard, Phoenix Feather, Blood-Bound Book, Freya''s Tears, Yogi''s Necklace,
    Helm of Radiance, Sphere of Negation, Helm of Darkness, Spear of the Magus, Breastplate
    of Valor, Erosion, Oni Hunter''s Garb, Eye of Providence, Chandra''s Grace, Jade
    Scepter, Draconic Scale, Midgardian Mail, Doom Orb, Ancient Signet, Regrowth Striders.'
  slot_scores:
    Genji's Guard:
      total: 0.73
      efficiency: 0.69
      win: 1.0
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.74
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.73
      efficiency: 0.59
      win: 1.0
      pick: 0.0
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
  starter: *id001
- source: suggested
  archetype: anti-tank
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
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Spear of Desolation, Obsidian Shard, Soul Gem, Spear
    of the Magus, Gluttonous Grimoire, Doom Orb, The World Stone, Dreamer''s Idol,
    The Cosmic Horror, Chronos'' Pendant, Ancient Signet, Gem of Focus, Heartwood
    Charm, Blood-Bound Book, Polynomicon, Totem of Death, Soul Reaver, Book of Thoth,
    Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm of Radiance, Ethereal Staff,
    Screeching Gargoyle, Typhon’s Heart, Genji''s Guard, Alchemist Coat, Staff of
    Myrddin.'
  slot_scores:
    Spear of Desolation:
      total: 0.81
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 1.0
    Doom Orb:
      total: 0.76
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.78
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.85
    Obsidian Shard:
      total: 0.8
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.95
    Rod of Tahuti:
      total: 0.88
      efficiency: 0.86
      win: 1.0
      pick: 0.0
      fit: 0.85
    Soul Gem:
      total: 0.78
      efficiency: 0.53
      win: 1.0
      pick: 0.0
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
  - Spear of Desolation
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
    this god: Rod of Tahuti, Nimble Ring, Soul Gem, Spear of Desolation, Gluttonous
    Grimoire, Obsidian Shard, Spear of the Magus, Blood-Bound Book, Bracer of The
    Abyss, Ancient Signet, Death Metal, Doom Orb, The World Stone, Chronos'' Pendant,
    Dreamer''s Idol, Bancroft''s Talon, Polynomicon, Gem of Focus, Heartwood Charm,
    The Cosmic Horror, Typhon’s Heart, Soul Reaver, Book of Thoth, Divine Ruin, Jade
    Scepter, Totem of Death, Damaru, Helm of Radiance.'
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
    Bragi's Harp:
      total: 0.75
      efficiency: 0.45
      win: 1.0
      pick: 1.0
      fit: 0.63
    Spear of Desolation:
      total: 0.72
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.4
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
  - Bragi's Harp
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Gem of Focus
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Spear of Desolation,
    Soul Gem, Chronos'' Pendant, Obsidian Shard, Gem of Focus, Heartwood Charm, Spear
    of the Magus, Totem of Death, Gluttonous Grimoire, Damaru, Doom Orb, Genji''s
    Guard, The World Stone, Death Metal, Ancient Signet, Dreamer''s Idol, Breastplate
    of Valor, Chandra''s Grace, The Cosmic Horror, Staff of Myrddin, Blood-Bound Book,
    Polynomicon, Eye of Erebus, Screeching Gargoyle, Soul Reaver, Book of Thoth, Freya''s
    Tears.'
  slot_scores:
    Chronos' Pendant:
      total: 0.74
      efficiency: 0.55
      win: 1.0
      pick: 0.0
      fit: 0.63
    Gem of Focus:
      total: 0.72
      efficiency: 0.5
      win: 1.0
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.79
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.86
    Obsidian Shard:
      total: 0.72
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.81
      efficiency: 0.86
      win: 1.0
      pick: 0.0
      fit: 0.37
    Soul Gem:
      total: 0.78
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Bragi's Harp
  - Spear of Desolation
  - Tekko-Kagi
  - Silverbranch Bow
  flex_slots:
  - Tekko-Kagi
  - Spear of Desolation
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
    Spear of Desolation, Obsidian Shard, Titan''s Bane, Soul Gem, Hydra''s Lament,
    Death Metal, The Crusher, Spear of the Magus, Heartseeker, Lernaean Bow, The Reaper,
    Nimble Ring, Gluttonous Grimoire, Golden Blade, Arondight, Doom Orb, The World
    Stone, Ancient Signet, Dominance, Chronos'' Pendant, Dreamer''s Idol, Pendulum
    Blade, Avatar''s Parashu, Bracer of The Abyss, Transcendence, Toxic Blade, Runeforged
    Hammer, Gem of Focus, The Cosmic Horror, Heartwood Charm, Blood-Bound Book, Polynomicon,
    Avenging Blade, Triton''s Conch.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.78
      efficiency: 0.67
      win: 1.0
      pick: 0.0
      fit: 0.65
    Tyrfing:
      total: 0.78
      efficiency: 0.5
      win: 1.0
      pick: 1.0
      fit: 0.69
    Bragi's Harp:
      total: 0.77
      efficiency: 0.45
      win: 1.0
      pick: 1.0
      fit: 0.77
    Spear of Desolation:
      total: 0.74
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.55
    Tekko-Kagi:
      total: 0.74
      efficiency: 0.55
      win: 1.0
      pick: 0.0
      fit: 0.66
    Silverbranch Bow:
      total: 0.75
      efficiency: 0.52
      win: 1.0
      pick: 1.0
      fit: 0.49
  community_ordered:
  - Tyrfing
  - Bragi's Harp
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Bragi's Harp
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Bragi's Harp
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
    Spear of Desolation, Soul Gem, Obsidian Shard, Titan''s Bane, Spear of the Magus,
    Death Metal, Hydra''s Lament, Gluttonous Grimoire, The Crusher, Doom Orb, The
    World Stone, Heartseeker, The Reaper, Dreamer''s Idol, Chronos'' Pendant, Ancient
    Signet, Arondight, Tekko-Kagi, Pendulum Blade, The Cosmic Horror, Gem of Focus,
    Heartwood Charm, Avatar''s Parashu, Blood-Bound Book, Polynomicon, Transcendence,
    Runeforged Hammer, Triton''s Conch, Soul Reaver, Totem of Death, Book of Thoth,
    Avenging Blade, Divine Ruin, Jade Scepter, Shield Splitter, Golden Blade, Eye
    of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.79
      efficiency: 0.67
      win: 1.0
      pick: 0.0
      fit: 0.69
    Bragi's Harp:
      total: 0.75
      efficiency: 0.41
      win: 1.0
      pick: 1.0
      fit: 0.71
    Spear of Desolation:
      total: 0.76
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.69
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
      total: 0.75
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.79
  community_ordered:
  - Bragi's Harp
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
    Underrated for this god: Rod of Tahuti, Spear of Desolation, Obsidian Shard, Soul
    Gem, Spear of the Magus, Gluttonous Grimoire, Doom Orb, The World Stone, Dreamer''s
    Idol, Chronos'' Pendant, The Cosmic Horror, Ancient Signet, Gem of Focus, Heartwood
    Charm, Blood-Bound Book, Polynomicon, Totem of Death, Soul Reaver, Book of Thoth,
    Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm of Radiance, Ethereal Staff,
    Staff of Myrddin, Typhon’s Heart, Alchemist Coat, Bracer of The Abyss, Death Metal.'
  slot_scores:
    Spear of Desolation:
      total: 0.81
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 1.0
    Doom Orb:
      total: 0.76
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.77
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.79
    Obsidian Shard:
      total: 0.79
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.89
    Rod of Tahuti:
      total: 0.87
      efficiency: 0.86
      win: 1.0
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.78
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Tahuti
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Spear of Desolation, Soul Gem, Obsidian Shard, Spear
    of the Magus, Gluttonous Grimoire, Doom Orb, The World Stone, Dreamer''s Idol,
    Nimble Ring, Chronos'' Pendant, Ancient Signet, The Cosmic Horror, Gem of Focus,
    Bracer of The Abyss, Heartwood Charm, Blood-Bound Book, Polynomicon, Totem of
    Death, Soul Reaver, Book of Thoth, Divine Ruin, Jade Scepter, Bancroft''s Talon,
    Helm of Radiance, Ethereal Staff, Typhon’s Heart, Staff of Myrddin, Alchemist
    Coat.'
  slot_scores:
    Nimble Ring:
      total: 0.73
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.5
    Spear of Desolation:
      total: 0.79
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.86
    Doom Orb:
      total: 0.74
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.68
    Spear of the Magus:
      total: 0.75
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.68
    Obsidian Shard:
      total: 0.77
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.78
    Rod of Tahuti:
      total: 0.85
      efficiency: 0.86
      win: 1.0
      pick: 0.0
      fit: 0.68
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Nimble Ring
  - Bragi's Harp
  - Spear of Desolation
  - Doom Orb
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Spear of Desolation, Soul Gem, Obsidian Shard, Death Metal, Spear of
    the Magus, Doom Orb, Ancient Signet, The World Stone, Gluttonous Grimoire, Nimble
    Ring, Chronos'' Pendant, Heartwood Charm, Polynomicon, Dreamer''s Idol, Gem of
    Focus, Bracer of The Abyss, Soul Reaver, Blood-Bound Book, Book of Thoth, The
    Cosmic Horror, Bancroft''s Talon, Totem of Death, Triton''s Conch, Divine Ruin,
    Jade Scepter, Genji''s Guard, Helm of Radiance.'
  slot_scores:
    Book of Thoth:
      total: 0.68
      efficiency: 0.49
      win: 1.0
      pick: 0.0
      fit: 0.36
    Nimble Ring:
      total: 0.7
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.34
    Bragi's Harp:
      total: 0.76
      efficiency: 0.45
      win: 1.0
      pick: 1.0
      fit: 0.7
    Spear of Desolation:
      total: 0.74
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.57
    Doom Orb:
      total: 0.72
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.53
    Rod of Tahuti:
      total: 0.83
      efficiency: 0.86
      win: 1.0
      pick: 0.0
      fit: 0.53
  community_ordered:
  - Bragi's Harp
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: burst
  slot_order:
  - Nimble Ring
  - Bragi's Harp
  - Spear of Desolation
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Tahuti
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Spear of Desolation, Soul Gem, Obsidian Shard, Spear of the
    Magus, Gluttonous Grimoire, Doom Orb, The World Stone, Chronos'' Pendant, Dreamer''s
    Idol, Death Metal, Nimble Ring, Ancient Signet, The Cosmic Horror, Gem of Focus,
    Heartwood Charm, Bracer of The Abyss, Blood-Bound Book, Polynomicon, Totem of
    Death, Soul Reaver, Book of Thoth, Damaru, Divine Ruin, Jade Scepter, Genji''s
    Guard, Triton''s Conch, Bancroft''s Talon.'
  slot_scores:
    Nimble Ring:
      total: 0.7
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.29
    Bragi's Harp:
      total: 0.74
      efficiency: 0.45
      win: 1.0
      pick: 1.0
      fit: 0.59
    Spear of Desolation:
      total: 0.76
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.71
    Spear of the Magus:
      total: 0.73
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.51
    Obsidian Shard:
      total: 0.75
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.61
    Rod of Tahuti:
      total: 0.83
      efficiency: 0.86
      win: 1.0
      pick: 0.0
      fit: 0.51
  community_ordered:
  - Bragi's Harp
  starter: *id001
  aspect: Aspect of Combustion
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
  - Genji's Guard
  - Spear of Desolation
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
    Grimoire, Kinetic Cuirass, Ethereal Staff, Genji''s Guard, Spear of Desolation,
    Obsidian Shard, Blood-Bound Book, Phoenix Feather, Yogi''s Necklace, Freya''s
    Tears, Helm of Radiance, Sphere of Negation, Breastplate of Valor, Spear of the
    Magus, Helm of Darkness, Oni Hunter''s Garb, Chandra''s Grace, Erosion, Eye of
    Providence, Jade Scepter, Draconic Scale, Nimble Ring, Midgardian Mail, Doom Orb,
    Ancient Signet.'
  slot_scores:
    Genji's Guard:
      total: 0.73
      efficiency: 0.69
      win: 1.0
      pick: 0.0
      fit: 0.24
    Kinetic Cuirass:
      total: 0.73
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.57
    Spear of Desolation:
      total: 0.73
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.81
      efficiency: 0.86
      win: 1.0
      pick: 0.0
      fit: 0.36
    Amanita Charm:
      total: 0.79
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.77
    Soul Gem:
      total: 0.76
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.86
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: anti-tank
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
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Spear of Desolation, Soul Gem, Obsidian Shard, Spear
    of the Magus, Gluttonous Grimoire, Doom Orb, The World Stone, Dreamer''s Idol,
    The Cosmic Horror, Nimble Ring, Chronos'' Pendant, Ancient Signet, Gem of Focus,
    Bracer of The Abyss, Heartwood Charm, Blood-Bound Book, Polynomicon, Soul Reaver,
    Totem of Death, Book of Thoth, Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm
    of Radiance, Ethereal Staff, Screeching Gargoyle, Genji''s Guard, Typhon’s Heart.'
  slot_scores:
    Spear of Desolation:
      total: 0.79
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.9
    Doom Orb:
      total: 0.75
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.77
    Spear of the Magus:
      total: 0.77
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.77
    Obsidian Shard:
      total: 0.78
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.87
    Rod of Tahuti:
      total: 0.87
      efficiency: 0.86
      win: 1.0
      pick: 0.0
      fit: 0.77
    Soul Gem:
      total: 0.78
      efficiency: 0.53
      win: 1.0
      pick: 0.0
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
  - Spear of Desolation
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
    this god: Rod of Tahuti, Nimble Ring, Soul Gem, Spear of Desolation, Gluttonous
    Grimoire, Obsidian Shard, Spear of the Magus, Blood-Bound Book, Bracer of The
    Abyss, Ancient Signet, Death Metal, Doom Orb, The World Stone, Chronos'' Pendant,
    Dreamer''s Idol, Bancroft''s Talon, Polynomicon, Gem of Focus, Heartwood Charm,
    The Cosmic Horror, Typhon’s Heart, Soul Reaver, Book of Thoth, Divine Ruin, Jade
    Scepter, Totem of Death, Damaru, Helm of Radiance.'
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
    Bragi's Harp:
      total: 0.75
      efficiency: 0.45
      win: 1.0
      pick: 1.0
      fit: 0.63
    Spear of Desolation:
      total: 0.72
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.4
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
  - Bragi's Harp
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Bragi's Harp
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Bragi's Harp
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Spear of Desolation,
    Soul Gem, Chronos'' Pendant, Obsidian Shard, Gem of Focus, Heartwood Charm, Spear
    of the Magus, Gluttonous Grimoire, Totem of Death, Damaru, Doom Orb, Nimble Ring,
    The World Stone, Genji''s Guard, Ancient Signet, Death Metal, Dreamer''s Idol,
    Breastplate of Valor, Chandra''s Grace, Bracer of The Abyss, The Cosmic Horror,
    Blood-Bound Book, Polynomicon, Staff of Myrddin, Eye of Erebus, Screeching Gargoyle,
    Soul Reaver.'
  slot_scores:
    Chronos' Pendant:
      total: 0.73
      efficiency: 0.55
      win: 1.0
      pick: 0.0
      fit: 0.57
    Bragi's Harp:
      total: 0.72
      efficiency: 0.45
      win: 1.0
      pick: 1.0
      fit: 0.45
    Spear of Desolation:
      total: 0.77
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.78
    Obsidian Shard:
      total: 0.72
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.8
      efficiency: 0.86
      win: 1.0
      pick: 0.0
      fit: 0.34
    Soul Gem:
      total: 0.77
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Bragi's Harp
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Bragi's Harp
  - Spear of Desolation
  - Tekko-Kagi
  - Silverbranch Bow
  flex_slots:
  - Tekko-Kagi
  - Spear of Desolation
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
    Spear of Desolation, Obsidian Shard, Titan''s Bane, Soul Gem, Hydra''s Lament,
    Death Metal, The Crusher, Spear of the Magus, Heartseeker, Lernaean Bow, The Reaper,
    Nimble Ring, Gluttonous Grimoire, Golden Blade, Arondight, Doom Orb, The World
    Stone, Ancient Signet, Dominance, Chronos'' Pendant, Dreamer''s Idol, Pendulum
    Blade, Avatar''s Parashu, Bracer of The Abyss, Transcendence, Toxic Blade, Runeforged
    Hammer, Gem of Focus, The Cosmic Horror, Heartwood Charm, Blood-Bound Book, Polynomicon,
    Avenging Blade, Triton''s Conch.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.78
      efficiency: 0.67
      win: 1.0
      pick: 0.0
      fit: 0.65
    Tyrfing:
      total: 0.78
      efficiency: 0.5
      win: 1.0
      pick: 1.0
      fit: 0.69
    Bragi's Harp:
      total: 0.77
      efficiency: 0.45
      win: 1.0
      pick: 1.0
      fit: 0.77
    Spear of Desolation:
      total: 0.74
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.55
    Tekko-Kagi:
      total: 0.74
      efficiency: 0.55
      win: 1.0
      pick: 0.0
      fit: 0.66
    Silverbranch Bow:
      total: 0.75
      efficiency: 0.52
      win: 1.0
      pick: 1.0
      fit: 0.49
  community_ordered:
  - Tyrfing
  - Bragi's Harp
  - Silverbranch Bow
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Bragi's Harp
  - Spear of Desolation
  - Silverbranch Bow
  - Rod of Tahuti
  flex_slots:
  - Silverbranch Bow
  - Spear of Desolation
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Spear of Desolation, Obsidian Shard, Soul Gem, Tekko-Kagi, Titan''s Bane, Spear
    of the Magus, Death Metal, Hydra''s Lament, Gluttonous Grimoire, The Crusher,
    Doom Orb, The World Stone, Nimble Ring, Heartseeker, The Reaper, Ancient Signet,
    Dreamer''s Idol, Chronos'' Pendant, Lernaean Bow, Arondight, Golden Blade, Pendulum
    Blade, The Cosmic Horror, Bracer of The Abyss, Gem of Focus, Heartwood Charm,
    Dominance, Avatar''s Parashu, Toxic Blade, Blood-Bound Book, Polynomicon, Transcendence,
    Runeforged Hammer, Soul Reaver, Triton''s Conch.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.78
      efficiency: 0.67
      win: 1.0
      pick: 0.0
      fit: 0.63
    Tyrfing:
      total: 0.77
      efficiency: 0.5
      win: 1.0
      pick: 1.0
      fit: 0.63
    Bragi's Harp:
      total: 0.77
      efficiency: 0.45
      win: 1.0
      pick: 1.0
      fit: 0.75
    Spear of Desolation:
      total: 0.75
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.63
    Silverbranch Bow:
      total: 0.75
      efficiency: 0.52
      win: 1.0
      pick: 1.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.83
      efficiency: 0.86
      win: 1.0
      pick: 0.0
      fit: 0.51
  community_ordered:
  - Tyrfing
  - Bragi's Harp
  - Silverbranch Bow
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: model
  slot_order:
  - Nimble Ring
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Obsidian Shard
  - Rod of Tahuti
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Spear of Desolation, Soul Gem, Obsidian
    Shard, Spear of the Magus, Gluttonous Grimoire, Doom Orb, The World Stone, Dreamer''s
    Idol, Nimble Ring, Chronos'' Pendant, Ancient Signet, The Cosmic Horror, Gem of
    Focus, Bracer of The Abyss, Heartwood Charm, Blood-Bound Book, Polynomicon, Totem
    of Death, Soul Reaver, Book of Thoth, Divine Ruin, Jade Scepter, Bancroft''s Talon,
    Helm of Radiance, Ethereal Staff, Typhon’s Heart, Staff of Myrddin, Alchemist
    Coat.'
  slot_scores:
    Nimble Ring:
      total: 0.73
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.5
    Spear of Desolation:
      total: 0.79
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.86
    Doom Orb:
      total: 0.74
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.68
    Spear of the Magus:
      total: 0.75
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.68
    Obsidian Shard:
      total: 0.77
      efficiency: 0.58
      win: 1.0
      pick: 0.0
      fit: 0.78
    Rod of Tahuti:
      total: 0.85
      efficiency: 0.86
      win: 1.0
      pick: 0.0
      fit: 0.68
  starter: *id001
  aspect: Aspect of Combustion
---

---
type: smite-build
god: Agni
mode: Conquest
builds:
- source: community
  aspect: Aspect of Combustion
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.35
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.44
    win_rate: 0.5
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.24
      win_rate: 0.51
    - name: Book of Thoth
      pick_rate: 0.16
      win_rate: 0.52
  - name: The World Stone
    pick_rate: 0.3
    win_rate: 0.52
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.17
      win_rate: 0.52
    - name: Book of Thoth
      pick_rate: 0.1
      win_rate: 0.51
  - name: Rod of Tahuti
    pick_rate: 0.2
    win_rate: 0.59
    alternates:
    - name: Soul Gem
      pick_rate: 0.15
      win_rate: 0.46
    - name: The World Stone
      pick_rate: 0.14
      win_rate: 0.45
  - name: Obsidian Shard
    pick_rate: 0.17
    win_rate: 0.52
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.34
      win_rate: 0.51
    - name: Soul Reaver
      pick_rate: 0.06
      win_rate: 0.52
  - name: Evil Eye
    pick_rate: 0.11
    win_rate: 0.37
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.19
      win_rate: 0.56
    - name: Rod of Tahuti
      pick_rate: 0.15
      win_rate: 0.56
  - name: Soul Reaver
    pick_rate: 0.08
    win_rate: 0.58
    alternates:
    - name: Evil Eye
      pick_rate: 0.11
      win_rate: 0.5
    - name: Obsidian Shard
      pick_rate: 0.09
      win_rate: 0.72
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.26
    win_rate: 0.56
  - name: Archmage's Gem
    pick_rate: 0.22
    win_rate: 0.57
  - name: Conduit Gem
    pick_rate: 0.19
    win_rate: 0.44
  source_url: https://smitebrain.com/gods/agni/
  last_verified: '2026-11-02'
  god_win_rate: 0.5029013539651838
  god_matches_won: 520
  god_matches_played: 1034
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14397
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
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
    The Cosmic Horror, Heartwood Charm, Gem of Focus, Ancient Signet, Polynomicon,
    Totem of Death, Blood-Bound Book, Divine Ruin, Jade Scepter, Bancroft''s Talon,
    Helm of Radiance, Ethereal Staff, Staff of Myrddin, Typhon’s Heart, Rod of Asclepius,
    Bracer of The Abyss, Alchemist Coat, Genji''s Guard.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.48
      win: 0.52
      pick: 0.16
      fit: 0.42
    Spear of Desolation:
      total: 0.59
      efficiency: 0.56
      win: 0.5
      pick: 0.44
      fit: 1.0
    The World Stone:
      total: 0.55
      efficiency: 0.5
      win: 0.52
      pick: 0.41
      fit: 0.79
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.81
      win: 0.59
      pick: 0.31
      fit: 0.79
    Obsidian Shard:
      total: 0.58
      efficiency: 0.55
      win: 0.52
      pick: 0.28
      fit: 0.89
    Soul Gem:
      total: 0.54
      efficiency: 0.5
      win: 0.46
      pick: 0.23
      fit: 1.0
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Sundering Echo
  - Spear of Desolation
  - The World Stone
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Sundering Echo
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Sundering
    Echo, Doom Orb, Death Metal, Spear of the Magus, Gluttonous Grimoire, Heartwood
    Charm, Ancient Signet, Polynomicon, Dreamer''s Idol, Bragi''s Harp, Gem of Focus,
    The Cosmic Horror, Blood-Bound Book, Bancroft''s Talon, Totem of Death, Triton''s
    Conch, Divine Ruin, Jade Scepter, Genji''s Guard, Helm of Radiance, Ethereal Staff,
    Breastplate of Valor.'
  slot_scores:
    Sundering Echo:
      total: 0.51
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.57
    Spear of Desolation:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.44
      fit: 0.61
    The World Stone:
      total: 0.52
      efficiency: 0.5
      win: 0.52
      pick: 0.41
      fit: 0.57
    Doom Orb:
      total: 0.5
      efficiency: 0.51
      win: 0.52
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.81
      win: 0.59
      pick: 0.31
      fit: 0.57
    Obsidian Shard:
      total: 0.53
      efficiency: 0.55
      win: 0.52
      pick: 0.28
      fit: 0.57
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The World Stone
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
    god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Sundering Echo, Dreamer''s
    Idol, Death Metal, The Cosmic Horror, Heartwood Charm, Gem of Focus, Totem of
    Death, Ancient Signet, Polynomicon, Bragi''s Harp, Blood-Bound Book, Genji''s
    Guard, Damaru, Divine Ruin, Jade Scepter, Triton''s Conch, Bancroft''s Talon,
    Breastplate of Valor, Chandra''s Grace.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.48
      win: 0.52
      pick: 0.16
      fit: 0.22
    Spear of Desolation:
      total: 0.56
      efficiency: 0.56
      win: 0.5
      pick: 0.44
      fit: 0.78
    The World Stone:
      total: 0.51
      efficiency: 0.5
      win: 0.52
      pick: 0.41
      fit: 0.56
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.81
      win: 0.59
      pick: 0.31
      fit: 0.56
    Obsidian Shard:
      total: 0.54
      efficiency: 0.55
      win: 0.52
      pick: 0.28
      fit: 0.66
    Soul Gem:
      total: 0.52
      efficiency: 0.5
      win: 0.46
      pick: 0.23
      fit: 0.88
  community_ordered:
  - Book of Thoth
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
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Amanita Charm, Shield of the Phoenix, Gluttonous Grimoire, Kinetic Cuirass,
    Ethereal Staff, Genji''s Guard, Phoenix Feather, Yogi''s Necklace, Freya''s Tears,
    Rod of Asclepius, Blood-Bound Book, Breastplate of Valor, Sphere of Negation,
    Chandra''s Grace, Helm of Radiance, Helm of Darkness, Spear of the Magus, Erosion,
    Oni Hunter''s Garb, Eye of Providence, Draconic Scale, Doom Orb, Jade Scepter,
    Midgardian Mail, Glorious Pridwen.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.61
    Spear of Desolation:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.44
      fit: 0.49
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.81
      win: 0.59
      pick: 0.31
      fit: 0.39
    Obsidian Shard:
      total: 0.52
      efficiency: 0.55
      win: 0.52
      pick: 0.28
      fit: 0.49
    Amanita Charm:
      total: 0.57
      efficiency: 0.62
      win: 0.52
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.53
      efficiency: 0.5
      win: 0.46
      pick: 0.23
      fit: 0.89
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
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
  - Spear of the Magus
  - Soul Gem
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
    The Cosmic Horror, Heartwood Charm, Gem of Focus, Ancient Signet, Polynomicon,
    Blood-Bound Book, Totem of Death, Divine Ruin, Jade Scepter, Bancroft''s Talon,
    Screeching Gargoyle, Helm of Radiance, Ethereal Staff, Genji''s Guard, Typhon’s
    Heart, Rod of Asclepius, Staff of Myrddin, Bracer of The Abyss.'
  slot_scores:
    Spear of Desolation:
      total: 0.59
      efficiency: 0.56
      win: 0.5
      pick: 0.44
      fit: 1.0
    Spear of the Magus:
      total: 0.55
      efficiency: 0.54
      win: 0.52
      pick: 0.0
      fit: 0.85
    The World Stone:
      total: 0.56
      efficiency: 0.5
      win: 0.52
      pick: 0.41
      fit: 0.85
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.81
      win: 0.59
      pick: 0.31
      fit: 0.85
    Obsidian Shard:
      total: 0.59
      efficiency: 0.55
      win: 0.52
      pick: 0.28
      fit: 0.95
    Soul Gem:
      total: 0.54
      efficiency: 0.5
      win: 0.46
      pick: 0.23
      fit: 1.0
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Spear of Desolation
  - Bragi's Harp
  - Rod of Tahuti
  - Obsidian Shard
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
    this god: Nimble Ring, Gluttonous Grimoire, Sundering Echo, Bragi''s Harp, Spear
    of the Magus, Blood-Bound Book, Bracer of The Abyss, Doom Orb, Eros'' Bow, Death
    Metal, Dreamer''s Idol, Bancroft''s Talon, Ancient Signet, Heartwood Charm, Polynomicon,
    Gem of Focus, The Cosmic Horror, Typhon’s Heart, Totem of Death, Divine Ruin,
    Jade Scepter, Genji''s Guard.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.52
      efficiency: 0.61
      win: 0.52
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.44
      fit: 0.4
    Bragi's Harp:
      total: 0.47
      efficiency: 0.41
      win: 0.52
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.81
      win: 0.59
      pick: 0.31
      fit: 0.32
    Obsidian Shard:
      total: 0.5
      efficiency: 0.55
      win: 0.52
      pick: 0.28
      fit: 0.42
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Heartwood Charm
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Heartwood Charm
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
    + fit + win/pick). Underrated for this god: Heartwood Charm, Gem of Focus, Spear
    of the Magus, Totem of Death, Gluttonous Grimoire, Sundering Echo, Doom Orb, Genji''s
    Guard, Damaru, Breastplate of Valor, Chandra''s Grace, Dreamer''s Idol, Death
    Metal, The Cosmic Horror, Staff of Myrddin, Ancient Signet, Polynomicon, Blood-Bound
    Book, Screeching Gargoyle, Eye of Erebus, Bragi''s Harp, Freya''s Tears.'
  slot_scores:
    Chronos' Pendant:
      total: 0.52
      efficiency: 0.52
      win: 0.51
      pick: 0.24
      fit: 0.63
    Spear of Desolation:
      total: 0.57
      efficiency: 0.56
      win: 0.5
      pick: 0.44
      fit: 0.86
    Heartwood Charm:
      total: 0.49
      efficiency: 0.47
      win: 0.52
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.81
      win: 0.59
      pick: 0.31
      fit: 0.37
    Obsidian Shard:
      total: 0.51
      efficiency: 0.55
      win: 0.52
      pick: 0.28
      fit: 0.47
    Soul Gem:
      total: 0.54
      efficiency: 0.5
      win: 0.46
      pick: 0.23
      fit: 0.96
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Nimble Ring
  - Tekko-Kagi
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Tekko-Kagi
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Tekko-Kagi, Sundering Echo,
    Titan''s Bane, Tyrfing, Hydra''s Lament, Bragi''s Harp, Death Metal, Heartseeker,
    Spear of the Magus, The Crusher, Nimble Ring, Gluttonous Grimoire, Lernaean Bow,
    Silverbranch Bow, The Reaper, Doom Orb, Golden Blade, Arondight, Pendulum Blade,
    Dominance, Dreamer''s Idol, Toxic Blade, Bracer of The Abyss, Transcendence, The
    Cosmic Horror, Avatar''s Parashu, Heartwood Charm, Gem of Focus, Runeforged Hammer,
    Eros'' Bow, Ancient Signet, Riptalon, Polynomicon, Blood-Bound Book, Avenging
    Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.65
    Spear of Desolation:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.44
      fit: 0.55
    Nimble Ring:
      total: 0.48
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.35
    Tekko-Kagi:
      total: 0.51
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.81
      win: 0.59
      pick: 0.31
      fit: 0.44
    Obsidian Shard:
      total: 0.52
      efficiency: 0.55
      win: 0.52
      pick: 0.28
      fit: 0.54
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Spear of Desolation
  - Transcendence
  - Rod of Tahuti
  - Obsidian Shard
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Sundering Echo,
    Titan''s Bane, Spear of the Magus, Death Metal, Gluttonous Grimoire, Doom Orb,
    Hydra''s Lament, Heartseeker, The Crusher, The Reaper, Dreamer''s Idol, Pendulum
    Blade, Tekko-Kagi, Arondight, The Cosmic Horror, Bragi''s Harp, Tyrfing, Heartwood
    Charm, Gem of Focus, Ancient Signet, Polynomicon, Blood-Bound Book, Avatar''s
    Parashu, Transcendence, Runeforged Hammer, Totem of Death, Triton''s Conch, Divine
    Ruin, Jade Scepter, Golden Blade, Avenging Blade, Silverbranch Bow, Eye of the
    Storm.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.48
      win: 0.52
      pick: 0.16
      fit: 0.31
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.69
    Spear of Desolation:
      total: 0.55
      efficiency: 0.56
      win: 0.5
      pick: 0.44
      fit: 0.69
    Transcendence:
      total: 0.45
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.31
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.81
      win: 0.59
      pick: 0.31
      fit: 0.56
    Obsidian Shard:
      total: 0.54
      efficiency: 0.55
      win: 0.52
      pick: 0.28
      fit: 0.66
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
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
    Underrated for this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Dreamer''s
    Idol, The Cosmic Horror, Heartwood Charm, Gem of Focus, Ancient Signet, Polynomicon,
    Totem of Death, Blood-Bound Book, Divine Ruin, Jade Scepter, Bancroft''s Talon,
    Helm of Radiance, Ethereal Staff, Staff of Myrddin, Typhon’s Heart, Rod of Asclepius,
    Bracer of The Abyss, Alchemist Coat, Genji''s Guard.'
  slot_scores:
    Spear of Desolation:
      total: 0.59
      efficiency: 0.56
      win: 0.5
      pick: 0.44
      fit: 1.0
    Doom Orb:
      total: 0.53
      efficiency: 0.51
      win: 0.52
      pick: 0.0
      fit: 0.79
    Spear of the Magus:
      total: 0.54
      efficiency: 0.54
      win: 0.52
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.81
      win: 0.59
      pick: 0.31
      fit: 0.79
    Obsidian Shard:
      total: 0.58
      efficiency: 0.55
      win: 0.52
      pick: 0.28
      fit: 0.89
    Soul Gem:
      total: 0.54
      efficiency: 0.5
      win: 0.46
      pick: 0.23
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
  - Rod of Tahuti
  - Obsidian Shard
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
    this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Nimble Ring, Dreamer''s
    Idol, The Cosmic Horror, Heartwood Charm, Gem of Focus, Bracer of The Abyss, Eros''
    Bow, Ancient Signet, Polynomicon, Blood-Bound Book, Totem of Death, Divine Ruin,
    Jade Scepter, Bancroft''s Talon, Helm of Radiance, Ethereal Staff, Staff of Myrddin,
    Typhon’s Heart, Rod of Asclepius.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.48
      win: 0.52
      pick: 0.16
      fit: 0.36
    Spear of Desolation:
      total: 0.57
      efficiency: 0.56
      win: 0.5
      pick: 0.44
      fit: 0.86
    Nimble Ring:
      total: 0.5
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.5
    The World Stone:
      total: 0.53
      efficiency: 0.5
      win: 0.52
      pick: 0.41
      fit: 0.68
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.81
      win: 0.59
      pick: 0.31
      fit: 0.68
    Obsidian Shard:
      total: 0.56
      efficiency: 0.55
      win: 0.52
      pick: 0.28
      fit: 0.78
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Nimble Ring
  - The World Stone
  - Rod of Tahuti
  - Soul Reaver
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Sundering
    Echo, Doom Orb, Death Metal, Spear of the Magus, Bragi''s Harp, Gluttonous Grimoire,
    Nimble Ring, Heartwood Charm, Ancient Signet, Polynomicon, Dreamer''s Idol, Gem
    of Focus, Bracer of The Abyss, The Cosmic Horror, Blood-Bound Book, Eros'' Bow,
    Bancroft''s Talon, Totem of Death, Triton''s Conch, Divine Ruin, Genji''s Guard,
    Jade Scepter.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.48
      win: 0.52
      pick: 0.16
      fit: 0.36
    Spear of Desolation:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.44
      fit: 0.57
    Nimble Ring:
      total: 0.48
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.34
    The World Stone:
      total: 0.51
      efficiency: 0.5
      win: 0.52
      pick: 0.41
      fit: 0.53
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.81
      win: 0.59
      pick: 0.31
      fit: 0.53
    Soul Reaver:
      total: 0.49
      efficiency: 0.39
      win: 0.58
      pick: 0.25
      fit: 0.56
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Soul Reaver
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Nimble Ring
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
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
    god: Spear of the Magus, Gluttonous Grimoire, Sundering Echo, Doom Orb, Dreamer''s
    Idol, Nimble Ring, Death Metal, Bragi''s Harp, The Cosmic Horror, Heartwood Charm,
    Gem of Focus, Bracer of The Abyss, Ancient Signet, Polynomicon, Blood-Bound Book,
    Totem of Death, Eros'' Bow, Genji''s Guard, Damaru, Divine Ruin, Jade Scepter,
    Bancroft''s Talon.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.48
      win: 0.52
      pick: 0.16
      fit: 0.2
    Spear of Desolation:
      total: 0.55
      efficiency: 0.56
      win: 0.5
      pick: 0.44
      fit: 0.71
    Nimble Ring:
      total: 0.47
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.29
    The World Stone:
      total: 0.51
      efficiency: 0.5
      win: 0.52
      pick: 0.41
      fit: 0.51
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.81
      win: 0.59
      pick: 0.31
      fit: 0.51
    Obsidian Shard:
      total: 0.53
      efficiency: 0.55
      win: 0.52
      pick: 0.28
      fit: 0.61
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
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
  - Spear of Desolation
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Amanita Charm, Shield of the Phoenix, Gluttonous Grimoire, Kinetic Cuirass,
    Ethereal Staff, Genji''s Guard, Phoenix Feather, Yogi''s Necklace, Blood-Bound
    Book, Freya''s Tears, Breastplate of Valor, Rod of Asclepius, Sphere of Negation,
    Chandra''s Grace, Helm of Radiance, Spear of the Magus, Helm of Darkness, Eros''
    Bow, Erosion, Oni Hunter''s Garb, Eye of Providence, Nimble Ring, Draconic Scale,
    Doom Orb, Jade Scepter, Midgardian Mail.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.57
    Spear of Desolation:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.44
      fit: 0.46
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.81
      win: 0.59
      pick: 0.31
      fit: 0.36
    Obsidian Shard:
      total: 0.51
      efficiency: 0.55
      win: 0.52
      pick: 0.28
      fit: 0.46
    Amanita Charm:
      total: 0.57
      efficiency: 0.62
      win: 0.52
      pick: 0.0
      fit: 0.77
    Soul Gem:
      total: 0.52
      efficiency: 0.5
      win: 0.46
      pick: 0.23
      fit: 0.86
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
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
  - Spear of the Magus
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
    The Cosmic Horror, Nimble Ring, Heartwood Charm, Gem of Focus, Bracer of The Abyss,
    Ancient Signet, Polynomicon, Blood-Bound Book, Eros'' Bow, Totem of Death, Divine
    Ruin, Jade Scepter, Bancroft''s Talon, Screeching Gargoyle, Helm of Radiance,
    Ethereal Staff, Genji''s Guard, Typhon’s Heart.'
  slot_scores:
    Nimble Ring:
      total: 0.48
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.37
    Spear of Desolation:
      total: 0.58
      efficiency: 0.56
      win: 0.5
      pick: 0.44
      fit: 0.9
    The World Stone:
      total: 0.55
      efficiency: 0.5
      win: 0.52
      pick: 0.41
      fit: 0.77
    Spear of the Magus:
      total: 0.54
      efficiency: 0.54
      win: 0.52
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.81
      win: 0.59
      pick: 0.31
      fit: 0.77
    Obsidian Shard:
      total: 0.57
      efficiency: 0.55
      win: 0.52
      pick: 0.28
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
  - Rod of Tahuti
  - Obsidian Shard
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
    this god: Nimble Ring, Gluttonous Grimoire, Sundering Echo, Bragi''s Harp, Spear
    of the Magus, Blood-Bound Book, Bracer of The Abyss, Doom Orb, Eros'' Bow, Death
    Metal, Dreamer''s Idol, Bancroft''s Talon, Ancient Signet, Heartwood Charm, Polynomicon,
    Gem of Focus, The Cosmic Horror, Typhon’s Heart, Totem of Death, Divine Ruin,
    Jade Scepter, Genji''s Guard.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.52
      efficiency: 0.61
      win: 0.52
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.44
      fit: 0.4
    Bragi's Harp:
      total: 0.47
      efficiency: 0.41
      win: 0.52
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.81
      win: 0.59
      pick: 0.31
      fit: 0.32
    Obsidian Shard:
      total: 0.5
      efficiency: 0.55
      win: 0.52
      pick: 0.28
      fit: 0.42
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Spear of Desolation
  - Heartwood Charm
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Heartwood Charm
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
    + fit + win/pick). Underrated for this god: Heartwood Charm, Gem of Focus, Spear
    of the Magus, Sundering Echo, Gluttonous Grimoire, Totem of Death, Doom Orb, Nimble
    Ring, Genji''s Guard, Damaru, Breastplate of Valor, Death Metal, Dreamer''s Idol,
    Chandra''s Grace, Bragi''s Harp, The Cosmic Horror, Bracer of The Abyss, Ancient
    Signet, Polynomicon, Blood-Bound Book, Staff of Myrddin, Eros'' Bow, Screeching
    Gargoyle, Eye of Erebus.'
  slot_scores:
    Chronos' Pendant:
      total: 0.51
      efficiency: 0.52
      win: 0.51
      pick: 0.24
      fit: 0.57
    Spear of Desolation:
      total: 0.56
      efficiency: 0.56
      win: 0.5
      pick: 0.44
      fit: 0.78
    Heartwood Charm:
      total: 0.49
      efficiency: 0.47
      win: 0.52
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.81
      win: 0.59
      pick: 0.31
      fit: 0.34
    Obsidian Shard:
      total: 0.51
      efficiency: 0.55
      win: 0.52
      pick: 0.28
      fit: 0.44
    Soul Gem:
      total: 0.52
      efficiency: 0.5
      win: 0.46
      pick: 0.23
      fit: 0.88
  community_ordered:
  - Chronos' Pendant
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Nimble Ring
  - Tekko-Kagi
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Tekko-Kagi
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Tekko-Kagi, Sundering Echo,
    Titan''s Bane, Tyrfing, Hydra''s Lament, Bragi''s Harp, Death Metal, Heartseeker,
    Spear of the Magus, The Crusher, Nimble Ring, Gluttonous Grimoire, Lernaean Bow,
    Silverbranch Bow, The Reaper, Doom Orb, Golden Blade, Arondight, Pendulum Blade,
    Dominance, Dreamer''s Idol, Toxic Blade, Bracer of The Abyss, Transcendence, The
    Cosmic Horror, Avatar''s Parashu, Heartwood Charm, Gem of Focus, Runeforged Hammer,
    Eros'' Bow, Ancient Signet, Riptalon, Polynomicon, Blood-Bound Book, Avenging
    Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.65
    Spear of Desolation:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.44
      fit: 0.55
    Nimble Ring:
      total: 0.48
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.35
    Tekko-Kagi:
      total: 0.51
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.81
      win: 0.59
      pick: 0.31
      fit: 0.44
    Obsidian Shard:
      total: 0.52
      efficiency: 0.55
      win: 0.52
      pick: 0.28
      fit: 0.54
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Combustion
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Sundering Echo
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Sundering Echo
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Sundering Echo,
    Tekko-Kagi, Titan''s Bane, Spear of the Magus, Death Metal, Gluttonous Grimoire,
    Hydra''s Lament, Bragi''s Harp, Doom Orb, Tyrfing, Heartseeker, Nimble Ring, The
    Crusher, Silverbranch Bow, The Reaper, Dreamer''s Idol, Lernaean Bow, Golden Blade,
    Arondight, Pendulum Blade, The Cosmic Horror, Heartwood Charm, Bracer of The Abyss,
    Gem of Focus, Toxic Blade, Ancient Signet, Dominance, Polynomicon, Blood-Bound
    Book, Eros'' Bow, Avatar''s Parashu, Transcendence, Riptalon, Runeforged Hammer.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.54
      efficiency: 0.56
      win: 0.5
      pick: 0.44
      fit: 0.63
    Sundering Echo:
      total: 0.51
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.55
    The World Stone:
      total: 0.51
      efficiency: 0.5
      win: 0.52
      pick: 0.41
      fit: 0.51
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.81
      win: 0.59
      pick: 0.31
      fit: 0.51
    Obsidian Shard:
      total: 0.53
      efficiency: 0.55
      win: 0.52
      pick: 0.28
      fit: 0.61
  community_ordered:
  - Spear of Desolation
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
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
    Underrated for this god: Spear of the Magus, Gluttonous Grimoire, Doom Orb, Nimble
    Ring, Dreamer''s Idol, The Cosmic Horror, Heartwood Charm, Gem of Focus, Bracer
    of The Abyss, Eros'' Bow, Ancient Signet, Polynomicon, Blood-Bound Book, Totem
    of Death, Divine Ruin, Jade Scepter, Bancroft''s Talon, Helm of Radiance, Ethereal
    Staff, Staff of Myrddin, Typhon’s Heart, Rod of Asclepius.'
  slot_scores:
    Spear of Desolation:
      total: 0.57
      efficiency: 0.56
      win: 0.5
      pick: 0.44
      fit: 0.86
    Doom Orb:
      total: 0.51
      efficiency: 0.51
      win: 0.52
      pick: 0.0
      fit: 0.68
    Spear of the Magus:
      total: 0.53
      efficiency: 0.54
      win: 0.52
      pick: 0.0
      fit: 0.68
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.81
      win: 0.59
      pick: 0.31
      fit: 0.68
    Obsidian Shard:
      total: 0.56
      efficiency: 0.55
      win: 0.52
      pick: 0.28
      fit: 0.78
    Soul Gem:
      total: 0.54
      efficiency: 0.5
      win: 0.46
      pick: 0.23
      fit: 0.96
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
  aspect: Aspect of Combustion
---
